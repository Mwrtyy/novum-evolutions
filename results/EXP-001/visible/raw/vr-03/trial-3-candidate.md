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
