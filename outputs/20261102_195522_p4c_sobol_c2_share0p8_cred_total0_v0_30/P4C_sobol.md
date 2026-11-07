# Paper 4C global sensitivity: Sobol indices (PhDPaper4C v1.1 (2026-11-05, surface validation for Paper 4D; model as v0.26/v0.27)) - stratum {'cred_total': 0, 'c2_share': 0.8}

Base sample N = 256, Latin hypercube on each variable's ladder; each configuration on wirings [6801, 6802] and seeds [6901, 6902]. First-order index: the share of the outcome's variance a variable explains alone. Total index: the share it explains alone or with others; the difference is its interaction share. A pair's term is the variance the two explain together beyond what each explains alone. Groups are not set in advance: a response surface is fitted to every sampled point and the variables are clustered by the size of their pairwise terms, so a group is a set of levers that act together in the data. Group, group-pair and group-triple terms are then computed on that surface. Intervals: 95% bootstrap over the sample. Variables not sampled sit at the register's neutral value.

## intrusion

### collapse (variance 0.1634)

| term | first-order | total | interaction share | 95% interval (first-order) |
|---|---|---|---|---|
| iface_closed | 2 | 38 | 36 | -10 to 14 |
| coverage | -5 | 18 | 23 | -14 to 4 |
| x_rate | -1 | 17 | 18 | -8 to 7 |
| server_share | -0 | 17 | 17 | -8 to 7 |
| n_chan | -1 | 15 | 17 | -9 to 5 |
| atk_cap | 4 | 15 | 12 | -1 to 10 |
| ext_total | -1 | 15 | 15 | -8 to 5 |
| n_ext | -3 | 13 | 17 | -12 to 3 |
| ext_auth | -4 | 10 | 14 | -11 to 1 |
| a_rate | 5 | 10 | 5 | -1 to 13 |
| size | -6 | 9 | 15 | -14 to 0 |
| chan_span | 4 | 9 | 5 | -2 to 11 |
| ext_share | 2 | 8 | 7 | -4 to 9 |
| ext_exploit | -1 | 8 | 9 | -7 to 6 |
| ext_bad | -7 | 8 | 15 | -16 to 1 |
| cloud_share | -3 | 8 | 11 | -9 to 1 |
| def_cap | 2 | 7 | 5 | -6 to 10 |
| chan_cov | -3 | 7 | 9 | -8 to 1 |
| rebuild_time | 3 | 6 | 3 | 0 to 8 |
| atk_budget | -4 | 5 | 9 | -12 to 1 |
| t_cut | 2 | 4 | 3 | -0 to 4 |
| seg_ep | -2 | 4 | 6 | -6 to 1 |
| seg_sv | -2 | 4 | 6 | -8 to 2 |
| zone_conn | -2 | 3 | 5 | -5 to 1 |
| payload_delay | 1 | 3 | 2 | -1 to 3 |
| blind_delay | -3 | 3 | 6 | -9 to 2 |
| chan | -2 | 3 | 5 | -7 to 1 |
| dose | 3 | 3 | 0 | 0 to 8 |
| supplied_x | -1 | 3 | 4 | -3 to 1 |
| tac_budget | 0 | 3 | 2 | -1 to 2 |
| theta | -4 | 2 | 6 | -11 to 0 |
| remote_share | 1 | 2 | 1 | -1 to 4 |
| retool | 3 | 2 | -1 | 0 to 9 |
| visibility | 0 | 2 | 1 | -1 to 2 |
| c_s | 0 | 2 | 2 | -1 to 1 |
| redundancy | 2 | 2 | -1 | 0 to 5 |
| t_clean | 0 | 1 | 1 | 0 to 1 |
| ep_conn | -0 | 1 | 2 | -2 to 2 |
| fanout | -1 | 1 | 3 | -4 to 1 |
| queue_order | -0 | 1 | 1 | -1 to 0 |
| inequality | -1 | 1 | 2 | -3 to 1 |
| concentration | -0 | 1 | 1 | -2 to 1 |
| reconf_time | 1 | 1 | -0 | -0 to 3 |
| auth_cred | 0 | 1 | 0 | -1 to 2 |
| manual_delay | 1 | 1 | -1 | 0 to 3 |
| cap_spread | -0 | 1 | 1 | -1 to 0 |
| cap_drift | -1 | 1 | 2 | -2 to 0 |
| vpn | 1 | 0 | -0 | 0 to 2 |
| supplied_a | 0 | 0 | -0 | -1 to 2 |
| stage_time | 0 | 0 | 0 | -1 to 1 |
| ep_sv | -0 | 0 | 1 | -1 to 0 |
| node_reconf | 1 | 0 | -0 | 0 to 2 |
| exfil_p | -0 | 0 | 1 | -1 to 0 |
| objective | 0 | 0 | -0 | 0 to 1 |
| managed | 0 | 0 | 0 | 0 to 0 |
| dval_sv | 0 | 0 | 0 | 0 to 0 |

