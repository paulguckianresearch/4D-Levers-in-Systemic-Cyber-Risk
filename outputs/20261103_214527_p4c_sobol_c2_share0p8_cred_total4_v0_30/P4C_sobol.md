# Paper 4C global sensitivity: Sobol indices (PhDPaper4C v1.1 (2026-11-05, surface validation for Paper 4D; model as v0.26/v0.27)) - stratum {'cred_total': 4, 'c2_share': 0.8}

Base sample N = 256, Latin hypercube on each variable's ladder; each configuration on wirings [6801, 6802] and seeds [6901, 6902]. First-order index: the share of the outcome's variance a variable explains alone. Total index: the share it explains alone or with others; the difference is its interaction share. A pair's term is the variance the two explain together beyond what each explains alone. Groups are not set in advance: a response surface is fitted to every sampled point and the variables are clustered by the size of their pairwise terms, so a group is a set of levers that act together in the data. Group, group-pair and group-triple terms are then computed on that surface. Intervals: 95% bootstrap over the sample. Variables not sampled sit at the register's neutral value.

## intrusion

### collapse (variance 0.1803)

| term | first-order | total | interaction share | 95% interval (first-order) |
|---|---|---|---|---|
| iface_closed | 21 | 41 | 20 | 4 to 38 |
| server_share | 7 | 33 | 26 | -5 to 19 |
| ext_auth | 5 | 16 | 11 | -4 to 14 |
| a_rate | 5 | 15 | 10 | -1 to 12 |
| cloud_share | 5 | 15 | 11 | -3 to 14 |
| size | 4 | 15 | 11 | -4 to 12 |
| n_ext | 7 | 14 | 7 | 0 to 17 |
| ext_total | 0 | 14 | 14 | -7 to 7 |
| x_rate | 3 | 13 | 11 | -1 to 8 |
| chan_cov | 3 | 12 | 9 | -4 to 10 |
| atk_cap | 3 | 12 | 9 | -2 to 9 |
| ext_exploit | -2 | 12 | 14 | -9 to 4 |
| n_chan | 4 | 11 | 7 | -3 to 12 |
| ext_bad | 7 | 11 | 4 | -3 to 17 |
| ext_share | -0 | 10 | 10 | -4 to 4 |
| remote_share | 3 | 10 | 7 | -2 to 8 |
| coverage | 2 | 9 | 7 | -5 to 11 |
| def_cap | -1 | 8 | 9 | -7 to 3 |
| chan_span | 3 | 8 | 5 | -4 to 10 |
| seg_sv | -2 | 7 | 9 | -7 to 3 |
| theta | 2 | 5 | 3 | -4 to 7 |
| blind_delay | -3 | 4 | 7 | -8 to 1 |
| node_reconf | -1 | 4 | 5 | -6 to 2 |
| payload_delay | -1 | 4 | 5 | -4 to 1 |
| zone_conn | -1 | 4 | 5 | -4 to 2 |
| seg_ep | 3 | 4 | 1 | -1 to 7 |
| atk_budget | -1 | 4 | 5 | -4 to 1 |
| cap_drift | -2 | 4 | 5 | -5 to 0 |
| cloud_link | -1 | 3 | 4 | -2 to 0 |
| ctl_link | 0 | 3 | 2 | -3 to 5 |
| retool | 2 | 3 | 1 | -1 to 5 |
| tac_budget | -0 | 3 | 3 | -3 to 2 |
| chan | 2 | 3 | 1 | -1 to 5 |
| supplied_x | 0 | 2 | 2 | -2 to 3 |
| redundancy | 2 | 2 | 0 | -0 to 4 |
| rebuild_time | -2 | 2 | 4 | -5 to 1 |
| fanout | -2 | 2 | 4 | -5 to -0 |
| reconf_time | -1 | 2 | 3 | -7 to 3 |
| visibility | 0 | 2 | 2 | -2 to 2 |
| manual_delay | 0 | 2 | 2 | -2 to 2 |
| obs_interval | 0 | 1 | 1 | -2 to 2 |
| queue_order | 1 | 1 | 1 | 0 to 2 |
| t_clean | -1 | 1 | 3 | -4 to 0 |
| dns | 2 | 1 | -1 | 0 to 5 |
| stage_time | -1 | 1 | 2 | -3 to 0 |
| concentration | -1 | 1 | 2 | -2 to 0 |
| auth_cred | -1 | 1 | 2 | -2 to 0 |
| rate_var | -1 | 1 | 2 | -3 to 0 |
| ep_sv | 0 | 1 | 1 | 0 to 0 |
| cap_spread | -1 | 1 | 1 | -2 to 1 |
| managed | -0 | 1 | 1 | -3 to 1 |
| objective | 1 | 1 | -0 | 0 to 2 |
| ep_conn | 0 | 1 | 1 | 0 to 0 |
| exfil_p | -1 | 0 | 1 | -2 to 0 |
| vpn | 0 | 0 | 0 | 0 to 0 |
| t_cut | 0 | 0 | 0 | 0 to 0 |
| c_s | 0 | 0 | 0 | 0 to 0 |
| dval_sv | 0 | 0 | 0 | 0 to 0 |

