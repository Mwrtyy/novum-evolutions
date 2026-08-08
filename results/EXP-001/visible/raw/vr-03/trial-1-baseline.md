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