Ranking by total index with cumulative share of the summed totals; a variable is incidental on this outcome if the upper end of its total-index interval is below 2%. Incidental here: inequality (1, interval 0 to 2), concentration (1, interval 0 to 2), reconf_time (1, interval 0 to 2), auth_cred (1, interval 0 to 2), manual_delay (1, interval 0 to 1), cap_spread (1, interval 0 to 1), cap_drift (1, interval 0 to 1), vpn (0, interval 0 to 1), supplied_a (0, interval 0 to 1), stage_time (0, interval 0 to 1), ep_sv (0, interval 0 to 1), node_reconf (0, interval 0 to 0), exfil_p (0, interval 0 to 0), objective (0, interval 0 to 0), managed (0, interval 0 to 0), dval_sv (0, interval 0 to 0). Their summed totals, the bound on the variance the pair pass cannot see on this outcome: 8%. A variable incidental on every reported outcome is left out of the pair pass; the kept set is the union over outcomes.

| rank | variable | total | share of totals | cumulative |
|---|---|---|---|---|
| 1 | iface_closed | 38 | 13 | 13 |
| 2 | coverage | 18 | 6 | 19 |
| 3 | x_rate | 17 | 6 | 24 |
| 4 | server_share | 17 | 6 | 30 |
| 5 | n_chan | 15 | 5 | 35 |
| 6 | atk_cap | 15 | 5 | 40 |
| 7 | ext_total | 15 | 5 | 45 |
| 8 | n_ext | 13 | 4 | 49 |
| 9 | ext_auth | 10 | 3 | 53 |
| 10 | a_rate | 10 | 3 | 56 |
| 11 | size | 9 | 3 | 59 |
| 12 | chan_span | 9 | 3 | 62 |
| 13 | ext_share | 8 | 3 | 65 |
| 14 | ext_exploit | 8 | 3 | 67 |
| 15 | ext_bad | 8 | 3 | 70 |
| 16 | cloud_share | 8 | 3 | 73 |
| 17 | def_cap | 7 | 2 | 75 |
| 18 | chan_cov | 7 | 2 | 77 |
| 19 | rebuild_time | 6 | 2 | 79 |
| 20 | atk_budget | 5 | 2 | 81 |
| 21 | t_cut | 4 | 1 | 82 |
| 22 | seg_ep | 4 | 1 | 84 |
| 23 | seg_sv | 4 | 1 | 85 |
| 24 | zone_conn | 3 | 1 | 86 |
| 25 | payload_delay | 3 | 1 | 87 |
| 26 | blind_delay | 3 | 1 | 88 |
| 27 | chan | 3 | 1 | 89 |
| 28 | dose | 3 | 1 | 90 |
| 29 | supplied_x | 3 | 1 | 91 |
| 30 | tac_budget | 3 | 1 | 92 |
| 31 | theta | 2 | 1 | 93 |
| 32 | remote_share | 2 | 1 | 93 |
| 33 | retool | 2 | 1 | 94 |
| 34 | visibility | 2 | 1 | 95 |
| 35 | c_s | 2 | 1 | 95 |
| 36 | redundancy | 2 | 1 | 96 |
| 37 | t_clean | 1 | 0 | 96 |
| 38 | ep_conn | 1 | 0 | 97 |
| 39 | fanout | 1 | 0 | 97 |
| 40 | queue_order | 1 | 0 | 98 |
| 41 | inequality | 1 | 0 | 98 |
| 42 | concentration | 1 | 0 | 98 |
| 43 | reconf_time | 1 | 0 | 98 |
| 44 | auth_cred | 1 | 0 | 99 |
| 45 | manual_delay | 1 | 0 | 99 |
| 46 | cap_spread | 1 | 0 | 99 |
| 47 | cap_drift | 1 | 0 | 99 |
| 48 | vpn | 0 | 0 | 100 |
| 49 | supplied_a | 0 | 0 | 100 |
| 50 | stage_time | 0 | 0 | 100 |
| 51 | ep_sv | 0 | 0 | 100 |
| 52 | node_reconf | 0 | 0 | 100 |
| 53 | exfil_p | 0 | 0 | 100 |
| 54 | objective | 0 | 0 | 100 |
| 55 | managed | 0 | 0 | 100 |
| 56 | dval_sv | 0 | 0 | 100 |

