# ThresholdSpec EXP-TS-001 — Result

Status: `COMPLETE`

Pre-registered decision: **`STRONG_GO`**.

This result supports continued investigation of the ThresholdSpec margin-headroom mechanism. It does **not** establish a lossless algorithm or a hardware speedup.

## Frozen-run result

Run: GitHub Actions `32019562064`, seed `20260817`.

Models:
- drafter: `HuggingFaceTB/SmolLM2-135M`
- target: `HuggingFaceTB/SmolLM2-360M`

Events: 1,024 total, first 512 calibration and last 512 held-out test.

Observed:
- speculative acceptance rate: **77.15%**
- median absolute full-precision acceptance margin: **0.871**
- INT4 held-out empirical-resolution rate: **1.56%**
- INT6: **46.48%**
- INT8: **82.23%**
- observed wrong accept/reject decisions among INT8 events called resolved by the frozen rule: **0 / 421**
- progressive 4→6→8→FP fallback: **17.77%**
- observed final progressive accept/reject agreement: **100% on the 512 held-out events**

The frozen `STRONG_GO` rule required INT8 resolution >=80%, zero observed resolved-decision errors, and FP fallback <=20%; all three conditions passed.

## Replication relative to the toy experiment

The earlier toy Transformer experiment found INT8 resolution 88.38% and FP fallback 11.62%. The pretrained pair reproduces the central signal but at a weaker magnitude: 82.23% and 17.77%, respectively. INT4 becomes nearly useless (1.56%), suggesting that an eventual runtime should probably not pay a standalone 4-bit stage unless that work is almost perfectly reusable by later precision stages.

## Post-result red-team: empirical bound failure

The frozen experiment used the maximum calibration absolute error in `log p(x)` as an empirical decision bound. This was never claimed to be a formal certificate.

Held-out inspection shows why that distinction matters:
- INT4: 1 / 512 held-out errors exceeded the calibration maximum.
- INT6: 0 / 512 exceeded it.
- INT8: 2 / 512 exceeded it.

Both INT8 exceedances still produced the same accept/reject sign as full precision, so the frozen result remains `STRONG_GO` under its pre-registered rule. However, the calibration maximum is demonstrably **not a valid worst-case bound** and must not be described as lossless certification.

## Post-hoc Monte Carlo stress test

Using the same 1,024 measured `(log q, log p, low-bit log p)` tuples, 10,000 new random 50/50 calibration/test splits and new `u ~ Uniform(0,1)` acceptance thresholds were sampled. This is a stress test, not an independent model replication.

Results:
- mean INT8 resolution rate: **76.11%**
- median INT8 resolution rate: **75.98%**
- 5th–95th percentile: **68.95%–84.38%**
- trials satisfying frozen `STRONG_GO`: **27.76%**
- trials satisfying `GO` or `STRONG_GO`: **88.96%**
- INT8 trials with at least one empirically “resolved” wrong sign: **45 / 10,000**
- total such INT8 wrong events: **45 across 5.12 million held-out event evaluations**
- progressive 4→6→8→FP trials with at least one wrong sign: **1,502 / 10,000**

This confirms strong statistical margin headroom while falsifying the idea that a split-calibrated maximum can provide exactness.

## Exploratory safety multiplier

A separate post-hoc 5,000-trial stress test multiplied each calibration maximum by a safety factor. At `1.5×`, no wrong INT8-resolved or progressive decisions were observed in that simulation, but mean INT8 resolution fell to about **65.5%** and mean FP fallback rose to about **34.5%**. This remains empirical, not formal.

## Systems red-team

The observed precision fractions only imply a speed opportunity if later precision **reuses earlier work**.

Using the frozen held-out fractions and an idealized bit-plane cost model:
- incremental 4→6→8→16 reveal cost: about **8.46 bit-equivalents** per verification event;
- incremental 6→8→16: about **8.49**;
- incremental 8→16: about **9.42**;
- naively recomputing complete 4-, 6-, 8-, and 16-bit passes when escalation occurs: about **17.03 bit-equivalents**.

Therefore a naive multi-forward implementation can be worse than a single 16-bit verifier. The practical mechanism requires bit-plane/residual reuse or another genuinely incremental computation scheme. The 4-bit stage saves only ~0.03 ideal bit-equivalents versus starting at 6 bits and is unlikely to justify a separate kernel launch.

## Prior-art boundary after the run

Closest known directions include fixed low-bit speculative verification (Quasar), multi-precision/bit-plane LLM execution (Any-Precision LLM / AnyBCQ), progressive precision transfer/verification for KV systems (Lynx), and runtime-bounded quantized attention. The currently differentiated hypothesis is narrowly:

> use the stochastic speculative-sampling acceptance margin itself to determine how much target numerical precision must be revealed before an accept/reject decision is resolved, with exact fallback for unresolved cases.

Novelty is still **potential**, not proven.

## Decision

**Continue, but change the next uncertainty.** Margin headroom is no longer the primary uncertainty. The two dominant unresolved questions are now:

1. Can a useful end-to-end correctness bound be made tight enough to replace the failed empirical bound?
2. Can the target computation be refined incrementally enough that 6→8→full precision saves real memory traffic/latency rather than replaying the model?

No production claim and no merge to `main` are authorized by EXP-TS-001 alone.
