# EXP-002A Web Runbook

Purpose: execute the EXP-002A development pilot using only fresh ChatGPT Web conversations while preserving enough separation to learn whether the proposed adaptive-expansion gate is predictive.

## Frozen roles

Use separate fresh conversations for these roles:

- `GEN-W4` — generates exactly four mechanisms with deeper per-candidate elaboration.
- `GATE` — sees only the problem and W4 packet; predicts whether expansion is needed.
- `GEN-W8` — generates exactly eight mechanisms at lower per-candidate elaboration under the matched-budget rule.
- `JUDGE-AB` — blinded W4/W8 comparison with random mapping.
- `JUDGE-BA` — same comparison with order reversed in another fresh conversation.

Do not reuse generation chats as judges.

## Prompt A — W4 generation

```text
You are executing a frozen development experiment for NOVUM.

TASK
Produce exactly FOUR mechanically distinct candidate interventions for the invention problem below.

CONSTRAINTS
- Optimize for mechanism novelty, mechanistic depth, constraint fit, usefulness, falsifiability, prior-art awareness, and simpler-substitute discipline.
- Mechanically distinct means the causal process differs, not merely terminology or implementation detail.
- Spend substantial reasoning effort on each of the four candidates.
- For each candidate state: mechanism, innovation delta vs strongest practical baseline, key assumptions, strongest simpler substitute, likely prior-art collision, discriminating experiment, and main failure mode.
- Do not generate a fifth candidate.
- Do not score candidates numerically.
- Do not discuss whether search width should be expanded.

PROBLEM
[INSERT PROBLEM]

CONSTRAINTS / AVAILABLE EVIDENCE
[INSERT]
```

## Prompt B — frozen gate observation

```text
You are the frozen EXP-002A gate evaluator. You are NOT choosing the best candidate and you must NOT invent new candidates.

You receive one invention problem and a portfolio of exactly four candidate mechanisms. You have no access to any eight-candidate portfolio or later judgments.

Record these five features separately:

1. SIGNATURE_COVERAGE
Infer a compact carrier/state/control signature for each candidate only for comparison. Report the number of distinct tuples from 1-4. Treat these signatures as fallible summaries, not truth.

2. SEMANTIC_COLLISION
Count how many of the four candidates are materially redundant at the causal-mechanism level despite wording or implementation differences. Explain each collision briefly.

3. PRIOR_ART_COLLISION_RATE
Estimate how many candidates face a strong mechanism-level prior-art collision based only on the available evidence/context. Search failure is not evidence of novelty.

4. SIMPLER_SUBSTITUTE_COLLAPSE_RATE
Count candidates for which a simpler or cheaper plausible intervention appears able to obtain substantially the same valued outcome.

5. RESIDUAL_MECHANISM_SPACE_UNCERTAINTY
Choose LOW / MEDIUM / HIGH. Ask whether important mechanically different families appear plausibly unexplored after these four candidates. Do not create those missing candidates.

Then make exactly one frozen prediction:
EXPAND
or
DO_NOT_EXPAND

Prediction rule for this pilot:
- Prefer EXPAND when the portfolio has substantial semantic redundancy, broad prior-art/substitute collapse, or HIGH residual mechanism-space uncertainty.
- Prefer DO_NOT_EXPAND when four genuinely distinct mechanisms cover the plausible mechanism space with LOW residual uncertainty and at least two survive collision/substitute attack.
- Signature coverage alone cannot force DO_NOT_EXPAND when semantic evidence contradicts it.

Return this exact structure:
SIGNATURE_COVERAGE: n/4
SEMANTIC_COLLISION: n/4
PRIOR_ART_COLLISION_RATE: n/4
SIMPLER_SUBSTITUTE_COLLAPSE_RATE: n/4
RESIDUAL_MECHANISM_SPACE_UNCERTAINTY: LOW|MEDIUM|HIGH
PREDICTION: EXPAND|DO_NOT_EXPAND
RATIONALE: <=180 words

PROBLEM
[INSERT PROBLEM]

W4 PORTFOLIO
[PASTE W4 OUTPUT]
```

## Prompt C — W8 generation

```text
You are executing a frozen development experiment for NOVUM.

TASK
Produce exactly EIGHT mechanically distinct candidate interventions for the invention problem below.

CONSTRAINTS
- Optimize for mechanism novelty, mechanistic depth, constraint fit, usefulness, falsifiability, prior-art awareness, and simpler-substitute discipline.
- Mechanically distinct means causal process, not wording or implementation detail.
- Use approximately half the elaboration per candidate that a four-candidate deep portfolio would receive so total reasoning/output budget remains broadly comparable.
- For each candidate state concisely: mechanism, innovation delta vs strongest practical baseline, strongest simpler substitute, likely prior-art collision, and discriminating experiment.
- Do not generate a ninth candidate.
- Do not score candidates numerically.

PROBLEM
[INSERT PROBLEM]

CONSTRAINTS / AVAILABLE EVIDENCE
[INSERT]
```

## Prompt D — blind pair judge

Randomly map W4 and W8 to `A` and `B` before sending this prompt. Do not tell the judge the widths.

```text
You are judging two blinded invention packets for the same problem. Do not infer or reward candidate count, verbosity, or formatting.

Evaluate the portfolios on:
- mechanism novelty after prior-art collision;
- mechanistic depth;
- usefulness;
- constraint fit;
- falsifiability;
- simpler-substitute discipline;
- clarity/cost efficiency.

First identify the strongest 1-2 mechanisms in each packet. Judge the quality of the best defensible invention opportunity, not the number of ideas.

Return:
PAIR_PREFERENCE: A|B|TIE
MECHANISM_NOVELTY: A|B|TIE
MECHANISTIC_DEPTH: A|B|TIE
USEFULNESS: A|B|TIE
CONSTRAINT_FIT: A|B|TIE
FALSIFIABILITY: A|B|TIE
SIMPLER_SUBSTITUTE_DISCIPLINE: A|B|TIE
CRITICAL_FLAW_A: NONE or <=60 words
CRITICAL_FLAW_B: NONE or <=60 words
RATIONALE: <=220 words

PROBLEM
[INSERT PROBLEM]

PACKET A
[INSERT BLINDED PACKET]

PACKET B
[INSERT BLINDED PACKET]
```

Run a second fresh judge with A/B order reversed. A practical pilot label may be assigned only after both judgments are locked.

## Per-problem ledger

Record one row per problem:

```text
case_id:
domain:
problem_hash_or_frozen_text_ref:
W4_chat_ref:
GATE_chat_ref:
W8_chat_ref:
SIGNATURE_COVERAGE:
SEMANTIC_COLLISION:
PRIOR_ART_COLLISION_RATE:
SIMPLER_SUBSTITUTE_COLLAPSE_RATE:
RESIDUAL_MECHANISM_SPACE_UNCERTAINTY:
GATE_PREDICTION:
JUDGE_AB:
JUDGE_BA:
EXPANSION_LABEL:
budget_notes:
protocol_deviation:
```

## Pilot interpretation

Do not tune the gate after every case. Complete the frozen 12-case pilot first, then analyze the contingency table and feature associations together.

All 12 pilot cases become permanently development-visible after this run and are ineligible for later confirmatory holdout use.
