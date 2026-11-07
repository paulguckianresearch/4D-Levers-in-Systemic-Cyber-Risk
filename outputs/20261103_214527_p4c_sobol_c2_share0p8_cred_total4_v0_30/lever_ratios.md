# Lever ratios from 20261103_214527_p4c_sobol_c2_share0p8_cred_total4_v0_30 (intrusion)

Stratum {'cred_total': 4, 'c2_share': 0.8}. 316,416 sampled configurations, 58 variables. Pair-and-square surface on standardised dial positions (same estimator as the Sobol report). A marginal is dy/du at the centre of the space in outcome units per full range of the dial (sign kept: negative lowers the outcome); 'per step' divides by the ladder's steps. The spread is the standard deviation of the marginal across fits on five disjoint fifths of the 256 base-row families (every point built on base row i stays with it). Ratios are among the defender levers with the largest marginals: one full range of the row lever is worth that many full ranges of the column lever. The pair table gives, for the same levers, how much a lever's marginal changes as another dial goes from bottom to top (its dependence on context).

## service loss (variance 0.0330; pair surface R2 91% in sample, -19% on held-out families, five family folds 2 +/- 10; additive surface -61% on held-out families, folds -0 +/- 18)

Contrast D (points per full range): |ext_total x ext_auth| = +12.3; D_node = -14.0; D_within = +3.7; D_all = -14.0

| rank | variable | who | marginal per full range | spread (5 fifths) | per ladder step |
|---|---|---|---|---|---|
| 1 | iface_closed | defender lever | -25.7 | 3.8 | -5.1 |
| 2 | x_rate | defender lever | +14.2 | 3.3 | +2.8 |
| 3 | a_rate | defender lever | +13.5 | 3.0 | +2.7 |
| 4 | atk_cap | attacker | +9.3 | 2.8 | +1.9 |
| 5 | ext_exploit | defender lever | +8.5 | 4.8 | +1.7 |
| 6 | coverage | defender lever | -7.8 | 3.4 | -1.6 |
| 7 | dval_sv | given | +7.1 | 2.4 | +1.4 |
| 8 | ext_total | defender lever | -6.4 | 3.9 | -1.3 |
| 9 | def_cap | defender lever | -5.4 | 1.4 | -1.1 |
| 10 | auth_cred | defender lever | +4.5 | 2.6 | +0.9 |
| 11 | ext_auth | defender lever | -4.3 | 2.7 | -0.9 |
| 12 | payload_delay | attacker | -4.3 | 1.9 | -0.9 |
| 13 | vpn | defender lever | +4.2 | 4.1 | +0.8 |
| 14 | reconf_time | attacker | +3.9 | 2.4 | +0.8 |
| 15 | rebuild_time | defender lever | +3.8 | 1.4 | +0.8 |

### Exchange rates among the top 12 defender levers (row worth in column units, full range to full range)

