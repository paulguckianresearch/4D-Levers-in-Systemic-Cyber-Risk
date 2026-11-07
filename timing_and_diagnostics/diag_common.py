"""Shared builder for the 4D diagnostic package. Reproduces run_timing.simulate's
construction exactly (same knobs, same seed arithmetic), with optional dial
overrides for the lockout audit (master_rebuild, svc_view) and a kind/topology
override. Any override is written into the run record."""
import hashlib
import json
import pathlib
import numpy as np
import engine_4c_v027 as E
from diag_engine import DiagEngine

ROOT = pathlib.Path(__file__).resolve().parent
WIRING0, SEED0 = 84001, 94001000          # the timing pilot's seed origins (PROTOCOL.txt)
PILOT_KEYS = ["cred_total", "ad_reach", "tac_budget", "coverage", "zone_conn"]


def digest(name: str) -> str:
    return hashlib.sha256((ROOT / name).read_bytes()).hexdigest()


def configurations():
    return json.loads((ROOT / "selection.json").read_text())["configurations"]


def knobs_for(config: dict, wiring: int, horizon: int, over: dict = None) -> E.Knobs:
    d = dict(E.POINTS["middle"])
    d.update({k: v for k, v in config.items() if k in PILOT_KEYS})
    d.update(detect_latency=0, obs_interval=1, kind="intrusion", topology="chain", size=100,
             wiring_seed=wiring, horizon=horizon, flag=0.0, flag_value=0.0)
    if over:
        d.update(over)
    return E.Knobs(**d)


def build(config: dict, period=1, lag=0, wi=0, si=0, horizon=600, over: dict = None,
          attacker_on=True, defence_on=True):
    """Return (engine, knobs, layout, built). Seeds follow the pilot: wiring
    WIRING0 + wi, dynamics SEED0 + si."""
    w, seed = WIRING0 + wi, SEED0 + si
    kn = knobs_for(config, w, horizon, over)
    sp, layout, built = E.generate(kn, 0)
    net = E._core_build_network(sp, np.random.default_rng(w))
    cfg = E.make_cfg(kn, 8, 8, seed)
    if not attacker_on:
        cfg.attacker_on = False
    if not defence_on:
        cfg.defender_tactical = False
        cfg.defender_strategic = False
    eng = DiagEngine(sp, cfg, layout, net=E.net_for_seed(net, seed), opts=E.make_opts(kn),
                     attack_period=period, response_lag=lag)
    eng.start(None)
    return eng, kn, layout, built


def first_crossing(rows, level=0.8):
    for r in rows:
        if r["comp"] >= level or r["unavail"] >= level:
            return r
    return None
