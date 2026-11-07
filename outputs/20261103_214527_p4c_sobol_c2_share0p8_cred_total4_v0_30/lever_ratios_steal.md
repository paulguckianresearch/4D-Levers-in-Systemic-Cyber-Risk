# Lever ratios from 20261103_214527_p4c_sobol_c2_share0p8_cred_total4_v0_30 (intrusion, objective steal)

Stratum {'cred_total': 4, 'c2_share': 0.8}. 158,208 sampled configurations, 58 variables. Pair-and-square surface on standardised dial positions (same estimator as the Sobol report). A marginal is dy/du at the centre of the space in outcome units per full range of the dial (sign kept: negative lowers the outcome); 'per step' divides by the ladder's steps. The spread is the standard deviation of the marginal across fits on five disjoint fifths of the 190 base-row families (every point built on base row i stays with it). Ratios are among the defender levers with the largest marginals: one full range of the row lever is worth that many full ranges of the column lever. The pair table gives, for the same levers, how much a lever's marginal changes as another dial goes from bottom to top (its dependence on context).

## data loss (variance 0.0527; pair surface R2 92% in sample, -91% on held-out families, five family folds -46 +/- 67; additive surface -114% on held-out families, folds -5 +/- 17)

Contrast D (points per full range): |ext_total x ext_auth| = +9.3; D_node = -10.2; D_within = +0.3; D_all = -36.3

| rank | variable | who | marginal per full range | spread (5 fifths) | per ladder step |
|---|---|---|---|---|---|
| 1 | exfil_p | defender lever | +32.7 | 18.5 | +6.5 |
| 2 | objective | attacker | -19.7 | 48.8 | -19.7 |
| 3 | iface_closed | defender lever | -18.5 | 14.0 | -3.7 |
| 4 | a_rate | defender lever | +16.5 | 7.3 | +3.3 |
| 5 | node_reconf | attacker | -15.9 | 10.5 | -3.2 |
| 6 | n_ext | defender lever | +14.9 | 10.4 | +3.0 |
| 7 | c_s | defender lever | +9.7 | 19.1 | +1.9 |
| 8 | dval_sv | given | +9.5 | 7.3 | +1.9 |
| 9 | atk_cap | attacker | +6.9 | 15.5 | +1.4 |
| 10 | managed | defender lever | +6.6 | 6.8 | +1.3 |
| 11 | retool | attacker | +6.0 | 5.8 | +1.2 |
| 12 | x_rate | defender lever | +5.2 | 6.4 | +1.0 |
| 13 | vpn | defender lever | +5.1 | 24.8 | +1.0 |
| 14 | ext_bad | given | +4.9 | 15.1 | +1.0 |
| 15 | ext_exploit | defender lever | +4.4 | 6.9 | +0.9 |

### Exchange rates among the top 12 defender levers (row worth in column units, full range to full range)

