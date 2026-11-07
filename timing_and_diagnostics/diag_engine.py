"""Paper 4D mechanism-validation engine v0.1 (2 November 2026).

A diagnostic subclass of the timing revision (timing_engine.TimingEngine v0.2)
over the unchanged Paper 4C v0.27 engine. It adds no mechanism. It adds:

  run_ticks(a, b)   the v0.27 step loop run from tick a to tick b inclusive, so a
                    run can be stopped, copied and continued. run_ticks(1, H) is
                    checked against Engine4C.run() outcome for outcome.
  snapshot()        a checkpoint: a deep copy of the whole engine, every array,
                    queue, store and all four random generators included.
                    Continuing the copy reproduces continuing the original
                    tick for tick (check_diag.py verifies this).
  rows              one state row per tick beyond the timing trace: excluded
                    share, reachable compromise, queue, footholds, payloads
                    issued, escalations, infections, stolen credentials, contact.
  disturb_burst(k)  an experimenter's disturbance: k clean, reachable, ordinary
                    estate nodes are put at stage 1 (a foothold with the current
                    payload). Drawn from a separate generator so the engine's own
                    draws are not moved.
  set_capacity(n)   change the team's responders from this tick.
  force_capture(m)  put Control Plane m in the attacker's hands now (for the
                    lockout audit), with exclusion recomputed.

Everything a disturbance or intervention does is logged in self.interventions
and copied into the run record. None of it runs unless called.
"""
import copy
import numpy as np
import engine_4c_v027 as E
from timing_engine import TimingEngine

MARK_TICKS = E.MARK_TICKS
COMPROMISED = E.COMPROMISED


