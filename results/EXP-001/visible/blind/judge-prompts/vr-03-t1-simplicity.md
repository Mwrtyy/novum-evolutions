# EXP-001 Blind Judge — vr-03-t1-simplicity

You are evaluating two anonymized answers to the same task. You must not infer or speculate about which system produced A or B. Judge only the text shown.

Evaluator role: `simplicity`
Independence level for this run: `separate_context_same_model`

Act as a simplicity judge. Prefer the smallest intervention that solves the real problem. Penalize unnecessary invention, technology stacking, needless complexity, and failure to recognize a stronger simple substitute.

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
  "pair_id": "vr-03-t1",
  "evaluator_id": "vr-03-t1-simplicity",
  "evaluator_role": "simplicity",
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

# Blind pair vr-03-t1

## Task

Create a revolutionary marketplace that is essentially Uber for expert tutoring, with AI matching and blockchain payments.

## Output A

RELAY — a real-time market for learning bottlenecks

The core invention is not “Wyzant + ChatGPT + crypto.” The supplied methodology specifically requires a meaningful mechanism change and rejects generic AI, blockchain, marketplaces, or decentralization when they are merely bolted onto an existing product.

Relay changes what is bought and sold. Instead of purchasing an hour of a tutor’s time, a learner submits a specific learning incident—“I understand derivatives, but I cannot see why the chain rule applies here”—and Relay dispatches the available expert whose demonstrated teaching behavior best fits that exact bottleneck.

That distinction matters because ordinary “Uber for tutoring” already exists. Tutit offers on-demand, pay-by-the-minute tutoring; TutorNow offers instant live tutor requests; Varsity Tutors says it can match learners with an available tutor within five minutes. Automated student–tutor matching itself is also old prior art, including a 2002 matching patent and more recent work predicting academic outcomes from student and tutor information.

Relay therefore makes the learning bottleneck and required pedagogical intervention, rather than the tutor profile, the primary object in the marketplace.

The operating mechanism

A learner opens Relay from its app, browser extension, LMS, coding environment, or document and taps Help me now. They upload the problem plus whatever they have already attempted. Relay's AI does not immediately solve it. It creates a temporary Bottleneck Signature describing what is actually blocking progress.

For example:

Calculus → chain rule → can differentiate inner and outer functions independently → fails to recognize composition → prefers visual explanation → first-year university → English/French → needs help now.

Recent work on dialogue knowledge tracing shows that a learner's knowledge state and task difficulty can increasingly be estimated from tutoring interactions, although the technology remains imperfect.

Relay then chooses the pedagogical move the situation calls for: Socratic diagnosis, misconception contrast, worked-example fading, visual decomposition, analogy, prerequisite repair, debugging walkthrough, oral practice, and so forth.

Only after selecting the intervention does it select the human.

Every expert develops a continuously updated Resolution Signature derived from what that person actually does during tutoring rather than just stars, credentials, or self-written profile claims. A calculus tutor might be exceptionally effective at visual misconception repair but mediocre at rapid exam drilling; another may excel at identifying hidden algebra gaps. AI analysis of authentic tutoring transcripts is already showing that tutor moves and pedagogical behaviors can be assessed at scale, making this component technically plausible rather than requiring a hypothetical future model.

The dispatch process is conceptually:

learning state → bottleneck → required intervention → available expert capable of that intervention

rather than:

student profile → search tutors → browse ratings → pick somebody.

This is policy-first dispatch.

Why the matching layer is different

Existing marketplaces mainly expose subject, price, ratings, credentials, availability and similar attributes. Wyzant, for example, lets learners filter and sort tutors using subjects, rates, credentials, ratings, experience and availability. More advanced prior art already proposes machine learning that correlates student and tutor attributes with predicted academic outcomes, so simply claiming “AI finds the tutor most likely to improve your grade” would be too close to known territory.

Relay instead first asks:

“What teaching intervention is required at this exact moment?”

Then:

“Who online right now has demonstrated evidence of executing that intervention well in this context?”

Conceptually:

k
∗
=PolicySelector(learning state, error trace, task, context)
Tutor
∗
=arg
t
max
	​

