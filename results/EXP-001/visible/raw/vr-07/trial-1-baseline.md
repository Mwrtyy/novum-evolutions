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