| lever | iface_closed | x_rate | a_rate | ext_exploit | coverage | ext_total | def_cap | auth_cred | ext_auth | vpn | rebuild_time | c_s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| iface_closed | 1 | -1.81 | -1.90 | -3.01 | +3.30 | +4.00 | +4.73 | -5.70 | +5.97 | -6.06 | -6.69 | +7.39 |
| x_rate | -0.55 | 1 | +1.05 | +1.66 | -1.82 | -2.21 | -2.61 | +3.14 | -3.29 | +3.34 | +3.69 | -4.07 |
| a_rate | -0.53 | +0.95 | 1 | +1.59 | -1.73 | -2.10 | -2.49 | +3.00 | -3.14 | +3.19 | +3.52 | -3.89 |
| ext_exploit | -0.33 | +0.60 | +0.63 | 1 | -1.09 | -1.33 | -1.57 | +1.89 | -1.98 | +2.01 | +2.22 | -2.45 |
| coverage | +0.30 | -0.55 | -0.58 | -0.91 | 1 | +1.21 | +1.43 | -1.73 | +1.81 | -1.84 | -2.03 | +2.24 |
| ext_total | +0.25 | -0.45 | -0.48 | -0.75 | +0.82 | 1 | +1.18 | -1.42 | +1.49 | -1.51 | -1.67 | +1.85 |
| def_cap | +0.21 | -0.38 | -0.40 | -0.64 | +0.70 | +0.85 | 1 | -1.20 | +1.26 | -1.28 | -1.41 | +1.56 |
| auth_cred | -0.18 | +0.32 | +0.33 | +0.53 | -0.58 | -0.70 | -0.83 | 1 | -1.05 | +1.06 | +1.17 | -1.30 |
| ext_auth | +0.17 | -0.30 | -0.32 | -0.50 | +0.55 | +0.67 | +0.79 | -0.95 | 1 | -1.01 | -1.12 | +1.24 |
| vpn | -0.17 | +0.30 | +0.31 | +0.50 | -0.54 | -0.66 | -0.78 | +0.94 | -0.99 | 1 | +1.10 | -1.22 |
| rebuild_time | -0.15 | +0.27 | +0.28 | +0.45 | -0.49 | -0.60 | -0.71 | +0.85 | -0.89 | +0.91 | 1 | -1.10 |
| c_s | +0.14 | -0.25 | -0.26 | -0.41 | +0.45 | +0.54 | +0.64 | -0.77 | +0.81 | -0.82 | -0.91 | 1 |

### Context dependence: change in the row lever's marginal (per full range) as the column dial goes bottom to top

| lever | iface_closed | x_rate | a_rate | ext_exploit | coverage | ext_total | def_cap | auth_cred | ext_auth | vpn | rebuild_time | c_s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| iface_closed | - | -25.1 | -26.3 | -11.9 | +11.1 | +21.9 | +2.2 | -4.0 | +9.7 | -1.2 | +4.6 | +10.0 |
| x_rate | -25.1 | - | +4.7 | +3.7 | -1.4 | -3.9 | -4.4 | -1.4 | -2.9 | +6.7 | -4.6 | +7.7 |
| a_rate | -26.3 | +4.7 | - | +10.1 | -7.0 | -4.0 | -8.9 | +1.7 | -6.7 | -5.9 | +4.1 | -2.2 |
| ext_exploit | -11.9 | +3.7 | +10.1 | - | -3.3 | -6.4 | +0.6 | +2.9 | -0.8 | -3.5 | -1.3 | +1.3 |
| coverage | +11.1 | -1.4 | -7.0 | -3.3 | - | +1.3 | -8.6 | -0.3 | +2.6 | -4.3 | +4.3 | -1.7 |
| ext_total | +21.9 | -3.9 | -4.0 | -6.4 | +1.3 | - | +4.0 | -6.7 | -12.3 | +0.1 | -5.9 | +8.2 |
| def_cap | +2.2 | -4.4 | -8.9 | +0.6 | -8.6 | +4.0 | - | -1.9 | -0.5 | -0.5 | +1.4 | -1.7 |
| auth_cred | -4.0 | -1.4 | +1.7 | +2.9 | -0.3 | -6.7 | -1.9 | - | -2.2 | +1.3 | -0.8 | +0.2 |
| ext_auth | +9.7 | -2.9 | -6.7 | -0.8 | +2.6 | -12.3 | -0.5 | -2.2 | - | -0.7 | +1.5 | +4.7 |
| vpn | -1.2 | +6.7 | -5.9 | -3.5 | -4.3 | +0.1 | -0.5 | +1.3 | -0.7 | - | +0.9 | -6.3 |
| rebuild_time | +4.6 | -4.6 | +4.1 | -1.3 | +4.3 | -5.9 | +1.4 | -0.8 | +1.5 | +0.9 | - | +2.3 |
| c_s | +10.0 | +7.7 | -2.2 | +1.3 | -1.7 | +8.2 | -1.7 | +0.2 | +4.7 | -6.3 | +2.3 | - |

## collapse (variance 0.1742; pair surface R2 84% in sample, -19% on held-out families, five family folds -32 +/- 28; additive surface -11% on held-out families, folds -26 +/- 18)

