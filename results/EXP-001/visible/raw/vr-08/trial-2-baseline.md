Decision: use a paper-first window-and-reserve schedule

Do not invent a new scheduling mechanism for this clinic. The strongest design is a deliberately simple combination of established mechanisms: paper appointment tracking, broad arrival windows, workload-based capacity, and protected same-day capacity.

That choice follows the governing NOVUM requirement that a mechanism justify itself through real advantage and constraint fit, rather than novelty for its own sake. Low-cost paper appointment systems have already been used successfully in resource-limited African settings without necessarily requiring additional staff, while advanced-access approaches show the value of preserving near-term capacity instead of filling every future slot.

The operating rule

Replace exact-time appointments such as “Tuesday 09:15” with arrival windows, for example:

Window	Patient instruction	Capacity
A	08:00–09:30	booked + reserved
B	09:30–11:00	booked + reserved
C	11:00–12:30	booked + reserved
D	13:30–15:00	booked + reserved

Exact boundaries should match the clinic's actual hours. Window scheduling tolerates variable consultation lengths and transport delays better than a tightly spaced electronic calendar; block scheduling is already a recognized outpatient scheduling pattern.

Capacity should be counted in workload marks, not simply patient count:

1 mark: known short return, routine refill/review.
2 marks: ordinary consultation.
3 marks: known longer visit or procedure.

These are workload categories, not medical urgency categories. Clinical urgency remains with the clinic's normal clinical triage process. If visit length is unknown, use 2 marks.

For each window, leave roughly 30% of its capacity unbooked for same-day demand and walk-ins as a starting operating rule. That percentage is deliberately adjustable rather than treated as a universal constant. Open/advanced-access scheduling uses this same underlying principle—do not commit all capacity far in advance.

The paper system is the master

Use one sheet per clinic day in a bound appointment book:

Patient ID	Window	Load	Visit code	Arrived	Seen	New date
1842	A	1	R	✓	✓	14 Sep
2311	A	2	C	✓	✓	—
0944	B	3	P			

Use patient identifiers rather than diagnoses on the scheduling sheet.

At the end of a consultation, the clinician writes the next required visit as something like “week of 14 Sep / standard / 2 marks.” Whoever already handles booking chooses an available window and writes it both in the appointment book and on the patient's appointment card.

That eliminates a major source of administrative guessing: the person booking does not have to determine how complex the next clinical encounter will be.

During the day

Scheduled patients arrive during their window rather than simultaneously at opening. This is important because concentrated morning arrivals themselves can drive excessive queues; primary-care evidence has found arrival patterns associated with waiting-time performance.

Within each window:

Existing clinical triage overrides the schedule when medically necessary.
Otherwise, serve scheduled patients for the current window in arrival order.
Walk-ins consume that window's protected reserve.
If reserve capacity is exhausted, place non-urgent walk-ins into the next window with capacity rather than silently overloading the current one.
A very late scheduled patient enters the next available capacity rather than displacing everyone already waiting.

This avoids pretending that a 09:15 booking means the clinician will actually be free at 09:15.

What the PC should do

The low-end PC should be a mirror and counting tool, never the operational dependency.

Use one local LibreOffice Calc file with columns for:

Date | Window | Patient ID | Load | Planned/Walk-in | Attended | Rescheduled

No cloud account, network database, server, automated synchronization, or specialized scheduling application is necessary.

When electricity is available, enter the paper records. The spreadsheet can total:

marks booked per window;
same-day demand;
unused capacity;
no-shows;
patients carried into later windows.

When electricity fails, nothing about scheduling changes. Continue writing in the appointment book and enter the missing records later. This is preferable to making an offline-capable digital system another piece of infrastructure the clinic must maintain. WHO specifically cautions that digital interventions cannot substitute for functioning health-system processes, while unreliable electricity remains especially problematic in rural facilities.

One simple feedback rule

Don't optimize the schedule with software. Change it one capacity mark at a time.

If the same window repeatedly runs out of walk-in reserve, shift one mark from advance-bookable capacity to reserve for that window. If reserve repeatedly goes unused while future appointments are backed up, shift one mark back to advance booking.

Similarly, if one window is continually overloaded while the following window is quiet, move one bookable mark forward.

This gives the clinic a crude but understandable feedback controller without forecasting software, algorithms, additional personnel, or reliable power.

Important special cases

Chronic-care follow-ups: book them before the patient leaves. Paper-based appointment/tracking systems have particular precedent for chronic-care settings in resource-constrained clinics.

Patients traveling long distances: give them the first practical window compatible with transport rather than mechanically assigning the earliest clock time.

Known long procedures: allocate three marks and preferably place them where they will not consume the entire same-day reserve.

Several clinicians: give each clinician a separate lane on the same daily sheet. Do not create separate databases.

Power outage lasting days: continue indefinitely on paper. The PC backlog affects reporting, not care access.

What I would reject

I would not deploy cloud scheduling, an offline-first custom application, AI prediction, SMS-dependent booking, optimization software, patient kiosks, or a local server. Each introduces maintenance or infrastructure dependencies without addressing the central scheduling problem better than the window-and-reserve workflow under the stated constraints.

I would also reject a pure first-come-first-served morning queue. Evidence from outpatient settings shows that arrival concentration and appointment design materially affect patient flow, and systems supporting both scheduled and unscheduled patients need explicit capacity for both.

NOVUM verdict

No-go on inventing a new mechanism. The defensible solution is a known/common set of mechanisms configured as a power-independent scheduling architecture:

paper master → workload-limited arrival windows → protected walk-in reserve → optional local spreadsheet mirror.

Its main advantage is architectural rather than technological: loss of electricity or internet removes reporting convenience but does not remove the clinic's ability to schedule or operate.
