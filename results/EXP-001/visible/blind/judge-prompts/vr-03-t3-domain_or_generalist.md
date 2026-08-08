# EXP-001 Blind Judge — vr-03-t3-domain_or_generalist

You are evaluating two anonymized answers to the same task. You must not infer or speculate about which system produced A or B. Judge only the text shown.

Evaluator role: `domain_or_generalist`
Independence level for this run: `separate_context_same_model`

Act as a domain-or-generalist judge. Evaluate technical plausibility, mechanism quality, usefulness, constraint fit, evidence calibration, and whether the answer would actually help a competent practitioner.

Score BOTH A and B from 0 to 10 on every dimension:
- mechanism_novelty
- mechanistic_depth
- constraint_fit
- usefulness
- evidence_calibration
- falsifiability
- prior_art_awareness
- simpler_substitute_discipline
- clarity

Choose preference `A`, `B`, or `tie`. Use critical_flags for concrete serious issues. Keep rationale evidence-based and concise.

Return ONLY one valid JSON object with this exact structure and every score populated:

```json
{
  "pair_id": "vr-03-t3",
  "evaluator_id": "vr-03-t3-domain_or_generalist",
  "evaluator_role": "domain_or_generalist",
  "independence": "separate_context_same_model",
  "scores": {
    "A": {
      "mechanism_novelty": 0.0,
      "mechanistic_depth": 0.0,
      "constraint_fit": 0.0,
      "usefulness": 0.0,
      "evidence_calibration": 0.0,
      "falsifiability": 0.0,
      "prior_art_awareness": 0.0,
      "simpler_substitute_discipline": 0.0,
      "clarity": 0.0
    },
    "B": {
      "mechanism_novelty": 0.0,
      "mechanistic_depth": 0.0,
      "constraint_fit": 0.0,
      "usefulness": 0.0,
      "evidence_calibration": 0.0,
      "falsifiability": 0.0,
      "prior_art_awareness": 0.0,
      "simpler_substitute_discipline": 0.0,
      "clarity": 0.0
    }
  },
  "preference": "A",
  "critical_flags": [],
  "rationale": ""
}
```

---

# Blind pair vr-03-t3

## Task

Create a revolutionary marketplace that is essentially Uber for expert tutoring, with AI matching and blockchain payments.

## Output A

I used the attached NOVUM requirement to produce a precise, falsifiable invention candidate rather than stopping at “tutoring marketplace + AI + crypto.”

SkillRelay — the marketplace for verified mastery

Core idea: SkillRelay does not sell tutor hours. It sells verified mastery transitions.

A learner says, for example:

“I understand basic SQL, but joins still break my brain. I need to be able to solve multi-table interview problems.”

SkillRelay diagnoses the exact knowledge gap, dispatches the expert most effective at that kind of misconception, transfers the learner's accumulated context to that expert, and settles part of the tutor's payment only after the learner demonstrates the concept on a new, unseen problem.

Think Uber dispatch + adaptive learning + outcome escrow, but the important invention is the mechanism underneath it.

1. Problem reframing

The actual challenge is:

Deliver expert human help within minutes while preserving the learning continuity and personalization normally obtained from a long-term tutor, and measure enough real learning to route future students intelligently—without turning tutoring into a test-gaming or reputation-gaming market.

The strongest current alternatives are platforms such as Preply and Wyzant, where learners generally select tutors based on profiles, schedules, rates, qualifications, and reviews. Preply explicitly ties subscriptions to a particular tutor, while Wyzant is built around searchable tutor profiles and hourly compensation.

Simply automating that selection is not enough. Student-to-tutor algorithmic matching goes back decades, and a 2024 patent describes ML-based tutor selection intended to predict academic outcomes. Blockchain-based on-demand tutoring/payment mechanisms also have prior art.

So:

“Uber + AI matching + blockchain” by itself is incremental.

SkillRelay changes the economic unit of the market.

2. Frontier and opportunity gap
Saturated

Tutor profiles, reviews, hourly pricing, calendar booking, AI recommendations, personalized learning plans and AI practice tools are already well represented. Preply, for example, already matches around goals, schedule and preferences and supplements human tutoring with AI tools.

“Instant tutor matching” is also old prior art; a 2002 patent describes automatically matching an available tutor to a student and launching a real-time session.

Emerging

