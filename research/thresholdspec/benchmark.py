import csv, gc, json, os, platform, random, sys, time
from pathlib import Path
import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer, __version__ as transformers_version

SEED=int(os.getenv('THRESHOLDSPEC_SEED','20260817'))
N=int(os.getenv('THRESHOLDSPEC_N','1024'))
CTX=int(os.getenv('THRESHOLDSPEC_CTX','32'))
BS=int(os.getenv('THRESHOLDSPEC_BS','8'))
GROUP=int(os.getenv('THRESHOLDSPEC_GROUP','64'))
DRAFT_ID=os.getenv('THRESHOLDSPEC_DRAFT','HuggingFaceTB/SmolLM2-135M')
TARGET_ID=os.getenv('THRESHOLDSPEC_TARGET','HuggingFaceTB/SmolLM2-360M')
OUT=Path(os.getenv('THRESHOLDSPEC_OUT','results/thresholdspec-pretrained'))
OUT.mkdir(parents=True,exist_ok=True)
random.seed(SEED); torch.manual_seed(SEED); torch.set_num_threads(min(4,os.cpu_count() or 4))

CORPUS='''Scientific progress is fastest when a hypothesis is precise enough to fail. A useful experiment separates observation from interpretation, preserves a baseline, and records negative results.\n\nA local language model runs under strict resource constraints. Memory capacity determines whether weights fit, while memory bandwidth can dominate autoregressive decoding.\n\nIn software engineering, a small reproducible test is more valuable than a large demonstration that cannot isolate cause. Freeze the input, seed randomness, collect raw measurements, and compare the smallest intervention against a strong baseline.\n\nOnce upon a time, a curious child found a brass key beneath an old tree. The key did not open the garden gate, the attic trunk, or the wooden cabinet. At sunset the child noticed a tiny door hidden behind ivy.\n\nThe train reached the coastal station before dawn. Rain tapped against the windows while passengers gathered their bags. A mechanic checked the brakes and waved when inspection was complete.\n\nWhen a program processes untrusted input, it should validate lengths before allocation, reject malformed encodings, and keep parsing separate from execution.\n\nA theorem is not established because many examples satisfy it. Examples can reveal structure and kill bad conjectures, but the final argument must cover every allowed case.\n\nThe city library had been renovated without losing its quiet character. Sunlight crossed the reading room while students worked beneath tall shelves.\n\nTo compare two algorithms fairly, hold the workload constant, measure warm and cold behavior separately, report variance, and include optimization overhead.\n\nA robot crossing a warehouse must plan around moving workers, temporary obstacles, battery constraints, and delayed sensor observations.\n\nThe chef tasted the sauce, lowered the heat, and added a small amount of water. The texture improved because the adjustment addressed the actual imbalance.\n\nMachine learning systems can appear confident when evidence is weak. Calibrated uncertainty distinguishes knowing from fluent guessing.\n\nIn a distributed service, retries can improve reliability or create an overload spiral. Backoff, idempotency, bounded queues, and deadlines keep failures controlled.\n\nA telescope does not make a discovery by magnifying every part of the sky equally. Observation time is limited, so astronomers allocate it toward discriminating measurements.\n\nThe old bridge was closed after sensors detected unusual vibration. Engineers compared wind, traffic, temperature, and historical measurements before examining components.\n\nA speculative decoder uses a cheap model to propose future tokens and a stronger model to verify them. Speedup depends on acceptance rate, verifier cost, draft cost, batching, memory traffic, and rejected work.\n\nThe researcher wrote the prediction before starting the run. If measurement contradicted it, the outcome would still remove one explanation.'''

def load(mid):
    return AutoModelForCausalLM.from_pretrained(mid,torch_dtype=torch.float32,low_cpu_mem_usage=False).eval()

def qgroup(w,bits):
    if w.ndim!=2:return w
    qmax=2**(bits-1)-1; r,c=w.shape; pad=(-c)%GROUP
    z=F.pad(w,(0,pad)) if pad else w; z=z.reshape(r,-1,GROUP)
    s=z.abs().amax(-1,keepdim=True).clamp_min(1e-12)/qmax
    return ((z/s).round().clamp(-qmax,qmax)*s).reshape(r,-1)[:,:c]

def quantize(model,bits):
    seen=set()
    with torch.no_grad():
        for p in model.parameters():
            ptr=p.untyped_storage().data_ptr()
            if ptr in seen:continue
            seen.add(ptr)
            if p.ndim==2 and p.is_floating_point():p.copy_(qgroup(p,bits))
    return model

def contexts(tok):
    ids=tok(CORPUS,add_special_tokens=False,return_tensors='pt').input_ids[0]
    g=torch.Generator().manual_seed(SEED+11)
    starts=torch.randint(0,ids.numel()-CTX-1,(N,),generator=g)
    return torch.stack([ids[s:s+CTX] for s in starts.tolist()])

