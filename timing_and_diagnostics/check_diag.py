"""Self-checks for the 4D diagnostic package. Every check is exact (==), none is
statistical. Run before run_diag.py; run_diag.py refuses to start if this has
not passed on the same file digests.

 1 Loop fidelity      DiagEngine.run_ticks(1, H) gives the same outcome dict and
                      the same timing trace as TimingEngine.run() on the same
                      draws, for P=1/D=0 and for P=2/D=8, two configurations,
                      two seeds. (The loop body is a copy; this is what makes the
                      copy trustworthy.)
 2 Checkpoint exact   run to t, snapshot, continue both to H: identical outcome,
                      trace and rows. And a snapshot continued equals a fresh
                      uninterrupted run (no hidden state outside the object).
 3 Branch isolation   two snapshots from one checkpoint; disturb one; the other
                      still equals the parent's continuation. Two snapshots given
                      the same disturbance and seed are identical.
 4 Cadence survives   attack-hook ticks after a restored checkpoint still obey
                      (t-1) mod P == 0; reactive hooks still wait for mobilisation.
 5 Forced capture     force_capture(m) makes the excluded set exactly the plane's
                      DIRECTING reach (plus any already excluded).
 6 Disturbance scope  burst nodes are clean, ordinary, reachable estate nodes and
                      end at stage 1 with L = auth_conn.
"""
import json
import pathlib
import time
import numpy as np
import engine_4c_v027 as E
from timing_engine import TimingEngine
from diag_common import build, configurations, digest, ROOT

P = ROOT
H = 300


def ref_run(config, period, lag, wi, si, horizon):
    """The reference: timing_engine.TimingEngine exactly as run_timing builds it."""
    w, seed = 84001 + wi, 94001000 + si
    d = dict(E.POINTS["middle"])
    d.update({k: v for k, v in config.items() if k in ["cred_total", "ad_reach", "tac_budget", "coverage", "zone_conn"]})
    d.update(detect_latency=0, obs_interval=1, kind="intrusion", topology="chain", size=100, wiring_seed=w,
             horizon=horizon, flag=0.0, flag_value=0.0)
    kn = E.Knobs(**d); sp, layout, built = E.generate(kn, 0)
    net = E._core_build_network(sp, np.random.default_rng(w))
    eng = TimingEngine(sp, E.make_cfg(kn, 8, 8, seed), layout, net=E.net_for_seed(net, seed), opts=E.make_opts(kn),
                       attack_period=period, response_lag=lag)
    eng.start(None); eng.run()
    return eng


def same(a, b):
    return json.dumps(a, sort_keys=True, default=float) == json.dumps(b, sort_keys=True, default=float)