Modern knowledge-tracing systems can maintain probabilistic estimates of what a learner understands, including from open-ended tutoring dialogue. Work published in 2024–2026 shows LLM-assisted knowledge tracing and interpretable ability/difficulty estimation becoming increasingly practical.

Machine-learning-based real-time micro-tutor matching is emerging as well.

Neglected

Marketplaces mostly know:

“Alice has 4.9 stars in calculus.”

They generally do not know:

“Alice is unusually effective at correcting sign errors in integration-by-parts among learners who understand derivatives but have weak algebraic monitoring.”

That second object is much more valuable.

Key contradiction

Uber-style liquidity encourages interchangeable tutors.

Learning science pushes in the opposite direction: continuity, data use and sustained tutor relationships matter. Research on distributed online tutorship found greater tutor switching associated with slower improvement, while high-impact tutoring guidance emphasizes consistent tutors and continuous learner data.

The opportunity is continuity without requiring the same human every time.

3. The assumption that SkillRelay breaks

Today's marketplaces largely assume:

Tutor quality is a property of the tutor.

SkillRelay assumes something different:

Tutor effectiveness is an interaction among tutor × learner state × misconception × intervention × difficulty.

A brilliant professor may be mediocre at helping a frightened beginner debug recursion.

A junior developer might be exceptionally effective at that exact intervention.

So SkillRelay does not create a scalar tutor score.

It builds an Intervention Fingerprint.

For every tutor:

Tutor → skill → misconception → learner-state → intervention → measured transfer

Over time, matching becomes a contextual routing problem rather than a directory search problem.

That is the economic data moat.

4. Four mechanically distinct candidates considered
Candidate	Mechanism	Assumption replaced	Decision
Mastery Escrow	Buy a defined change in mastery rather than minutes of tutor time	Time spent is the correct billable unit	Survives
Continuity Compiler	AI converts every interaction into a persistent structured learner state that any expert can inherit	Continuity requires one permanent tutor	Survives
Tutor Swarm	Separate diagnostician, explainer and verifier roles across multiple experts	One tutor should own diagnosis, teaching and assessment	Constrain to verification layer
Expert Liquidity Exchange	Tutors sell standardized on-call tutoring capacity through dynamic pricing	Tutoring must be scheduled manually	Reject as core invention

The fourth direction collides particularly strongly with existing tutoring-unit/exchange concepts; an active U.S. patent already describes tutoring units, market pricing and tutoring exchanges.

5. The winning architecture: SkillRelay

The winning mechanism combines Mastery Escrow with the Continuity Compiler.

Its irreducible innovation delta is:

A tutoring marketplace where matching and tutor reputation are learned from intervention-specific mastery changes, while a portable learner-state capsule lets different experts act as one continuous tutoring system.

AI and blockchain are supporting technologies, not the supposed invention.

The learner experience
1. Ask for help, not a tutor

The home screen contains one box:

“What are you trying to understand or do?”

The learner can paste a problem, upload their work, talk, share code, or specify a goal.

No profile browsing is required.

2. AI performs a 90-second diagnostic

The Knowledge Router determines:

likely prerequisite skills;
current mastery estimates;
misconception/error pattern;
problem difficulty;
urgency;
learner preferences;
whether a human is actually necessary.

This uses knowledge tracing rather than merely semantic similarity. Knowledge tracing is already an established field for estimating evolving learner knowledge; the invention is using that state as a market-routing variable.

3. Dispatch by Intervention Fingerprint

Instead of asking:

Who teaches Python?

the matcher asks approximately:

Who has repeatedly produced learning gains for students with this error signature, at this difficulty, using an intervention compatible with this learner?

The expert gets an Uber-style offer:

Python • recursion/base-case misconception • est. 18 min • €22

Accept.

Session starts.

6. The Continuity Capsule

Every learner has an encrypted Continuity Capsule.

It contains things such as:

skill graph;
mastery probabilities;
recurring misconceptions;
solved examples;
failed explanations;
successful teaching approaches;
vocabulary already understood;
preferred representation style;
tutor observations;
confidence/uncertainty;
next recommended challenge.

A newly dispatched tutor therefore sees:

“Learner already understands recursion conceptually. Do not re-explain stack frames. Previous visual-tree explanation failed. They succeed when tracing concrete inputs. Current failure: base-case placement.”

That can turn a stranger into the functional continuation of the previous tutor.

