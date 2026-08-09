# EXP-001 protocol audit — visible phase

Status: `VISIBLE_PHASE_AUDITED_HIDDEN_PHASE_PENDING`

## Passed

- Frozen candidate identity matches `FREEZE_RECORD.json` and `MUTATION.json`.
- All nine frozen mutation/execution/evaluation artifacts match their recorded byte sizes and SHA-256 values.
- Official raw layout contains exactly 48 non-empty outputs: 8 cases × 3 trials × 2 arms.
- The 24 adopted `vr-05`–`vr-08` official copies are byte-identical to their preserved protocol-deviation sources.
- Deterministic blinding regeneration is byte-for-byte reproducible.
- Blind public material contains 24 A/B pair packets and 72 role-specific judge prompts.
- The private A/B mapping is stored outside judge-facing directories.
- Exactly 72 judgments passed mechanical validation and were locked before reveal.
- Aggregation refuses to run without a valid 72-judgment lock.

## Declared deviations and limits

- `vr-01`–`vr-04`: exact frozen prompt strings.
- `vr-05`–`vr-08`: near-equivalent prompt strings adopted post-hoc through `EXP-001-PROTOCOL-AMENDMENT-001`.
- Therefore the whole visible campaign is not exact-string preregistration compliant.
- The three evaluator roles ran in fresh contexts from the same model family. This is not external replication.
- Each role was represented by one evaluator context across all 24 pairs, so role and evaluator identity are confounded.
- Visible cases were available during development and cannot authorize promotion.
- Most pair-cluster bootstrap intervals for dimension deltas include zero.

## Scientific conclusion at this boundary

The visible phase produces a favorable but modest signal for portfolio compression. It is compatible with a real improvement, a small role/model-specific preference effect, or task-family heterogeneity. Regressions on some cases remain meaningful.

No final EXP-001 decision is authorized. The remaining required evidence is a strict post-freeze hidden holdout using exact paired prompts, blind judging before reveal, and a final protocol audit combining visible and holdout evidence.
