# EXP-TS-003 — Greedy argmax headroom

Status: `FROZEN`

Working name: **ArgmaxSpec**. This is invention research conducted with NOVUM discipline; it does not mutate NOVUM 2.0.0.

## Why this mutation exists

EXP-TS-002 killed the original exact stochastic ThresholdSpec v1 for multi-token blocks because stochastic rejection normally requires the exact residual correction distribution, forcing a full target pass too often. Greedy decoding has no such residual. At the first mismatch, the exact target argmax is itself the correction token.

ArgmaxSpec asks whether a low-precision target can certify that exact FP target argmax often enough to avoid the full target verifier.

## Frozen setup

- drafter: `HuggingFaceTB/SmolLM2-135M`
- target: `HuggingFaceTB/SmolLM2-360M`
- 256 contexts
- context length: 32
- greedy draft length: K=4
- greedy drafter (`do_sample=false`)
- FP32 target reference
- group-64 symmetric INT8 target weight quantize/dequantize
- seed: `20260817`
- first 128 blocks calibration; last 128 held-out

For each block, the target scores all four draft positions plus the bonus position after the fourth draft token.

## Empirical argmax interval rule

For every vocabulary logit coordinate `v`, calibration measures

`delta_v = max_cal |z8_v - zFP_v|`.

On held-out positions, INT8 predicts argmax `j`. The argmax is called empirically resolved only when

`z8_j - delta_j > max_{v != j}(z8_v + delta_v)`.

If the calibration bounds were sound worst-case intervals, this inequality would certify the FP argmax. In this experiment they are empirical maxima only, so a positive result demonstrates headroom, not formal correctness.

A global-error rule using one maximum `delta` is also reported as a conservative diagnostic.

## Exact greedy block logic

Process draft positions in order:

1. If INT8 argmax at the next relevant position is unresolved, full-target fallback is required.
2. If resolved argmax equals the draft token, accept it and continue.
3. If resolved argmax differs, that resolved target argmax is the exact greedy correction candidate and the block terminates successfully without needing a residual distribution.
4. If all K draft tokens are resolved and match, verification-only succeeds. A separate stricter metric also requires the K+1 bonus target argmax to be resolved.

No target logits after the first FP mismatch are treated as relevant.

## Primary pre-registered gate — K=4 verification-only

Let `skip_full` be the fraction of held-out blocks that can complete the exact greedy verification logic using only empirical INT8 argmax intervals.

Idealized two-pass weight traffic is `8 + 16*(1-skip_full)` bit-equivalents. Break-even versus one 16-bit target pass therefore requires `skip_full > 50%` before any overhead.

- `STRONG_GO_GREEDY`: skip_full >= 70%, zero observed errors among relevant empirically resolved argmax decisions, and no block output disagreement on blocks marked skip-full.
- `GO_GREEDY`: skip_full > 50%, zero observed resolved/output errors.
- `STOP_GREEDY`: skip_full <= 40%.
- otherwise `INCONCLUSIVE`.

The bonus-token metric is diagnostic and cannot override the primary gate.

## Required red-team outputs

The run must report:
- raw INT8-vs-FP argmax agreement;
- empirical per-token and global argmax resolution rates;
- held-out violations of calibration error bounds;
- relevant-position resolved-argmax error count;
- block skip-full fraction and ideal bit-equivalent cost;
- strict K+1 bonus skip-full fraction;
- full-target draft-match/first-mismatch statistics.

## Interpretation guard

A positive result cannot be called lossless until the empirical `delta_v` values are replaced by valid end-to-end numerical error bounds relative to the reference target. It also cannot establish GPU speedup until a real low-bit verifier implementation is benchmarked against Quasar and a full-precision target on hardware.
