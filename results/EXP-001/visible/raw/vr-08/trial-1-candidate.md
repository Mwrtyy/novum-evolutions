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
