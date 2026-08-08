# EXP-001 Blind Judge — vr-07-t2-domain_or_generalist

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
  "pair_id": "vr-07-t2",
  "evaluator_id": "vr-07-t2-domain_or_generalist",
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

# Blind pair vr-07-t2

## Task

Create a revolutionary hiring platform for small restaurants using AI agents, blockchain, and a marketplace. The main operational bottleneck is that hired workers frequently do not show up for scheduled shifts.

## Output A

NOVUM result: Kitchen Reserve Protocol

I followed the uploaded NOVUM requirement to produce a concrete, falsifiable invention candidate rather than a generic feature bundle.

1. Problem reframing

The real product is not “AI recruiting for restaurants.”

The challenge is:

Achieve near-continuous staffed-shift coverage for small restaurants after a hiring decision, despite worker cancellations and no-shows, while keeping backup labor economically tolerable and avoiding punitive worker incentives.

The strongest current substitutes attack pieces of this problem. Restaurant hiring systems automate sourcing, screening and scheduling; Qwick uses AI trained on hospitality shift history and reliability signals; Instawork imposes reliability policies and can place paid backup workers; WorkWhile offers paid remote standby; ordinary staffing agencies already sell fill-rate guarantees.

That means AI matching, reminders, ratings, blockchain reputation, and a normal shift marketplace are individually saturated mechanisms.

2. The neglected opportunity

The key contradiction is:

Restaurants need redundancy, but dedicated redundancy is expensive.

Instawork's backup model, for example, can require a backup professional to arrive ready to work and receive four hours of pay even when unused. Remote standby reduces that burden, but it is still usually organized around an individual company or anticipated shift.

The overlooked mechanism is borrowed from electricity grids and reliability engineering:

Pool reserve capacity across many independent restaurants rather than assigning one backup to every risky shift.

A power grid does not put a spare generator beside every customer. It pools reserve capacity and dispatches it when failure actually occurs. Kitchen Reserve applies that architecture to neighborhood restaurant labor.

3. The invention

Kitchen Reserve is a marketplace where restaurants buy a coverage commitment, not merely a candidate or a worker assignment.

Every new hire enters a short stabilization window—for example, their first eight scheduled shifts. The platform does not earn its full hiring fee merely because an offer was accepted. It becomes responsible for keeping those shifts covered.

Behind each restaurant's schedule sits a neighborhood Human Reserve Market. Qualified workers voluntarily sell paid availability windows such as:

Line cook, 5–10 p.m., Tuesday, able to reach this restaurant cluster within 35 minutes.

Those workers are not attached one-for-one to specific restaurants. AI agents pool them against the combined failure risk of dozens of nearby shifts. If three restaurants each have a modest probability of a call-out, the network might need one or two reserve workers rather than three dedicated backups.

That pooling mechanism is the principal innovation.

4. Operating cycle

A restaurant's agent imports schedules, roles, wages, certifications and location constraints. When somebody is hired, the first several shifts automatically become covered shifts.

A worker-side agent maintains the worker's voluntarily supplied availability, qualifications, commute constraints, workload limits and preferences. It refuses commitments that are physically unrealistic and can offer unused time as paid reserve capacity.

The market-making agent continuously maintains enough qualified reserve capacity for each geographic zone. It explicitly models correlated failures—bad weather, transit outages, major events or widespread illness—rather than assuming every absence is independent.

As a shift approaches, the system moves through commitment states. A worker can release an early commitment cleanly while there is still time to reallocate. Nearer the start, the platform increases reserve protection around deteriorating commitments.

When a primary worker calls out or becomes sufficiently unlikely to arrive, the dispatch agent exercises the best reserve commitment and sends that worker to the restaurant. The restaurant manager sees “covered”, not a panic-driven list of candidates to phone.

5. Why this is different

The closest pieces already exist, but separately.

AI prediction of whether a temporary worker will actually show for a shift has already been disclosed in patent literature. Automated replacement-worker searches are decades old, and a 2024 patent describes designated backup-worker networks with reminder and replacement workflows.