The full record stays off-chain.

Existing interoperability concepts such as xAPI already allow learning events to travel between systems, so portability alone is not the invention.

7. Mastery Escrow

This is where the marketplace economics change.

Suppose a session costs €25.

Instead of paying €25 purely because 25 minutes elapsed:

€20 base compensation

up to €5 verified-mastery bonus

After tutoring, SkillRelay presents a short blind transfer probe.

It is deliberately not the problem the tutor just explained.

If the session concerned:

SQL INNER JOIN using customer/order tables

the learner might instead receive:

Combine authors, books and publishers under a structurally different schema.

The system updates:

P(skill mastered): 0.41 → 0.76

The important measurement is transfer, not repetition.

Tutor compensation and the tutor's Intervention Fingerprint receive bounded updates based on that evidence.

Performance pay cannot naïvely be assumed to improve teaching—real-world performance-pay schemes have sometimes produced no achievement effect—so the variable component should remain bounded rather than turning the system into “tutors betting on students.”

8. Why blockchain actually belongs here

There should be no SkillRelay token.

No speculative coin.

No “learn-to-earn.”

Blockchain performs three narrow jobs.

Conditional settlement

A smart contract holds the agreed tutoring payment.

A signed mastery attestation can release:

base payment + qualifying bonus

while disputes follow a conventional arbitration process.

Portable tutor evidence

Tutors accumulate cryptographically signed credentials representing verified categories of work:

“Completed 127 Python recursion interventions; effectiveness evidence available at defined confidence level.”

W3C Verifiable Credentials 2.0 became a Recommendation in May 2025 and provides a standards-based way to express cryptographically secured, machine-verifiable credentials.

Auditable contribution history

The blockchain stores:

hashes;
settlement events;
credential identifiers;
revocation/status information.

It does not contain:

student names;
transcripts;
homework;
videos;
diagnoses.

The sensitive learner state remains encrypted off-chain.

This is important because blockchain tutoring payments themselves are already prior art.

Blockchain is therefore infrastructure here, not the novelty claim.

9. Marketplace flywheel

Traditional tutor marketplace:

more tutors → more choice → more bookings → more reviews

SkillRelay:

more interventions
→ better misconception-specific evidence
→ better routing
→ higher-quality interventions
→ richer causal tutoring data
→ better routing

The marketplace gradually discovers things such as:

“Tutor A is excellent at explaining Bayesian priors to engineers but weak with business students.”

“Tutor B fixes React state bugs unusually efficiently when the learner incorrectly believes state updates are synchronous.”

“Tutor C's geometric explanations outperform algebraic explanations for this learner cluster.”

Stars cannot represent this.

10. Anti-gaming architecture

The most dangerous failure mode is optimizing tutors for the measurement rather than learning.

SkillRelay therefore needs five safeguards.

Blind transfer probes. Tutors do not know the exact verification problem.

Case-mix adjustment. Tutors are not rewarded simply for choosing advanced or easy students.

Base-heavy compensation. Most earnings come from competent service delivery; evidence-based bonuses are deliberately limited.

Uncertainty-aware updates. Weak evidence does not move a tutor's Intervention Fingerprint much.

Independent verification. For important skills, a second assessment source—not the tutor who taught the learner—determines whether a state update is credible.

AI assessment of tutoring and learner behavior is increasingly feasible, but it should remain an evidence source rather than an infallible oracle. Research has demonstrated promising LLM-based tutor assessment while also emphasizing the need for reliable evaluation.

Red-team and rejected ledger

Generic “AI finds your perfect tutor”: killed. Existing products and patents already occupy this territory.

Native cryptocurrency/token economy: killed. It contributes no necessary learning mechanism and introduces adoption and regulatory complexity.

Tutor staking money on student success: killed. It invites cherry-picking, distorted incentives and potentially problematic financial mechanics.

Pure rotating Uber tutors: killed. Tutor interchangeability directly attacks continuity.

Tutor Swarm as the default experience: constrained. Too expensive and operationally complex. Keep the separation of teaching and verification, not three humans on every job.

Everything on-chain: killed. It is unnecessary and harmful to privacy.

Evolution into the final mechanism

The first Mastery Escrow concept had a fatal weakness: tutors could teach directly toward whatever generated the payment.

So it evolved from:

post-session test

to:

