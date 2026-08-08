# EXP-001 Blind Judge — vr-07-t1-domain_or_generalist

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
  "pair_id": "vr-07-t1",
  "evaluator_id": "vr-07-t1-domain_or_generalist",
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

# Blind pair vr-07-t1

## Task

Create a revolutionary hiring platform for small restaurants using AI agents, blockchain, and a marketplace. The main operational bottleneck is that hired workers frequently do not show up for scheduled shifts.

## Output A

Using the uploaded NOVUM requirement to end with a precise, falsifiable invention candidate rather than a feature bundle, the strongest design is below.

SHIFTGRID
A reliability-underwritten hiring marketplace for small restaurants

Core invention: restaurants stop hiring a person for a shift and start buying a staffed-position commitment.

Every critical scheduled position is backed by a neighborhood labor grid. Cross-trained workers who would otherwise be doing interruptible prep, cleaning, inventory, dish, runner, or other movable work can be automatically rerouted when another restaurant suffers a no-show.

The conceptual transfer is from electricity grids and preemptible cloud computing into restaurant labor:

Firm capacity: “I need a line cook at 18:00 and this position cannot disappear.”
Interruptible capacity: “I need four hours of prep today, but its exact timing can move.”
Reserve capacity: workers already being paid and doing productive work who can be rerouted.
AI agents: continually match and rebalance those capacity classes.
Blockchain: locks capacity so it cannot be promised twice and settles transfers between independent restaurants.
Marketplace: simultaneously supports permanent hiring, ordinary shifts, and reserve-grid work.

The fundamental unit of the system is therefore reliable labor capacity, not an applicant.

1. Problem reframing

Assumption: initial launch is for dense U.S. restaurant markets and common hourly roles rather than highly specialized chefs or management.

Achieve near-continuous coverage of critical restaurant positions for small operators, despite unpredictable worker no-shows, while remaining cheaper than keeping an idle backup worker and without financially punishing workers.

The strongest current approaches attack pieces of the problem:

Workstream automates hourly recruiting, reminders, screening and interview scheduling. Qwick and Instawork use suspensions and reliability consequences after cancellations/no-shows. Instawork goes further and offers actual backup shifts, but backup workers must arrive ready to work and can receive four hours of pay even if they are not ultimately required.

That exposes the key contradiction:

A restaurant wants guaranteed spare capacity, but paying a second worker to stand idle destroys the economics.

ShiftGrid attempts to remove that contradiction by making reserve labor productive until needed elsewhere.

2. Frontier and opportunity gap
Saturated

AI recruiting and reminders. Already deployed in hourly-work systems such as Workstream.

Punishment-based reliability systems. Qwick and Instawork already suspend workers for no-shows or repeated late cancellations.

AI no-show prediction. Patent literature already describes ML systems predicting whether an individual worker will show up for a staffing assignment.

Automated substitute matching. Automated replacement-worker systems are decades old, and newer patents describe designated backup-worker networks.

Blockchain employment records. Blockchain attendance, employment reputation and employment-contract systems have also been disclosed.

Emerging

AI agents are beginning to autonomously procure human labor, while hospitality software is already moving toward AI-triggered replacement from float pools.

Cross-trained float pools have substantial precedent in healthcare, including geographic “market float pools,” and recent operations research studies their optimal sizing.

Neglected gap

The interesting space is the combination:

A network of independent small businesses buying two classes of labor—firm and interruptible—so productive workers can function as shared reserve capacity, with automated multi-business clearing when that capacity is preempted.

That is materially different from simply finding a substitute after somebody disappears.

3. Assumption graph

The causal chain is:

Restaurant tasks differ in urgency
→ some work can be moved by 30–120 minutes without damaging service
→ those tasks can host productive reserve workers
→ multiple nearby restaurants pool that reserve
→ individual no-shows become statistically absorbable across the network.

The weakest assumptions are not AI capability.

They are:

enough restaurant work is genuinely interruptible;
enough restaurants exist within a short travel radius;
workers can be standardized across selected roles;
emergency demand is not so correlated that the entire reserve grid fails simultaneously;
the economics of paid travel and reserve staffing remain attractive.

That last point is the primary kill risk.

