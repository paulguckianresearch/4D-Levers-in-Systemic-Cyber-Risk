# Worked example of an exchange rate (PhDPaper4C v1.1 (2026-11-05, surface validation for Paper 4D; model as v0.26/v0.27))

Stratum {'cred_total': 0, 'c2_share': 0.8}, intrusion, outcome collapse. Base configuration: the sampled configuration with observed fl nearest 0.5 (0.50), each variable at the centre of its rung (iface_closed 0.6, a_rate 0.2, atk_cap 100.0, t_cut 4, tac_budget 2.0, zone_conn 0.0, def_cap 20.0, chan_cov 1.0, x_rate 0.2, ext_auth 0.6, coverage 0.6, ext_exploit 1.0, atk_budget 2, ext_total 0.6, n_chan 1, blind_delay 200, payload_delay 1, manual_delay 1, chan_span 0.4, remote_share 0.2, ext_bad 1.0, seg_ep 8, cloud_share 0.6, server_share 0.6, t_clean 4, size 200, stage_time 0, concentration 0.4, fanout 0.1, redundancy 1, seg_sv 2, supplied_a 1.0, dose 1.0, rebuild_time 20, supplied_x 0.4, visibility 0.0, chan 0.2, vpn 1.0, cap_spread 0.2, auth_cred 100.0, cap_drift 0.0, c_s 10, reconf_time 1, inequality 0.6, node_reconf 4, retool 20, ep_sv 0.4, exfil_p 0.2, managed 0.6, ext_share 0.0, queue_order value, ep_conn 0.0, n_ext 2, objective destroy, theta all, dval_sv 80.0); other dials neutral.

Surface prediction (pair-and-square surface over 291,584 sampled points, R2 86% in sample, -51% on held-out families). Move A: iface_closed 0.6 -> 0.8, predicted -8.6 points. Move B, chosen as the rung on coverage whose prediction is nearest: 0.6 -> 0.2, predicted -2.0 points.

Observed on 160 fresh paired draws (40 wirings 9200001.., 4 seeds 9300001..; intervals: percentile bootstrap over wirings, 2,000 resamples):

| move | predicted | observed mean change | 95% interval | share of draws below base |
|---|---|---|---|---|
| A: iface_closed 0.6 -> 0.8 | -8.6 | -11.9 | [-21.9, -1.2] | 0.14 |
| B: coverage 0.6 -> 0.2 | -2.0 | +6.9 | [+1.9, +13.1] | 0.03 |
| A minus B | -6.6 | -18.8 | [-31.2, -6.2] | |

Base collapse on these draws: 0.181; after A 0.062; after B 0.250.

Reading: the surface's exchange rate is confirmed at this point of the space if the two observed changes agree with each other (the A minus B interval includes zero) and each with its prediction (the prediction inside the move's interval). A marginal is a local slope; a one-rung move is a finite step, so a difference of a few points between prediction and observation is the curvature the surface does not carry, not a failure of the ranking.