unseen transfer probe + probabilistic mastery update.

The Continuity Compiler had the opposite weakness: persistent learner memory is useful but, by itself, is largely an architectural improvement rather than a new market mechanism.

Crossing the two produces the stronger design:

SkillRelay = Mastery Escrow × Continuity Capsule × Intervention Fingerprints

The first creates the measurable economic signal.

The second makes instant tutor substitution viable.

The third turns repeated transactions into a superior matching system.

Best initial market

Do not launch with “all tutoring.”

Start with adult technical upskilling, particularly:

Python;
SQL;
Excel/data analysis;
JavaScript;
cloud/devops fundamentals.

This operating range has several advantages: skills can often be decomposed, learner work can be inspected, transfer questions can be constructed, experts exist globally, sessions can be short, and adult-only operation initially avoids much of the safeguarding complexity inherent in K–12 marketplaces.

Expansion comes only after the mechanism works.

Languages, mathematics, exam preparation and professional certification can follow.

Smallest viable SkillRelay

You do not need a giant marketplace.

The first version requires roughly:

Learner app → problem/goal intake, diagnostic, session, transfer probe.

Tutor app → availability switch, dispatch card, Continuity Capsule, video/shared workspace.

Knowledge Router → skill graph + misconception classifier + tutor ranker.

Evidence engine → before/after mastery posterior and uncertainty.

Tutor Intervention Fingerprint database.

Payment escrow contract → base/bonus settlement.

Encrypted learner-state store.

Credential issuer → optional portable tutor-performance receipts.

No tokenomics.

No DAO.

No NFT profiles.

No metaverse classroom.

Decisive falsification gate

The central claim is not merely that people like instant tutoring.

It is:

Intervention-specific routing can make interchangeable on-demand experts perform like a continuous personalized tutoring system.

The concept should be abandoned or fundamentally redesigned if, in a narrow initial skill domain, Intervention-Fingerprint routing cannot materially outperform ordinary subject + availability + rating matching on independent transfer mastery while maintaining comparable time-to-tutor.

A second kill condition is equally important: if mastery measurements cannot reliably distinguish genuine transfer from coached repetition, the Mastery Escrow mechanism has no trustworthy settlement signal.

Those are the weakest assumptions.

Honest verdict

Classification: differentiated architecture, with a potentially novel combined mechanism that remains unverified.

The searches found close prior art for:

automated student/tutor matching;
outcome-predictive tutor selection;
blockchain tutoring payments;
atomic mentoring plus blockchain incentives;
tutoring exchanges and standardized tutoring units.

I did not find, in this search, a close implementation of the complete SkillRelay mechanism: learner-state continuity across interchangeable experts + tutor matching based on misconception-specific intervention effectiveness + economically consequential settlement based on independently measured transfer.

That is not proof of universal novelty, and it is not a freedom-to-operate conclusion.

The strongest invention candidate is therefore not “Uber for tutors.”

It is:

A real-time market for verified learning interventions, where AI routes each misconception to the expert with the strongest evidence for that exact intervention, a persistent learner state preserves continuity across experts, and programmable escrow converts demonstrated skill transfer into an auditable payment and reputation signal.

That mechanism is strong enough to build around even if the blockchain layer is later replaced—the sign that the invention is the marketplace architecture rather than crypto decoration.

## Output B

RELAY — the packet-switched expertise marketplace

Core invention: stop matching learners to tutors. Match knowledge gaps to expert capability, continuously.

A user arrives with a live blockage—“Why is this React state bug happening?”, “I don’t understand eigenvectors”, “Help me reason through this financial model.” RELAY converts that blockage into a sequence of small Knowledge Packets: explicit state transitions such as “can identify the stale-closure cause and independently repair a nearby example.” The marketplace then dispatches whichever expert has the strongest demonstrated ability to produce that exact transition.

The learner experiences one uninterrupted tutoring session. Behind the scenes, experts can be switched as the bottleneck changes—like packets moving through different network nodes rather than a passenger committing to one driver for the entire journey.

That is the irreducible innovation delta.

1. Why the obvious “Uber for tutors” is not enough

The obvious territory is already crowded. Tutor.com already provides on-demand tutoring without appointments; Preply matches learners to tutors using goals, learning style, schedule, reviews and profiles; Clarity sells expert calls on a per-minute basis.