Ranking by total index with cumulative share of the summed totals; a variable is incidental on this outcome if the upper end of its total-index interval is below 2%. Incidental here: concentration (1, interval 0 to 2), rate_var (1, interval 0 to 2), ep_sv (1, interval 0 to 2), cap_spread (1, interval 0 to 1), managed (1, interval 0 to 1), objective (1, interval 0 to 1), ep_conn (1, interval 0 to 1), exfil_p (0, interval 0 to 1), vpn (0, interval 0 to 0), t_cut (0, interval 0 to 0), c_s (0, interval 0 to 0), dval_sv (0, interval 0 to 0). Their summed totals, the bound on the variance the pair pass cannot see on this outcome: 6%. A variable incidental on every reported outcome is left out of the pair pass; the kept set is the union over outcomes.

| rank | variable | total | share of totals | cumulative |
|---|---|---|---|---|
| 1 | iface_closed | 41 | 11 | 11 |
| 2 | server_share | 33 | 9 | 20 |
| 3 | ext_auth | 16 | 5 | 25 |
| 4 | a_rate | 15 | 4 | 29 |
| 5 | cloud_share | 15 | 4 | 33 |
| 6 | size | 15 | 4 | 38 |
| 7 | n_ext | 14 | 4 | 42 |
| 8 | ext_total | 14 | 4 | 46 |
| 9 | x_rate | 13 | 4 | 49 |
| 10 | chan_cov | 12 | 3 | 53 |
| 11 | atk_cap | 12 | 3 | 56 |
| 12 | ext_exploit | 12 | 3 | 59 |
| 13 | n_chan | 11 | 3 | 62 |
| 14 | ext_bad | 11 | 3 | 65 |
| 15 | ext_share | 10 | 3 | 68 |
| 16 | remote_share | 10 | 3 | 71 |
| 17 | coverage | 9 | 3 | 73 |
| 18 | def_cap | 8 | 2 | 76 |
| 19 | chan_span | 8 | 2 | 78 |
| 20 | seg_sv | 7 | 2 | 80 |
| 21 | theta | 5 | 1 | 81 |
| 22 | blind_delay | 4 | 1 | 82 |
| 23 | node_reconf | 4 | 1 | 83 |
| 24 | payload_delay | 4 | 1 | 85 |
| 25 | zone_conn | 4 | 1 | 86 |
| 26 | seg_ep | 4 | 1 | 87 |
| 27 | atk_budget | 4 | 1 | 88 |
| 28 | cap_drift | 4 | 1 | 89 |
| 29 | cloud_link | 3 | 1 | 89 |
| 30 | ctl_link | 3 | 1 | 90 |
| 31 | retool | 3 | 1 | 91 |
| 32 | tac_budget | 3 | 1 | 92 |
| 33 | chan | 3 | 1 | 92 |
| 34 | supplied_x | 2 | 1 | 93 |
| 35 | redundancy | 2 | 1 | 94 |
| 36 | rebuild_time | 2 | 1 | 94 |
| 37 | fanout | 2 | 1 | 95 |
| 38 | reconf_time | 2 | 1 | 95 |
| 39 | visibility | 2 | 0 | 96 |
| 40 | manual_delay | 2 | 0 | 96 |
| 41 | obs_interval | 1 | 0 | 97 |
| 42 | queue_order | 1 | 0 | 97 |
| 43 | t_clean | 1 | 0 | 97 |
| 44 | dns | 1 | 0 | 98 |
| 45 | stage_time | 1 | 0 | 98 |
| 46 | concentration | 1 | 0 | 98 |
| 47 | auth_cred | 1 | 0 | 99 |
| 48 | rate_var | 1 | 0 | 99 |
| 49 | ep_sv | 1 | 0 | 99 |
| 50 | cap_spread | 1 | 0 | 99 |
| 51 | managed | 1 | 0 | 100 |
| 52 | objective | 1 | 0 | 100 |
| 53 | ep_conn | 1 | 0 | 100 |
| 54 | exfil_p | 0 | 0 | 100 |
| 55 | vpn | 0 | 0 | 100 |
| 56 | t_cut | 0 | 0 | 100 |
| 57 | c_s | 0 | 0 | 100 |
| 58 | dval_sv | 0 | 0 | 100 |