4. Four mechanically distinct candidates
Candidate	Mechanism	Assumption replaced	Why absence decreases
A. ShiftGrid	Firm versus interruptible labor capacity across a neighborhood	Every restaurant needs its own backup	Pool capacity → preempt low-criticality work → reroute worker
B. Coverage Rights Market	Restaurants reserve qualified workers for defined response windows	Backup labor must be scheduled as a full extra shift	Buy reservation → activate only if needed → pay activation premium
C. Crew Mutuals	3–5 workers collectively guarantee a coverage obligation	Employment commitments must be individual	Member unavailable → crew self-replaces → crew retains reliability benefits
D. Commitment Agent	Worker AI checks schedule conflicts, travel feasibility and commitment state before accepting	A worker clicking “accept” is meaningful proof of feasibility	detect impossible commitment → decline/renegotiate → avoid foreseeable no-show

Their signatures are substantially different:

A: resource pooling + preemption.
B: reservation-market incentive.
C: collective/social guarantee.
D: information and control.
5. Anti-fake-novelty verdict

Several tempting ideas should be discarded.

“AI predicts who will no-show.” Too close to existing staffing ML prior art.

“Blockchain stores worker attendance.” Known mechanism.

“AI instantly calls a replacement.” Existing hospitality products and substitute systems already approach this.

“Every shift gets a backup worker.” Operationally effective but economically expensive; Instawork already has an adjacent model.

So, after removing the buzzwords, the innovation delta of ShiftGrid is:

Convert low-urgency productive restaurant work into economically useful reserve capacity that can be preempted across independent restaurants to satisfy firm staffing commitments.

AI, blockchain and the marketplace exist to make that mechanism operate; they are not themselves the invention.

6. Red-team and rejected mechanisms
No-show deposits from workers — reject

Do not require workers to stake cash or cryptocurrency. It disproportionately excludes workers with less liquidity, creates wage/legal complications and converts a reliability problem into punitive finance.

Permanent immutable reliability score — reject

Do not put subjective ratings or personal employment histories on-chain. Third-party algorithmic worker scores used for employment decisions can trigger Fair Credit Reporting Act obligations including accuracy, disclosure and dispute rights.

Instead, the worker owns revocable attestations, while the chain holds hashes and credential status—not raw employment records.

Unpaid standby — reject

Reserve workers should be performing paid work, not sitting around unpaid subject to severe restrictions. U.S. wage law treats some waiting/on-call arrangements as compensable depending on how constrained the employee is.

Gig-classify everyone — reject

The system should not depend on classifying restaurant labor as independent contracting. Worker status remains legally fact-specific, and federal classification rules are currently an active regulatory area.

Preferred launch model: ShiftGrid or a licensed staffing partner employs the reserve-grid workforce as W-2 workers; ordinary permanent hires can remain employees of the individual restaurants.

7. Evolution into the strongest architecture
Mutation 1: idle reserve → productive reserve

The initial reservation-market concept still wasted labor capacity.

Replace “wait nearby in case somebody fails to arrive” with:

Work a real, explicitly interruptible assignment until the grid needs you.

A restaurant receiving interruptible labor gets a cheaper service class. In exchange, it agrees that the worker may be reassigned within preset rules.

This removes most of the waste inherent in conventional backup staffing.

Mutation 2: predictive worker scoring → capacity prediction

Do not make the AI's primary question:

“Is Maria unreliable?”

Make it:

“How much reserve capacity does the grid need between 17:00 and 20:00?”

The system can use aggregate historical absence, weather, transit disruption, role scarcity and real-time voluntary confirmations to size reserves without turning an opaque prediction about one person's character into an employment gate.

That is both operationally cleaner and less dangerous.

8. The winning platform
ShiftGrid has four markets
1. Permanent Hire Market

Restaurants publish jobs.

A Restaurant Agent specifies wage, hours, required skills, availability and working conditions.

A Worker Agent represents the worker's constraints: minimum wage, commute radius, schedule, preferred roles, hours and employer preferences.

The agents negotiate matches instead of forcing applicants through repeated forms.

2. Firm Shift Market

A restaurant marks a scheduled role:

FIRM — must be covered.

Example:

Saturday
17:00–23:00
Grill
Level 2
Maximum replacement arrival: 20 minutes

ShiftGrid prices the required reserve capacity.

3. Interruptible Work Market

Restaurants submit productive work that can tolerate displacement:

prep vegetables;
portion ingredients;
dish;
deep clean;
organize inventory;
receive stock;
folding/packaging;
basic kitchen production.

They pay less because capacity can be preempted.

