# EXP-001 Blind Judge — vr-08-t1-domain_or_generalist

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
  "pair_id": "vr-08-t1",
  "evaluator_id": "vr-08-t1-domain_or_generalist",
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

# Blind pair vr-08-t1

## Task

Improve scheduling for a rural clinic with intermittent power, no reliable cloud access, one low-end PC, and no budget for additional staff. Invent a new mechanism only if it clearly beats a simpler workflow.

## Output A

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

## Output B

Decision: improve the workflow; do not invent a new scheduling mechanism

The strongest design is a paper-first hybrid access schedule: pre-book only the visits that truly need certainty, preserve substantial same-day capacity, give patients arrival windows rather than fragile exact times, and keep the PC out of the critical path.

I would not build an offline scheduling app, synchronization scheme, algorithmic optimizer, or novel token system. Advanced/open-access scheduling is already well established, with a 2026 systematic review finding reduced appointment waits across all 23 studies that measured them. Meanwhile, unreliable electricity is a genuine operating constraint for rural health facilities, and even offline-capable EMR approaches introduce storage, login, synchronization, and shared-computer complications.

The operating model

Use one bound paper appointment book as the sole scheduling authority. One page represents one clinic day, split into morning and afternoon. Within each half-day, divide capacity into three buckets:

Capacity	Starting allocation	Purpose
Anchored	~50–60%	Visits that genuinely benefit from advance certainty: chronic follow-up, antenatal care, procedures, patients travelling long distances
Same-day	~30–40%	Acute problems, walk-ins, requests made that day
Buffer	~10%	Urgent additions and protection against visits running long

These are starting proportions, not extra mathematics for staff.

Use only two appointment sizes: S for a normal visit and L for something that routinely takes about twice as long. More categories create clerical work without enough benefit.

Patients should normally receive a time window, such as “morning early,” “morning late,” “afternoon early,” or “afternoon late,” rather than promises such as 09:15. Variable consultation lengths make exact times brittle, while scheduling scheduled and unscheduled patients together is already a recognized outpatient scheduling problem.

What happens in practice

When someone books, staff write the patient's identifier, S/L, and arrival window directly into the master book and onto the patient's appointment card. No computer entry is required.

At opening time, the clinic begins filling the same-day portion. The buffer remains protected until roughly halfway through the session. If it has not been required by then, it becomes ordinary capacity.

If the anchored section is full, do not squeeze another routine patient between appointments. Offer another day/window. Clinical urgency can always override the schedule through the clinic's normal triage process.

If electricity disappears, absolutely nothing changes operationally.

One useful feedback rule

At the bottom of every day's paper page, add four tally boxes:

Booked attended | Booked absent | Walk-ins seen | Patients deferred

Once a week, adjust only one capacity space at a time:

repeated unused same-day spaces → convert one to anchored capacity;
repeated deferrals of appropriate same-day patients → convert one anchored space to same-day capacity;
repeated overruns → enlarge the buffer before increasing total bookings.

This creates a slow feedback loop without forecasting software, statistics expertise, or additional staff.

The low-end PC can be used when power happens to be available to enter those four weekly totals into a simple offline spreadsheet. It should not contain the authoritative appointment calendar. That avoids maintaining two masters and eliminates reconciliation after outages.

Why the more elaborate mechanisms lose

I considered four mechanically different approaches. An offline PC scheduler fails because the single PC and electricity remain failure points. A paper-plus-digital dual-master system creates reconciliation labor and conflicting versions. A physical capacity-token system survives outages but makes rescheduling and lost tokens unnecessarily awkward. A dynamically recalculated reservation scheme could respond faster to fluctuating demand, but the additional bookkeeping is hard to justify for a one-PC clinic with no additional administrative capacity.

The surviving elements—shorter-horizon/open capacity, protected walk-in capacity, coarse appointment windows, and paper operation—are largely known scheduling mechanisms rather than a defensible new invention. Advanced-access scheduling specifically aims to leave meaningful capacity available rather than filling the calendar far in advance, and published reviews characterize it as a relatively economical intervention that does not inherently require additional staffing.

The physical page

A half-day can be as simple as:

TUESDAY MORNING

ANCHORED
[ ] S  Patient ______  Early
[ ] S  Patient ______  Early
[ ][ ] L Patient _____  Late
[ ] S  Patient ______  Late

SAME-DAY
[ ] __________
[ ] __________
[ ] __________

BUFFER — DO NOT FILL EARLY
[ ] __________

END-OF-DAY
Booked attended __
Booked absent   __
Walk-ins seen   __
Deferred        __

Appointment cards need only date + arrival window + clinic/service + patient identifier. Avoid sensitive diagnoses on cards patients carry publicly.

Verdict

Known/common mechanisms, deliberately simplified into a differentiated outage-resilient workflow. No-go on inventing a new mechanism.

The irreducible design choice is that electronic availability must never determine whether the clinic knows who is expected or how much capacity remains. Everything digital is optional reporting support rather than operational state.

That is preferable to novelty for its own sake: the governing instructions explicitly require constraint fit and an outcome advantage, and permit an honest no-go when no invention is worth carrying forward.

