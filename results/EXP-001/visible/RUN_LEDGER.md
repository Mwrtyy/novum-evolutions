# EXP-001 Visible Run Ledger

Authoritative progress record for visible execution. EXP-001 Protocol Amendment 001 adopts near-equivalent prompt runs for vr-05 through vr-08. The campaign is complete with a declared prompt deviation; it is not exact-frozen-prompt compliant.

## Progress

| Case | Trial | Baseline | Candidate | Pair status | Prompt status |
|---|---:|---|---|---|---|
| vr-01-private-memory | 1 | RECORDED | RECORDED | COMPLETE | FROZEN_EXACT |
| vr-01-private-memory | 2 | RECORDED | RECORDED | COMPLETE | FROZEN_EXACT |
| vr-01-private-memory | 3 | RECORDED | RECORDED | COMPLETE | FROZEN_EXACT |
| vr-02-waterless-cooling | 1 | RECORDED | RECORDED | COMPLETE | FROZEN_EXACT |
| vr-02-waterless-cooling | 2 | RECORDED | RECORDED | COMPLETE | FROZEN_EXACT |
| vr-02-waterless-cooling | 3 | RECORDED | RECORDED | COMPLETE | FROZEN_EXACT |
| vr-03-false-novelty | 1 | RECORDED | RECORDED | COMPLETE | FROZEN_EXACT |
| vr-03-false-novelty | 2 | RECORDED | RECORDED | COMPLETE | FROZEN_EXACT |
| vr-03-false-novelty | 3 | RECORDED | RECORDED | COMPLETE | FROZEN_EXACT |
| vr-04-battery-detection | 1 | RECORDED | RECORDED | COMPLETE | FROZEN_EXACT |
| vr-04-battery-detection | 2 | RECORDED | RECORDED | COMPLETE | FROZEN_EXACT |
| vr-04-battery-detection | 3 | RECORDED | RECORDED | COMPLETE | FROZEN_EXACT |
| vr-05-simplify-not-invent | 1 | RECORDED | RECORDED | COMPLETE | ADOPTED_NEAR_EQUIVALENT |
| vr-05-simplify-not-invent | 2 | RECORDED | RECORDED | COMPLETE | ADOPTED_NEAR_EQUIVALENT |
| vr-05-simplify-not-invent | 3 | RECORDED | RECORDED | COMPLETE | ADOPTED_NEAR_EQUIVALENT |
| vr-06-impossible-premise | 1 | RECORDED | RECORDED | COMPLETE | ADOPTED_NEAR_EQUIVALENT |
| vr-06-impossible-premise | 2 | RECORDED | RECORDED | COMPLETE | ADOPTED_NEAR_EQUIVALENT |
| vr-06-impossible-premise | 3 | RECORDED | RECORDED | COMPLETE | ADOPTED_NEAR_EQUIVALENT |
| vr-07-ai-wrapper-trap | 1 | RECORDED | RECORDED | COMPLETE | ADOPTED_NEAR_EQUIVALENT |
| vr-07-ai-wrapper-trap | 2 | RECORDED | RECORDED | COMPLETE | ADOPTED_NEAR_EQUIVALENT |
| vr-07-ai-wrapper-trap | 3 | RECORDED | RECORDED | COMPLETE | ADOPTED_NEAR_EQUIVALENT |
| vr-08-offline-clinic | 1 | RECORDED | RECORDED | COMPLETE | ADOPTED_NEAR_EQUIVALENT |
| vr-08-offline-clinic | 2 | RECORDED | RECORDED | COMPLETE | ADOPTED_NEAR_EQUIVALENT |
| vr-08-offline-clinic | 3 | RECORDED | RECORDED | COMPLETE | ADOPTED_NEAR_EQUIVALENT |

## Completion

- recorded visible generations: **48/48**
- vr-01 through vr-04: exact frozen prompts
- vr-05 through vr-08: near-equivalent prompts adopted post-hoc under `experiments/EXP-001-PROTOCOL-AMENDMENT-001.md`
- baseline and candidate used identical wording within every affected case
- no behavioral scoring was performed during adoption

## Completed judgment history

The original visible judging is retained for audit:

- judgments locked: **72/72**
- pairs: **24/24**
- evaluator roles per pair: **3/3**
- pair-majority result after post-lock reveal: candidate 15, baseline 6, tie 3
- detailed analysis: `results/EXP-001/visible/analysis/VISIBLE_JUDGING_ANALYSIS.md`
- protocol audit: `results/EXP-001/PROTOCOL_AUDIT_VISIBLE.md`

A corrected rerun then used one fresh context per pair-role assignment:

- judgments: **72/72**
- contexts: **72**
- pair majorities: candidate 11, baseline 11, tie 2
- votes: candidate 34, baseline 34, tie 4
- corrected analysis: `results/EXP-001/visible/analysis/VISIBLE_INDEPENDENCE_RERUN_ANALYSIS.md`

The strict hidden holdout is complete and the final EXP-001 verdict is `REJECT`.

## Scientific status

48/48 visible generations are preserved with the declared prompt deviation. The original 72 judgments are historical; the 72-context rerun is authoritative for visible interpretation. Neither same-family rerun is external replication.