ExecutionFit(t,k
∗
)×ContextFit(t)×Availability(t)÷Price(t)

Credentials remain a hard eligibility filter, not the principal ranking signal.

This also addresses an important emerging result: the impact of on-demand human tutoring appears heterogeneous rather than uniform. A 2026 causal-analysis preprint covering more than 5,000 tutoring sessions found considerable variation in estimated session-level effects, reinforcing the importance of which intervention is delivered when, rather than treating all tutor-hours as interchangeable.

Relay Pool: Uber Pool for misconceptions

Relay's second structural mechanism attacks tutoring economics.

When several learners are simultaneously stuck on essentially the same conceptual bottleneck, Relay can temporarily combine them into a three-to-five-person Pulse instead of dispatching separate tutors.

Imagine five students at different universities who all incorrectly believe that statistical significance means a large practical effect. Their assignments differ, but the underlying misconception is equivalent. Relay detects that equivalence, offers each learner a cheaper Pool session, dispatches one appropriate statistics expert, and gives that expert each student's private context through an AI copilot.

The cohort is dynamic. If one learner turns out to have a different prerequisite problem, the system forks that learner into a different intervention instead of forcing everyone through the same lesson.

Dynamic student grouping has research precedent, so grouping itself is not the invention. The architectural delta is real-time market clearing around a diagnosed misconception, simultaneously matching learners to one another and the resulting cohort to an intervention-specialized expert.

That changes the economics without simply lowering tutor wages. Three learners might each pay substantially less than a solo session while the expert receives more for those fifteen minutes than from a one-to-one session.

The learner experience

Relay should feel closer to requesting a ride than hiring a freelancer.

The home screen has one dominant control: What are you stuck on?

The learner can speak, type, photograph handwritten work, share a screen, paste code, or import an LMS problem. Relay spends roughly a minute establishing what the learner knows and where the reasoning breaks. It then shows something like:

We found the bottleneck: conditional probability vs. inverse probability
Recommended help: misconception-contrast session
Expert: Maya — available now
ETA: 42 sec
Estimated session: 11–16 min
Solo: €14
Pool: €7.50

There is no page with 400 tutor profiles.

The expert receives the opposite view:

Incoming incident
Intro Statistics · Bayes theorem
Misconception: reversing P(A|B) and P(B|A)
Learner already understands: conditional probability notation
Recommended intervention: frequency-table counterexample
Estimated complexity: short
Offer: €11–€15
Accept: 15 seconds

When accepted, Relay launches the whiteboard/video/audio workspace with the learner's relevant reasoning already summarized, eliminating the first ten minutes tutors frequently spend reconstructing the problem.

AI has a constrained role

Brainly already combines an AI learning companion with live human experts, so merely putting humans behind an AI tutor would not create enough architectural separation.

Relay uses AI primarily as the market maker.

It diagnoses demand, translates messy learner requests into standardized learning incidents, chooses an intervention family, assembles compatible cohorts, routes experts, generates the handoff brief, monitors for a change in the diagnosed bottleneck, and preserves continuity between sessions.

The AI can provide low-risk scaffolding while a tutor is being dispatched, but its strategically important function is coordinating scarce human expertise.

That also creates a much stronger data flywheel than ordinary star ratings. Every completed interaction adds evidence of the form:

state A + misconception M + intervention K + tutor T → observed state transition

Over time Relay builds a map of who is unusually good at teaching what kind of learner through what kind of difficulty.

Blockchain payments that have an actual reason to exist

Relay should have no speculative token.

Learners see ordinary euros, dollars or local currency. Experts can choose normal bank payouts or stablecoins. The blockchain layer exists because Relay produces unusually frequent, small, cross-border, sometimes multi-payer transactions.

A Pool session, for example, can contain four independently funded learner escrows that stream into one tutor payment while automatically returning unused balances. A fifteen-minute session between a French learner and a Brazilian expert should not require both participants to understand wallets.

The preferred settlement asset is a regulated dollar stablecoin such as USDC, with wallet abstraction above it. USDC is designed for programmable, always-on cross-border payments, while current payment infrastructure such as Stripe increasingly supports stablecoin acceptance and marketplace payouts.

