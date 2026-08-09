# EXP-001 Visible Blind-Judging Analysis

Status: `VISIBLE_JUDGING_COMPLETE_HIDDEN_HOLDOUT_REQUIRED`

- Locked judgments: **72/72** across **24/24** blinded pairs.
- Pair-majority: candidate **15**, baseline **6**, tie **3**.
- Judge preferences: candidate **43**, baseline **22**, tie **7**.
- Tie-adjusted candidate judge win rate: **64.6%** (pair-cluster bootstrap 95% CI 50.7%–77.1%).

## Scores and deltas

| Dimension | Baseline mean | Candidate mean | Delta C−B | dz | Cluster-bootstrap 95% CI |
|---|---:|---:|---:|---:|---:|
| mechanism_novelty | 5.942 | 6.008 | +0.067 | 0.087 | [-0.178, +0.349] |
| mechanistic_depth | 8.917 | 8.951 | +0.035 | 0.076 | [-0.132, +0.186] |
| constraint_fit | 9.289 | 9.319 | +0.031 | 0.073 | [-0.103, +0.160] |
| usefulness | 8.969 | 9.024 | +0.054 | 0.124 | [-0.094, +0.201] |
| evidence_calibration | 8.881 | 8.972 | +0.092 | 0.213 | [-0.046, +0.228] |
| falsifiability | 8.804 | 8.976 | +0.172 | 0.194 | [-0.176, +0.478] |
| prior_art_awareness | 8.983 | 9.171 | +0.188 | 0.310 | [+0.011, +0.401] |
| simpler_substitute_discipline | 8.547 | 8.674 | +0.126 | 0.102 | [-0.306, +0.540] |
| clarity | 9.015 | 9.025 | +0.010 | 0.021 | [-0.146, +0.158] |

## Results by case

| Case | Prompt status | Candidate prefs | Baseline prefs | Ties | Pair majorities C/B/tie | Mean delta across dimensions |
|---|---|---:|---:|---:|---:|---:|
| vr-01-private-memory | FROZEN_EXACT | 4 | 5 | 0 | 1/2/0 | -0.120 |
| vr-02-waterless-cooling | FROZEN_EXACT | 5 | 4 | 0 | 2/1/0 | +0.081 |
| vr-03-false-novelty | FROZEN_EXACT | 6 | 2 | 1 | 2/0/1 | +0.133 |
| vr-04-battery-detection | FROZEN_EXACT | 7 | 2 | 0 | 2/1/0 | +0.340 |
| vr-05-simplify-not-invent | ADOPTED_NEAR_EQUIVALENT | 4 | 5 | 0 | 1/2/0 | -0.143 |
| vr-06-impossible-premise | ADOPTED_NEAR_EQUIVALENT | 3 | 2 | 4 | 1/0/2 | -0.031 |
| vr-07-ai-wrapper-trap | ADOPTED_NEAR_EQUIVALENT | 6 | 2 | 1 | 3/0/0 | +0.093 |
| vr-08-offline-clinic | ADOPTED_NEAR_EQUIVALENT | 8 | 0 | 1 | 3/0/0 | +0.335 |

## Results by trial

| Trial | Candidate prefs | Baseline prefs | Ties | Mean delta across dimensions |
|---:|---:|---:|---:|---:|
| 1 | 15 | 5 | 4 | +0.095 |
| 2 | 14 | 8 | 2 | +0.105 |
| 3 | 14 | 9 | 1 | +0.058 |

## Results by evaluator role

| Role | Candidate prefs | Baseline prefs | Ties | Mean delta across dimensions |
|---|---:|---:|---:|---:|
| hostile_regression | 14 | 6 | 4 | +0.081 |
| simplicity | 14 | 10 | 0 | +0.083 |
| domain_or_generalist | 15 | 6 | 3 | +0.094 |

## Disagreement, regressions, and flags

- Fleiss’ kappa over candidate/baseline/tie preferences: **0.255**.
- Unanimous pairs: **11**; split pairs: **13**.
- Dimensions with negative mean delta: **none**.
- Baseline-majority pairs: **vr-01-t1, vr-01-t2, vr-02-t3, vr-04-t2, vr-05-t2, vr-05-t3**.
- Critical flags preserved: **60**; arm-prefixed flags were translated only after reveal.

### Candidate-targeted critical flags

- `vr-01-t1` / `hostile_regression` — bounded choice operations can still leak preferences through adaptive probing
- `vr-01-t1` / `domain_or_generalist` — bounded verdicts still expose preference signals and open-ended generation remains under-specified.
- `vr-02-t2` / `hostile_regression` — limited trim capacity may not preserve its stated full-load objective through an unusually prolonged heat event
- `vr-02-t3` / `hostile_regression` — hybrid sensible-plus-PCM storage adds complexity without proving superiority to dry-first trim refrigeration
- `vr-02-t3` / `simplicity` — hybrid_storage_adds_unproven_complexity
- `vr-03-t1` / `hostile_regression` — outcome-linked settlement risks Goodhart effects despite its bounded variable component
- `vr-03-t3` / `hostile_regression` — mastery-linked compensation remains gameable and transfer probes may not measure durable learning
- `vr-03-t3` / `simplicity` — mastery_linked_settlement_adds_measurement_and_incentive_risk
- `vr-04-t1` / `hostile_regression` — press-and-measure prior art leaves novelty dependent on a narrow hysteresis observable
- `vr-04-t2` / `hostile_regression` — two-transducer pulse-order spectroscopy may cost more and calibrate less reliably than its claimed production-screen simplicity
- `vr-05-t3` / `hostile_regression` — no decisive time-savings validation protocol is supplied
- `vr-07-t1` / `hostile_regression` — preempting workers already serving another restaurant may create operational, employment, and second-failure risks

All baseline-targeted and unspecified/both flags remain preserved in `VISIBLE_JUDGING_ANALYSIS.json`.

## Limits and interpretation boundary

- `vr-01`–`vr-04` used exact frozen prompts; `vr-05`–`vr-08` used near-equivalent prompts adopted post-hoc. The campaign is not exact-string preregistration compliant.
- Evaluators were fresh contexts from the same model family. This reduces shared conversation context but is not independent external replication.
- The 72 judgments are nested within 24 pairs; cluster-bootstrap intervals account for pair clustering, but eight visible cases remain a small, development-visible sample.
- Effect sizes are descriptive paired dz values across judge records, not population guarantees.
- No promotion decision is authorized from the visible set alone. The next evidentiary phase is the strict post-freeze hidden holdout, followed by a protocol audit.
