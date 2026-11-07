"""Paper 4D mechanism-validation package v0.1: one command, three audits.

  python run_diag.py --out diag_v01 --workers 8            run everything
  python run_diag.py --benchmark                           time a few runs, print an estimate
  python run_diag.py --out diag_v01 --workers 8 --only A1  one audit

Audits (PROTOCOL_diag.md has the definitions and the placeholders to be fixed):
  A1  Sustained attack pressure.  Does the source keep issuing payloads and the
      attacker keep acting through the whole horizon, including after the
      operational collapse threshold is crossed? Per 100-tick window.
  A2  Authority lockout.  Which Control Plane captures the team can and cannot
      undo under the dials in force, and under two restoration settings; how
      each observed collapse divides into reachable and unreachable compromise;
      a forced single-capture test per plane.
  A3  Recovery under sustained pressure.  From a checkpoint of a contained
      estate, a burst of k footholds with the attack continuing, with and
      without a capacity change, against the undisturbed continuation of the
      same checkpoint. Return to the pre-disturbance band or not, and when.

Nothing here is confirmatory. Seeds are the pilot's development seeds. The
output folder gets diag_results.jsonl.gz (every run and branch, with its per-tick
state rows), diag_report.md (the tables), manifest.json (digests, settings,
measured runtime). Refuses to run unless check_diag.json exists and matches the
current file digests.
"""
import argparse
import concurrent.futures
import gzip
import json
import os
import pathlib
import statistics as st
import time
import numpy as np
import engine_4c_v027 as E
from diag_common import build, configurations, digest, first_crossing, ROOT, WIRING0, SEED0

VERSION = "4D diag 0.1"
HORIZON = 600
WINDOW = 100
DRAWS = [(0, 0), (0, 1), (1, 0), (1, 1)]            # (wiring index, seed index): development draws only
FORCE_T0 = 20          # forced single capture: tick of the checkpoint (before any natural capture in the chosen estates)
FORCE_CONFIGS = ("c0005", "c0303")
DIAL_SETS = {"default": {}, "rebuild5": {"master_rebuild": 5}, "rebuild5_view": {"master_rebuild": 5, "svc_view": 1}}
# A3 development placeholders (PROTOCOL_diag.md section 4): to be calibrated, then frozen
A3 = dict(T0=200, pre_window=50, band_floor=0.05, band_sd=2.0, residence=30, obs=400,
          bursts=[5, 10, 20, 40], capacity_factor=2.0, contained_max=0.5, configs=["c0005", "c0303", "c0275"])
ROW_COLS = None


def rows_pack(rows):
    cols = list(rows[0].keys()) if rows else []
    return dict(columns=cols, rows=[[r[c] for c in cols] for r in rows])


def windows(rows, W=WINDOW):
    """Per-window attacker and defender activity from cumulative counters."""
    out = []
    prev = dict(refs=0, n_esc=0, n_inf=0, n_rep=0, n_alarm=0, n_hunt=0)
    for a in range(0, len(rows), W):
        seg = rows[a:a + W]
        last = seg[-1]
        w = dict(t0=seg[0]["tick"], t1=last["tick"], n=len(seg))
        for k in prev:
            w["d_" + k] = int(last[k] - prev[k]); prev[k] = last[k]
        for k in ("footholds", "comp", "excl", "q_wait", "contact", "stolen", "planes_held", "isolated"):
            w["mean_" + k] = float(np.mean([r[k] for r in seg]))
        out.append(w)
    return out


