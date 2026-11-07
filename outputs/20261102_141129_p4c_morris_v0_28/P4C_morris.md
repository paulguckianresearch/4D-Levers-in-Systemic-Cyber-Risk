# Paper 4C global screen: Morris elementary effects (PhDPaper4C v0.28 (2026-11-02))

Every register dial and the setup variables (topology, governance scope), 20 trajectories per kind, each configuration on wirings [6801, 6802] and seeds [6901, 6902] (common random numbers). Effects are in outcome units (share of the estate, or probability) per full range of the variable, extrapolated from half-range steps, so a value can exceed 100. mu* is the mean absolute effect, sigma its spread across trajectories: a large sigma with a small mu* is a variable that matters only in part of the space. A variable is kept for Stage 2 (Sobol) if mu* or sigma reaches 5 points on any outcome.

## intrusion

| variable | layer | mu* collapse | sigma collapse | mu* furthest | mu* data loss | mu* service loss | kept |
|---|---|---|---|---|---|---|---|
| c2_share | system | 44 | 96 | 27 | 10 | 3 | yes |
| g | system | 58 | 94 | 31 | 3 | 4 | yes |
| ext_bad | system of systems | 25 | 67 | 28 | 2 | 2 | yes |
| n_ext | system of systems | 22 | 66 | 25 | 6 | 6 | yes |
| ext_total | system of systems | 25 | 61 | 25 | 8 | 4 | yes |
| server_share | system | 12 | 54 | 15 | 1 | 9 | yes |
| n_chan | system | 12 | 54 | 8 | 1 | 1 | yes |
| seg_sv | system | 15 | 52 | 10 | 4 | 1 | yes |
| size | system | 15 | 45 | 15 | 3 | 3 | yes |
| visibility | node | 9 | 41 | 2 | 1 | 5 | yes |
| ext_share | node | 9 | 38 | 4 | 0 | 5 | yes |
| atk_cap | attacker | 12 | 38 | 8 | 7 | 11 | yes |
| seg_ep | system | 8 | 33 | 13 | 4 | 2 | yes |
| iface_closed | node | 9 | 30 | 21 | 4 | 12 | yes |
| chan | system | 6 | 27 | 1 | 1 | 1 | yes |
| remote_share | system | 12 | 27 | 8 | 3 | 2 | yes |
| chan_verify | system | 6 | 27 | 4 | 4 | 0 | yes |
| ad_reach | system | 6 | 27 | 3 | 4 | 1 | yes |
| managed | system | 6 | 27 | 1 | 1 | 1 | yes |
| theta | operator | 8 | 24 | 4 | 2 | 1 | yes |
| atk_budget | attacker | 5 | 22 | 1 | 1 | 1 | yes |
| retool | attacker | 6 | 20 | 5 | 1 | 1 | yes |
| node_reconf | attacker | 6 | 19 | 3 | 3 | 6 | yes |
| ext_auth | system of systems | 6 | 19 | 14 | 5 | 4 | yes |
| concentration | system | 3 | 14 | 1 | 1 | 0 | yes |
| fanout | operator | 3 | 14 | 1 | 1 | 0 | yes |
| tac_budget | adaptation | 3 | 14 | 2 | 2 | 1 | yes |
| def_cap | adaptation | 3 | 14 | 3 | 1 | 1 | yes |
| manual_delay | time | 3 | 14 | 1 | 1 | 1 | yes |
| t_clean | time | 3 | 14 | 1 | 3 | 1 | yes |
| t_cut | time | 3 | 14 | 4 | 0 | 3 | yes |
| payload_delay | attacker | 3 | 14 | 2 | 2 | 8 | yes |
| cloud_share | system | 3 | 14 | 7 | 12 | 5 | yes |
| ep_sv | system | 3 | 14 | 0 | 0 | 0 | yes |
| ext_exploit | node | 3 | 14 | 2 | 2 | 5 | yes |
| zone_conn | system | 3 | 14 | 1 | 0 | 0 | yes |
| reconf_time | time | 3 | 14 | 4 | 3 | 8 | yes |
| chan_cov | system | 3 | 14 | 5 | 1 | 2 | yes |
| chan_span | system | 3 | 14 | 1 | 1 | 0 | yes |
| dose | adaptation | 3 | 13 | 0 | 0 | 4 | yes |
| redundancy | operator | 2 | 11 | 0 | 0 | 0 | yes |
| rotate | adaptation | 2 | 11 | 1 | 0 | 0 | yes |
| dns | system | 1 | 5 | 0 | 1 | 0 | yes |
| objective | attacker | 1 | 5 | 0 | 14 | 0 | yes |
| supplied_x | node | 0 | 0 | 0 | 0 | 0 |  |
| supplied_a | node | 0 | 0 | 1 | 1 | 1 |  |
| x_rate | node | 0 | 0 | 4 | 5 | 7 | yes |
| a_rate | node | 0 | 0 | 5 | 1 | 8 | yes |
| rate_var | node | 0 | 0 | 2 | 4 | 0 | yes |
| blind_delay | node | 0 | 0 | 0 | 0 | 1 |  |
| coverage | system | 0 | 0 | 5 | 2 | 6 | yes |
| inequality | operator | 0 | 0 | 1 | 0 | 1 |  |
| block_delay | time | 0 | 0 | 0 | 0 | 0 |  |
| c_s | time | 0 | 0 | 5 | 4 | 2 | yes |
| obs_interval | time | 0 | 0 | 1 | 1 | 0 |  |
| detect_latency | time | 0 | 0 | 0 | 1 | 0 |  |
| manual_scope | adaptation | 0 | 0 | 0 | 0 | 0 |  |
| auto_clean | adaptation | 0 | 0 | 0 | 0 | 0 |  |
| rebuild_time | adaptation | 0 | 0 | 1 | 0 | 4 | yes |
| queue_order | adaptation | 0 | 0 | 0 | 0 | 0 |  |
| dormant_share | attacker | 0 | 0 | 0 | 0 | 0 |  |
| dormant_delay | attacker | 0 | 0 | 0 | 0 | 0 |  |
| cap_spread | attacker | 0 | 0 | 0 | 0 | 0 |  |
| fixed_clock | attacker | 0 | 0 | 0 | 0 | 0 |  |
| ep_conn | system | 0 | 0 | 1 | 0 | 0 |  |
| cloud_link | system | 0 | 0 | 1 | 0 | 1 |  |
| vpn | system | 0 | 0 | 0 | 0 | 0 |  |
| cloud_bad | system of systems | 0 | 0 | 0 | 0 | 0 |  |
| ceil_deliv | system | 0 | 0 | 0 | 0 | 2 | yes |
| ceil_edr | system | 0 | 0 | 0 | 0 | 0 |  |
| ceil_ext | system of systems | 0 | 0 | 0 | 0 | 0 |  |
| auth_cred | system | 0 | 0 | 1 | 0 | 3 | yes |
| exfil_esc | node | 0 | 0 | 0 | 0 | 0 |  |
| sig_block | node | 0 | 0 | 0 | 0 | 0 |  |
| cred_ttl | time | 0 | 0 | 0 | 0 | 0 |  |
| restore_rotate | adaptation | 0 | 0 | 0 | 0 | 0 |  |
| svc_view | adaptation | 0 | 0 | 0 | 0 | 0 |  |
| exfil_p | node | 0 | 0 | 0 | 18 | 0 | yes |
| val_sv | system | 0 | 0 | 0 | 0 | 1 |  |
| dval_sv | system | 0 | 0 | 0 | 3 | 0 | yes |
| exc_share | system | 0 | 0 | 0 | 1 | 0 |  |
| edr_site | system of systems | 0 | 0 | 0 | 0 | 0 |  |
| dns_site | system of systems | 0 | 0 | 0 | 0 | 0 |  |
| hand_delay | time | 0 | 0 | 0 | 0 | 0 |  |
| ctl_link | system | 0 | 0 | 1 | 0 | 0 |  |
| repl_delay | time | 0 | 0 | 1 | 0 | 0 |  |
| stage_time | time | 0 | 0 | 0 | 0 | 0 |  |
| cap_drift | attacker | 0 | 0 | 1 | 0 | 2 |  |
| topology | setup | 0 | 0 | 0 | 0 | 0 |  |
| gamma | setup | 0 | 0 | 0 | 0 | 0 |  |