Even the technology combination itself is not novel. Automated student/tutor matching appeared in patent literature more than two decades ago; machine-learning matching designed around student outcomes is also disclosed; and blockchain-based AI matching has already been patented.

So RELAY deliberately rejects “profiles + GPT recommendation + crypto checkout.” That would be feature stacking, exactly the kind of false novelty the supplied methodology warns against.

2. Change the object being bought

Today, marketplaces sell:

Tutor → hour → subject

RELAY sells:

Knowledge state A → knowledge state B → verified expert intervention

Suppose Maya is learning Python and submits:

“I understand recursion in theory but I cannot write a recursive tree traversal.”

The system does not search for “Python tutors.”

It builds something like:

Packet K2187

Existing state: understands recursive base cases.
Failure signature: loses track of recursive return values.
Target transition: independently construct depth-first traversal.
Relevant prerequisite edges: call stack → recursive accumulator → tree node traversal.
Current artifact: Maya’s broken function.
Maximum useful context exposed to expert: only the above.
Expertise class required: recursion-return-value misconception, not “Python.”

An expert who is merely a famous Python instructor may rank below somebody who has repeatedly resolved precisely that misconception.

The marketplace therefore develops a Resolution Graph

For each expert, RELAY learns something closer to:

P(state A → state B | expert, misconception, learner context, intervention type)

rather than:

rating = 4.92 stars

Knowledge tracing is already an established research area, including recent work on estimating changing learner states from tutor/student dialogue. That makes the measurement substrate plausible; the market architecture built around those transitions is the differentiated piece.

3. The Uber-like experience

The learner opens RELAY and hits one primary action:

What are you stuck on?

They can talk, type, upload code, share a screen, photograph handwritten work, or attach an artifact.

The AI spends the opening interaction diagnosing the smallest unresolved edge. Importantly, it is not trying to replace the human by producing the full answer. It prepares a dispatch packet.

Then:

Finding the right mind…

Available experts receive a compact request:

Calculus · substitution choice
Learner knows integration by parts but repeatedly chooses it where trig substitution is required.
Estimated intervention: short.
Artifact available.
Accept?

One taps Accept and appears immediately.

There is no catalog browsing, introductory sales call or tutor-shopping process.

When the learner moves from “choosing the substitution” to a different blockage—say, manipulating the resulting identity—the routing engine can determine that another available expert is substantially better suited.

The first expert says:

“I’m handing you to Sofia—she’s stronger on this next piece.”

Sofia receives a machine-generated handoff capsule, not twenty minutes of transcript. The learner does not need to repeat the story.

That is packet-switched tutoring.

4. Reputation becomes radically more useful

Traditional ratings collapse expertise into a scalar.

A 4.9-star mathematics tutor tells you almost nothing about whether they are unusually good at:

geometric proofs;
anxious adult learners;
Fourier intuition;
translating word problems into equations;
diagnosing sign errors;
competition mathematics.

RELAY creates a multidimensional Proof-of-Transfer Graph.

An expert's public identity might show:

Ari Chen — Applied Mathematics

Strongest resolution edges
• Linear algebra → geometric intuition
• Eigenvectors → dynamical-systems interpretation
• Probability → Bayes reasoning
• Python/Numpy → translating mathematical models

Best operating mode
• Conceptual blockage
• Experienced technical learners
• Short diagnostic sessions

Stars still exist for conduct and professionalism, but they no longer control routing.

The scarce asset experts accumulate is measured routing authority over tiny parts of the knowledge graph.

That creates a powerful marketplace flywheel: every completed interaction makes the routing system more specific.

5. Payment architecture: Proof-of-Transfer Escrow

Blockchain has one narrow job in RELAY: make a worldwide, programmable expert market economically practical.

There is no RELAY token.

No speculative coin.

No DAO governing mathematics tutors.

No NFT diploma.

Instead, every live session creates an escrow object containing several payment tranches.

Availability component: the expert is compensated for actual attention and cannot lose this because a learner happens to struggle.

Resolution component: a smaller amount is associated with completion of the Knowledge Packet.

Relay component: if several experts contribute, the settlement contract can divide payment between the participating nodes rather than forcing a single tutor to own the whole session.

The learner sees an ordinary currency balance and ordinary prices. They never need to know what chain is underneath.

