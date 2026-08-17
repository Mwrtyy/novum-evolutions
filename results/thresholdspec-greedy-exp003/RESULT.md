# ArgmaxSpec EXP-TS-003 — Result

Status: `COMPLETE`

Pre-registered decision: **`STOP_GREEDY`**.

## Result

On SmolLM2-135M → SmolLM2-360M, K=4 greedy blocks:

- raw INT8 vs FP target argmax agreement: **97.34%** across held-out relevant+bonus positions;
- symmetric per-token empirical interval resolution: **48.91%** of positions;
- blocks completing verification without full target: **12.50%**;
- idealized 8-bit-first + 16-bit-fallback cost: **22.0 bit-equivalents**, worse than a 16-bit verifier;
- strict bonus-token skip-full rate: **9.38%**;
- observed wrong argmax among positions called resolved: **0**;
- observed output disagreement among blocks called skip-full: **0**.

The frozen gate therefore stops this **symmetric-interval** ArgmaxSpec variant.

## Important diagnosis

The failure is not primarily low-bit model quality. INT8 already matches the FP argmax on 97.34% of positions. The failure is the conservatism of the empirical certificate: treating each vocabulary coordinate as an independent symmetric `±delta_v` interval makes the proof obligation much harder than the actual ranking event.

The calibration maxima are also not valid worst-case bounds. Although only ~0.09% of held-out logit coordinates exceed their per-token calibration maximum, **51.56% of held-out positions contain at least one vocabulary coordinate exceeding its bound** because the vocabulary is large. No formal correctness claim is allowed.

## Mutation justified before further model work

For argmax, independent absolute-logit accuracy is unnecessary. If the INT8 error for vocabulary coordinate `v` is `e_v = z8_v - zFP_v` and a sound signed interval `l_v <= e_v <= u_v` is available, candidate `j` is certified whenever

`z8_j - u_j > max_{v != j}(z8_v - l_v)`.

This directly bounds the pairwise ranking event and is strictly tighter than symmetric intervals whenever quantization error is biased or asymmetric. A toy-scale post-hoc test performed after freezing EXP-TS-003 improved K=4 skip-full from 55.86% to 69.14%; a 1,000-resplit stress test averaged 71.77% with no observed resolved-block errors. This evidence is exploratory and cannot alter the official EXP-TS-003 STOP.

Next experiment: pre-register the signed-ranking mutation separately and test it on the same pretrained pair.