4. Grid Worker Market

Cross-trained workers select:

approved roles;
geographic zone;
availability;
wage floor;
maximum travel;
preferred restaurants;
whether they accept Grid assignments.

They receive guaranteed pay for the scheduled block whether they remain at their starting location or are rerouted.

9. How one Friday-night no-show works

Assume Restaurant A has a critical 18:00 dishwasher shift.

Restaurant A's agent purchases Firm Coverage.

At 17:20 the system determines that the primary worker has cancelled.

Three blocks away, Grid Worker Elena is doing an interruptible prep assignment at Restaurant B.

The Grid Agent checks:

Skill: dishwasher certified ✓
Travel: 8 minutes ✓
Worker's agreed zone: ✓
Restaurant A approved: ✓
Restaurant B minimum staffing after removal: ✓
capacity already committed elsewhere: no ✓

Elena receives the reassignment.

Her travel remains paid.

Restaurant B automatically receives a preemption credit and its unfinished prep task is placed back into the marketplace.

Restaurant A receives Elena.

No manager posts a frantic job, calls six employees, or waits to discover whether a marketplace worker accepts.

The system has treated the no-show like a grid outage and rerouted already-online capacity.

10. The AI-agent architecture
Restaurant Agent

Maintains:

staffing requirements;
firm versus interruptible tasks;
wage budget;
skill requirements;
critical service periods;
scheduling-system integration.

Its objective is not “hire cheapest.”

It optimizes:

staffing reliability × cost × worker compatibility.

Worker Agent

Acts exclusively for the worker.

It stores locally/private-off-chain:

availability;
commute preferences;
wage floor;
skills;
workplace exclusions;
desired hours;
accepted commitments.

It may automatically reject an assignment that creates an impossible commute or double booking.

Grid Agent

Continuously solves:

Which workers should remain where so that the network can absorb the next plausible staffing failure with minimum disruption?

It controls capacity, not employment rights.

Compliance Agent

Checks:

required certifications;
overtime;
breaks;
travel-pay requirements;
local scheduling requirements;
role restrictions;
worker accommodations.

AI employment tools also need accommodation and anti-discrimination controls; the EEOC has specifically warned that algorithmic systems can unlawfully screen out people with disabilities.

Human override remains available.

11. Why the blockchain actually exists

The blockchain should not run resumes, AI inference or GPS tracking.

Its job is much narrower.

A. Capacity locking

A worker's 18:00–22:00 Grid capacity can be committed once.

When reserved, a cryptographic capacity lock prevents Restaurant A, Restaurant B or another marketplace from simultaneously representing that exact capacity as guaranteed.

It solves a double-spend problem for labor commitments.

B. Multi-restaurant clearing

If Restaurant B's worker is preempted to Restaurant A:

Restaurant A incurs emergency capacity charge;
Restaurant B receives interruption credit;
worker receives correct pay/travel/surge;
ShiftGrid receives its clearing fee.

Smart contracts provide a common state machine for these independent parties.

C. Portable credentials

Restaurants issue signed attestations such as:

“Completed approved grill-station training.”

or

“Completed shift #… as scheduled.”

Raw information remains off-chain. The chain contains issuer identity, credential hash and revocation status.

D. Open-network future

A Homebase-scheduled restaurant, a 7shifts restaurant and another staffing marketplace could eventually reserve capacity through the same protocol without giving one software company complete control of the trust layer.

That is the strongest reason for blockchain.

If ShiftGrid remains permanently a closed single-company marketplace, a conventional database is the simpler architecture and the blockchain should be removed.

12. Marketplace flywheel

The platform creates an unusual positive feedback loop:

More restaurants
→ more interruptible work
→ reserve workers stay productive
→ cheaper reserve capacity
→ more firm positions can be guaranteed
→ restaurants experience less staffing fragility
→ more restaurants join.

And:

More workers
→ more geographic/skill coverage
→ smaller reserve requirements
→ more paid work opportunities
→ better supply density.

This is substantially stronger than a normal job board's “more listings → more applicants” network effect.

13. Business model

The pricing object should be reliability, not applicant volume.

An illustrative structure:

Core hiring/scheduling: $99–$199 per location/month.
Firm Coverage: small per-shift reservation charge based on role, geography, time and reserve scarcity.
Emergency reassignment: percentage markup on dispatched Grid labor.
Interruptible labor: lower markup than guaranteed labor.
Workers: no membership fee and no token purchase.

