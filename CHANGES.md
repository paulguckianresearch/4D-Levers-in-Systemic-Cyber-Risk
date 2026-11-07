# PhDPaper4C v0.28 (2 November 2026): analysis-only

Model digest unchanged: d3f90805edfee3c7 (the citable model of the second confirmatory study, v0.26/v0.27). Nothing between
MODEL BEGINS and MODEL ENDS was touched. Self-test passes.

Why: the first Morris dry run (`--mode morris --quick`, 2 Nov, 14:05) stopped at task 73 of 276 with
`cred_cluster: no service mdm in this estate`. The global designs sample every register entry over its
ladder; `cred_cluster` (added for the second confirmatory study at v0.25) is a placement policy for three named services and
its generator path raises when a jointly sampled setup has no endpoints (no device management), or when
the named populations do not intersect (levels 2 and 3).

1. `cred_cluster` is excluded from the global designs (`SA_EXCLUDED`), with its reason added to
   `FIXED_REASON`, so the ledger reports it as not varied and why. 90 variables remain (was 91).
2. `run_task` records a configuration the generator refuses as an invalid point (`invalid` = the reason,
   no cells) instead of raising, so one refused joint sample cannot end a long design run. Every
   analysis already treats a configuration with no runs as missing (NaN); `morris_analyse` drops the
   elementary effects that touch it, `sobol_analyse` drops the rows. `mode_morris` prints the invalid
   configurations and writes them to the run record.

Checked here: dry Morris (intrusion, 90 variables, 273 configurations) runs end to end with no invalid
points; `--mode selftest` passes.

# PhDPaper4C v0.29 (2 November 2026): analysis-only

Model digest unchanged: d3f90805edfee3c7. Reason: the first full Morris screen (intrusion, 90 variables,
1,820 configurations, 2 Nov 14:11) found collapse at 600 ticks to be a step over the full space (70% of
configurations collapse in every run, 22% in none, 8% between), set by credential exposure (g = 0: 5%;
g >= 0.1: 88 to 95%) and the route out (c2_share = 0: 11%; otherwise 76 to 100%). Every other dial's
elementary effect on collapse was zero or a single-run flip. The conditional screens inside the region
those switches leave open need the switches held.

1. `--fix name=value,...` (mode morris): the named knobs are held at the given values and leave the
   design, together with any knob they override (`cred_total` holds `g`). Recorded in design.json, the
   run record (`fixed`) and the report heading; the run directory name carries the stratum; a resumed
   directory refuses a different --fix.
2. `--draws W,D` (mode morris): W wirings from 6801 and D dynamics seeds from 6901 per configuration
   (default 2,2 as in the protocol). The first screen's four runs per configuration let the keep rule be
   passed by one run flipping once; sixteen resolve a probability to a sixteenth.

Checked here: dry stratum screen (cred_total=1, c2_share=0.8, draws 1,1) runs end to end, 88 variables,
exactly one placement in every configuration.

# PhDPaper4C v0.30 (2 November 2026): analysis-only

Model digest unchanged: d3f90805edfee3c7. `--fix` and `--draws` extended to `--mode sobol`. With
`--from-morris` pointing at a stratum folder and no `--fix` given, Sobol inherits that folder's fix
(read from design.json), so a stratum's Stage 2 cannot accidentally sample the held knobs. The fix is
recorded in the Sobol design.json, run record (`fixed`), report heading and folder name; a resumed
folder refuses a different fix. Checked here: dry Sobol on the cred_total=0 Morris folder, four named
knobs, both passes and the incidental rule run end to end with the fix inherited.

# PhDPaper4C v0.31 (4 November 2026): analysis-only

Model digest unchanged: d3f90805edfee3c7. The first full Sobol stratum (cred_total 0, 2 to 3 Nov)
wrote sobol.csv and incidental.csv and then stopped in the response-surface step: with 56 variables
and about 291,000 sampled points the pair surface is a 291,000 x 1,653 design matrix (3.9 GB), and
the point count then passed the three-way test, which would have needed 29,400 terms (68 GB). No
groups.csv, run_record.json, sobol_all.csv or P4C_sobol.md were written.

1. fit_surface accumulates the normal equations over chunks of 20,000 rows and never holds the design
   matrix; same estimator, coefficients identical to the direct solve (checked to machine precision),
   56 variables x 291,000 points in under a minute.
2. Three-way terms are fitted only up to 20 variables (SURFACE_TRIPLES_MAX_K); above that the pair
   surface stands and the report says so.
3. A surface that still cannot be fitted is reported and skipped for that outcome; the record and the
   report are always written.

