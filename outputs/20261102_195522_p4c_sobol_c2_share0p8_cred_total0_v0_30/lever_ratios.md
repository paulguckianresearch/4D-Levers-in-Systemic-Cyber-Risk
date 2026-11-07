# Lever ratios from 20261102_195522_p4c_sobol_c2_share0p8_cred_total0_v0_30 (intrusion)

Stratum {'cred_total': 0, 'c2_share': 0.8}. 291,584 sampled configurations, 56 variables. Pair-and-square surface on standardised dial positions (same estimator as the Sobol report). A marginal is dy/du at the centre of the space in outcome units per full range of the dial (sign kept: negative lowers the outcome); 'per step' divides by the ladder's steps. The spread is the standard deviation of the marginal across fits on five disjoint fifths of the 256 base-row families (every point built on base row i stays with it). Ratios are among the defender levers with the largest marginals: one full range of the row lever is worth that many full ranges of the column lever. The pair table gives, for the same levers, how much a lever's marginal changes as another dial goes from bottom to top (its dependence on context).

## service loss (variance 0.0304; pair surface R2 90% in sample, -17% on held-out families, five family folds -8 +/- 25; additive surface 30% on held-out families, folds 14 +/- 25)

Contrast D (points per full range): |ext_total x ext_auth| = +11.3; D_node = -15.7; D_within = +4.6; D_all = -15.7; family bootstrap (40 refits) D_node [-23.6, -6.4], D_within [-1.7, +10.1], D_all [-24.0, -9.2]

| rank | variable | who | marginal per full range | spread (5 fifths) | per ladder step |
|---|---|---|---|---|---|
| 1 | iface_closed | defender lever | -22.3 | 5.2 | -4.5 |
| 2 | x_rate | defender lever | +13.2 | 5.9 | +2.6 |
| 3 | a_rate | defender lever | +12.3 | 3.4 | +2.5 |
| 4 | atk_cap | attacker | +9.5 | 2.5 | +1.9 |
| 5 | coverage | defender lever | -8.0 | 4.3 | -1.6 |
| 6 | ext_exploit | defender lever | +7.4 | 3.3 | +1.5 |
| 7 | def_cap | defender lever | -6.0 | 2.7 | -1.2 |
| 8 | ext_total | defender lever | -5.9 | 3.3 | -1.2 |
| 9 | blind_delay | defender lever | +5.0 | 2.4 | +1.0 |
| 10 | ext_auth | defender lever | -4.9 | 3.4 | -1.0 |
| 11 | server_share | given | +4.9 | 2.7 | +1.0 |
| 12 | tac_budget | defender lever | -4.2 | 1.2 | -0.8 |
| 13 | rebuild_time | defender lever | +4.1 | 1.7 | +0.8 |
| 14 | remote_share | defender lever | -3.9 | 2.6 | -0.8 |
| 15 | t_cut | defender lever | +3.9 | 0.9 | +0.8 |

### Exchange rates among the top 12 defender levers (row worth in column units, full range to full range)