Contrast D (points per full range): |ext_total x ext_auth| = +41.6; D_node = -0.8; D_within = -9.4; D_all = -9.4

| rank | variable | who | marginal per full range | spread (5 fifths) | per ladder step |
|---|---|---|---|---|---|
| 1 | iface_closed | defender lever | -54.0 | 13.3 | -10.8 |
| 2 | ext_auth | defender lever | +20.1 | 12.1 | +4.0 |
| 3 | ext_total | defender lever | +19.4 | 14.6 | +3.9 |
| 4 | chan_cov | defender lever | +19.1 | 10.8 | +3.8 |
| 5 | x_rate | defender lever | +18.7 | 2.6 | +3.7 |
| 6 | n_chan | defender lever | +18.7 | 9.2 | +3.7 |
| 7 | server_share | given | +18.7 | 11.8 | +3.7 |
| 8 | ext_share | defender lever | +18.2 | 12.3 | +2.6 |
| 9 | ext_bad | given | +17.0 | 8.7 | +3.4 |
| 10 | a_rate | defender lever | +16.2 | 2.6 | +3.2 |
| 11 | atk_cap | attacker | +15.5 | 5.0 | +3.1 |
| 12 | ext_exploit | defender lever | +14.0 | 5.7 | +2.8 |
| 13 | coverage | defender lever | -13.2 | 7.6 | -2.6 |
| 14 | def_cap | defender lever | -12.9 | 4.8 | -2.6 |
| 15 | cloud_share | defender lever | -11.8 | 11.3 | -2.4 |

### Exchange rates among the top 12 defender levers (row worth in column units, full range to full range)

| lever | iface_closed | ext_auth | ext_total | chan_cov | x_rate | n_chan | ext_share | a_rate | ext_exploit | coverage | def_cap | cloud_share |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| iface_closed | 1 | -2.70 | -2.78 | -2.82 | -2.89 | -2.89 | -2.97 | -3.35 | -3.85 | +4.08 | +4.20 | +4.57 |
| ext_auth | -0.37 | 1 | +1.03 | +1.05 | +1.07 | +1.07 | +1.10 | +1.24 | +1.43 | -1.52 | -1.56 | -1.70 |
| ext_total | -0.36 | +0.97 | 1 | +1.02 | +1.04 | +1.04 | +1.07 | +1.20 | +1.38 | -1.47 | -1.51 | -1.64 |
| chan_cov | -0.35 | +0.95 | +0.99 | 1 | +1.02 | +1.02 | +1.05 | +1.18 | +1.36 | -1.45 | -1.49 | -1.62 |
| x_rate | -0.35 | +0.93 | +0.96 | +0.98 | 1 | +1.00 | +1.03 | +1.16 | +1.33 | -1.42 | -1.46 | -1.58 |
| n_chan | -0.35 | +0.93 | +0.96 | +0.98 | +1.00 | 1 | +1.03 | +1.16 | +1.33 | -1.41 | -1.45 | -1.58 |
| ext_share | -0.34 | +0.91 | +0.94 | +0.95 | +0.97 | +0.97 | 1 | +1.13 | +1.29 | -1.37 | -1.41 | -1.54 |
| a_rate | -0.30 | +0.81 | +0.83 | +0.84 | +0.86 | +0.87 | +0.89 | 1 | +1.15 | -1.22 | -1.26 | -1.37 |
| ext_exploit | -0.26 | +0.70 | +0.72 | +0.73 | +0.75 | +0.75 | +0.77 | +0.87 | 1 | -1.06 | -1.09 | -1.19 |
| coverage | +0.24 | -0.66 | -0.68 | -0.69 | -0.71 | -0.71 | -0.73 | -0.82 | -0.94 | 1 | +1.03 | +1.12 |
| def_cap | +0.24 | -0.64 | -0.66 | -0.67 | -0.69 | -0.69 | -0.71 | -0.80 | -0.92 | +0.97 | 1 | +1.09 |
| cloud_share | +0.22 | -0.59 | -0.61 | -0.62 | -0.63 | -0.63 | -0.65 | -0.73 | -0.84 | +0.89 | +0.92 | 1 |

