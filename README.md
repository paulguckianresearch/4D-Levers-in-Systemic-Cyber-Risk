# Levers in Systemic Cyber Risk: code deposit v1.1

Paul Guckian, Independent Researcher, London, United Kingdom. 7 November 2026.
Companion to the manuscript "Levers in Systemic Cyber Risk: Which Matter, and When".

This deposit holds every piece of code that produced the results reported in the manuscript, together
with the small output files those results were read from. The estate model is **not** changed here. It is
the model of the preceding paper in this programme as frozen for its second confirmatory study (file
`PhDPaper4C.py` v0.26/v0.27, model digest `d3f90805edfee3c7...`, frozen core `97dbae47...`), deposited at
doi:10.5281/zenodo.23669511 (code) and doi:10.5281/zenodo.23669054 (specifications, protocols and run
outputs). Everything in this deposit is analysis, instrumentation or a declared exploratory revision around
that model. Each run record carries the model digest it ran on; a result whose record shows another digest
is not one of ours.

## Contents

```
analysis/
  PhDPaper4C.py          v1.1: the full runner with the global sensitivity programme
                         (--mode morris / sobol / surface / setup / theory / ledger / selftest) and the
                         v0.28 to v1.1 analysis-only additions (see CHANGES.md)
  lever_ratios.py        marginals with spreads over base-row families, additive against pair surface,
                         the pre-registered contrast D with a family bootstrap (--boot)
  lever_check.py         the paired worked example of an exchange rate on fresh draws
  noise_ceiling.py       the ceiling on any single-run R2, from a folder with replicated configurations
  surface_flags.py       the headline contrasts by collapse route (node flag, value flag) on a saved surface folder
timing_and_diagnostics/
  engine_4c_v027.py      the model file as it stood at v0.27 (identical model digest; used by the code below)
  timing_engine.py       timing revision v0.2: attack_period and response_lag over the unchanged engine
  run_timing.py, check_timing.py, selection.json, PROTOCOL_timing_v0.2.txt, validation_timing.json, benchmark_timing.json
  diag_engine.py         DiagEngine: run_ticks, exact snapshot, state rows, burst, capacity, forced capture
  diag_common.py, check_diag.py, run_diag.py, check_diag.json, README_diag.txt
protocols/
  Mechanism_Validation_Protocol_v0.1.md     the three audits and their placeholders
  Validation_Runbook_v1.1.md                the commands, in order, that produced the validation results
outputs/                 the analysis outputs the manuscript quotes (see outputs/README.md for the list)
CHANGES.md               every analysis-only change from v0.28 to v1.1, with the reason for each
CITATION.cff, LICENSE (MIT), requirements.txt, MANIFEST_SHA256.txt, make_manifest.py
```

## Reproducing the results

All commands run from the folder holding the file named. Python 3.10+, numpy. Run folders are created
under `<out-root>/4C` (default `C:\cemt_runs\4C` on Windows; pass `--out-root` elsewhere). Simulation
runs are expensive (the two Sobol strata took about 22 and 26 hours on sixteen cores, the fresh-draw run
about five); every analysis step can instead be re-run on a saved folder with `--run-dir`, and the
outputs folder holds what those steps produced.

1. Self-tests: `python PhDPaper4C.py --mode selftest` (analysis) and `python check_diag.py`
   (timing_and_diagnostics). Both must pass before anything else is run; `run_diag.py` refuses to start
   unless `check_diag.json` matches the current file digests.
2. Unstratified Morris screen: `python PhDPaper4C.py --mode morris --workers 16`.
3. Strata: `... --mode morris --fix cred_total=K,c2_share=0.8 --draws 4,4` for K = 0, 1, 2, 4.
4. Sobol: `... --mode sobol --from-morris <stratum folder> --workers 16` (inherits the stratum).
   Re-analysis of a saved folder under v1.1: `... --mode sobol --run-dir <folder> --kinds intrusion`.
5. Lever ratios: `python lever_ratios.py --run-dir <sobol folder> [--boot 40]` and
   `... --outcomes dl --objective steal`.
6. Fresh-draw surface confirmation: `python PhDPaper4C.py --mode surface --workers 16 --from-sobol <zero folder>`
   (60,000 configurations x 2 arms, one run each; `--points`, `--boot` to change; re-analyse with `--run-dir`).
7. Worked example: `python lever_check.py --run-dir <zero folder> --base auto --workers 16`.
8. Noise ceiling: `python noise_ceiling.py --run-dir <zero folder>`.
9. Contrasts by route: `python surface_flags.py --run-dir <surface folder>` (reads the saved runs; about 40 minutes).
10. Theory checks: `python PhDPaper4C.py --mode theory --run-dir <folder>`.
11. Timing pilot and diagnostic audits: `python run_timing.py` and `python run_diag.py --out diag_v01 --workers 8`
    (timing_and_diagnostics), after their checks.

## Draw ranges (no two designs share a stream)

Development wirings 6801 onward and seeds 6901 onward for the screens and Sobol; the fresh-draw "own" arm
uses wiring 9,000,001+i and seed 9,100,001+i per configuration, the "shared" arm wiring 8,900,001 and seed
8,900,001; the worked example wirings 9,200,001.. and seeds 9,300,001..; the timing pilot wirings 84001..
and seeds 94001000... The manuscript's Reproducibility section lists the run folders.

## Provenance

Results produced by v1.0 (4 November 2026) and v1.1 (5 to 7 November) are reported as such in the
manuscript; v1.1 adds analyses and changes no reported v1.0 number. `CHANGES.md` records every change
between v0.28 and v1.1 with its reason. The manifest lists the SHA-256 of every file; `make_manifest.py`
regenerates it.

## Licence

MIT (see LICENSE). The model file `engine_4c_v027.py` is a verbatim copy of the file deposited at
doi:10.5281/zenodo.23669511 and carries that deposit's licence.
