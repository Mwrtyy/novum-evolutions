import gc, json, os, platform, random, sys, time
from pathlib import Path
import numpy as np
import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer, __version__ as transformers_version

SEED=int(os.getenv('TS3_SEED','20260817'))
NB=int(os.getenv('TS3_BLOCKS','256'))
CTX=int(os.getenv('TS3_CTX','32'))
K=int(os.getenv('TS3_K','4'))
BS=int(os.getenv('TS3_BS','8'))
GROUP=int(os.getenv('TS3_GROUP','64'))
DRAFT_ID=os.getenv('TS3_DRAFT','HuggingFaceTB/SmolLM2-135M')
TARGET_ID=os.getenv('TS3_TARGET','HuggingFaceTB/SmolLM2-360M')
OUT=Path(os.getenv('TS3_OUT','results/thresholdspec-greedy-exp003'))
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

def greedy_draft(model,ctx):
    out=[]
    with torch.inference_mode():
        for i in range(0,len(ctx),BS):
            cur=ctx[i:i+BS].clone(); toks=[]
            for _ in range(K):
                nxt=model(cur).logits[:,-1,:].argmax(-1)
                toks.append(nxt.cpu()); cur=torch.cat([cur,nxt[:,None]],1)
            out.append(torch.stack(toks,1))
    return torch.cat(out)

def target_slice(model,ctx,draft):
    seq=torch.cat([ctx,draft],1)
    return model(seq).logits[:,CTX-1:CTX+K,:].float()

def certify(logits8, delta):
    pred=logits8.argmax(-1)
    dp=delta[pred]
    lower=logits8.gather(-1,pred[...,None]).squeeze(-1)-dp
    upper=logits8+delta.view(1,1,-1)
    upper.scatter_(-1,pred[...,None],float('-inf'))
    cert=lower>upper.amax(-1)
    return pred,cert

def certify_global(logits8, eps):
    top=torch.topk(logits8,2,dim=-1)
    return top.indices[...,0], (top.values[...,0]-top.values[...,1])>2*eps

def block_complete(draft, pred, cert, fp_pred, need_bonus=False):
    Kloc=draft.numel(); relevant_errors=0
    for i in range(Kloc):
        if not bool(cert[i]):return False,False,relevant_errors,i+1
        if int(pred[i])!=int(fp_pred[i]):relevant_errors+=1
        if int(pred[i])!=int(draft[i]):
            good=int(pred[i])==int(fp_pred[i])
            return True,good,relevant_errors,i+1
    if need_bonus:
        if not bool(cert[Kloc]):return False,False,relevant_errors,Kloc+1
        if int(pred[Kloc])!=int(fp_pred[Kloc]):relevant_errors+=1
        good=int(pred[Kloc])==int(fp_pred[Kloc])
        return True,good,relevant_errors,Kloc+1
    good=all(int(pred[i])==int(fp_pred[i]) for i in range(Kloc))
    return True,good,relevant_errors,Kloc+1

