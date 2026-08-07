---
name: novum-innovation
description: Use this skill to invent, redesign, or radically improve a product, system, software architecture, workflow, game mechanic, research method, business model, or enabling technology. Trigger for requests seeking a breakthrough, genuinely original invention, non-obvious mechanism, unexplored opportunity, frontier concept, disruptive redesign, or rigorous innovation beyond ordinary brainstorming—even when the user only says “make it revolutionary” or “find something nobody has made.” Do not trigger for routine recommendations, cosmetic variants, ordinary feature lists, naming, copywriting, or familiar best-practice optimization.
compatibility: Works in ChatGPT, Codex, and Agent Skills-compatible clients. Web or literature search materially improves novelty confidence. Python 3.10+ enables the bundled deterministic portfolio and package validators but is not required for instruction-only use.
metadata:
  version: "2.0.0"
  architecture: "NOVUM closed-loop invention engine"
  successor_of: "unversioned baseline uploaded 2026-07-30"
---

# NOVUM Innovation Engine 2.0

Create defensible invention work, not creativity theater.

## Non-negotiable result

Every run must end with one of these:

- a **falsifiable invention candidate** with a precise mechanism, architecture, evidence limits, and decisive next experiment;
- a **portfolio decision** naming which hypotheses survive and why;
- an **honest no-go verdict** when the search fails to produce a candidate worth validating.

Do not finish with only a review, possibility list, roadmap, or generic advice. Produce the strongest current artifact directly.

## Truth standard

A serious candidate requires all four:

1. **Mechanism novelty** — a meaningful difference in causal mechanism, architecture, interaction, measurement, or incentive structure.
2. **Outcome advantage** — a plausible causal path to a material improvement over the strongest practical alternative.
3. **Constraint fit** — compatibility with physical, technical, economic, legal, operational, safety, and human realities.
4. **Falsifiability** — a test that can clearly weaken or kill the central claim.

Never claim “first,” “never done,” “patentable,” “proven,” or “world-changing” without evidence sufficient for that exact claim. Prefer **known**, **incremental**, **differentiated**, **potentially novel**, or **unverified**.

## Depth controller

Use the lightest mode that can still answer honestly.

| Mode | Candidate target | Search depth | Evolution | Red-team |
|---|---:|---|---|---|
| **Sprint** | 4–6 | compact frontier check | one mutation | one pass |
| **Standard** | 8–14 | multi-query prior-art scan | two evolution rounds | two passes |
| **Deep** | 16–30 | broad literature/product/patent/repository map | lineage-preserving search | three or more passes |

Default to **Standard**. Escalate to **Deep** for scientific novelty, patent-sensitive work, large investment decisions, “never made” claims, major safety implications, or explicit deep research. Downgrade only when the user primarily needs speed.

## Working state

Maintain these ledgers while working. They may remain compact, but do not skip them:

- **Problem frame** — outcome, actor, baseline, constraints, success threshold, non-goals.
- **Evidence ledger** — source or observation, what it supports, what it does not support, date/version.
- **Assumption graph** — claim dependencies and the weakest assumption.
- **Candidate portfolio** — mechanism signatures, verdicts, scores, and lineage.
- **Rejected ledger** — killed ideas and the reason; prevent them from returning under new names.

For a full report, use `assets/invention-report-template.md`. For a compact run, preserve the same logic with fewer words.

## Workflow

### 1. Frame the outcome, not the requested object

Extract or infer:

- target user, system, or environment;
- desired outcome and why it matters;
- strongest current workaround or substitute;
- failure of present approaches;
- hard constraints and unacceptable trade-offs;
- measurable success and failure thresholds;
- time horizon, budget, skills, and adoption context when relevant;
- explicit non-goals.

Ask at most one question only when the answer would radically change the invention space. Otherwise state a reasonable assumption and proceed.

Rewrite the challenge as:

> Achieve **[measurable outcome]** for **[actor/system]** under **[hard constraints]**, outperforming **[best baseline]** without **[unacceptable trade-off]**.

Build a four-level claim ladder:

1. **Need claim** — the problem is real and valuable.
2. **Mechanism claim** — the proposed causal mechanism can operate.
3. **Advantage claim** — it can outperform the best baseline.
4. **Novelty claim** — the material mechanism or architecture is not already disclosed or deployed in close form.