Paid standby is also known. Staffing SLAs are known. Recruiting agencies commonly offer replacement guarantees when hires depart early.

The irreducible difference here is therefore:

A probabilistic, geographically pooled labor-reserve market in which independent restaurants purchase shift-coverage capacity, reserve workers receive capacity payments independent of actual dispatch, and the hiring company's obligation continues through the new hire's operational stabilization period.

This changes redundancy from one backup per worker into shared reserve capacity against a portfolio of attendance risks.

6. Where the AI agents matter

There are five agents, and none is simply a chatbot.

Agent	Control responsibility
Restaurant Agent	Converts the restaurant's schedule into coverage requirements and decides which shifts need higher reliability tiers.
Worker Agent	Protects worker preferences, checks schedule/commute feasibility and sells only genuinely available capacity.
Reserve Market Agent	Calculates how much shared standby capacity each zone needs and clears capacity payments.
Dispatch Agent	Reassigns workers when coverage risk changes and optimizes arrival time, qualification and labor cost.
Trust Agent	Verifies qualifications, commitment receipts, attendance evidence and suspicious manipulation.

The important change from current AI matching is that the AI is managing a reliability portfolio, not merely ranking which individual looks most likely to show up.

Current Qwick matching already incorporates skills, experience, reliability, shift history, attendance patterns and preferences, so simply predicting a better candidate would not provide enough innovation delta.

7. Where blockchain actually belongs

Blockchain should not hold résumés, GPS histories, personal information or a speculative restaurant-work token.

Its useful job is preventing trust failures in an open reserve market.

A reserve commitment is a scarce resource. A worker, agency or labor cooperative should not be able to secretly promise the exact same 6–10 p.m. reserve capacity to five competing market operators. Each time-bounded commitment therefore creates a pseudonymous capacity lock anchored on a low-cost chain.

Successful shifts create cryptographically signed attendance receipts. Skills, certifications and work-history assertions are carried as privacy-preserving verifiable credentials; W3C Verifiable Credentials 2.0 is already a standardized basis for machine-verifiable, cryptographically secured credentials.

Existing blockchain labor systems already demonstrate escrow and blockchain-based reputation, so merely putting worker ratings on-chain would be incremental.

Kitchen Reserve instead uses the ledger for cross-market capacity accounting and portable fulfillment proofs.

All sensitive data remains off-chain. The chain contains commitment identifiers, hashes, signatures and settlement state.

8. A two-sided reliability passport

One major repair is necessary: do not create a permanent worker blacklist.

Real-world app-based attendance records can be wrong when GPS, cellular connectivity or clock-in systems fail; worker reports describe being marked absent despite working.

Attendance therefore uses multiple attestations: a venue QR/NFC challenge, worker signature, restaurant signature and optional device/location evidence. Disputed events remain disputed rather than automatically becoming negative permanent records.

And the passport is reciprocal.

Workers accumulate verified evidence such as completed commitments and timely releases. Restaurants accumulate evidence such as whether promised shifts existed, workers were actually needed, cancellations were handled properly and payment obligations were honored.

This matters because reputation systems can create value for smaller employers too; research on online labor markets has found that employer reputation can materially affect workers' willingness and ability to transact with smaller employers.

9. Marketplace structure

Kitchen Reserve has three things for sale simultaneously:

Market	Buyer	Seller	Object
Employment market	Restaurant	Worker	Regular job/recurring schedule
Reserve market	Coverage pool	Worker or staffing provider	Paid availability window
Coverage market	Restaurant	Kitchen Reserve	Guaranteed staffing service level

Workers never deposit money or stake tokens against their attendance. Instead, reliable availability itself is compensated.

That distinction is important. Financial slashing would disproportionately burden workers with little liquidity and could turn a useful reliability mechanism into a coercive one.

A worker who reserves four hours but is never dispatched still receives the agreed capacity fee. If dispatched, they receive the applicable wage under the compliant employment/staffing structure.

10. Small-restaurant advantage

Large chains can create internal float pools. Independent restaurants usually cannot.

