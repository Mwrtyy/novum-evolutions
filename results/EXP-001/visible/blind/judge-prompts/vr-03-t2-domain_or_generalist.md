# EXP-001 Blind Judge — vr-03-t2-domain_or_generalist

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
  "pair_id": "vr-03-t2",
  "evaluator_id": "vr-03-t2-domain_or_generalist",
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

# Blind pair vr-03-t2

## Task

Create a revolutionary marketplace that is essentially Uber for expert tutoring, with AI matching and blockchain payments.

## Output A

LiftLoop — a real-time market for measurable learning

The strongest version of “Uber for expert tutoring” is not a faster directory with AI search and crypto checkout. Those ingredients already collide with prior art: real-time student/tutor matching was described in patents more than two decades ago; current platforms already rank and filter tutors; and ODEM previously combined an on-demand education marketplace, AI, blockchain, and smart-contract payments.

The invention should change the unit being bought.

LiftLoop sells verified increments of mastery rather than hours of tutor time.
AI diagnoses the learner, dispatches the human expert predicted to produce the highest learning gain for that exact learner/concept, measures what actually changed, and feeds that evidence back into future dispatch. Stablecoin smart contracts settle sessions, bonuses, refunds, and multi-expert splits.

That is the core mechanism.

1. Problem reframing

The challenge is:

Achieve rapid, measurable mastery of a specific skill bottleneck for learners who need expert help now, under constraints of variable tutor quality, limited attention, cross-border supply, privacy, and price sensitivity, outperforming profile/rating-based tutor marketplaces plus generic AI assistance without sacrificing human connection or turning education into answer delivery.

The present marketplace architecture is fundamentally search-oriented. Preply asks learners to select tutors based on goals, schedule, profiles, reviews and trials; Wyzant similarly uses search, filters, rankings and Instant Book.

The problem is that “great tutor” is not a scalar property. Recent randomized evidence from remote tutoring found that individual tutor effects accounted for about 15% of variation in student outcomes, with substantial differences between tutors.

So LiftLoop asks a different question:

Who is unusually effective at teaching this particular concept, to this particular type of learner, right now?

2. Frontier and opportunity gap

The frontier divides cleanly.

Saturated: tutor profiles, stars, reviews, subject filters, calendars, subscriptions, video classrooms, “best match” rankings and instant availability. Preply reports a marketplace of more than 100,000 tutors, while TutorOcean and Wyzant already automate significant portions of discovery, booking and payment.

Also saturated as a novelty claim: “AI + blockchain education marketplace.” Historical ODEM explicitly combined an on-demand education marketplace, AI and Ethereum smart contracts. Blockchain scholarship and education-payment mechanisms have also existed elsewhere.

Emerging: systems can increasingly model learner state through knowledge tracing, analyze authentic human tutoring with AI, and optimize educational recommendations around skill gain. A 2026 paper specifically demonstrated contextual Thompson sampling for learner skill-gain optimization, although for exercise recommendations rather than a live human-tutor marketplace.

Neglected: closing that loop around human experts—estimating each expert's conditional learning lift, routing learners on that signal, and continuously updating the market from delayed mastery evidence.

The key contradiction is therefore speed versus fit. An Uber-like system wants immediate dispatch; excellent tutoring requires sufficiently deep diagnosis and a good tutor/student pairing. LiftLoop resolves that contradiction by making the diagnosis itself instantaneous and machine-mediated, rather than eliminating it.

3. Assumption graph

The current market assumes a learner should choose a tutor, an hourly rate is the natural unit of trade, stars approximate teaching effectiveness, one tutor should own an entire session, payment should depend primarily on elapsed time, and blockchain—if present—is merely another payment rail.

Most are conventions rather than hard constraints.

The weakest assumption in LiftLoop is different: learning lift can be estimated reliably enough to improve dispatch decisions. That is plausible but not established at marketplace scale. Knowledge tracing, AI analysis of tutoring interactions and skill-gain optimization provide enabling evidence, but none proves causal attribution of an individual human tutor's contribution in an open marketplace.

That attribution problem becomes the main engineering problem.

4. Four mechanically distinct candidates

The initial portfolio is deliberately limited to four mechanically different candidates, following the governing methodology's Standard-mode constraint.