# ---------------------------------------------------------------- A1 / A2 runs
def task_run(t):
    cfg, wi, si, dials, defence = t
    eng, kn, layout, built = build(cfg, 1, 0, wi, si, HORIZON, over=DIAL_SETS[dials], defence_on=defence)
    eng.run()
    rows = eng.rows
    x = first_crossing(rows)
    ev = eng._events
    names = {v: k for k, v in eng.net.index.items()}
    caps = [dict(node=e[1], name=names[e[1]], tick=e[2], how=e[3]) for e in ev if e[0] == "cap"]
    res = [dict(node=e[1], name=names[e[1]], tick=e[2], ok=e[3]) for e in ev if e[0] == "res"]
    retool = int(kn.retool)
    win = windows(rows)
    def expected_in(w):      # distinct re-tooling periods whose first tick falls in the window
        return len({t // retool for t in range(w["t0"], w["t1"] + 1)} - ({(w["t0"] - 1) // retool} if w["t0"] > 1 else set()))
    for w in win:
        w["expected_refs"] = expected_in(w)
    rec = dict(
        audit="A1A2", key=f"{cfg['id']}|{dials}|{int(defence)}|{WIRING0 + wi}|{SEED0 + si}",
        configuration=cfg["id"], role=cfg["role"], dials=dials, defence=int(defence),
        wiring=WIRING0 + wi, seed=SEED0 + si, retool=retool,
        collapse=int(x is not None), first_collapse_tick=x["tick"] if x else None,
        at_crossing=(dict(comp=x["comp"], excl=x["excl"], comp_reach=x["comp_reach"], comp_excl=x["comp_excl"],
                          planes_held=x["planes_held"], planes=x["planes"], sys_held=x["sys_held"]) if x else None),
        final=dict(comp=rows[-1]["comp"], excl=rows[-1]["excl"], comp_reach=rows[-1]["comp_reach"],
                   planes_held=rows[-1]["planes_held"], unavail=rows[-1]["unavail"]),
        min_comp_after_crossing=(min(r["comp"] for r in rows if r["tick"] >= x["tick"]) if x else None),
        planes_within_20=(max(r["planes_held"] for r in rows if x["tick"] <= r["tick"] <= x["tick"] + 20) if x else None),
        excl_within_20=(max(r["excl"] for r in rows if x["tick"] <= r["tick"] <= x["tick"] + 20) if x else None),
        max_excl=max(r["excl"] for r in rows),
        excl_ever_fell=bool(any(rows[i + 1]["excl"] < rows[i]["excl"] for i in range(len(rows) - 1))),
        captures=caps, restorations=res,
        n_restore_ok=sum(r["ok"] for r in res), n_restore_fail=sum(1 - r["ok"] for r in res),
        windows=win,
        pressure=dict(
            issue_persists=all(w["d_refs"] == w["expected_refs"] for w in win),
            activity_persists=all((w["d_n_esc"] + w["d_n_inf"]) > 0 for w in win[1:]),
            first_quiet_window=next((w["t0"] for w in win[1:] if (w["d_n_esc"] + w["d_n_inf"]) == 0), None),
            activity_after_collapse=(sum(w["d_n_esc"] + w["d_n_inf"] for w in win if x and w["t0"] > x["tick"]) if x else None),
        ),
        plane_table=eng.plane_table() if (wi, si) == (0, 0) and defence else None,
        hashes=None, rows=rows_pack(rows),
    )
    return rec


# ---------------------------------------------------------------- A2 forced capture
def task_force(t):
    cfg, dials = t
    eng, kn, layout, built = build(cfg, 1, 0, 0, 0, HORIZON, over=DIAL_SETS[dials])
    eng.run_ticks(1, FORCE_T0)
    base = eng.snapshot()
    names = {v: k for k, v in eng.net.index.items()}
    out = []
    for row in base.plane_table():
        m = row["node"]
        s = base.snapshot()
        s.force_capture(m)
        zone = int(s.cluster_of[m])
        s.run_ticks(FORCE_T0 + 1, FORCE_T0 + 300)
        res = [e for e in s._events if e[0] == "res" and e[1] == m]
        rows = s.rows[FORCE_T0:]
        # did the team start any fix job in the plane's own zone on a node the plane does not direct?
        en = s.rel_enabled[E.DIRECTING][m]
        zone_nodes = np.flatnonzero((s.cluster_of == zone) & s._ord) if zone >= 0 else np.array([], dtype=int)
        other = [int(j) for j in zone_nodes if not en[j]]
        out.append(dict(
            audit="A2force", configuration=cfg["id"], dials=dials, plane=row["name"], node=m, zoneless=row["zoneless"],
            reach_share=row["reach_share"], restorable_now=row["restorable_now"], needs=row["needs"],
            excl_at_capture=float(s.interventions[0]["excl_after"]),
            restore_attempts=len(res), restore_ok=sum(e[3] for e in res), first_restore_ok_tick=next((e[2] for e in res if e[3]), None),
            excl_min_after=min(r["excl"] for r in rows), excl_final=rows[-1]["excl"],
            plane_held_final=bool(s.state[m] == E.COMPROMISED),
            zone_other_nodes=len(other),
            team_isolations_in_zone_other=int(sum(1 for (t_, j) in s.isolation_log if t_ > FORCE_T0 and j in set(other))),
            team_isolations_total=int(sum(1 for (t_, j) in s.isolation_log if t_ > FORCE_T0)),
            team_acted_in_zone=(bool(any(j in set(other) for (t_, j) in s.isolation_log if t_ > FORCE_T0)) if other else None),
            planes_held_at_T0=int(base.rows[-1]["planes_held"]),
            comp_final=rows[-1]["comp"],
        ))
    return out


# ---------------------------------------------------------------- A3 recovery branches
def band_of(parent_rows):
    T0, W = A3["T0"], A3["pre_window"]
    pre = [r["comp"] for r in parent_rows if T0 - W < r["tick"] <= T0]
    mu = float(np.mean(pre)); sd = float(np.std(pre))
    half = max(A3["band_floor"], A3["band_sd"] * sd)
    return mu, sd, half


def recovery(rows, mu, half):
    """First tick after T0 from which comp stays inside [mu-half, mu+half] for
    `residence` consecutive ticks; None if never within `obs` ticks."""
    T0, R, obs = A3["T0"], A3["residence"], A3["obs"]
    seq = [r for r in rows if T0 < r["tick"] <= T0 + obs]
    inside = [abs(r["comp"] - mu) <= half for r in seq]
    run_ = 0
    for i, ok in enumerate(inside):
        run_ = run_ + 1 if ok else 0
        if run_ >= R:
            return seq[i - R + 1]["tick"]
    return None


def task_recovery(t):
    cfg, wi, si = t
    T0 = A3["T0"]
    eng, kn, layout, built = build(cfg, 1, 0, wi, si, HORIZON)
    eng.run_ticks(1, T0)
    ck = eng.snapshot()
    mu, sd, half = band_of(ck.rows)
    pre100 = [r["comp"] for r in ck.rows if T0 - 100 < r["tick"] <= T0]
    pre_outside = float(np.mean([abs(v - mu) > half for v in pre100]))
    pre_max_dev = float(max(abs(v - mu) for v in pre100))
    contained = ck.rows[-1]["comp"] <= A3["contained_max"]
    cap0 = int(ck.domains[0].tac_budget)
    plans = [("B0", 0, 1.0)] + [(f"B{k}", k, 1.0) for k in A3["bursts"]] + \
            [(f"B{k}c", k, A3["capacity_factor"]) for k in A3["bursts"]] + [("Bc", 0, A3["capacity_factor"])]
    out = []
    refs_T0 = ck.rows[-1]["refs"]; esc_T0 = ck.rows[-1]["n_esc"]; inf_T0 = ck.rows[-1]["n_inf"]
    for name, k, cf in plans:
        s = ck.snapshot()
        if cf != 1.0:
            s.set_capacity(int(round(cap0 * cf)))
        if k:
            s.disturb_burst(k, seed=SEED0 + si + 100 * k)
        s.run_ticks(T0 + 1, HORIZON)
        rows = s.rows
        after = [r for r in rows if r["tick"] > T0]
        peak = max(r["comp"] for r in after)
        t_ret = recovery(rows, mu, half)
        x = first_crossing(after)
        applied = next((i["applied"] for i in s.interventions if i["kind"] == "burst"), 0)
        out.append(dict(
            audit="A3", configuration=cfg["id"], role=cfg["role"], wiring=WIRING0 + wi, seed=SEED0 + si,
            branch=name, burst=k, burst_applied=applied, capacity_factor=cf, capacity=int(s.domains[0].tac_budget),
            contained_at_T0=bool(contained), comp_T0=ck.rows[-1]["comp"], planes_T0=ck.rows[-1]["planes_held"],
            band=dict(mu=mu, sd=sd, half=half, pre100_outside_share=pre_outside, pre100_max_dev=pre_max_dev),
            peak_after=peak, comp_final=rows[-1]["comp"], excl_final=rows[-1]["excl"],
            planes_final=rows[-1]["planes_held"], planes_new=int(rows[-1]["planes_held"] - ck.rows[-1]["planes_held"]),
            recovered=t_ret is not None, return_tick=t_ret, return_time=(t_ret - T0) if t_ret else None,
            crossed_after=int(x is not None), crossing_tick=x["tick"] if x else None,
            pressure=dict(refs_issued=int(rows[-1]["refs"] - refs_T0), expected=(HORIZON - T0) // int(kn.retool),
                          esc_attempts=int(rows[-1]["n_esc"] - esc_T0), infections=int(rows[-1]["n_inf"] - inf_T0)),
            interventions=s.interventions, rows=rows_pack(rows),
        ))
    return out


# ---------------------------------------------------------------- report
def pct(v):
    return f"{100 * v:.0f}%"


def report(out, recs, elapsed, manifest):
    L = []
    L.append(f"# Paper 4D mechanism-validation package v0.1: results\n")
    L.append(f"Run {manifest['started']} on {manifest['workers']} workers, {elapsed:.0f} s. Engine digest {manifest['hashes']['engine_4c_v027.py'][:16]} (v0.27), timing {manifest['hashes']['timing_engine.py'][:16]}, diag {manifest['hashes']['diag_engine.py'][:16]}. Development draws only (wirings {WIRING0}-{WIRING0 + 1}, seeds {SEED0}-{SEED0 + 1}); P=1, D=0 throughout. Not confirmatory.\n")
    A = [r for r in recs if r["audit"] == "A1A2"]
    F = [r for r in recs if r["audit"] == "A2force"]
    R = [r for r in recs if r["audit"] == "A3"]

    # ---- A1
    L.append("## A1 Sustained attack pressure\n")
    L.append("Per run: does the source issue the expected number of new payloads in every 100-tick window (mechanical, retool = 20), and does the attacker act (escalation attempts + infections > 0) in every window after the first? `quiet@` is the first window with no attacker action; `act>coll` is attacker actions after the first crossing of 0.8.\n")
    L.append("| cfg | dials | def | wiring | seed | coll | t_coll | issue persists | activity persists | quiet@ | act>coll | footholds by window | comp by window |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in sorted(A, key=lambda r: (r["configuration"], r["dials"], -r["defence"], r["wiring"], r["seed"])):
        p = r["pressure"]
        fh = " ".join(f"{w['mean_footholds']:.0f}" for w in r["windows"])
        cm = " ".join(f"{w['mean_comp']:.2f}" for w in r["windows"])
        L.append(f"| {r['configuration']} | {r['dials']} | {r['defence']} | {r['wiring']} | {r['seed']} | {r['collapse']} | {r['first_collapse_tick'] or ''} | {p['issue_persists']} | {p['activity_persists']} | {p['first_quiet_window'] or ''} | {p['activity_after_collapse'] if p['activity_after_collapse'] is not None else ''} | {fh} | {cm} |")
    n_issue = sum(r["pressure"]["issue_persists"] for r in A); n_act = sum(r["pressure"]["activity_persists"] for r in A)
    L.append(f"\nPayload issue persisted in {n_issue}/{len(A)} runs; attacker activity persisted in every window in {n_act}/{len(A)} runs. Runs where activity stopped are listed with their first quiet window; the footholds column shows whether the attacker had anything left to act from.\n")

    # ---- A2 static
    L.append("## A2 Authority lockout\n")
    L.append("### A2.1 Control Planes of each selected estate (wiring 84001), under the default dials\n")
    L.append("`reach` is the share of the 100 estate nodes the plane directs: the share the team is excluded from while the plane is held. `restorable now` requires master_rebuild < horizon (default 9999) and the plane inside the team's view (zone-less services need svc_view = 1; a third party's never are).\n")
    L.append("| cfg | plane | zone | reach | in view | visible | cred holders | restorable now | what it would need |")
    L.append("|---|---|---|---|---|---|---|---|---|")
    for r in sorted(A, key=lambda r: r["configuration"]):
        if r["plane_table"] and r["dials"] == "default":
            for p in r["plane_table"]:
                L.append(f"| {r['configuration']} | {p['name']} | {'none' if p['zoneless'] else p['zone']} | {pct(p['reach_share'])} | {p['in_team_view']} | {p['visible']} | {p['cred_holders']} | {p['restorable_now']} | {p['needs'].strip('; ') or 'nothing'} |")
    L.append("\n### A2.2 Captures, restorations and the composition of each collapse\n")
    L.append("`excl@x` is the excluded share of the estate at the first crossing of 0.8; `reach@x` / `unreach@x` split the compromised share at that tick into nodes the team could act on and nodes it could not. `min after` is the lowest compromised share after the crossing (the pilot's apparent recoveries). `excl fell` is whether the excluded share ever decreased in the run (it can only if a plane is restored).\n")
    L.append("| cfg | dials | wiring | seed | captures (method) | restore ok/fail | coll | t | excl@x | reach@x | unreach@x | planes@x | planes@x+20 | excl@x+20 | min after | excl final | excl fell |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in sorted(A, key=lambda r: (r["configuration"], r["dials"], r["wiring"], r["seed"])):
        if not r["defence"]:
            continue
        caps = ", ".join(f"{c['name']}@{c['tick']}({c['how'][:3]})" for c in r["captures"]) or "none"
        x = r["at_crossing"]
        mca = f"{r['min_comp_after_crossing']:.2f}" if x else ""
        L.append(f"| {r['configuration']} | {r['dials']} | {r['wiring']} | {r['seed']} | {caps} | {r['n_restore_ok']}/{r['n_restore_fail']} | {r['collapse']} | {r['first_collapse_tick'] or ''} | {pct(x['excl']) if x else ''} | {pct(x['comp_reach']) if x else ''} | {pct(x['comp_excl']) if x else ''} | {x['planes_held'] if x else ''} | {r['planes_within_20'] if x else ''} | {pct(r['excl_within_20']) if x else ''} | {mca} | {pct(r['final']['excl'])} | {r['excl_ever_fell']} |")
    coll = [r for r in A if r["defence"] and r["collapse"] and r["dials"] == "default"]
    if coll:
        prop = [r for r in coll if r["at_crossing"]["excl"] == 0]
        prop_stay = [r for r in prop if r["planes_within_20"] == 0]
        auth = [r for r in coll if r["at_crossing"]["comp_excl"] >= r["at_crossing"]["comp_reach"]]
        L.append(f"\nUnder the default dials, {len(coll)} collapses: {len(prop)} with no plane held at the crossing (propagation at the crossing), of which {len(prop_stay)} still had no plane 20 ticks later (propagation collapse proper) and {len(prop) - len(prop_stay)} took planes within 20 ticks (propagation leading authority); {len(auth)} where more than half the compromise at the crossing was unreachable (authority-dominant); {len(coll) - len(prop) - len(auth)} mixed. Restorations under default: {sum(r['n_restore_ok'] for r in coll)} (none are possible: master_rebuild = 9999).\n")
    for ds in ("rebuild5", "rebuild5_view"):
        sub = [r for r in A if r["defence"] and r["dials"] == ds]
        if sub:
            L.append(f"With `{ds}` ({DIAL_SETS[ds]}): {sum(r['n_restore_ok'] for r in sub)} restorations succeeded and {sum(r['n_restore_fail'] for r in sub)} failed across {len(sub)} runs; the excluded share fell at some point in {sum(r['excl_ever_fell'] for r in sub)} of them; collapses {sum(r['collapse'] for r in sub)}/{len(sub)}.\n")
    L.append("\n### A2.3 Forced single capture at tick 50 (c0275 and c0005 estates, wiring 84001, seed 94001000), 300 ticks on\n")
    L.append("Each plane is put in the attacker's hands alone, with the attack otherwise running as normal. `team acted in zone` is whether the team isolated any node of the plane's own zone that the plane does not direct, which tests whether an identity-plane capture locks the team out of the zone (the lockout_delay rule) or only out of the directed nodes.\n")
    L.append("| cfg | dials | plane | zone-less | reach | planes@T0 | excl at capture | restore attempts | ok | first ok tick | excl min after | excl final | still held | team acted in zone |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in sorted(F, key=lambda r: (r["configuration"], r["dials"], r["plane"])):
        L.append(f"| {r['configuration']} | {r['dials']} | {r['plane']} | {r['zoneless']} | {pct(r['reach_share'])} | {r['planes_held_at_T0']} | {pct(r['excl_at_capture'])} | {r['restore_attempts']} | {r['restore_ok']} | {r['first_restore_ok_tick'] or ''} | {pct(r['excl_min_after'])} | {pct(r['excl_final'])} | {r['plane_held_final']} | {r['team_acted_in_zone']} |")

    # ---- A3
    L.append("\n## A3 Recovery under sustained pressure\n")
    L.append(f"Checkpoint at T0 = {A3['T0']}. Operating band = mean compromised share over the {A3['pre_window']} ticks before T0 +/- max({A3['band_floor']}, {A3['band_sd']} sd). Recovered = inside the band for {A3['residence']} consecutive ticks within {A3['obs']} ticks of T0, with the attack continuing (payloads issued after T0 are reported). B0 is the undisturbed continuation of the same checkpoint; Bk a burst of k footholds; Bkc the same burst with the team's responders x {A3['capacity_factor']}; Bc the capacity change alone. All placeholders; see PROTOCOL_diag.md.\n")
    L.append("| cfg | wiring | seed | contained@T0 | comp@T0 | band mu +/- h | parent outside band (100 ticks before T0) | branch | burst applied | cap | peak after | recovered | return time | crossed 0.8 | planes new | comp final | refs issued |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in sorted(R, key=lambda r: (r["configuration"], r["wiring"], r["seed"], r["burst"], r["capacity_factor"])):
        b = r["band"]
        L.append(f"| {r['configuration']} | {r['wiring']} | {r['seed']} | {r['contained_at_T0']} | {r['comp_T0']:.2f} | {b['mu']:.2f} +/- {b['half']:.2f} | {pct(b['pre100_outside_share'])}, max dev {b['pre100_max_dev']:.2f} | {r['branch']} | {r['burst_applied']} | {r['capacity']} | {r['peak_after']:.2f} | {r['recovered']} | {r['return_time'] or ''} | {r['crossed_after']} | {r['planes_new']} | {r['comp_final']:.2f} | {r['pressure']['refs_issued']}/{r['pressure']['expected']} |")
    # summary per config and branch
    L.append("\n### A3 summary by configuration and branch (draws with a contained checkpoint only)\n")
    L.append("| cfg | branch | draws | recovered | median return time | crossed 0.8 | mean peak | mean planes new |")
    L.append("|---|---|---|---|---|---|---|---|")
    keys = sorted({(r["configuration"], r["branch"]) for r in R}, key=lambda k: (k[0], len(k[1]), k[1]))
    for c, b in keys:
        sub = [r for r in R if r["configuration"] == c and r["branch"] == b and r["contained_at_T0"]]
        if not sub:
            continue
        rt = [r["return_time"] for r in sub if r["return_time"] is not None]
        L.append(f"| {c} | {b} | {len(sub)} | {sum(r['recovered'] for r in sub)} | {st.median(rt) if rt else ''} | {sum(r['crossed_after'] for r in sub)} | {np.mean([r['peak_after'] for r in sub]):.2f} | {np.mean([r['planes_new'] for r in sub]):.2f} |")
    L.append("\n## What the first result answers\n")
    L.append("1. Whether recoverability under sustained pressure is measurable with this engine: A3 B0 against Bk, with the payload count after T0 showing the pressure did not stop.")
    L.append("2. Whether propagation collapse and authority lockout are distinguishable: A2.2 `reach@x` against `unreach@x`, and A2.3 for what each plane's capture does on its own.")
    L.append("3. Which captures prevent recovery under the dials in force: A2.1 `restorable now`, confirmed dynamically in A2.3 (`restore attempts`, `excl min after`).")
    (out / "diag_report.md").write_text("\n".join(L), encoding="utf-8")


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="diag_v01")
    ap.add_argument("--workers", type=int, default=min(8, os.cpu_count() or 1))
    ap.add_argument("--only", choices=["A1", "A2", "A3"], action="append")
    ap.add_argument("--benchmark", action="store_true")
    ap.add_argument("--report-only", action="store_true", help="rebuild diag_report.md from an existing --out folder")
    a = ap.parse_args()
    if a.report_only:
        out = pathlib.Path(a.out)
        manifest = json.loads((out / "manifest.json").read_text(encoding="utf-8"))
        recs = []
        with gzip.open(out / "diag_results.jsonl.gz", "rt", encoding="utf-8") as f:
            for line in f:
                x = json.loads(line); x.pop("rows", None); recs.append(x)
        report(out, recs, float(manifest.get("elapsed_s", 0)), manifest)
        print(f"report rebuilt from {len(recs)} records: {out / 'diag_report.md'}")
        return
    files = ["engine_4c_v027.py", "timing_engine.py", "diag_engine.py", "diag_common.py", "check_diag.py", "run_diag.py", "selection.json"]
    hashes = {n: digest(n) for n in files}
    ck = ROOT / "check_diag.json"
    if not ck.exists():
        raise SystemExit("check_diag.json missing: run python check_diag.py first")
    ckh = json.loads(ck.read_text())["hashes"]
    stale = [n for n in ckh if ckh[n] != hashes.get(n)]
    if stale:
        raise SystemExit(f"check_diag.json is stale for {stale}: run python check_diag.py again")
    cfgs = {c["id"]: c for c in configurations()}
    only = set(a.only or ["A1", "A2", "A3"])
    runs, forces, recs3 = [], [], []
    if only & {"A1", "A2"}:
        for c in cfgs.values():
            for wi, si in DRAWS:
                runs.append((c, wi, si, "default", True))
        for cid in ("c0005", "c0275"):
            for wi, si in DRAWS[:2]:
                runs.append((cfgs[cid], wi, si, "default", False))      # attacker opportunity with no reactive defence
    if "A2" in only:
        for ds in ("rebuild5", "rebuild5_view"):
            for c in cfgs.values():
                for wi, si in DRAWS:
                    runs.append((c, wi, si, ds, True))
        for cid in FORCE_CONFIGS:
            for ds in DIAL_SETS:
                forces.append((cfgs[cid], ds))
    if "A3" in only:
        for cid in A3["configs"]:
            for wi, si in DRAWS:
                recs3.append((cfgs[cid], wi, si))
    n_tasks = len(runs) + len(forces) + len(recs3)
    if a.benchmark:
        t = time.monotonic(); task_run(runs[0]); one = time.monotonic() - t
        t = time.monotonic(); task_recovery((cfgs["c0303"], 0, 0)); rec = time.monotonic() - t
        t = time.monotonic(); task_force((cfgs["c0275"], "default")); frc = time.monotonic() - t
        total = len(runs) * one + len(forces) * frc + len(recs3) * rec
        print(json.dumps(dict(one_run_s=round(one, 2), one_recovery_task_s=round(rec, 1), one_force_task_s=round(frc, 1),
                              tasks=dict(runs=len(runs), force=len(forces), recovery=len(recs3)),
                              serial_estimate_s=round(total), estimate_with_workers_s=round(total / max(1, a.workers)),
                              workers=a.workers), indent=2))
        return
    out = pathlib.Path(a.out); out.mkdir(parents=True, exist_ok=True)
    manifest = dict(version=VERSION, status="mechanism validation, exploratory, development draws",
                    started=time.strftime("%Y-%m-%dT%H:%M:%S"), workers=a.workers, horizon=HORIZON, window=WINDOW,
                    draws=[(WIRING0 + w, SEED0 + s) for w, s in DRAWS], dial_sets=DIAL_SETS, A3=A3,
                    tasks=dict(runs=len(runs), force=len(forces), recovery=len(recs3)), hashes=hashes, check=ckh)
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"{n_tasks} tasks ({len(runs)} runs, {len(forces)} forced-capture tasks, {len(recs3)} recovery tasks) on {a.workers} workers", flush=True)
    t0 = time.monotonic(); recs = []; done = 0
    with concurrent.futures.ProcessPoolExecutor(a.workers) as pool, gzip.open(out / "diag_results.jsonl.gz", "wt", encoding="utf-8") as f:
        futs = [pool.submit(task_run, t) for t in runs] + [pool.submit(task_force, t) for t in forces] + [pool.submit(task_recovery, t) for t in recs3]
        for fut in concurrent.futures.as_completed(futs):
            r = fut.result(); rs = r if isinstance(r, list) else [r]
            for x in rs:
                f.write(json.dumps(x, separators=(",", ":"), default=float) + "\n")
                x.pop("rows", None); recs.append(x)
            done += 1
            if done % 10 == 0 or done == n_tasks:
                print(f"{done}/{n_tasks} tasks | {time.monotonic() - t0:.0f}s", flush=True)
    elapsed = time.monotonic() - t0
    manifest["elapsed_s"] = round(elapsed, 1); manifest["records"] = len(recs)
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    report(out, recs, elapsed, manifest)
    print(f"done in {elapsed:.0f}s: {out / 'diag_report.md'}")


if __name__ == "__main__":
    main()