### Context dependence: change in the row lever's marginal (per full range) as the column dial goes bottom to top

| lever | iface_closed | ext_auth | ext_total | chan_cov | x_rate | n_chan | ext_share | a_rate | ext_exploit | coverage | def_cap | cloud_share |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| iface_closed | - | +20.7 | +20.1 | -4.9 | -42.0 | +33.6 | -47.3 | -42.5 | -17.3 | +25.1 | +18.2 | +3.4 |
| ext_auth | +20.7 | - | +41.6 | +19.4 | -16.9 | +6.8 | -4.5 | -8.1 | -7.3 | +17.7 | -5.0 | -2.7 |
| ext_total | +20.1 | +41.6 | - | -1.4 | +0.2 | -1.6 | +7.4 | +7.9 | -12.1 | -6.9 | -2.8 | +1.9 |
| chan_cov | -4.9 | +19.4 | -1.4 | - | +15.0 | +51.1 | +1.7 | +15.9 | -4.4 | -15.8 | -6.6 | +5.6 |
| x_rate | -42.0 | -16.9 | +0.2 | +15.0 | - | +6.9 | +20.9 | -1.6 | +0.8 | +10.1 | -9.7 | +6.7 |
| n_chan | +33.6 | +6.8 | -1.6 | +51.1 | +6.9 | - | +3.7 | +25.0 | -2.1 | -0.0 | +2.8 | +7.9 |
| ext_share | -47.3 | -4.5 | +7.4 | +1.7 | +20.9 | +3.7 | - | +1.8 | +0.1 | -8.4 | -10.5 | -1.4 |
| a_rate | -42.5 | -8.1 | +7.9 | +15.9 | -1.6 | +25.0 | +1.8 | - | +22.6 | -7.4 | -6.2 | -15.8 |
| ext_exploit | -17.3 | -7.3 | -12.1 | -4.4 | +0.8 | -2.1 | +0.1 | +22.6 | - | -3.6 | +11.2 | +4.3 |
| coverage | +25.1 | +17.7 | -6.9 | -15.8 | +10.1 | -0.0 | -8.4 | -7.4 | -3.6 | - | -22.8 | +11.7 |
| def_cap | +18.2 | -5.0 | -2.8 | -6.6 | -9.7 | +2.8 | -10.5 | -6.2 | +11.2 | -22.8 | - | +7.1 |
| cloud_share | +3.4 | -2.7 | +1.9 | +5.6 | +6.7 | +7.9 | -1.4 | -15.8 | +4.3 | +11.7 | +7.1 | - |

## peak reach (variance 0.1055; pair surface R2 90% in sample, 20% on held-out families, five family folds 9 +/- 15; additive surface -7% on held-out families, folds -12 +/- 17)

Contrast D (points per full range): |ext_total x ext_auth| = +37.0; D_node = -6.2; D_within = +10.8; D_all = -6.2

| rank | variable | who | marginal per full range | spread (5 fifths) | per ladder step |
|---|---|---|---|---|---|
| 1 | iface_closed | defender lever | -48.5 | 6.3 | -9.7 |
| 2 | ext_auth | defender lever | +22.8 | 8.3 | +4.6 |
| 3 | x_rate | defender lever | +22.8 | 6.9 | +4.6 |
| 4 | a_rate | defender lever | +19.6 | 2.7 | +3.9 |
| 5 | ext_total | defender lever | +19.0 | 8.0 | +3.8 |
| 6 | ext_bad | given | +18.5 | 6.8 | +3.7 |
| 7 | atk_cap | attacker | +15.2 | 1.6 | +3.0 |
| 8 | ext_share | defender lever | +13.4 | 5.4 | +1.9 |
| 9 | coverage | defender lever | -11.3 | 8.6 | -2.3 |
| 10 | n_chan | defender lever | +10.7 | 6.3 | +2.1 |
| 11 | ext_exploit | defender lever | +10.3 | 6.1 | +2.1 |
| 12 | chan_cov | defender lever | +9.5 | 3.6 | +1.9 |
| 13 | managed | defender lever | +9.1 | 9.8 | +1.8 |
| 14 | n_ext | defender lever | +7.9 | 4.3 | +1.6 |
| 15 | server_share | given | +7.3 | 7.4 | +1.5 |

