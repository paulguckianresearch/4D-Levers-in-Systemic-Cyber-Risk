"""Paired worked example of an exchange rate (PhDPaper4C v1.1), 5 November 2026.

Paper 4D, Validation of the Surface: two feasible moves on the actual ladders that
the response surface predicts to deliver the same reduction in collapse, one on
lever A (default interface closure) and one on lever B (default control coverage),
run paired from one base configuration on fresh draws, with the observed reductions
reported beside the prediction.

  python lever_check.py --run-dir <sobol stratum folder> [--kind intrusion]
         [--lever-a iface_closed --steps-a 1] [--lever-b coverage] [--outcome fl]
         [--base centre|auto] [--wirings 40 --seeds 4] [--workers 16] [--out <folder>]

Procedure
  1. The pair-and-square surface is fitted to every sampled point of the stratum
     (the same estimator as the Sobol report and lever_ratios.py).
  2. The base configuration is, by default (--base centre), the centre of the kept
     space: every kept variable at the middle rung of its ladder (u = (i + 0.5) /
     rungs), every other dial at the register's neutral value, the stratum's --fix
     applied. With --base auto it is instead the sampled configuration of the
     stratum whose mean outcome is nearest 0.5 (so that a move has room to show in
     either direction), each variable snapped to the centre of its rung.
  3. Move A: lever A moved steps-a rungs up its ladder from the base rung (down if
     the ladder has no room). The surface's predicted change in the outcome is
     y(A) - y(base).
  4. Move B: the number of rungs on lever B (either direction, within the ladder)
     whose predicted change is nearest to move A's. Both predictions are reported.
  5. Base, A and B are run on W fresh wirings x D fresh dynamics seeds from ranges no
     mode has used (wirings 9,200,001.., seeds 9,300,001..). Each (wiring, seed) draw
     gives a paired triple; the observed effect of each move is the mean paired
     difference from base, with a percentile bootstrap over wirings (2,000
     resamples), and the difference between the two moves' effects likewise.
Writes lever_check.md, lever_check.csv (per-draw outcomes) and lever_check.json.
"""
import argparse
import csv
import json
import os
import sys
import time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import PhDPaper4C as P   # noqa: E402
from lever_ratios import load_points, surface_terms, OUTCOME_NAMES   # noqa: E402

WIRING0, SEED0 = 9_200_001, 9_300_001


def rung_u(i, rungs):
    return (i + 0.5) / rungs


