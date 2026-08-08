Portfolio decision

Do not invent a new scheduling mechanism for this clinic. The strongest solution is a deliberately simple, paper-first, short-horizon scheduling workflow with protected same-day capacity and a very small weekly feedback rule. The more novel-looking alternatives add failure points or staff burden without a clear causal advantage. That follows the supplied requirement that a serious candidate needs mechanism novelty, outcome advantage, constraint fit, and falsifiability—not novelty for its own sake.

1. Problem reframing

Achieve more reliable access, less waiting/overload, and fewer wasted appointment slots for a rural clinic under intermittent electricity, unreliable Internet, one low-end PC, and fixed staffing, outperforming a conventional fixed appointment book plus ad-hoc walk-ins without making power, connectivity, or extra clerical work critical dependencies.

Intermittent electricity is a genuine operating constraint for rural health facilities; WHO specifically reports that unreliable power is disproportionately a problem in remote and rural facilities.

The baseline to beat is not sophisticated software. It is a well-run paper appointment book.

2. Frontier and opportunity gap

Cloud booking, automated reminders, predictive optimization and patient portals are poor fits because connectivity and computer availability become operational dependencies. Local systems such as Bahmni can operate without Internet, but still introduce software installation and maintenance. An OpenMRS deployment example assumes dedicated registration/data-entry staff, system administration and UPS-backed infrastructure—resources explicitly absent here.

Conversely, shorter scheduling horizons and same-day capacity are established mechanisms. A 2024 systematic review found significant no-show reductions in 10 of 16 studies of open-access scheduling, while an earlier systematic review identified longer booking lead time as an important predictor of missed appointments. Reserving capacity specifically for same-day demand is also well-established scheduling prior art.

The neglected opportunity here is therefore not a clever algorithm. It is making the schedule power-failure invariant while preventing advance bookings from consuming all near-term capacity.

3. Key contradiction

The conventional assumption is that a better schedule needs more precise future bookings. In this setting that can make things worse:

More advance certainty → longer lead times + more no-shows + less room for walk-ins.

The useful inversion is:

Commit less capacity far in advance; keep more capacity controllable near the day of care.

The second important convention to discard is that the PC must contain the authoritative schedule. With intermittent power, paper should hold transactional state; the PC should only help with occasional analysis.

4. Four mechanically distinct candidates
Candidate	Mechanism	Decision
A. Protected short-horizon capacity	Keep a portion of each session unavailable for advance booking and fill it with near-term/same-day demand.	Survive. Strong evidence basis, minimal complexity.
B. Arrival waves	Give routine patients broad arrival bands instead of precise appointment times, absorbing uncertain travel/service times.	Conditional. Use only if lateness and transport variability are major problems.
C. Physical capacity tokens	Each visit type consumes physical workload tokens; no tokens means no further booking.	Reject. Extra handling does not clearly beat simply marking long visits as two slots.
D. Bounded feedback reserve	Once weekly, change protected capacity by at most one slot based on unused capacity versus unmet same-day demand.	Survive as a small addition. Does not require continuous computing.

Candidate A collides directly with known open-access/carve-out scheduling, so it should not be presented as novel. Candidate D is ordinary feedback control applied very lightly. Candidate C has a more distinctive interface but fails the simpler-substitute test.

5. Resulting workflow

Use A + a stripped-down D, while retaining ordinary paper slots.

1. Make one paper sheet the master schedule. Use one weekly ledger kept at reception. Record only the minimum scheduling information—patient name or identifier, appointment class, and contact information if needed. Avoid diagnoses or sensitive clinical detail on a publicly visible sheet.

The PC is never required to know whether a slot is free.

2. Stop filling the distant calendar with ordinary visits. Book far ahead only when the date itself matters: planned procedures, scheduled maternal/child care, chronic follow-up at a clinically specified interval, vaccination sessions, visiting specialist days, etc. For ordinary consultations, preferentially offer appointments within the next few clinic days.