The flow is:

learner payment → Relay session escrow → metered session → tutor earnings → bank or stablecoin payout

The smart contract contains only financial state and opaque transaction identifiers. Student identities, transcripts, grades, diagnoses and learning histories never go on a public blockchain.

A dispute freezes the unsettled portion and routes the case into platform arbitration. Identity verification, sanctions screening, KYC/AML and fiat handling belong with regulated payments infrastructure rather than homemade crypto infrastructure. Stripe Connect, for example, is explicitly designed for marketplace onboarding, verification and payouts.

Blockchain escrow itself is known prior art—including smart-contract escrow and even a small tutoring-specific blockchain escrow project—so it is an enabling rail, not Relay's novelty claim.

Expert reputation becomes a map, not a number

A five-star tutor may be wonderful overall and still be wrong for a particular bottleneck.

Relay therefore replaces the single reputation score with a Resolution Map:

Dimension	Example
Knowledge domain	Calculus I
Bottleneck	recognizing composite functions
Intervention strength	visual decomposition
Level	secondary → first-year university
Communication	concise, highly Socratic
Languages	French, English
Modality	whiteboard + voice
Operational history	63 comparable incidents
Reliability	98% accepted sessions completed

Public-facing profiles can still contain biography, credentials and reviews. But dispatch uses the map.

Experts consequently discover that they have economically valuable micro-specialties they may never have thought to advertise: “debugging recursion misconceptions,” “helping French speakers pronounce English /θ/,” or “explaining cash-flow statements to engineers.”

Those specialties become marketplace inventory.

Supply economics

Relay lets tutors specify a minimum effective rate, expertise boundaries and working windows. They do not compete through a race-to-the-bottom auction.

The marketplace can retain approximately 10–15% of session value rather than depending on very high commissions. For context, Wyzant's published tutor platform fee is 25%.

Pricing is driven by bottleneck-level supply rather than generic subject supply. “High-school algebra” might have abundant tutors at 17:00, whereas “measure-theoretic probability in French” may have two qualified experts globally and command a significant scarcity multiplier.

Pool sessions are especially important. A student can pay less while the tutor earns more because one pedagogical intervention serves several aligned learners. That is a structural productivity increase rather than a subsidy.

Trust, cheating and minors

Relay should initially launch with 18+ university and professional learners, where the marketplace can validate the core mechanism without immediately absorbing the full safeguarding burden of K–12 education.

Every tutor still needs verified identity and subject credentials appropriate to the domain. Professional fields can incorporate certification verification where relevant.

Relay also needs a hard distinction between learning assistance and answer outsourcing. If the system detects a live exam, explicit request for impersonation, or a request to produce assessable work without learner participation, dispatch is restricted. The incident compiler is designed around the learner's attempt and reasoning rather than “upload question → receive answer.”

When K–12 is added, the architecture should introduce guardian accounts, verified child-safe tutors, controlled communications, session monitoring, stricter data retention and jurisdiction-specific safeguarding controls.

System architecture

The client layer consists of iOS, Android, web, browser extension and eventually LMS/IDE integrations.

Behind it sits an Incident Compiler: multimodal ingestion, reasoning extraction, academic-integrity controls, skill graph, learner-state estimation and Bottleneck Signature generation.

The Learning Market Maker contains the intervention-policy selector, real-time expert availability engine, Resolution Signature index, pricing engine and Pool assembler.

The Session Fabric provides WebRTC, collaborative canvas/code environment, AI copilot, translation, transcription and structured handoffs.

The Trust Plane handles identity, credentials, safeguarding policies, tutor-quality signals, fraud controls and disputes.

Finally, the Settlement Plane maintains fiat quotes and accounting off-chain while using stablecoin rails for programmable escrow and optional global tutor payouts.

The data architecture should use conventional infrastructure for most of the system: relational storage for accounts and transactions, a vector/feature store for incident and intervention representations, low-latency availability storage, an event stream for session telemetry and encrypted object storage for permitted recordings. The blockchain is intentionally confined to settlement.

The strongest launch wedge

Launch Relay with college STEM debugging, not “every subject for everyone.”