| pair | joint first-order | pair interaction term | 95% interval (joint) |
|---|---|---|---|
| iface_closed+coverage | 6 | 9 | -9 to 22 |
| cloud_share+size | -2 | 7 | -7 to 3 |
| server_share+size | 0 | 7 | -8 to 8 |
| x_rate+size | -0 | 6 | -10 to 9 |
| ext_auth+ext_bad | -5 | 6 | -16 to 5 |
| ext_auth+n_ext | -2 | 5 | -10 to 6 |
| ext_total+ext_bad | -2 | 5 | -14 to 8 |
| size+seg_sv | -3 | 5 | -11 to 3 |
| ext_auth+size | -5 | 5 | -13 to 2 |
| atk_budget+remote_share | 2 | 5 | -6 to 9 |
| server_share+supplied_x | 3 | 5 | -4 to 11 |
| zone_conn+supplied_x | 2 | 4 | 0 to 4 |
| seg_ep+cloud_share | -1 | 4 | -4 to 2 |
| atk_budget+supplied_x | -1 | 4 | -6 to 2 |
| atk_budget+ext_share | 2 | 4 | -4 to 9 |

Response surface fitted to all 291584 sampled configurations. Pairwise terms only: R2 86% in sample, -51% on a held-out fifth. Too few points for the three-way terms; pairs only. Groups derived by clustering the variables on the surface's pairwise terms: 2 groups (silhouette 0.05), holding 96% of the interaction mass within groups.

| derived group | members |
|---|---|
| group:iface_closed | iface_closed, a_rate, atk_cap, t_cut, tac_budget, zone_conn, def_cap, chan_cov, x_rate, ext_auth, coverage, ext_exploit, atk_budget, ext_total, n_chan, blind_delay, payload_delay, manual_delay, chan_span, remote_share, ext_bad, cloud_share, server_share, t_clean, size, stage_time, concentration, redundancy, seg_sv, supplied_a, dose, rebuild_time, supplied_x, visibility, chan, vpn, cap_spread, auth_cred, cap_drift, c_s, reconf_time, inequality, node_reconf, retool, ep_sv, exfil_p, managed, ext_share, queue_order, ep_conn, n_ext, objective, theta, dval_sv |
| group:fanout | seg_ep, fanout |

| group term (on the surface) | first-order | total | interaction term |
|---|---|---|---|
| group:iface_closed | 99 | 100 | 1 |
| group:fanout | 0 | 1 | 1 |
| group:iface_closed+group:fanout | 100 | 100 | 1 |

### data loss (variance 0.0299)