Small restaurants should be able to activate coverage only for the handful of shifts whose failure would seriously damage service.

Friday grill? Firm.

Tuesday afternoon prep? Interruptible.

14. Initial operating boundary

Do not begin with every restaurant role.

Start where transfer friction is lowest:

Strong candidates

dishwasher;
prep cook;
food runner;
counter/cashier;
basic line stations;
porter/utility.

Later

experienced line cook;
barista;
server.

Initially exclude or tightly constrain

executive chefs;
restaurant managers;
specialized pastry;
alcohol-serving roles where jurisdiction-specific credentials matter;
highly restaurant-specific tasting-menu stations.

Cross-training itself is known to improve workforce flexibility, but operational research also shows the importance of differences in productivity between primary and cross-trained workers.

So ShiftGrid needs a standardized role-competency system rather than pretending every “cook” is interchangeable.

15. Smallest defensible prototype

Launch one geographic cell:

10–15 independent restaurants within roughly a 10-minute travel radius.

20–30 Grid workers.

Only four standardized roles.

Integrate existing schedules rather than replacing them.

For the first implementation, use the blockchain only for:

capacity reservation;
reassignment settlement;
credential hashes.

Do not put worker PII, exact location or manager reviews on-chain.

Kill criteria

The mechanism is worth continuing only if real operating incidents show that:

qualified reserve capacity can usually reach the affected restaurant within its contracted response window;
host restaurants can tolerate preemption without creating a second staffing emergency;
workers willingly accept the Grid-work model at sustainable compensation;
total reserve cost is materially below keeping dedicated idle backup labor.

If the model requires nearly one reserve worker for every firm worker, the core economic claim fails.

If a dense restaurant cluster can pool significantly less reserve capacity while maintaining coverage, the central mechanism survives.

16. Confidence profile
Dimension	Current view /10
Problem value	9
Mechanism differentiation	7
Potential advantage magnitude	8
Technical feasibility	8
Adoption feasibility	6
Falsifiability	9
Defensibility	7
Evidence confidence	5
Fatal-risk severity	7

The two numbers most likely to move are adoption feasibility and fatal-risk severity. Restaurant density, worker acceptance, staffing-law structure and the percentage of truly interruptible work will determine them.

Honest verdict
Differentiated architecture; potentially novel mechanism, prior-art status unverified

What is well supported is that the component technologies themselves are not new: AI staffing, no-show prediction, substitute fulfillment, float pools, labor marketplaces and blockchain employment credentials all have precedent.

What appears differentiated in the search performed here is the market architecture connecting independent restaurants through firm versus interruptible labor capacity, where productive workers serve as a preemptible neighborhood reserve and multi-party commitments are automatically cleared.

The largest unresolved prior-art region is workforce-management and staffing patents involving float pools, preemptible worker allocation, shared labor pools and capacity reservation. Finding an existing system with substantially that same causal mechanism would downgrade the novelty claim.

But even if that maximal novelty claim fails, ShiftGrid remains a substantially stronger product thesis than an AI recruiting app with blockchain credentials because it directly restructures the operational system that makes a no-show catastrophic.

## Output B

RELAY — an attendance-capacity market for small restaurants

The platform should not be another job board with AI matching. The bottleneck is certainty that a qualified human will physically be present when service starts. Following the uploaded NOVUM method, I treated AI agents, blockchain, and a marketplace as constraints rather than sources of novelty; the irreducible mechanism has to change how staffing reliability is produced.

1. Reframe the problem

Challenge: Achieve near-guaranteed role coverage at shift start for small restaurants, despite individual cancellations and no-shows, without requiring restaurants to employ excessive spare staff or requiring unused backup workers to travel to the restaurant.

Hiring is therefore only half the product. RELAY turns every hire into part of a continuously hedged staffing system.

This matters because much of the obvious frontier is already occupied. Qwick automatically matches hospitality workers using skills, history, reliability, attendance and millions of prior shifts. Instawork offers backup workers, including paid backup shifts where a worker can receive four hours of pay even when they are not ultimately needed. WorkWhile goes further and pays people to remain on standby away from the job site. Other hospitality products already advertise standby or reserve pools.

Likewise, predicting whether a temporary worker will show up has already been disclosed in patent literature, as have automated backup staffing and blockchain-based work-history credentials. Those cannot be the invention.