| lever | exfil_p | iface_closed | a_rate | n_ext | c_s | managed | x_rate | vpn | ext_exploit | visibility | n_chan | tac_budget |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| exfil_p | 1 | -1.77 | +1.98 | +2.19 | +3.38 | +4.97 | +6.31 | +6.43 | +7.48 | -8.35 | +9.06 | -9.83 |
| iface_closed | -0.56 | 1 | -1.12 | -1.24 | -1.91 | -2.81 | -3.56 | -3.63 | -4.23 | +4.72 | -5.12 | +5.55 |
| a_rate | +0.50 | -0.89 | 1 | +1.11 | +1.70 | +2.51 | +3.18 | +3.24 | +3.77 | -4.21 | +4.56 | -4.95 |
| n_ext | +0.46 | -0.81 | +0.90 | 1 | +1.54 | +2.27 | +2.88 | +2.93 | +3.41 | -3.81 | +4.13 | -4.48 |
| c_s | +0.30 | -0.52 | +0.59 | +0.65 | 1 | +1.47 | +1.87 | +1.90 | +2.21 | -2.47 | +2.68 | -2.91 |
| managed | +0.20 | -0.36 | +0.40 | +0.44 | +0.68 | 1 | +1.27 | +1.29 | +1.50 | -1.68 | +1.82 | -1.98 |
| x_rate | +0.16 | -0.28 | +0.31 | +0.35 | +0.54 | +0.79 | 1 | +1.02 | +1.19 | -1.32 | +1.44 | -1.56 |
| vpn | +0.16 | -0.28 | +0.31 | +0.34 | +0.53 | +0.77 | +0.98 | 1 | +1.16 | -1.30 | +1.41 | -1.53 |
| ext_exploit | +0.13 | -0.24 | +0.27 | +0.29 | +0.45 | +0.66 | +0.84 | +0.86 | 1 | -1.12 | +1.21 | -1.31 |
| visibility | -0.12 | +0.21 | -0.24 | -0.26 | -0.40 | -0.60 | -0.76 | -0.77 | -0.90 | 1 | -1.08 | +1.18 |
| n_chan | +0.11 | -0.20 | +0.22 | +0.24 | +0.37 | +0.55 | +0.70 | +0.71 | +0.83 | -0.92 | 1 | -1.09 |
| tac_budget | -0.10 | +0.18 | -0.20 | -0.22 | -0.34 | -0.51 | -0.64 | -0.65 | -0.76 | +0.85 | -0.92 | 1 |

### Context dependence: change in the row lever's marginal (per full range) as the column dial goes bottom to top

| lever | exfil_p | iface_closed | a_rate | n_ext | c_s | managed | x_rate | vpn | ext_exploit | visibility | n_chan | tac_budget |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| exfil_p | - | -45.6 | +4.5 | +16.4 | +7.7 | -3.2 | +14.6 | +16.6 | +24.9 | -0.1 | +3.5 | -7.9 |
| iface_closed | -45.6 | - | -19.5 | +10.2 | +5.0 | +14.9 | -16.1 | -21.5 | -8.1 | -6.0 | +3.7 | +14.5 |
| a_rate | +4.5 | -19.5 | - | +5.1 | -11.9 | +3.0 | +1.2 | -13.2 | +5.5 | -2.3 | +2.0 | +4.3 |
| n_ext | +16.4 | +10.2 | +5.1 | - | +6.7 | +8.0 | +7.3 | +10.0 | -1.4 | -4.3 | -0.6 | -6.7 |
| c_s | +7.7 | +5.0 | -11.9 | +6.7 | - | -1.4 | +20.1 | -3.0 | +5.7 | +3.3 | +3.3 | +1.1 |
| managed | -3.2 | +14.9 | +3.0 | +8.0 | -1.4 | - | -11.0 | +7.3 | -1.5 | +7.0 | -6.2 | -1.4 |
| x_rate | +14.6 | -16.1 | +1.2 | +7.3 | +20.1 | -11.0 | - | +0.6 | -0.5 | +3.1 | +12.3 | +4.4 |
| vpn | +16.6 | -21.5 | -13.2 | +10.0 | -3.0 | +7.3 | +0.6 | - | +9.7 | +0.9 | +6.0 | +0.9 |
| ext_exploit | +24.9 | -8.1 | +5.5 | -1.4 | +5.7 | -1.5 | -0.5 | +9.7 | - | +5.0 | -2.8 | -1.8 |
| visibility | -0.1 | -6.0 | -2.3 | -4.3 | +3.3 | +7.0 | +3.1 | +0.9 | +5.0 | - | -3.2 | -2.0 |
| n_chan | +3.5 | +3.7 | +2.0 | -0.6 | +3.3 | -6.2 | +12.3 | +6.0 | -2.8 | -3.2 | - | +2.7 |
| tac_budget | -7.9 | +14.5 | +4.3 | -6.7 | +1.1 | -1.4 | +4.4 | +0.9 | -1.8 | -2.0 | +2.7 | - |