| term | first-order | total | interaction share | 95% interval (first-order) |
|---|---|---|---|---|
| objective | 25 | 52 | 27 | 11 to 40 |
| exfil_p | 7 | 35 | 28 | 0 to 15 |
| iface_closed | 6 | 19 | 12 | 1 to 15 |
| ext_exploit | -1 | 11 | 12 | -4 to 2 |
| node_reconf | 4 | 11 | 6 | -0 to 10 |
| n_ext | -5 | 10 | 16 | -15 to 1 |
| server_share | -2 | 10 | 12 | -6 to 2 |
| ext_total | 3 | 8 | 6 | -0 to 7 |
| atk_cap | -1 | 7 | 8 | -4 to 2 |
| a_rate | 4 | 7 | 3 | 1 to 8 |
| x_rate | 1 | 6 | 6 | -1 to 3 |
| ext_auth | 1 | 6 | 5 | -4 to 6 |
| ext_bad | -4 | 6 | 10 | -12 to 1 |
| ext_share | 1 | 4 | 4 | -1 to 2 |
| coverage | 1 | 4 | 3 | -3 to 4 |
| manual_delay | 1 | 3 | 2 | -1 to 2 |
| def_cap | 1 | 2 | 1 | -1 to 4 |
| n_chan | -3 | 2 | 5 | -6 to -0 |
| dose | 0 | 2 | 2 | -0 to 1 |
| size | -0 | 2 | 2 | -2 to 1 |
| payload_delay | 0 | 2 | 2 | -1 to 1 |
| remote_share | 1 | 2 | 1 | -2 to 5 |
| reconf_time | 2 | 2 | -0 | 0 to 4 |
| retool | 1 | 2 | 1 | -1 to 2 |
| cloud_share | -2 | 2 | 3 | -4 to 0 |
| zone_conn | 1 | 1 | 0 | 0 to 2 |
| chan_span | 0 | 1 | 1 | -1 to 2 |
| rebuild_time | -1 | 1 | 2 | -2 to 1 |
| blind_delay | 2 | 1 | -1 | 0 to 5 |
| seg_ep | -0 | 1 | 1 | -1 to 1 |
| chan_cov | -1 | 1 | 2 | -2 to 0 |
| atk_budget | -0 | 1 | 1 | -3 to 2 |
| t_cut | 0 | 1 | 1 | -1 to 1 |
| visibility | -2 | 1 | 3 | -4 to -1 |
| t_clean | 0 | 1 | 1 | -1 to 1 |
| ep_sv | 0 | 1 | 0 | -0 to 1 |
| tac_budget | 0 | 1 | 0 | -1 to 2 |
| seg_sv | 0 | 1 | 0 | -0 to 1 |
| cap_drift | -0 | 1 | 1 | -2 to 1 |
| fanout | 1 | 0 | -0 | -1 to 2 |
| supplied_x | 0 | 0 | 0 | -0 to 1 |
| stage_time | 0 | 0 | 0 | -0 to 0 |
| dval_sv | -0 | 0 | 0 | -1 to 1 |
| cap_spread | 0 | 0 | 0 | -1 to 1 |
| c_s | -0 | 0 | 0 | -1 to 1 |
| concentration | 0 | 0 | 0 | -0 to 1 |
| redundancy | -1 | 0 | 2 | -4 to 0 |
| supplied_a | -0 | 0 | 0 | -1 to 1 |
| auth_cred | 0 | 0 | 0 | -0 to 0 |
| theta | -0 | 0 | 1 | -1 to 0 |
| inequality | -0 | 0 | 1 | -1 to 0 |
| queue_order | -1 | 0 | 1 | -2 to 0 |
| chan | 0 | 0 | 0 | -0 to 1 |
| ep_conn | -0 | 0 | 1 | -2 to 1 |
| vpn | -0 | 0 | 0 | -1 to -0 |
| managed | -0 | 0 | 0 | -0 to 0 |

Ranking by total index with cumulative share of the summed totals; a variable is incidental on this outcome if the upper end of its total-index interval is below 2%. Incidental here: rebuild_time (1, interval 0 to 2), blind_delay (1, interval 0 to 2), seg_ep (1, interval 1 to 2), chan_cov (1, interval 0 to 2), atk_budget (1, interval 0 to 2), visibility (1, interval 0 to 2), tac_budget (1, interval 0 to 1), seg_sv (1, interval 0 to 1), cap_drift (1, interval 0 to 1), fanout (0, interval 0 to 1), supplied_x (0, interval 0 to 1), stage_time (0, interval 0 to 1), dval_sv (0, interval 0 to 1), cap_spread (0, interval 0 to 1), c_s (0, interval 0 to 1), concentration (0, interval 0 to 1), redundancy (0, interval 0 to 1), supplied_a (0, interval 0 to 1), auth_cred (0, interval 0 to 1), theta (0, interval 0 to 1), inequality (0, interval 0 to 0), queue_order (0, interval 0 to 0), chan (0, interval 0 to 0), ep_conn (0, interval 0 to 0), vpn (0, interval 0 to 0), managed (0, interval 0 to 0). Their summed totals, the bound on the variance the pair pass cannot see on this outcome: 13%. A variable incidental on every reported outcome is left out of the pair pass; the kept set is the union over outcomes.

