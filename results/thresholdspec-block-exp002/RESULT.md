# ThresholdSpec EXP-TS-002 — Result

Status: `COMPLETE`

Pre-registered decision: **`STOP_STOCHASTIC`**.

## What was tested

EXP-TS-001 established isolated-event margin headroom. EXP-TS-002 tested the structural economics of exact stochastic speculative decoding in real draft blocks, where the first rejected draft normally requires the exact residual correction distribution `norm(max(0, p-q))`.

Models: SmolLM2-135M drafter → SmolLM2-360M target. 256 real sampled draft blocks, Kmax=8; first 128 calibration, last 128 held-out.

## Primary K=4 result

Frozen primary gate: stop if the *oracle* full-target fallback rate is at least 50%. The oracle assumes perfect low-bit accept/reject certification and therefore favors ThresholdSpec as strongly as possible; full precision is charged only when the reference stochastic block contains a rejection.

Held-out K=4:
- all four draft tokens accepted: **20.31%**
- oracle full-target fallback: **79.69%**
- idealized 8-bit-first + 16-bit-fallback weight cost: **20.75 bit-equivalents**
- single 16-bit target baseline: **16 bit-equivalents**

Therefore the current exact stochastic two-pass design loses even under its optimistic oracle lower bound, before kernel-launch, activation, recomputation, draft, or bookkeeping overhead.

## Diagnostics

- K=1: oracle fallback 26.56%, ideal cost 12.25 — potentially favorable.
- K=2: oracle fallback 57.03%, ideal cost 17.125 — already beyond break-even.
- K=4: 79.69%, cost 20.75.
- K=6: 87.50%, cost 22.0.
- K=8: 91.41%, cost 22.625.

The empirical INT8 margin rule is worse: at K=4 only 10.94% of blocks could skip the full target, implying 89.06% fallback and 22.25 ideal bit-equivalents.

The calibration maximum was again not a valid worst-case bound: calibration max INT8 chosen-token log-probability error was 0.2231 while held-out max reached 0.3152.

## Scientific conclusion

**Kill the original stochastic ThresholdSpec v1 path for multi-token blocks.** The isolated-event signal from EXP-TS-001 is real but insufficient. Standard stochastic rejection correction creates a structural full-target fallback bottleneck that dominates for K>=2 on this model pair.

This negative finding does not kill the broader principle of precision-adaptive verification. It specifically redirects the research toward mechanisms that do not require a full target distribution after a rejected proposal, including:

1. exact greedy/argmax verification, where a certified target argmax directly supplies the correction token; and
2. an exploratory interval-certified Gumbel residual sampler, which would attempt to certify the exact stochastic correction token without full precision.

The next experiment should target greedy argmax first because it removes the residual-correction bottleneck cleanly and is directly relevant to temperature-zero local coding/reasoning workloads.
