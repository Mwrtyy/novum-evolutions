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