To recover a stratum that stopped: python PhDPaper4C.py --mode sobol --run-dir <its folder> --kinds intrusion
re-reads results.jsonl (no tasks re-run) and writes the missing files.

# PhDPaper4C v0.32 (4 November 2026): analysis-only
Model digest unchanged. A Morris or Sobol folder resumed with --run-dir and no --fix inherits the fix
recorded in its design.json instead of refusing (the v0.31 guard required the fix to be repeated).

# PhDPaper4C v0.33 (4 November 2026): analysis-only
`--traj N` for mode morris: a reduced screen with fewer trajectories (default 20) for a quick look; the
folder name carries `_tN`. Used for the reduced implant screens of 4 November (8 trajectories, 2 x 2 draws).

# PhDPaper4C v1.0 (4 November 2026): the analysis freeze for the levers paper
Model digest d3f90805edfee3c7, unchanged since v0.26 (the citable model of the second confirmatory study). Adds AUDIT_NOTES, the
verdicts of the detection-dial audit (detect_latency and obs_interval inert by construction under the
stage rule; block_delay inert for the intrusion by design; blind_delay and manual_delay the dials that
carry detection and response speed), printed by `--mode ledger` beside the variable. No design, estimator
or output changed between v0.33 and v1.0. Every later change is a new version and a new Zenodo version.

# PhDPaper4C v1.1 (5 November 2026): surface validation for the levers paper (analysis-only)
Model digest unchanged: d3f90805edfee3c7 (selftest passed). Adds the three validation analyses that the manuscript's
"Validation of the Surface" section names as owed, so that no reported surface number rests on a hold-out
that saw near-duplicates of its training points.

1. Family hold-out. `sa_family(name)` recovers the base-row family of a Sobol design point from its name
   (A{i}, B{i}, v:{var}|{i}, p:{a}+{b}|{i}: every point built on base row i). `fit_surface` takes `groups`
   and holds out a fifth of the FAMILIES rather than of the rows; `--mode sobol` now uses it for the
   surface step and writes `surface_fit.csv` (pair and additive surfaces, in sample, family hold-out,
   five family folds). `lever_ratios.py` computes its five-fold spreads over family folds and reports both
   surfaces' held-out R2 in each outcome heading. The v1.0 random-fifth numbers are superseded.
2. Additivity. `fit_surface(pairs=False)` fits the linear-and-square surface; `surface_fit_report` sets it
   beside the pair surface under the same family hold-out and reports the interaction gain.
3. Fresh-draw confirmation: `--mode surface --from-sobol <stratum folder> [--points 60000] [--boot 500]`.
   A Latin-hypercube sample over the stratum's kept variables, run in two arms: "own" (configuration i on
   wiring 9,000,001+i and dynamics seed 9,100,001+i, ranges no mode has used, one run each) and "shared"
   (the same configurations on wiring 8,900,001, seed 8,900,001). On each arm: the pair surface, the
   pre-registered contrast D_node = |ext_total x ext_auth| - max(|iface_closed x x_rate|, |iface_closed x
   a_rate|) in points per full range, D_within against n_chan x chan_cov, n_chan x chan_span and
   coverage x def_cap, D_all against every other pair, each with a percentile interval over bootstrap
   resamples of the points (every replicate a refit). Writes surface_report.md, surface_contrast.csv,
   surface_terms_<arm>.csv. A folder holding only incidental.csv can be given with an explicit --fix.
   `lever_ratios.py --boot B` gives the same contrast on the development surface with a bootstrap over
   families.
4. Worked example: `lever_check.py --run-dir <stratum folder> [--base centre|auto]`. Two one-rung moves on
   the actual ladders (interface closure, and the rung on coverage the surface predicts nearest to it),
   run paired from one base configuration on fresh draws (wirings 9,200,001.., seeds 9,300,001..), with the
   observed changes and the difference between them beside the prediction.
5. `surface_lambda_scan`: hold-out R2 of the pair and additive surfaces over a ridge-penalty grid (1e-3 to 1e5) on
   one family split, reported in surface_fit.csv (best penalty and its R2, and the whole scan), so a poor hold-out can
   be told apart from over-fitting that regularisation would cure. Added after the four-placement re-analysis
   returned negative family hold-outs (5 Nov, 09:10).
6. A small correction in `fit_surface`: a training set smaller than the number of terms used to fall back to
   the full fit for the hold-out prediction, which made the hold-out R2 of a tiny design meaningless. No
   v1.0 result had fewer training rows than terms, so no reported number changes.
Checked here: dry and 400-point surface runs end to end; dry Sobol with the family hold-out; lever_check
dry on the dry Sobol folder; selftest passed; model digest unchanged.
