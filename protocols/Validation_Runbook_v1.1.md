# Paper 4D: v1.1 validation runbook

5 November 2026. PhDPaper4C v1.1 (model digest d3f90805edfee3c7 unchanged; selftest passed). Deposit: Paper4D_Code_v1.1.zip. Unzip over the working copy in `C:\cemt_runs\4C` (or run from the deposit's `4C_analysis` folder with `--out-root C:\cemt_runs`). Runtimes are for the 16-core machine.

## 1. Four-placement stratum: finish the analysis under v1.1 (about 15 min, no runs)

```
python PhDPaper4C.py --mode sobol --run-dir C:\cemt_runs\4C\20261103_214527_p4c_sobol_c2_share0p8_cred_total4_v0_30 --kinds intrusion
```
Re-reads results.jsonl, writes sobol_all.csv, groups.csv, `surface_fit.csv` (new: pair and additive surfaces, family hold-out, five family folds), run_record.json and P4C_sobol.md. Then

```
python lever_ratios.py --run-dir <that folder>
python lever_ratios.py --run-dir <that folder> --outcomes dl --objective steal
```
Send: P4C_sobol.md, sobol.csv, incidental.csv, surface_fit.csv, lever_ratios.md, lever_ratios_steal.md, run_record.json.

## 2. Zero-placement stratum: re-fit under v1.1 (about 20 min, no runs)

```
python PhDPaper4C.py --mode sobol --run-dir C:\cemt_runs\4C\20261102_195522_p4c_sobol_c2_share0p8_cred_total0_v0_30 --kinds intrusion
python lever_ratios.py --run-dir <that folder> --boot 40
python lever_ratios.py --run-dir <that folder> --outcomes dl --objective steal
```
`--boot 40` adds the family-bootstrap interval on the contrast D to the development surface (about 40 refits, 10 to 15 min). Send: surface_fit.csv, surface_contrast.csv, lever_ratios.md, lever_ratios_steal.md. This replaces the random-fifth R2 values (86/87/90/93) in the paper with family-held-out ones.

## 3. Fresh-draw surface confirmation (about 5 h of runs plus 2 to 3 h of bootstrap; start it last thing)

```
python PhDPaper4C.py --mode surface --workers 16 --from-sobol C:\cemt_runs\4C\20261102_195522_p4c_sobol_c2_share0p8_cred_total0_v0_30
```
60,000 Latin-hypercube configurations over the 47 kept variables (pair-term standard error about 1.5 to 2 points per full range on collapse), two arms (own wiring and seed per configuration; one shared fresh wiring and seed), one run each. Resumable: if interrupted, rerun with `--run-dir <its folder>`. Prints the bootstrap time after the first replicate; `--boot 200` halves it if needed. Send: surface_report.md, surface_contrast.csv, surface_terms_own.csv, surface_terms_shared.csv, design.json. Pre-registered reading: the own-arm D_node interval on collapse above zero confirms the external pair ahead of both leading node pairs on independent estates; an interval including zero means it ranks alongside them.

## 4. Worked example (about 2 min)

```
python lever_check.py --run-dir C:\cemt_runs\4C\20261102_195522_p4c_sobol_c2_share0p8_cred_total0_v0_30 --base auto --workers 16
```
Two one-rung moves (interface closure, and the coverage rung the surface predicts nearest to it) from one base configuration, 40 fresh wirings x 4 seeds, paired. Send: lever_check.md, lever_check.json.

## 5. Theory checks on both folders (a few minutes each, no runs)

```
python PhDPaper4C.py --mode theory --run-dir <zero folder>
python PhDPaper4C.py --mode theory --run-dir <four folder>
```
Send the P4C_theory.md written in each.

Order: 1, 2, 4 (about 40 min together), then 3 overnight, then 5 while 3 runs (it only reads files).