### Exchange rates among the top 12 defender levers (row worth in column units, full range to full range)

| lever | iface_closed | ext_auth | x_rate | a_rate | ext_total | ext_share | coverage | n_chan | ext_exploit | chan_cov | managed | n_ext |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| iface_closed | 1 | -2.12 | -2.13 | -2.47 | -2.55 | -3.60 | +4.29 | -4.53 | -4.71 | -5.11 | -5.35 | -6.10 |
| ext_auth | -0.47 | 1 | +1.00 | +1.16 | +1.20 | +1.70 | -2.02 | +2.13 | +2.22 | +2.41 | +2.52 | +2.87 |
| x_rate | -0.47 | +1.00 | 1 | +1.16 | +1.20 | +1.69 | -2.02 | +2.13 | +2.21 | +2.40 | +2.51 | +2.87 |
| a_rate | -0.41 | +0.86 | +0.86 | 1 | +1.03 | +1.46 | -1.74 | +1.84 | +1.91 | +2.07 | +2.17 | +2.47 |
| ext_total | -0.39 | +0.83 | +0.84 | +0.97 | 1 | +1.41 | -1.68 | +1.78 | +1.85 | +2.00 | +2.10 | +2.40 |
| ext_share | -0.28 | +0.59 | +0.59 | +0.68 | +0.71 | 1 | -1.19 | +1.26 | +1.31 | +1.42 | +1.48 | +1.69 |
| coverage | +0.23 | -0.49 | -0.50 | -0.57 | -0.59 | -0.84 | 1 | -1.06 | -1.10 | -1.19 | -1.25 | -1.42 |
| n_chan | -0.22 | +0.47 | +0.47 | +0.54 | +0.56 | +0.80 | -0.95 | 1 | +1.04 | +1.13 | +1.18 | +1.35 |
| ext_exploit | -0.21 | +0.45 | +0.45 | +0.52 | +0.54 | +0.77 | -0.91 | +0.96 | 1 | +1.09 | +1.14 | +1.30 |
| chan_cov | -0.20 | +0.42 | +0.42 | +0.48 | +0.50 | +0.71 | -0.84 | +0.89 | +0.92 | 1 | +1.05 | +1.19 |
| managed | -0.19 | +0.40 | +0.40 | +0.46 | +0.48 | +0.67 | -0.80 | +0.85 | +0.88 | +0.96 | 1 | +1.14 |
| n_ext | -0.16 | +0.35 | +0.35 | +0.40 | +0.42 | +0.59 | -0.70 | +0.74 | +0.77 | +0.84 | +0.88 | 1 |

### Context dependence: change in the row lever's marginal (per full range) as the column dial goes bottom to top

