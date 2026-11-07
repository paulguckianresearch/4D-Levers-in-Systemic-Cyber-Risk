# Paper 4D mechanism-validation package v0.1 — protocol

2 November 2026. Exploratory. Development draws only. Nothing here is a confirmatory result.

## 1. Purpose

Before any further grid, establish that the engine can answer the 4D research question (loss of recoverability under sustained pressure; propagation collapse against authority lockout). Three audits, one command, measured runtime. Each audit has a yes/no first result and a set of measurement definitions that are placeholders until calibrated in development runs and then fixed.

## 2. What the package adds, and what it does not

Built on the timing revision v0.2 (`timing_engine.py`) over the unchanged Paper 4C v0.27 engine (`engine_4c_v027.py`, sha256 724a97c3…). `diag_engine.py` adds no mechanism: it adds a step loop that can be stopped and continued (`run_ticks`), an exact checkpoint (`snapshot`, a deep copy of the whole engine including all four random generators, with the team's view map re-keyed because the engine keys it by object id), per-tick state rows, and three experimenter actions that run only when called: a burst of k footholds, a change of responders, a forced plane capture. `check_diag.py` proves the loop copy and the checkpoint are exact (outcome, trace and rows identical to `TimingEngine.run()`, to a fresh run, and to the parent after a restore; equal disturbances give equal branches; the attack period and mobilisation gate survive a restore). `run_diag.py` refuses to run unless `check_diag.json` matches the current file digests.

Flags are off throughout (`flag = 0`, `flag_value = 0`, as in the timing pilot), so a run continues after the 0.8 crossing; the crossing is reconstructed from the rows. Seeds are the pilot's (wirings 84001–84002, dynamics 94001000–94001001). Runs reproduce the pilot's records key for key (checked: c0432 first crossings 8, 9, 10, 10; c0005 221; c0602 38, 40).

## 3. The audits

### A1 Sustained attack pressure
Per 100-tick window: payloads the source issued (against the exact count of re-tooling periods in the window), escalation attempts, infections, mean footholds, mean contact share, stolen credentials valid. Verdict per run: issue persists (every window exact) and activity persists (attempts + infections > 0 in every window after the first). Also reported: attacker actions after the first crossing. Runs: 6 configurations × 4 draws with defence on; c0005 and c0275 × 2 draws with reactive defence off (pure opportunity).

### A2 Authority lockout
A2.1 Static, per Control Plane: directing reach (the share of the estate the team is excluded from while it is held), whether it is inside the team's view, visible, credential holders, restorable under the dials in force, and what it would need. A2.2 Dynamic on the A1 runs under three dial sets (`default`; `rebuild5` = master_rebuild 5; `rebuild5_view` = master_rebuild 5 + svc_view 1): captures with method (access | lateral), restoration attempts and outcomes, and at the first crossing the split of the compromised share into reachable and unreachable, the planes held then and within 20 ticks after, the lowest compromised share after the crossing, and whether the excluded share ever fell. A2.3 Forced single capture: from a checkpoint at tick 20 of c0005 (no credential exposed) and c0303 (contained control), each plane is put in the attacker's hands alone and the run continued 300 ticks under each dial set; records restoration, the excluded share over time, whether the plane is still held, and whether the team isolated any node of the plane's own zone that the plane does not direct.

### A3 Recovery under sustained pressure
From a checkpoint at T0 of c0005, c0303 and c0275 (4 draws each): B0 the undisturbed continuation; Bk a burst of k clean, reachable, ordinary nodes put at stage 1 with the current payload (k = 5, 10, 20, 40); Bkc the same burst with responders × 2 from T0; Bc the capacity change alone. Per branch: peak after T0, return (inside the operating band for R consecutive ticks within the observation window), return time, crossing of 0.8 after T0, planes newly captured, final compromise, and the payloads issued after T0 against the expected count (the pressure check).

## 4. Measurement definitions: development placeholders, to be calibrated then frozen

| Quantity | Placeholder | Calibration question |
|---|---|---|
| Checkpoint tick T0 | 200 | After the transient of the selected configurations; report the parent's state at T0 |
| Contained at T0 | compromised share ≤ 0.5 | Whether planes held at T0 should also be required (c0275 holds four planes at T0 in one draw and is still "contained" by share) |
| Operating band | mean over the 50 ticks before T0 ± max(0.05, 2 sd) | Too tight where the undisturbed trajectory fluctuates: on c0005/84002 the parent spends 15% of the 100 ticks before T0 outside it (max deviation 0.17) and the undisturbed B0 "returns" after 142 ticks. Candidates: a longer pre-window; a quantile band from the parent; the B0 branch as the null against which Bk is compared |
| Residence time R | 30 ticks | Longer than one re-tooling period (20) so a return survives at least one new payload; to be set from B0's excursion lengths |
| Observation window | 400 ticks after T0 | Bounded by the horizon; a return later than this is "not recovered" |
| Burst sizes k | 5, 10, 20, 40 (of 100) | Range to bracket the margin: c0303 absorbs 40; c0005 at 40 crosses 0.8 in both draws |
| Capacity intervention | responders × 2 at T0 | Matched on state by construction (same checkpoint); the factor and a × 0.5 arm are open |
| Collapse composition | propagation if no plane held at the crossing; authority-dominant if unreachable ≥ reachable compromise at the crossing; planes within 20 ticks after reported | The 20-tick look-ahead is a reporting convenience; the split itself needs no threshold |
| Authority lockout treatment | default dials (no restoration; zone-less services out of view) and two restoration settings reported side by side | Ruling needed: which is 4D's reference (section 6) |

## 5. First result (this run, 94 tasks, 33 s on 2 workers; benchmark 0.35 s per 600-tick run)

1. Recoverability under sustained pressure is measurable. In every A3 branch the source issued 20 of 20 payloads after T0 and attacker actions continued; the undisturbed continuation of the same checkpoint is available as the null in every case; the burst, the return and the return time are computed and reproducible. What is not yet right is the band (section 4): the measure exists, its calibration does not.
2. Propagation collapse and authority lockout are distinguishable, and both occur. Under the default dials, 10 collapses in 24 runs: 5 crossed 0.8 with no plane held, of which 1 (c0005, no credential exposed) still held none 20 ticks later and 4 (all c0432) took four planes within 2 to 10 ticks of crossing; 5 (c0602, c0681) crossed with 52 to 78 per cent of the estate already unreachable and only 2 to 30 per cent of the compromise reachable. The pilot's apparent recoveries after collapse are the compromised share settling at the excluded share: in c0602 the minimum after crossing is 0.54 to 0.60 with the excluded share at 52 to 58 per cent and five planes held to the end.
3. Which captures prevent recovery, under the dials in force: all seven, permanently. `master_rebuild` is 9999, so no plane is ever restored; the third party's hypervisor (hvc, 6 per cent) is never restorable under any dial; device management (mdm, 80 per cent) and the on-premises hypervisor (hv, 14 per cent) are restorable only with `svc_view = 1`; the four Active Directory controllers (1 to 32 per cent each by configuration) are restorable with `master_rebuild < horizon` alone. Two further facts from A2.3: (a) a single captured controller becomes all four controllers within the replication delay (8 ticks) with no credential exposed at all (c0005: exclusion 6% → 14%, all held), and under `rebuild5` a restored controller is retaken by replication from its peers unless all four are restored inside the delay (c0005: retaken every time; c0303: all four cleared); (b) the team went on isolating nodes in the zone of a captured identity plane in every forced case, so the `lockout_delay` rule (locked out of the zone) does not act under the queue: it lives in `_manual_dom`, which the queue never calls. Under the queue, authority lockout is exclusion from exactly the directed nodes, plus the loss of automated defence where every console of a system is held.
4. Sustained pressure: payload issue exact and attacker activity present in every window in 76 of 76 runs, including after collapse (hundreds of actions). With reactive defence off, compromise reaches 0.90 to 0.98 and footholds fall to zero only because every held node has been escalated.

## 6. Rulings needed before the screen

1. 4D's reference treatment of authority lockout: the 4C defaults (no restoration, zone-less services unseen), or one of the restoration settings, or both as a declared setup variable. Under the defaults the authority route is absorbing by construction; the fold question is then confined to propagation, and c0005-type configurations (no credential exposed) are where it can be asked cleanly.
2. Whether replication among controllers (ctl_link 2, repl_delay 8) is a control for 4D or a fixed scenario assumption; it decides whether single-plane restoration can ever hold.
3. The band, residence and burst placeholders of section 4, after one calibration run on the chosen configurations.
4. Whether the `lockout_delay` inertness is to be left as a documented fact of the 4C model or corrected in a declared 4D revision (correcting it changes 4C's results, so the former unless there is a reason).

## 7. Running it

```
python check_diag.py                       # 7 s; must pass
python run_diag.py --benchmark             # prints the estimate for your machine
python run_diag.py --out diag_v01 --workers 8
```
Outputs: `diag_report.md` (all tables), `diag_results.jsonl.gz` (every run and branch with per-tick rows and intervention log), `manifest.json` (digests, settings, measured runtime). A changed placeholder in `run_diag.py` (`A3 = dict(...)`, `FORCE_T0`, `DIAL_SETS`) changes the manifest; use a new output folder.