Kitchen Reserve manufactures comparable scale by pooling geographically adjacent independents.

A neighborhood containing twelve restaurants effectively behaves like one distributed employer for reserve planning while remaining twelve separate businesses for everything else.

The marketplace becomes stronger as it learns that a prep cook who has verified experience at Restaurant A can also safely cover Restaurant B, while somebody certified only for front-of-house cannot.

That creates a restaurant labor mesh rather than another job board.

11. Business model

The platform should align its revenue with the restaurant's operational problem.

The base product can be a low monthly restaurant subscription covering hiring, scheduling integration and the worker passport. Restaurants then pay a transparent coverage premium for stabilization and critical shifts. Reserve workers receive availability fees from that pool, while actual emergency labor is billed separately.

Crucially, there should be no anti-poaching trap. If a restaurant repeatedly likes a reserve worker, it should be allowed to hire that person permanently. The platform wins because every converted worker enlarges its credential network and the newly hired worker can still optionally participate in reserve markets elsewhere when legally and contractually appropriate.

That makes the marketplace a permanent-hiring engine fed by verified work, rather than a temp platform trying to prevent successful matches from leaving.

12. Red-team repairs

The greatest technical danger is correlated failure. A snowstorm can make ten seemingly independent worker commitments fail together. The reserve engine therefore prices correlation and can stop selling high coverage levels when the available reserve margin becomes unsafe.

The greatest economic danger is insufficient density. A rural restaurant with three potential workers within an hour cannot benefit much from pooled redundancy. Kitchen Reserve is initially a dense-metro/suburban-cluster product.

The greatest human danger is surveillance. Worker agents therefore keep precise calendar, location and preference information private whenever possible; the market receives feasibility assertions rather than raw histories.

The greatest governance danger is algorithmic exclusion. AI can collect structured hiring information, but consequential hiring decisions should remain auditable and human-controlled. Current research shows both potential benefits from standardized AI interviewing and continuing concerns about discriminatory or dehumanizing AI-mediated hiring.

The greatest regulatory danger is worker classification. Reserve labor needs jurisdiction-specific employment, staffing-agency or employer-of-record treatment rather than assuming that every restaurant worker can simply be labeled an independent contractor.

13. The falsifiable core claim

The invention lives or dies on one mechanism:

No-show risk across a dense restaurant cluster must be poolable enough that shared paid reserve capacity costs materially less than maintaining dedicated backup capacity while still providing useful dispatch times.

If simultaneous failures are so correlated that Kitchen Reserve effectively needs one standby worker for every vulnerable shift, the core architectural advantage disappears.

If restaurant density is too low for a qualified reserve worker to reach a failed shift quickly, the mechanism also fails.

If those conditions hold, the platform should not hide behind better AI, better branding or a token.

Honest verdict

Classification: potentially novel mechanism, with meaningful prior-art risk.

The search found all of the surrounding components: AI show-up prediction, automated substitute fulfillment, worker backup networks, paid standby, staffing fill-rate SLAs, hiring replacement guarantees, blockchain employment reputation and verifiable credentials.

I did not find a close match for the specific combination in which a neighborhood of independent restaurants is treated as a stochastic reliability portfolio, workers sell paid reserve capacity rather than being dedicated backups, AI agents perform real-time reserve dispatch, blockchain prevents undisclosed double-sale of that capacity across marketplace participants, and the hiring provider's commercial responsibility extends through the new hire's early attended shifts.

That does not establish universal novelty or patentability. The largest unresolved prior-art territory is the intersection of workforce overbooking, standby staffing, capacity/reserve markets, staffing SLAs and contingent-labor optimization. The strongest invention is therefore not “blockchain restaurant hiring.” It is turning restaurant labor reliability into a pooled reserve-capacity market.

## Output B

ShiftMesh — a hiring platform that guarantees the shift, not just the hire

The core redesign is simple: small restaurants should stop buying a promise from one worker and start buying guaranteed role coverage from a local labor network.

