# Fresh-draw surface confirmation (PhDPaper4C v1.1 (2026-11-05, surface validation for Paper 4D; model as v0.26/v0.27))

Stratum {'cred_total': 0, 'c2_share': 0.8}. 60000 Latin-hypercube configurations over 56 variables, two arms. Own: each configuration on its own, never-used wiring and dynamics seed (one run). Shared: the same configurations on one fresh wiring and seed (one run). Pair-and-square ridge surface on standardised dial positions, as the Sobol report. Pair terms are in points of outcome per full range of each dial (the units of the context tables). D_node = |ext_total x ext_auth| - max(|iface_closed x x_rate|, |iface_closed x a_rate|); D_within the same against n_chan x chan_cov, n_chan x chan_span and coverage x def_cap; D_all against every other pair. Intervals: 2.5 and 97.5 percentiles over 500 bootstrap resamples of the points, each a refit. Pre-registered reading (Paper 4D): D_node interval above zero on collapse means the external pair exceeds both leading node pairs on independent draws; an interval including zero means it ranks alongside them.

## Arm: own (60000 points)

### fl: pairs R2 0.41 in sample, 0.37 held out (5 folds 0.37 +/- 0.01); additive 0.29 held out

| contrast | estimate | 2.5% | 97.5% | share of replicates > 0 |
|---|---|---|---|---|
| lead | +44.5 | +40.9 | +47.4 | 1.000 |
| D_node | -3.2 | -8.0 | +0.3 | 0.036 |
| D_within | +12.1 | +7.4 | +16.6 | 1.000 |
| D_all | -3.2 | -8.0 | +0.3 | 0.036 |

Largest pair terms (per full range, points):

- a_rate x iface_closed: -47.7
- iface_closed x x_rate: -46.4
- ext_auth x ext_total: +44.5
- ext_auth x ext_bad: +38.6
- ext_bad x ext_total: +38.3
- atk_cap x iface_closed: -38.1
- chan_cov x n_chan: +32.4
- ext_share x iface_closed: -29.1

### pk: pairs R2 0.59 in sample, 0.56 held out (5 folds 0.56 +/- 0.01); additive 0.47 held out

| contrast | estimate | 2.5% | 97.5% | share of replicates > 0 |
|---|---|---|---|---|
| lead | +38.5 | +36.2 | +40.5 | 1.000 |
| D_node | +2.8 | -0.2 | +5.4 | 0.970 |
| D_within | +22.5 | +19.4 | +25.0 | 1.000 |
| D_all | -3.1 | -6.1 | -0.5 | 0.012 |

Largest pair terms (per full range, points):

- ext_auth x ext_bad: +41.6
- ext_auth x ext_total: +38.5
- ext_bad x ext_total: +37.4
- a_rate x iface_closed: -35.7
- iface_closed x x_rate: -34.5
- ext_share x server_share: -31.6
- ext_exploit x server_share: +25.5
- ext_share x iface_closed: -22.9

### sl: pairs R2 0.53 in sample, 0.49 held out (5 folds 0.50 +/- 0.01); additive 0.42 held out

| contrast | estimate | 2.5% | 97.5% | share of replicates > 0 |
|---|---|---|---|---|
| lead | +8.3 | +7.1 | +9.7 | 1.000 |
| D_node | -13.1 | -14.9 | -11.7 | 0.000 |
| D_within | -2.0 | -3.9 | +0.1 | 0.034 |
| D_all | -13.1 | -14.9 | -11.7 | 0.000 |

Largest pair terms (per full range, points):

- a_rate x iface_closed: -21.5
- iface_closed x x_rate: -21.2
- ext_share x server_share: -17.3
- ext_exploit x iface_closed: -14.0
- atk_cap x iface_closed: -14.0
- ext_exploit x server_share: +13.3
- coverage x def_cap: -10.3
- coverage x iface_closed: +10.3

### dl: pairs R2 0.45 in sample, 0.42 held out (5 folds 0.41 +/- 0.01); additive 0.31 held out

| contrast | estimate | 2.5% | 97.5% | share of replicates > 0 |
|---|---|---|---|---|
| lead | +0.8 | +0.0 | +2.1 | 1.000 |
| D_node | -6.1 | -7.8 | -4.8 | 0.000 |
| D_within | -0.9 | -2.7 | +0.4 | 0.070 |
| D_all | -40.4 | -42.0 | -38.5 | 0.000 |

