# EXP-002A — predictive validity of the adaptive expansion gate

Status: `DRAFT_READY_FOR_WEB_PILOT`

## Exact uncertainty being reduced

Before spending a confirmatory campaign on EXP-002, determine whether the proposed pre-frozen gate signals actually predict when expanding a four-candidate portfolio to eight improves invention behavior.

This experiment does **not** test or authorize a NOVUM production mutation. It tests whether EXP-002's decision rule is informative enough to justify a later adaptive-breadth experiment.

## Why this experiment exists

EXP-001 rejected a fixed global four-candidate policy. EXP-002 proposes using mechanism-signature diversity and prior-art/substitute collisions to decide whether to expand from four candidates to eight.

Historical evidence already warns that mechanism diversity can be simulated and that carrier/state/control roles are partly self-declared. Therefore the gate itself must earn trust before it controls search budget.

## Competing hypotheses

- **H2A-1 — predictive gate:** pre-output gate signals distinguish tasks where 4→8 expansion produces a material gain from tasks where it does not.
- **H2A-2 — noisy gate:** apparent low diversity/collision does not predict expansion benefit better than chance or a trivial task-complexity heuristic.
- **H2A-3 — collision-only signal:** prior-art/substitute collision carries the useful signal; mechanism-signature diversity adds little or harms prediction.
- **H2A-4 — diversity-only signal:** signature diversity carries useful signal while collision evidence adds little.
- **H2A-5 — expansion rarely helps:** the main EXP-001 lesson is not conditionality; four-versus-eight differences are mostly noise at this budget.

## Experimental unit

One unseen invention problem evaluated under two search-width conditions using the same model family and approximately matched total reasoning/output budget:

- `W4`: exactly four candidate mechanisms.
- `W8`: exactly eight candidate mechanisms.

The gate prediction is made **before** W8 outputs or comparative judgments are revealed.

## Gate features under test

Record separately; do not collapse them into one opaque score during the pilot.

1. **Signature coverage** — count of distinct carrier/state/control tuples among the four W4 candidates.
2. **Semantic mechanism collision** — evaluator judgment of how many W4 candidates are materially the same mechanism despite wording/signature differences.
3. **Prior-art collision rate** — fraction of W4 candidates with strong mechanism-level prior-art collision.
4. **Simpler-substitute collapse rate** — fraction of W4 candidates dominated by a simpler plausible substitute.
5. **Residual mechanism-space uncertainty** — pre-frozen ordinal judgment (`low`, `medium`, `high`) answering whether important mechanism families remain unexplored after W4.

Feature 5 is included as a deliberately more semantic alternative to self-declared signatures. It must be judged from a frozen rubric and cannot see W8.

## Web-native execution design

The pilot is deliberately executable with fresh ChatGPT Web chats. No Codex, autonomous agents, API orchestration, or programmatic multi-agent framework is required.

For each problem:

1. Fresh chat `GEN-W4`: produce the W4 invention packet.
2. Fresh chat `GATE`: receive only the problem, constraints, frozen gate rubric, and W4 packet; record all five gate features plus binary prediction `EXPAND` / `DO_NOT_EXPAND`.
3. Fresh chat `GEN-W8`: produce W8 under the matched budget rule.
4. Fresh blind judge chats compare W4 and W8 in both orders where practical.
5. Lock judgments and gate prediction before revealing whether W4 or W8 won.
6. Record whether expansion produced a practically meaningful improvement.

No chat that generated W4 may judge W4 versus W8 for confirmatory evidence.

## Pilot task count

Start with **12 development-only problems** spanning at least six invention domains. These are calibration data and can never become final holdout evidence for EXP-002.

Recommended composition:

- 2 inference/systems problems;
- 2 algorithmic problems;
- 2 hardware/physical-system problems;
- 2 software/tooling problems;
- 2 product/strategy mechanism problems;
- 2 deliberately low-entropy problems where a simple solution may dominate.

Do not select problems after observing gate performance.

## Matched-budget rule

Width must be the main manipulated variable.

- W4 may spend up to twice the per-candidate elaboration budget of W8.
- Both arms receive the same problem, constraints, available evidence, prior-art access policy, and final output cap.
- Record words/tokens when available, tool/search count, and wall-clock proxy if manually observable.

If the platform prevents exact token matching, report the achieved imbalance rather than claiming equality.

## Expansion benefit label

The label is not "W8 scored higher somewhere".

Mark `EXPANSION_HELPED` only when the blinded comparison shows:

1. W8 wins pair preference, **and**
2. W8 improves mechanism novelty or mechanistic depth, **and**
3. there is no practically meaningful usefulness or constraint-fit regression.

Otherwise label `EXPANSION_NOT_ESTABLISHED`.

Exact numeric equivalence bounds are intentionally deferred until the pilot reveals realistic judgment variance; they must be frozen before any confirmatory EXP-002 campaign.

## Primary pilot analyses

Because this is a small calibration pilot, report raw contingency tables before any model fit.

- Gate `EXPAND` vs observed `EXPANSION_HELPED`.
- Sensitivity and specificity.
- Positive and negative predictive value.
- Balanced accuracy.
- Leave-one-domain-out stability.
- Feature-wise association for signature coverage, semantic collision, prior-art collision, substitute collapse, and residual-space uncertainty.

Compare against two trivial predictors:

- `ALWAYS_EXPAND`;
- a frozen simple task-complexity heuristic that does not inspect W4 outputs.

Do not claim a useful gate merely because accuracy exceeds 50% on 12 tasks.

## Decision rule for proceeding to EXP-002

Proceed to a frozen confirmatory EXP-002 gate only if the pilot shows all of the following:

1. the gate makes both `EXPAND` and `DO_NOT_EXPAND` predictions often enough to be operationally nontrivial;
2. prediction is directionally better than both trivial comparators;
3. performance is not carried by a single domain;
4. at least one observable feature has a coherent relationship with expansion benefit;
5. no evidence shows the gate systematically suppresses expansion on cases where W8 gains novelty/depth.

Otherwise revise or reject the adaptive-gate hypothesis **before** spending a hidden holdout.

## Failure / stop conditions

Stop and mark the gate unsupported if:

- it predicts expansion on nearly every problem;
- it almost never predicts expansion;
- signature coverage conflicts repeatedly with semantic collision and the frozen rule has no principled resolution;
- W8 rarely produces a meaningful benefit at all;
- same-family judging is too unstable to label expansion benefit;
- post-hoc threshold edits are needed to make the gate look predictive.

## What this experiment cannot establish

A successful pilot does not show that adaptive breadth beats NOVUM 2.0. It only establishes that there may be a predictive signal worth testing in EXP-002.

A failed pilot does not establish that adaptive breadth is useless; it establishes that this proposed gate is not yet justified.

## Production status

NOVUM Innovation 2.0.0 remains unchanged. No production mutation, new `SKILL.md`, or NOVUM 3 artifact is authorized by EXP-002A.