This attacks the lead-time/no-show mechanism rather than compensating for it with overbooking.

3. Protect near-term capacity every half-day. Determine how many patients the clinic can safely handle in a normal half-day. Leave a fraction visibly marked S for same-day demand.

If there are no usable historical counts, a practical starting rule is roughly one protected slot for every three or four ordinary slots. Treat that purely as an initial setting, not a universal optimum. Do not double-book.

For example, if a normal half-day safely handles eight standard visits:

B B B S | B B S S

B = advance-bookable
S = held for same-day/near-term demand

A predictably long appointment simply occupies two adjacent positions. No token system is necessary.

4. Fill protected slots from real demand, not forecasts. When the clinic opens, same-day callers and appropriate walk-ins use the S positions. If a protected position is still unused close to its service time, give it to the next routine walk-in rather than leaving it idle.

Administrative scheduling should not replace whatever clinical triage process the clinic already uses for urgent presentations.

5. Use arrival bands only where punctuality is genuinely poor. If patients routinely travel long distances with uncertain transport, replace 09:10/09:30/09:50 promises with something like a small 09:00–10:00 group served in arrival order. Keep exact times for procedures and visits whose timing matters.

If transport punctuality is not a significant problem, retain ordinary appointment times—the simpler method wins.

6. At closing, make four tally marks. No patient-level data entry is required:

unused protected slots;
non-emergency same-day requests that could not be accommodated;
no-shows;
whether the session ran materially beyond normal closing time.

Once each week, change the next week's protected capacity by no more than one slot per half-day. If same-day demand repeatedly exceeds protected capacity, add one. If protected capacity repeatedly goes unused while nobody is being deferred, remove one. If the signals conflict, make no change.

This bounded adjustment is intentionally slow so one unusual market day, weather event, vaccination campaign, or transport disruption does not cause the schedule to oscillate.

6. Role of the single PC

Keep the PC off the critical path.

When electricity happens to be available, enter only weekly totals into a tiny local spreadsheet:

Week	Booked visits	Same-day requests	Same-day unable to fit	No-shows	Unused protected slots	Late sessions

Its purpose is trend visibility and monthly review—not booking, synchronization, patient check-in, or real-time optimization.

No Internet connection is required. A power failure therefore causes zero scheduling-state loss and zero switch to a downtime procedure; staff simply continue using the same ledger.

7. Rejected ledger

Full local EMR/scheduler: rejected as the first intervention. Local/offline systems exist, but their implementation and support burden does not beat the paper workflow under these staffing and power constraints.

Predictive/AI scheduling: rejected. Insufficient data, unnecessary computing dependency, and the principal bottleneck is capacity allocation rather than prediction.

Routine overbooking: rejected initially. Carve-out research sometimes combines protected slots with double-booking, but doing so requires credible local no-show and service-time information; otherwise the clinic transfers uncertainty directly into queues and overtime.

Physical colored tokens/cards: rejected. They make capacity tangible but create another object staff must maintain and reconcile. A marked paper slot performs the essential function more simply.

8. Failure thresholds

The added mechanism—the weekly reserve adjustment—should be removed if it creates appreciable clerical burden without changing capacity decisions. Likewise, abandon arrival-wave scheduling if it increases crowding or patient waiting compared with ordinary slots.

For the workflow as a whole, track three operational measures against the clinic's own current baseline: patient waiting time, requests that cannot be accommodated, and sessions finishing late. If those do not improve without increasing administrative work, retain the power-safe paper master but revert to the simpler fixed-capacity schedule.

Final verdict

Classification: incremental recombination, not a new invention.

The strongest architecture is:

paper master schedule + short booking horizon + protected same-day capacity + slow one-slot-per-week adjustment + optional PC reporting.

Its advantage comes from eliminating infrastructure dependencies and deliberately preserving controllable capacity, not from a new algorithm. The available prior art already covers open access, protected same-day slots and local/offline digital systems, so there is no defensible reason to invent something more elaborate here.
