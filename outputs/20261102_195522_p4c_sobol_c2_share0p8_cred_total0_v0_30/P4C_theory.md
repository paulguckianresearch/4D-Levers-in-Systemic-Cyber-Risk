# Paper 4C theory checks on the draws used (PhDPaper4C v1.1 (2026-11-05, surface validation for Paper 4D; model as v0.26/v0.27))

1166816 runs under C:\cemt_runs\4C\20261102_195522_p4c_sobol_c2_share0p8_cred_total0_v0_30.

## 1. Percolation: furthest reach against the Connection giant component

For an attack that spreads only node to node, the share of the estate it can ever reach is bounded by the share of the estate in the largest Connection component of the wiring it ran on (site percolation on the realised graph). The check is the share of runs whose furthest reach exceeded that bound, which the law says should be none, and the mean gap below it.

- all runs: 1166816 runs; reach exceeded the component bound in 20.8% of runs; mean reach 40% against mean component 71%; mean degree 16.32.

## 2. Queueing: waiting time against team utilisation

A pool of responders serving a queue has a waiting time that stays near zero at low utilisation and rises steeply as utilisation approaches one (the Erlang C shape). The table bins the runs by utilisation.

| utilisation | runs | mean wait (ticks) | 90th percentile wait |
|---|---|---|---|
| 0.0 to 0.2 | 724499 | 2.21 | 4.91 |
| 0.2 to 0.4 | 131409 | 16.71 | 47.85 |
| 0.4 to 0.6 | 92825 | 36.07 | 112.29 |
| 0.6 to 0.8 | 93107 | 55.87 | 196.30 |
| 0.8 to 0.9 | 78319 | 76.43 | 185.44 |
| 0.9 to 1.0 | 46657 | 113.98 | 200.34 |

## 3. Independent hub capture: collapse against exposed placements (pooled)

One-placement collapse q = nan% over 0 runs. The law predicts 1 - (1 - q)^k.

| placements | runs | observed | law | difference |
|---|---|---|---|---|