| lever | iface_closed | x_rate | a_rate | coverage | ext_exploit | def_cap | ext_total | blind_delay | ext_auth | tac_budget | rebuild_time | remote_share |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| iface_closed | 1 | -1.70 | -1.82 | +2.80 | -3.01 | +3.71 | +3.80 | -4.48 | +4.58 | +5.32 | -5.49 | +5.69 |
| x_rate | -0.59 | 1 | +1.07 | -1.65 | +1.77 | -2.19 | -2.24 | +2.64 | -2.70 | -3.13 | +3.23 | -3.35 |
| a_rate | -0.55 | +0.93 | 1 | -1.54 | +1.65 | -2.04 | -2.08 | +2.46 | -2.52 | -2.92 | +3.01 | -3.12 |
| coverage | +0.36 | -0.61 | -0.65 | 1 | -1.07 | +1.32 | +1.35 | -1.60 | +1.63 | +1.90 | -1.96 | +2.03 |
| ext_exploit | -0.33 | +0.56 | +0.61 | -0.93 | 1 | -1.24 | -1.26 | +1.49 | -1.53 | -1.77 | +1.83 | -1.89 |
| def_cap | +0.27 | -0.46 | -0.49 | +0.76 | -0.81 | 1 | +1.02 | -1.21 | +1.23 | +1.43 | -1.48 | +1.53 |
| ext_total | +0.26 | -0.45 | -0.48 | +0.74 | -0.79 | +0.98 | 1 | -1.18 | +1.21 | +1.40 | -1.45 | +1.50 |
| blind_delay | -0.22 | +0.38 | +0.41 | -0.63 | +0.67 | -0.83 | -0.85 | 1 | -1.02 | -1.19 | +1.23 | -1.27 |
| ext_auth | +0.22 | -0.37 | -0.40 | +0.61 | -0.66 | +0.81 | +0.83 | -0.98 | 1 | +1.16 | -1.20 | +1.24 |
| tac_budget | +0.19 | -0.32 | -0.34 | +0.53 | -0.57 | +0.70 | +0.71 | -0.84 | +0.86 | 1 | -1.03 | +1.07 |
| rebuild_time | -0.18 | +0.31 | +0.33 | -0.51 | +0.55 | -0.68 | -0.69 | +0.82 | -0.84 | -0.97 | 1 | -1.04 |
| remote_share | +0.18 | -0.30 | -0.32 | +0.49 | -0.53 | +0.65 | +0.67 | -0.79 | +0.81 | +0.93 | -0.96 | 1 |

### Context dependence: change in the row lever's marginal (per full range) as the column dial goes bottom to top

| lever | iface_closed | x_rate | a_rate | coverage | ext_exploit | def_cap | ext_total | blind_delay | ext_auth | tac_budget | rebuild_time | remote_share |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| iface_closed | - | -26.9 | -24.1 | +2.7 | -10.1 | +9.6 | +12.1 | -5.6 | +13.7 | -5.5 | -13.8 | +4.3 |
| x_rate | -26.9 | - | +3.5 | -5.8 | +8.6 | +4.6 | -12.0 | +1.5 | -11.9 | -2.5 | -2.0 | -6.5 |
| a_rate | -24.1 | +3.5 | - | -5.9 | +7.3 | -1.5 | -3.7 | +0.7 | -2.8 | -6.6 | -3.7 | -6.2 |
| coverage | +2.7 | -5.8 | -5.9 | - | -2.9 | -6.7 | +6.1 | -0.6 | +5.1 | -4.3 | -1.2 | +3.8 |
| ext_exploit | -10.1 | +8.6 | +7.3 | -2.9 | - | -1.3 | -2.5 | -0.1 | -7.2 | -5.5 | -0.4 | -4.9 |
| def_cap | +9.6 | +4.6 | -1.5 | -6.7 | -1.3 | - | +4.1 | +2.5 | +4.9 | -6.2 | -3.0 | +3.3 |
| ext_total | +12.1 | -12.0 | -3.7 | +6.1 | -2.5 | +4.1 | - | -3.1 | -11.3 | -3.5 | +1.6 | -3.3 |
| blind_delay | -5.6 | +1.5 | +0.7 | -0.6 | -0.1 | +2.5 | -3.1 | - | -1.1 | +7.1 | -5.9 | +0.8 |
| ext_auth | +13.7 | -11.9 | -2.8 | +5.1 | -7.2 | +4.9 | -11.3 | -1.1 | - | +5.1 | -2.1 | +1.6 |
| tac_budget | -5.5 | -2.5 | -6.6 | -4.3 | -5.5 | -6.2 | -3.5 | +7.1 | +5.1 | - | +2.2 | -2.0 |
| rebuild_time | -13.8 | -2.0 | -3.7 | -1.2 | -0.4 | -3.0 | +1.6 | -5.9 | -2.1 | +2.2 | - | -0.4 |
| remote_share | +4.3 | -6.5 | -6.2 | +3.8 | -4.9 | +3.3 | -3.3 | +0.8 | +1.6 | -2.0 | -0.4 | - |

## collapse (variance 0.1641; pair surface R2 86% in sample, -51% on held-out families, five family folds -19 +/- 17; additive surface -7% on held-out families, folds -18 +/- 16)

