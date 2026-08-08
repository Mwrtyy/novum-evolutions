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
