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
