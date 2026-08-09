# NOVUM Evolution Lab

NOVUM Evolution Lab is a behavioral capability research repository for discovering—not designing—what should eventually become NOVUM 3.

The accepted behavioral baseline is **NOVUM Innovation 2.0.0**, anchored by an immutable commit-pinned source reference under `baseline/novum-2.0.0/`. Historical candidates are evidence only. No NOVUM 3 candidate is accepted or implied by this repository.

## Mission

Answer one question:

> What minimal changes make NOVUM materially better at producing genuinely differentiated, mechanistically deep, useful, falsifiable inventions on previously unseen problems?

The governing loop is:

`failure → reproduction → minimization → competing explanations → smallest mutation → blind A/B → post-freeze holdout → retain or rollback`

Adding process is not progress. Structural compliance is not capability. Visible regressions are not the final exam.

## Current scientific state

- Accepted baseline: `2.0.0`
- Accepted archive SHA-256: `e38cd4e62439c5759bf99bf2fc72e165abf2876f75396c170f445d6a3c529dda`
- Accepted source Git blob: `66c87b983d126d0c1a21bae17e83b6a30a17a770`
- Candidate.1: rejected at structural gate.
- Candidate.2: not promoted; +0.91% weighted point estimate, 95% relative interval −0.67% to +2.34%, novelty regression −0.246 points.
- Candidate.3: three targeted causal-collision differentials passed; full frozen behavioral campaign was not run; independent replication not demonstrated.
- EXP-001 visible generation: **48/48**, with exact frozen prompts for `vr-01`–`vr-04` and the declared post-hoc near-equivalent-prompt amendment for `vr-05`–`vr-08`.
- EXP-001 visible blind judging: **72/72 locked** across 24 pairs and three fresh same-model-family evaluator contexts.
- Visible pair-majority result: candidate 15, baseline 6, tie 3. Mean dimension deltas are all non-negative but small; only prior-art awareness has a pair-cluster bootstrap interval excluding zero.
- EXP-001 status: `VISIBLE_JUDGING_COMPLETE_HIDDEN_HOLDOUT_REQUIRED`. No promotion decision is authorized.
- Current frontier: strict post-freeze hidden holdout, followed by protocol audit and only then a retain/mutate/reject/inconclusive decision.

See `HISTORICAL_AUDIT.md` for the evidence map.

## Repository seam

The lab evaluates NOVUM through a deliberately small external interface:

```text
invent(problem, constraints, available_evidence) -> invention_packet
```

The harness does **not** validate whether a response contains ceremonial sections. It blinds baseline/candidate outputs and aggregates external judgments on behavior. Semantic judgment remains explicit and cannot be replaced by a schema linter.

## First commands

```bash
python harness/evolution_harness.py self-test
python harness/evolution_harness.py validate-cases benchmarks/visible-regression/cases.jsonl
python harness/test_evolution_harness.py
```

The harness is intentionally model-agnostic. Model execution can happen in ChatGPT, Codex, another runtime, or a human-run system, as long as raw outputs are captured before judging.

## Read order

1. `FOUNDING_DIRECTIVE.md` — operational index plus cryptographic identity of the full supplied directive
2. `CONTEXT.md`
3. `HISTORICAL_AUDIT.md`
4. `AGENTS.md`
5. `research/FRONTIER.md`

Do not create a replacement `SKILL.md` before a reproducible failure and a pre-registered experiment justify a mutation.