| pair | joint first-order | pair interaction term | 95% interval (joint) |
|---|---|---|---|
| n_chan+seg_sv | 8 | 5 | 0 to 16 |
| iface_closed+x_rate | 28 | 5 | 9 to 47 |
| cloud_share+size | 13 | 4 | 3 to 24 |
| x_rate+coverage | 9 | 4 | 0 to 20 |
| coverage+ext_share | 6 | 4 | -3 to 16 |
| atk_cap+cap_drift | 5 | 4 | -1 to 12 |
| x_rate+seg_sv | 4 | 4 | -3 to 13 |
| theta+size | 9 | 4 | 1 to 19 |
| seg_sv+fanout | -1 | 4 | -7 to 5 |
| seg_sv+cap_drift | -0 | 4 | -6 to 5 |
| theta+ctl_link | 5 | 4 | -2 to 15 |
| atk_cap+seg_sv | 4 | 3 | -3 to 12 |
| server_share+ext_total | 10 | 3 | -4 to 23 |
| iface_closed+zone_conn | 23 | 3 | 6 to 41 |
| atk_budget+t_clean | 0 | 3 | -3 to 4 |

Response surface fitted to all 316416 sampled configurations. Pairwise terms only: R2 84% in sample, -19% on a held-out fifth. Too few points for the three-way terms; pairs only. Groups derived by clustering the variables on the surface's pairwise terms: 2 groups (silhouette 0.08), holding 98% of the interaction mass within groups.

| derived group | members |
|---|---|
| group:iface_closed | server_share, a_rate, iface_closed, atk_cap, tac_budget, ext_exploit, manual_delay, x_rate, chan_cov, ext_auth, coverage, zone_conn, remote_share, ext_total, n_chan, chan_span, theta, seg_sv, cloud_share, atk_budget, t_cut, n_ext, ep_conn, node_reconf, blind_delay, supplied_x, chan, payload_delay, visibility, retool, size, rebuild_time, ext_bad, fanout, ctl_link, ext_share, t_clean, def_cap, c_s, concentration, dns, cap_drift, rate_var, vpn, auth_cred, seg_ep, stage_time, cloud_link, ep_sv, queue_order, cap_spread, managed, reconf_time, obs_interval, exfil_p, objective, dval_sv |
| group:redundancy | redundancy |

| group term (on the surface) | first-order | total | interaction term |
|---|---|---|---|
| group:iface_closed | 100 | 101 | 0 |
| group:redundancy | 0 | 1 | 0 |
| group:iface_closed+group:redundancy | 101 | 101 | 0 |

### data loss (variance 0.0299)