| rank | variable | total | share of totals | cumulative |
|---|---|---|---|---|
| 1 | objective | 52 | 22 | 22 |
| 2 | exfil_p | 35 | 15 | 37 |
| 3 | iface_closed | 19 | 8 | 45 |
| 4 | ext_exploit | 11 | 5 | 50 |
| 5 | node_reconf | 11 | 5 | 54 |
| 6 | n_ext | 10 | 4 | 58 |
| 7 | server_share | 10 | 4 | 63 |
| 8 | ext_total | 8 | 3 | 66 |
| 9 | atk_cap | 7 | 3 | 69 |
| 10 | a_rate | 7 | 3 | 72 |
| 11 | x_rate | 6 | 3 | 74 |
| 12 | ext_auth | 6 | 3 | 77 |
| 13 | ext_bad | 6 | 3 | 80 |
| 14 | ext_share | 4 | 2 | 82 |
| 15 | coverage | 4 | 2 | 83 |
| 16 | manual_delay | 3 | 1 | 84 |
| 17 | def_cap | 2 | 1 | 85 |
| 18 | n_chan | 2 | 1 | 86 |
| 19 | dose | 2 | 1 | 87 |
| 20 | size | 2 | 1 | 88 |
| 21 | payload_delay | 2 | 1 | 89 |
| 22 | remote_share | 2 | 1 | 90 |
| 23 | reconf_time | 2 | 1 | 91 |
| 24 | retool | 2 | 1 | 91 |
| 25 | cloud_share | 2 | 1 | 92 |
| 26 | zone_conn | 1 | 1 | 93 |
| 27 | chan_span | 1 | 1 | 93 |
| 28 | rebuild_time | 1 | 0 | 94 |
| 29 | blind_delay | 1 | 0 | 94 |
| 30 | seg_ep | 1 | 0 | 95 |
| 31 | chan_cov | 1 | 0 | 95 |
| 32 | atk_budget | 1 | 0 | 95 |
| 33 | t_cut | 1 | 0 | 96 |
| 34 | visibility | 1 | 0 | 96 |
| 35 | t_clean | 1 | 0 | 97 |
| 36 | ep_sv | 1 | 0 | 97 |
| 37 | tac_budget | 1 | 0 | 97 |
| 38 | seg_sv | 1 | 0 | 98 |
| 39 | cap_drift | 1 | 0 | 98 |
| 40 | fanout | 0 | 0 | 98 |
| 41 | supplied_x | 0 | 0 | 98 |
| 42 | stage_time | 0 | 0 | 98 |
| 43 | dval_sv | 0 | 0 | 99 |
| 44 | cap_spread | 0 | 0 | 99 |
| 45 | c_s | 0 | 0 | 99 |
| 46 | concentration | 0 | 0 | 99 |
| 47 | redundancy | 0 | 0 | 99 |
| 48 | supplied_a | 0 | 0 | 99 |
| 49 | auth_cred | 0 | 0 | 99 |
| 50 | theta | 0 | 0 | 100 |
| 51 | inequality | 0 | 0 | 100 |
| 52 | queue_order | 0 | 0 | 100 |
| 53 | chan | 0 | 0 | 100 |
| 54 | ep_conn | 0 | 0 | 100 |
| 55 | vpn | 0 | 0 | 100 |
| 56 | managed | 0 | 0 | 100 |

| pair | joint first-order | pair interaction term | 95% interval (joint) |
|---|---|---|---|
| exfil_p+objective | 38 | 6 | 19 to 59 |
| atk_cap+server_share | 2 | 5 | -3 to 7 |
| node_reconf+objective | 33 | 5 | 18 to 50 |
| iface_closed+objective | 35 | 4 | 21 to 53 |
| remote_share+objective | 30 | 4 | 14 to 47 |
| x_rate+objective | 29 | 4 | 15 to 46 |
| x_rate+blind_delay | 7 | 4 | -0 to 19 |
| iface_closed+x_rate | 11 | 4 | 0 to 28 |
| ext_total+exfil_p | 13 | 3 | 3 to 23 |
| atk_cap+objective | 26 | 3 | 10 to 45 |
| atk_cap+x_rate | 2 | 3 | -2 to 7 |
| atk_cap+redundancy | 0 | 3 | -4 to 5 |
| iface_closed+ext_bad | 5 | 2 | -1 to 13 |
| cloud_share+exfil_p | 8 | 2 | -0 to 18 |
| a_rate+zone_conn | 7 | 2 | 2 to 14 |

