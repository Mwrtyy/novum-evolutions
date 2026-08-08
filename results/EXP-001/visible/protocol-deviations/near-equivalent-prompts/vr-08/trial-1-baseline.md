Decision

Do not build or invent a new scheduling mechanism. The strongest solution here is a deliberately simple, paper-first banded schedule with protected same-day capacity. The NOVUM standard allows an honest no-go when a new mechanism cannot justify itself on novelty, advantage, constraint fit, and falsifiability; that is the appropriate conclusion here.

Call the workflow Banded Reserve Scheduling (BRS) for convenience, but the name is not a novelty claim.

1. Problem reframing

Assuming the clinic handles a mixture of routine follow-ups, urgent visits, and walk-ins:

Achieve a manageable daily patient flow for a rural clinic despite power outages, unreliable connectivity, uncertain patient arrival times, one low-end PC, and no additional staff, outperforming a conventional exact-time appointment book or pure walk-in queue without making technology a point of failure.

The key contradiction is clinic predictability versus patient-arrival uncertainty. Rural and remote health facilities disproportionately face unreliable electricity, so making the PC or cloud the authoritative schedule would reproduce the infrastructure problem inside the scheduling system.

Distance, transportation problems, and longer booking lead times are also associated with missed appointments, which makes rigid, far-ahead exact-time booking particularly poorly matched to this environment.

2. Frontier and opportunity gap

The obvious alternatives are already well explored. Advanced/open-access scheduling has substantial primary-care literature; a 2026 systematic review found appointment waiting time decreased in all 23 included studies reporting that measure, although the model has implementation and continuity considerations. Block scheduling is also established rather than novel. More sophisticated approaches now include predictive double-booking and optimization algorithms, but they add data, computation, maintenance, and operational assumptions that this clinic does not possess.

Likewise, offline/local health software already exists. OpenMRS can run as a standalone local installation, and Bahmni is designed for low-resource environments, but installing a clinical platform merely to improve this clinic's appointment control rule is unnecessary complexity.

The neglected opportunity is therefore not new software. It is making the paper schedule itself resilient to uncertain arrivals, urgent demand, and outages.

3. Directions rejected
Direction	Decision	Constraint collision
Cloud scheduler	Reject	Connectivity becomes operational dependency
Local EHR/scheduling server	Reject as primary scheduler	More maintenance and power dependence than the problem warrants
Exact 10–20 minute appointments	Reject as default	Treats rural travel and arrival time as predictable
Pure first-come, first-served	Reject	Gives the clinic almost no control over workload concentration
Routine double-booking	Reject	Converts no-show uncertainty into potentially severe crowding
Patient-specific no-show prediction	Reject	Requires data upkeep for a problem solvable with a general rule
Full same-day/open access	Constrain	Useful principle, but too aggressive for chronic follow-up and limited capacity
Geographic/village batching	Conditional only	Useful only where travel patterns genuinely cluster
Banded schedule + protected reserve	Keep	Works without power, internet, additional equipment, or additional staff
4. The workflow

Replace most exact appointment times with three arrival bands, adjusted to the clinic's actual opening hours. For example: early morning, late morning, and afternoon.

Each band gets a fixed number of capacity marks based initially on however many patients the clinic already regards as a normal workload. Only about 80% of those marks are pre-bookable. The remaining roughly 20% are visibly marked R for same-day urgent demand, unavoidable late arrivals, and clinically appropriate walk-ins.

A paper page might look like this:

Band	Pre-booked capacity	Protected reserve	Serving rule
Early	8 marks	2 R	Urgency, then current-band arrivals
Late morning	8 marks	2 R	Urgency, then current-band arrivals
Afternoon	8 marks	2 R	Urgency, then current-band arrivals

Those numbers are illustrative; reuse the clinic's existing daily capacity rather than increasing bookings.

Patients receive a date plus a window, not a falsely precise promise: for example, “Tuesday, early-morning band; arrive between 08:00 and 09:30.” Clinical emergencies are never governed by the booking order.

Reserve capacity remains protected through most of the band. Near the end of the band, an unused reserve mark may be assigned to an already-present routine walk-in or spillover patient. There is no speculative double-booking.

If visit durations differ substantially and predictably, add one small refinement: a normal visit consumes one capacity mark and a known long procedure consumes two. If durations are broadly similar, do not add this refinement. Headcount is simpler.

5. Power-outage architecture

The paper book is the sole operational source of truth. It contains only the information needed to identify the patient, the date/band, and capacity consumed; sensitive clinical detail stays in the proper clinical record.

The PC becomes a noncritical shadow tool. When electricity is available it may hold a simple local spreadsheet for printing blank weekly templates and recording aggregate figures. Nobody has to reconcile two active appointment databases, and no synchronization event is required before the clinic can continue working.

A blackout therefore causes exactly zero scheduling mode change.

This is the important architectural improvement: computing is moved out of the critical path rather than made more outage-resistant.

6. Control policy

Within each band, use the same deterministic priority rule every day:

clinical urgency → patient booked for the current band → unresolved patient from an earlier band → routine walk-in.

Patients arriving substantially before their assigned band do not automatically jump the queue. Patients arriving late move into reserve/spillover capacity rather than forcing every subsequent appointment to slide.

For long-horizon follow-ups, keep the clinically required future booking, but assign a band instead of an exact minute whenever precise timing is unnecessary. This preserves continuity without adopting an extreme all-same-day model; earlier research on advanced access has noted the risk of chronic patients being lost to follow-up when pre-scheduled care is minimized too aggressively.

7. Failure boundaries

Banded scheduling is inappropriate for visits whose safety genuinely depends on precise timing—for example, procedures requiring tightly coordinated preparation, medication timing, external transport, laboratory availability, or another clinician. Those remain fixed-time appointments.

The system also has a simple operational kill condition: if a band repeatedly ends with a substantial unresolved queue, do not add software or overbooking. Reduce that band's pre-bookable capacity, shift capacity to another band, or split the overloaded band. Conversely, persistently unused reserve can be reduced modestly. The paper structure remains unchanged.

8. Innovation delta and verdict

After stripping away terminology, the architecture is simply:

Make arrival windows rather than exact times the default, permanently protect a small portion of each window from advance booking, and keep the authoritative schedule on paper so electrical or network state cannot alter clinic operations.

I found close precedents for its individual mechanisms—block scheduling, advanced access, reserved capacity, offline/local systems, and flexible appointment windows. I therefore would not claim a new mechanism. The combination is well fitted to the stated operating regime, but novelty would be branding rather than a defensible causal invention.

NOVUM verdict: no-go on inventing something new. Adopt the simpler Banded Reserve Scheduling workflow. Its strongest feature is precisely that there is no app, server, synchronization process, prediction model, new employee, or special hardware to keep alive.