Largest pair terms (per full range, points):

- exfil_p x objective: -41.1
- iface_closed x objective: +31.9
- node_reconf x objective: +23.8
- exfil_p x iface_closed: -17.6
- exfil_p x node_reconf: -16.6
- a_rate x objective: -15.4
- objective x x_rate: -15.4
- iface_closed x node_reconf: +10.2

## Arm: shared (60000 points)

### fl: pairs R2 0.42 in sample, 0.39 held out (5 folds 0.38 +/- 0.01); additive 0.30 held out

| contrast | estimate | 2.5% | 97.5% | share of replicates > 0 |
|---|---|---|---|---|
| lead | +24.2 | +21.1 | +27.1 | 1.000 |
| D_node | -24.5 | -29.2 | -21.0 | 0.000 |
| D_within | -9.0 | -13.3 | -4.7 | 0.000 |
| D_all | -24.5 | -29.2 | -21.0 | 0.000 |

Largest pair terms (per full range, points):

- a_rate x iface_closed: -48.7
- iface_closed x x_rate: -47.6
- atk_cap x iface_closed: -39.9
- chan_cov x n_chan: +33.2
- ext_auth x ext_bad: +31.9
- ext_bad x ext_total: +30.7
- ext_share x iface_closed: -29.9
- ext_exploit x iface_closed: -28.3

### pk: pairs R2 0.61 in sample, 0.58 held out (5 folds 0.59 +/- 0.01); additive 0.49 held out

| contrast | estimate | 2.5% | 97.5% | share of replicates > 0 |
|---|---|---|---|---|
| lead | +24.1 | +22.0 | +26.0 | 1.000 |
| D_node | -13.0 | -16.0 | -11.1 | 0.000 |
| D_within | +8.3 | +5.5 | +11.2 | 1.000 |
| D_all | -13.0 | -16.0 | -11.3 | 0.000 |

Largest pair terms (per full range, points):

- iface_closed x x_rate: -37.1
- a_rate x iface_closed: -36.7
- ext_auth x ext_bad: +35.7
- ext_share x server_share: -33.4
- ext_bad x ext_total: +33.4
- ext_exploit x server_share: +28.7
- ext_share x iface_closed: -25.4
- ext_total x n_ext: +24.4

### sl: pairs R2 0.55 in sample, 0.51 held out (5 folds 0.52 +/- 0.00); additive 0.44 held out

| contrast | estimate | 2.5% | 97.5% | share of replicates > 0 |
|---|---|---|---|---|
| lead | +4.9 | +3.6 | +6.2 | 1.000 |
| D_node | -17.2 | -18.9 | -15.6 | 0.000 |
| D_within | -5.2 | -6.9 | -3.3 | 0.000 |
| D_all | -17.2 | -18.9 | -15.6 | 0.000 |

Largest pair terms (per full range, points):

- iface_closed x x_rate: -22.1
- a_rate x iface_closed: -21.3
- ext_share x server_share: -17.7
- ext_exploit x iface_closed: -15.4
- atk_cap x iface_closed: -14.9
- ext_exploit x server_share: +13.4
- coverage x iface_closed: +11.9
- coverage x def_cap: -10.1

### dl: pairs R2 0.46 in sample, 0.43 held out (5 folds 0.42 +/- 0.00); additive 0.32 held out

| contrast | estimate | 2.5% | 97.5% | share of replicates > 0 |
|---|---|---|---|---|
| lead | +1.3 | +0.2 | +2.6 | 1.000 |
| D_node | -6.1 | -8.0 | -4.7 | 0.000 |
| D_within | -0.2 | -2.1 | +1.1 | 0.244 |
| D_all | -38.9 | -40.8 | -37.1 | 0.000 |

Largest pair terms (per full range, points):

- exfil_p x objective: -40.2
- iface_closed x objective: +34.9
- node_reconf x objective: +23.4
- exfil_p x iface_closed: -19.0
- objective x x_rate: -17.0
- exfil_p x node_reconf: -16.4
- a_rate x objective: -15.6
- iface_closed x node_reconf: +11.3
