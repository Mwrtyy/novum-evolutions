# Agent operating rules

## Session opening

Before substantial work, write down the exact uncertainty being reduced. Read `FOUNDING_DIRECTIVE.md`, `CONTEXT.md`, `HISTORICAL_AUDIT.md`, and `research/FRONTIER.md` when relevant.

## Hard constraints

1. `baseline/novum-2.0.0/novum-innovation-v2.0.0.zip` is immutable scientific evidence. Never rebuild it under the same identity.
2. Do not draft NOVUM 3 or a broad replacement `SKILL.md` from intuition.
3. Do not create a mutation without a reproducible behavioral failure and a falsifiable hypothesis.
4. Change one important variable at a time when practical. Preserve exact parent/diff lineage.
5. Structural validators may protect integrity; they never count as behavioral improvement by themselves.
6. Never call visible regression tasks hidden holdouts.
7. Freeze candidate bytes before selecting or generating final holdout tasks.
8. Never describe same-context or same-model judging as independent evaluation.
9. Preserve raw outputs, public blind bundles, private mappings, judgments, and analysis separately.
10. A no-go, rejected hypothesis, regression, or no-meaningful-effect result is valid research.
11. Do not rescue a disappointing result by changing the evaluation after seeing it.
12. Prefer deleting ceremony to adding fields. Every new mechanism must name the reproduced failure that requires it.

## Behavioral evaluation

Judge outputs on mechanism novelty, mechanistic depth, constraint fit, usefulness, evidence calibration, falsifiability, prior-art awareness, simpler-substitute discipline, clarity, and cost/verbosity. Report dimensions separately; do not let one aggregate hide a critical regression.

## Repository discipline

- Keep the public behavior seam small.
- Use temporary directories for harness execution.
- Seed blinding/generation randomness where available.
- Do not allow evaluator runs to mutate frozen candidate or benchmark artifacts.
- Store exact hashes at freeze boundaries.
- Create ADRs only for surprising or expensive-to-reverse decisions.

## Current frontier

The first active experiment is H1: portfolio compression. It deliberately does **not** test independent contexts; that is H2 and must remain a separate intervention so attribution survives.

## Useful checks

```bash
python harness/evolution_harness.py self-test
python harness/evolution_harness.py validate-cases benchmarks/visible-regression/cases.jsonl
python harness/test_evolution_harness.py
sha256sum baseline/novum-2.0.0/novum-innovation-v2.0.0.zip
```

Expected baseline SHA-256:
`e38cd4e62439c5759bf99bf2fc72e165abf2876f75396c170f445d6a3c529dda`
