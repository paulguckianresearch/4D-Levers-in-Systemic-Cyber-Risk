"""Declared 4D timing revision v0.2; original v0.27 source is unchanged.
Attack cadence throttles ALL attack-transition hooks; existing timers remain in
wall ticks. Defence delay is ONE incident mobilisation lag after first evidence,
not a repeated per-node evidence delay. Period=1, lag=0 reproduces v0.27.
"""
import engine_4c_v027 as E
import numpy as np
ATTACK_HOOKS=('_deliver','_advance_residents','_controller_step','_master_push','_channel_push','_trigger','_retool_retry','_attacker','_reconfigure','_impact_step')
REACTIVE_HOOKS=('_apply_pending_blocks','_finish_rebuilds','_hand_updates','_block_dom','_adapt_dom','_queue_step','_tactical_dom')
class TimingEngine(E.Engine4C):
 def __init__(self,*args,attack_period=1,response_lag=0,**kwargs):
  if int(attack_period)!=attack_period or attack_period<1 or int(response_lag)!=response_lag or response_lag<0:raise ValueError('invalid clock settings')
  self.attack_period=int(attack_period);self.response_lag=int(response_lag);self.first_evidence=None;self.first_response=None;self.first_containment=None;self.contamination_at_containment=None;self.planes_at_containment=None;self.contamination_at_response=None;self.authority_at_response=None;self._deferred_refs={};self.trace=[];self.hook_calls={k:[] for k in ATTACK_HOOKS};self.response_calls=[]
  super().__init__(*args,**kwargs)
 def attack_due(self):return (self._tick-1)%self.attack_period==0
 def mark_evidence(self,tick):
  if self.first_evidence is None:self.first_evidence=int(tick)
 def ready(self):
  if self.first_evidence is None:
   for di,d in enumerate(self.domains):
    vm=self._vm_of.get(id(d),d.mask)
    alarm=(self._alarm>=0)&vm&~self.isolated&((self.state==E.COMPROMISED)|(self._inf_ref>=0))
    if alarm.any() or self._observe_dom(di).any():self.mark_evidence(self._tick);break
  return self.response_lag==0 or (self.first_evidence is not None and self._tick>=self.first_evidence+self.response_lag)
 def _seen_ref(self,ref,tick):
  if not self._sig or ref in self._known_refs:return
  self.mark_evidence(tick)
  if self.response_lag==0 or self.ready():return super()._seen_ref(ref,tick)
  self._deferred_refs.setdefault(int(ref),int(tick))
 def note_response(self):
  if self.first_response is None:
   self.first_response=int(self._tick);self.contamination_at_response=float((self.state[self._def_idx]==E.COMPROMISED).mean());self.authority_at_response=int(sum(self.state[m]==E.COMPROMISED for m in self._cp_set))
 def note_containment(self):
  if self.first_containment is None:
   self.first_containment=int(self._tick);self.contamination_at_containment=float((self.state[self._def_idx]==E.COMPROMISED).mean());self.planes_at_containment=int(sum(self.state[m]==E.COMPROMISED for m in self._cp_set))
 def _isolate_node(self,j):
  if not self.isolated[j] and (self.state[j]==E.COMPROMISED or self._inf_ref[j]>=0):self.note_containment()
  if not self.isolated[j]:self.note_response()
  return super()._isolate_node(j)
 def _auto_reset(self,j):
  if self.state[j]==E.COMPROMISED:self.note_response();self.note_containment()
  return super()._auto_reset(j)
 def _cut_apply(self,c):
  # This records an executed cut action; it is not proof every cut removes a live path.
  self.note_response();return super()._cut_apply(c)
 def _record(self,tick):
  super()._record(tick)
  self.trace.append([int(tick),float(self._last_share),float(self._nval[self._down].sum()/self._nval_tot),int(sum(self.state[m]==E.COMPROMISED for m in self._cp_set))])
 def run(self):
  if self._kind not in ('intrusion','implant','malware','stealer'):
   raise ValueError('Timing v0.2 excludes campaign/delayed phase-switch attacks')
  return super().run()
def make_attack_hook(name):
 base=getattr(E.Engine4C,name)
 def hook(self,*args,**kw):
  if not self.attack_due():return
  self.hook_calls[name].append(int(self._tick))
  result=base(self,*args,**kw)
  if name=='_impact_step' and self.trace and self.trace[-1][0]==self._tick:
   self.trace[-1][2]=float(self._nval[self._down].sum()/self._nval_tot)
  return result
 return hook
def make_reactive_hook(name):
 base=getattr(E.Engine4C,name)
 def hook(self,*args,**kw):
  if not self.ready():return
  self.response_calls.append((name,int(self._tick)))
  if name=='_apply_pending_blocks' and self._deferred_refs:
   refs=list(self._deferred_refs);self._deferred_refs.clear()
   for ref in refs:E.Engine4C._seen_ref(self,ref,self._tick)
  if name=='_apply_pending_blocks':
   before=sum(len(b) for b in self.blacklist.values());result=base(self,*args,**kw)
   if sum(len(b) for b in self.blacklist.values())>before:self.note_response()
   return result
  return base(self,*args,**kw)
 return hook
for _name in ATTACK_HOOKS:setattr(TimingEngine,_name,make_attack_hook(_name))
for _name in REACTIVE_HOOKS:setattr(TimingEngine,_name,make_reactive_hook(_name))
