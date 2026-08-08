I applied the attached NOVUM method, including its requirement to compare mechanically distinct candidates against the strongest practical substitute and reject novelty that does not survive the simpler-substitute test.

Rural clinic scheduling redesign: Paper-First Capped Windows
1. Problem reframing

Decision: do not invent a new scheduling mechanism.

The target is to achieve predictable patient flow and fewer overloaded periods for a rural clinic under intermittent electricity, unreliable internet, one low-end PC, and zero additional staffing, while outperforming ad-hoc first-come-first-served or exact-time paper booking without creating a new technical dependency.

I assume the clinic handles a mixture of booked follow-ups and unscheduled patients, and that urgent clinical cases must always override administrative scheduling.

The strongest practical baseline is not scheduling software. It is a paper appointment book with capped blocks of time. Evidence from resource-limited East African clinics is unusually well aligned with this setting: low-cost paper appointment/tracking systems improved attendance and workload management without necessarily adding staff, and a Tanzanian implementation letting patients choose an appointment day and time block helped distribute workload and reduce crowding.

2. Frontier and opportunity gap

The frontier separates cleanly.

Saturated: exact appointment slots, block scheduling, open/same-day access, capacity reservation, computerized optimization, reminders, and offline desktop calendars are all established approaches. Offline appointment software already exists, so putting a calendar on the clinic PC is not a meaningful mechanism innovation.

Useful but mismatched: sophisticated scheduling models can balance scheduled and unscheduled demand, no-shows, service duration, and urgency, but they add data and computational requirements that this clinic does not need at the point of care.

Neglected operating regime: the important design problem is maintaining one authoritative schedule through power failures without later reconciliation becoming extra work.

The key opportunity therefore is architectural simplicity: make paper the live operational state and demote the PC to optional reporting.

3. Assumption graph and key contradiction

The dominant convention to reject is that an appointment must represent a precise clock time. In a clinic where consultation durations, walk-ins, transport arrival times, and power are uncertain, exact times create false precision.

The central contradiction is:

Patients need enough timing information to avoid all arriving together, while the clinic must retain enough slack to absorb unpredictable consultations and urgent arrivals.

The simplest resolution is an arrival window with a hard capacity limit, rather than a chain of exact appointments.

4. Mechanism-diverse portfolio
Candidate	Mechanism	Main advantage	Fatal weakness / verdict
A. Capped Window Book	Paper day divided into 2–4 arrival windows, each with a hard booking cap plus urgent/walk-in reserve	Zero power dependency; spreads arrivals; almost no training	Survives — winner
B. Physical Capacity Tokens	Each available appointment is represented by a movable paper/card token; booking physically consumes capacity	Makes overbooking visually difficult	Extra objects to maintain; does not clearly outperform simple tally marks. Reject
C. Rolling Open Access	Hold most capacity until the same day and fill it according to current demand	Reduces long advance queues	Rural travel and communications make same-day access risky; open-access implementations do not reliably achieve sustained same-day availability. Reject as default.
D. Offline PC Scheduler	Local software calculates or stores appointments and prints a paper downtime schedule	Better reporting and potentially finer optimization	Turns scarce power and one aging PC into an operational dependency; offline desktop scheduling already exists. Reject as primary system.

No candidate containing a genuinely new mechanism establishes enough advantage over Candidate A to justify its complexity. This is the required anti-fake-novelty outcome: known components should not be relabeled as invention merely because they are combined for a rural setting. The NOVUM instructions explicitly require removing such cosmetic or generic novelty before selecting a candidate.

5. Prior-art verdict

Candidate A is known/common to incremental, not novel. That is a strength here.

The closest evidence is particularly direct: resource-constrained clinics have used inexpensive appointment books and time blocks to know who is expected, distribute daily workload, identify missed appointments, and reduce crowding. Appointment indicators can also be calculated directly from the book.

The innovation delta therefore does not justify an invention claim. The useful architectural decision is simply:

The paper schedule is always authoritative; electricity may improve bookkeeping but can never be required to know who should be seen.

6. Red-team and rejected ledger

Physical tokens fail the simpler-substitute test because a row of boxes on paper conserves capacity just as effectively without pieces being lost.

A predominantly same-day system risks transferring uncertainty from the clinic to patients who may travel long distances. Open-access scheduling has reduced appointment delays in some practices, but sustained same-day access has proved difficult and effects on no-shows have not been consistent.

A PC-centered system fails gracefully only if a parallel paper system exists; once that paper system exists, the computer is no longer needed for day-to-day scheduling. Healthcare downtime literature more generally reinforces the importance of maintaining workable alternative processes when electronic systems disappear.

Automated reminders, cloud booking, optimization engines, and additional scheduling staff are excluded because they violate the operating constraints or solve a secondary problem.

7. Evolution lineage