| lever | iface_closed | ext_auth | x_rate | a_rate | ext_total | ext_share | coverage | n_chan | ext_exploit | chan_cov | managed | n_ext |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| iface_closed | - | +27.6 | -32.6 | -43.2 | +29.7 | -18.6 | +6.1 | +13.0 | -11.4 | -0.6 | +19.8 | +11.2 |
| ext_auth | +27.6 | - | -8.4 | -14.0 | +37.0 | -11.0 | +14.6 | -3.9 | -3.4 | +6.8 | +10.9 | +6.3 |
| x_rate | -32.6 | -8.4 | - | +2.4 | -4.9 | +12.1 | +2.6 | +5.5 | -5.7 | +4.3 | -9.1 | -7.6 |
| a_rate | -43.2 | -14.0 | +2.4 | - | -9.2 | -2.4 | +1.7 | +7.6 | +14.8 | +3.7 | +4.2 | +5.0 |
| ext_total | +29.7 | +37.0 | -4.9 | -9.2 | - | +1.0 | -1.3 | +1.6 | -12.1 | -1.8 | +3.4 | +26.3 |
| ext_share | -18.6 | -11.0 | +12.1 | -2.4 | +1.0 | - | -4.9 | +1.4 | -13.9 | -5.3 | -6.4 | -7.8 |
| coverage | +6.1 | +14.6 | +2.6 | +1.7 | -1.3 | -4.9 | - | -5.6 | +1.0 | -2.3 | -0.6 | -0.1 |
| n_chan | +13.0 | -3.9 | +5.5 | +7.6 | +1.6 | +1.4 | -5.6 | - | -2.4 | +26.1 | +0.2 | -0.6 |
| ext_exploit | -11.4 | -3.4 | -5.7 | +14.8 | -12.1 | -13.9 | +1.0 | -2.4 | - | +1.5 | -9.3 | +7.6 |
| chan_cov | -0.6 | +6.8 | +4.3 | +3.7 | -1.8 | -5.3 | -2.3 | +26.1 | +1.5 | - | -0.4 | +19.6 |
| managed | +19.8 | +10.9 | -9.1 | +4.2 | +3.4 | -6.4 | -0.6 | +0.2 | -9.3 | -0.4 | - | +1.7 |
| n_ext | +11.2 | +6.3 | -7.6 | +5.0 | +26.3 | -7.8 | -0.1 | -0.6 | +7.6 | +19.6 | +1.7 | - |

## data loss (variance 0.0341; pair surface R2 89% in sample, -78% on held-out families, five family folds -4 +/- 23; additive surface -105% on held-out families, folds -9 +/- 11)

Contrast D (points per full range): |ext_total x ext_auth| = +5.5; D_node = -4.0; D_within = +1.8; D_all = -46.3

| rank | variable | who | marginal per full range | spread (5 fifths) | per ladder step |
|---|---|---|---|---|---|
| 1 | objective | attacker | -30.3 | 7.5 | -30.3 |
| 2 | exfil_p | defender lever | +16.5 | 4.4 | +3.3 |
| 3 | iface_closed | defender lever | -11.8 | 7.9 | -2.4 |
| 4 | node_reconf | attacker | -8.9 | 4.1 | -1.8 |
| 5 | a_rate | defender lever | +5.5 | 2.5 | +1.1 |
| 6 | x_rate | defender lever | +5.2 | 3.2 | +1.0 |
| 7 | vpn | defender lever | +4.5 | 4.4 | +0.9 |
| 8 | managed | defender lever | +3.7 | 5.6 | +0.7 |
| 9 | dval_sv | given | +3.4 | 3.6 | +0.7 |
| 10 | n_ext | defender lever | +3.3 | 5.1 | +0.7 |
| 11 | ext_exploit | defender lever | +3.2 | 3.4 | +0.6 |
| 12 | t_cut | defender lever | +3.1 | 2.7 | +0.6 |
| 13 | ep_sv | defender lever | +3.1 | 4.4 | +0.6 |
| 14 | atk_cap | attacker | +2.7 | 2.0 | +0.5 |
| 15 | visibility | defender lever | -2.3 | 2.6 | -0.5 |

### Exchange rates among the top 12 defender levers (row worth in column units, full range to full range)