| term | first-order | total | interaction share | 95% interval (first-order) |
|---|---|---|---|---|
| objective | 15 | 62 | 47 | 7 to 26 |
| exfil_p | 7 | 28 | 21 | 1 to 14 |
| iface_closed | 2 | 26 | 24 | -3 to 7 |
| x_rate | 4 | 17 | 13 | -1 to 12 |
| node_reconf | 8 | 15 | 7 | 2 to 16 |
| server_share | 2 | 14 | 11 | -3 to 11 |
| atk_cap | 0 | 11 | 11 | -3 to 3 |
| ext_exploit | 0 | 11 | 10 | -1 to 2 |
| a_rate | 2 | 9 | 7 | -0 to 5 |
| ext_total | -0 | 9 | 9 | -5 to 6 |
| n_ext | 1 | 7 | 6 | -1 to 4 |
| ext_bad | -2 | 7 | 9 | -5 to 0 |
| coverage | -1 | 5 | 6 | -4 to 2 |
| ext_auth | -0 | 5 | 6 | -1 to 0 |
| remote_share | 1 | 3 | 2 | -0 to 2 |
| cloud_share | 0 | 3 | 3 | -1 to 2 |
| chan_cov | 2 | 3 | 1 | -1 to 7 |
| def_cap | 1 | 3 | 1 | -0 to 4 |
| cloud_link | -0 | 2 | 3 | -2 to 1 |
| seg_ep | 0 | 2 | 2 | -1 to 2 |
| size | 0 | 2 | 2 | -1 to 2 |
| ext_share | 0 | 2 | 2 | -2 to 3 |
| obs_interval | 1 | 2 | 1 | -0 to 2 |
| zone_conn | -0 | 2 | 2 | -1 to 0 |
| rebuild_time | 0 | 2 | 2 | -1 to 1 |
| n_chan | -0 | 2 | 2 | -2 to 1 |
| retool | -1 | 2 | 2 | -2 to 1 |
| seg_sv | 2 | 2 | 0 | -1 to 5 |
| atk_budget | -0 | 2 | 2 | -2 to 2 |
| dns | 0 | 1 | 1 | -0 to 1 |
| reconf_time | -0 | 1 | 2 | -1 to 0 |
| blind_delay | 0 | 1 | 1 | -0 to 1 |
| payload_delay | -0 | 1 | 1 | -1 to 1 |
| manual_delay | 1 | 1 | 1 | -0 to 1 |
| tac_budget | 0 | 1 | 1 | -1 to 1 |
| chan_span | 1 | 1 | 0 | -1 to 3 |
| theta | -1 | 1 | 2 | -2 to 0 |
| cap_spread | 0 | 1 | 1 | -0 to 1 |
| ctl_link | -0 | 1 | 1 | -0 to 0 |
| t_clean | 0 | 1 | 1 | -0 to 1 |
| cap_drift | 1 | 1 | 0 | -1 to 2 |
| redundancy | 0 | 1 | 0 | -0 to 1 |
| chan | -0 | 1 | 1 | -1 to 1 |
| concentration | 0 | 1 | 0 | -0 to 1 |
| supplied_x | 0 | 1 | 1 | -1 to 1 |
| ep_conn | 0 | 1 | 0 | -0 to 1 |
| rate_var | -0 | 1 | 1 | -0 to 0 |
| visibility | 0 | 1 | 1 | -1 to 1 |
| fanout | 0 | 1 | 1 | -0 to 1 |
| stage_time | -0 | 1 | 1 | -0 to 0 |
| dval_sv | -0 | 0 | 1 | -1 to 1 |
| vpn | 0 | 0 | 0 | -0 to 0 |
| queue_order | 2 | 0 | -1 | -0 to 5 |
| auth_cred | -0 | 0 | 0 | -1 to 0 |
| ep_sv | 0 | 0 | 0 | -1 to 1 |
| managed | -0 | 0 | 0 | -0 to 0 |
| t_cut | -0 | 0 | 0 | -0 to 0 |
| c_s | -0 | 0 | 0 | -0 to 0 |

Ranking by total index with cumulative share of the summed totals; a variable is incidental on this outcome if the upper end of its total-index interval is below 2%. Incidental here: tac_budget (1, interval 0 to 2), t_clean (1, interval 0 to 2), cap_drift (1, interval 0 to 1), redundancy (1, interval 0 to 1), chan (1, interval 0 to 2), concentration (1, interval 0 to 2), supplied_x (1, interval 0 to 2), ep_conn (1, interval 0 to 2), rate_var (1, interval 0 to 1), visibility (1, interval 0 to 1), fanout (1, interval 0 to 1), stage_time (1, interval 0 to 1), dval_sv (0, interval 0 to 1), vpn (0, interval 0 to 1), queue_order (0, interval 0 to 1), auth_cred (0, interval 0 to 1), ep_sv (0, interval 0 to 1), managed (0, interval 0 to 0), t_cut (0, interval 0 to 0), c_s (0, interval 0 to 0). Their summed totals, the bound on the variance the pair pass cannot see on this outcome: 11%. A variable incidental on every reported outcome is left out of the pair pass; the kept set is the union over outcomes.