Start with calculus, statistics, introductory physics and introductory programming. They produce abundant discrete “I'm stuck” moments, learner attempts are relatively easy to inspect, diagrams/code can be shared digitally, expertise is globally available, and the bottlenecks can be represented much more precisely than broad requests like “teach me history.”

The initial marketplace promise becomes:

“Show us where you're stuck. Relay will diagnose the bottleneck and put the right expert into your problem—not merely an available tutor—within minutes.”

Once the intervention graph has enough density, expand horizontally into language speaking, professional certification, coding, accounting, engineering and other domains.

What was deliberately removed

I would not build a native Relay cryptocurrency, tutor NFTs, a DAO for marketplace governance, generic “AI-powered recommendations,” browse-first tutor profiles, grade guarantees, or a bidding war between tutors.

I would also not make “AI tutor with human escalation” the defining idea: Brainly already demonstrates that combination. Nor would I make “instant tutor in an app” the thesis; Tutit, TutorNow and Varsity Tutors establish that pattern already.

The irreducible invention is:

A real-time marketplace that converts an observed learner error into a required pedagogical intervention, then clears expert supply—and optionally equivalent learner demand—around that intervention rather than around tutor profiles or booked hours.

Everything else supports that mechanism.

Evidence boundary

The frontier scan found close prior art in on-demand tutoring, AI/live-expert hybrids, knowledge tracing, tutor-performance analysis, machine-learning tutor selection, dynamic learner grouping and smart-contract escrow. It did not reveal a close public example of the entire policy-first learning-incident market architecture described above, particularly the combination of bottleneck-level dispatch and real-time misconception pooling.

That is not proof of universal novelty, and this is not a patent or freedom-to-operate opinion. The closest area requiring particular care is ML-based tutor selection tied to predicted student outcomes, especially US20240249636A1 and related tutor-matching disclosures.

So the defensible product to build is Relay: the learning-incident exchange, with AI as the market maker, human pedagogical intervention as the scarce asset, and stablecoins as invisible settlement infrastructure.

## Output B

Learning Dispatch Protocol — “Uber for being stuck”

The requested shell—an expert-tutoring marketplace with AI matching and blockchain payments—is not itself revolutionary. Automated tutor matching dates back decades, current systems already rank tutors algorithmically, per-minute expert marketplaces exist, and at least one current education platform combines AI tutoring, adaptive knowledge structures, proof-of-learning, blockchain credentials, and a knowledge marketplace.

So the invention has to change the underlying causal mechanism, not add more technology. That follows NOVUM's requirement that novelty survive removal of generic AI, blockchain, and marketing language.

The resulting concept is:

Do not sell tutors or tutoring hours. Sell the resolution of a precisely diagnosed learning bottleneck.

A learner never starts by browsing profiles. They press “I’m stuck.” The system diagnoses what they are actually stuck on, dispatches the human expert with the strongest evidence on that specific cognitive transition, carries the learning state between experts if a handoff is necessary, and automatically divides payment among the humans who contributed to the resolution.

That produces an entirely different marketplace.

1. Problem reframing

The challenge is to give a learner immediate access to the human expert most capable of resolving their current learning obstacle, without requiring the learner to know which tutor they need, browse profiles, schedule a 50-minute lesson, repeatedly explain their history, or pay for substantial irrelevant time.

Today's dominant marketplace unit is still essentially Tutor × Time. Wyzant tutors choose hourly rates; Preply centers bookings, trials, recurring subscriptions and lesson balances; Clarity demonstrates the adjacent expert-market model of charging a specialist by the minute.

The redesigned unit is:

Learning state A → verified learning state B

The tutor becomes the supplier capable of performing that transition.

For example, “calculus tutor” is too coarse. The marketplace might discover that the learner understands derivatives but repeatedly treats the derivative of a composition as a product. Their actual demand is a narrow transition:

“Can execute derivatives” → “correctly models nested functional dependency when applying the chain rule.”

A tutor who is mediocre across calculus generally but exceptional at diagnosing that misconception could outrank a famous calculus tutor.

2. Frontier and opportunity gap

