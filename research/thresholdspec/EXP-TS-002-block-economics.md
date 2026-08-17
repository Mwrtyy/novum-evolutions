# ThresholdSpec EXP-TS-002 — stochastic block economics

Status: `FROZEN`

This experiment is invention research using NOVUM discipline. It does not mutate NOVUM 2.0.0.

## Exact uncertainty

EXP-TS-001 showed that isolated speculative accept/reject events often have substantial low-precision margin headroom. Real speculative decoding verifies blocks, however, and stochastic rejection sampling requires an exact target correction distribution after the first rejected draft token. Does block structure erase the theoretical verifier-memory advantage even under optimistic certification?

## Frozen setup

- drafter: `HuggingFaceTB/SmolLM2-135M`
- target: `HuggingFaceTB/SmolLM2-360M`
- contexts: 256
- context length: 32 tokens
- maximum draft length: 8
- evaluated prefix lengths: K = 1, 2, 4, 6, 8
- sampling temperature: 1.0, unrestricted categorical sampling
- seed: `20260817`
- target approximation: group-64 symmetric weight quantize/dequantize at INT8
- reference target: FP32

The drafter generates an 8-token continuation autoregressively. Draft log-probabilities `q(x_i | prefix, x_<i)` are recomputed by teacher forcing over the exact generated draft. FP target and INT8 target score the same block in parallel-style teacher forcing. Independent seeded `u_i ~ Uniform(0,1)` determine stochastic speculative acceptance using `log p_i(x_i) - log q_i(x_i) - log u_i >= 0`.

The first 128 blocks calibrate the empirical maximum INT8 chosen-token log-probability error. The last 128 blocks are held out.

## Two block-level tests

### A. Oracle-certification structural ceiling

Assume, unrealistically favorably, that every accept/reject decision could be resolved perfectly from the low-bit pass. A block can still avoid the full target only when all K draft tokens are accepted, because the first stochastic rejection requires sampling from the exact residual correction distribution `norm(max(0, p-q))`.

Thus:

`oracle_full_fallback = 1 - P(all K accepted)`.

With an 8-bit first pass and a fresh 16-bit full pass on fallback, the idealized weight-traffic cost is:

`C_oracle = 8 + 16 * oracle_full_fallback` bit-equivalents per block.

Ignoring every other overhead, break-even against one 16-bit verifier pass requires `oracle_full_fallback < 0.5`, equivalently `P(all K accepted) > 0.5`.

### B. Empirical-margin fallback

Using the calibration maximum INT8 error as an explicitly non-formal empirical bound, a full pass is required when either:

1. the FP reference block contains a stochastic rejection (exact correction required), or
2. at least one decision in the relevant accepted/rejection prefix is unresolved by the empirical INT8 margin bound.

This produces a more realistic but still optimistic `empirical_full_fallback` and corresponding `C_empirical = 8 + 16*fallback`.

## Pre-registered decision at K=4

K=4 is the primary gate because it is a common useful speculative block scale and is less punitive than K=6/8.

- `CONTINUE_STOCHASTIC`: oracle full fallback < 40% (`C_oracle < 14.4` bit-equivalents), leaving meaningful headroom for overhead.
- `BORDERLINE`: oracle fallback 40% to <50%.
- `STOP_STOCHASTIC`: oracle fallback >=50%; even perfect low-bit decision certification cannot beat a 16-bit verifier in the simple two-pass weight-traffic model.

K=1,2,6,8 are diagnostic and cannot override the K=4 primary gate.

## Interpretation guard

- `STOP_STOCHASTIC` kills only the current exact stochastic two-pass ThresholdSpec path, not greedy decoding or a future method that computes the rejection correction without a full target pass.
- `CONTINUE_STOCHASTIC` does not prove speedup; it only survives an optimistic bandwidth lower bound.
- The empirical calibration maximum is not a certificate and is not used for the primary oracle gate.
- No bonus target token is charged. This deliberately favors ThresholdSpec; standard bonus-token work would make the economics less favorable.
