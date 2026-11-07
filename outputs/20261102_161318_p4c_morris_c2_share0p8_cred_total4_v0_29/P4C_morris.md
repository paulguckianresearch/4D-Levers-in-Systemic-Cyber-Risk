# Paper 4C global screen: Morris elementary effects (PhDPaper4C v0.29 (2026-11-02)) - stratum {'cred_total': 4, 'c2_share': 0.8}

Every register dial and the setup variables (topology, governance scope), 20 trajectories per kind, each configuration on wirings [6801, 6802, 6803, 6804] and seeds [6901, 6902, 6903, 6904] (common random numbers). Effects are in outcome units (share of the estate, or probability) per full range of the variable, extrapolated from half-range steps, so a value can exceed 100. mu* is the mean absolute effect, sigma its spread across trajectories: a large sigma with a small mu* is a variable that matters only in part of the space. A variable is kept for Stage 2 (Sobol) if mu* or sigma reaches 5 points on any outcome.

## intrusion

| variable | layer | mu* collapse | sigma collapse | mu* furthest | mu* data loss | mu* service loss | kept |
|---|---|---|---|---|---|---|---|
| server_share | system | 41 | 75 | 25 | 4 | 13 | yes |
| a_rate | node | 34 | 74 | 23 | 2 | 13 | yes |
| iface_closed | node | 47 | 61 | 46 | 17 | 30 | yes |
| atk_cap | attacker | 37 | 60 | 16 | 8 | 16 | yes |
| tac_budget | adaptation | 30 | 58 | 13 | 5 | 13 | yes |
| ext_exploit | node | 20 | 53 | 17 | 6 | 9 | yes |
| manual_delay | time | 14 | 48 | 3 | 5 | 4 | yes |
| x_rate | node | 19 | 46 | 12 | 3 | 9 | yes |
| chan_cov | system | 31 | 46 | 10 | 5 | 6 | yes |
| ext_auth | system of systems | 20 | 43 | 28 | 6 | 8 | yes |
| coverage | system | 23 | 40 | 17 | 8 | 12 | yes |
| zone_conn | system | 15 | 38 | 8 | 5 | 5 | yes |
| remote_share | system | 16 | 38 | 8 | 5 | 3 | yes |
| ext_total | system of systems | 20 | 37 | 17 | 10 | 8 | yes |
| n_chan | system | 19 | 35 | 12 | 3 | 3 | yes |
| chan_span | system | 16 | 32 | 8 | 1 | 4 | yes |
| theta | operator | 13 | 32 | 9 | 2 | 2 | yes |
| seg_sv | system | 20 | 32 | 10 | 2 | 6 | yes |
| cloud_share | system | 12 | 27 | 10 | 3 | 7 | yes |
| atk_budget | attacker | 11 | 22 | 3 | 2 | 2 | yes |
| t_cut | time | 9 | 22 | 8 | 1 | 7 | yes |
| n_ext | system of systems | 9 | 20 | 17 | 4 | 4 | yes |
| ep_conn | system | 7 | 19 | 4 | 2 | 2 | yes |
| node_reconf | attacker | 9 | 19 | 8 | 29 | 4 | yes |
| blind_delay | node | 7 | 19 | 6 | 2 | 8 | yes |
| supplied_x | node | 6 | 18 | 3 | 1 | 2 | yes |
| chan | system | 8 | 17 | 4 | 2 | 3 | yes |
| redundancy | operator | 8 | 17 | 3 | 2 | 2 | yes |
| payload_delay | attacker | 6 | 16 | 4 | 2 | 3 | yes |
| visibility | node | 9 | 16 | 4 | 1 | 2 | yes |
| retool | attacker | 9 | 15 | 4 | 1 | 4 | yes |
| size | system | 9 | 15 | 7 | 4 | 6 | yes |
| rebuild_time | adaptation | 7 | 14 | 3 | 1 | 5 | yes |
| ext_bad | system of systems | 5 | 14 | 12 | 4 | 3 | yes |
| fanout | operator | 6 | 14 | 3 | 1 | 1 | yes |
| ctl_link | system | 3 | 14 | 1 | 0 | 1 | yes |
| ext_share | node | 5 | 13 | 12 | 3 | 7 | yes |
| t_clean | time | 5 | 13 | 3 | 2 | 1 | yes |
| def_cap | adaptation | 6 | 12 | 6 | 4 | 5 | yes |
| c_s | time | 5 | 12 | 2 | 2 | 4 | yes |
| concentration | system | 5 | 11 | 2 | 1 | 2 | yes |
| dns | system | 7 | 11 | 3 | 1 | 1 | yes |
| cap_drift | attacker | 5 | 10 | 4 | 3 | 3 | yes |
| rate_var | node | 2 | 10 | 2 | 0 | 1 | yes |
| vpn | system | 2 | 10 | 1 | 0 | 1 | yes |
| auth_cred | system | 3 | 10 | 0 | 0 | 4 | yes |
| seg_ep | system | 3 | 9 | 5 | 3 | 2 | yes |
| stage_time | time | 4 | 9 | 1 | 1 | 2 | yes |
| cloud_link | system | 3 | 9 | 1 | 2 | 1 | yes |
| ep_sv | system | 2 | 8 | 1 | 0 | 0 | yes |
| queue_order | adaptation | 3 | 7 | 3 | 1 | 2 | yes |
| cap_spread | attacker | 3 | 7 | 2 | 1 | 1 | yes |
| managed | system | 2 | 7 | 3 | 2 | 1 | yes |
| reconf_time | time | 3 | 7 | 1 | 1 | 2 | yes |
| detect_latency | time | 2 | 5 | 1 | 1 | 0 |  |
| ad_reach | system | 2 | 5 | 1 | 1 | 1 |  |
| dose | adaptation | 1 | 4 | 2 | 1 | 1 |  |
| supplied_a | node | 1 | 3 | 1 | 2 | 1 |  |
| inequality | operator | 1 | 3 | 3 | 1 | 1 |  |
| obs_interval | time | 1 | 3 | 2 | 0 | 1 | yes |
| ceil_deliv | system | 1 | 3 | 1 | 0 | 1 |  |
| exfil_p | node | 1 | 3 | 1 | 20 | 1 | yes |
| edr_site | system of systems | 1 | 2 | 0 | 0 | 0 |  |
| objective | attacker | 1 | 2 | 1 | 24 | 1 | yes |
| dns_site | system of systems | 0 | 1 | 0 | 0 | 0 |  |
| block_delay | time | 0 | 0 | 0 | 0 | 0 |  |
| manual_scope | adaptation | 0 | 0 | 0 | 0 | 0 |  |
| auto_clean | adaptation | 0 | 0 | 0 | 0 | 0 |  |
| dormant_share | attacker | 0 | 0 | 0 | 0 | 0 |  |
| dormant_delay | attacker | 0 | 0 | 0 | 0 | 0 |  |
| fixed_clock | attacker | 0 | 0 | 0 | 0 | 0 |  |
| cloud_bad | system of systems | 0 | 0 | 0 | 0 | 0 |  |
| ceil_edr | system | 0 | 0 | 0 | 0 | 0 |  |
| ceil_ext | system of systems | 0 | 0 | 0 | 0 | 0 |  |
| chan_verify | system | 0 | 0 | 0 | 0 | 0 |  |
| exfil_esc | node | 0 | 0 | 0 | 1 | 0 |  |
| sig_block | node | 0 | 0 | 0 | 0 | 0 |  |
| rotate | adaptation | 0 | 0 | 0 | 0 | 0 |  |
| cred_ttl | time | 0 | 0 | 0 | 0 | 0 |  |
| restore_rotate | adaptation | 0 | 0 | 0 | 0 | 0 |  |
| svc_view | adaptation | 0 | 0 | 0 | 0 | 0 |  |
| val_sv | system | 0 | 0 | 0 | 0 | 1 |  |
| dval_sv | system | 0 | 0 | 0 | 2 | 0 | yes |
| exc_share | system | 0 | 0 | 0 | 0 | 0 |  |
| hand_delay | time | 0 | 0 | 0 | 0 | 0 |  |
| repl_delay | time | 0 | 0 | 0 | 0 | 0 |  |
| topology | setup | 0 | 0 | 0 | 0 | 0 |  |
| gamma | setup | 0 | 0 | 0 | 0 | 0 |  |