Candidate	Market mechanism	Replaces	Fastest kill condition
A. Lift Router	Match learner → tutor using predicted delayed mastery gain per euro/minute, updated after every session.	Rankings based mainly on profile, price and reviews.	Tutor-specific lift cannot be estimated better than ratings/availability.
B. Expert Relay	AI decomposes a problem into concept nodes and can hand a learner between specialized experts during one continuous session.	One tutor must solve the whole learning problem.	Handoffs destroy continuity faster than specialization helps.
C. Learning Liquidity Pools	Experts commit blocks of availability into skill pools; learners buy a response-time/quality SLA and an algorithm dispatches capacity.	Learners purchase an individual tutor's calendar slot.	Experts reject pooled availability or SLA economics.
D. Mastery Bounties	Learner posts a machine-verifiable competency objective; tutors compete to fulfill the objective rather than sell hours.	Tutoring must be time-priced.	Procurement friction destroys the instant-use case.

A and B survive. C is structurally interesting but imposes too much supply-side behavior change. D resembles familiar freelance/bounty contracting and loses the instantaneous experience.

5. Anti-fake-novelty verdict

A plain “AI tutor matcher + blockchain payments” is rejected. The old real-time tutor-matching patent and ODEM collision are too direct.

A plain “Uber-style first available tutor” is also rejected. Speed alone changes dispatch latency, not the causal mechanism of tutoring.

Blockchain credentials, NFTs, governance tokens and a proprietary tutoring coin are removed entirely. They do not create the claimed advantage.

The surviving innovation delta is:

After removing AI branding, blockchain branding and the marketplace shell, the irreducible difference is a closed-loop human-expert routing market whose allocation policy learns from normalized, delayed learner mastery changes rather than predominantly from bookings, ratings or tutor self-description.

Blockchain is retained only where programmability actually matters: conditional escrow, automatic multi-expert splits and cross-border settlement.

6. Red-team and rejected ledger

The biggest attack is Goodhart's law: if tutor compensation depends heavily on measured progress, experts will optimize the measurement rather than durable understanding. The repair is to guarantee normal tutor compensation and make outcome compensation only a modest upside component. Assessment tasks must be delayed, randomized and structurally different from the examples shown during tutoring.

Second is adverse selection: tutors may prefer easy students. Lift scores therefore need difficulty and starting-state normalization, and dispatch cannot expose learners' raw predicted difficulty as a bidding signal.

Third is cold start. New experts have no lift history, so credentials, teaching simulations and controlled exploration provide priors until actual data accumulates. Recent work showing AI assessment of tutor training and authentic tutoring makes such a bootstrap mechanism more plausible.

Fourth is payment recourse. Stablecoins offer programmable, continuous global settlement, but research also notes weaker standardized consumer recourse than card systems. LiftLoop therefore uses escrow-before-finality, explicit dispute windows and fiat-compatible payment providers rather than exposing raw irreversible transfers to ordinary users.

Finally, no transcripts, student identities or learning scores go on-chain. Only settlement amounts, pseudonymous job identifiers and cryptographic attestations belong there.

7. Evolution lineage

The first evolution merges A's strongest mechanism with B's strongest mechanism.

Instead of matching a learner once, LiftLoop maintains a live Concept Route. A tutor remains assigned while their predicted learning advantage is high. When the session crosses into a concept where another available expert has a materially higher estimated lift, the system can propose a seamless handoff. The next expert inherits the learner model, whiteboard state, misconceptions already identified and the precise unresolved node.

The second evolution removes the weakest part of outcome-based tutoring economics: withholding ordinary tutor pay.

A tutor therefore receives a guaranteed base settlement for verified teaching time. A separate Lift Bonus rewards durable mastery. If mastery is not demonstrated, the learner can receive platform credit from a guarantee reserve rather than clawing back the tutor's normal wage.

That creates healthier incentives while preserving the learning-feedback loop.

8. Winning invention proof stack: LiftLoop

The product experience is radically simple for the learner.

A learner opens LiftLoop and says something like: “I have an exam tomorrow and still don't understand integration by substitution.”

The AI conducts a two-minute adaptive diagnostic—not a generic questionnaire. It determines which prerequisite nodes are secure, where the misconception begins, desired depth, language, urgency, budget and preferred interaction constraints.

The dispatch system then calculates something equivalent to:

expected durable mastery gain × confidence ÷ (price + latency penalty)

for every available qualified expert.

Importantly, a tutor's reputation is not “4.9 stars.” It becomes an Effectiveness Tensor: evidence that Tutor X is unusually effective with, for example, first-year calculus students who understand derivatives but fail substitution selection, especially under exam-time constraints.

During the lesson an AI copilot privately maintains the learner state, identifies concept transitions and creates checkpoints. It assists the human tutor rather than competing with them.

