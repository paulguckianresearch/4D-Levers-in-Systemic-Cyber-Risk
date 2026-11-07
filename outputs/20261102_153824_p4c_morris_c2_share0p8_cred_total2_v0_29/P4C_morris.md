# Paper 4C global screen: Morris elementary effects (PhDPaper4C v0.29 (2026-11-02)) - stratum {'cred_total': 2, 'c2_share': 0.8}

Every register dial and the setup variables (topology, governance scope), 20 trajectories per kind, each configuration on wirings [6801, 6802, 6803, 6804] and seeds [6901, 6902, 6903, 6904] (common random numbers). Effects are in outcome units (share of the estate, or probability) per full range of the variable, extrapolated from half-range steps, so a value can exceed 100. mu* is the mean absolute effect, sigma its spread across trajectories: a large sigma with a small mu* is a variable that matters only in part of the space. A variable is kept for Stage 2 (Sobol) if mu* or sigma reaches 5 points on any outcome.

## intrusion

| variable | layer | mu* collapse | sigma collapse | mu* furthest | mu* data loss | mu* service loss | kept |
|---|---|---|---|---|---|---|---|
| a_rate | node | 29 | 75 | 23 | 2 | 14 | yes |
| iface_closed | node | 41 | 67 | 42 | 17 | 31 | yes |
| atk_cap | attacker | 36 | 61 | 16 | 8 | 17 | yes |
| tac_budget | adaptation | 26 | 56 | 13 | 5 | 14 | yes |
| chan_cov | system | 32 | 56 | 10 | 5 | 6 | yes |
| manual_delay | time | 15 | 55 | 2 | 7 | 5 | yes |
| zone_conn | system | 18 | 50 | 9 | 7 | 5 | yes |
| ext_exploit | node | 16 | 50 | 18 | 8 | 9 | yes |
| coverage | system | 25 | 48 | 18 | 10 | 14 | yes |
| x_rate | node | 17 | 47 | 11 | 3 | 10 | yes |
| server_share | system | 23 | 43 | 20 | 3 | 14 | yes |
| remote_share | system | 14 | 42 | 9 | 3 | 2 | yes |
| ext_auth | system of systems | 12 | 42 | 26 | 5 | 7 | yes |
| def_cap | adaptation | 20 | 35 | 8 | 4 | 6 | yes |
| t_cut | time | 16 | 35 | 7 | 1 | 7 | yes |
| cloud_share | system | 22 | 34 | 10 | 3 | 7 | yes |
| ext_total | system of systems | 15 | 33 | 16 | 10 | 9 | yes |
| chan_span | system | 16 | 32 | 8 | 1 | 4 | yes |
| n_chan | system | 12 | 31 | 11 | 3 | 4 | yes |
| atk_budget | attacker | 11 | 22 | 3 | 1 | 3 | yes |
| seg_sv | system | 11 | 22 | 4 | 2 | 5 | yes |
| concentration | system | 9 | 21 | 2 | 0 | 2 | yes |
| node_reconf | attacker | 8 | 20 | 6 | 28 | 3 | yes |
| theta | operator | 9 | 20 | 7 | 2 | 2 | yes |
| supplied_x | node | 6 | 18 | 3 | 1 | 2 | yes |
| t_clean | time | 7 | 18 | 3 | 2 | 2 | yes |
| retool | attacker | 6 | 18 | 5 | 1 | 4 | yes |
| blind_delay | node | 5 | 18 | 5 | 2 | 9 | yes |
| rebuild_time | adaptation | 9 | 17 | 4 | 1 | 6 | yes |
| seg_ep | system | 5 | 17 | 5 | 2 | 2 | yes |
| ext_bad | system of systems | 5 | 17 | 11 | 4 | 3 | yes |
| ctl_link | system | 4 | 16 | 0 | 0 | 1 | yes |
| stage_time | time | 6 | 16 | 2 | 1 | 2 | yes |
| fanout | operator | 9 | 16 | 3 | 2 | 2 | yes |
| c_s | time | 5 | 15 | 3 | 2 | 5 | yes |
| redundancy | operator | 5 | 14 | 3 | 2 | 2 | yes |
| cap_spread | attacker | 6 | 14 | 2 | 2 | 2 | yes |
| size | system | 8 | 13 | 9 | 5 | 6 | yes |
| dose | adaptation | 4 | 13 | 2 | 1 | 1 | yes |
| visibility | node | 4 | 11 | 3 | 1 | 2 | yes |
| payload_delay | attacker | 3 | 11 | 3 | 3 | 2 | yes |
| vpn | system | 2 | 10 | 1 | 0 | 1 | yes |
| cap_drift | attacker | 5 | 9 | 4 | 3 | 3 | yes |
| inequality | operator | 3 | 8 | 2 | 2 | 1 | yes |
| rate_var | node | 3 | 8 | 2 | 1 | 1 | yes |
| auth_cred | system | 2 | 8 | 0 | 0 | 4 | yes |
| dns | system | 3 | 8 | 1 | 0 | 1 | yes |
| chan | system | 2 | 7 | 3 | 1 | 2 | yes |
| n_ext | system of systems | 2 | 7 | 16 | 3 | 3 | yes |
| queue_order | adaptation | 3 | 7 | 3 | 1 | 2 | yes |
| ext_share | node | 2 | 7 | 12 | 4 | 7 | yes |
| ep_sv | system | 2 | 6 | 1 | 0 | 0 | yes |
| ad_reach | system | 2 | 6 | 1 | 0 | 1 | yes |
| reconf_time | time | 2 | 6 | 1 | 0 | 2 | yes |
| cloud_link | system | 2 | 5 | 1 | 2 | 1 |  |
| obs_interval | time | 2 | 5 | 2 | 1 | 1 |  |
| supplied_a | node | 1 | 3 | 1 | 2 | 1 |  |
| detect_latency | time | 1 | 3 | 1 | 0 | 0 |  |
| ep_conn | system | 1 | 3 | 3 | 2 | 2 | yes |
| ceil_deliv | system | 1 | 3 | 0 | 0 | 1 |  |
| exfil_p | node | 1 | 3 | 0 | 19 | 0 | yes |
| managed | system | 1 | 3 | 2 | 2 | 1 | yes |
| objective | attacker | 2 | 3 | 1 | 23 | 1 | yes |
| edr_site | system of systems | 0 | 1 | 0 | 0 | 0 |  |
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
| dval_sv | system | 0 | 0 | 0 | 1 | 0 |  |
| exc_share | system | 0 | 0 | 0 | 1 | 0 |  |
| dns_site | system of systems | 0 | 0 | 0 | 0 | 0 |  |
| hand_delay | time | 0 | 0 | 0 | 0 | 0 |  |
| repl_delay | time | 0 | 0 | 0 | 0 | 0 |  |
| topology | setup | 0 | 0 | 0 | 0 | 0 |  |
| gamma | setup | 0 | 0 | 0 | 0 | 0 |  |
