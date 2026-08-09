# EXP-001 visible blind-judging execution record

Status: `72_OF_72_LOCKED_AND_REVEALED_FOR_AGGREGATION`

## Isolation actually used

Three fresh evaluator contexts were created, one per frozen role:

| Evaluator ID | Role | Assignments | Independence classification |
|---|---|---:|---|
| `hostile_regression-01` | `hostile_regression` | 24 | `separate_context_same_model` |
| `simplicity-01` | `simplicity` | 24 | `separate_context_same_model` |
| `domain_or_generalist-01` | `domain_or_generalist` | 24 | `separate_context_same_model` |

Each evaluator received only its 24 role-specific public judge prompts. Evaluators were explicitly prohibited from opening `blind/private/AB_MAPPING.json`, inspecting private files, or inferring system identity. They did not receive each other’s judgments.

This is context isolation, not strong external replication. The evaluators belong to the same model family.

## Mechanical lock

- expected assignments: 72
- accepted assignments: 72
- pairs: 24
- roles per pair: 3
- judgment-set SHA-256: `825cef9dd7950bc35fbdddc6cd74a2c1330aef6284ad7a2f142988fc935af1cd`
- A/B mapping used during validation/lock: no
- reveal allowed only after the lock existed: yes

Validation required exact pair and role coverage, a non-empty evaluator ID, both A/B score objects, all nine frozen dimensions, finite numeric values from 0 through 10, preference `A`/`B`/`tie`, a string-list `critical_flags`, and a non-empty rationale.

The canonical lock is `judgments-locked/LOCK.json`. The submitted JSONL is preserved, and each canonical judgment is stored separately under `judgments-locked/`.

## Interpretation boundary

The visible result is evidence, not a promotion decision. `vr-05`–`vr-08` remain subject to Protocol Amendment 001 and must not be represented as exact-string preregistration compliant. Strict hidden holdout evidence remains required.