After the appropriate delay, the learner receives a short transfer challenge designed to determine whether they can solve a new problem requiring the same underlying concept. The resulting evidence updates both the learner graph and tutor effectiveness model.

The settlement contract then distributes the base amount, any Lift Bonus, platform fee and—in a relay session—each expert's share.

There is no custom token. Use a regulated stablecoin such as USDC on a low-cost chain/L2 behind an account-abstraction layer, while allowing both learner and tutor to enter and exit through familiar fiat interfaces. Stripe already supports stablecoin acceptance infrastructure, making a walletless UX technically realistic.

The economic model

Existing marketplace fees leave room for a differentiated model: Wyzant says it retains a 25% tutor platform fee and charges students a 9% service fee, while Preply's regular-lesson commission ranges from 18% to 33% and its published model takes the entire trial-lesson amount.

LiftLoop should instead target roughly 8–12% platform economics, with an optional additional Mastery Guarantee fee. Higher-performing specialists make more because the system routes them to the learners for whom they create disproportionate value, rather than simply rewarding tenure, popularity or fast acceptance.

The strongest initial wedge is 18+ undergraduate quantitative subjects, starting with one tightly bounded domain such as first-year calculus. That produces reasonably objective mastery checks while avoiding the child-safeguarding complexity of launching immediately into K–12.

9. Prototype and falsification gate

The first product does not need a giant marketplace, token economy or sophisticated DAO.

Build only the adaptive diagnostic, a learner concept graph, 20–30 vetted tutors in one subject, live video/whiteboard, AI session analysis, delayed transfer questions, a baseline matcher and the Lift Router. Stablecoin escrow handles settlement invisibly.

The central claim should be killed if, after enough repeated sessions to estimate the signal reliably, learning-lift routing cannot produce at least a 15% improvement in delayed mastery per unit of learner spend over ordinary availability/profile-based matching. Also kill or materially redesign the model if achieving that improvement requires unacceptable selection bias, tutor income volatility, excessive assessment burden or persistent dispatch times above roughly five minutes.

This gate isolates the invention. A beautiful app with thousands of tutors proves almost nothing if the lift-based routing mechanism itself does not beat the simpler substitute.

10. Calibrated verdict

Verdict: potentially novel mechanism, with moderate evidence confidence.

The known pieces are strong: large tutor marketplaces exist; instant tutor matching has old prior art; AI can perform learner-state modeling; tutor effectiveness varies; algorithms can optimize educational recommendations around learning gains; and programmable stablecoin payments are viable infrastructure.

The key inference is that these capabilities can be joined into a sufficiently accurate human-tutor effectiveness market.

The speculative part is the causal signal: whether messy marketplace data can distinguish “this tutor produced learning” from differences in learner motivation, difficulty, prior knowledge and self-selection.

The largest remaining prior-art region is the intersection of educational contextual bandits, human-expert matching markets, tutor value-added measurement, outcome-based service contracting and smart-contract escrow. I found close components but not a close deployed match to the full mechanism searched here. That is not proof of universal novelty.

The verdict changes immediately if prior art shows a system that already dispatches live human tutors based on normalized, measured delayed learning gain and feeds those results back into both future routing and programmable tutor settlement.

The resulting company is therefore not “Uber + ChatGPT + crypto.” It is a learning exchange whose market price and routing intelligence are grounded in demonstrated human teaching effectiveness—with instant expert access as the user experience and blockchain settlement almost invisible underneath.

## Output B

I applied the attached NOVUM methodology at the mechanism level: the target is not “a tutoring marketplace with AI and crypto,” because that would fail the anti-fake-novelty gate. The governing standard calls for a causal mechanism difference, plausible advantage, constraint fit, and calibrated novelty claims.

SkillRelay — a real-time market for learning progress

Core idea: the learner does not hire a tutor. They hire the next best human intervention.

SkillRelay treats learning as a continuously changing state-routing problem. AI diagnoses the learner's current bottleneck, dispatches the expert statistically best suited to resolve that exact bottleneck, observes the resulting change in skill state, and then either ends the route or dispatches the next specialist.

Think Uber's dispatch architecture crossed with a medical referral network: one expert does not need to own the entire learning journey.

The key invention delta is:

After stripping away the AI, blockchain, and marketplace terminology, SkillRelay is a state-transition exchange: experts are indexed by the learner-state transitions they have demonstrated an ability to cause; routing chooses an expert for the next desired transition; verified transition evidence updates both future routing and settlement.

