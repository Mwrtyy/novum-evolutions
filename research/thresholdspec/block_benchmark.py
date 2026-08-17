import gc, json, os, platform, random, sys, time
from pathlib import Path
import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer, __version__ as transformers_version

SEED=int(os.getenv('TS2_SEED','20260817'))
NB=int(os.getenv('TS2_BLOCKS','256'))
CTX=int(os.getenv('TS2_CTX','32'))
KMAX=int(os.getenv('TS2_KMAX','8'))
BS=int(os.getenv('TS2_BS','8'))
GROUP=int(os.getenv('TS2_GROUP','64'))
DRAFT_ID=os.getenv('TS2_DRAFT','HuggingFaceTB/SmolLM2-135M')
TARGET_ID=os.getenv('TS2_TARGET','HuggingFaceTB/SmolLM2-360M')
OUT=Path(os.getenv('TS2_OUT','results/thresholdspec-block-exp002'))
OUT.mkdir(parents=True,exist_ok=True)
random.seed(SEED); torch.manual_seed(SEED); torch.set_num_threads(min(4,os.cpu_count() or 4))

CORPUS='''Scientific progress is fastest when a hypothesis is precise enough to fail. A useful experiment separates observation from interpretation, preserves a baseline, and records negative results.\n\nA local language model runs under strict resource constraints. Memory capacity determines whether weights fit, while memory bandwidth can dominate autoregressive decoding.\n\nIn software engineering, a small reproducible test is more valuable than a large demonstration that cannot isolate cause. Freeze the input, seed randomness, collect raw measurements, and compare the smallest intervention against a strong baseline.\n\nOnce upon a time, a curious child found a brass key beneath an old tree. The key did not open the garden gate, the attic trunk, or the wooden cabinet. At sunset the child noticed a tiny door hidden behind ivy.\n\nThe train reached the coastal station before dawn. Rain tapped against the windows while passengers gathered their bags. A mechanic checked the brakes and waved when inspection was complete.\n\nWhen a program processes untrusted input, it should validate lengths before allocation, reject malformed encodings, and keep parsing separate from execution.\n\nA theorem is not established because many examples satisfy it. Examples can reveal structure and kill bad conjectures, but the final argument must cover every allowed case.\n\nThe city library had been renovated without losing its quiet character. Sunlight crossed the reading room while students worked beneath tall shelves.\n\nTo compare two algorithms fairly, hold the workload constant, measure warm and cold behavior separately, report variance, and include optimization overhead.\n\nA robot crossing a warehouse must plan around moving workers, temporary obstacles, battery constraints, and delayed sensor observations.\n\nThe chef tasted the sauce, lowered the heat, and added a small amount of water. The texture improved because the adjustment addressed the actual imbalance.\n\nMachine learning systems can appear confident when evidence is weak. Calibrated uncertainty distinguishes knowing from fluent guessing.\n\nIn a distributed service, retries can improve reliability or create an overload spiral. Backoff, idempotency, bounded queues, and deadlines keep failures controlled.\n\nA telescope does not make a discovery by magnifying every part of the sky equally. Observation time is limited, so astronomers allocate it toward discriminating measurements.\n\nThe old bridge was closed after sensors detected unusual vibration. Engineers compared wind, traffic, temperature, and historical measurements before examining components.\n\nA speculative decoder uses a cheap model to propose future tokens and a stronger model to verify them. Speedup depends on acceptance rate, verifier cost, draft cost, batching, memory traffic, and rejected work.\n\nThe researcher wrote the prediction before starting the run. If measurement contradicted it, the outcome would still remove one explanation.'''

def load(mid):
    return AutoModelForCausalLM.from_pretrained(mid,torch_dtype=torch.float32,low_cpu_mem_usage=False).eval()

def qgroup(w,bits=8):
    if w.ndim!=2:return w
    qmax=2**(bits-1)-1; r,c=w.shape; pad=(-c)%GROUP
    z=F.pad(w,(0,pad)) if pad else w; z=z.reshape(r,-1,GROUP)
    s=z.abs().amax(-1,keepdim=True).clamp_min(1e-12)/qmax
    return ((z/s).round().clamp(-qmax,qmax)*s).reshape(r,-1)[:,:c]

def quantize8(model):
    seen=set()
    with torch.no_grad():
        for p in model.parameters():
            ptr=p.untyped_storage().data_ptr()
            if ptr in seen:continue
            seen.add(ptr)
            if p.ndim==2 and p.is_floating_point():p.copy_(qgroup(p,8))
    return model

def make_contexts(tok):
    ids=tok(CORPUS,add_special_tokens=False,return_tensors='pt').input_ids[0]
    g=torch.Generator().manual_seed(SEED+11)
    starts=torch.randint(0,ids.numel()-CTX-1,(NB,),generator=g)
    return torch.stack([ids[s:s+CTX] for s in starts.tolist()])

