"""Lever ratios from a Sobol stratum folder (PhDPaper4C v1.1), 5 November 2026.

Re-fits the pair-and-square response surface the Sobol mode fits (same estimator,
same standardisation, chunked so the design matrix is never held), and reads from
it what one lever is worth in terms of another: Paul's "this lever pulls that lever".

For an outcome y and dials u_i in [0, 1] (0 = bottom of the dial's ladder, 1 = top):
  marginal_i   = dy/du_i at the centre of the space (every other dial mid-range),
                 in outcome units per full range of the dial, with its sign
  per_step_i   = the same per one ladder step
  ratio_ij     = marginal_i / marginal_j: one full range of i is worth ratio_ij full
                 ranges of j (reported among the defender levers with the largest
                 marginals)
  slope_ij     = the pair coefficient: how much dy/du_i changes as u_j goes from
                 bottom to top, so a large slope_ij is a lever whose worth depends
                 on where another dial sits
Uncertainty: the fit is repeated on five disjoint fifths of the base-row FAMILIES
(v1.1: a Saltelli design's hybrids of base row i stay with base row i, so no fifth
holds near-duplicates of another) and the spread (standard deviation across
fifths) is reported beside each marginal. The held-out R2 is likewise by family,
and the additive surface (linear and square terms) is reported beside the pair
surface. With --boot B, the pre-registered contrast D of Paper 4D (the external
pair against the leading node-level pairs, and against the within-system pairs)
is given a percentile interval from B bootstrap resamples of the families, each
a refit (about a minute each on a full stratum; B = 40 is an evening).

  python lever_ratios.py --run-dir <sobol stratum folder> [--kind intrusion]
         [--outcomes sl,fl,pk,dl] [--top 12] [--objective steal] [--boot 40]

--objective steal restricts data loss (and any outcome) to configurations whose
payload exfiltrates, so data loss is read as a defender's map rather than an
attacker's choice. Writes lever_ratios_<outcome>.csv, lever_pairs_<outcome>.csv and
lever_ratios.md into the folder. Reads results.jsonl once (a few minutes for a full
stratum). Analysis only; nothing is run.
"""
import argparse
import csv
import json
import os
import sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import PhDPaper4C as P   # noqa: E402

OUTCOME_NAMES = dict(fl="collapse", pk="peak reach", ar="area (mean share compromised)", dl="data loss", sl="service loss", sv="share of horizon stood")


def load_points(sub: str, kind: str, objective: str = None):
    d = json.load(open(os.path.join(sub, "design.json"), encoding="utf-8"))
    names = d["variables"]
    fix = d.get("fix") or {}
    out = P._sa_outcomes(P.load_results(sub))
    pts = [(nm, d["design"][nm]) for nm in d["design"] if nm in out]
    if objective:
        allv = dict(P.sa_variables(kind, fix))
        var = [(n_, allv[n_]) for n_ in names]
        keep = []
        for nm, pt in pts:
            kn, _g = P._knobs_from_point(kind, pt, var, fix)
            if str(kn.objective) == objective:
                keep.append((nm, pt))
        pts = keep
    U = np.array([[pt[v] for v in names] for _nm, pt in pts])
    Y = {k: np.array([out[nm][k] for nm, _pt in pts]) for k in OUTCOME_NAMES}
    fam = np.array([P.sa_family(nm) for nm, _pt in pts])
    return names, fix, U, Y, fam


def surface_terms(names, U, y, fam=None, hold_mask=None):
    """Fit; return intercept, linear, square and pair coefficients in standardised units,
    plus the standardisation so marginals can be expressed per unit u. The hold-out is
    a fifth of the families (v1.1)."""
    b, feats, r2, r2h = P.fit_surface(U, y, groups=fam, hold_mask=hold_mask)
    k = len(names)
    mu, sd = U.mean(0), U.std(0) + 1e-12
    lin = np.zeros(k); sq = np.zeros(k); pair = np.zeros((k, k))
    for c, (kind, i, j, _l) in zip(b[1:], feats):
        if kind == "lin":
            lin[i] = c
        elif kind == "sq":
            sq[i] = c
        elif kind == "pair":
            pair[i, j] = pair[j, i] = c
    return dict(lin=lin, sq=sq, pair=pair, mu=mu, sd=sd, r2=r2, r2h=r2h)