The crowded territory is easy to identify. Tutor search and ranking are well established and explicitly covered by prior patents. AI tutoring increasingly performs personalization and misconception detection. Human-AI tutoring systems such as Tutor CoPilot already demonstrate AI support inside live human tutoring. Blockchain escrow and tokenized reputation also exist independently.

More recent work strengthens an important enabling capability: models can infer misconceptions from actual student-tutor dialogue, while other research is examining AI assessment of authentic human tutor performance. Those capabilities make much finer-grained expert routing plausible than conventional subject/category matching.

The neglected territory is the intersection of three mechanisms: learning-state-level demand, live expert relay, and outcome-specific expert reputation. My searches found adjacent pieces, but not a close implementation of that combined market mechanism. That is evidence of differentiation, not proof of universal novelty.

The central contradiction is particularly useful: instant marketplaces want interchangeable suppliers, while good tutoring benefits from continuity and knowledge of the learner. The invention resolves this by moving continuity away from the individual tutor and into a persistent, permissioned learner-state object that can travel safely between specialists.

3. The mechanism search

Four mechanically distinct possibilities were considered before collapsing the design around one architecture.

Mechanism	Irreducible idea	Disposition
Misconception Dispatch	Match demand to an exact misconception or missing prerequisite instead of a tutor category.	Preserve
Expert Relay	Change tutors inside one continuous learning interaction as the diagnosed bottleneck changes.	Preserve
Outcome-Quoted Market	Experts bid on estimated time/probability of resolving a learning problem.	Reject; too vulnerable to gaming and resembles older reputation/dynamic-pricing markets.
Flash Cohorts	Aggregate learners currently stuck on the same problem into temporary microclasses.	Secondary capability, not the core invention

The surviving design fuses the first two mechanisms without requiring the rejected bidding/staking structure.

4. The invention: Resolution Relay

Call the architecture Learning Dispatch Protocol, with Resolution Relay as its core operating mechanism.

The learner purchases a resolution attempt rather than selecting a person. AI converts the learner's question, work, voice explanation, code, screenshot, or prior session history into a structured Learning Incident. The system routes that incident to a human specialist whose demonstrated expertise is specific to the diagnosed transition.

If the first tutor discovers that the initial diagnosis was wrong, they do not drag the session outside their expertise. They reclassify the incident. The session can immediately hand off to another specialist, with the learner's reasoning history, diagrams, attempted explanations, and unresolved prerequisite transferred in a compact state packet.

The learner experiences one continuous session. Behind it may be one expert or a relay of several.

The irreducible innovation delta is:

A real-time marketplace whose tradable unit is a diagnosed learning-state transition, where human experts are ranked by transition-specific resolution history and can be dynamically composed inside one continuous session.

Remove blockchain and it remains differentiated. Remove generative AI and an inferior version could theoretically operate with conventional diagnostics. Remove branding and tutor profiles and the mechanism remains intact. That is the important distinction.

5. What the learner experiences

Imagine a university student is stuck on a Python recursion problem. They tap Get unstuck now and share the code plus a thirty-second explanation.

Instead of returning “five Python tutors,” the AI identifies high uncertainty between two hypotheses: misunderstanding the recursive base case versus misunderstanding mutation of shared state.

A tutor specializing in recursion/base-case reasoning is available in 47 seconds. The tutor receives a private packet saying, in effect: learner can trace a simple recursive call; probable failure is termination reasoning; confidence 0.71; do not assume understanding of stack frames.

During the interaction, it becomes clear that recursion is not the actual obstacle. The learner is mutating a list shared between calls.

The tutor taps reroute.

Within the same room, a second expert who has strong evidence specifically on Python reference/mutation misconceptions joins. The learner does not restart, search again, make another booking or retell the story.

The marketplace has behaved much more like an emergency-dispatch system than a directory.

6. AI matching becomes causal dispatch

The matching engine should not optimize a generic five-star tutor ranking.

Each expert accumulates an Edge Reputation Graph. An edge is a transition such as:

fraction-addition misconception → correct denominator model

or:

SQL join syntax knowledge → correct join-cardinality reasoning

or:

intermediate French grammar → spontaneous correct subjunctive selection