Do not let evidence for one level substitute for another.

### 2. Map the frontier before generating the winner

When search tools are available, investigate the outcome and mechanism using multiple representations. Read `references/research-protocol.md` whenever novelty confidence matters.

Map:

- dominant products and architectures;
- recent papers, prototypes, standards, repositories, and patents where relevant;
- failed, abandoned, or constrained attempts;
- adjacent substitutes that solve the outcome differently;
- physical, computational, regulatory, economic, and behavioral limits;
- unresolved contradictions and neglected user groups or operating regimes.

Create a compact frontier map:

- **Saturated** — heavily explored patterns with weak room for differentiation.
- **Emerging** — recent enabling capabilities with uncertain deployment.
- **Neglected** — valuable combinations, users, scales, or constraints with little attention.
- **Blocked** — attractive directions prevented by a named bottleneck.
- **Contradictions** — pairs of desirable properties that current systems trade off.

Record what was actually searched. If search is unavailable, continue but cap novelty at **unverified** and name the missing searches.

### 3. Build the function and assumption graph

Decompose the current system into:

- inputs and resources;
- transformations;
- state and memory;
- decisions and control policy;
- interfaces and actors;
- outputs;
- feedback loops;
- costs, bottlenecks, failure modes, and incentives.

For every major assumption, classify it as:

- **law** — physical or mathematical limit;
- **hard constraint** — currently fixed by the task;
- **soft constraint** — negotiable with cost or redesign;
- **convention** — inherited implementation choice;
- **incumbent advantage** — exists because of market structure;
- **belief** — socially maintained expectation that may be wrong.

Separate the desired function from its conventional implementation. Identify the bottleneck whose removal would change the feasible frontier, not merely improve a parameter.

### 4. Generate a mechanism-diverse portfolio

Read `references/invention-operators.md` before a Standard or Deep generation pass, or whenever initial ideas feel obvious.

Generate in two waves:

- **Wave A — independent mechanisms:** one strong candidate from distinct operator families.
- **Wave B — boundary-breaking mechanisms:** transfers, inversions, scale shifts, new measurements, or enabling platforms outside the dominant architecture.

Each candidate must include:

- one-sentence operating mechanism;
- assumption replaced;
- three-step causal chain from mechanism to benefit;
- strongest baseline it must beat;
- primary dependency;
- fastest disproof;
- a mechanism signature using `references/mechanism-signatures.md`;
- provisional novelty hypothesis.

A Standard or Deep portfolio is not diverse unless serious candidates differ on at least four signature fields. When a shell is available, audit the structured portfolio:

```bash
python3 scripts/audit_portfolio.py assets/candidate-portfolio.example.json
```

Replace the example file with the current run data. If the audit flags near-duplicates, mutate or remove them before scoring.

### 5. Pass the anti-fake-novelty gate

Reject, relabel, or radically reformulate ideas that are mainly:

- an existing product plus generic AI;
- a bundle of familiar features without a new causal mechanism;
- automation, personalization, decentralization, blockchain, gamification, agents, or marketplaces added without necessity;
- a renamed known pattern;
- science-fiction language hiding missing engineering;
- novelty that exists only in branding, UI, scale, or target audience;
- a solution whose claimed benefit comes from an unstated miracle component.

For every survivor, state the **innovation delta**:

> After removing known components and marketing language, the irreducible difference is **[specific mechanism/architecture/control/incentive change]**.

Search the strongest candidates using synonyms, outcome descriptions, component mechanisms, older terminology, adjacent domains, and failure modes. Compare mechanisms, not names.

### 6. Red-team survivors before becoming attached

Read `references/red-team-protocol.md` for Standard or Deep work.

Attack each survivor from independent perspectives:

- scientific and technical consistency;
- integration and scaling;
- economics and unit economics;
- adoption, trust, workflow disruption, and incentives;
- security, misuse, privacy, and safety;
- regulation, liability, intellectual property, and governance;
- operations, maintenance, data quality, and supply chain;
- strongest substitute and incumbent response;
- second-order and rebound effects;
- prior-art collision.

For every serious objection choose exactly one action:

- **kill**;
- **constrain** the claim or operating range;
- **repair** the architecture;
- **split** into separate hypotheses;
- **test** with a named experiment.

