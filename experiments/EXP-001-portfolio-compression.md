# EXP-001 — Portfolio compression

Status: `COMPLETE_REJECTED`

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
- mutation artifact: `mutations/EXP-001-portfolio-compression/candidate-SKILL.md`
- baseline skill SHA-256: `1d6dea7cdb5343aad114ad48fa9f010ea88bd8bf1ccb6c45059f88e1bfa4c4a6`
- candidate skill SHA-256: `ad61ff084f482d9e06b3398970be565bdd5d7d29c132b1a3dfd0c45bd88a4688`
- freeze commit: `a5fbd315401340486895384607b7ed92a33a05be`
- freeze timestamp UTC: `2026-08-07T23:35:32Z`
- exact diff: `mutations/EXP-001-portfolio-compression/SKILL.patch`
- freeze record: `mutations/EXP-001-portfolio-compression/FREEZE_RECORD.json`

The frozen runtime change is one conceptual variable: Standard initial portfolio breadth/depth allocation. The candidate produces exactly four initial candidates and reallocates the saved candidate-generation/research effort across NOVUM 2.0 mechanisms that already existed. No other runtime mechanism was intentionally changed.

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

## Frozen execution preparation

- generation protocol: `mutations/EXP-001-portfolio-compression/execution/GENERATION_PROTOCOL.md`
- baseline packet: `mutations/EXP-001-portfolio-compression/execution/BASELINE_PACKET.md`
- candidate packet: `mutations/EXP-001-portfolio-compression/execution/CANDIDATE_PACKET.md`
- blind evaluator packet: `mutations/EXP-001-portfolio-compression/evaluation/BLIND_JUDGING_PACKET.md`
- visible cases: 8 validated cases, 3 trials per case per arm
- harness self-test: `PASS`
- visible-case schema validation: `PASS`
- repository-native harness test: `PASS`
- hidden holdout: `NOT_GENERATED_NOT_SELECTED_NOT_EXPOSED`
- behavioral evidence: `NOT_RUN`

## Final result

The original visible result was superseded by a 72-fresh-context rerun: candidate 11, baseline 11, tie 2 by pair majority.

The strict hidden holdout used 21 pairs and 63 fresh-context judgments. Baseline won 14–7 by pair majority and 38–25 by individual preference. Mean candidate-minus-baseline deltas were -0.067 for mechanism novelty and -0.021 for mechanistic depth. All dimension intervals included zero.

H1a is not supported. Verdict: `REJECT`. The accepted NOVUM 2.0.0 skill remains unchanged; the frozen candidate is retained only as an experimental artifact.

See `results/EXP-001/FINAL_REPORT.md` and `results/EXP-001/PROTOCOL_AUDIT_FINAL.md`.