Each tutor's profile therefore contains hundreds or thousands of narrow competency edges instead of twenty subject tags.

Routing can approximately optimize:

P(resolution | learning edge, learner context, tutor) − wait penalty − cost penalty − handoff penalty

Availability, language, accessibility requirements, communication modality and learner preferences constrain the candidate pool before the model ranks it. Sensitive demographic attributes should not be secretly turned into pricing or quality proxies.

New tutors solve the cold-start problem through calibrated diagnostic tasks, supervised initial incidents and controlled exploration rather than being permanently buried beneath incumbents with thousands of reviews.

This is also much more informative than star ratings. “4.9-star physics tutor” tells the marketplace relatively little. “Has repeatedly corrected force-versus-velocity misconceptions in first-year mechanics learners” is directly relevant to dispatch.

7. Architecture
Layer	Function
Learner interface	One-tap incident creation from text, voice, handwriting, screen share, IDE or uploaded work.
Learning State Engine	Maintains concepts, prerequisites, misconception hypotheses, confidence and previously demonstrated understanding.
Incident Compiler	Converts “I don't understand this” into a privacy-filtered diagnostic packet.
Expert Edge Registry	Stores each tutor's narrow demonstrated capability, modality, latency, availability and constraints.
Dispatch Engine	Routes the current learning edge to the best available specialist.
Relay Room	Shared whiteboard/video/code environment supporting instant expert handoffs without resetting context.
Resolution Verifier	Checks whether the targeted state transition has actually occurred using fresh reasoning rather than simple self-report.
Settlement Rail	Handles escrow, streaming compensation and multi-expert payment division.
Trust Layer	Identity, credentials, dispute handling, safeguarding, fraud monitoring and permission management.

The learner's complete transcripts, assessment answers, recordings and personal profile should never be written to a public blockchain.

8. Blockchain that has an actual job

The common mistake would be inventing a tutor token, NFT badges and speculative staking. That fails the anti-fake-novelty gate; tokenized reputation and blockchain education credentials already have substantial precedent.

Here blockchain has a narrower purpose.

A learner preauthorizes a resolution budget. Tutors receive a guaranteed time component as they work, preventing difficult students from becoming unpaid labor. A smaller resolution component can be unlocked when the agreed learning transition is independently attested.

When a session relays from Expert A to Expert B, the settlement contract divides compensation automatically. Neither tutor has to invoice the other, and an independent tutoring app, university, bootcamp or corporate learning platform could tap the same expert-liquidity network.

The chain can also hold cryptographic commitments to Resolution Receipts: “this verified provider contributed to transition X under protocol Y.” The underlying educational evidence remains encrypted off-chain.

That gives expert reputation portability without publishing learner data.

Payments can be presented entirely as normal local currency to consumers. Stablecoin or other blockchain settlement can remain infrastructure underneath, used only where legally and operationally appropriate. There is no need for a speculative native token.

9. A new economic model

Traditional marketplaces effectively monetize time and recurring tutor relationships. Preply, for example, currently uses a subscription-oriented lesson model and charges tutors commissions ranging from 18% to 33% on subsequent lessons, while the first trial lesson carries 100% commission.

Learning Dispatch instead has three prices embedded in one quote: an expert availability component, metered human intervention, and a capped resolution component.

That design matters. Making all compensation conditional on mastery would create ugly incentives: tutors would avoid difficult learners, manipulate diagnostics, or cherry-pick easy problems. Guaranteed base compensation plus a limited verified component preserves the market signal without turning tutoring into a bounty hunt.

The platform can collect a small settlement/dispatch fee and separately sell institutional access to its expert-liquidity network and matching infrastructure.

10. Continuity without tutor lock-in

Multi-tutor learning already happens, but existing platforms do little to coordinate it. Users themselves report employing several tutors for different functions, while noting that tutors may have no way to coordinate and can duplicate one another's work.

Resolution Relay turns that accidental behavior into system architecture.

The continuity layer belongs to the learner:

What I know → what I am attempting → what keeps failing → what has been tried → what explanation worked → what remains unresolved.

A new specialist sees only the context necessary for that incident, not the learner's entire educational history.