Contrast D (points per full range): |ext_total x ext_auth| = +61.4; D_node = +11.8; D_within = +30.8; D_all = +11.8; family bootstrap (40 refits) D_node [-17.0, +17.9], D_within [+1.0, +42.7], D_all [-25.0, +14.6]

| rank | variable | who | marginal per full range | spread (5 fifths) | per ladder step |
|---|---|---|---|---|---|
| 1 | iface_closed | defender lever | -41.4 | 7.7 | -8.3 |
| 2 | n_chan | defender lever | +19.4 | 14.4 | +3.9 |
| 3 | ext_total | defender lever | +18.4 | 10.9 | +3.7 |
| 4 | chan_cov | defender lever | +17.6 | 5.6 | +3.5 |
| 5 | atk_cap | attacker | +16.1 | 8.8 | +3.2 |
| 6 | coverage | defender lever | -15.8 | 11.0 | -3.2 |
| 7 | server_share | given | +15.7 | 12.6 | +3.1 |
| 8 | ext_auth | defender lever | +15.1 | 7.9 | +3.0 |
| 9 | x_rate | defender lever | +13.3 | 12.2 | +2.7 |
| 10 | a_rate | defender lever | +13.2 | 12.6 | +2.6 |
| 11 | supplied_a | defender lever | -13.1 | 17.1 | -2.6 |
| 12 | chan_span | defender lever | +11.9 | 2.1 | +2.4 |
| 13 | ext_share | defender lever | +11.8 | 6.6 | +1.7 |
| 14 | cap_spread | attacker | -11.7 | 13.3 | -2.3 |
| 15 | cap_drift | attacker | +10.8 | 16.8 | +2.2 |

### Exchange rates among the top 12 defender levers (row worth in column units, full range to full range)

| lever | iface_closed | n_chan | ext_total | chan_cov | coverage | ext_auth | x_rate | a_rate | supplied_a | chan_span | ext_share | def_cap |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| iface_closed | 1 | -2.13 | -2.25 | -2.35 | +2.62 | -2.75 | -3.10 | -3.14 | +3.17 | -3.48 | -3.50 | +3.94 |
| n_chan | -0.47 | 1 | +1.06 | +1.10 | -1.23 | +1.29 | +1.46 | +1.48 | -1.49 | +1.63 | +1.64 | -1.85 |
| ext_total | -0.44 | +0.95 | 1 | +1.05 | -1.17 | +1.22 | +1.38 | +1.40 | -1.41 | +1.55 | +1.56 | -1.75 |
| chan_cov | -0.43 | +0.91 | +0.96 | 1 | -1.12 | +1.17 | +1.32 | +1.34 | -1.35 | +1.48 | +1.49 | -1.68 |
| coverage | +0.38 | -0.81 | -0.86 | -0.90 | 1 | -1.05 | -1.18 | -1.20 | +1.21 | -1.33 | -1.33 | +1.50 |
| ext_auth | -0.36 | +0.78 | +0.82 | +0.86 | -0.96 | 1 | +1.13 | +1.15 | -1.15 | +1.27 | +1.28 | -1.44 |
| x_rate | -0.32 | +0.69 | +0.72 | +0.76 | -0.85 | +0.89 | 1 | +1.01 | -1.02 | +1.12 | +1.13 | -1.27 |
| a_rate | -0.32 | +0.68 | +0.72 | +0.75 | -0.83 | +0.87 | +0.99 | 1 | -1.01 | +1.11 | +1.11 | -1.25 |
| supplied_a | +0.32 | -0.67 | -0.71 | -0.74 | +0.83 | -0.87 | -0.98 | -0.99 | 1 | -1.10 | -1.11 | +1.24 |
| chan_span | -0.29 | +0.61 | +0.65 | +0.68 | -0.75 | +0.79 | +0.89 | +0.90 | -0.91 | 1 | +1.01 | -1.13 |
| ext_share | -0.29 | +0.61 | +0.64 | +0.67 | -0.75 | +0.78 | +0.89 | +0.90 | -0.90 | +0.99 | 1 | -1.13 |
| def_cap | +0.25 | -0.54 | -0.57 | -0.60 | +0.67 | -0.70 | -0.79 | -0.80 | +0.80 | -0.88 | -0.89 | 1 |