| rank | variable | total | share of totals | cumulative |
|---|---|---|---|---|
| 1 | objective | 62 | 22 | 22 |
| 2 | exfil_p | 28 | 10 | 32 |
| 3 | iface_closed | 26 | 9 | 41 |
| 4 | x_rate | 17 | 6 | 47 |
| 5 | node_reconf | 15 | 5 | 53 |
| 6 | server_share | 14 | 5 | 58 |
| 7 | atk_cap | 11 | 4 | 62 |
| 8 | ext_exploit | 11 | 4 | 65 |
| 9 | a_rate | 9 | 3 | 69 |
| 10 | ext_total | 9 | 3 | 72 |
| 11 | n_ext | 7 | 3 | 74 |
| 12 | ext_bad | 7 | 3 | 77 |
| 13 | coverage | 5 | 2 | 79 |
| 14 | ext_auth | 5 | 2 | 81 |
| 15 | remote_share | 3 | 1 | 82 |
| 16 | cloud_share | 3 | 1 | 83 |
| 17 | chan_cov | 3 | 1 | 84 |
| 18 | def_cap | 3 | 1 | 85 |
| 19 | cloud_link | 2 | 1 | 86 |
| 20 | seg_ep | 2 | 1 | 87 |
| 21 | size | 2 | 1 | 87 |
| 22 | ext_share | 2 | 1 | 88 |
| 23 | obs_interval | 2 | 1 | 89 |
| 24 | zone_conn | 2 | 1 | 89 |
| 25 | rebuild_time | 2 | 1 | 90 |
| 26 | n_chan | 2 | 1 | 91 |
| 27 | retool | 2 | 1 | 91 |
| 28 | seg_sv | 2 | 1 | 92 |
| 29 | atk_budget | 2 | 1 | 92 |
| 30 | dns | 1 | 1 | 93 |
| 31 | reconf_time | 1 | 1 | 93 |
| 32 | blind_delay | 1 | 0 | 94 |
| 33 | payload_delay | 1 | 0 | 94 |
| 34 | manual_delay | 1 | 0 | 95 |
| 35 | tac_budget | 1 | 0 | 95 |
| 36 | chan_span | 1 | 0 | 95 |
| 37 | theta | 1 | 0 | 96 |
| 38 | cap_spread | 1 | 0 | 96 |
| 39 | ctl_link | 1 | 0 | 97 |
| 40 | t_clean | 1 | 0 | 97 |
| 41 | cap_drift | 1 | 0 | 97 |
| 42 | redundancy | 1 | 0 | 97 |
| 43 | chan | 1 | 0 | 98 |
| 44 | concentration | 1 | 0 | 98 |
| 45 | supplied_x | 1 | 0 | 98 |
| 46 | ep_conn | 1 | 0 | 98 |
| 47 | rate_var | 1 | 0 | 99 |
| 48 | visibility | 1 | 0 | 99 |
| 49 | fanout | 1 | 0 | 99 |
| 50 | stage_time | 1 | 0 | 99 |
| 51 | dval_sv | 0 | 0 | 100 |
| 52 | vpn | 0 | 0 | 100 |
| 53 | queue_order | 0 | 0 | 100 |
| 54 | auth_cred | 0 | 0 | 100 |
| 55 | ep_sv | 0 | 0 | 100 |
| 56 | managed | 0 | 0 | 100 |
| 57 | t_cut | 0 | 0 | 100 |
| 58 | c_s | 0 | 0 | 100 |

| pair | joint first-order | pair interaction term | 95% interval (joint) |
|---|---|---|---|
| iface_closed+objective | 24 | 7 | 12 to 38 |
| ext_exploit+objective | 20 | 5 | 9 to 34 |
| chan_cov+exfil_p | 14 | 4 | 2 to 32 |
| ext_total+ext_bad | 2 | 4 | -4 to 10 |
| n_ext+objective | 20 | 4 | 9 to 34 |
| ext_share+objective | 19 | 4 | 8 to 32 |
| chan_span+exfil_p | 11 | 3 | 2 to 24 |
| iface_closed+ext_total | 4 | 3 | -2 to 12 |
| x_rate+zone_conn | 6 | 2 | -1 to 18 |
| coverage+exfil_p | 8 | 2 | -0 to 19 |
| iface_closed+ext_share | 4 | 2 | -2 to 12 |
| node_reconf+objective | 25 | 2 | 14 to 37 |
| tac_budget+size | 2 | 2 | -2 to 9 |
| iface_closed+exfil_p | 11 | 2 | 2 to 21 |
| iface_closed+ext_exploit | 4 | 2 | -1 to 11 |