ShiftMesh is an AI-agent labor marketplace in which every important scheduled shift becomes a Coverage Contract. The restaurant still hires a real person as the primary worker, but the contract is simultaneously backed by fractional reserve capacity from nearby qualified workers. AI agents continuously clear that reserve capacity across many restaurants; blockchain provides portable work credentials and neutral settlement of the coverage obligation.

That distinction matters because existing technology already does most of the obvious things. Restaurant and hourly-work platforms recruit, schedule, remind, swap, and find replacements. Instawork even uses paid backup workers who may receive four hours of pay when they arrive but are not needed, while Teambridge now markets AI agents that automatically find replacements after call-outs. The opportunity is therefore not another AI scheduling app, another backup-worker marketplace, or blockchain-based résumés. The irreducible mechanism has to be different, consistent with the attached instructions to reject decorative AI/blockchain/marketplace recombinations.

1. Reframe the problem

The real job-to-be-done is:

Keep every operationally critical restaurant role covered at shift start, despite individual worker unreliability, without forcing a small restaurant to overstaff or keep a full backup worker on payroll.

This is economically meaningful. The National Restaurant Association's 2026 staffing research says being short even one team member can cost a restaurant hundreds of dollars in a shift, while understaffing also contributes to slower service, lost sales, overtime and employee stress.

The strongest present alternatives are reminders and confirmation systems; employee shift swapping; firing unreliable workers; frantic manager phone trees; on-demand marketplaces; algorithmic last-minute replacement; staffing-agency replacement guarantees; and dedicated paid backups. None fundamentally changes the object being purchased: one worker is still assigned first, and redundancy is mostly bolted on after or beside that assignment.

2. The opportunity gap

The frontier is already crowded in three directions. AI hiring is established: Workstream uses AI for hourly recruiting and reminder calls, including no-show reduction at the interview stage. AI shift recovery is also becoming established: Teambridge describes agents that continuously detect call-outs, search available qualified workers and confirm replacements. Hospitality marketplaces are established too; for example, ShiftChef lets restaurants post shifts and select rated hospitality workers on demand.

Backup staffing itself is prior art. Instawork operates explicit paid backup shifts, and a published patent application describes a primary worker with designated backup workers activated when the primary declines. Blockchain employment marketplaces are also prior art: patents already describe matching a worker to a job, creating a blockchain smart contract, escrow/payment and blockchain work histories or ratings.

So ShiftMesh changes the unit of commerce:

Existing market: restaurant buys Worker A for Shift X.

ShiftMesh: restaurant buys one unit of qualified role coverage for Shift X, and the market decides how much primary and reserve labor capacity is necessary to honor it.

That is the key architectural break.

3. Four mechanisms considered
Mechanism	Core idea	Verdict
Reliability-capacity market	Restaurants purchase primary labor plus dynamically priced reserve capacity sufficient to satisfy a coverage target.	Survives; becomes the core.
Self-guaranteeing crew cells	Groups of 3–5 workers sell a collective promise that one qualified member will cover each booked role.	Useful later, but coordination, peer-pressure and employment issues make it a poor foundation.
Progressive commitment ledger	Replace one confirmation with staged readiness states before the shift so risk is detected earlier.	Useful subsystem, but too close to reminders/confirmation when used alone.
Worker mutual no-show pool	Groups share bonuses for complete coverage and receive extra pay for rescuing one another's shifts.	Rejected as the primary mechanism because group incentives can become coercive and invite adverse selection.

The winning mechanism therefore preserves pre-purchased redundancy, but removes the expensive assumption that every restaurant needs its own dedicated backup.

4. The invention: pooled labor capacity

Imagine 25 independent restaurants inside a 15-minute travel zone. Instead of each restaurant maintaining one emergency worker, they collectively support a small paid reserve pool covering compatible roles.

A Friday-night line-cook shift might therefore be represented internally as:

LINE_COOK · 17:00–23:00 · Zone 14 · primary=1 · coverage_target=99.5% · activation_deadline=16:15 · reserve_capacity=0.21

