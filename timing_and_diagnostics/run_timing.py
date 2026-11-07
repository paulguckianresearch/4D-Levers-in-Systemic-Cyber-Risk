"""Small, resumable timing pilot. NumPy only. Compact results and selected traces."""
import argparse,concurrent.futures,csv,dataclasses,hashlib,itertools,json,os,pathlib,statistics,sys,time,zipfile
import numpy as np
from timing_engine import TimingEngine,E
ROOT=pathlib.Path(__file__).resolve().parent

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def simulate(task):
 config,period,lag,wi,si,horizon=task;w=84001+wi;seed=94001000+si
 d=dict(E.POINTS['middle']);d.update({k:v for k,v in config.items() if k in ['cred_total','ad_reach','tac_budget','coverage','zone_conn']});d.update(detect_latency=0,obs_interval=1,kind='intrusion',topology='chain',size=100,wiring_seed=w,horizon=horizon,flag=0.,flag_value=0.)
 kn=E.Knobs(**d);sp,layout,built=E.generate(kn,0);net=E._core_build_network(sp,np.random.default_rng(w));eng=TimingEngine(sp,E.make_cfg(kn,8,8,seed),layout,net=E.net_for_seed(net,seed),opts=E.make_opts(kn),attack_period=period,response_lag=lag);eng.start(None);eng.run()
 trace=eng.trace;first=next((t for t,c,u,_ in trace if c>=.8 or u>=.8),None)
 r={'key':f"{config['id']}|{period}|{lag}|{w}|{seed}",'configuration':config['id'],'attack_period':period,'response_lag':lag,'wiring':w,'seed':seed,'collapse':int(first is not None),'first_collapse_tick':first,'standing_ticks':first if first is not None else horizon,'first_evidence_tick':eng.first_evidence,'mobilisation_tick':eng.first_evidence+lag if eng.first_evidence is not None else None,'first_response_action_tick':eng.first_response,'contamination_at_first_response':eng.contamination_at_response,'captured_planes_at_first_response':eng.authority_at_response,'late_compromise':statistics.mean(x[1] for x in trace[-100:]),'late_unavailable':statistics.mean(x[2] for x in trace[-100:]),'final_compromise':trace[-1][1],'final_unavailable':trace[-1][2],'first_node_containment_tick':eng.first_containment,'contamination_at_node_containment':eng.contamination_at_containment,'captured_planes_at_node_containment':eng.planes_at_containment,'alarms':int(eng.n_alarms),'hunt_discoveries':int(eng.n_hunt),'queue_peak':int(eng.q_max),'realised':E.realised(kn,built)}
 if wi==0 and si==0:r['selected_trace']={'columns':['tick','compromise','unavailable_value','planes_held'],'rows':[v for v in trace if v[0]<=30 or v[0]%10==0]}
 return r