Response surface fitted to all 316416 sampled configurations. Pairwise terms only: R2 89% in sample, -78% on a held-out fifth. Too few points for the three-way terms; pairs only. Groups derived by clustering the variables on the surface's pairwise terms: 2 groups (silhouette 0.02), holding 96% of the interaction mass within groups.

| derived group | members |
|---|---|
| group:objective | server_share, a_rate, iface_closed, atk_cap, ext_exploit, manual_delay, x_rate, chan_cov, ext_auth, coverage, zone_conn, remote_share, ext_total, n_chan, chan_span, theta, seg_sv, cloud_share, atk_budget, t_cut, n_ext, ep_conn, node_reconf, blind_delay, supplied_x, chan, redundancy, payload_delay, visibility, retool, size, rebuild_time, ext_bad, fanout, ctl_link, ext_share, t_clean, def_cap, c_s, concentration, dns, cap_drift, rate_var, vpn, auth_cred, seg_ep, stage_time, cloud_link, ep_sv, queue_order, managed, reconf_time, obs_interval, exfil_p, objective, dval_sv |
| group:tac_budget | tac_budget, cap_spread |

| group term (on the surface) | first-order | total | interaction term |
|---|---|---|---|
| group:objective | 97 | 98 | 1 |
| group:tac_budget | 0 | 1 | 1 |
| group:objective+group:tac_budget | 98 | 98 | 1 |

### service loss (variance 0.0323)

| term | first-order | total | interaction share | 95% interval (first-order) |
|---|---|---|---|---|
| iface_closed | 26 | 48 | 22 | 10 to 43 |
| x_rate | 2 | 27 | 25 | -2 to 6 |
| a_rate | 6 | 22 | 16 | -0 to 13 |
| atk_cap | -3 | 16 | 19 | -11 to 4 |
| ext_exploit | 5 | 16 | 11 | -0 to 11 |
| ext_share | 2 | 12 | 11 | -6 to 9 |
| server_share | 3 | 11 | 8 | -4 to 11 |
| coverage | 5 | 7 | 2 | -0 to 11 |
| ext_auth | -3 | 7 | 10 | -10 to 5 |
| def_cap | 2 | 6 | 4 | -4 to 7 |
| ext_total | -2 | 6 | 8 | -8 to 3 |
| chan_cov | 6 | 5 | -2 | -1 to 16 |
| reconf_time | -7 | 5 | 11 | -11 to -3 |
| n_ext | 1 | 5 | 4 | -2 to 5 |
| cloud_share | 8 | 4 | -3 | 1 to 17 |
| size | 1 | 4 | 3 | -4 to 7 |
| remote_share | 1 | 4 | 3 | -3 to 5 |
| ext_bad | 2 | 3 | 1 | -3 to 8 |
| tac_budget | -1 | 3 | 3 | -6 to 4 |
| chan_span | 4 | 3 | -2 | -1 to 11 |
| auth_cred | 2 | 3 | 0 | -1 to 7 |
| seg_sv | -3 | 3 | 5 | -8 to 2 |
| retool | -3 | 2 | 5 | -6 to -0 |
| payload_delay | -1 | 2 | 4 | -5 to 2 |
| rebuild_time | -1 | 2 | 4 | -4 to 1 |
| n_chan | -2 | 2 | 3 | -4 to -0 |
| atk_budget | 1 | 1 | -0 | -2 to 5 |
| theta | -1 | 1 | 2 | -3 to 1 |
| blind_delay | -1 | 1 | 3 | -4 to 1 |
| seg_ep | -3 | 1 | 4 | -5 to -0 |
| node_reconf | 1 | 1 | 0 | -1 to 2 |
| ctl_link | 1 | 1 | -1 | -1 to 4 |
| cap_drift | -1 | 1 | 2 | -3 to 1 |
| supplied_x | -1 | 1 | 1 | -2 to 1 |
| redundancy | 1 | 1 | -0 | -1 to 4 |
| zone_conn | -1 | 1 | 2 | -3 to -0 |
| visibility | 0 | 1 | 0 | -1 to 2 |
| chan | -0 | 0 | 1 | -2 to 1 |
| cloud_link | 1 | 0 | -0 | -0 to 2 |
| dns | -2 | 0 | 2 | -3 to -0 |
| stage_time | -2 | 0 | 2 | -4 to 0 |
| fanout | -0 | 0 | 0 | -1 to 1 |
| manual_delay | 1 | 0 | -0 | -1 to 3 |
| t_clean | -1 | 0 | 1 | -2 to 0 |
| cap_spread | 0 | 0 | 0 | -1 to 1 |
| obs_interval | 0 | 0 | -0 | -1 to 2 |
| concentration | -0 | 0 | 0 | -1 to 1 |
| ep_conn | 1 | 0 | -0 | -0 to 2 |
| rate_var | -1 | 0 | 1 | -2 to -0 |
| queue_order | 0 | 0 | -0 | -0 to 1 |
| managed | 0 | 0 | 0 | -1 to 1 |
| ep_sv | -0 | 0 | 0 | -1 to 1 |
| vpn | 0 | 0 | 0 | -0 to 0 |
| objective | -1 | 0 | 1 | -1 to 0 |
| exfil_p | -0 | 0 | 0 | -0 to 0 |
| dval_sv | -0 | 0 | 0 | -0 to -0 |
| c_s | -0 | 0 | 0 | -0 to -0 |
| t_cut | -0 | 0 | 0 | -0 to 0 |

