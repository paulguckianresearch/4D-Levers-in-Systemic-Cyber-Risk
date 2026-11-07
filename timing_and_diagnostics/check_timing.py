import json,pathlib,time,dataclasses
import numpy as np
from timing_engine import TimingEngine,E,ATTACK_HOOKS,REACTIVE_HOOKS
P=pathlib.Path(__file__).resolve().parent

def build(period=1,lag=0,seed=93001000,kind='intrusion',horizon=120,defence=True):
 d=dict(E.POINTS['middle']);d.update(kind=kind,horizon=horizon,wiring_seed=83001,flag=0.,flag_value=0.,cred_total=4)
 kn=E.Knobs(**d);sp,layout,_=E.generate(kn,0);net=E._core_build_network(sp,np.random.default_rng(kn.wiring_seed));cfg=E.make_cfg(kn,8,8,seed)
 if not defence:cfg.defender_tactical=False;cfg.defender_strategic=False
 eng=TimingEngine(sp,cfg,layout,net=E.net_for_seed(net,seed),opts=E.make_opts(kn),attack_period=period,response_lag=lag);eng.start(None)
 return eng,kn,sp,layout,net

def main():
 start=time.monotonic();passed=[]
 # Full neutral-settings equivalence for four profiles, three independent seeds.
 for kind in ['intrusion','implant','malware','stealer']:
  for seed in range(93001000,93001003):
   eng,kn,sp,layout,net=build(seed=seed,kind=kind);eng.run();got=eng.outcome();expected=E.run_one(sp,layout,net,kn,8,8,None,seed)
   assert got==expected,(kind,seed)
 passed.append('12 exact baseline outcome comparisons across four attack profiles')
 # A valid new all-route cadence must delay whole-estate growth with other routes active.
 propagation=[]
 for period in [1,2,4]:
  ts=[]
  for seed in range(93001000,93001008):
   eng,*_=build(period=period,seed=seed,horizon=168,defence=False);eng.run()
   for name,calls in eng.hook_calls.items():assert all((t-1)%period==0 for t in calls),(name,period)
   tf=next((r[0] for r in eng.trace if r[1]>=.5),None);ts.append(tf)
  propagation.append({'attack_period':period,'restricted_time_to_half_mean':float(np.mean([t if t is not None else 168 for t in ts])),'not_reached':sum(t is None for t in ts)})
 assert propagation[2]['restricted_time_to_half_mean']>propagation[0]['restricted_time_to_half_mean']
 passed.append('24 full-route attack runs: all attack hooks obey cadence and half-compromise is delayed')
 # Hand fixtures ensure each reactive route is held until first-evidence + lag.
 for evidence in ['passive','alarm','signature']:
  eng,*_=build(lag=8,kind='malware' if evidence=='signature' else 'intrusion')
  eng.o.obs_interval=1;eng.o.detect_latency=0;eng.state[:]=0;eng._inf_ref[:]=-1;eng._alarm[:]=-1;eng._known[:]=False;eng.resident.clear();eng._jobs=[];eng._job_keys.clear()
  d=eng.domains[0];vm=eng._vm_of.get(id(d),d.mask);j=int(np.flatnonzero(vm&eng._vis&~eng.isolated&~np.isin(np.arange(eng.n),list(eng._cp_set)))[0]);eng._tick=10;eng.state[j]=E.COMPROMISED;eng.comp_ref[j]=11;eng._comp_tick[j]=0
  if evidence=='alarm':eng._vis[j]=False;eng._alarm[j]=10
  if evidence=='signature':eng._vis[j]=False;eng._seen_ref(11,10);assert not eng.pending_blocks and 11 not in eng._known_refs
  assert not eng.ready() and eng.first_evidence==10,(evidence,eng.first_evidence,eng._tick)
  for t in range(10,18):
   eng._tick=t
   for name in REACTIVE_HOOKS:
    if name in ['_block_dom','_adapt_dom','_tactical_dom']:getattr(eng,name)(0,t)
    else:getattr(eng,name)(t)
  assert not eng.response_calls and not eng._known[j] and eng.first_response is None
  eng._tick=18;assert eng.ready();eng._apply_pending_blocks(18);eng._queue_step(18)
  if evidence=='signature':assert 11 in eng._known_refs and all(b[0]>=18 for b in eng.pending_blocks)
 passed.append('Passive, alarm and signature fixtures: all reactive hooks gated; deferred signatures released only at mobilisation')
 # End-to-end: no response calls before mobilisation; hunt is inside gated investigation.
 for lag in [0,8,24]:
  eng,*_=build(lag=lag);eng.run()
  if lag:
   assert all(t>=eng.first_evidence+lag for _,t in eng.response_calls)
   assert eng.first_response is None or eng.first_response>=eng.first_evidence+lag
 passed.append('End-to-end lag checks: investigation, hunt-origin and containment cannot act before mobilisation')
 report={'status':'PASS','checks':passed,'propagation':propagation,'seconds':time.monotonic()-start,'limitations':'Opportunity cadence is not uniform rescaling of wall-time timers. Lag is one-off mobilisation, not repeated per-node delay. Preventive repulsion stays active.'}
 (P/'validation.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
if __name__=='__main__':main()
