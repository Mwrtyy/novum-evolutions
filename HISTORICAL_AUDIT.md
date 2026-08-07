# Historical audit — NOVUM Innovation and NOVUM Innovation Lab

This audit was produced from the supplied NOVUM 2.0.0 skill archive and the complete historical lab archive (455 top-level lab files plus nested packages/results). It treats history as evidence, not as a specification for the new lab.

## Accepted baseline

The accepted version is NOVUM Innovation `2.0.0`.

- archive SHA-256: `e38cd4e62439c5759bf99bf2fc72e165abf2876f75396c170f445d6a3c529dda`
- accepted stage in historical state: `1.3`
- package: 21 files
- `SKILL.md`: 339 lines, historical heuristic ≈3,676 tokens
- current re-validation: package validator PASS; deterministic self-tests PASS

The baseline already contains strong ideas: strongest-baseline framing, mechanism signatures, prior-art search, red-team roles, falsification, rejected-idea memory, candidate scoring, and archive/manifest validation. Its major weakness is not absence of methodology; it is that much of the methodology is self-declared and therefore easy to satisfy ceremonially.

## What Candidate.1 taught

`2.1.0-candidate.1` implemented an Evidence-Bearing Tournament to bind baseline delta, causal links, evidence status, simpler substitutes, and discriminating tests.

It was correctly **rejected before full behavioral expense**. A hostile verifier showed the selected survivor could explicitly lose to its simpler substitute and still pass. Additional deterministic failures included scorer-contract mismatch, prose-only threshold checks, incorrect unused-evidence accounting, Unicode causal-token collapse, and ZIP mode drift.

Lesson: adding a stronger contract can create more surface area without guaranteeing the contract actually enforces the intended behavior. Structural machinery must itself be attacked before it is trusted.

## What Candidate.2 taught

Candidate.2 repaired Candidate.1's structural bypasses and completed the frozen six-task behavioral campaign.

Observed results:

- weighted score: `7.9703 → 8.0430`
- relative weighted gain: **+0.91%**
- 95% relative interval: **−0.67% to +2.34%**
- blind preferences: candidate 33, baseline 15, tie 6
- novelty delta: **−0.246**
- feasibility delta: `+0.324`
- usefulness delta: `+0.219`
- constraint satisfaction delta: `+0.248`
- waterless-cooling task delta: **−0.104**
- independent replication: not demonstrated; generators/judges remained within the same inherited model family

It was **not promoted**. The system became somewhat more conservative, feasible, and constraint-aware, but did not demonstrate material overall capability gain and regressed novelty.

Lesson: structural rigor can improve caution while reducing invention quality. The lab must measure the actual behavioral trade, not reward the stricter method.

## What Candidate.3 taught

Candidate.3 introduced a causal-collision firewall with typed causal roles, path matching, simpler-substitute checks, and core-node ablations.

It successfully repaired three targeted attacks:

1. lexical label gaming: baseline PASS false-negative; Candidate.3 fail-closed, similarity 1.0;
2. causal-role synonym renaming: pre-hardening PASS; hardened candidate rejects unsupported kinds;
3. pass-through node padding: pre-hardening PASS; hardened candidate detects high structural/path similarity.

A valid diverse portfolio still passed.

But the historical record explicitly says:

- full frozen behavioral benchmark: **NOT RUN**
- independent evaluation: **NOT DEMONSTRATED**
- promotion: **NOT AUTHORIZED**

Its own known limit is decisive: causal roles/graphs remain self-declared and can be fabricated or misassigned.

Lesson: Candidate.3 is useful failure-reproduction machinery, not evidence that more causal metadata improves invention capability.

## Benchmark and evaluation lessons

Historical strengths:

- exact accepted-baseline hashing and rollback identity;
- frozen evaluation protocol and immutable task weights;
- deterministic blinding;
- coverage validation;
- evaluator-role separation;
- critical flags and no-imputation rule;
- cluster-bootstrap uncertainty;
- explicit independence limitation;
- hostile tests against evidence substitution and protocol tampering.

Historical weaknesses:

- the frozen six tasks were visible and therefore unsuitable as a final unseen exam;
- package evals overlapped several frozen tasks;
- candidate development could learn the benchmark family too directly;
- same-model-family evaluation limited external independence;
- the old lab invested heavily in schemas, governance, and integrity before proving corresponding behavioral gains;
- one current archival startup path (`NOVUM/harness/test_harness.py`) fails against the supplied snapshot because `state-manifest.json` expects a different Candidate.1 `MANIFEST.json` hash, while `test_github_canonical_state.py` passes and explicitly treats that historical state manifest as a separate snapshot rather than GitHub byte authority.

The last point is preserved, not repaired: historical bytes should not be silently rewritten to make an old snapshot look cleaner.

## Dominant behavioral risks carried forward

1. **Portfolio breadth can crowd out depth.** The accepted skill asks for 8–14 Standard candidates plus substantial research/red-team work.
2. **Self-scoring can create false precision.** Candidate quality inputs may be model-authored before evidence is strong enough.
3. **Mechanism diversity can be simulated.** Candidate.3 proves this for signatures and reduces several attacks, but semantic equivalence remains a judge problem.
4. **Simpler substitutes are easy to underweight.** Candidate.1's central bypass is a direct warning.
5. **Causal explanations can be self-authored fiction.** A causal graph is not evidence unless interventions/ablations discriminate it.
6. **Visible benchmarks invite Goodhart effects.** They are regression tests, not promotion proof.
7. **Rigor can trade away novelty.** Candidate.2 is direct evidence.

## What the new lab should not rediscover

Do not spend another cycle proving that:

- lexical signature labels can be gamed;
- a validator can pass while its semantics fail;
- stricter evidence packet structure automatically improves invention behavior;
- the existing six tasks are hidden;
- same-model evaluation is independent;
- Candidate.3 is already a behavioral winner.

## Highest-value next uncertainty

The strongest untested architecture-level hypothesis is whether the accepted skill's breadth target itself is causing shallow exploration. The first new experiment therefore isolates **portfolio compression** before adding new causal schemas or roles.