def generate_blocks(model,ctx,tok):
    chunks=[]
    torch.manual_seed(SEED+23)
    with torch.inference_mode():
        for i in range(0,len(ctx),BS):
            c=ctx[i:i+BS]
            y=model.generate(c,max_new_tokens=KMAX,do_sample=True,temperature=1.0,top_p=1.0,top_k=0,pad_token_id=tok.eos_token_id,use_cache=True)
            chunks.append(y[:,CTX:CTX+KMAX].cpu())
    return torch.cat(chunks)

def chosen_logps(model,ctx,draft):
    vals=[]
    with torch.inference_mode():
        for i in range(0,len(ctx),BS):
            c=ctx[i:i+BS]; d=draft[i:i+len(c)]; seq=torch.cat([c,d],dim=1)
            logits=model(seq[:,:-1]).logits[:,CTX-1:CTX+KMAX-1,:].float()
            lp=F.log_softmax(logits,-1).gather(2,d[:,:,None]).squeeze(2)
            vals.append(lp.cpu())
    return torch.cat(vals)

def main():
    t0=time.time(); tok=AutoTokenizer.from_pretrained(TARGET_ID); dtok=AutoTokenizer.from_pretrained(DRAFT_ID)
    if tok.get_vocab()!=dtok.get_vocab():raise RuntimeError('draft/target vocabularies differ')
    ctx=make_contexts(tok)
    draft_model=load(DRAFT_ID); draft=generate_blocks(draft_model,ctx,tok); logq=chosen_logps(draft_model,ctx,draft)
    del draft_model; gc.collect()
    target=load(TARGET_ID); logp=chosen_logps(target,ctx,draft); del target; gc.collect()
    target8=quantize8(load(TARGET_ID)); logp8=chosen_logps(target8,ctx,draft); del target8; gc.collect()
    g=torch.Generator().manual_seed(SEED+37); u=torch.rand((NB,KMAX),generator=g).clamp_min(1e-12)
    base=logq+u.log(); m=logp-base; m8=logp8-base; err=(logp8-logp).abs()
    half=NB//2; bound=float(err[:half].max()); test=slice(half,None)
    R={'status':'COMPLETE','seed':SEED,'blocks':NB,'calibration_blocks':half,'test_blocks':NB-half,'context_tokens':CTX,'kmax':KMAX,'batch_size':BS,'group_size':GROUP,'draft_model':DRAFT_ID,'target_model':TARGET_ID,'int8_cal_max_logp_error':bound,'int8_test_max_logp_error':float(err[test].max()),'bound_status':'EMPIRICAL_ONLY_NOT_FORMAL_CERTIFICATE','per_k':{}}
    test_m=m[test]; test_m8=m8[test]
    for K in (1,2,4,6,8):
        fp_accept=test_m[:,:K]>=0
        cert=test_m8[:,:K].abs()>bound
        all_accept=fp_accept.all(dim=1)
        all_cert=cert.all(dim=1)
        oracle_fallback=~all_accept
        empirical_can_skip=all_accept & all_cert
        empirical_fallback=~empirical_can_skip
        oracle_rate=float(oracle_fallback.float().mean()); empirical_rate=float(empirical_fallback.float().mean())
        first_rej=[]
        for row in fp_accept:
            bad=(~row).nonzero()
            first_rej.append(int(bad[0])+1 if len(bad) else K+1)
        R['per_k'][str(K)]={'all_accept_rate':float(all_accept.float().mean()),'oracle_full_fallback_rate':oracle_rate,'oracle_ideal_bit_cost':8+16*oracle_rate,'empirical_all_positions_cert_rate':float(all_cert.float().mean()),'empirical_can_skip_full_rate':float(empirical_can_skip.float().mean()),'empirical_full_fallback_rate':empirical_rate,'empirical_ideal_bit_cost':8+16*empirical_rate,'mean_first_rejection_position_or_Kplus1':sum(first_rej)/len(first_rej)}
    k4=R['per_k']['4']['oracle_full_fallback_rate']
    R['preregistered_decision']='CONTINUE_STOCHASTIC' if k4<.40 else ('BORDERLINE' if k4<.50 else 'STOP_STOCHASTIC')
    R['elapsed_seconds']=time.time()-t0; R['environment']={'python':sys.version,'torch':torch.__version__,'transformers':transformers_version,'platform':platform.platform(),'cpu_count':os.cpu_count()}
    (OUT/'summary.json').write_text(json.dumps(R,indent=2,sort_keys=True)+'\n')
    raw={'draft_token_ids':draft.tolist(),'u':u.tolist(),'log_q':logq.tolist(),'log_p':logp.tolist(),'log_p_int8':logp8.tolist(),'full_margin':m.tolist(),'int8_margin':m8.tolist()}
    (OUT/'blocks.json').write_text(json.dumps(raw,separators=(',',':')))
    print(json.dumps(R,indent=2,sort_keys=True))
if __name__=='__main__':main()