def main():
    t0=time.time(); half=NB//2
    tok=AutoTokenizer.from_pretrained(TARGET_ID); dtok=AutoTokenizer.from_pretrained(DRAFT_ID)
    if tok.get_vocab()!=dtok.get_vocab():raise RuntimeError('draft/target vocabularies differ')
    ctx=make_contexts(tok)
    drafter=load(DRAFT_ID); draft=greedy_draft(drafter,ctx); del drafter; gc.collect()

    target=load(TARGET_ID); V=target.config.vocab_size
    fp_path=OUT/'fp_logits.dat'; fp=np.memmap(fp_path,dtype='float32',mode='w+',shape=(NB,K+1,V))
    with torch.inference_mode():
        for i in range(0,NB,BS):
            c=ctx[i:i+BS]; d=draft[i:i+len(c)]; fp[i:i+len(c)]=target_slice(target,c,d).cpu().numpy()
    fp.flush(); del target; gc.collect()

    target8=quantize8(load(TARGET_ID))
    per_delta=torch.zeros(V); global_delta=0.0
    with torch.inference_mode():
        for i in range(0,half,BS):
            c=ctx[i:i+BS]; d=draft[i:i+len(c)]; z8=target_slice(target8,c,d).cpu()
            zfp=torch.from_numpy(np.array(fp[i:i+len(c)],copy=True)); e=(z8-zfp).abs()
            per_delta=torch.maximum(per_delta,e.amax(dim=(0,1))); global_delta=max(global_delta,float(e.max()))

    totals={'positions':0,'raw_agree':0,'per_cert':0,'per_cert_wrong':0,'global_cert':0,'global_cert_wrong':0,'bound_violations':0,'positions_any_bound_violation':0}
    block_rows=[]; skip=skip_correct=skip_bonus=skip_bonus_correct=0; skip_g=skip_g_correct=0
    all_match=0; first_mismatch=[]
    with torch.inference_mode():
        for i in range(half,NB,BS):
            c=ctx[i:i+BS]; d=draft[i:i+len(c)]; z8=target_slice(target8,c,d).cpu()
            zfp=torch.from_numpy(np.array(fp[i:i+len(c)],copy=True)); fp_pred=zfp.argmax(-1)
            pred,cert=certify(z8,per_delta); predg,certg=certify_global(z8,global_delta)
            err=(z8-zfp).abs(); violations=err>per_delta.view(1,1,-1)
            totals['bound_violations']+=int(violations.sum()); totals['positions_any_bound_violation']+=int(violations.any(-1).sum())
            totals['positions']+=z8.shape[0]*(K+1); totals['raw_agree']+=int((pred==fp_pred).sum()); totals['per_cert']+=int(cert.sum()); totals['per_cert_wrong']+=int((cert&(pred!=fp_pred)).sum()); totals['global_cert']+=int(certg.sum()); totals['global_cert_wrong']+=int((certg&(predg!=fp_pred)).sum())
            for b in range(len(c)):
                db=d[b]; f=fp_pred[b]; p=pred[b]; ce=cert[b]; pg=predg[b]; cg=certg[b]
                mm=K+1
                for j in range(K):
                    if int(f[j])!=int(db[j]):mm=j+1; break
                first_mismatch.append(mm); all_match+=int(mm==K+1)
                ok,corr,relerr,stop=block_complete(db,p,ce,f,False); okb,corrb,relerrb,stopb=block_complete(db,p,ce,f,True); okg,corrg,_,_=block_complete(db,pg,cg,f,False)
                skip+=int(ok); skip_correct+=int(ok and corr); skip_bonus+=int(okb); skip_bonus_correct+=int(okb and corrb); skip_g+=int(okg); skip_g_correct+=int(okg and corrg)
                block_rows.append({'block':i+b,'first_fp_mismatch':mm,'per_token_skip_full':bool(ok),'per_token_output_correct':bool(corr) if ok else None,'per_token_bonus_skip_full':bool(okb),'global_skip_full':bool(okg),'relevant_cert_errors':relerr})
    del target8; gc.collect(); del fp
    try:fp_path.unlink()
    except FileNotFoundError:pass

    test_blocks=NB-half; skip_rate=skip/test_blocks; bonus_rate=skip_bonus/test_blocks; global_skip=skip_g/test_blocks
    R={'status':'COMPLETE','seed':SEED,'blocks':NB,'calibration_blocks':half,'test_blocks':test_blocks,'context_tokens':CTX,'K':K,'batch_size':BS,'group_size':GROUP,'draft_model':DRAFT_ID,'target_model':TARGET_ID,'global_cal_max_logit_error':global_delta,'per_token_delta_median':float(per_delta.median()),'per_token_delta_p99':float(torch.quantile(per_delta,.99)),'per_token_delta_max':float(per_delta.max()),'test_raw_argmax_agreement':totals['raw_agree']/totals['positions'],'test_per_token_empirical_cert_rate':totals['per_cert']/totals['positions'],'test_per_token_cert_wrong':totals['per_cert_wrong'],'test_global_empirical_cert_rate':totals['global_cert']/totals['positions'],'test_global_cert_wrong':totals['global_cert_wrong'],'test_bound_violation_fraction_logits':totals['bound_violations']/(totals['positions']*V),'test_positions_any_bound_violation_rate':totals['positions_any_bound_violation']/totals['positions'],'fp_all_K_drafts_match_rate':all_match/test_blocks,'mean_first_fp_mismatch_or_Kplus1':sum(first_mismatch)/len(first_mismatch),'per_token_skip_full_rate':skip_rate,'per_token_skip_full_output_correct_rate':skip_correct/skip if skip else 1.0,'per_token_ideal_bit_cost':8+16*(1-skip_rate),'per_token_bonus_skip_full_rate':bonus_rate,'per_token_bonus_skip_full_output_correct_rate':skip_bonus_correct/skip_bonus if skip_bonus else 1.0,'per_token_bonus_ideal_bit_cost':8+16*(1-bonus_rate),'global_skip_full_rate':global_skip,'global_skip_full_output_correct_rate':skip_g_correct/skip_g if skip_g else 1.0,'global_ideal_bit_cost':8+16*(1-global_skip),'bound_status':'EMPIRICAL_CALIBRATION_ONLY_NOT_FORMAL_CERTIFICATE'}
    zero_errors=(R['test_per_token_cert_wrong']==0 and R['per_token_skip_full_output_correct_rate']==1.0)
    if skip_rate>=.70 and zero_errors:R['preregistered_decision']='STRONG_GO_GREEDY'
    elif skip_rate>.50 and zero_errors:R['preregistered_decision']='GO_GREEDY'
    elif skip_rate<=.40:R['preregistered_decision']='STOP_GREEDY'
    else:R['preregistered_decision']='INCONCLUSIVE'
    R['elapsed_seconds']=time.time()-t0; R['environment']={'python':sys.version,'torch':torch.__version__,'transformers':transformers_version,'platform':platform.platform(),'cpu_count':os.cpu_count()}
    (OUT/'summary.json').write_text(json.dumps(R,indent=2,sort_keys=True)+'\n'); (OUT/'blocks.json').write_text(json.dumps(block_rows,indent=2)+'\n')
    print(json.dumps(R,indent=2,sort_keys=True))
if __name__=='__main__':main()