### Context dependence: change in the row lever's marginal (per full range) as the column dial goes bottom to top

| lever | iface_closed | n_chan | ext_total | chan_cov | coverage | ext_auth | x_rate | a_rate | supplied_a | chan_span | ext_share | def_cap |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| iface_closed | - | -13.1 | +25.2 | -2.7 | +24.5 | -6.1 | -49.6 | -47.8 | +17.4 | -16.8 | -12.0 | +8.4 |
| n_chan | -13.1 | - | -5.8 | +26.5 | -7.1 | -4.4 | -0.7 | +3.6 | -8.1 | +27.6 | -13.1 | -4.5 |
| ext_total | +25.2 | -5.8 | - | +5.0 | +7.3 | +61.4 | +0.4 | +1.1 | +2.0 | -4.9 | +8.4 | +0.9 |
| chan_cov | -2.7 | +26.5 | +5.0 | - | -0.8 | +7.7 | -11.9 | +1.0 | +0.2 | +24.1 | -11.8 | -2.1 |
| coverage | +24.5 | -7.1 | +7.3 | -0.8 | - | +5.2 | -4.4 | -13.1 | +0.8 | +10.9 | +8.1 | -30.6 |
| ext_auth | -6.1 | -4.4 | +61.4 | +7.7 | +5.2 | - | +9.0 | +1.8 | +2.5 | +10.2 | +14.1 | -17.4 |
| x_rate | -49.6 | -0.7 | +0.4 | -11.9 | -4.4 | +9.0 | - | -11.2 | +8.5 | -1.6 | +9.4 | -3.3 |
| a_rate | -47.8 | +3.6 | +1.1 | +1.0 | -13.1 | +1.8 | -11.2 | - | +2.9 | -6.7 | +6.4 | -5.0 |
| supplied_a | +17.4 | -8.1 | +2.0 | +0.2 | +0.8 | +2.5 | +8.5 | +2.9 | - | +11.1 | +2.4 | +0.4 |
| chan_span | -16.8 | +27.6 | -4.9 | +24.1 | +10.9 | +10.2 | -1.6 | -6.7 | +11.1 | - | -2.6 | -8.0 |
| ext_share | -12.0 | -13.1 | +8.4 | -11.8 | +8.1 | +14.1 | +9.4 | +6.4 | +2.4 | -2.6 | - | -6.1 |
| def_cap | +8.4 | -4.5 | +0.9 | -2.1 | -30.6 | -17.4 | -3.3 | -5.0 | +0.4 | -8.0 | -6.1 | - |

## peak reach (variance 0.1018; pair surface R2 93% in sample, 17% on held-out families, five family folds 22 +/- 13; additive surface 18% on held-out families, folds 4 +/- 15)

Contrast D (points per full range): |ext_total x ext_auth| = +50.7; D_node = +2.1; D_within = +32.5; D_all = +2.1; family bootstrap (40 refits) D_node [-12.6, +19.7], D_within [+22.9, +44.6], D_all [-14.9, +19.5]

| rank | variable | who | marginal per full range | spread (5 fifths) | per ladder step |
|---|---|---|---|---|---|
| 1 | iface_closed | defender lever | -38.4 | 6.3 | -7.7 |
| 2 | x_rate | defender lever | +19.7 | 6.3 | +3.9 |
| 3 | ext_auth | defender lever | +19.5 | 10.1 | +3.9 |
| 4 | ext_total | defender lever | +19.0 | 3.8 | +3.8 |
| 5 | a_rate | defender lever | +18.5 | 3.6 | +3.7 |
| 6 | ext_bad | given | +16.5 | 7.5 | +3.3 |
| 7 | atk_cap | attacker | +13.6 | 3.8 | +2.7 |
| 8 | cap_drift | attacker | +12.8 | 8.1 | +2.6 |
| 9 | ext_share | defender lever | +12.2 | 5.6 | +1.7 |
| 10 | server_share | given | +12.1 | 4.3 | +2.4 |
| 11 | n_chan | defender lever | +12.0 | 7.6 | +2.4 |
| 12 | cap_spread | attacker | -11.2 | 4.0 | -2.2 |
| 13 | coverage | defender lever | -10.4 | 6.7 | -2.1 |
| 14 | ext_exploit | defender lever | +10.1 | 2.6 | +2.0 |
| 15 | chan_cov | defender lever | +10.0 | 2.1 | +2.0 |