Ranking by total index with cumulative share of the summed totals; a variable is incidental on this outcome if the upper end of its total-index interval is below 2%. Incidental here: blind_delay (1, interval 1 to 2), seg_ep (1, interval 1 to 2), node_reconf (1, interval 0 to 2), ctl_link (1, interval 0 to 1), cap_drift (1, interval 0 to 1), supplied_x (1, interval 0 to 1), redundancy (1, interval 0 to 1), zone_conn (1, interval 0 to 1), visibility (1, interval 0 to 1), chan (0, interval 0 to 1), cloud_link (0, interval 0 to 1), dns (0, interval 0 to 1), stage_time (0, interval 0 to 1), fanout (0, interval 0 to 1), manual_delay (0, interval 0 to 1), t_clean (0, interval 0 to 1), cap_spread (0, interval 0 to 0), obs_interval (0, interval 0 to 1), concentration (0, interval 0 to 0), ep_conn (0, interval 0 to 0), rate_var (0, interval 0 to 0), queue_order (0, interval 0 to 0), managed (0, interval 0 to 0), ep_sv (0, interval 0 to 0), vpn (0, interval 0 to 0), objective (0, interval 0 to 0), exfil_p (0, interval 0 to 0), dval_sv (0, interval 0 to 0), c_s (0, interval 0 to 0), t_cut (0, interval 0 to 0). Their summed totals, the bound on the variance the pair pass cannot see on this outcome: 11%. A variable incidental on every reported outcome is left out of the pair pass; the kept set is the union over outcomes.

