# Blind behavioral judging protocol

Evaluators receive only the task and anonymized outputs A/B. They must not receive candidate identity, mutation hypothesis, expected winner, or development narrative.

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

Populate every dimension for A and B. Do not infer missing scores.

## Independence

Record the actual independence level: same context, separate context same model, separate model family, or human/external. Only the latter levels should be considered strong replication. Never rename same-model judging as independent.