class DiagEngine(TimingEngine):
    def __init__(self, *args, **kw):
        self.rows = []
        self.interventions = []
        self.isolation_log = []          # (tick, node) each time the team isolates a node
        self._disturb_rng = None
        self._stopped_at = -1
        super().__init__(*args, **kw)

    def _isolate_node(self, j):
        if not self.isolated[j]:
            self.isolation_log.append((int(self._tick), int(j)))
        return super()._isolate_node(j)

    # ---- state rows ---------------------------------------------------------
    def state_row(self):
        comp = self.state == COMPROMISED
        d = self._def_idx
        ex = self._excl
        n_est = max(len(d), 1)
        held_ord = comp & self._ord
        foot = held_ord & ~self.isolated & (self._L < getattr(self, "_want", 0.0))
        planes = [int(m) for m in self._cp_set if comp[m]]
        waiting = sum(1 for jb in self._jobs if jb["left"] < 0)
        busy = sum(1 for jb in self._jobs if jb["left"] >= 0)
        held_idx = np.flatnonzero(held_ord)
        return dict(
            tick=int(self._tick),
            comp=float(comp[d].sum()) / n_est,                         # compromised share of the estate
            unavail=float(self._nval[self._down].sum() / self._nval_tot),
            excl=float(ex[d].mean()),                                  # share of the estate the team cannot reach
            comp_reach=float((comp[d] & ~ex[d]).sum()) / n_est,        # compromised AND reachable by the team
            comp_excl=float((comp[d] & ex[d]).sum()) / n_est,          # compromised AND unreachable
            planes_held=len(planes),
            planes=planes,
            sys_held=int(sum(self._system_held(k) for k in range(self.K))),
            dns_held=int(self._dns_held()),
            q_wait=int(waiting), q_busy=int(busy),
            cap=int(self.domains[0].tac_budget),
            footholds=int(foot.sum()),
            refs=len(self.first_seen_ref),                             # payloads the source has issued so far
            n_esc=int(self.n_esc), n_esc_won=int(self.n_esc_won),
            n_inf=int(self.n_infected), n_rep=int(self.n_repelled),
            n_alarm=int(self.n_alarms), n_hunt=int(self.n_hunt),
            stolen=int(sum(len(v) for v in self._stolen.values())),
            contact=float(self._contact[held_idx].mean()) if held_idx.size else 1.0,
            pend_blocks=len(self.pending_blocks),
            known_refs=len(self._known_refs),
            isolated=int((self.isolated & self._ord).sum()),
            down=int((self._down & self._ord).sum()),
            ext_bad=int(sum(1 for x in self._ext if self.state[x] == COMPROMISED)),
        )

    # ---- the v0.27 step loop, run over a tick range ------------------------
    def run_ticks(self, start: int, stop: int):
        """Engine4C.run() body, verbatim, for tick in [start, stop]. Returns the
        tick it stopped at (stop, or earlier if a flag fired)."""
        if self._kind not in ("intrusion", "implant", "malware", "stealer"):
            raise ValueError("Timing v0.2 excludes campaign/delayed phase-switch attacks")
        cfg = self.cfg
        if not cfg.strategic_reconfigure or cfg.blind_mode or cfg.drift_rate > 0:
            raise ValueError("Engine4C runs the austere E8 configuration only")
        O = max(1, int(self.o.obs_interval))
        nd = range(len(self.domains))
        last = start - 1
        for tick in range(start, stop + 1):
            self._tick = tick
            if self._phase in ("stealer", "idle") and self._kind in ("campaign", "delayed") and tick > int(self.o.handoff):
                self._apply_kind("intrusion")
                self._spend_credentials(tick)
            if self._c2:
                self._contact_update()
            self._deliver(tick)
            self._advance_residents(tick)
            if self._roles:
                if self._cred:
                    self._controller_step(tick)
            self._master_push(tick)
            if self._roles:
                if self._channels:
                    self._channel_push(tick)
                if self._payload:
                    self._trigger(tick)
                    self._retool_retry(tick)
                self._hand_updates(tick)
            self._apply_pending_blocks(tick)
            if self._manual or self._mr_on:
                self._finish_rebuilds(tick)
            if O > 1 and tick % O == 0:
                for di in nd:
                    self._snap[di] = self._picture(self.domains[di])
            self._note_observed()
            if cfg.defender_tactical:
                for di in nd:
                    if tick % self.domains[di].block_cycle == 0:
                        self._block_dom(di, tick)
            if self.adapt_on:
                for di in nd:
                    if tick % self.domains[di].strategic_cycle == 0:
                        self._adapt_dom(di, tick)
            if cfg.defender_tactical:
                if self._queue:
                    self._queue_step(tick)
                else:
                    for di in nd:
                        if tick % self.domains[di].tactical_cycle == 0:
                            self._tactical_dom(di, tick)
            if cfg.attacker_on and tick % cfg.attacker_cycle == 0:
                self._attacker(tick)
            self._record(tick)
            last = tick
            flagged = False
            if self._roles:
                self._reconfigure(tick)
                self.impact += float(self._rec[self._def_idx].sum()) / max(len(self._def_idx), 1)
                if self._stages:
                    self._impact_step(tick)
                    out_v = float(self._nval[self._down].sum()) / self._nval_tot
                    self.svc_att += out_v
                    self.svc_def += float(self._nval[self.isolated & ~self._down].sum()) / self._nval_tot
                    if tick in MARK_TICKS:
                        self._marks[tick] = (float(self._dval[self._exfil].sum() / self._dval_tot),
                                             float(self.svc_att / tick), float(self._last_share))
                    if self.o.flag_value > 0 and out_v >= self.o.flag_value:
                        self.t_flag = tick
                        self.which_flag = 2
                        flagged = True
                if not flagged and self._flag > 0 and self._last_share >= self._flag:
                    self.t_flag = tick
                    self.which_flag = 1
                    flagged = True
            self.rows.append(self.state_row())
            if flagged:
                self._stopped_at = tick
                break
        return last

    def run(self):
        self.run_ticks(1, int(self.cfg.horizon))
        return self.rec

    # ---- checkpoints --------------------------------------------------------
    def snapshot(self):
        """Deep copy, then re-key the team's view map. The engine keys _vm_of by
        id(domain) and falls back to the zone mask for an unknown id, so a plain
        deep copy would silently drop svc_view after a restore."""
        memo = {}
        s = copy.deepcopy(self, memo)
        s._vm_of = {id(memo[id(d)]): s._vm_of[id(d)] for d in self.domains}
        return s

    # ---- interventions ------------------------------------------------------
    def _log(self, **kw):
        kw["tick"] = int(self._tick)
        self.interventions.append(kw)
        return kw

    def disturb_burst(self, k: int, seed: int, reachable_only: bool = True):
        """Put k clean estate nodes at stage 1 with the source's current payload.
        Candidates: ordinary estate nodes, clean, not infected, not isolated, not
        a Control Plane, and (default) not under a captured plane, so the team
        could in principle act on them. Returns the nodes chosen."""
        if self._disturb_rng is None:
            self._disturb_rng = np.random.default_rng([int(seed) & 0x7FFFFFFF, 4401])
        clean = (self.state != COMPROMISED) & (self._inf_ref < 0) & ~self.isolated & self._ord
        if reachable_only:
            clean &= ~self._excl
        cands = np.flatnonzero(clean)
        k_eff = int(min(k, cands.size))
        chosen = self._disturb_rng.choice(cands, size=k_eff, replace=False) if k_eff else np.array([], dtype=int)
        ref = self._source_reference(self._tick) if self._payload else self.atk_reference
        for j in chosen.tolist():
            self.state[j] = COMPROMISED
            self.comp_ref[j] = ref
            self._comp_tick[j] = self._tick
            self._cause[j] = 1
            self._L[j] = float(self.o.auth_conn)
            self._inf_ref[j] = -1
        self._log(kind="burst", requested=int(k), applied=k_eff, nodes=[int(x) for x in chosen], ref=int(ref))
        return chosen

    def set_capacity(self, responders: int):
        d = self.domains[0]
        before = int(d.tac_budget)
        d.tac_budget = int(max(1, responders))
        self._log(kind="capacity", before=before, after=int(d.tac_budget))
        return before

    def force_capture(self, m: int, how: str = "forced"):
        self.state[m] = COMPROMISED
        self.comp_ref[m] = self.atk_reference
        self._cause[m] = 3
        self._cp_how[m] = how
        self._cap_tick.setdefault(int(m), int(self._tick))
        self._comp_tick[m] = self._tick
        self._update_exclusion()
        self._log(kind="force_capture", node=int(m), excl_after=float(self._excl[self._def_idx].mean()))

    # ---- plane facts --------------------------------------------------------
    def plane_table(self):
        """Static facts per Control Plane: reach, whether the team can see and
        restore it under the dials in force, and what would make it restorable."""
        names = {v: k for k, v in self.net.index.items()}
        en = self.rel_enabled[E.DIRECTING]
        vm = self._vm_of[id(self.domains[0])]
        out = []
        for m in sorted(self._cp_set):
            reach = en[m] & self._ord
            zoneless = bool(self.cluster_of[m] < 0)
            in_view = bool(vm[m])
            out.append(dict(
                node=int(m), name=names[m], zone=int(self.cluster_of[m]), zoneless=zoneless,
                reach_estate=int(reach.sum()), reach_share=float(reach.sum()) / max(len(self._def_idx), 1),
                in_team_view=in_view, visible=bool(self._vis[m]), cred_holders=len(self._cred.get(m, [])),
                restorable_now=bool(self._cp_rebuild and in_view),
                needs=("master_rebuild < horizon" if not self._cp_rebuild else "") +
                      (("; svc_view=1" if zoneless else "; (in view)") if not in_view else ""),
            ))
        return out
