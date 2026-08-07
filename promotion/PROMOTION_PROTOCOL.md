# Promotion protocol

Promotion means replacing the accepted NOVUM behavioral baseline. It is intentionally harder than merging a research artifact.

## Before final evaluation

1. Freeze candidate bytes and record SHA-256.
2. Freeze the experiment hypothesis, evaluation dimensions, generation budget, stopping rules, and any experiment-specific effect threshold.
3. Freeze judge instructions.
4. Verify the candidate still passes visible regression/integrity checks.
5. Only then select/generate final holdouts under `benchmarks/hidden-holdout/PROTOCOL.md`.

## Required evidence

A promotion report must include:

- blind baseline-vs-candidate results on post-freeze unseen tasks;
- per-dimension and per-task distributions, not only one aggregate;
- mechanism novelty and mechanistic depth;
- usefulness and constraint fit;
- evidence calibration and falsifiability;
- simpler-substitute discipline;
- evaluator disagreement;
- critical failures/flags;
- output/runtime/search/tool-call cost;
- complexity added to the deployed skill;
- evaluator/generator independence level;
- visible-regression results;
- exact candidate and baseline hashes.

## Decision rules

- Structural compliance alone cannot promote.
- A serious collapse in a critical dimension can block promotion even if an aggregate improves.
- A tiny gain with large instruction/runtime complexity can be rejected as `NO_MEANINGFUL_EFFECT`.
- Unseen performance must be materially better under the precommitted experiment criterion; do not invent a favorable threshold after results.
- If confidence/replication is inadequate, return `INCONCLUSIVE` rather than promote.
- Independent replication should be sought before replacing the accepted baseline; if unavailable, state the limitation and do not relabel internal judging as independent.
- Rollback must remain a one-artifact operation to the previous accepted hash.

Valid outcomes: `SUPPORTED`, `PARTIALLY_SUPPORTED`, `INCONCLUSIVE`, `REJECTED`, `REGRESSION`, `NO_MEANINGFUL_EFFECT`.