### Exchange rates among the top 12 defender levers (row worth in column units, full range to full range)

| lever | iface_closed | x_rate | ext_auth | ext_total | a_rate | ext_share | n_chan | coverage | ext_exploit | chan_cov | inequality | def_cap |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| iface_closed | 1 | -1.95 | -1.97 | -2.02 | -2.08 | -3.14 | -3.19 | +3.68 | -3.80 | -3.84 | +5.38 | +5.66 |
| x_rate | -0.51 | 1 | +1.01 | +1.04 | +1.07 | +1.62 | +1.64 | -1.89 | +1.96 | +1.97 | -2.77 | -2.91 |
| ext_auth | -0.51 | +0.99 | 1 | +1.02 | +1.05 | +1.59 | +1.62 | -1.87 | +1.93 | +1.94 | -2.73 | -2.87 |
| ext_total | -0.49 | +0.96 | +0.98 | 1 | +1.03 | +1.56 | +1.58 | -1.82 | +1.88 | +1.90 | -2.66 | -2.80 |
| a_rate | -0.48 | +0.94 | +0.95 | +0.97 | 1 | +1.51 | +1.54 | -1.78 | +1.83 | +1.85 | -2.59 | -2.73 |
| ext_share | -0.32 | +0.62 | +0.63 | +0.64 | +0.66 | 1 | +1.02 | -1.17 | +1.21 | +1.22 | -1.71 | -1.80 |
| n_chan | -0.31 | +0.61 | +0.62 | +0.63 | +0.65 | +0.98 | 1 | -1.15 | +1.19 | +1.20 | -1.69 | -1.77 |
| coverage | +0.27 | -0.53 | -0.54 | -0.55 | -0.56 | -0.85 | -0.87 | 1 | -1.03 | -1.04 | +1.46 | +1.54 |
| ext_exploit | -0.26 | +0.51 | +0.52 | +0.53 | +0.55 | +0.83 | +0.84 | -0.97 | 1 | +1.01 | -1.42 | -1.49 |
| chan_cov | -0.26 | +0.51 | +0.51 | +0.53 | +0.54 | +0.82 | +0.83 | -0.96 | +0.99 | 1 | -1.40 | -1.48 |
| inequality | +0.19 | -0.36 | -0.37 | -0.38 | -0.39 | -0.58 | -0.59 | +0.68 | -0.71 | -0.71 | 1 | +1.05 |
| def_cap | +0.18 | -0.34 | -0.35 | -0.36 | -0.37 | -0.56 | -0.56 | +0.65 | -0.67 | -0.68 | +0.95 | 1 |

### Context dependence: change in the row lever's marginal (per full range) as the column dial goes bottom to top

