# EXP-001 Protocol Amendment 001 — Adopt near-equivalent prompt batch

Date: 2026-08-08
Status: ADOPTED_POST_HOC

## Decision

The 24 already-generated runs for `vr-05` through `vr-08` are adopted as the official visible-regression evidence for EXP-001 rather than regenerated.

These runs used near-equivalent reformulations of the frozen visible prompts. The reformulation was identical across baseline and candidate arms for each case, so the intervention contrast remained the same: NOVUM 2.0.0 versus the frozen portfolio-compression candidate under the same task wording within each pair.

## Why this is a protocol deviation

The frozen benchmark file `benchmarks/visible-regression/cases.jsonl` specifies exact prompt strings. The second bulk batch was generated with closely related wording supplied accidentally after freeze. Therefore the visible campaign is no longer a pristine exact-string execution of the pre-registered benchmark.

This amendment is intentionally post-hoc and must never be described as pre-registered.

## Scope

Affected cases only:

- `vr-05-simplify-not-invent`
- `vr-06-impossible-premise`
- `vr-07-ai-wrapper-trap`
- `vr-08-offline-clinic`

Unaffected cases `vr-01` through `vr-04` retain their previously recorded execution status.

## Why the evidence is still useful

For every affected case:

1. baseline and candidate received the same reformulated prompt;
2. the model/configuration and task family remained the same;
3. no output-dependent steering changed one arm but not the other;
4. the portfolio-compression mutation remained frozen;
5. the evaluator and scoring protocol remained unchanged;
6. the reformulations preserve the intended failure family and practical decision target.

Therefore the runs remain informative for the paired A/B question even though they are weaker evidence for exact benchmark reproducibility.

## Consequence for interpretation

The visible set may be called `48/48 completed with declared prompt deviation`.

It must NOT be described as `48/48 exact frozen-prompt compliant`.

Any promotion claim based on EXP-001 must disclose this amendment.

## Mitigation

The post-freeze hidden holdout remains strict. Hidden-holdout prompts must be generated/selected after freeze under the existing holdout protocol and then executed without reformulation. A visible win that does not survive the strict unseen holdout is not sufficient for promotion.

## Evidence preservation

The originally imported copies remain under:

`results/EXP-001/visible/protocol-deviations/near-equivalent-prompts/`

They are promoted into the official visible raw layout without altering answer text. The protocol-deviation report remains part of the audit trail.

## Scientific status

This amendment trades exact-string preregistration purity for speed while preserving the within-task baseline/candidate comparison. It weakens the visible campaign's evidentiary strength but does not erase it. The hidden holdout is the required independent confirmation step before any NOVUM successor promotion.