def marginals(S, at=None):
    """dy/du_i at the point `at` (u units; default the centre 0.5), per full range."""
    k = len(S["lin"])
    u = np.full(k, 0.5) if at is None else at
    z = (u - S["mu"]) / S["sd"]
    # y = b0 + sum lin_i z_i + sum sq_i z_i^2 + sum_{i<j} pair_ij z_i z_j ; dz_i/du_i = 1/sd_i
    dz = S["lin"] + 2 * S["sq"] * z + S["pair"] @ z
    return dz / S["sd"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--kind", default="intrusion")
    ap.add_argument("--outcomes", default="sl,fl,pk,dl")
    ap.add_argument("--top", type=int, default=12)
    ap.add_argument("--objective", default=None, help="steal | destroy: keep only configurations with that payload objective")
    ap.add_argument("--boot", type=int, default=0, help="bootstrap resamples of the families for the contrast D (0 = off)")
    a = ap.parse_args()
    sub = os.path.join(a.run_dir, a.kind)
    names, fix, U, Y, fam = load_points(sub, a.kind, a.objective)
    n, k = U.shape
    ufam = np.unique(fam)
    reg = P.REGISTER
    who = {nm: (P.WHO[reg[nm][1]] if nm in reg else "setup") for nm in names}
    steps = {nm: (len(P.CONN_LADDER["chain"]) if nm == "conn" else len(reg[nm][3])) - 1 if nm in reg else 1 for nm in names}
    L = [f"# Lever ratios from {os.path.basename(a.run_dir)} ({a.kind}" + (f", objective {a.objective}" if a.objective else "") + ")", "",
         f"Stratum {fix}. {n:,} sampled configurations, {k} variables. Pair-and-square surface on standardised dial positions "
         "(same estimator as the Sobol report). A marginal is dy/du at the centre of the space in outcome units per full range of the dial "
         "(sign kept: negative lowers the outcome); 'per step' divides by the ladder's steps. The spread is the standard deviation of the "
         f"marginal across fits on five disjoint fifths of the {len(ufam)} base-row families (every point built on base row i stays with it). "
         "Ratios are among the defender levers with the largest marginals: "
         "one full range of the row lever is worth that many full ranges of the column lever. The pair table gives, for the same levers, "
         "how much a lever's marginal changes as another dial goes from bottom to top (its dependence on context).", ""]
    rng = np.random.default_rng(11)
    fold_of_family = dict(zip(ufam.tolist(), rng.integers(0, 5, len(ufam)).tolist()))
    fold = np.array([fold_of_family[x] for x in fam.tolist()])
    C = P.SURFACE["contrast"]
    fit_rows, con_rows = [], []
    for oc in [x.strip() for x in a.outcomes.split(",") if x.strip()]:
        y = Y[oc]
        ok = np.isfinite(y)
        if ok.sum() < 3 * k + 10 or y[ok].var() <= 0:
            L += [f"## {OUTCOME_NAMES.get(oc, oc)}: not fitted (too few points or no variance)", ""]
            continue
        S = surface_terms(names, U[ok], y[ok], fam[ok])
        m = marginals(S)
        reps = []
        for f in range(5):
            sel = ok & (fold == f)
            if sel.sum() > 3 * k + 10:
                reps.append(marginals(surface_terms(names, U[sel], y[sel])))
        spread = np.std(np.array(reps), axis=0) if len(reps) >= 3 else np.full(k, np.nan)
        # v1.1: pair against additive surface, held out by family, with the five family folds
        rep = P.surface_fit_report(U[ok], y[ok], fam[ok])
        rep.update(outcome=oc)
        fit_rows.append(rep)
        # v1.1: the pre-registered contrast on this (development) surface, in points per full range
        sd_ok = U[ok].std(0) + 1e-12
        b_full, feats_full, _r, _h = P.fit_surface(U[ok], y[ok], hold_mask=np.zeros(int(ok.sum()), dtype=bool))
        con = P._contrast(P._pair_terms_per_range(b_full, feats_full, sd_ok, names), C)
        if a.boot > 0:
            print(f"{oc}: bootstrapping D over {len(ufam)} families, {a.boot} refits", flush=True)
            con = P._bootstrap_contrast(U[ok], y[ok], names, C, a.boot, 20261105, groups=fam[ok], log=lambda msg: print(msg, flush=True))
        con["outcome"] = oc
        con_rows.append(con)
        order = np.argsort(-np.abs(m))
        rows = []
        for i in order:
            rows.append(dict(outcome=oc, variable=names[i], who=who[names[i]], marginal_per_range=float(m[i]),
                             spread_5fold=float(spread[i]), per_step=float(m[i] / max(steps[names[i]], 1)),
                             abs_rank=int(np.where(order == i)[0][0]) + 1))
        with open(os.path.join(a.run_dir, f"lever_ratios_{oc}.csv"), "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
        L += [f"## {OUTCOME_NAMES.get(oc, oc)} (variance {y[ok].var():.4f}; pair surface R2 {S['r2'] * 100:.0f}% in sample, "
              f"{rep['r2_pairs_family_holdout'] * 100:.0f}% on held-out families, five family folds {rep['r2_pairs_cv_mean'] * 100:.0f} +/- {rep['r2_pairs_cv_sd'] * 100:.0f}; "
              f"additive surface {rep['r2_additive_family_holdout'] * 100:.0f}% on held-out families, folds {rep['r2_additive_cv_mean'] * 100:.0f} +/- {rep['r2_additive_cv_sd'] * 100:.0f})", "",
              f"Contrast D (points per full range): |ext_total x ext_auth| = {100 * con['lead']:+.1f}; D_node = {100 * con['D_node']:+.1f}; "
              f"D_within = {100 * con['D_within']:+.1f}; D_all = {100 * con['D_all']:+.1f}"
              + (f"; family bootstrap ({con['boot']} refits) D_node [{100 * con['D_node_lo']:+.1f}, {100 * con['D_node_hi']:+.1f}], "
                 f"D_within [{100 * con['D_within_lo']:+.1f}, {100 * con['D_within_hi']:+.1f}], D_all [{100 * con['D_all_lo']:+.1f}, {100 * con['D_all_hi']:+.1f}]" if a.boot > 0 else ""), "",
              "| rank | variable | who | marginal per full range | spread (5 fifths) | per ladder step |", "|---|---|---|---|---|---|"]
        for r in rows[:max(a.top, 15)]:
            L.append(f"| {r['abs_rank']} | {r['variable']} | {r['who']} | {100 * r['marginal_per_range']:+.1f} | {100 * r['spread_5fold']:.1f} | {100 * r['per_step']:+.1f} |")
        L.append("")
        lev = [i for i in order if who[names[i]] == "defender lever"][:a.top]
        L += [f"### Exchange rates among the top {len(lev)} defender levers (row worth in column units, full range to full range)", "",
              "| lever | " + " | ".join(names[j] for j in lev) + " |", "|---|" + "---|" * len(lev)]
        for i in lev:
            cells = []
            for j in lev:
                cells.append("1" if i == j else (f"{m[i] / m[j]:+.2f}" if abs(m[j]) > 1e-9 else "-"))
            L.append(f"| {names[i]} | " + " | ".join(cells) + " |")
        L.append("")
        L += [f"### Context dependence: change in the row lever's marginal (per full range) as the column dial goes bottom to top", "",
              "| lever | " + " | ".join(names[j] for j in lev) + " |", "|---|" + "---|" * len(lev)]
        prow = []
        for i in lev:
            cells = []
            for j in lev:
                v = 0.0 if i == j else float(S["pair"][i, j] / (S["sd"][i] * S["sd"][j]))   # per unit u_i per unit u_j
                cells.append("-" if i == j else f"{100 * v:+.1f}")
                prow.append(dict(outcome=oc, lever=names[i], context=names[j], slope_per_range=v))
            L.append(f"| {names[i]} | " + " | ".join(cells) + " |")
        L.append("")
        with open(os.path.join(a.run_dir, f"lever_pairs_{oc}.csv"), "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(prow[0])); w.writeheader(); w.writerows(prow)
        print(f"{oc}: R2 {S['r2']:.3f}/{S['r2h']:.3f}; top marginals: " + ", ".join(f"{names[i]} {100 * m[i]:+.1f}" for i in order[:6]), flush=True)
    sfx = f"_{a.objective}" if a.objective else ""
    if fit_rows:
        with open(os.path.join(a.run_dir, f"surface_fit{sfx}.csv"), "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(fit_rows[0])); w.writeheader(); w.writerows(fit_rows)
    if con_rows:
        keys = sorted(set().union(*[set(r) for r in con_rows]), key=lambda x: (x != "outcome", x))
        with open(os.path.join(a.run_dir, f"surface_contrast{sfx}.csv"), "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=keys); w.writeheader(); w.writerows(con_rows)
    path = os.path.join(a.run_dir, "lever_ratios" + sfx + ".md")
    open(path, "w", encoding="utf-8").write("\n".join(L))
    print(f"written {path}")


if __name__ == "__main__":
    main()