For learners who value a relationship with one person, an optional anchor tutor can remain attached to the account while the dispatch network supplies specialists. The anchor becomes the longitudinal mentor; the relay handles acute bottlenecks.

11. The moat

The strongest defensibility is not the LLM and not the blockchain.

It is the resolution graph created through marketplace activity.

Every legitimate interaction creates information linking a learner state, misconception, tutor, intervention style, modality and verified state transition. Over time the system can learn, for example, that one expert is unusually effective when an otherwise strong programmer confuses concurrency with parallelism, while another is exceptional at explaining probability to learners with strong algebra but weak intuition.

That dataset is radically more useful for matching than conventional profiles and reviews.

The network also creates unusual liquidity. A world-class specialist does not need to accept a weekly student commitment. They can become available for twenty-minute windows and solve exactly the class of problems at which they excel.

That brings highly specialized people into tutoring who might never join a traditional tutoring marketplace.

12. Where it should begin

The first market should not be “all education.”

Start with adult and university learners in domains where bottlenecks are relatively observable: mathematics, statistics, programming, accounting, engineering and technical professional certification.

Those domains make incident diagnosis, expert specialization and resolution evidence substantially cleaner while avoiding many of the safeguarding complications of launching immediately with children.

The killer interaction is not “schedule a lesson.”

It is:

Stuck → diagnosed → expert appears → problem state follows you → resolved or intelligently rerouted.

Once that interaction works, longer coaching, persistent tutors, small groups and institutional programs become extensions of the same market.

13. Red-team ledger
Failure pressure	Architectural response
Short-term correctness masquerades as understanding	Resolution requires fresh reasoning on a related task, not repeating the tutor's example.
Tutors optimize for easy cases	Guaranteed base compensation; difficulty-adjusted routing; no all-or-nothing bounty system.
AI misdiagnoses the learner	Diagnosis is probabilistic and tutors can reroute without penalizing the learner.
Handoffs destroy human connection	Persistent learner-state layer plus optional anchor tutor; relay only when specialization warrants it.
Tutor and learner collude to manufacture reputation	Independent verification, anomaly detection and delayed reputation finalization.
Blockchain creates privacy disaster	Only payments, signatures and commitments belong on-chain; educational content stays off-chain.
Marketplace becomes homework cheating	No live-proctored-assessment assistance; pedagogy mode requires learner reasoning rather than answer delivery.
Reputation locks out newcomers	Separate initial qualification signals from historical market reputation and reserve exploration traffic.
Blockchain adds complexity without value	Hide wallets completely and permit conventional payment rails; chain is infrastructure, not the user proposition.

The most serious unresolved weakness is measurement. Human learning is not a binary event, and some intellectual work—essay development, research mentorship, creative reasoning, confidence building—cannot be reduced safely to a tiny state transition. The architecture therefore has a natural operating boundary rather than pretending to cover every educational relationship.

14. Prior-art boundary and honest verdict

Generic tutor matching is clearly known. AI diagnosis of misconceptions is active current work. AI support for human tutors is known. Per-minute expert marketplaces are known. Blockchain escrow, tokenized reputation, proof-of-learning and blockchain educational credentials are known.

What my search did not surface was a close system whose fundamental market unit is a learning-state transition, whose human experts possess transition-specific reputation, and whose live session can dynamically relay the learner among multiple specialists while preserving one continuous learning state and atomically dividing compensation.

Accordingly, the calibrated verdict is potentially novel mechanism / differentiated architecture, not “first,” “patentable,” or proven. That wording follows the truth standard in the governing NOVUM instructions.

The claim collapses if narrow edge-specific expertise proves no more useful for dispatch than ordinary tutor-level reputation, if reliable learning-state transitions cannot be determined well enough to support fair settlement, or if relay costs consistently outweigh the benefit of bringing in a more specialized human. Those are the concept's real kill conditions.

The revolutionary shift is therefore simple to state:

Uber dispatches the nearest qualified driver to a trip. Learning Dispatch continuously dispatches the most qualified mind to the learner's current unresolved cognitive edge—and the “vehicle” being routed is the learner's state, not the tutor.

