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