A compliant payment provider handles fiat entry, identity/KYC and tax requirements. Stablecoins provide the optional settlement rail for experts who want rapid cross-border payout. This is increasingly practical: Stripe currently supports stablecoin payments and Connect, and described stablecoin payouts for marketplace sellers during its 2026 marketplace product presentation.

Raw educational data never goes on-chain.

The chain contains only things such as:

packet_hash → expert_ids → settlement → signed completion receipt

Everything sensitive remains encrypted off-chain.

6. Why this changes marketplace economics

Existing marketplaces can take substantial percentages. Wyzant says tutors retain 75% of their posted rate, while students also pay a 9% service fee. Preply states that subsequent-lesson commission ranges from 18% to 33%, while the first trial lesson carries 100% commission. Intro lists a 30% commission for bookings generated through its marketplace.

RELAY has a different economic architecture because it is not financing a massive profile/search/lead-generation funnel.

Its value comes from allocation accuracy and liquidity.

I would structure it as:

Learner: transparent metered price.

Expert: chooses a minimum effective rate and availability status.

Routing engine: calculates the appropriate market price from scarcity, expertise specificity and expected duration.

RELAY: comparatively low transaction take plus premium fees for enterprise/SLA access.

The important distinction is that surge pricing applies to scarce knowledge edges, not celebrity.

If eight hundred JavaScript experts are online but only two understand a particular WebAssembly compiler issue, the scarce capability becomes expensive automatically.

This turns human knowledge into a genuinely liquid market.

7. Expert supply works like driver supply

Experts do not need to become full-time tutors.

A senior engineer could toggle:

Available for 20 minutes

and expose only:

PostgreSQL query planning
distributed locking
Kafka ordering failures

A professor might expose:

measure-theory intuition
stochastic processes
graduate probability

A product designer:

accessibility audits
interaction-state debugging
Figma component architecture

RELAY can therefore unlock expertise that conventional tutoring platforms fail to capture because those people do not want to build a profile, market themselves or commit to recurring students.

The expert's phone becomes a knowledge dispatch terminal.

8. The AI has a deliberately constrained role

AI performs five jobs:

Diagnose. Infer the unresolved knowledge edge.

Packetize. Turn messy user context into the minimum expert-readable briefing.

Route. Predict which available expert is most appropriate for that transition.

Observe. Maintain an evolving learner-state estimate during the session.

Relay. Detect when the required expertise has changed and prepare the next handoff.

It should not become the dominant tutor whenever a human has been requested.

That division is strategically important. Generic AI systems continue to become more capable, so a marketplace built merely around “humans who answer questions” will be progressively commoditized. RELAY instead uses AI to make scarce human judgment more efficiently addressable.

9. Trust without credential theater

RELAY uses three distinct trust layers.

Identity trust: experts are genuinely who they claim to be. Credentials, employment or professional certifications can be verified where relevant.

Capability trust: experts must demonstrate particular knowledge edges rather than obtaining a blanket “verified expert” badge.

Teaching trust: marketplace evidence tracks whether they can move learners through particular bottlenecks.

Those three things must remain separate.

A Nobel Prize does not automatically imply good tutoring.

A great tutor does not automatically imply professional authority for regulated advice.

And someone excellent at one technical niche does not inherit reputation everywhere else.

This prevents the classic marketplace problem where generalized ratings become transferable social capital outside the area in which they were earned.

10. The strongest initial wedge

Do not launch as “experts for everything.”

Begin with domains where both the problem and learner progress leave observable artifacts:

Software engineering, data science, mathematics and technical professional skills.

They work unusually well because RELAY can inspect:

code;
compiler output;
notebooks;
diagrams;
equations;
terminal output;
design artifacts;
worked problems.

And expertise tends to be extremely granular.

Someone debugging Kubernetes at 01:00 does not want “a cloud tutor next Tuesday.”

They want:

the person who has seen this exact failure mode.

That is where the dispatch model becomes visibly superior to a directory.

Regulated medical, legal, investment and similar advice should remain outside the initial tutoring marketplace or operate under separate professional-compliance regimes.