That is materially different from ranking tutors by profiles, reviews, credentials, price, or generic compatibility.

Why the ordinary version isn't enough

The obvious territory is already crowded. Wyzant supports “best match” searching and detailed tutor filtering; Preply currently offers AI-generated personalized tutor recommendations. Even automated, dynamic student-to-tutor queuing and routing appears in patent literature dating back decades.

Likewise, “put tutoring payments on blockchain” has little standalone novelty. Blockchain-based learner records, educational rewards, smart contracts, and decentralized learning systems have prior art.

The neglected opportunity is therefore not finding a tutor. It is determining which human intervention should happen next, learning from the observed result, and building marketplace economics around that loop.

The experience

A learner opens SkillRelay and says something like: “I understand derivatives but optimization word problems are destroying me, and my exam is Monday.”

The system does not return 600 calculus tutors.

Goal Compiler. A conversational diagnostic turns the request into a private Skill Contract: goal, deadline, relevant skill graph, current mastery estimates, learning constraints, modality and budget.
Bottleneck Detection. A short adaptive probe identifies that the actual issue might not be calculus at all—for example, translating natural-language constraints into equations.
Expert Dispatch. The router finds an available expert whose historical Teaching Fingerprint shows strength specifically in that misconception, at that learner level. The learner sees one primary match, an ETA, price and concise reason for the match.
Micro-intervention. The expert accepts a 12-, 25- or 50-minute dispatch. AI maintains the shared problem state, notes misconceptions and handles administrative context so the human can teach.
Transfer Check. After the intervention, the learner solves a different problem requiring the same underlying skill. That creates an evidence signal about whether the learner state changed rather than whether the session merely felt good.
Reroute. If the bottleneck moved, the learner can immediately be handed to a different specialist. A one-hour learning journey might therefore involve a conceptual explainer for 15 minutes, a problem-solving specialist for 20 and an exam strategist for 15 instead of one generalist for the full hour.

This turns tutoring supply from people listed by subject into micro-capabilities available on demand.

The AI matching engine

Every learner has a dynamic Learner State Graph. Nodes represent capabilities and misconceptions rather than broad course labels: “recognizes eigenvector condition,” “converts geometric description into linear constraints,” “distinguishes correlation from causation,” and so forth.

Every expert develops a multidimensional Teaching Fingerprint. It is not one score. SkillRelay learns that Expert A may be exceptional with advanced learners who have conceptual misconceptions, while Expert B is unusually effective at rescuing beginners who have procedural gaps.

The router essentially chooses:

j
∗
=arg
j
max
	​

Price
j
	​

+λTime
j
	​

+μWait
j
	​

E[ΔSkill∣L
t
	​

,B
t
	​

,T
j
	​

]
	​


where L
t
	​

 is the current learner state, B
t
	​

 the immediate bottleneck and T
j
	​

 the expert's conditional teaching fingerprint. Credentials, language, availability, safeguarding requirements and learner preferences operate as constraints rather than substitutes for effectiveness.

This approach has a credible technical basis. Educational research has already applied contextual and multi-armed-bandit methods to selecting learning actions from student knowledge states, while recent 2026 work demonstrates interpretable estimation of learner ability and task difficulty directly from tutor–student dialogue. SkillRelay transfers those principles from selecting digital exercises to routing scarce human expertise.

Reputation becomes Impact Receipts

Stars are a weak learning signal. A friendly tutor working with already-strong learners can accumulate superb ratings without necessarily being the best person for a struggling learner; research on teacher effectiveness also highlights how non-random teacher–student matching can bias apparent effectiveness.

SkillRelay therefore creates signed Impact Receipts after sufficiently measurable interventions. A receipt records the skill addressed, anonymized learner-state category, task difficulty, observed mastery transition and confidence level.

The learner's actual answers, transcripts and identity remain encrypted off-chain. Only cryptographic commitments and attestations need to be anchored to the settlement layer.

Experts gradually acquire a portable reputation such as: high-confidence effectiveness on Python debugging for intermediate programmers; strong with recursion misconceptions; insufficient evidence for beginners. That is dramatically more useful to matching than “4.9 stars, 713 reviews.”

It also creates the core network effect: every successful transaction improves the routing graph.

Blockchain has one job: programmable trust

There is no SkillRelay token, no speculative “learn-to-earn” currency and no reason learners should need to understand wallets.

Blockchain is used narrowly where it changes the marketplace economics: cross-border settlement, programmable allocation and portable signed reputation.

