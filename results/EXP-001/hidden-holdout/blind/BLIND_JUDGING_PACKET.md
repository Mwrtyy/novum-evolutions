# Blind behavioral judging packet

Use this packet in a fresh evaluator context after outputs have been blinded. The evaluator receives only the task, anonymized Output A, anonymized Output B, this rubric, and its assigned evaluator role. Do not reveal system identity, source order, mutation hypothesis, expected winner, development history, or the private blinding map.

## Dimensions (0–10)

- `mechanism_novelty`
- `mechanistic_depth`
- `constraint_fit`
- `usefulness`
- `evidence_calibration`
- `falsifiability`
- `prior_art_awareness`
- `simpler_substitute_discipline`
- `clarity`

Scores are observations from an evaluator, not truth. Preserve per-dimension values and disagreement.

## Required evaluator roles

Every blinded pair must receive one locked judgment from each existing role:

- `hostile_regression`
- `simplicity`
- `domain_or_generalist`

## Required judgment record

```json
{
  "pair_id": "...",
  "evaluator_id": "...",
  "evaluator_role": "hostile_regression | simplicity | domain_or_generalist",
  "scores": {
    "A": {"mechanism_novelty": 0.0},
    "B": {"mechanism_novelty": 0.0}
  },
  "preference": "A | B | tie",
  "critical_flags": [],
  "rationale": "short evidence-based explanation"
}
```

Populate every frozen dimension for A and B. Do not infer missing scores.

## Independence

Before judging begins, record the actual independence level for each evaluator as one of: `same_context`, `separate_context_same_model`, `separate_model_family`, or `human_or_external`. Only the latter levels should be considered strong replication. Never rename same-model judging as independent external replication. No independence claim is made at freeze time.

Judgments must be locked before the private A/B mapping is revealed.