| lever | iface_closed | x_rate | ext_auth | ext_total | a_rate | ext_share | n_chan | coverage | ext_exploit | chan_cov | inequality | def_cap |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| iface_closed | - | -48.6 | +18.6 | +31.4 | -31.4 | -16.5 | -5.9 | +2.5 | -17.0 | -0.0 | -10.7 | +12.3 |
| x_rate | -48.6 | - | -11.5 | -16.0 | +6.8 | +3.1 | -9.1 | -6.2 | +9.4 | -13.1 | -7.0 | +6.5 |
| ext_auth | +18.6 | -11.5 | - | +50.7 | -11.4 | -1.5 | -1.6 | +4.8 | -8.7 | +2.6 | -4.7 | -6.0 |
| ext_total | +31.4 | -16.0 | +50.7 | - | -5.5 | +0.8 | -0.6 | +5.3 | -6.0 | +4.5 | +2.1 | +1.6 |
| a_rate | -31.4 | +6.8 | -11.4 | -5.5 | - | +11.3 | -4.4 | -5.1 | +2.3 | -4.0 | +2.5 | +1.1 |
| ext_share | -16.5 | +3.1 | -1.5 | +0.8 | +11.3 | - | -7.8 | -1.6 | -9.7 | -2.5 | +6.4 | -2.3 |
| n_chan | -5.9 | -9.1 | -1.6 | -0.6 | -4.4 | -7.8 | - | -4.9 | +6.4 | +18.2 | -11.7 | -4.7 |
| coverage | +2.5 | -6.2 | +4.8 | +5.3 | -5.1 | -1.6 | -4.9 | - | +6.2 | -1.9 | +2.9 | -12.6 |
| ext_exploit | -17.0 | +9.4 | -8.7 | -6.0 | +2.3 | -9.7 | +6.4 | +6.2 | - | +5.1 | -3.0 | -5.5 |
| chan_cov | -0.0 | -13.1 | +2.6 | +4.5 | -4.0 | -2.5 | +18.2 | -1.9 | +5.1 | - | -0.9 | -1.5 |
| inequality | -10.7 | -7.0 | -4.7 | +2.1 | +2.5 | +6.4 | -11.7 | +2.9 | -3.0 | -0.9 | - | -13.2 |
| def_cap | +12.3 | +6.5 | -6.0 | +1.6 | +1.1 | -2.3 | -4.7 | -12.6 | -5.5 | -1.5 | -13.2 | - |

## data loss (variance 0.0256; pair surface R2 87% in sample, -36% on held-out families, five family folds -69 +/- 95; additive surface -21% on held-out families, folds -50 +/- 62)

Contrast D (points per full range): |ext_total x ext_auth| = +1.3; D_node = -5.1; D_within = +0.1; D_all = -46.4; family bootstrap (40 refits) D_node [-11.7, +2.3], D_within [-3.4, +5.2], D_all [-54.1, -33.4]

| rank | variable | who | marginal per full range | spread (5 fifths) | per ladder step |
|---|---|---|---|---|---|
| 1 | objective | attacker | -22.8 | 5.3 | -22.8 |
| 2 | exfil_p | defender lever | +17.1 | 6.7 | +3.4 |
| 3 | iface_closed | defender lever | -9.2 | 7.6 | -1.8 |
| 4 | node_reconf | attacker | -7.2 | 1.8 | -1.4 |
| 5 | x_rate | defender lever | +4.3 | 0.8 | +0.9 |
| 6 | cap_drift | attacker | +3.9 | 4.8 | +0.8 |
| 7 | dval_sv | given | -3.9 | 3.8 | -0.8 |
| 8 | a_rate | defender lever | +3.8 | 3.3 | +0.8 |
| 9 | stage_time | defender lever | +3.7 | 2.7 | +0.7 |
| 10 | ext_exploit | defender lever | +3.4 | 4.0 | +0.7 |
| 11 | server_share | given | +3.0 | 2.5 | +0.6 |
| 12 | ext_bad | given | +2.3 | 2.7 | +0.5 |
| 13 | remote_share | defender lever | -2.1 | 2.5 | -0.4 |
| 14 | inequality | defender lever | -2.0 | 5.6 | -0.4 |
| 15 | seg_ep | defender lever | -2.0 | 2.2 | -0.7 |

### Exchange rates among the top 12 defender levers (row worth in column units, full range to full range)

