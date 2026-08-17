# EXP-TS-004 — SignedRankSpec pretrained ranking bounds

Status: `FROZEN`

This is a pre-registered mutation of the failed EXP-TS-003 certificate, not a retroactive reinterpretation of its result.

## Exact uncertainty

EXP-TS-003 found 97.34% raw INT8↔FP target argmax agreement but only 12.5% K=4 block skip-full under symmetric empirical logit intervals. Is that failure caused primarily by throwing away the sign and correlation structure of logit error?

## Mechanism

For each vocabulary coordinate `v`, define the low-bit target logit error

`e_v = z8_v - zFP_v`.

On calibration positions, record signed coordinate bounds

`l_v = min_cal e_v`, `u_v = max_cal e_v`.

If those intervals were valid bounds, then for the INT8 argmax candidate `j` the exact FP pairwise gap obeys

`zFP_j - zFP_v = (z8_j - z8_v) - e_j + e_v`

and therefore

`zFP_j - zFP_v >= (z8_j - u_j) - (z8_v - l_v)`.

Thus the FP argmax is certified whenever

`z8_j - u_j > max_{v != j}(z8_v - l_v)`.

This is a ranking certificate: it spends no precision on absolute probabilities that cannot change the argmax ordering.

## Frozen setup

Identical model/workload setup to EXP-TS-003:
- drafter `HuggingFaceTB/SmolLM2-135M`
- target `HuggingFaceTB/SmolLM2-360M`
- 256 contexts; first 128 calibration, last 128 held-out
- context 32, greedy K=4
- FP32 reference target
- group-64 symmetric INT8 weight quantize/dequantize
- seed `20260817`

The target scores K draft positions plus the bonus position. Only positions up to the first target/draft mismatch are relevant for verification.

## Primary gate

`skip_full` is the held-out fraction of K=4 blocks whose exact greedy verification path can terminate using the empirical signed ranking intervals without invoking the FP target.

Idealized two-pass traffic: `8 + 16*(1-skip_full)` bit-equivalents; theoretical break-even requires `skip_full > 50%`.

- `STRONG_GO_SIGNED`: skip_full >= 70%, zero observed wrong signed-certified argmax decisions, and zero output disagreement among skip-full blocks.
- `GO_SIGNED`: skip_full > 50%, same zero-observed-error conditions.
- `STOP_SIGNED`: skip_full <= 40%.
- otherwise `INCONCLUSIVE`.

## Frozen diagnostics

Report:
- raw INT8↔FP argmax agreement;
- signed position certification rate;
- symmetric certification rate on the same run for comparison;
- signed skip-full and strict bonus skip-full rates;
- idealized bit costs;
- calibration signed interval widths;
- held-out fraction of logit coordinates outside `[l_v,u_v]`;
- fraction of positions with any interval violation;
- wrong argmax count among signed-certified positions;
- output disagreement among signed skip-full blocks.

## Interpretation guard

Calibration extrema are not formal numerical bounds. A GO demonstrates ranking headroom and justifies work on sound runtime bounds; it does not establish lossless decoding or GPU speedup. If this mutation returns STOP, the empirical precision-certificate route is considered exhausted for this model pair unless a qualitatively new bound is introduced.
