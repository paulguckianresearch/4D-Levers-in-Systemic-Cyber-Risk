# 4D-Levers-in-Systemic-Cyber-Risk

Code and analysis outputs for the manuscript "Levers in Systemic Cyber Risk: Which Matter, and When". The deposit holds everything that produced the paper's reported results, built over a frozen simulated hundred-node estate model whose code is deposited separately (doi:10.5281/zenodo.23669511, model digest d3f90805edfee3c7). Nothing here changes that model; every run record carries its digest.

**analysis/** contains the runner with the global sensitivity programme: a Morris screen over all 88 dials and two setup variables, with exposure strata; a two-pass Sobol decomposition with a pre-set incidental rule; a chunked pair-and-square response surface; and the surface's validation, added after review: hold-out by base-row family, an additive-against-pairwise comparison, a ridge-penalty scan, a fresh-draw surface mode in which each of 60,000 configurations receives its own estate and random stream, a noise-ceiling estimator, a paired worked example of an exchange rate, and a breakdown of the headline contrasts by collapse route.

**timing_and_diagnostics/** contains a declared exploratory timing revision over the unchanged engine (an attack-transition opportunity interval and a one-off mobilisation lag) and a mechanism-validation package: exact checkpoints and branches, disturbance and capacity interventions, forced Control Plane capture, and three audits, with self-tests that prove the checkpoint reproduces a fresh run tick for tick.

**protocols/** holds the mechanism-validation protocol and the validation runbook, the ordered commands that produced the validation results.

**outputs/** holds the run folders the manuscript cites, under their original names: the unstratified screen, the four exposure strata, the Sobol decompositions at zero and four placements with their lever-ratio, noise-ceiling, worked-example and theory-check outputs, the fresh-draw confirmation, the two reduced implant screens, the diagnostics run and the timing pilot. The per-run result files and the large design files are omitted; the seeded designs regenerate them exactly, and the raw results are archived separately.

CHANGES.md records every analysis-only change from v0.28 to v1.1 with its reason. A SHA-256 manifest covers every file. Licence MIT. Python 3.10 and numpy are the only requirements; the README gives the commands, in order, to reproduce each result or to re-run any analysis on the saved folders.