The 0.21 is important. The restaurant does not necessarily buy another whole worker. ShiftMesh aggregates many restaurants' independent risks and determines how many actual reserve workers the entire zone needs. A reserve worker can economically protect several mutually compatible shifts because only a fraction of primaries are expected to require replacement. The model also increases reserves when failure risks are correlated—for example, severe weather or transit disruption.

This is statistical multiplexing applied to restaurant labor. It borrows the logic of capacity markets, where capacity is procured specifically to make a system reliable rather than merely purchasing the resource when failure has already occurred. Capacity markets are used in electricity systems for exactly that separation between ordinary production and reliability capacity.

The AI-agent layer

Every participant gets a bounded agent.

The Restaurant Agent reads schedules, sales forecasts and the manager's rules. It decides which positions are critical, submits Coverage Contracts, and has a spending ceiling such as “never spend more than $18 protecting this shift without asking me.”

The Worker Delegate represents the worker rather than the restaurant. The worker sets minimum pay, roles, locations, travel radius, maximum hours, reserve windows and other preferences. Within those limits, the agent can negotiate primary shifts or paid reserve blocks without the worker endlessly checking notifications.

The Clearing Agent prices correlated no-show risk, travel time, skills and available reserve capacity and clears the local market. It is optimizing coverage probability per dollar, rather than merely ranking applicants.

The Continuity Agent operates after hiring. During a new hire's first weeks, it can attach more backup capacity to their shifts. As actual attendance evidence accumulates, the expensive redundancy can shrink. Thus the system protects a restaurant precisely during the period when a résumé and interview give the least evidence about whether the person will actually show up.

5. How a shift works

Suppose a small restaurant hires Maya as a new line cook.

The manager schedules Maya Friday from 5 p.m. to 11 p.m. Instead of the schedule ending there, the Restaurant Agent converts the shift into a Coverage Contract. It purchases a small amount of line-cook reserve capacity from the neighborhood mesh.

Before the shift, Maya receives a few low-friction readiness checkpoints. These are not invasive surveillance. A worker can simply confirm; optional transit/ETA information can strengthen confidence without becoming a permanent employment record.

If the readiness state deteriorates sufficiently early, the Continuity Agent exercises a reserve option. The reserve worker is promoted to the shift before the restaurant enters crisis mode. Maya's absence is handled as an employment matter separately; the restaurant's ability to serve dinner no longer depends on resolving that personnel issue first.

The business model therefore separates two questions that restaurants currently conflate:

“Is Maya a good employee?” is a hiring/management question.

“Will I have a line cook at 5 p.m.?” becomes an infrastructure-reliability question.

That separation is the central invention.

6. Why blockchain actually belongs here

Blockchain should be nearly invisible to users. There is no restaurant coin, no speculative token and no requirement for workers to receive cryptocurrency.

Its first necessary job is cross-party settlement. Coverage may eventually be supplied by ShiftMesh workers, independent staffing firms, worker co-ops and neighboring restaurant groups. A smart contract records who sold reserve capacity, who exercised it, who worked and whether the contracted coverage obligation was satisfied. Restaurant-funded coverage premiums, reserve compensation and automatic service credits can settle against the same auditable contract.

Its second job is portable, worker-controlled evidence. A completed shift can generate a W3C Verifiable Credential signed by the venue or time-clock authority. W3C's Verifiable Credentials 2.0 is already a web standard for cryptographically secure, machine-verifiable credentials. The blockchain stores credential/status anchors rather than a person's employment history.

Crucially, ShiftMesh should never put raw no-shows, GPS trails, manager complaints or a permanent negative reputation score on-chain. Workers hold their credentials and selectively prove things such as “completed at least 18 verified line-cook shifts recently.” Blockchain résumé and employment-reputation mechanisms already exist in research and patents, so merely putting work history on-chain would be neither new nor desirable.

7. Marketplace and economic design

Restaurants buy three things through one interface: ordinary hiring, temporary labor and Guaranteed Coverage. The distinctive revenue line is the coverage premium.

