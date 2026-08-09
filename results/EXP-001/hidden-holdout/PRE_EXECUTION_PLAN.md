# EXP-001 strict post-freeze hidden holdout — pre-execution plan

Status: `TASKS_NOT_SELECTED_NOT_GENERATED_NOT_EXPOSED`

This plan records the next phase without selecting tasks from visible performance. It does not contain holdout prompts.

## Selection isolation

The task-set owner must run in a fresh context that receives only:

- `CONTEXT.md`;
- `benchmarks/generators/problem_grammar.json`;
- `benchmarks/hidden-holdout/PROTOCOL.md`;
- frozen visible task text solely for overlap rejection;
- the candidate freeze identity.

The selector must not receive visible raw outputs, blind packets, judgments, A/B mapping, visible analysis, or candidate performance summaries.

## Task-set contract

- seven cases, one per grammar domain;
- three generation trials per case per arm;
- exact same prompt bytes for baseline and candidate within every trial;
- no prompt reformulation after task-set freeze;
- no lightly reworded visible case;
- all exact prompt text, selection seed/procedure, timestamp, task hashes, and overlap audit frozen before either arm runs;
- baseline and candidate generation performed in separated fresh contexts with equivalent tool, evidence, and approximate reasoning budgets;
- 21 blinded pairs;
- the same three frozen evaluator roles, each in a fresh context and blind to A/B identity;
- all 63 judgments locked before reveal;
- final analysis must keep visible and holdout results separate before any combined interpretation.

## Deterministic seed

The selector seed is SHA-256 of:

`EXP-001-HIDDEN-HOLDOUT-V1|ad61ff084f482d9e06b3398970be565bdd5d7d29c132b1a3dfd0c45bd88a4688`

The seed fixes grammar-cell selection. Task wording still requires semantic generation and an overlap audit, so the task-set owner and actual independence level must be recorded honestly.

## Stricter treatment required

Because half of the visible cases used post-hoc adopted near-equivalent prompts, any hidden prompt edit after freeze invalidates the hidden campaign. Invalid runs must be discarded as invalid evidence, not repaired or silently adopted.

## Decision boundary

No final EXP-001 decision follows from this plan. Only locked visible results + locked hidden results + final protocol audit can support `PROMOTE`, `PARTIAL WIN / MUTATE`, `REJECT`, or `INCONCLUSIVE`.
