"""Noise ceiling for a single-run surface (PhDPaper4C v1.1), 7 November 2026.

The fresh-draw surface (--mode surface) fits one run per configuration, so part of
what it cannot explain is the run-to-run randomness of the model at a fixed
configuration, which no surface could explain. This script estimates that part
from a Sobol stratum folder, where every configuration has several runs (two
wirings x two seeds), and reports the ceiling: the largest out-of-sample R2 any
function of the dials could reach on single runs of that outcome.

For each sampled configuration with m runs, with mean ybar and unbiased within-
configuration variance s2: the variance of the true expected outcome across
configurations is  V_true = var(ybar) - mean(s2) / m, the single-run noise is
E_noise = mean(s2), and the ceiling is  V_true / (V_true + E_noise). The same
configurations with their m-run means have ceiling V_true / var(ybar).

  python noise_ceiling.py --run-dir <sobol stratum folder> [--kind intrusion] [--outcomes fl,pk,sl,dl]

Reads results.jsonl once (a few minutes). Writes noise_ceiling.csv and prints a table.
"""
import argparse
import csv
import os
import sys
from collections import defaultdict
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import PhDPaper4C as P   # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--kind", default="intrusion")
    ap.add_argument("--outcomes", default="fl,pk,sl,dl")
    a = ap.parse_args()
    sub = os.path.join(a.run_dir, a.kind)
    ocs = [x.strip() for x in a.outcomes.split(",") if x.strip()]
    runs = defaultdict(lambda: defaultdict(list))
    for r in P.load_results(sub):
        if not r.get("cells"):
            continue
        c = r["cells"][0]["c"]
        for oc in ocs:
            if oc in c:
                runs[r["name"]][oc].extend(float(v) for v in c[oc])
    rows = []
    print(f"{len(runs):,} configurations under {sub}")
    print(f"{'outcome':8}{'m':>4}{'var(mean)':>11}{'within':>9}{'V_true':>9}{'ceiling 1 run':>15}{'ceiling m runs':>16}")
    for oc in ocs:
        ms = [len(v[oc]) for v in runs.values() if oc in v]
        m = int(np.median(ms)) if ms else 0
        pts = [np.array(v[oc]) for v in runs.values() if oc in v and len(v[oc]) == m and np.all(np.isfinite(v[oc]))]
        if m < 2 or len(pts) < 10:
            print(f"{oc:8} not enough replicated configurations"); continue
        means = np.array([p.mean() for p in pts]); s2 = np.array([p.var(ddof=1) for p in pts])
        var_mean = means.var(); noise = s2.mean(); v_true = max(var_mean - noise / m, 0.0)
        c1 = v_true / (v_true + noise) if v_true + noise > 0 else float("nan")
        cm = v_true / var_mean if var_mean > 0 else float("nan")
        rows.append(dict(outcome=oc, configurations=len(pts), runs_per_configuration=m, var_of_means=var_mean, within_variance=noise,
                         var_true=v_true, ceiling_single_run=c1, ceiling_m_run_mean=cm))
        print(f"{oc:8}{m:4d}{var_mean:11.4f}{noise:9.4f}{v_true:9.4f}{c1:15.3f}{cm:16.3f}")
    if not rows:
        sys.exit("no outcome had replicated configurations (this folder has one run per configuration)")
    out = os.path.join(a.run_dir, "noise_ceiling.csv")
    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    print(f"written {out}\nReading: a single-run surface's held-out R2 divided by 'ceiling 1 run' is the share of the learnable variance it captures.")


if __name__ == "__main__":
    main()
