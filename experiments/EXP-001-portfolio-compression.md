# EXP-001 — Portfolio compression

Status: `PLANNED`

## Exact uncertainty

Does NOVUM 2.0.0's Standard-mode breadth target (8–14 sequential candidates) reduce mechanism depth and novelty by spreading a fixed reasoning budget too thin?

## Observed failure motivating the experiment

Historical evidence shows that NOVUM's structural rigor can be satisfied without material behavioral improvement, and Candidate.2 improved feasibility/constraint handling while novelty fell. The accepted skill also requires a broad Standard portfolio while simultaneously asking for prior-art search, red-team work, evolution, and falsification.

We do **not** yet know that candidate count is causal. This experiment isolates that question.

## Competing hypotheses

- **H1a — depth-budget hypothesis:** reducing the initial portfolio to exactly four candidates and reallocating the released budget to collision/deepening improves mechanistic depth and novelty without harming usefulness.
- **H1b — search-coverage hypothesis:** 8–14 candidates provide valuable breadth; compression increases anchoring and misses better mechanisms.
- **H1c — no-material-effect:** candidate count is not the main bottleneck; output quality remains within noise once total budget is held constant.
- **H1d — conservative-selection side effect:** compression improves depth but reduces novelty because fewer exploratory branches survive.

## Selected intervention

One primary change only:

> In Standard mode, generate **exactly four** initial candidates instead of 8–14, while holding the total generation/reasoning budget approximately constant and spending the released budget on deeper baseline collision, prior-art attack, simpler-substitute testing, and falsification of the survivors.

Do **not** introduce independent contexts in this experiment. That is H2 and must remain separately testable.

Do **not** add new causal schemas, validators, scores, roles, or metadata.

## Parent and lineage

- parent: immutable NOVUM Innovation `2.0.0`
- parent SHA-256: `e38cd4e62439c5759bf99bf2fc72e165abf2876f75396c170f445d6a3c529dda`
- mutation artifact: not yet created

## Pre-result prediction

If H1a is true, the mutation should show:

- fewer mechanically redundant candidates;
- stronger mechanism-to-observable explanations;
- better discriminating experiments;
- equal or better novelty at survivor level;
- similar or lower output cost;
- no increase in forced-invention behavior.

Possible regression: fewer candidates may reduce search coverage and cross-domain surprise.

## Evaluation design

Development uses visible regressions only. Once the mutation bytes are frozen, create/select a post-freeze holdout from `benchmarks/generators/problem_grammar.json`.

Compare baseline and mutation with equivalent model, tools, evidence access, and approximate total token budget. Use at least repeated trials where runtime allows. Blind identity and ordering before judging.

Primary behavioral dimensions:

- mechanism novelty;
- mechanistic depth;
- usefulness;
- constraint fit;
- falsifiability;
- simpler-substitute discipline.

Secondary:

- prior-art awareness;
- evidence calibration;
- output words/tokens;
- evaluator disagreement.

No result exists yet. Do not treat this file as evidence for H1a.