2. The core invention: the Attendance Capacity Exchange

RELAY converts a restaurant shift from a binary promise—“Alex says they will come”—into a portfolio of executable labor capacity.

A restaurant doesn't buy a backup worker. It buys attendance capacity for a particular role, location and time window.

For each critical shift, the system creates a primary assignment plus a dynamically sized pool of conditional capacity. Nearby qualified workers receive small payments for granting RELAY an activation option over a defined portion of their availability. They stay wherever they are; they travel only if activated.

The significant difference is that these reserves are pooled across many nearby restaurants rather than attached one-for-one to individual shifts. Ten restaurants with twenty statistically independent staffing risks might require only a much smaller shared reserve pool. The exact reserve requirement changes continuously with correlated attendance risk, geography, role interchangeability and travel time.

The conceptual transfer comes from capacity markets: instead of paying only for electricity actually generated, capacity markets pay resources for being available when the system needs them. RELAY applies that underlying reliability mechanism to perishable human availability, with worker-protective controls.

3. How RELAY works
Moment	System behavior
Hire	Restaurant owner tells an AI agent something like “I need a line cook Tues–Sat evenings.” The agent searches permanent candidates and marketplace workers, checks credentials, negotiates constraints and builds the recurring schedule.
Commit	The hired worker's agent accepts specific recurring shifts. Each accepted shift creates a cryptographic time-bound commitment.
Hedge	The Restaurant Agent purchases enough qualified reserve capacity from the neighborhood Attendance Capacity Exchange to bring the shift above the restaurant's selected coverage threshold.
Rebalance	As the shift approaches, agents continuously recalculate feasible coverage from confirmations, travel feasibility, cancellations, past behavior and reserve availability.
Activate	If coverage deteriorates, RELAY exercises a reserve commitment before the worker's activation deadline. That person becomes the replacement and receives the normal shift compensation.
Release	Unneeded reserve workers are automatically released and receive their availability payment.
Verify	Arrival is proven through a paired restaurant/worker check-in rather than manager ratings alone.
Record	Worker and restaurant each receive cryptographically verifiable records of what actually happened.

So the platform is simultaneously a hiring system, workforce scheduler, labor marketplace and reliability market.

4. Three AI agents, with conflicting responsibilities

Restaurant Agent. This agent represents the restaurant rather than simply recommending applicants. It forecasts required roles, recruits permanent employees, purchases reserve capacity, activates replacements, finds emergency spot labor and minimizes staffing cost subject to a restaurant-defined reliability requirement.

Worker Agent. Every worker gets an agent whose job is explicitly not to maximize restaurant coverage. It protects the worker's schedule, minimum compensation, commute radius, preferred roles, maximum weekly hours and activation notice. It can negotiate both regular shifts and paid reserve windows. This makes the system bilateral rather than an employer-controlled allocation algorithm.

Market-Clearing Agent. This agent sees the aggregate supply-demand graph for a neighborhood. It determines how much reserve capacity is actually needed, groups interchangeable skills, prevents impossible assignments and continuously clears reserve and emergency markets.

That separation matters: one omnipotent scheduling AI would optimize workers into exhaustion. RELAY instead creates algorithmic counterparties with different objectives.

5. Where blockchain is actually necessary

The blockchain is not a database for résumés, employee reviews or personal location history.

Its useful role is a neutral commitment and settlement layer shared by restaurants, workers and eventually competing staffing platforms.

A worker's agent cannot secretly sell exclusive availability for Tuesday 7–10 p.m. to three independent restaurants, because the time commitment is cryptographically locked. A restaurant cannot deny that it activated a reserve worker after the fact. Reservation fees and activation terms are timestamped. Credential issuers and revocations are independently checkable.

Sensitive information stays off-chain. Workers hold a Presence Passport built on W3C Verifiable Credentials 2.0, which became a W3C Recommendation in May 2025 and is specifically designed for cryptographically secure, privacy-respecting, machine-verifiable credentials.

An attendance credential might reveal only: “holder completed 47 verified kitchen shifts in the last 180 days; 45 began within the agreed arrival window.” It need not reveal restaurant names, home address, exact historical locations or wages.

RELAY should also avoid turning this into a single public five-star reputation score. Research on portable labor-market reputation indicates that portability can concentrate demand disproportionately around workers who already have large volumes of ratings. The better primitive is therefore portable evidence with contextual matching, not a universal leaderboard.