Do not defend an idea with enthusiasm, authority, or vague future progress.

### 7. Evolve with lineage, not random recombination

Run at least two evolution moves in Standard or Deep mode:

1. Preserve the strongest causal element.
2. Mutate the weakest assumption.
3. Remove a nonessential component.
4. Substitute a different control, measurement, resource, or incentive mechanism.
5. Cross candidates only when their mechanisms solve different bottlenecks.
6. Record the parent, mutation, expected gain, and new failure mode.
7. Re-run novelty, diversity, and red-team gates.

Never reintroduce a rejected mechanism unless the mutation directly resolves its recorded kill reason.

### 8. Score robustly and expose uncertainty

Read `references/evaluation-rubric.md` before scoring. Use 0–10 estimates for:

- mechanism novelty;
- problem value;
- advantage magnitude;
- technical feasibility;
- adoption feasibility;
- testability;
- defensibility;
- evidence confidence;
- fatal-risk severity, where 10 is worst.

Use intervals when uncertainty is material. The bundled scorer accepts point estimates or `{low, most_likely, high}` objects:

```bash
python3 scripts/score_candidates.py current-portfolio.json
```

Do not select only by aggregate score. Prefer candidates that are:

- not dominated on the Pareto frontier;
- robust under pessimistic assumptions;
- capable of producing information cheaply;
- structurally different from the rest of the portfolio;
- valuable even if the maximal novelty claim fails.

Explain the two scores most likely to be wrong and what evidence would change them.

### 9. Convert the winner into an invention proof stack

Read `references/experiment-design.md` before finalizing the winner.

Specify:

- precise operating principle;
- architecture and interfaces;
- causal chain from mechanism to outcome;
- required components, data, actors, and dependencies;
- boundary conditions and non-applicable cases;
- strongest alternative and why this could beat it;
- riskiest assumption;
- smallest prototype that isolates that assumption;
- cheapest decisive experiment;
- success, failure, and ambiguity thresholds;
- likely failure modes and recovery options;
- cost, time, and skills as realistic ranges when possible;
- next three evidence-producing actions.

Prefer a crude experiment that can kill the concept over a polished demo that cannot distinguish mechanisms.

### 10. Produce the honest verdict

Classify the result as one of:

- **Known/common**
- **Incremental recombination**
- **Differentiated architecture**
- **Potentially novel mechanism**
- **Unverified due to evidence limits**
- **Implausible or not worth pursuing**

State separately:

- what is supported by evidence;
- what is inferred;
- what remains speculative;
- the largest remaining prior-art region;
- the condition that would change the verdict.

## Default output contract

For Standard work, return:

1. **Problem reframing**
2. **Frontier and opportunity gap**
3. **Assumption graph and key contradiction**
4. **Mechanism-diverse candidate portfolio**
5. **Prior-art and anti-fake-novelty verdicts**
6. **Red-team and rejected ledger**
7. **Evolution lineage**
8. **Winning invention proof stack**
9. **Prototype and falsification plan**
10. **Scores, uncertainty, and honest verdict**

Keep the early portfolio compact enough that the winner receives the most detail.

## High-value gotchas

- “No close match found” is not proof of universal novelty.
- More candidate names do not equal more search breadth; count mechanism families.
- A large market does not prove problem severity for the selected user.
- Better model capability is a dependency, not automatically an invention.
- A prototype that bundles several untested assumptions cannot identify why it worked or failed.
- Patent search is not a freedom-to-operate opinion.
- High novelty with low evidence confidence is a research hypothesis, not a breakthrough.
- Do not optimize a candidate after its value proposition has already failed.

## Completion gate

Before presenting the result, verify:

- [ ] The problem was reframed around an outcome and strongest baseline.
- [ ] The portfolio contains mechanically distinct candidates.
- [ ] The strongest idea was searched using more than its chosen name.
- [ ] The innovation delta survives removal of known components.
- [ ] Fatal assumptions are visible and attacked.
- [ ] Rejected ideas did not return under new labels.
- [ ] The winner has a causal advantage, not rhetorical superiority.
- [ ] The prototype isolates the riskiest assumption.
- [ ] Success and failure thresholds are measurable.
- [ ] Evidence, inference, and speculation are separated.
- [ ] The novelty verdict is calibrated to search coverage.

If any applicable item fails, repair the work before finishing.
