# EXP-001 mutation plan

Status: pre-result implementation plan. This document does not contain behavioral results.

## Verified parent

- Accepted artifact: NOVUM Innovation 2.0.0
- Source repository: `Mwrtyy/novum-innovation-lab`
- Source commit: `e591937931d2a04f2b308e23f2edca488bea9fcd`
- Source path: `NOVUM/accepted/novum-innovation-v2.0.0.zip`
- Git blob SHA: `66c87b983d126d0c1a21bae17e83b6a30a17a770`
- Archive SHA-256: `e38cd4e62439c5759bf99bf2fc72e165abf2876f75396c170f445d6a3c529dda`
- Archive bytes: `44090`
- Accepted version metadata: `2.0.0`
- Baseline `SKILL.md` SHA-256: `1d6dea7cdb5343aad114ad48fa9f010ea88bd8bf1ccb6c45059f88e1bfa4c4a6`

The experiment-local `baseline-SKILL.md` is an exact copy extracted from that verified archive. Historical baseline bytes remain untouched.

## Minimum mutation surface

Package-wide search found one clause that directly encodes the Standard-mode breadth target:

1. `SKILL.md` depth-controller table: `Standard | 8–14 | ...`
   - Required change: replace `8–14` with `exactly 4`.
   - Reason: this is the independent variable registered by EXP-001.

One adjacent sentence is added immediately after the mode table:

- stop Standard initial portfolio generation at four mechanically distinct candidates;
- spend the released candidate-generation/research budget deepening those four through NOVUM 2.0 mechanisms that already exist;
- prohibit new mechanisms or a larger total run budget.

This sentence is necessary because candidate-count compression without the registered depth reallocation would test a different intervention.

## Intentionally unchanged

The mutation does **not** alter:

- Sprint or Deep candidate targets;
- the two-wave portfolio-generation method;
- mechanism-signature diversity rules;
- frontier mapping or research-source rules;
- anti-fake-novelty logic;
- prior-art search representations;
- red-team attacks or actions;
- simpler-substitute logic;
- evolution moves or lineage rules;
- scoring timing, dimensions, or selection rules;
- causal/falsification requirements;
- output contract or completion gate;
- schemas, scripts, validators, references, assets, or evaluator rules.

## Expected behavioral consequence

Standard mode produces exactly four initial candidates instead of 8–14 and allocates the saved breadth effort to deeper use of existing evaluation/deepening steps on those four. No claim is made that this improves quality.

## Minimality decision

A deletion test was applied to every proposed change. The final overlay changes one package file and one conceptual variable. Removing either the numeric replacement or the reallocation sentence would no longer implement the pre-registered EXP-001 intervention; changing anything else was unnecessary and therefore rejected.
