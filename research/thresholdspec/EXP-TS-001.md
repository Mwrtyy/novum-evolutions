# ThresholdSpec EXP-TS-001 — pretrained margin survival

Status: `FROZEN`

This is invention research using NOVUM discipline, not a mutation of NOVUM 2.0.0.

## Exact uncertainty

Does the toy-scale signal survive on a pretrained language-model pair: are speculative accept/reject margins usually large enough that a lower-precision target evaluation can resolve the decision before full precision?

## Frozen setup

- drafter: `HuggingFaceTB/SmolLM2-135M`
- target: `HuggingFaceTB/SmolLM2-360M`
- events: 1,024
- context length: 32 tokens
- symmetric groupwise quantize/dequantize: 4, 6, 8 bits, group size 64
- seed: `20260817`
- first 50%: calibration; second 50%: held-out test

For draft token `x ~ q` and `u ~ U(0,1)`, reference acceptance is determined by the sign of `log p(x) - log q(x) - log u`.

At each precision tier, the calibration maximum absolute error in `log p(x)` is used as an empirical bound. A test event is resolved early only when its approximate margin magnitude exceeds that bound.

## Pre-registered decision

- `STRONG_GO`: INT8 resolves at least 80% of held-out events with zero observed certified-decision errors, and progressive 4→6→8→FP sends at most 20% to FP.
- `GO`: INT8 resolves at least 70% with zero observed certified-decision errors, and FP fallback is at most 30%.
- `STOP`: INT8 resolves less than 40%.
- otherwise: `INCONCLUSIVE`.

## Guardrail

The calibration maximum is empirical, not a formal worst-case certificate. A positive result supports further work on certified progressive verification; it does not establish losslessness, GPU speedup, or large-model performance.

## Raw evidence

The workflow uploads `summary.json` and per-event `events.csv` as a GitHub Actions artifact.
