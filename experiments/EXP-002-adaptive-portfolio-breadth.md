# EXP-002 draft — adaptive portfolio expansion

Status: `DRAFT_NOT_AUTHORIZED`

## Motivation

EXP-001 rejected a global fixed-four policy. The hidden candidate won physical-system and product-strategy cases but lost five other domains, while average score effects remained small. This suggests a task-dependent breadth/depth trade rather than one universal candidate count.

## Exact uncertainty

Can a frozen, observable expansion gate retain the depth benefits of a four-candidate start on low-entropy tasks while recovering breadth on tasks whose mechanism space remains under-covered?

## Candidate intervention

In Standard mode:

1. generate exactly four initial candidates;
2. compute the existing mechanism signatures and collision evidence;
3. expand once to eight candidates only if either:
   - fewer than three distinct carrier/state/control signatures survive the structured diversity audit; or
   - all four candidates collide with strong prior art or collapse to simpler substitutes;
4. freeze the expansion decision before survivor scoring and do not iterate the gate.

The gate uses existing NOVUM artifacts. EXP-002 must not add new evaluators, dimensions, causal schemas, or post-output steering.

## Competing hypotheses

- H2a: adaptive expansion preserves fixed-four depth where sufficient and restores coverage where four candidates are inadequate.
- H2b: the gate is noisy overhead; the accepted 8–14 baseline remains better.
- H2c: the apparent domain heterogeneity in EXP-001 is sampling noise.
- H2d: any benefit comes from extra collision work, not adaptive breadth.

## Minimum design before execution

- Freeze the gate code/text, judge packet, analysis code, success thresholds, and task-stratification procedure before selecting exact prompts.
- Use at least three arms: accepted baseline, fixed four, adaptive gate. Equalize model, tools, output cap, and approximate reasoning budget.
- Include repeated unseen cases stratified by predicted expansion status, with the stratum label generated without access to arm outputs.
- Use one fresh generation context per case/trial/arm and one fresh evaluator context per pair/role.
- Prefer at least one human or separate-model-family replication layer; same-family judgments must remain labeled internal.
- Lock all judgments before any A/B/C mapping reveal.

## Pre-registered primary outcomes

Primary: mechanism novelty, mechanistic depth, usefulness, pair preference. Secondary: constraint fit, falsifiability, simpler-substitute discipline, words/tokens, tool calls, expansion frequency, and evaluator disagreement.

The adaptive arm may advance only if it beats the accepted baseline on pair preference and improves at least one of novelty/depth without a practically meaningful usefulness regression. Exact numeric margins and equivalence bounds must be frozen before task selection.

## Stop rules

Reject the gate if it expands on almost every task, rarely expands despite repeated breadth failures, adds material cost without preference gain, or creates a new regression in clarity/constraint fit. Do not rescue it with post-hoc threshold tuning on the confirmatory set.

No production change is authorized by this draft.