A restaurant might pay the scheduled wage normally plus a small variable coverage premium determined by role scarcity, time, location and desired reliability. Those premiums from dozens of restaurants finance paid reserve blocks. The platform keeps a spread for operating the risk pool and also puts part into a guarantee reserve.

Workers never stake wages and never lose earned pay because someone else fails. A worker taking a reserve block receives compensation for that availability, plus an activation premium when dispatched. A primary worker can also receive a small additive completion bonus. Incentives are therefore positive and pre-funded, rather than punitive.

If ShiftMesh sells “guaranteed coverage” and then fails to cover the role, part of the smart-contract escrow automatically becomes a restaurant service credit. That changes the platform's incentives dramatically: ordinary recruiting software is paid when it produces applicants or hires; ShiftMesh increasingly gets paid for operational continuity.

8. The important legal boundary

The system should not depend on unpaid, tightly constrained standby. U.S. Department of Labor guidance distinguishes workers who are free to use waiting time for themselves from workers whose waiting time is sufficiently controlled by the employer; additional on-call restrictions can make that time compensable.

For the initial U.S. model, the cleanest design is therefore for reserve-pool workers to be properly paid during reserve blocks and for ShiftMesh or a licensed staffing partner to act as employer of record where appropriate. Worker classification cannot simply be declared in an app: both federal labor guidance and IRS guidance look at the substance of control and economic relationship. State-specific scheduling, reporting-time, staffing and employment rules would still need jurisdiction-by-jurisdiction treatment.

9. Product experience

For the restaurant owner, ShiftMesh should feel dramatically simpler than its architecture.

The schedule would visually show, for example:

Friday dinner
Line cook — Maya — Covered ✓
Server — Andre — Covered ✓
Dishwasher — Open — Agent filling
Bartender — Sam — Unprotected: add coverage for $11

The owner never chooses blockchain networks or reserve workers. They choose an operational promise: “Protect critical shifts.”

The worker app is equally different from normal gig apps. Instead of constantly hunting individual jobs, a worker can tell their Delegate:

Line cook or prep. At least $21/hour. Within 5 miles. No Tuesdays. I’m willing to sell reserve availability Friday 4–10 p.m. if the reserve payment is at least $35.

The agent participates in the market under those rules and returns only commitments requiring human attention.

10. The defensible core

The innovation delta is:

After removing the AI branding, blockchain, résumé features and conventional gig marketplace, ShiftMesh still converts a restaurant shift from a single-worker assignment into a market-cleared reliability contract backed by statistically pooled, paid reserve labor capacity across nearby businesses.

AI is necessary because continually clearing thousands of conditional labor commitments, correlated absence risks and travel constraints manually would be impractical.

The marketplace is necessary because pooling only works when many independent restaurants and workers share capacity.

Blockchain becomes useful when the reserve market crosses organizational boundaries and needs portable credentials and neutral contractual settlement; it is not the source of the staffing advantage.

That is why the architecture survives removal of the buzzwords.

Honest verdict

Potentially novel mechanism, with material prior-art uncertainty.

Paid backups, backup-worker networks, replacement guarantees, AI replacement agents, blockchain labor marketplaces and blockchain employment credentials are all already disclosed or deployed. What I did not find in the searched product and patent landscape was a close restaurant-staffing match whose fundamental product is a market-cleared coverage obligation backed by fractional, geographically pooled reserve labor capacity, with autonomous agent negotiation and cross-provider cryptographic settlement.

The concept loses its reason to exist if pooled reserve capacity cannot cover shifts materially more economically than dedicated backups or reactive emergency hiring. It also fails if enough compatible workers cannot be concentrated into small geographic zones, or if reserve constraints make the labor model legally or economically unattractive. Those are the decisive kill conditions.

The product I would build is therefore ShiftMesh: “Hire the person. Guarantee the role.” Its initial wedge should be independent restaurants clustered tightly enough to share a line-cook, prep/dish and FOH-support reserve pool; the long-term platform becomes a local market for labor reliability itself, rather than another marketplace selling résumés or individual shifts.