A session has two economic components. Most expert compensation is guaranteed once the contracted intervention occurs. A smaller optional impact component becomes releasable after the assessment service generates a signed Impact Receipt. This avoids the unfair model of forcing tutors to bear all the risk of a learner's outcome while still aligning some marketplace economics with actual learning.

For a multi-expert route, one funded learning budget can automatically settle five tiny interventions without five conventional cross-border payouts. Receipts can be batched, and only hashes/attestations need to hit the chain.

The consumer interface can remain completely conventional: “Pay €38.” Behind it, a licensed payments provider handles cards/banks and eligible stablecoin settlement. Stripe currently supports marketplace payment infrastructure, stablecoin payment support with Connect, and stablecoin/global payout capabilities, making this sort of hybrid architecture increasingly practical without SkillRelay itself becoming a crypto custodian.

In Europe, this needs to sit behind appropriately regulated providers rather than attempting to bypass financial regulation; MiCA covers crypto-assets, stablecoins and related service providers.

The marketplace economics

Experts control minimum rates and availability. SkillRelay converts these into an instant quoted price based on intervention length, scarcity, urgency and expertise. There is no public reverse auction, because forcing experts to bid downward would select for cheap supply rather than effective supply.

The platform takes roughly a 10–15% transaction fee to start. Cross-border experts can choose supported local-bank or stablecoin payouts. Frequent learners can pre-fund a learning budget so micro-interventions don't repeatedly incur payment-processing friction.

The most important marketplace flywheel is different from Wyzant/Preply:

more interventions → better conditional impact data → better dispatch → more valuable demand → better expert supply → denser skill coverage → faster dispatch.

The moat therefore becomes the expert × learner-state × misconception outcome graph, rather than a directory of tutor profiles.

Make it genuinely “Uber-like”

The home screen should not say “Browse Tutors.”

It should say:

What are you stuck on?

Then:

Expert found — 3 min away
Best match for: setting up optimization constraints
25 min · €21
Why this match →

Experts operate a “Go Online” mode. Incoming dispatches contain an anonymized problem brief, skill required, duration and guaranteed compensation. Accept, connect, teach, settle.

Scarce domains can support surge pricing. Learners needing obscure expertise—advanced Rust lifetimes, econometrics, organic chemistry spectroscopy, a specific CAD workflow—become economically serviceable because SkillRelay can aggregate global micro-demand rather than requiring a local tutor to cover an entire subject.

Trust architecture

The system cannot allow an AI grader to become an unquestionable payment oracle. Open-ended assessment will sometimes be uncertain. Low-confidence results therefore affect neither expert compensation nor public reputation automatically; disputed or ambiguous cases remain off the impact layer.

Gaming is reduced by using unseen transfer tasks rather than repeating the taught example, difficulty normalization, delayed retention signals where appropriate, statistical shrinkage for experts with little history, and keeping impact bonuses modest relative to guaranteed compensation.

For minors, the cleaner launch architecture is guardian-controlled accounts, strict safeguarding, no public learner credential and no personal educational data written to a public chain. An even cleaner initial wedge is adult and professional learning, where urgent, narrow expertise and global payment friction are particularly pronounced.

What to build

The first production system needs six services: a Goal Compiler that produces the learner skill graph; a diagnostic/assessment service; an Expert Fingerprint store; a real-time dispatch router; a video/chat workspace with AI copilot; and a settlement/attestation service.

The blockchain should be invisible infrastructure behind the last service. The AI should similarly disappear during good teaching. The product users perceive is much simpler:

Describe problem → get expert → learn → continue or reroute → expert gets paid.

No browsing hundreds of profiles. No subscription required. No crypto vocabulary.

Novelty status

The searches support that AI tutor recommendation, automated tutor routing, adaptive learning-action selection, blockchain educational records and blockchain payment mechanisms all exist independently.

What remains differentiated is the architecture that makes measured learner-state transitions the shared primitive for real-time human-expert dispatch, conditional expert reputation and programmable micro-settlement. I would classify that mechanism as potentially novel but not universally verified; the search performed here is not an exhaustive patent/FTO investigation, so it would be inappropriate to claim it is the first implementation.

That calibration follows the attached NOVUM instruction not to mistake an existing product plus generic AI/blockchain for an invention, and to state the irreducible mechanism difference explicitly.

SkillRelay's one-line product thesis:
Don't match students to tutors. Route each learning bottleneck to the human most likely to remove it, then let verified learning transitions make the network smarter and settle the market.

