# Paper 4C global screen: Morris elementary effects (PhDPaper4C v0.29 (2026-11-02)) - stratum {'cred_total': 0, 'c2_share': 0.8}

Every register dial and the setup variables (topology, governance scope), 20 trajectories per kind, each configuration on wirings [6801, 6802, 6803, 6804] and seeds [6901, 6902, 6903, 6904] (common random numbers). Effects are in outcome units (share of the estate, or probability) per full range of the variable, extrapolated from half-range steps, so a value can exceed 100. mu* is the mean absolute effect, sigma its spread across trajectories: a large sigma with a small mu* is a variable that matters only in part of the space. A variable is kept for Stage 2 (Sobol) if mu* or sigma reaches 5 points on any outcome.

## intrusion

| variable | layer | mu* collapse | sigma collapse | mu* furthest | mu* data loss | mu* service loss | kept |
|---|---|---|---|---|---|---|---|
| iface_closed | node | 40 | 71 | 41 | 17 | 31 | yes |
| a_rate | node | 25 | 70 | 24 | 2 | 16 | yes |
| atk_cap | attacker | 29 | 59 | 18 | 8 | 17 | yes |
| t_cut | time | 22 | 57 | 8 | 2 | 8 | yes |
| tac_budget | adaptation | 22 | 54 | 13 | 6 | 15 | yes |
| zone_conn | system | 20 | 51 | 11 | 11 | 7 | yes |
| def_cap | adaptation | 29 | 47 | 11 | 4 | 8 | yes |
| chan_cov | system | 24 | 42 | 10 | 5 | 5 | yes |
| x_rate | node | 16 | 42 | 11 | 3 | 10 | yes |
| ext_auth | system of systems | 12 | 42 | 25 | 5 | 8 | yes |
| coverage | system | 23 | 41 | 20 | 10 | 16 | yes |
| ext_exploit | node | 12 | 37 | 19 | 10 | 9 | yes |
| atk_budget | attacker | 18 | 36 | 3 | 1 | 3 | yes |
| ext_total | system of systems | 13 | 34 | 13 | 8 | 9 | yes |
| n_chan | system | 16 | 32 | 11 | 3 | 4 | yes |
| blind_delay | node | 10 | 31 | 5 | 3 | 10 | yes |
| payload_delay | attacker | 12 | 30 | 4 | 3 | 4 | yes |
| manual_delay | time | 11 | 30 | 3 | 5 | 4 | yes |
| chan_span | system | 10 | 29 | 8 | 1 | 4 | yes |
| remote_share | system | 9 | 29 | 4 | 3 | 2 | yes |
| ext_bad | system of systems | 9 | 27 | 11 | 3 | 2 | yes |
| seg_ep | system | 7 | 25 | 3 | 2 | 1 | yes |
| cloud_share | system | 14 | 25 | 7 | 2 | 7 | yes |
| server_share | system | 10 | 23 | 17 | 2 | 12 | yes |
| t_clean | time | 5 | 18 | 3 | 2 | 2 | yes |
| size | system | 8 | 16 | 8 | 7 | 8 | yes |
| stage_time | time | 6 | 16 | 2 | 0 | 2 | yes |
| concentration | system | 6 | 15 | 2 | 0 | 2 | yes |
| fanout | operator | 5 | 15 | 4 | 2 | 2 | yes |
| redundancy | operator | 5 | 14 | 3 | 2 | 2 | yes |
| seg_sv | system | 6 | 14 | 6 | 1 | 5 | yes |
| supplied_a | node | 4 | 14 | 2 | 2 | 1 | yes |
| dose | adaptation | 4 | 14 | 2 | 2 | 1 | yes |
| rebuild_time | adaptation | 6 | 12 | 4 | 2 | 7 | yes |
| supplied_x | node | 5 | 12 | 4 | 1 | 3 | yes |
| visibility | node | 4 | 11 | 3 | 1 | 2 | yes |
| chan | system | 4 | 11 | 4 | 1 | 2 | yes |
| vpn | system | 2 | 10 | 1 | 0 | 1 | yes |
| cap_spread | attacker | 5 | 10 | 3 | 2 | 1 | yes |
| auth_cred | system | 3 | 10 | 0 | 0 | 4 | yes |
| cap_drift | attacker | 4 | 9 | 4 | 2 | 3 | yes |
| c_s | time | 3 | 8 | 2 | 1 | 3 | yes |
| reconf_time | time | 3 | 8 | 1 | 0 | 1 | yes |
| inequality | operator | 2 | 8 | 3 | 2 | 1 | yes |
| node_reconf | attacker | 2 | 8 | 2 | 26 | 1 | yes |
| retool | attacker | 3 | 7 | 4 | 2 | 4 | yes |
| ep_sv | system | 2 | 7 | 1 | 1 | 0 | yes |
| exfil_p | node | 2 | 7 | 0 | 19 | 0 | yes |
| managed | system | 2 | 7 | 0 | 0 | 0 | yes |
| rate_var | node | 2 | 5 | 1 | 0 | 1 |  |
| obs_interval | time | 2 | 5 | 2 | 0 | 1 |  |
| ext_share | node | 1 | 4 | 11 | 4 | 7 | yes |
| queue_order | adaptation | 1 | 4 | 3 | 1 | 2 | yes |
| dns | system | 2 | 4 | 1 | 1 | 1 |  |
| detect_latency | time | 1 | 3 | 0 | 0 | 0 |  |
| ep_conn | system | 1 | 3 | 3 | 2 | 3 | yes |
| cloud_link | system | 1 | 3 | 2 | 2 | 1 |  |
| n_ext | system of systems | 1 | 3 | 16 | 3 | 3 | yes |
| objective | attacker | 1 | 2 | 1 | 23 | 1 | yes |
| theta | operator | 0 | 0 | 4 | 1 | 2 | yes |
| block_delay | time | 0 | 0 | 0 | 0 | 0 |  |
| manual_scope | adaptation | 0 | 0 | 0 | 0 | 0 |  |
| auto_clean | adaptation | 0 | 0 | 0 | 0 | 0 |  |
| dormant_share | attacker | 0 | 0 | 0 | 0 | 0 |  |
| dormant_delay | attacker | 0 | 0 | 0 | 0 | 0 |  |
| fixed_clock | attacker | 0 | 0 | 0 | 0 | 0 |  |
| cloud_bad | system of systems | 0 | 0 | 0 | 0 | 0 |  |
| ceil_deliv | system | 0 | 0 | 1 | 0 | 1 |  |
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
| exc_share | system | 0 | 0 | 0 | 1 | 0 |  |
| edr_site | system of systems | 0 | 0 | 0 | 0 | 0 |  |
| dns_site | system of systems | 0 | 0 | 0 | 0 | 0 |  |
| ad_reach | system | 0 | 0 | 0 | 0 | 0 |  |
| hand_delay | time | 0 | 0 | 0 | 0 | 0 |  |
| ctl_link | system | 0 | 0 | 0 | 0 | 0 |  |
| repl_delay | time | 0 | 0 | 0 | 0 | 0 |  |
| topology | setup | 0 | 0 | 0 | 0 | 0 |  |
| gamma | setup | 0 | 0 | 0 | 0 | 0 |  |