| rank | variable | total | share of totals | cumulative |
|---|---|---|---|---|
| 1 | iface_closed | 48 | 20 | 20 |
| 2 | x_rate | 27 | 11 | 31 |
| 3 | a_rate | 22 | 9 | 40 |
| 4 | atk_cap | 16 | 7 | 47 |
| 5 | ext_exploit | 16 | 7 | 54 |
| 6 | ext_share | 12 | 5 | 59 |
| 7 | server_share | 11 | 5 | 63 |
| 8 | coverage | 7 | 3 | 66 |
| 9 | ext_auth | 7 | 3 | 69 |
| 10 | def_cap | 6 | 2 | 72 |
| 11 | ext_total | 6 | 2 | 74 |
| 12 | chan_cov | 5 | 2 | 76 |
| 13 | reconf_time | 5 | 2 | 78 |
| 14 | n_ext | 5 | 2 | 80 |
| 15 | cloud_share | 4 | 2 | 82 |
| 16 | size | 4 | 2 | 84 |
| 17 | remote_share | 4 | 2 | 85 |
| 18 | ext_bad | 3 | 1 | 86 |
| 19 | tac_budget | 3 | 1 | 87 |
| 20 | chan_span | 3 | 1 | 89 |
| 21 | auth_cred | 3 | 1 | 90 |
| 22 | seg_sv | 3 | 1 | 91 |
| 23 | retool | 2 | 1 | 92 |
| 24 | payload_delay | 2 | 1 | 93 |
| 25 | rebuild_time | 2 | 1 | 94 |
| 26 | n_chan | 2 | 1 | 94 |
| 27 | atk_budget | 1 | 1 | 95 |
| 28 | theta | 1 | 1 | 95 |
| 29 | blind_delay | 1 | 0 | 96 |
| 30 | seg_ep | 1 | 0 | 96 |
| 31 | node_reconf | 1 | 0 | 96 |
| 32 | ctl_link | 1 | 0 | 97 |
| 33 | cap_drift | 1 | 0 | 97 |
| 34 | supplied_x | 1 | 0 | 97 |
| 35 | redundancy | 1 | 0 | 98 |
| 36 | zone_conn | 1 | 0 | 98 |
| 37 | visibility | 1 | 0 | 98 |
| 38 | chan | 0 | 0 | 98 |
| 39 | cloud_link | 0 | 0 | 99 |
| 40 | dns | 0 | 0 | 99 |
| 41 | stage_time | 0 | 0 | 99 |
| 42 | fanout | 0 | 0 | 99 |
| 43 | manual_delay | 0 | 0 | 99 |
| 44 | t_clean | 0 | 0 | 99 |
| 45 | cap_spread | 0 | 0 | 99 |
| 46 | obs_interval | 0 | 0 | 99 |
| 47 | concentration | 0 | 0 | 100 |
| 48 | ep_conn | 0 | 0 | 100 |
| 49 | rate_var | 0 | 0 | 100 |
| 50 | queue_order | 0 | 0 | 100 |
| 51 | managed | 0 | 0 | 100 |
| 52 | ep_sv | 0 | 0 | 100 |
| 53 | vpn | 0 | 0 | 100 |
| 54 | objective | 0 | 0 | 100 |
| 55 | exfil_p | 0 | 0 | 100 |
| 56 | dval_sv | 0 | 0 | 100 |
| 57 | c_s | 0 | 0 | 100 |
| 58 | t_cut | 0 | 0 | 100 |

| pair | joint first-order | pair interaction term | 95% interval (joint) |
|---|---|---|---|
| server_share+iface_closed | 34 | 5 | 16 to 53 |
| a_rate+iface_closed | 36 | 5 | 19 to 56 |
| ext_auth+ext_total | -0 | 4 | -9 to 9 |
| atk_cap+ext_share | 2 | 4 | -7 to 12 |
| iface_closed+atk_cap | 26 | 4 | 10 to 45 |
| ext_bad+reconf_time | -1 | 4 | -8 to 7 |
| iface_closed+x_rate | 31 | 3 | 14 to 49 |
| ext_auth+seg_sv | -2 | 3 | -10 to 7 |
| atk_cap+ext_exploit | 5 | 3 | -4 to 14 |
| atk_cap+ext_auth | -3 | 3 | -14 to 8 |
| server_share+a_rate | 12 | 3 | 2 to 23 |
| chan_span+seg_ep | 4 | 3 | -3 to 14 |
| coverage+seg_ep | 5 | 3 | -0 to 11 |
| seg_sv+seg_ep | -3 | 3 | -8 to 3 |
| ext_exploit+payload_delay | 6 | 3 | -0 to 14 |

Response surface fitted to all 316416 sampled configurations. Pairwise terms only: R2 91% in sample, -19% on a held-out fifth. Too few points for the three-way terms; pairs only. Groups derived by clustering the variables on the surface's pairwise terms: 2 groups (silhouette 0.06), holding 98% of the interaction mass within groups.

| derived group | members |
|---|---|
| group:iface_closed | server_share, a_rate, iface_closed, atk_cap, tac_budget, ext_exploit, manual_delay, x_rate, chan_cov, ext_auth, coverage, remote_share, ext_total, n_chan, chan_span, theta, seg_sv, cloud_share, atk_budget, t_cut, n_ext, ep_conn, node_reconf, blind_delay, supplied_x, chan, redundancy, payload_delay, visibility, retool, size, rebuild_time, ext_bad, fanout, ctl_link, ext_share, t_clean, def_cap, c_s, concentration, dns, cap_drift, rate_var, vpn, auth_cred, seg_ep, stage_time, cloud_link, ep_sv, queue_order, cap_spread, managed, reconf_time, obs_interval, exfil_p, objective, dval_sv |
| group:zone_conn | zone_conn |

| group term (on the surface) | first-order | total | interaction term |
|---|---|---|---|
| group:iface_closed | 100 | 100 | -0 |
| group:zone_conn | 0 | 1 | 0 |
| group:iface_closed+group:zone_conn | 101 | 100 | 0 |