def main():
    t0 = time.monotonic()
    cfgs = configurations()
    passed = []
    # 1 loop fidelity
    n = 0
    for c in (cfgs[1], cfgs[4]):
        for (p, l) in ((1, 0), (2, 8)):
            for si in (0, 1):
                ref = ref_run(c, p, l, 0, si, H)
                eng, *_ = build(c, p, l, 0, si, H); eng.run()
                assert same(ref.outcome(), eng.outcome()), ("outcome", c["id"], p, l, si)
                assert ref.trace == eng.trace, ("trace", c["id"], p, l, si)
                assert len(eng.rows) == H
                n += 1
    passed.append(f"1 loop fidelity: {n} exact outcome and trace matches against TimingEngine.run()")
    # 2 checkpoint exact
    n = 0
    for c in (cfgs[1], cfgs[5]):
        for (p, l) in ((1, 0), (4, 24)):
            fresh, *_ = build(c, p, l, 0, 0, H); fresh.run()
            eng, *_ = build(c, p, l, 0, 0, H); eng.run_ticks(1, 120)
            snap = eng.snapshot()
            eng.run_ticks(121, H); snap.run_ticks(121, H)
            for a, b in ((eng, snap), (eng, fresh)):
                assert same(a.outcome(), b.outcome()), ("ckpt outcome", c["id"], p, l)
                assert a.trace == b.trace and a.rows == b.rows, ("ckpt rows", c["id"], p, l)
                assert a.hook_calls == b.hook_calls and a.response_calls == b.response_calls
            n += 1
    # 2b the same with the service view on and restoration on: the view map is keyed by object id
    over = dict(master_rebuild=5, svc_view=1)
    fresh, *_ = build(cfgs[4], 1, 0, 0, 0, H, over=over); fresh.run()
    eng, *_ = build(cfgs[4], 1, 0, 0, 0, H, over=over); eng.run_ticks(1, 40)
    snap = eng.snapshot(); eng.run_ticks(41, H); snap.run_ticks(41, H)
    assert snap._vm_of[id(snap.domains[0])] is not None and snap._vm_of[id(snap.domains[0])].sum() > snap.domains[0].mask.sum(), "service view lost on restore"
    assert same(snap.outcome(), fresh.outcome()) and snap.rows == fresh.rows == eng.rows, "svc_view round trip"
    assert any(e[0] == "res" for e in fresh._events), "no restoration occurred in the svc_view fixture (fixture too weak)"
    passed.append(f"2 checkpoint exact: {n} snapshot continuations identical to the parent and to a fresh run; also with svc_view=1 and master_rebuild=5 (view map re-keyed)")
    # 3 branch isolation
    c = cfgs[3]
    eng, *_ = build(c, 1, 0, 0, 0, H); eng.run_ticks(1, 100)
    a, b, d = eng.snapshot(), eng.snapshot(), eng.snapshot()
    a.disturb_burst(10, seed=1); d.disturb_burst(10, seed=1)
    eng.run_ticks(101, H); a.run_ticks(101, H); b.run_ticks(101, H); d.run_ticks(101, H)
    assert b.rows == eng.rows and same(b.outcome(), eng.outcome()), "undisturbed branch drifted from parent"
    assert a.rows == d.rows and a.interventions == d.interventions, "same disturbance, different result"
    assert a.rows != b.rows, "disturbance had no effect at all (suspicious)"
    passed.append("3 branch isolation: undisturbed branch equals parent; equal disturbances give equal branches")
    # 4 cadence survives a restore
    eng, *_ = build(cfgs[2], 4, 24, 0, 0, H); eng.run_ticks(1, 60)
    s = eng.snapshot(); s.run_ticks(61, H)
    for name, calls in s.hook_calls.items():
        assert all((t - 1) % 4 == 0 for t in calls), name
    if s.first_evidence is not None:
        assert all(t >= s.first_evidence + 24 for _, t in s.response_calls)
    passed.append("4 cadence survives: attack period and mobilisation gate hold after a restore")
    # 5 forced capture
    eng, *_ = build(cfgs[1], 1, 0, 0, 0, H); eng.run_ticks(1, 5)
    en = eng.rel_enabled[E.DIRECTING]
    for row in eng.plane_table():
        m = row["node"]
        s = eng.snapshot(); before = s._excl.copy(); s.force_capture(m)
        expect = before | en[m]
        assert np.array_equal(s._excl, expect), ("exclusion", row["name"])
        assert s.state[m] == E.COMPROMISED and m in {x for x in s._cp_set if s.state[x] == E.COMPROMISED}
    passed.append("5 forced capture: excluded set equals the plane's directing reach for every Control Plane")
    # 6 disturbance scope
    eng, *_ = build(cfgs[1], 1, 0, 1, 1, H); eng.run_ticks(1, 150)
    s = eng.snapshot(); pre_excl = s._excl.copy(); pre_state = s.state.copy()
    chosen = s.disturb_burst(15, seed=7)
    for j in chosen.tolist():
        assert pre_state[j] != E.COMPROMISED and not pre_excl[j] and s._ord[j] and not s.isolated[j]
        assert s.state[j] == E.COMPROMISED and s._L[j] == s.o.auth_conn and s._inf_ref[j] < 0
    assert s.interventions[-1]["applied"] == len(chosen)
    passed.append("6 disturbance scope: burst lands on clean, reachable, ordinary nodes at stage 1")
    report = dict(status="PASS", checks=passed, seconds=round(time.monotonic() - t0, 1),
                  hashes={n_: digest(n_) for n_ in ["engine_4c_v027.py", "timing_engine.py", "diag_engine.py", "diag_common.py", "check_diag.py"]})
    (P / "check_diag.json").write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
