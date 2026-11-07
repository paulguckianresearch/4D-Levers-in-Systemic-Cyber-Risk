# Paper 4C global screen: Morris elementary effects (PhDPaper4C v1.1 (2026-11-05, surface validation for Paper 4D; model as v0.26/v0.27)) - stratum {'cred_total': 4, 'c2_share': 0.8}

Every register dial and the setup variables (topology, governance scope), 8 trajectories per kind, each configuration on wirings [6801, 6802] and seeds [6901, 6902] (common random numbers). Effects are in outcome units (share of the estate, or probability) per full range of the variable, extrapolated from half-range steps, so a value can exceed 100. mu* is the mean absolute effect, sigma its spread across trajectories: a large sigma with a small mu* is a variable that matters only in part of the space. A variable is kept for Stage 2 (Sobol) if mu* or sigma reaches 5 points on any outcome.

## implant

| variable | layer | mu* collapse | sigma collapse | mu* furthest | mu* data loss | mu* service loss | kept |
|---|---|---|---|---|---|---|---|
| chan_span | system | 55 | 93 | 9 | 8 | 7 | yes |
| atk_cap | attacker | 39 | 69 | 10 | 9 | 9 | yes |
| size | system | 31 | 53 | 16 | 0 | 1 | yes |
| blind_delay | node | 23 | 49 | 10 | 10 | 7 | yes |
| managed | system | 31 | 44 | 21 | 0 | 3 | yes |
| supplied_x | node | 16 | 41 | 7 | 2 | 1 | yes |
| iface_closed | node | 16 | 41 | 13 | 9 | 5 | yes |
| rebuild_time | adaptation | 16 | 41 | 3 | 3 | 3 | yes |
| n_ext | system of systems | 16 | 41 | 26 | 1 | 3 | yes |
| ext_total | system of systems | 16 | 41 | 49 | 2 | 9 | yes |
| ext_auth | system of systems | 16 | 41 | 20 | 0 | 1 | yes |
| redundancy | operator | 12 | 33 | 7 | 2 | 2 | yes |
| queue_order | adaptation | 12 | 33 | 2 | 1 | 2 | yes |
| coverage | system | 16 | 27 | 35 | 2 | 12 | yes |
| seg_sv | system | 9 | 25 | 7 | 2 | 2 | yes |
| x_rate | node | 8 | 21 | 3 | 2 | 2 | yes |
| def_cap | adaptation | 8 | 21 | 8 | 1 | 2 | yes |
| ext_bad | system of systems | 8 | 21 | 21 | 5 | 4 | yes |
| ceil_ext | system of systems | 8 | 21 | 3 | 0 | 0 | yes |
| chan_cov | system | 8 | 21 | 8 | 2 | 2 | yes |
| ext_share | node | 7 | 19 | 3 | 0 | 0 | yes |
| edr_site | system of systems | 9 | 17 | 8 | 1 | 1 | yes |
| repl_delay | time | 6 | 17 | 1 | 0 | 0 | yes |
| dns_site | system of systems | 3 | 8 | 2 | 1 | 1 | yes |
| dns | system | 3 | 8 | 3 | 1 | 1 | yes |
| supplied_a | node | 0 | 0 | 1 | 1 | 1 |  |
| a_rate | node | 0 | 0 | 0 | 2 | 1 |  |
| rate_var | node | 0 | 0 | 0 | 0 | 0 |  |
| visibility | node | 0 | 0 | 5 | 4 | 1 | yes |
| chan | system | 0 | 0 | 2 | 1 | 1 | yes |
| concentration | system | 0 | 0 | 1 | 1 | 1 |  |
| fanout | operator | 0 | 0 | 0 | 0 | 1 |  |
| inequality | operator | 0 | 0 | 1 | 1 | 0 |  |
| theta | operator | 0 | 0 | 0 | 0 | 0 |  |
| block_delay | time | 0 | 0 | 1 | 1 | 1 |  |
| c_s | time | 0 | 0 | 1 | 0 | 2 |  |
| obs_interval | time | 0 | 0 | 1 | 1 | 2 |  |
| detect_latency | time | 0 | 0 | 2 | 2 | 1 | yes |
| dose | adaptation | 0 | 0 | 1 | 1 | 0 |  |
| tac_budget | adaptation | 0 | 0 | 4 | 0 | 4 | yes |
| manual_scope | adaptation | 0 | 0 | 0 | 0 | 0 |  |
| auto_clean | adaptation | 0 | 0 | 0 | 0 | 0 |  |
| manual_delay | time | 0 | 0 | 5 | 3 | 3 | yes |
| t_clean | time | 0 | 0 | 0 | 2 | 1 |  |
| t_cut | time | 0 | 0 | 4 | 2 | 5 | yes |
| atk_budget | attacker | 0 | 0 | 6 | 5 | 2 | yes |
| retool | attacker | 0 | 0 | 1 | 1 | 1 |  |
| payload_delay | attacker | 0 | 0 | 0 | 0 | 0 |  |
| dormant_share | attacker | 0 | 0 | 0 | 0 | 0 |  |
| dormant_delay | attacker | 0 | 0 | 9 | 2 | 2 | yes |
| cap_spread | attacker | 0 | 0 | 1 | 0 | 0 |  |
| node_reconf | attacker | 0 | 0 | 2 | 4 | 1 | yes |
| fixed_clock | attacker | 0 | 0 | 2 | 0 | 2 | yes |
| server_share | system | 0 | 0 | 21 | 11 | 4 | yes |
| remote_share | system | 0 | 0 | 8 | 4 | 3 | yes |
| cloud_share | system | 0 | 0 | 19 | 3 | 10 | yes |
| seg_ep | system | 0 | 0 | 8 | 1 | 4 | yes |
| ep_conn | system | 0 | 0 | 0 | 0 | 0 |  |
| ep_sv | system | 0 | 0 | 0 | 1 | 1 |  |
| cloud_link | system | 0 | 0 | 6 | 3 | 4 | yes |
| vpn | system | 0 | 0 | 0 | 0 | 0 |  |
| ext_exploit | node | 0 | 0 | 5 | 5 | 1 | yes |
| cloud_bad | system of systems | 0 | 0 | 24 | 0 | 2 | yes |
| ceil_deliv | system | 0 | 0 | 2 | 0 | 3 | yes |
| ceil_edr | system | 0 | 0 | 0 | 0 | 0 |  |
| chan_verify | system | 0 | 0 | 0 | 0 | 0 |  |
| auth_cred | system | 0 | 0 | 1 | 1 | 9 | yes |
| exfil_esc | node | 0 | 0 | 0 | 3 | 0 | yes |
| sig_block | node | 0 | 0 | 0 | 0 | 0 |  |
| rotate | adaptation | 0 | 0 | 0 | 0 | 0 |  |
| cred_ttl | time | 0 | 0 | 0 | 0 | 0 |  |
| restore_rotate | adaptation | 0 | 0 | 0 | 0 | 0 |  |
| svc_view | adaptation | 0 | 0 | 0 | 0 | 0 |  |
| exfil_p | node | 0 | 0 | 0 | 6 | 0 | yes |
| objective | attacker | 0 | 0 | 1 | 15 | 1 | yes |
| val_sv | system | 0 | 0 | 0 | 0 | 1 |  |
| dval_sv | system | 0 | 0 | 0 | 3 | 0 | yes |
| exc_share | system | 0 | 0 | 0 | 1 | 0 |  |
| zone_conn | system | 0 | 0 | 3 | 4 | 2 | yes |
| ad_reach | system | 0 | 0 | 2 | 2 | 2 |  |
| hand_delay | time | 0 | 0 | 0 | 1 | 1 |  |
| reconf_time | time | 0 | 0 | 1 | 2 | 2 | yes |
| ctl_link | system | 0 | 0 | 0 | 0 | 0 |  |
| n_chan | system | 0 | 0 | 3 | 1 | 2 |  |
| stage_time | time | 0 | 0 | 2 | 1 | 1 |  |
| cap_drift | attacker | 0 | 0 | 1 | 1 | 2 |  |
| topology | setup | 0 | 0 | 0 | 0 | 0 |  |
| gamma | setup | 0 | 0 | 0 | 0 | 0 |  |