6. Presence proof: blockchain cannot solve the physical world

A smart contract cannot independently know that somebody actually walked into a kitchen.

RELAY therefore uses a hybrid oracle. At arrival, the worker's phone and restaurant POS/tablet jointly sign a fresh nonce using QR, NFC or Bluetooth proximity. The matching signatures produce the attendance receipt. Managers can dispute it, but neither party can silently manufacture the other's signature.

Only the receipt hash and credential status need anchoring on-chain.

That constraint is important because research on blockchain commerce shows that purely on-chain settlement for physical-world performance cannot magically eliminate the need for trusted evidence or arbitration.

7. The marketplace becomes progressively more powerful

Initially, RELAY can clear reserve capacity inside its own worker population.

Once enough restaurants join a neighborhood, it becomes a local staffing grid. A dishwasher employed 25 hours per week by Restaurant A might voluntarily sell two reserve windows through their Worker Agent. Restaurant B's cook might do the same. Independent workers add more reserve capacity. Restaurants effectively share redundancy without sharing employees manually.

Then comes a spot market. If three simultaneous cancellations exhaust the reserve pool, restaurant agents automatically bid for emergency qualified labor. Workers see the premium and their agents decide whether accepting it fits their rules.

Eventually the blockchain commitment protocol can be opened so existing staffing companies can participate. RELAY then stops needing to own the entire labor supply; it becomes the clearing infrastructure connecting restaurant schedules, workers and staffing networks.

8. The hiring product itself

The owner experience stays radically simple.

An owner says:

“I need two dependable prep cooks. Wednesday through Sunday, 2–10. I care more about attendance than fine-dining experience.”

RELAY's agent translates that into skills, schedule, compensation range, commute constraints and staffing-risk requirements. Candidates' Worker Agents negotiate against it. Interviews become targeted to unresolved questions rather than generic screening.

When someone is hired, RELAY automatically protects the schedule with the neighborhood capacity market. Thus the product doesn't merely answer “Who should I hire?” It answers the operationally more valuable question: “Who will cover this kitchen even when the person I hired unexpectedly cannot?”

9. Worker incentives are deliberately different from conventional gig platforms

There should be no worker deposit, crypto stake or financial slashing for illness or emergencies.

Reliability is created by positive economics: workers can earn ordinary wages plus paid availability income. If they realize they cannot attend, releasing a commitment early lets the system hedge the shift while preserving a factual record that distinguishes an early cancellation from a no-call/no-show.

The restaurant has symmetrical obligations. Once a reserve is activated, the restaurant cannot cancel without the contractually defined worker protection. Restaurant behavior—late cancellations, inaccurate job descriptions, payment problems and excessive early sends—is credentialed too.

Trust becomes two-sided.

10. Innovation delta

Strip away the terminology:

AI matching is known. Paid standby is known. Reserve pools are known. No-show prediction is known. Labor marketplaces are known. Blockchain employment credentials are known.

The irreducible difference in RELAY is:

A geographically pooled market in cryptographically exclusive, time-bounded human availability capacity, continuously purchased and exercised by bilateral AI agents to hedge the attendance risk of permanent restaurant schedules.

That is the part worth protecting and developing.

The closest mechanisms found in this scan cover individual backup workers, standby pools, no-show prediction and decentralized work histories, but I did not find a close disclosed system combining cross-restaurant statistical reserve pooling + executable availability capacity + autonomous bilateral agent clearing + a shared conflict-prevention ledger. That supports a potentially novel mechanism classification, not a claim of universal novelty. The NOVUM instructions explicitly require this distinction between meaningful mechanism novelty and merely adding AI, decentralization or blockchain to existing products.

11. Boundary conditions that can kill the concept

The central mechanism does not survive if geographically pooled reserve capacity costs essentially the same as attaching a paid backup to every critical shift; if sufficient workers will not sell time-bounded reserve availability on worker-friendly terms; if correlations between restaurant no-shows are so high that meaningful pooling disappears; or if jurisdiction-specific employment rules make flexible reserve commitments operationally uneconomic.

Those are features, not weaknesses, of the invention definition: the platform's claim is specifically that staffing uncertainty can be pooled and traded as capacity more efficiently than restaurants can absorb it independently.

If that holds, RELAY is no longer primarily a recruiting marketplace. It becomes a reliability layer for the restaurant labor market.