| lever | exfil_p | iface_closed | x_rate | a_rate | stage_time | ext_exploit | remote_share | inequality | seg_ep | n_ext | def_cap | ext_share |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| exfil_p | 1 | -1.86 | +3.96 | +4.55 | +4.65 | +5.02 | -7.96 | -8.42 | -8.51 | +9.13 | +10.04 | +10.87 |
| iface_closed | -0.54 | 1 | -2.13 | -2.45 | -2.51 | -2.70 | +4.28 | +4.53 | +4.58 | -4.91 | -5.40 | -5.85 |
| x_rate | +0.25 | -0.47 | 1 | +1.15 | +1.17 | +1.27 | -2.01 | -2.12 | -2.15 | +2.30 | +2.53 | +2.74 |
| a_rate | +0.22 | -0.41 | +0.87 | 1 | +1.02 | +1.10 | -1.75 | -1.85 | -1.87 | +2.01 | +2.21 | +2.39 |
| stage_time | +0.21 | -0.40 | +0.85 | +0.98 | 1 | +1.08 | -1.71 | -1.81 | -1.83 | +1.96 | +2.16 | +2.33 |
| ext_exploit | +0.20 | -0.37 | +0.79 | +0.91 | +0.93 | 1 | -1.59 | -1.68 | -1.70 | +1.82 | +2.00 | +2.17 |
| remote_share | -0.13 | +0.23 | -0.50 | -0.57 | -0.58 | -0.63 | 1 | +1.06 | +1.07 | -1.15 | -1.26 | -1.37 |
| inequality | -0.12 | +0.22 | -0.47 | -0.54 | -0.55 | -0.60 | +0.95 | 1 | +1.01 | -1.08 | -1.19 | -1.29 |
| seg_ep | -0.12 | +0.22 | -0.47 | -0.53 | -0.55 | -0.59 | +0.94 | +0.99 | 1 | -1.07 | -1.18 | -1.28 |
| n_ext | +0.11 | -0.20 | +0.43 | +0.50 | +0.51 | +0.55 | -0.87 | -0.92 | -0.93 | 1 | +1.10 | +1.19 |
| def_cap | +0.10 | -0.19 | +0.39 | +0.45 | +0.46 | +0.50 | -0.79 | -0.84 | -0.85 | +0.91 | 1 | +1.08 |
| ext_share | +0.09 | -0.17 | +0.36 | +0.42 | +0.43 | +0.46 | -0.73 | -0.77 | -0.78 | +0.84 | +0.92 | 1 |

### Context dependence: change in the row lever's marginal (per full range) as the column dial goes bottom to top

| lever | exfil_p | iface_closed | x_rate | a_rate | stage_time | ext_exploit | remote_share | inequality | seg_ep | n_ext | def_cap | ext_share |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| exfil_p | - | -22.8 | +3.0 | +5.1 | +2.0 | +4.3 | -8.1 | -15.6 | -5.2 | +3.5 | -6.9 | +3.4 |
| iface_closed | -22.8 | - | -6.4 | -1.9 | +1.5 | -1.0 | +1.5 | -1.8 | +2.5 | +1.6 | +1.6 | -4.2 |
| x_rate | +3.0 | -6.4 | - | +7.2 | -5.3 | -2.4 | -0.6 | +2.7 | -0.8 | +0.2 | +2.3 | -2.0 |
| a_rate | +5.1 | -1.9 | +7.2 | - | -0.4 | +1.0 | -0.2 | -7.1 | -1.9 | -2.2 | +3.5 | +6.2 |
| stage_time | +2.0 | +1.5 | -5.3 | -0.4 | - | -0.8 | +0.4 | +13.9 | -0.8 | -0.3 | -1.1 | -0.0 |
| ext_exploit | +4.3 | -1.0 | -2.4 | +1.0 | -0.8 | - | -1.9 | -7.0 | +0.2 | -3.2 | +3.0 | -4.2 |
| remote_share | -8.1 | +1.5 | -0.6 | -0.2 | +0.4 | -1.9 | - | -1.4 | +2.7 | +1.1 | -2.4 | +0.7 |
| inequality | -15.6 | -1.8 | +2.7 | -7.1 | +13.9 | -7.0 | -1.4 | - | +2.0 | -4.9 | +1.3 | +5.9 |
| seg_ep | -5.2 | +2.5 | -0.8 | -1.9 | -0.8 | +0.2 | +2.7 | +2.0 | - | +2.5 | +1.7 | -0.0 |
| n_ext | +3.5 | +1.6 | +0.2 | -2.2 | -0.3 | -3.2 | +1.1 | -4.9 | +2.5 | - | +3.6 | -4.5 |
| def_cap | -6.9 | +1.6 | +2.3 | +3.5 | -1.1 | +3.0 | -2.4 | +1.3 | +1.7 | +3.6 | - | +5.5 |
| ext_share | +3.4 | -4.2 | -2.0 | +6.2 | -0.0 | -4.2 | +0.7 | +5.9 | -0.0 | -4.5 | +5.5 | - |
