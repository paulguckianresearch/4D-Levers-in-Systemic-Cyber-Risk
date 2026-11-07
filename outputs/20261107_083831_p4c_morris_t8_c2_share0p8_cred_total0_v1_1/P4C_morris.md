# Paper 4C global screen: Morris elementary effects (PhDPaper4C v1.1 (2026-11-05, surface validation for Paper 4D; model as v0.26/v0.27)) - stratum {'cred_total': 0, 'c2_share': 0.8}

Every register dial and the setup variables (topology, governance scope), 8 trajectories per kind, each configuration on wirings [6801, 6802] and seeds [6901, 6902] (common random numbers). Effects are in outcome units (share of the estate, or probability) per full range of the variable, extrapolated from half-range steps, so a value can exceed 100. mu* is the mean absolute effect, sigma its spread across trajectories: a large sigma with a small mu* is a variable that matters only in part of the space. A variable is kept for Stage 2 (Sobol) if mu* or sigma reaches 5 points on any outcome.

## implant

| variable | layer | mu* collapse | sigma collapse | mu* furthest | mu* data loss | mu* service loss | kept |
|---|---|---|---|---|---|---|---|
| atk_cap | attacker | 31 | 83 | 11 | 8 | 10 | yes |
| blind_delay | node | 23 | 49 | 13 | 10 | 7 | yes |
| supplied_x | node | 16 | 41 | 5 | 2 | 1 | yes |
| iface_closed | node | 16 | 41 | 13 | 10 | 5 | yes |
| rebuild_time | adaptation | 16 | 41 | 3 | 4 | 3 | yes |
| ext_total | system of systems | 16 | 41 | 44 | 2 | 7 | yes |
| managed | system | 16 | 41 | 13 | 3 | 2 | yes |
| chan_cov | system | 16 | 41 | 7 | 2 | 2 | yes |
| chan_span | system | 16 | 41 | 6 | 4 | 2 | yes |
| redundancy | operator | 12 | 33 | 6 | 1 | 3 | yes |
| size | system | 12 | 33 | 10 | 0 | 1 | yes |
| seg_sv | system | 9 | 25 | 7 | 1 | 2 | yes |
| x_rate | node | 8 | 21 | 3 | 2 | 1 | yes |
| a_rate | node | 8 | 21 | 0 | 2 | 1 | yes |
| n_ext | system of systems | 8 | 21 | 19 | 4 | 5 | yes |
| ext_bad | system of systems | 8 | 21 | 15 | 4 | 3 | yes |
| ceil_deliv | system | 8 | 21 | 0 | 0 | 0 | yes |
| edr_site | system of systems | 6 | 17 | 7 | 1 | 1 | yes |
| dns_site | system of systems | 3 | 8 | 2 | 1 | 1 | yes |
| ext_share | node | 0 | 0 | 1 | 0 | 0 |  |
| supplied_a | node | 0 | 0 | 0 | 1 | 0 |  |
| rate_var | node | 0 | 0 | 0 | 0 | 0 |  |
| visibility | node | 0 | 0 | 4 | 4 | 1 | yes |
| chan | system | 0 | 0 | 1 | 1 | 1 |  |
| coverage | system | 0 | 0 | 23 | 3 | 7 | yes |
| concentration | system | 0 | 0 | 1 | 0 | 0 |  |
| fanout | operator | 0 | 0 | 1 | 0 | 1 |  |
| inequality | operator | 0 | 0 | 1 | 1 | 0 |  |
| theta | operator | 0 | 0 | 0 | 0 | 0 |  |
| block_delay | time | 0 | 0 | 1 | 0 | 0 |  |
| c_s | time | 0 | 0 | 1 | 0 | 1 |  |
| obs_interval | time | 0 | 0 | 1 | 1 | 2 |  |
| detect_latency | time | 0 | 0 | 1 | 2 | 0 | yes |
| dose | adaptation | 0 | 0 | 1 | 1 | 0 |  |
| tac_budget | adaptation | 0 | 0 | 6 | 0 | 4 | yes |
| def_cap | adaptation | 0 | 0 | 9 | 1 | 3 | yes |
| manual_scope | adaptation | 0 | 0 | 0 | 0 | 0 |  |
| auto_clean | adaptation | 0 | 0 | 0 | 0 | 0 |  |
| manual_delay | time | 0 | 0 | 4 | 3 | 2 | yes |
| t_clean | time | 0 | 0 | 0 | 2 | 1 |  |
| t_cut | time | 0 | 0 | 3 | 1 | 2 | yes |
| queue_order | adaptation | 0 | 0 | 2 | 3 | 3 | yes |
| atk_budget | attacker | 0 | 0 | 5 | 3 | 2 | yes |
| retool | attacker | 0 | 0 | 1 | 1 | 1 |  |
| payload_delay | attacker | 0 | 0 | 0 | 0 | 0 |  |
| dormant_share | attacker | 0 | 0 | 0 | 0 | 0 |  |
| dormant_delay | attacker | 0 | 0 | 8 | 2 | 2 | yes |
| cap_spread | attacker | 0 | 0 | 1 | 0 | 0 |  |
| node_reconf | attacker | 0 | 0 | 1 | 4 | 1 | yes |
| fixed_clock | attacker | 0 | 0 | 1 | 0 | 1 |  |
| server_share | system | 0 | 0 | 21 | 10 | 4 | yes |
| remote_share | system | 0 | 0 | 7 | 2 | 0 | yes |
| cloud_share | system | 0 | 0 | 17 | 4 | 9 | yes |
| seg_ep | system | 0 | 0 | 5 | 1 | 2 | yes |
| ep_conn | system | 0 | 0 | 0 | 0 | 0 |  |
| ep_sv | system | 0 | 0 | 0 | 0 | 1 |  |
| cloud_link | system | 0 | 0 | 6 | 4 | 3 | yes |
| vpn | system | 0 | 0 | 0 | 0 | 0 |  |
| ext_exploit | node | 0 | 0 | 5 | 1 | 0 | yes |
| ext_auth | system of systems | 0 | 0 | 17 | 0 | 1 | yes |
| cloud_bad | system of systems | 0 | 0 | 20 | 0 | 1 | yes |
| ceil_edr | system | 0 | 0 | 0 | 0 | 0 |  |
| ceil_ext | system of systems | 0 | 0 | 1 | 0 | 0 |  |
| chan_verify | system | 0 | 0 | 0 | 0 | 0 |  |
| auth_cred | system | 0 | 0 | 2 | 1 | 7 | yes |
| exfil_esc | node | 0 | 0 | 0 | 3 | 0 | yes |
| sig_block | node | 0 | 0 | 0 | 0 | 0 |  |
| rotate | adaptation | 0 | 0 | 0 | 0 | 0 |  |
| cred_ttl | time | 0 | 0 | 0 | 0 | 0 |  |
| restore_rotate | adaptation | 0 | 0 | 0 | 0 | 0 |  |
| svc_view | adaptation | 0 | 0 | 0 | 0 | 0 |  |
| exfil_p | node | 0 | 0 | 0 | 6 | 0 | yes |
| objective | attacker | 0 | 0 | 0 | 15 | 1 | yes |
| val_sv | system | 0 | 0 | 0 | 0 | 0 |  |
| dval_sv | system | 0 | 0 | 0 | 3 | 0 | yes |
| exc_share | system | 0 | 0 | 0 | 0 | 0 |  |
| zone_conn | system | 0 | 0 | 4 | 6 | 2 | yes |
| ad_reach | system | 0 | 0 | 0 | 0 | 0 |  |
| hand_delay | time | 0 | 0 | 0 | 1 | 1 |  |
| reconf_time | time | 0 | 0 | 0 | 2 | 0 |  |
| ctl_link | system | 0 | 0 | 0 | 0 | 0 |  |
| repl_delay | time | 0 | 0 | 0 | 0 | 0 |  |
| dns | system | 0 | 0 | 1 | 0 | 0 |  |
| n_chan | system | 0 | 0 | 5 | 1 | 2 | yes |
| stage_time | time | 0 | 0 | 3 | 2 | 0 |  |
| cap_drift | attacker | 0 | 0 | 2 | 0 | 1 |  |
| topology | setup | 0 | 0 | 0 | 0 | 0 |  |
| gamma | setup | 0 | 0 | 0 | 0 | 0 |  |