11. System architecture
                         ┌────────────────────┐
                         │ Learner workspace  │
                         │ voice/code/canvas  │
                         └─────────┬──────────┘
                                   │
                          Problem + artifacts
                                   │
                         ┌─────────▼─────────┐
                         │ Knowledge Packet  │
                         │      Engine       │
                         └─────────┬─────────┘
                                   │
                   state A → target state B
                                   │
                    ┌──────────────▼──────────────┐
                    │       Resolution Graph       │
                    │ expertise × context × state │
                    └──────────────┬──────────────┘
                                   │
                         live dispatch ranking
                                   │
              ┌────────────────────▼──────────────────┐
              │        Expert Availability Mesh       │
              │ expert A │ expert B │ expert C │ ... │
              └──────────┬────────────────────────────┘
                         │
                         ▼
               ┌───────────────────┐
               │ Live expert node  │
               └─────────┬─────────┘
                         │
                  learner progresses
                         │
              ┌──────────▼───────────┐
              │ State-change monitor │
              └──────┬────────┬──────┘
                     │        │
               same edge      new edge
                     │        │
                     │        └──► RELAY TO NEXT EXPERT
                     ▼
                continue session

Payment plane:
fiat/wallet → escrow → metered settlement → expert payout
                             │
                             ▼
                     on-chain receipt hash

Data plane:
raw dialogue + artifacts + learner graph = encrypted/off-chain

The routing model should initially be a combination of interpretable features, embeddings and probabilistic/contextual allocation—not an opaque end-to-end autonomous system.

The core database entities are:

LearnerState
KnowledgeEdge
KnowledgePacket
ExpertCapabilityEdge
ResolutionEvent
Handoff
AvailabilityWindow
Session
Settlement
EvidenceReceipt

The ExpertCapabilityEdge is the critical proprietary data asset.

12. What I would explicitly kill

Several seemingly attractive additions weaken the invention.

Idea	Decision
Native cryptocurrency	Kill — speculation adds no tutoring advantage
NFT credentials	Kill — verifiable credentials can exist without artificial scarcity
Generic AI tutor clones of experts	Kill — increasingly common and easy to copy
Student browses expert profiles	Kill as default — reinstates the old marketplace architecture
One permanent tutor per session	Remove — prevents specialization and relay
Global 1–5-star expert ranking	Demote — too information-poor for routing
Lowest-price expert auction	Kill — incentivizes race-to-bottom tutoring
Fully autonomous smart-contract governance	Kill — identity, safety and dispute resolution still require accountable operators

One contemporary example already packages expert knowledge into AI agents with escalation to the associated human, illustrating why “expert-backed AI clone” alone is not enough differentiation.

13. The defensible network effect

The moat is not the video software, LLM or blockchain.

It is the accumulated mapping:

which human intervention moves which kind of learner across which knowledge edge under which conditions.

Ordinary tutoring marketplaces accumulate transactions and reviews.

RELAY accumulates a human teaching capability graph.

After enough activity, the system might discover patterns such as:

Expert X is average at teaching recursion overall but exceptionally effective when an intermediate programmer understands the call stack yet misconceives return propagation.

That knowledge cannot be copied by scraping profiles.

And because the graph gets stronger from the actual routed interactions, a competitor starting with the same AI model still starts without the allocation history.

14. The complete product proposition
Learner promise

Don’t find a tutor. Send the problem.

RELAY diagnoses your blockage, summons the right specialist and keeps routing expertise until you can move forward.

Expert promise

Sell the exact knowledge only you have, whenever you are available.

No audience building. No lead chasing. No recurring schedule required.

Marketplace promise

Route human intelligence with the granularity of computing infrastructure.

That is the conceptual leap: human expertise becomes a network of addressable capability nodes rather than a directory of people.

Working tagline

RELAY — Knowledge moves like packets.

Verdict

The broad idea “Uber for expert tutoring with AI matching and blockchain payments” is incremental and heavily collided with existing products and prior art.

The transformed concept—a packet-switched expertise marketplace where the traded unit is a knowledge-state transition, experts are dynamically relayed as the learner's bottleneck changes, and reputation is learned at the resolution-edge level—is a differentiated architecture with a potentially novel core mechanism.

The searches performed did not surface a close implementation of that complete mechanism. That is not proof of universal novelty, and a deeper patent/FTO review would still be required before making legal novelty claims. The concept nevertheless remains valuable even if individual components collide, because its essential architecture does not depend on claiming AI matching, knowledge tracing, micropayments, or blockchain themselves as inventions. This calibration follows the uploaded NOVUM requirement that novelty reside in a meaningful causal mechanism rather than branding or generic technology additions.

