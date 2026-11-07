# Outputs quoted in the manuscript

Copy the following files from the run folders into the sub-folders named here, then run
`python make_manifest.py` from the deposit root and re-zip. The large `results.jsonl` files
(1.5 GB per Sobol stratum, about 100 MB for the fresh-draw run) are not included; they are
archived separately and can be supplied on request.

```
outputs/
  morris_unstratified/      20261102_141129: P4C_morris.md, morris.csv, run_record.json
  morris_strata/            20261102_142939, _150328, _153824, _161318: P4C_morris.md, morris.csv per stratum
  sobol_0/                  20261102_195522 (intrusion/): P4C_sobol.md, sobol.csv, incidental.csv, surface_fit.csv,
                            run_record.json, P4C_theory.md; (root): lever_ratios.md, lever_ratios_steal.md,
                            surface_fit.csv, surface_contrast.csv, noise_ceiling.csv; lever_check/lever_check.md,
                            lever_check.json, lever_check.csv
  sobol_4/                  20261103_214527 (intrusion/): P4C_sobol.md, sobol.csv, incidental.csv, surface_fit.csv,
                            run_record.json, P4C_theory.md; (root): lever_ratios.md, lever_ratios_steal.md,
                            surface_fit.csv, surface_contrast.csv
  surface_0/                20261106_132933 (intrusion/): surface_report.md, surface_contrast.csv,
                            surface_terms_own.csv, surface_terms_shared.csv, design.json, run_record.json
  implant_screen/           the reduced implant Morris screens at 0 and 4 placements: P4C_morris.md, morris.csv
  timing_pilot/             the timing pilot results folder (report and manifest)
  diagnostics/              diag_v01: diag_report.md, manifest.json (diag_results.jsonl.gz if under 50 MB)
```