Response surface fitted to all 291584 sampled configurations. Pairwise terms only: R2 87% in sample, -36% on a held-out fifth. Too few points for the three-way terms; pairs only. Groups derived by clustering the variables on the surface's pairwise terms: 2 groups (silhouette 0.04), holding 98% of the interaction mass within groups.

| derived group | members |
|---|---|
| group:objective | iface_closed, a_rate, atk_cap, t_cut, tac_budget, zone_conn, def_cap, chan_cov, x_rate, ext_auth, coverage, ext_exploit, atk_budget, ext_total, n_chan, blind_delay, payload_delay, manual_delay, chan_span, remote_share, ext_bad, seg_ep, cloud_share, server_share, t_clean, size, stage_time, concentration, fanout, redundancy, seg_sv, supplied_a, dose, rebuild_time, visibility, chan, vpn, cap_spread, auth_cred, cap_drift, c_s, reconf_time, inequality, node_reconf, retool, ep_sv, exfil_p, managed, ext_share, queue_order, ep_conn, n_ext, objective, theta, dval_sv |
| group:supplied_x | supplied_x |

| group term (on the surface) | first-order | total | interaction term |
|---|---|---|---|
| group:objective | 99 | 100 | 0 |
| group:supplied_x | 0 | 1 | 0 |
| group:objective+group:supplied_x | 100 | 100 | 0 |

### service loss (variance 0.0325)

| term | first-order | total | interaction share | 95% interval (first-order) |
|---|---|---|---|---|
| iface_closed | 22 | 37 | 15 | 11 to 34 |
| x_rate | 10 | 22 | 11 | 3 to 20 |
| a_rate | 7 | 21 | 14 | -0 to 15 |
| server_share | 1 | 13 | 12 | -5 to 6 |
| atk_cap | 6 | 12 | 6 | -0 to 13 |
| ext_exploit | 3 | 11 | 9 | -3 to 8 |
| coverage | 1 | 10 | 9 | -5 to 6 |
| ext_share | 3 | 8 | 5 | -3 to 11 |
| ext_total | 7 | 7 | -0 | 1 to 13 |
| ext_auth | 9 | 6 | -3 | 0 to 19 |
| n_chan | -1 | 5 | 6 | -5 to 4 |
| ext_bad | 6 | 5 | -1 | -2 to 16 |
| def_cap | 2 | 5 | 3 | -1 to 6 |
| n_ext | 2 | 4 | 2 | -4 to 7 |
| remote_share | 2 | 4 | 2 | 0 to 4 |
| tac_budget | -0 | 4 | 4 | -6 to 5 |
| size | -0 | 3 | 3 | -4 to 3 |
| blind_delay | -1 | 3 | 4 | -5 to 3 |
| retool | 0 | 3 | 3 | -1 to 2 |
| t_cut | 0 | 3 | 2 | -3 to 4 |
| payload_delay | 2 | 3 | 1 | -2 to 7 |
| chan_cov | 2 | 2 | 0 | -1 to 6 |
| cloud_share | 2 | 2 | 0 | 0 to 4 |
| chan_span | -0 | 2 | 3 | -3 to 3 |
| dose | 3 | 2 | -1 | -0 to 7 |
| reconf_time | 1 | 2 | 1 | -2 to 5 |
| rebuild_time | 2 | 2 | -0 | -1 to 5 |
| auth_cred | 2 | 2 | 0 | -2 to 5 |
| seg_ep | 3 | 2 | -1 | 0 to 5 |
| seg_sv | -1 | 1 | 2 | -2 to 1 |
| atk_budget | 0 | 1 | 1 | -2 to 2 |
| visibility | -0 | 1 | 1 | -2 to 2 |
| zone_conn | 0 | 1 | 1 | -1 to 2 |
| ep_conn | 1 | 1 | -1 | -0 to 5 |
| manual_delay | 1 | 1 | -0 | -0 to 2 |
| queue_order | 0 | 1 | 0 | -0 to 1 |
| cap_drift | 1 | 1 | -0 | -1 to 3 |
| fanout | 1 | 1 | -0 | -0 to 2 |
| c_s | -2 | 1 | 2 | -4 to -0 |
| chan | 1 | 1 | -0 | -1 to 3 |
| supplied_x | 1 | 1 | -1 | 0 to 3 |
| redundancy | 1 | 0 | -1 | -0 to 2 |
| theta | -1 | 0 | 1 | -2 to -0 |
| stage_time | 0 | 0 | -0 | -1 to 1 |
| inequality | 0 | 0 | -0 | -0 to 1 |
| t_clean | -0 | 0 | 0 | -1 to 1 |
| cap_spread | -0 | 0 | 1 | -1 to 0 |
| concentration | 0 | 0 | -0 | -0 to 1 |
| supplied_a | 0 | 0 | -0 | -0 to 1 |
| ep_sv | -1 | 0 | 1 | -1 to -0 |
| objective | -0 | 0 | 0 | -1 to 0 |
| node_reconf | -0 | 0 | 0 | -0 to 0 |
| vpn | 0 | 0 | -0 | -0 to 1 |
| exfil_p | 0 | 0 | -0 | 0 to 1 |
| managed | 0 | 0 | -0 | -0 to 0 |
| dval_sv | -0 | 0 | 0 | -0 to 0 |

