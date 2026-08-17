import gc,json,os,platform,random,sys,time
from pathlib import Path
import numpy as np
import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM,AutoTokenizer,__version__ as transformers_version
SEED=20260817; NB=256; CTX=32; K=4; BS=8; GROUP=64
DRAFT_ID='HuggingFaceTB/SmolLM2-135M'; TARGET_ID='HuggingFaceTB/SmolLM2-360M'
OUT=Path('results/thresholdspec-signed-exp004'); OUT.mkdir(parents=True,exist_ok=True)
random.seed(SEED); torch.manual_seed(SEED); torch.set_num_threads(min(4,os.cpu_count() or 4))
CORPUS='''Scientific progress is fastest when a hypothesis is precise enough to fail. A useful experiment separates observation from interpretation, preserves a baseline, and records negative results.\n\nA local language model runs under strict resource constraints. Memory capacity determines whether weights fit, while memory bandwidth can dominate autoregressive decoding.\n\nIn software engineering, a small reproducible test is more valuable than a large demonstration that cannot isolate cause. Freeze the input, seed randomness, collect raw measurements, and compare the smallest intervention against a strong baseline.\n\nOnce upon a time, a curious child found a brass key beneath an old tree. The key did not open the garden gate, the attic trunk, or the wooden cabinet. At sunset the child noticed a tiny door hidden behind ivy.\n\nThe train reached the coastal station before dawn. Rain tapped against the windows while passengers gathered their bags. A mechanic checked the brakes and waved when inspection was complete.\n\nWhen a program processes untrusted input, it should validate lengths before allocation, reject malformed encodings, and keep parsing separate from execution.\n\nA theorem is not established because many examples satisfy it. Examples can reveal structure and kill bad conjectures, but the final argument must cover every allowed case.\n\nThe city library had been renovated without losing its quiet character. Sunlight crossed the reading room while students worked beneath tall shelves.\n\nTo compare two algorithms fairly, hold the workload constant, measure warm and cold behavior separately, report variance, and include optimization overhead.\n\nA robot crossing a warehouse must plan around moving workers, temporary obstacles, battery constraints, and delayed sensor observations.\n\nThe chef tasted the sauce, lowered the heat, and added a small amount of water. The texture improved because the adjustment addressed the actual imbalance.\n\nMachine learning systems can appear confident when evidence is weak. Calibrated uncertainty distinguishes knowing from fluent guessing.\n\nIn a distributed service, retries can improve reliability or create an overload spiral. Backoff, idempotency, bounded queues, and deadlines keep failures controlled.\n\nA telescope does not make a discovery by magnifying every part of the sky equally. Observation time is limited, so astronomers allocate it toward discriminating measurements.\n\nThe old bridge was closed after sensors detected unusual vibration. Engineers compared wind, traffic, temperature, and historical measurements before examining components.\n\nA speculative decoder uses a cheap model to propose future tokens and a stronger model to verify them. Speedup depends on acceptance rate, verifier cost, draft cost, batching, memory traffic, and rejected work.\n\nThe researcher wrote the prediction before starting the run. If measurement contradicted it, the outcome would still remove one explanation.'''
def load(mid): return AutoModelForCausalLM.from_pretrained(mid,torch_dtype=torch.float32,low_cpu_mem_usage=False).eval()
def qgroup(w):
    if w.ndim!=2:return w
    qmax=127;r,c=w.shape;pad=(-c)%GROUP;z=F.pad(w,(0,pad)) if pad else w;z=z.reshape(r,-1,GROUP);s=z.abs().amax(-1,keepdim=True).clamp_min(1e-12)/qmax
    return ((z/s).round().clamp(-qmax,qmax)*s).reshape(r,-1)[:,:c]
def quantize8(m):
    seen=set()
    with torch.no_grad():
        for p in m.parameters():
            ptr=p.untyped_storage().data_ptr()
            if ptr in seen:continue
            seen.add(ptr)
            if p.ndim==2 and p.is_floating_point():p.copy_(qgroup(p))
    return m
def contexts(tok):
    ids=tok(CORPUS,add_special_tokens=False,return_tensors='pt').input_ids[0];g=torch.Generator().manual_seed(SEED+11);starts=torch.randint(0,ids.numel()-CTX-1,(NB,),generator=g)
    return torch.stack([ids[s:s+CTX] for s in starts.tolist()])
def draft_greedy(m,ctx):
    out=[]
    with torch.inference_mode():
        for i in range(0,NB,BS):
            cur=ctx[i:i+BS].clone();ts=[]
            for _ in range(K):
                n=m(cur).logits[:,-1,:].argmax(-1);ts.append(n.cpu());cur=torch.cat([cur,n[:,None]],1)
            out.append(torch.stack(ts,1))
    return torch.cat(out)
def target_logits(m,c,d):
    return m(torch.cat([c,d],1)).logits[:,CTX-1:CTX+K,:].float()
def cert_signed(z,lo,hi):
    pred=z.argmax(-1);lower=z.gather(-1,pred[...,None]).squeeze(-1)-hi[pred];comp=z-lo.view(1,1,-1);comp=comp.clone();comp.scatter_(-1,pred[...,None],float('-inf'));return pred,lower>comp.amax(-1)
def cert_sym(z,delta):
    pred=z.argmax(-1);lower=z.gather(-1,pred[...,None]).squeeze(-1)-delta[pred];comp=z+delta.view(1,1,-1);comp=comp.clone();comp.scatter_(-1,pred[...,None],float('-inf'));return pred,lower>comp.amax(-1)