| lever | exfil_p | iface_closed | a_rate | x_rate | vpn | managed | n_ext | ext_exploit | t_cut | ep_sv | visibility | ext_share |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| exfil_p | 1 | -1.40 | +3.01 | +3.16 | +3.68 | +4.49 | +4.97 | +5.16 | +5.26 | +5.32 | -7.31 | +7.61 |
| iface_closed | -0.72 | 1 | -2.15 | -2.26 | -2.63 | -3.21 | -3.55 | -3.69 | -3.76 | -3.81 | +5.23 | -5.44 |
| a_rate | +0.33 | -0.46 | 1 | +1.05 | +1.22 | +1.49 | +1.65 | +1.71 | +1.75 | +1.77 | -2.43 | +2.53 |
| x_rate | +0.32 | -0.44 | +0.95 | 1 | +1.17 | +1.42 | +1.57 | +1.63 | +1.66 | +1.68 | -2.32 | +2.41 |
| vpn | +0.27 | -0.38 | +0.82 | +0.86 | 1 | +1.22 | +1.35 | +1.40 | +1.43 | +1.45 | -1.99 | +2.07 |
| managed | +0.22 | -0.31 | +0.67 | +0.70 | +0.82 | 1 | +1.11 | +1.15 | +1.17 | +1.19 | -1.63 | +1.70 |
| n_ext | +0.20 | -0.28 | +0.61 | +0.64 | +0.74 | +0.90 | 1 | +1.04 | +1.06 | +1.07 | -1.47 | +1.53 |
| ext_exploit | +0.19 | -0.27 | +0.58 | +0.61 | +0.71 | +0.87 | +0.96 | 1 | +1.02 | +1.03 | -1.42 | +1.47 |
| t_cut | +0.19 | -0.27 | +0.57 | +0.60 | +0.70 | +0.85 | +0.94 | +0.98 | 1 | +1.01 | -1.39 | +1.45 |
| ep_sv | +0.19 | -0.26 | +0.57 | +0.59 | +0.69 | +0.84 | +0.93 | +0.97 | +0.99 | 1 | -1.37 | +1.43 |
| visibility | -0.14 | +0.19 | -0.41 | -0.43 | -0.50 | -0.61 | -0.68 | -0.71 | -0.72 | -0.73 | 1 | -1.04 |
| ext_share | +0.13 | -0.18 | +0.40 | +0.41 | +0.48 | +0.59 | +0.65 | +0.68 | +0.69 | +0.70 | -0.96 | 1 |

### Context dependence: change in the row lever's marginal (per full range) as the column dial goes bottom to top

| lever | exfil_p | iface_closed | a_rate | x_rate | vpn | managed | n_ext | ext_exploit | t_cut | ep_sv | visibility | ext_share |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| exfil_p | - | -23.8 | +2.5 | +6.8 | +4.6 | -0.9 | +5.5 | +8.9 | -3.1 | +6.3 | +4.5 | +11.1 |
| iface_closed | -23.8 | - | -9.3 | -9.5 | -9.3 | +4.8 | +5.5 | -3.5 | -2.7 | +0.3 | -3.1 | -2.2 |
| a_rate | +2.5 | -9.3 | - | +2.2 | -8.2 | +6.3 | +1.0 | +2.2 | -0.7 | +1.8 | -1.7 | -7.2 |
| x_rate | +6.8 | -9.5 | +2.2 | - | +5.2 | -7.5 | +4.3 | -0.8 | +10.8 | -5.0 | -0.3 | +4.1 |
| vpn | +4.6 | -9.3 | -8.2 | +5.2 | - | +3.8 | +5.1 | +3.2 | +6.9 | -4.1 | +1.7 | +0.1 |
| managed | -0.9 | +4.8 | +6.3 | -7.5 | +3.8 | - | +4.4 | -2.5 | -5.0 | +0.9 | +2.3 | -1.6 |
| n_ext | +5.5 | +5.5 | +1.0 | +4.3 | +5.1 | +4.4 | - | -3.4 | -2.8 | +0.4 | -2.6 | -1.0 |
| ext_exploit | +8.9 | -3.5 | +2.2 | -0.8 | +3.2 | -2.5 | -3.4 | - | +1.0 | -10.1 | +2.7 | -2.7 |
| t_cut | -3.1 | -2.7 | -0.7 | +10.8 | +6.9 | -5.0 | -2.8 | +1.0 | - | +6.5 | -2.0 | +3.9 |
| ep_sv | +6.3 | +0.3 | +1.8 | -5.0 | -4.1 | +0.9 | +0.4 | -10.1 | +6.5 | - | -2.7 | +1.0 |
| visibility | +4.5 | -3.1 | -1.7 | -0.3 | +1.7 | +2.3 | -2.6 | +2.7 | -2.0 | -2.7 | - | -1.0 |
| ext_share | +11.1 | -2.2 | -7.2 | +4.1 | +0.1 | -1.6 | -1.0 | -2.7 | +3.9 | +1.0 | -1.0 | - |