Ranking by total index with cumulative share of the summed totals; a variable is incidental on this outcome if the upper end of its total-index interval is below 2%. Incidental here: atk_budget (1, interval 1 to 2), visibility (1, interval 0 to 2), zone_conn (1, interval 0 to 2), ep_conn (1, interval 0 to 2), manual_delay (1, interval 0 to 1), queue_order (1, interval 0 to 2), cap_drift (1, interval 0 to 1), fanout (1, interval 0 to 1), c_s (1, interval 0 to 1), chan (1, interval 0 to 1), supplied_x (1, interval 0 to 1), redundancy (0, interval 0 to 1), theta (0, interval 0 to 1), stage_time (0, interval 0 to 0), inequality (0, interval 0 to 0), t_clean (0, interval 0 to 0), cap_spread (0, interval 0 to 0), concentration (0, interval 0 to 0), supplied_a (0, interval 0 to 0), ep_sv (0, interval 0 to 0), objective (0, interval 0 to 0), node_reconf (0, interval 0 to 0), vpn (0, interval 0 to 0), exfil_p (0, interval 0 to 0), managed (0, interval 0 to 0), dval_sv (0, interval 0 to 0). Their summed totals, the bound on the variance the pair pass cannot see on this outcome: 11%. A variable incidental on every reported outcome is left out of the pair pass; the kept set is the union over outcomes.