def complete(d,p,c,f,bonus=False):
    for j in range(K):
        if not bool(c[j]):return False,False
        if int(p[j])!=int(d[j]):return True,int(p[j])==int(f[j])
        if int(p[j])!=int(f[j]):return True,False
    if bonus:
        if not bool(c[K]):return False,False
        return True,int(p[K])==int(f[K])
    return True,all(int(p[j])==int(f[j]) for j in range(K))
def main():
    t0=time.time();half=NB//2;tok=AutoTokenizer.from_pretrained(TARGET_ID);dt=AutoTokenizer.from_pretrained(DRAFT_ID)
    if tok.get_vocab()!=dt.get_vocab():raise RuntimeError('vocab mismatch')
    ctx=contexts(tok);dm=load(DRAFT_ID);draft=draft_greedy(dm,ctx);del dm;gc.collect()
    tm=load(TARGET_ID);V=tm.config.vocab_size;path=OUT/'fp.dat';mm=np.memmap(path,dtype='float32',mode='w+',shape=(NB,K+1,V))
    with torch.inference_mode():
        for i in range(0,NB,BS):
            c=ctx[i:i+BS];d=draft[i:i+len(c)];mm[i:i+len(c)]=target_logits(tm,c,d).cpu().numpy()
    mm.flush();del tm;gc.collect();qm=quantize8(load(TARGET_ID))
    lo=torch.full((V,),float('inf'));hi=torch.full((V,),float('-inf'));delta=torch.zeros(V)
    with torch.inference_mode():
        for i in range(0,half,BS):
            c=ctx[i:i+BS];d=draft[i:i+len(c)];z=target_logits(qm,c,d).cpu();r=torch.from_numpy(np.array(mm[i:i+len(c)],copy=True));e=z-r;lo=torch.minimum(lo,e.amin((0,1)));hi=torch.maximum(hi,e.amax((0,1)));delta=torch.maximum(delta,e.abs().amax((0,1)))
    pos=raw=signed_cert=signed_wrong=sym_cert=sym_wrong=viol=posviol=0;skip=good=bonus=bonusgood=symskip=symgood=0;rows=[]
    with torch.inference_mode():
        for i in range(half,NB,BS):
            c=ctx[i:i+BS];d=draft[i:i+len(c)];z=target_logits(qm,c,d).cpu();r=torch.from_numpy(np.array(mm[i:i+len(c)],copy=True));f=r.argmax(-1);p,cs=cert_signed(z,lo,hi);ps,cy=cert_sym(z,delta);e=z-r;v=(e<lo.view(1,1,-1))|(e>hi.view(1,1,-1));viol+=int(v.sum());posviol+=int(v.any(-1).sum());pos+=z.shape[0]*(K+1);raw+=int((p==f).sum());signed_cert+=int(cs.sum());signed_wrong+=int((cs&(p!=f)).sum());sym_cert+=int(cy.sum());sym_wrong+=int((cy&(ps!=f)).sum())
            for b in range(len(c)):
                ok,co=complete(d[b],p[b],cs[b],f[b],False);okb,cob=complete(d[b],p[b],cs[b],f[b],True);oky,coy=complete(d[b],ps[b],cy[b],f[b],False)
                skip+=ok;good+=ok and co;bonus+=okb;bonusgood+=okb and cob;symskip+=oky;symgood+=oky and coy;rows.append({'block':i+b,'signed_skip':bool(ok),'signed_correct':bool(co) if ok else None,'signed_bonus_skip':bool(okb),'symmetric_skip':bool(oky)})
    del qm,mm;gc.collect();path.unlink(missing_ok=True);n=NB-half;sr=skip/n;br=bonus/n;syr=symskip/n
    R={'status':'COMPLETE','seed':SEED,'blocks':NB,'calibration_blocks':half,'test_blocks':n,'K':K,'draft_model':DRAFT_ID,'target_model':TARGET_ID,'raw_argmax_agreement':raw/pos,'signed_position_cert_rate':signed_cert/pos,'signed_cert_wrong':signed_wrong,'symmetric_position_cert_rate':sym_cert/pos,'symmetric_cert_wrong':sym_wrong,'signed_skip_full_rate':sr,'signed_skip_full_output_correct_rate':good/skip if skip else 1.0,'signed_ideal_bit_cost':8+16*(1-sr),'signed_bonus_skip_full_rate':br,'signed_bonus_correct_rate':bonusgood/bonus if bonus else 1.0,'signed_bonus_ideal_bit_cost':8+16*(1-br),'symmetric_skip_full_rate':syr,'symmetric_skip_full_output_correct_rate':symgood/symskip if symskip else 1.0,'symmetric_ideal_bit_cost':8+16*(1-syr),'signed_interval_width_median':float((hi-lo).median()),'signed_interval_width_p99':float(torch.quantile(hi-lo,.99)),'signed_interval_width_max':float((hi-lo).max()),'test_signed_bound_violation_fraction_logits':viol/(pos*V),'test_positions_any_signed_bound_violation_rate':posviol/pos,'bound_status':'EMPIRICAL_CALIBRATION_ONLY_NOT_FORMAL_CERTIFICATE'}
    zero=(signed_wrong==0 and R['signed_skip_full_output_correct_rate']==1.0)
    R['preregistered_decision']='STRONG_GO_SIGNED' if sr>=.70 and zero else ('GO_SIGNED' if sr>.50 and zero else ('STOP_SIGNED' if sr<=.40 else 'INCONCLUSIVE'))
    R['elapsed_seconds']=time.time()-t0;R['environment']={'python':sys.version,'torch':torch.__version__,'transformers':transformers_version,'platform':platform.platform(),'cpu_count':os.cpu_count()}
    (OUT/'summary.json').write_text(json.dumps(R,indent=2,sort_keys=True)+'\n');(OUT/'blocks.json').write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps(R,indent=2,sort_keys=True))
if __name__=='__main__':main()
