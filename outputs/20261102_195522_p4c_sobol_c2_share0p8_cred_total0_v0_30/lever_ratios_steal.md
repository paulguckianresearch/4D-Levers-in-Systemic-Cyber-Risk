# Lever ratios from 20261102_195522_p4c_sobol_c2_share0p8_cred_total0_v0_30 (intrusion, objective steal)

Stratum {'cred_total': 0, 'c2_share': 0.8}. 145,792 sampled configurations, 56 variables. Pair-and-square surface on standardised dial positions (same estimator as the Sobol report). A marginal is dy/du at the centre of the space in outcome units per full range of the dial (sign kept: negative lowers the outcome); 'per step' divides by the ladder's steps. The spread is the standard deviation of the marginal across fits on five disjoint fifths of the 193 base-row families (every point built on base row i stays with it). Ratios are among the defender levers with the largest marginals: one full range of the row lever is worth that many full ranges of the column lever. The pair table gives, for the same levers, how much a lever's marginal changes as another dial goes from bottom to top (its dependence on context).

## data loss (variance 0.0400; pair surface R2 90% in sample, -241% on held-out families, five family folds -84 +/- 69; additive surface -164% on held-out families, folds -52 +/- 29)

Contrast D (points per full range): |ext_total x ext_auth| = +3.9; D_node = -13.8; D_within = -4.7; D_all = -34.8

| rank | variable | who | marginal per full range | spread (5 fifths) | per ladder step |
|---|---|---|---|---|---|
| 1 | exfil_p | defender lever | +39.7 | 16.4 | +7.9 |
| 2 | iface_closed | defender lever | -21.5 | 13.7 | -4.3 |
| 3 | a_rate | defender lever | +14.5 | 7.5 | +2.9 |
| 4 | node_reconf | attacker | -14.2 | 9.3 | -2.8 |
| 5 | x_rate | defender lever | +12.7 | 13.7 | +2.5 |
| 6 | n_ext | defender lever | +9.2 | 12.5 | +1.8 |
| 7 | dval_sv | given | -7.7 | 13.4 | -1.5 |
| 8 | server_share | given | +7.4 | 9.9 | +1.5 |
| 9 | ext_exploit | defender lever | +6.0 | 4.1 | +1.2 |
| 10 | ext_auth | defender lever | +5.6 | 8.6 | +1.1 |
| 11 | ext_share | defender lever | +5.5 | 5.8 | +0.8 |
| 12 | inequality | defender lever | -5.4 | 17.7 | -1.1 |
| 13 | def_cap | defender lever | +5.1 | 4.5 | +1.0 |
| 14 | seg_sv | defender lever | -4.6 | 4.5 | -1.5 |
| 15 | atk_budget | attacker | +4.6 | 5.4 | +1.1 |

### Exchange rates among the top 12 defender levers (row worth in column units, full range to full range)

