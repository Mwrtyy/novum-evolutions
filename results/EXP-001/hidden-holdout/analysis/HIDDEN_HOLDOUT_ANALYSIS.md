# EXP-001 hidden-holdout analysis

Status: `COMPLETE_REVEALED_AFTER_LOCK`

## Result

The frozen portfolio-compression candidate lost the strict holdout.

| Measure | Candidate | Baseline | Tie |
|---|---:|---:|---:|
| Pair majorities (21 pairs) | 7 | 14 | 0 |
| Individual preferences (63 judgments) | 25 | 38 | 0 |

The candidate's tie-adjusted judgment win rate was 0.397. The 10,000-iteration cluster bootstrap by pair gave a 95% interval of [0.238, 0.571]. Fleiss' kappa over the three preference categories was 0.469; 13 pairs were unanimous and 8 were split.

This is evidence against promoting the mutation, not proof that four candidates are universally worse. The interval includes 0.5 and the score effects are small, but EXP-001 required positive behavioral evidence and did not produce it.

## Dimension effects

Mean deltas are candidate minus baseline. Confidence intervals are 10,000-iteration cluster bootstraps over the 21 pairs.

| Dimension | Mean delta | Paired dz | 95% CI |
|---|---:|---:|---:|
| mechanism novelty | -0.067 | -0.134 | [-0.273, +0.124] |
| mechanistic depth | -0.021 | -0.043 | [-0.192, +0.183] |
| constraint fit | +0.019 | +0.031 | [-0.208, +0.259] |
| usefulness | -0.003 | -0.006 | [-0.194, +0.230] |
| evidence calibration | +0.006 | +0.012 | [-0.187, +0.225] |
| falsifiability | +0.014 | +0.038 | [-0.113, +0.165] |
| prior-art awareness | -0.117 | -0.095 | [-0.652, +0.375] |
| simpler-substitute discipline | +0.086 | +0.097 | [-0.235, +0.438] |
| clarity | -0.060 | -0.104 | [-0.289, +0.154] |

No dimension interval excluded zero. The intended primary gains—mechanism novelty and mechanistic depth—were both directionally negative. Small positive movement in simpler-substitute discipline did not compensate for the preference loss.

## Heterogeneity

| Case | Candidate votes | Baseline votes | Candidate pair wins | Baseline pair wins | Mean judgment win rate |
|---|---:|---:|---:|---:|---:|
| hh-01 software | 2 | 7 | 1 | 2 | 0.222 |
| hh-02 physical system | 6 | 3 | 2 | 1 | 0.667 |
| hh-03 operations | 2 | 7 | 1 | 2 | 0.222 |
| hh-04 scientific method | 3 | 6 | 1 | 2 | 0.333 |
| hh-05 economic system | 3 | 6 | 0 | 3 | 0.333 |
| hh-06 product strategy | 6 | 3 | 2 | 1 | 0.667 |
| hh-07 public service | 3 | 6 | 0 | 3 | 0.333 |

The candidate won physical-system and product-strategy cases, but lost five of seven domains. Economic-system and public-service cases were 0–3 at the pair level. This pattern is compatible with task-dependent value rather than a universally superior breadth target.

Trial preference counts were 10–11, 7–14, and 8–13 candidate–baseline. Role counts were 9–12 for hostile regression, 9–12 for simplicity, and 7–14 for domain/generalist. The loss therefore was not confined to one evaluator role.

## Cost parity

Baseline outputs averaged 1,815 words and 7.62 self-reported tool calls. Candidate outputs averaged 1,809 words and 8.43 tool calls. Output length was effectively held constant; the candidate did not obtain a lower-cost win.

## Confirmatory interpretation

The visible rerun under one fresh context per assignment was exactly neutral: 11–11–2 pair majorities and 34–34–4 votes. The original visible 15–6 candidate result came from only three persistent evaluator contexts and did not replicate under stricter independence. The hidden result must be reported separately, not pooled with visible data.

Taken together, EXP-001 does not support H1a. Four initial candidates may help selected constraint-heavy or product-design cases, but the fixed global compression did not improve the intended novelty/depth targets and lost the strict holdout preference comparison.

## Integrity anchors

- Holdout task set SHA-256: `819f17cb4a62200aab6252047b03f74e84fb757bf01758f0b4d97db51f2107e7`
- Holdout freeze manifest SHA-256: `6e3d48a88f8db3cdc76c1455f48475bde71e6076e4a98559c28b4f827ae99e2c`
- Generation config SHA-256: `4ad5f533b0560d066d11ac099755835836514c82eaa0eb563fea5f8b63b04720`
- Validated output manifest SHA-256: `0a66e62ef70e1c02b5420fa0095a96645da3769ca2670e5c22ec0a7b3c995519`
- Public blind bundle SHA-256: `0633945304f979983d7c872b54e936097ac13272c08dcce3b7016c02573b1671`
- Frozen judge packet SHA-256: `babae4b92adfa8a7181ebf4f5b9885de85adc25f4631b42c75de6d0e391d8cf0`
- Locked judgments SHA-256: `80009ca7863240f5149321254742dc06c3d5349f59d0a2c1adb5c281f6ad5f49`
- Lock file SHA-256: `ee8f1efc605dd0381aa54bdde62eef3de4261325450e4188b8902e018c3fa7ca`
- Mapping SHA-256: `c699ee0c5c1448539348b0c1b8483cc202035e803a7a38df930fb60d0a8e25e3`
- Analysis JSON SHA-256: `b8464d45028dab04cb02279e9991429b0b4a0e0923be7d5396710c594439454d`

Verdict contribution: `REJECT`.