def lps(model,ctx,chosen=None):
    out=[]
    with torch.inference_mode():
        for i in range(0,len(ctx),BS):
            c=ctx[i:i+BS]; lp=F.log_softmax(model(c).logits[:,-1,:].float(),-1)
            if chosen is None:out.append(lp.cpu())
            else:
                x=chosen[i:i+len(c)]; out.append(lp.gather(1,x[:,None]).squeeze(1).cpu())
    return torch.cat(out)

def main():
    t0=time.time(); tok=AutoTokenizer.from_pretrained(TARGET_ID); dtok=AutoTokenizer.from_pretrained(DRAFT_ID)
    if tok.get_vocab()!=dtok.get_vocab():raise RuntimeError('draft/target vocabularies differ')
    ctx=contexts(tok)
    d=load(DRAFT_ID); dlp=lps(d,ctx); g=torch.Generator().manual_seed(SEED+23)
    x=torch.multinomial(dlp.exp(),1,generator=g).squeeze(1); logq=dlp.gather(1,x[:,None]).squeeze(1)
    del d,dlp; gc.collect()
    t=load(TARGET_ID); logp=lps(t,ctx,x); del t; gc.collect()
    gu=torch.Generator().manual_seed(SEED+37); u=torch.rand(N,generator=gu).clamp_min(1e-12)
    base=logq+u.log(); m=logp-base; qlp={}
    for b in (4,6,8):
        q=quantize(load(TARGET_ID),b); qlp[b]=lps(q,ctx,x); del q; gc.collect()
    half=N//2; cal=slice(0,half); test=slice(half,None)
    R={'status':'COMPLETE','seed':SEED,'N':N,'context_tokens':CTX,'batch_size':BS,'group_size':GROUP,'draft_model':DRAFT_ID,'target_model':TARGET_ID,'acceptance_rate':float((m>=0).float().mean()),'abs_margin_median':float(m.abs().median()),'calibration_N':half,'test_N':N-half}
    margins={}; bounds={}
    for b in (4,6,8):
        mb=qlp[b]-base; e=(qlp[b]-logp).abs(); margins[b]=mb; bounds[b]=float(e[cal].max())
        cert=mb[test].abs()>bounds[b]; bad=((mb[test]>=0)!=(m[test]>=0))
        R[f'int{b}_cal_max_bound']=bounds[b]; R[f'int{b}_raw_agreement_all']=float(((mb>=0)==(m>=0)).float().mean()); R[f'int{b}_test_cert_rate']=float(cert.float().mean()); R[f'int{b}_test_cert_error']=float(bad[cert].float().mean()) if cert.any() else 0.0; R[f'int{b}_error_median']=float(e.median()); R[f'int{b}_error_p99']=float(torch.quantile(e,.99))
    unresolved=torch.ones(N-half,dtype=torch.bool); pred=torch.zeros(N-half,dtype=torch.bool)
    for b in (4,6,8):
        mb=margins[b][test]; cert=unresolved&(mb.abs()>bounds[b]); pred[cert]=mb[cert]>=0; R[f'progressive_{b}_fraction']=float(cert.float().mean()); unresolved&=~cert
    pred[unresolved]=m[test][unresolved]>=0; R['progressive_fp_fraction']=float(unresolved.float().mean()); R['progressive_agreement']=float((pred==(m[test]>=0)).float().mean())
    if R['int8_test_cert_rate']>=.80 and R['int8_test_cert_error']==0 and R['progressive_fp_fraction']<=.20:R['preregistered_decision']='STRONG_GO'
    elif R['int8_test_cert_rate']>=.70 and R['int8_test_cert_error']==0 and R['progressive_fp_fraction']<=.30:R['preregistered_decision']='GO'
    elif R['int8_test_cert_rate']<.40:R['preregistered_decision']='STOP'
    else:R['preregistered_decision']='INCONCLUSIVE'
    R['bound_status']='EMPIRICAL_CALIBRATION_ONLY_NOT_FORMAL_CERTIFICATE'; R['elapsed_seconds']=time.time()-t0; R['environment']={'python':sys.version,'torch':torch.__version__,'transformers':transformers_version,'platform':platform.platform(),'cpu_count':os.cpu_count()}
    (OUT/'summary.json').write_text(json.dumps(R,indent=2,sort_keys=True)+'\n')
    with (OUT/'events.csv').open('w',newline='') as f:
        names=['index','split','token_id','u','log_q','log_p','margin_fp','log_p_q4','log_p_q6','log_p_q8']; w=csv.DictWriter(f,fieldnames=names); w.writeheader()
        for i in range(N):w.writerow({'index':i,'split':'calibration' if i<half else 'test','token_id':int(x[i]),'u':float(u[i]),'log_q':float(logq[i]),'log_p':float(logp[i]),'margin_fp':float(m[i]),'log_p_q4':float(qlp[4][i]),'log_p_q6':float(qlp[6][i]),'log_p_q8':float(qlp[8][i])})
    print(json.dumps(R,indent=2,sort_keys=True))
if __name__=='__main__':main()
