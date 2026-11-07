# Paper 4C global screen: Morris elementary effects (PhDPaper4C v0.29 (2026-11-02)) - stratum {'cred_total': 1, 'c2_share': 0.8}

Every register dial and the setup variables (topology, governance scope), 20 trajectories per kind, each configuration on wirings [6801, 6802, 6803, 6804] and seeds [6901, 6902, 6903, 6904] (common random numbers). Effects are in outcome units (share of the estate, or probability) per full range of the variable, extrapolated from half-range steps, so a value can exceed 100. mu* is the mean absolute effect, sigma its spread across trajectories: a large sigma with a small mu* is a variable that matters only in part of the space. A variable is kept for Stage 2 (Sobol) if mu* or sigma reaches 5 points on any outcome.

## intrusion

| variable | layer | mu* collapse | sigma collapse | mu* furthest | mu* data loss | mu* service loss | kept |
|---|---|---|---|---|---|---|---|
| a_rate | node | 30 | 74 | 23 | 2 | 15 | yes |
| iface_closed | node | 47 | 72 | 41 | 17 | 31 | yes |
| atk_cap | attacker | 35 | 59 | 18 | 9 | 18 | yes |
| tac_budget | adaptation | 24 | 56 | 13 | 6 | 14 | yes |
| manual_delay | time | 15 | 55 | 2 | 6 | 4 | yes |
| coverage | system | 27 | 51 | 18 | 10 | 15 | yes |
| ext_exploit | node | 17 | 50 | 19 | 10 | 9 | yes |
| chan_cov | system | 30 | 47 | 9 | 5 | 6 | yes |
| zone_conn | system | 16 | 43 | 10 | 8 | 6 | yes |
| ext_auth | system of systems | 12 | 42 | 25 | 6 | 8 | yes |
| x_rate | node | 16 | 41 | 11 | 3 | 10 | yes |
| ext_total | system of systems | 16 | 36 | 15 | 10 | 9 | yes |
| t_cut | time | 15 | 36 | 8 | 1 | 7 | yes |
| n_chan | system | 14 | 34 | 11 | 3 | 4 | yes |
| server_share | system | 16 | 34 | 19 | 2 | 14 | yes |
| def_cap | adaptation | 20 | 33 | 9 | 4 | 7 | yes |
| chan_span | system | 14 | 32 | 8 | 1 | 4 | yes |
| remote_share | system | 10 | 32 | 7 | 3 | 4 | yes |
| cloud_share | system | 16 | 29 | 8 | 3 | 7 | yes |
| blind_delay | node | 9 | 28 | 5 | 3 | 10 | yes |
| seg_ep | system | 7 | 25 | 4 | 1 | 2 | yes |
| atk_budget | attacker | 11 | 24 | 3 | 1 | 3 | yes |
| payload_delay | attacker | 9 | 23 | 4 | 2 | 3 | yes |
| stage_time | time | 8 | 22 | 2 | 0 | 2 | yes |
| size | system | 9 | 19 | 8 | 5 | 8 | yes |
| fanout | operator | 9 | 17 | 4 | 2 | 2 | yes |
| supplied_a | node | 5 | 17 | 2 | 2 | 1 | yes |
| concentration | system | 8 | 17 | 3 | 1 | 2 | yes |
| c_s | time | 7 | 17 | 2 | 2 | 4 | yes |
| ext_bad | system of systems | 5 | 17 | 12 | 3 | 3 | yes |
| ctl_link | system | 4 | 16 | 0 | 0 | 1 | yes |
| seg_sv | system | 8 | 16 | 5 | 2 | 4 | yes |
| chan | system | 5 | 15 | 4 | 1 | 2 | yes |
| redundancy | operator | 6 | 15 | 3 | 2 | 2 | yes |
| visibility | node | 6 | 14 | 3 | 1 | 2 | yes |
| rate_var | node | 5 | 14 | 1 | 0 | 1 | yes |
| obs_interval | time | 4 | 14 | 2 | 1 | 1 | yes |
| dose | adaptation | 4 | 13 | 2 | 2 | 1 | yes |
| cap_spread | attacker | 6 | 13 | 2 | 1 | 1 | yes |
| node_reconf | attacker | 5 | 13 | 5 | 28 | 2 | yes |
| rebuild_time | adaptation | 7 | 13 | 4 | 2 | 6 | yes |
| supplied_x | node | 5 | 12 | 4 | 1 | 3 | yes |
| theta | operator | 3 | 11 | 4 | 1 | 2 | yes |
| vpn | system | 3 | 11 | 1 | 0 | 1 | yes |
| retool | attacker | 5 | 11 | 4 | 2 | 4 | yes |
| queue_order | adaptation | 2 | 9 | 3 | 1 | 2 | yes |
| t_clean | time | 3 | 8 | 3 | 1 | 2 | yes |
| reconf_time | time | 3 | 8 | 1 | 1 | 2 | yes |
| ad_reach | system | 2 | 8 | 0 | 0 | 0 | yes |
| ceil_deliv | system | 2 | 7 | 0 | 0 | 1 | yes |
| auth_cred | system | 2 | 7 | 0 | 0 | 4 | yes |
| cap_drift | attacker | 3 | 7 | 4 | 3 | 3 | yes |
| objective | attacker | 2 | 6 | 1 | 23 | 1 | yes |
| inequality | operator | 2 | 5 | 3 | 1 | 1 | yes |
| detect_latency | time | 2 | 5 | 0 | 0 | 0 |  |
| ext_share | node | 1 | 4 | 11 | 4 | 6 | yes |
| dns | system | 2 | 4 | 1 | 1 | 1 |  |
| ep_conn | system | 1 | 3 | 3 | 2 | 2 | yes |
| ep_sv | system | 1 | 3 | 1 | 1 | 0 |  |
| n_ext | system of systems | 1 | 3 | 16 | 3 | 3 | yes |
| managed | system | 1 | 3 | 1 | 2 | 1 | yes |
| edr_site | system of systems | 1 | 2 | 0 | 0 | 0 |  |
| block_delay | time | 0 | 0 | 0 | 0 | 0 |  |
| manual_scope | adaptation | 0 | 0 | 0 | 0 | 0 |  |
| auto_clean | adaptation | 0 | 0 | 0 | 0 | 0 |  |
| dormant_share | attacker | 0 | 0 | 0 | 0 | 0 |  |
| dormant_delay | attacker | 0 | 0 | 0 | 0 | 0 |  |
| fixed_clock | attacker | 0 | 0 | 0 | 0 | 0 |  |
| cloud_link | system | 0 | 0 | 2 | 1 | 1 |  |
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
| exfil_p | node | 0 | 0 | 0 | 19 | 0 | yes |
| val_sv | system | 0 | 0 | 0 | 0 | 2 |  |
| dval_sv | system | 0 | 0 | 0 | 1 | 0 |  |
| exc_share | system | 0 | 0 | 0 | 1 | 0 |  |
| dns_site | system of systems | 0 | 0 | 0 | 0 | 0 |  |
| hand_delay | time | 0 | 0 | 0 | 0 | 0 |  |
| repl_delay | time | 0 | 0 | 0 | 0 | 0 |  |
| topology | setup | 0 | 0 | 0 | 0 | 0 |  |
| gamma | setup | 0 | 0 | 0 | 0 | 0 |  |