def predict(S, u):
    """Surface value at u (without intercept; differences only)."""
    z = (np.asarray(u) - S["mu"]) / S["sd"]
    return float(S["lin"] @ z + S["sq"] @ (z * z) + 0.5 * z @ S["pair"] @ z)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--kind", default="intrusion")
    ap.add_argument("--lever-a", default="iface_closed")
    ap.add_argument("--steps-a", type=int, default=1)
    ap.add_argument("--lever-b", default="coverage")
    ap.add_argument("--outcome", default="fl")
    ap.add_argument("--wirings", type=int, default=40)
    ap.add_argument("--seeds", type=int, default=4)
    ap.add_argument("--workers", type=int, default=None)
    ap.add_argument("--out", default=None, help="output folder (default <run-dir>/lever_check)")
    ap.add_argument("--base", default="centre", choices=["centre", "auto"], help="centre of the space, or the sampled point with outcome nearest 0.5")
    ap.add_argument("--dry", action="store_true", help="4 wirings x 1 seed")
    a = ap.parse_args()
    if a.dry:
        a.wirings, a.seeds = 4, 1
    workers = a.workers or P._default_workers()
    out_dir = a.out or os.path.join(a.run_dir, "lever_check")
    os.makedirs(out_dir, exist_ok=True)
    sub = os.path.join(a.run_dir, a.kind)
    names, fix, U, Y, fam = load_points(sub, a.kind)
    for lv in (a.lever_a, a.lever_b):
        if lv not in names:
            sys.exit(f"{lv} is not a kept variable of this stratum ({', '.join(names)})")
    y = Y[a.outcome]
    ok = np.isfinite(y)
    print(f"{P.CODE_VERSION}: fitting the surface on {int(ok.sum()):,} points, {len(names)} variables", flush=True)
    S = surface_terms(names, U[ok], y[ok], fam[ok])
    allv = dict(P.sa_variables(a.kind, fix))
    var = [(n_, allv[n_]) for n_ in names]
    rungs = {n_: len(allv[n_]) for n_ in names}
    if a.base == "auto":
        cand = np.where(ok & (np.abs(y - 0.5) <= 0.15))[0]
        if len(cand) == 0:
            cand = np.where(ok)[0]
            print("no sampled point has an outcome within 0.35..0.65; taking the nearest", flush=True)
        # among the candidates, the one whose surface prediction is nearest its observed value
        pred = np.array([predict(S, U[i]) for i in cand])
        pred = pred - pred.mean() + y[cand].mean()
        pick = cand[np.argmin(np.abs(y[cand] - 0.5) + np.abs(pred - y[cand]))]
        base_i = {n_: min(int(U[pick, i] * rungs[n_]), rungs[n_] - 1) for i, n_ in enumerate(names)}
        base_desc = f"the sampled configuration with observed {a.outcome} nearest 0.5 ({y[pick]:.2f}), each variable at the centre of its rung"
    else:
        base_i = {n_: rungs[n_] // 2 for n_ in names}
        base_desc = "every kept variable at the middle rung of its ladder"
    base_u = np.array([rung_u(base_i[n_], rungs[n_]) for n_ in names])
    ia, ib = names.index(a.lever_a), names.index(a.lever_b)
    # move A
    ra = rungs[a.lever_a]
    ja = base_i[a.lever_a] + a.steps_a
    if ja >= ra:
        ja = base_i[a.lever_a] - a.steps_a
    ua = base_u.copy(); ua[ia] = rung_u(ja, ra)
    pa = predict(S, ua) - predict(S, base_u)
    # move B: the rung whose predicted change is nearest to A's
    rb = rungs[a.lever_b]
    best = None
    for jb in range(rb):
        if jb == base_i[a.lever_b]:
            continue
        ub = base_u.copy(); ub[ib] = rung_u(jb, rb)
        pb = predict(S, ub) - predict(S, base_u)
        if best is None or abs(pb - pa) < abs(best[1] - pa):
            best = (jb, pb, ub)
    jb, pb, ub = best
    la, lb = allv[a.lever_a], allv[a.lever_b]
    moves = dict(base=base_u, A=ua, B=ub)
    print(f"base: {base_desc}. Move A: {a.lever_a} {la[base_i[a.lever_a]]} -> {la[ja]} "
          f"(predicted {100 * pa:+.1f} points of {OUTCOME_NAMES.get(a.outcome, a.outcome)}). "
          f"Move B: {a.lever_b} {lb[base_i[a.lever_b]]} -> {lb[jb]} (predicted {100 * pb:+.1f}).", flush=True)
    # runs on fresh draws
    seeds = [SEED0 + i for i in range(a.seeds)]
    tasks = []
    for label, u in moves.items():
        pt = dict(zip(names, u.tolist()))
        kn, gamma = P._knobs_from_point(a.kind, pt, var, fix)
        for w in range(a.wirings):
            d = P.dataclasses.asdict(P.dataclasses.replace(kn, wiring_seed=WIRING0 + w))
            tasks.append((label, d, gamma, "a", (8,), (8,), tuple(seeds), 1))
    done = {r["key"] for r in P.load_results(out_dir)}
    todo = [t for t in tasks if P.task_key(t) not in done]
    print(f"{len(todo)} of {len(tasks)} tasks to run ({a.wirings} wirings x {a.seeds} seeds x 3 configurations), workers={workers}", flush=True)
    t0 = time.time()
    if todo:
        P._run_named(out_dir, todo, workers, "lever_check")
    res = P.load_results(out_dir)
    # paired table: (label, wiring) -> list over seeds
    tab = {}
    for r in res:
        if not r["cells"]:
            continue
        tab[(r["name"], r["wiring"])] = list(r["cells"][0]["c"][a.outcome])
    rows = []
    for w in range(a.wirings):
        wi = WIRING0 + w
        for si, sd_ in enumerate(seeds):
            try:
                rows.append(dict(wiring=wi, seed=sd_, base=tab[("base", wi)][si], A=tab[("A", wi)][si], B=tab[("B", wi)][si]))
            except (KeyError, IndexError):
                pass
    with open(os.path.join(out_dir, "lever_check.csv"), "w", newline="", encoding="utf-8") as fh:
        wr = csv.DictWriter(fh, fieldnames=["wiring", "seed", "base", "A", "B"]); wr.writeheader(); wr.writerows(rows)
    base = np.array([r["base"] for r in rows]); A = np.array([r["A"] for r in rows]); B = np.array([r["B"] for r in rows])
    wir = np.array([r["wiring"] for r in rows])
    dA, dB = A - base, B - base
    rng = np.random.default_rng(20261105)
    uw = np.unique(wir)
    boots = {"A": [], "B": [], "A-B": []}
    for _ in range(2000):
        pick = rng.choice(uw, len(uw), replace=True)
        sel = np.concatenate([np.where(wir == x)[0] for x in pick])
        boots["A"].append(dA[sel].mean()); boots["B"].append(dB[sel].mean()); boots["A-B"].append((dA[sel] - dB[sel]).mean())
    def ci(v):
        return float(np.percentile(v, 2.5)), float(np.percentile(v, 97.5))
    summary = dict(code=P.CODE_VERSION, stratum=fix, kind=a.kind, outcome=a.outcome, base=base_desc, n_draws=len(rows), wirings=a.wirings, seeds=a.seeds,
                   base_rungs={n_: allv[n_][base_i[n_]] for n_ in names},
                   move_A=dict(lever=a.lever_a, from_=la[base_i[a.lever_a]], to=la[ja], predicted=pa, observed=float(dA.mean()), ci=ci(boots["A"])),
                   move_B=dict(lever=a.lever_b, from_=lb[base_i[a.lever_b]], to=lb[jb], predicted=pb, observed=float(dB.mean()), ci=ci(boots["B"])),
                   A_minus_B=dict(predicted=pa - pb, observed=float((dA - dB).mean()), ci=ci(boots["A-B"])),
                   base_mean=float(base.mean()), A_mean=float(A.mean()), B_mean=float(B.mean()),
                   share_draws_A_below_base=float((dA < 0).mean()), share_draws_B_below_base=float((dB < 0).mean()),
                   seconds=round(time.time() - t0, 1))
    json.dump(summary, open(os.path.join(out_dir, "lever_check.json"), "w", encoding="utf-8"), indent=1, default=float)
    oc = OUTCOME_NAMES.get(a.outcome, a.outcome)
    L = [f"# Worked example of an exchange rate ({P.CODE_VERSION})", "",
         f"Stratum {fix}, {a.kind}, outcome {oc}. Base configuration: {base_desc} "
         f"({', '.join(f'{n_} {allv[n_][base_i[n_]]}' for n_ in names)}); other dials neutral.", "",
         f"Surface prediction (pair-and-square surface over {int(ok.sum()):,} sampled points, R2 {100 * S['r2']:.0f}% in sample, "
         f"{100 * S['r2h']:.0f}% on held-out families). Move A: {a.lever_a} {la[base_i[a.lever_a]]} -> {la[ja]}, predicted {100 * pa:+.1f} points. "
         f"Move B, chosen as the rung on {a.lever_b} whose prediction is nearest: {lb[base_i[a.lever_b]]} -> {lb[jb]}, predicted {100 * pb:+.1f} points.", "",
         f"Observed on {len(rows)} fresh paired draws ({a.wirings} wirings {WIRING0}.., {a.seeds} seeds {SEED0}..; intervals: percentile bootstrap over wirings, 2,000 resamples):", "",
         "| move | predicted | observed mean change | 95% interval | share of draws below base |", "|---|---|---|---|---|",
         f"| A: {a.lever_a} {la[base_i[a.lever_a]]} -> {la[ja]} | {100 * pa:+.1f} | {100 * dA.mean():+.1f} | [{100 * ci(boots['A'])[0]:+.1f}, {100 * ci(boots['A'])[1]:+.1f}] | {(dA < 0).mean():.2f} |",
         f"| B: {a.lever_b} {lb[base_i[a.lever_b]]} -> {lb[jb]} | {100 * pb:+.1f} | {100 * dB.mean():+.1f} | [{100 * ci(boots['B'])[0]:+.1f}, {100 * ci(boots['B'])[1]:+.1f}] | {(dB < 0).mean():.2f} |",
         f"| A minus B | {100 * (pa - pb):+.1f} | {100 * (dA - dB).mean():+.1f} | [{100 * ci(boots['A-B'])[0]:+.1f}, {100 * ci(boots['A-B'])[1]:+.1f}] | |", "",
         f"Base {oc} on these draws: {base.mean():.3f}; after A {A.mean():.3f}; after B {B.mean():.3f}.", "",
         "Reading: the surface's exchange rate is confirmed at this point of the space if the two observed changes agree with each other "
         "(the A minus B interval includes zero) and each with its prediction (the prediction inside the move's interval). A marginal is a "
         "local slope; a one-rung move is a finite step, so a difference of a few points between prediction and observation is the "
         "curvature the surface does not carry, not a failure of the ranking.", ""]
    open(os.path.join(out_dir, "lever_check.md"), "w", encoding="utf-8").write("\n".join(L))
    print("\n".join(L[-10:-2]))
    print(f"written {os.path.join(out_dir, 'lever_check.md')} ({summary['seconds']} s)")


if __name__ == "__main__":
    main()