def summarise(out):
 groups={};rows=[]
 with (out/'results.jsonl').open() as f:
  for line in f:
   r=json.loads(line);groups.setdefault((r['configuration'],r['attack_period'],r['response_lag']),[]).append(r)
 for key,rr in sorted(groups.items()):
  row=dict(configuration=key[0],attack_period=key[1],response_lag=key[2],runs=len(rr),wirings=len({r['wiring'] for r in rr}))
  for metric in ['collapse','standing_ticks','late_compromise','late_unavailable','first_response_action_tick','contamination_at_first_response']:
   vals=[r[metric] for r in rr if r[metric] is not None];row[metric]=statistics.mean(vals) if vals else '';row[metric+'_observed']=len(vals)
  rows.append(row)
 with (out/'summary.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 with zipfile.ZipFile(out/'upload_timing_results.zip','w',zipfile.ZIP_DEFLATED,compresslevel=1) as z:
  for n in ['manifest.json','results.jsonl','summary.csv']:z.write(out/n,n)
  for n in ['timing_engine.py','run_timing.py','check_timing.py','selection.json','PROTOCOL.txt','validation.json','benchmark.json']:
   if (ROOT/n).exists():z.write(ROOT/n,n)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--out',default='timing_pilot');ap.add_argument('--workers',type=int,default=min(8,os.cpu_count() or 1));ap.add_argument('--wirings',type=int,default=4);ap.add_argument('--seeds',type=int,default=4);ap.add_argument('--horizon',type=int,default=600);ap.add_argument('--execute',action='store_true');ap.add_argument('--limit',type=int);a=ap.parse_args()
 if min(a.workers,a.wirings,a.seeds,a.horizon)<1 or a.horizon<100 or (a.limit is not None and a.limit<1):ap.error('positive counts; horizon >=100')
 configs=json.loads((ROOT/'selection.json').read_text())['configurations'];tasks=[(c,p,l,w,s,a.horizon) for c in configs for p,l in itertools.product([1,2,4],[0,8,24]) for w in range(a.wirings) for s in range(a.seeds)]
 record={'version':'4D timing 0.2','status':'exploratory pilot, not confirmation','configurations':configs,'attack_periods':[1,2,4],'response_lags':[0,8,24],'wirings':a.wirings,'seeds':a.seeds,'horizon':a.horizon,'initial':'clean','fixed_overrides':{'detect_latency':0,'obs_interval':1},'planned_runs':len(tasks),'hashes':{n:digest(ROOT/n) for n in ['engine_4c_v027.py','timing_engine.py','run_timing.py','selection.json']},'seed_ranges':{'wiring_start':84001,'dynamics_start':94001000}}
 out=pathlib.Path(a.out);out.mkdir(parents=True,exist_ok=True);mp=out/'manifest.json'
 if mp.exists():
  if json.loads(mp.read_text())!=record:raise ValueError('Scientific manifest differs; choose a new folder')
 else:mp.write_text(json.dumps(record,indent=2))
 print(f'{len(configs)} configurations x 9 timing combinations: {len(tasks):,} planned runs',flush=True)
 if not a.execute:print('Plan saved; add --execute to run.',flush=True);return
 done=set();rp=out/'results.jsonl'
 if rp.exists():
  print('Reading compact resume records...',flush=True)
  with rp.open() as f:
   for i,line in enumerate(f,1):
    try:r=json.loads(line)
    except ValueError:raise ValueError(f'Incomplete resume record at line {i}; no records deleted. Repair the final line before resuming.')
    if r['key'] in done:raise ValueError('Duplicate key in existing results')
    done.add(r['key'])
 tasks=[t for t in tasks if f"{t[0]['id']}|{t[1]}|{t[2]}|{84001+t[3]}|{94001000+t[4]}" not in done]
 if a.limit:tasks=tasks[:a.limit]
 print(f'{len(done):,} already saved; executing {len(tasks):,} with {a.workers} workers',flush=True)
 start=time.monotonic();count=0
 with rp.open('a') as f:
  if a.workers==1:
   for t in tasks:
    f.write(json.dumps(simulate(t),separators=(',',':'))+'\n');f.flush();count+=1
    if count%12==0 or count==len(tasks):print(f'{len(done)+count}/{record["planned_runs"]} saved | {time.monotonic()-start:.1f}s',flush=True)
  else:
   # Bounded submissions avoid holding a whole large campaign in memory.
   with concurrent.futures.ProcessPoolExecutor(a.workers) as pool:
    it=iter(tasks);pending=set()
    for _ in range(min(len(tasks),a.workers*2)):
     pending.add(pool.submit(simulate,next(it)))
    while pending:
     finished,pending=concurrent.futures.wait(pending,return_when=concurrent.futures.FIRST_COMPLETED)
     for future in finished:
      r=future.result();f.write(json.dumps(r,separators=(',',':'))+'\n');f.flush();count+=1
      if count%12==0 or count==len(tasks):print(f'{len(done)+count}/{record["planned_runs"]} saved | {time.monotonic()-start:.1f}s',flush=True)
      t=next(it,None)
      if t is not None:pending.add(pool.submit(simulate,t))
 if rp.exists():summarise(out)
 elapsed=time.monotonic()-start;print(f'Completed this invocation: {count} runs in {elapsed:.1f}s. Upload {out / "upload_timing_results.zip"}',flush=True)
 (out/'invocation.json').write_text(json.dumps({'runs':count,'seconds':elapsed,'workers':a.workers,'already_saved':len(done)},indent=2))
if __name__=='__main__':main()