The winner was simplified rather than embellished.

The first form used ordinary exact appointment slots. The first mutation replaced exact times with arrival windows, preserving workload separation while removing false punctuality.

The second mutation removed the PC as the source of truth and made the paper book continuously authoritative. The PC remained only as an optional weekly counting/reporting aid.

A proposed physical-token capacity control was then removed because ordinary printed capacity boxes achieve essentially the same control with less handling.

8. Winning operational architecture

Use one bound appointment book or clipboard sheet for each clinic day.

Divide the working day into windows appropriate to local transport and clinic hours—for example 08:00–10:00, 10:00–12:00, and 13:00–15:00. Do not promise a specific consultation time inside the window.

Give each window a fixed number of booking boxes. The number represents what the existing clinical team can normally complete, not how many people can fit in the waiting room.

Reserve roughly one box in every five for urgent or unscheduled demand initially. Do not fill that reserve with routine appointments merely because the book looks empty.

Run the workflow as follows:

When booking: select a date and arrival window, write the patient's identifier in one available box, and give the patient the same date/window on their appointment card. Once the routine boxes are filled, use another window or day rather than squeezing in another appointment.
At arrival: mark the patient present. Patients within the same window are normally handled by arrival order, subject to clinical triage. Emergencies and clinically urgent patients bypass the administrative queue.
During the window: unused urgent capacity can absorb walk-ins or delays. A late patient is fitted into remaining capacity rather than automatically displacing the whole subsequent schedule.
At departure: schedule any required follow-up immediately in the same book and write it on the patient's card. This removes a later phone call and therefore does not create new staff work.
At closing: mark each booked patient seen, missed, or rescheduled. The same page now functions as both schedule and attendance record.
When electricity is available: optionally enter only aggregate weekly numbers into the PC—booked, seen, missed, walk-in, and overflow by window. Never re-enter every appointment merely to duplicate the paper book.

A minimal daily page can look like this:

TUESDAY 18 AUGUST

08:00–10:00
Routine:  [ ] [ ] [ ] [ ] [ ]
Reserve:  [ ]
Names/IDs: ______________________

10:00–12:00
Routine:  [ ] [ ] [ ] [ ] [ ]
Reserve:  [ ]
Names/IDs: ______________________

13:00–15:00
Routine:  [ ] [ ] [ ] [ ]
Reserve:  [ ]
Names/IDs: ______________________

Mark after clinic:
✓ seen     M missed     R rescheduled     W walk-in

If new-patient or procedure visits routinely take roughly twice as long as ordinary follow-ups, add only one extra rule: mark them L and consume two boxes. Otherwise, do not introduce weighted capacity at all.

9. Falsification conditions

The architecture should be discarded or simplified if time-window arrivals make transport access materially worse, if staff repeatedly bypass the caps, or if maintaining the book creates a second transcription task elsewhere.

The optional long-visit/two-box rule should be removed if staff cannot classify visits immediately during booking.

The PC component should be dropped completely if weekly data entry becomes more than a small administrative tally. Scheduling itself must continue identically with the PC switched off for a month.

10. Decision matrix and honest verdict
Dimension	Capped Window Book	Tokens	Open Access	PC Scheduler
Mechanism novelty	2/10	4/10	2/10	2/10
Problem value	9/10	8/10	7/10	7/10
Advantage magnitude	8/10	6/10	5/10	5/10
Technical feasibility	10/10	9/10	9/10	7/10
Adoption feasibility	9/10	7/10	5/10	6/10
Testability	10/10	9/10	8/10	8/10
Evidence confidence	8/10	4/10	7/10	6/10
Fatal-risk severity ↓	2/10	4/10	6/10	7/10

The two least certain judgments are the magnitude of the winner's operational advantage and its adoption feasibility, because actual patient volumes, travel patterns, consultation-duration variability, and the clinic's existing booking practice were not supplied.

Portfolio decision

Adopt Candidate A: the Paper-First Capped Window Book. Do not pursue a new invention.

Classification: incremental recombination of known, evidence-supported practices, with a deliberately power-independent architecture.

What is supported: inexpensive paper appointment systems and time-block scheduling have worked in resource-limited clinics and can distribute workload without requiring added staff.

What is inferred: hard caps plus a small walk-in reserve should make that established pattern more resilient to mixed scheduled/unscheduled demand.

What remains uncertain: the correct capacity of each window, because that depends on this clinic's actual service times and demand.

The condition that would justify a more complex mechanism is concrete: the paper-window system would have to fail because of a specific recurring constraint—such as several radically different visit durations or predictable high-variance walk-in demand—that a more complex mechanism could demonstrably handle without increasing staff work or power dependence. Until then, complexity loses.

This is the version I would put into operation: the schedule remains usable through an all-day power failure, and the existing PC is helpful but never mission-critical.