| rank | variable | total | share of totals | cumulative |
|---|---|---|---|---|
| 1 | iface_closed | 37 | 17 | 17 |
| 2 | x_rate | 22 | 10 | 27 |
| 3 | a_rate | 21 | 10 | 37 |
| 4 | server_share | 13 | 6 | 43 |
| 5 | atk_cap | 12 | 5 | 48 |
| 6 | ext_exploit | 11 | 5 | 54 |
| 7 | coverage | 10 | 5 | 58 |
| 8 | ext_share | 8 | 4 | 62 |
| 9 | ext_total | 7 | 3 | 65 |
| 10 | ext_auth | 6 | 3 | 68 |
| 11 | n_chan | 5 | 2 | 70 |
| 12 | ext_bad | 5 | 2 | 72 |
| 13 | def_cap | 5 | 2 | 75 |
| 14 | n_ext | 4 | 2 | 77 |
| 15 | remote_share | 4 | 2 | 79 |
| 16 | tac_budget | 4 | 2 | 80 |
| 17 | size | 3 | 1 | 82 |
| 18 | blind_delay | 3 | 1 | 83 |
| 19 | retool | 3 | 1 | 84 |
| 20 | t_cut | 3 | 1 | 86 |
| 21 | payload_delay | 3 | 1 | 87 |
| 22 | chan_cov | 2 | 1 | 88 |
| 23 | cloud_share | 2 | 1 | 89 |
| 24 | chan_span | 2 | 1 | 90 |
| 25 | dose | 2 | 1 | 91 |
| 26 | reconf_time | 2 | 1 | 92 |
| 27 | rebuild_time | 2 | 1 | 93 |
| 28 | auth_cred | 2 | 1 | 93 |
| 29 | seg_ep | 2 | 1 | 94 |
| 30 | seg_sv | 1 | 1 | 95 |
| 31 | atk_budget | 1 | 0 | 95 |
| 32 | visibility | 1 | 0 | 96 |
| 33 | zone_conn | 1 | 0 | 96 |
| 34 | ep_conn | 1 | 0 | 97 |
| 35 | manual_delay | 1 | 0 | 97 |
| 36 | queue_order | 1 | 0 | 97 |
| 37 | cap_drift | 1 | 0 | 98 |
| 38 | fanout | 1 | 0 | 98 |
| 39 | c_s | 1 | 0 | 98 |
| 40 | chan | 1 | 0 | 99 |
| 41 | supplied_x | 1 | 0 | 99 |
| 42 | redundancy | 0 | 0 | 99 |
| 43 | theta | 0 | 0 | 99 |
| 44 | stage_time | 0 | 0 | 99 |
| 45 | inequality | 0 | 0 | 100 |
| 46 | t_clean | 0 | 0 | 100 |
| 47 | cap_spread | 0 | 0 | 100 |
| 48 | concentration | 0 | 0 | 100 |
| 49 | supplied_a | 0 | 0 | 100 |
| 50 | ep_sv | 0 | 0 | 100 |
| 51 | objective | 0 | 0 | 100 |
| 52 | node_reconf | 0 | 0 | 100 |
| 53 | vpn | 0 | 0 | 100 |
| 54 | exfil_p | 0 | 0 | 100 |
| 55 | managed | 0 | 0 | 100 |
| 56 | dval_sv | 0 | 0 | 100 |

| pair | joint first-order | pair interaction term | 95% interval (joint) |
|---|---|---|---|
| iface_closed+coverage | 30 | 7 | 15 to 46 |
| reconf_time+retool | 6 | 5 | -0 to 14 |
| atk_cap+server_share | 11 | 4 | 1 to 21 |
| ext_auth+n_ext | 14 | 3 | 4 to 28 |
| coverage+ext_total | 11 | 3 | 2 to 20 |
| coverage+n_ext | 6 | 3 | -3 to 14 |
| ext_auth+coverage | 12 | 3 | 2 to 25 |
| a_rate+x_rate | 20 | 3 | 7 to 34 |
| x_rate+server_share | 14 | 3 | 4 to 26 |
| t_cut+server_share | 4 | 3 | -2 to 10 |
| a_rate+ext_auth | 17 | 2 | 5 to 32 |
| size+c_s | 0 | 2 | -3 to 3 |
| t_cut+ext_share | 6 | 2 | -1 to 14 |
| ext_auth+ext_exploit | 13 | 2 | 3 to 25 |
| iface_closed+payload_delay | 26 | 2 | 13 to 40 |

Response surface fitted to all 291584 sampled configurations. Pairwise terms only: R2 90% in sample, -17% on a held-out fifth. Too few points for the three-way terms; pairs only. Groups derived by clustering the variables on the surface's pairwise terms: 2 groups (silhouette 0.04), holding 92% of the interaction mass within groups.

| derived group | members |
|---|---|
| group:iface_closed | iface_closed, a_rate, atk_cap, t_cut, tac_budget, zone_conn, def_cap, chan_cov, x_rate, ext_auth, coverage, ext_exploit, atk_budget, ext_total, n_chan, blind_delay, payload_delay, manual_delay, chan_span, remote_share, ext_bad, seg_ep, cloud_share, server_share, t_clean, size, stage_time, concentration, redundancy, supplied_a, dose, rebuild_time, supplied_x, visibility, chan, vpn, cap_spread, auth_cred, cap_drift, c_s, reconf_time, inequality, retool, ep_sv, exfil_p, managed, ext_share, queue_order, ep_conn, n_ext, theta, dval_sv |
| group:seg_sv | fanout, seg_sv, node_reconf, objective |

| group term (on the surface) | first-order | total | interaction term |
|---|---|---|---|
| group:iface_closed | 97 | 99 | 1 |
| group:seg_sv | 0 | 2 | 2 |
| group:iface_closed+group:seg_sv | 100 | 99 | 2 |