| lever | exfil_p | iface_closed | a_rate | x_rate | n_ext | ext_exploit | ext_auth | ext_share | inequality | def_cap | seg_sv | coverage |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| exfil_p | 1 | -1.85 | +2.74 | +3.13 | +4.31 | +6.67 | +7.08 | +7.21 | -7.29 | +7.78 | -8.63 | -10.38 |
| iface_closed | -0.54 | 1 | -1.49 | -1.70 | -2.34 | -3.61 | -3.84 | -3.91 | +3.95 | -4.21 | +4.67 | +5.62 |
| a_rate | +0.36 | -0.67 | 1 | +1.14 | +1.57 | +2.43 | +2.58 | +2.63 | -2.66 | +2.84 | -3.15 | -3.78 |
| x_rate | +0.32 | -0.59 | +0.88 | 1 | +1.38 | +2.13 | +2.26 | +2.30 | -2.33 | +2.48 | -2.76 | -3.31 |
| n_ext | +0.23 | -0.43 | +0.64 | +0.73 | 1 | +1.55 | +1.64 | +1.67 | -1.69 | +1.80 | -2.00 | -2.41 |
| ext_exploit | +0.15 | -0.28 | +0.41 | +0.47 | +0.65 | 1 | +1.06 | +1.08 | -1.09 | +1.17 | -1.29 | -1.56 |
| ext_auth | +0.14 | -0.26 | +0.39 | +0.44 | +0.61 | +0.94 | 1 | +1.02 | -1.03 | +1.10 | -1.22 | -1.47 |
| ext_share | +0.14 | -0.26 | +0.38 | +0.43 | +0.60 | +0.92 | +0.98 | 1 | -1.01 | +1.08 | -1.20 | -1.44 |
| inequality | -0.14 | +0.25 | -0.38 | -0.43 | -0.59 | -0.91 | -0.97 | -0.99 | 1 | -1.07 | +1.18 | +1.42 |
| def_cap | +0.13 | -0.24 | +0.35 | +0.40 | +0.55 | +0.86 | +0.91 | +0.93 | -0.94 | 1 | -1.11 | -1.33 |
| seg_sv | -0.12 | +0.21 | -0.32 | -0.36 | -0.50 | -0.77 | -0.82 | -0.84 | +0.84 | -0.90 | 1 | +1.20 |
| coverage | -0.10 | +0.18 | -0.26 | -0.30 | -0.42 | -0.64 | -0.68 | -0.69 | +0.70 | -0.75 | +0.83 | 1 |

### Context dependence: change in the row lever's marginal (per full range) as the column dial goes bottom to top

| lever | exfil_p | iface_closed | a_rate | x_rate | n_ext | ext_exploit | ext_auth | ext_share | inequality | def_cap | seg_sv | coverage |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| exfil_p | - | -38.7 | +19.4 | +4.9 | +8.9 | +7.6 | +4.2 | +3.1 | -20.3 | -11.6 | -2.6 | -10.1 |
| iface_closed | -38.7 | - | -12.6 | -17.7 | +2.7 | +2.8 | +3.7 | -6.6 | -0.9 | +2.5 | +8.1 | -4.0 |
| a_rate | +19.4 | -12.6 | - | +10.0 | -5.7 | +6.9 | -5.0 | +8.1 | -4.1 | +7.4 | +0.0 | -1.7 |
| x_rate | +4.9 | -17.7 | +10.0 | - | -3.4 | +3.4 | -6.0 | -2.5 | +7.9 | +3.4 | +2.6 | +1.9 |
| n_ext | +8.9 | +2.7 | -5.7 | -3.4 | - | -8.9 | +0.7 | -7.4 | -11.3 | +4.8 | -0.5 | +4.6 |
| ext_exploit | +7.6 | +2.8 | +6.9 | +3.4 | -8.9 | - | -4.1 | -6.8 | -8.1 | +5.0 | +6.2 | +3.1 |
| ext_auth | +4.2 | +3.7 | -5.0 | -6.0 | +0.7 | -4.1 | - | +0.4 | -7.4 | +3.5 | -0.7 | -5.4 |
| ext_share | +3.1 | -6.6 | +8.1 | -2.5 | -7.4 | -6.8 | +0.4 | - | +12.3 | +5.5 | -1.8 | -2.1 |
| inequality | -20.3 | -0.9 | -4.1 | +7.9 | -11.3 | -8.1 | -7.4 | +12.3 | - | +5.6 | -1.7 | -7.3 |
| def_cap | -11.6 | +2.5 | +7.4 | +3.4 | +4.8 | +5.0 | +3.5 | +5.5 | +5.6 | - | +1.9 | -3.0 |
| seg_sv | -2.6 | +8.1 | +0.0 | +2.6 | -0.5 | +6.2 | -0.7 | -1.8 | -1.7 | +1.9 | - | +0.4 |
| coverage | -10.1 | -4.0 | -1.7 | +1.9 | +4.6 | +3.1 | -5.4 | -2.1 | -7.3 | -3.0 | +0.4 | - |
