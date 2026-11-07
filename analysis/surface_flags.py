"""Headline contrasts by collapse route (PhDPaper4C v1.1), 7 November 2026.

Collapse (fl) is either flag within the horizon: the node flag (share of nodes held
crosses the threshold) or the value flag (share of value held crosses it). The
saved runs record which flag ended the run (wf: 1 nodes, 2 value, 0 none). This
script splits the fresh-draw surface's collapse outcome into the two routes,
fn = 1 if the node flag ended the run, fw = 1 if the value flag did, refits the
pair-and-square surface per arm, and reports the pre-registered contrasts and the
largest pair terms for each route beside the combined endpoint.

  python surface_flags.py --run-dir <surface folder> [--kind intrusion] [--boot 200]

Analysis only; reads results.jsonl once; writes surface_flags.md and surface_flags.csv.
"""
import argparse
import csv
import json
import os
import sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import PhDPaper4C as P   # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--kind", default="intrusion")
    ap.add_argument("--boot", type=int, default=200)
    a = ap.parse_args()
    sub = os.path.join(a.run_dir, a.kind)
    d = json.load(open(os.path.join(sub, "design.json"), encoding="utf-8"))
    names, design, arms = d["variables"], d["design"], d["arms"]
    C = P.SURFACE["contrast"]
    # per configuration: fl, fn, fw from the saved runs
    out = {}
    for r in P.load_results(sub):
        acc = out.setdefault(r["name"], dict(fl=[], fn=[], fw=[]))
        for cell in r["cells"]:
            c = cell["c"]
            for f_, w_ in zip(c.get("fl", []), c.get("wf", [])):
                acc["fl"].append(float(f_)); acc["fn"].append(1.0 if w_ == 1 else 0.0); acc["fw"].append(1.0 if w_ == 2 else 0.0)
    L = [f"# Headline contrasts by collapse route ({P.CODE_VERSION})", "",
         f"Stratum {d.get('fix')}. {d['points']} configurations per arm. fl = either flag; fn = the node flag ended the run; fw = the value flag did. "
         f"Pair terms in points per full range; intervals from {a.boot} bootstrap resamples of the points, each a refit.", ""]
    rows = []
    for arm in ("own", "shared"):
        pts = [nm for nm in design if nm in out and arms[nm]["arm"] == arm and out[nm]["fl"]]
        U = np.array([[design[nm][v] for v in names] for nm in pts])
        L += [f"## Arm: {arm} ({len(pts)} points)", ""]
        for oc in ("fl", "fn", "fw"):
            y = np.array([np.mean(out[nm][oc]) for nm in pts])
            share = float(y.mean())
            if y.var() <= 0:
                L += [f"- {oc}: no variance (mean {share:.3f})", ""]; continue
            bc = P._bootstrap_contrast(U, y, names, C, a.boot, 20261107, log=lambda m: print(m, flush=True))
            b, feats, _r, _h = P.fit_surface(U, y, hold_mask=np.zeros(len(y), dtype=bool))
            terms = P._pair_terms_per_range(b, feats, U.std(0) + 1e-12, names)
            top = sorted([(pr, v) for pr, v in terms.items() if pr[0] < pr[1]], key=lambda t: -abs(t[1]))[:8]
            L += [f"### {oc}: mean {share:.3f}; pair surface R2 {bc['r2']:.2f} in sample, {bc['r2_holdout']:.2f} held out", "",
                  "| contrast | estimate | 2.5% | 97.5% |", "|---|---|---|---|"]
            for k in ("lead", "D_node", "D_within", "D_all"):
                L.append(f"| {k} | {100 * bc[k]:+.1f} | {100 * bc[k + '_lo']:+.1f} | {100 * bc[k + '_hi']:+.1f} |")
            L += ["", "Largest pair terms:", ""] + [f"- {pr[0]} x {pr[1]}: {100 * v:+.1f}" for pr, v in top] + [""]
            row = dict(arm=arm, outcome=oc, mean=share); row.update(bc); rows.append(row)
            print(f"{arm} {oc}: mean {share:.3f}; R2 {bc['r2_holdout']:.2f}; lead {100 * bc['lead']:+.1f}; D_node {100 * bc['D_node']:+.1f} "
                  f"[{100 * bc['D_node_lo']:+.1f}, {100 * bc['D_node_hi']:+.1f}]; D_within {100 * bc['D_within']:+.1f}", flush=True)
    with open(os.path.join(sub, "surface_flags.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    open(os.path.join(sub, "surface_flags.md"), "w", encoding="utf-8").write("\n".join(L))
    print(f"written {os.path.join(sub, 'surface_flags.md')}")


if __name__ == "__main__":
    main()
