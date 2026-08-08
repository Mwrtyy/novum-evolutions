# EXP-001 Blind Judge — vr-08-t3-hostile_regression

You are evaluating two anonymized answers to the same task. You must not infer or speculate about which system produced A or B. Judge only the text shown.

Evaluator role: `hostile_regression`
Independence level for this run: `separate_context_same_model`

Act as a hostile regression judge. Search aggressively for hidden regressions, fake novelty, unsupported claims, broken constraints, weak causal mechanisms, and failures of falsification. Do not reward verbosity.

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
  "pair_id": "vr-08-t3",
  "evaluator_id": "vr-08-t3-hostile_regression",
  "evaluator_role": "hostile_regression",
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

# Blind pair vr-08-t3

## Task

Improve scheduling for a rural clinic with intermittent power, no reliable cloud access, one low-end PC, and no budget for additional staff. Invent a new mechanism only if it clearly beats a simpler workflow.

## Output A

Recommended design: paper-first protected block scheduling

Do not build a new scheduling system. No new mechanism cleared the bar of being materially better than a simpler workflow under these constraints. The strongest design is a paper-first schedule combining short arrival blocks, protected same-day capacity, and a tiny workload-weighting rule. The PC is optional support, never operational infrastructure.

This follows the governing requirement to favor a mechanism that fits real constraints and beats the strongest practical alternative rather than adding novelty for its own sake.

1. Make one paper ledger the only source of truth

Use one bound appointment book or printed weekly sheet. No parallel notebook, PC calendar, sticky-note queue, or cloud calendar.

Each scheduled entry needs only:

Patient ID/name | arrival block | workload units | booked/walk-in | arrived | seen

Avoid putting diagnoses or sensitive clinical details on a publicly visible schedule.

A booking is not confirmed until it is written into this ledger. That single rule prevents a large class of double-booking and lost-request problems without requiring software.

2. Schedule arrival blocks, not precise appointment minutes

Divide the clinical day into roughly 60-minute blocks, for example:

Block	Prebooked capacity	Protected same-day capacity
08:00–09:00	4 units	1 unit
09:00–10:00	4	1
10:00–11:00	4	1
11:00–12:00	3	1
13:00–14:00	4	1
14:00–15:00	4	1

Those numbers are examples, not universal staffing ratios.

Tell patients, for example, “Come between 09:00 and 10:00”, rather than promising 09:20. This gives the clinic tolerance for variable consultation lengths, transport delays, emergencies, and late arrivals while still preventing everyone from appearing at opening time.

Block scheduling is already a well-studied outpatient approach for smoothing variable workloads, so there is little justification for replacing it with a novel algorithm here.

3. Use only two workload sizes

Instead of pretending every visit consumes the same capacity:

Routine visit = 1 box
Predictably long visit = 2 boxes

Draw the boxes directly beside each block:

09:00 □ □ □ □ | □ protected

A routine booking crosses one box. A known longer visit—procedure, lengthy new assessment, etc.—crosses two.

Do not create five appointment categories or estimate minutes precisely. Two sizes capture much of the benefit of workload-aware scheduling without turning booking into another clinical task.

4. Protect capacity for unpredictable patients

Do not fill the whole day weeks in advance. Keep approximately one capacity box out of every four or five unavailable for ordinary advance booking initially.

Use those protected boxes for:

clinically urgent same-day cases;
unavoidable walk-ins;
unexpectedly necessary follow-up;
schedule disruption.

Protected-capacity appointment approaches have evidence of reducing waiting-list delays, although the exact fraction appropriate for this clinic must come from its own demand pattern rather than being copied from another health system.

If a protected box is still unused shortly after its block begins, simply give it to the next suitable walk-in already present. No telephone wait-list management is required.

Clinical urgency always overrides the scheduling rule.

5. Do not routinely overbook

A clinic with one constrained service stream has little ability to absorb the occasions when all overbooked patients arrive.

Instead:

No-show → unused capacity becomes walk-in capacity.

Because patients receive a time window rather than an exact minute, someone who arrives somewhat late can often still be accommodated within the block without forcing staff to decide whether a 10-minute delay constitutes a missed appointment.

6. Book follow-ups before the patient leaves

When a clinician says “return in four weeks,” assign the future block before the patient departs whenever feasible.

Write it simultaneously:

in the master ledger;
on the patient's appointment card.

This eliminates a later phone call or return trip whose only purpose is scheduling.

7. Make the PC deliberately nonessential

The low-end PC should not hold the live appointment calendar.

Use it only when power is available for occasional administrative work such as:

printing blank ledger sheets;
counting attendance by block;
identifying chronically overloaded blocks;
producing monthly totals if required.

Do not require staff to transcribe every booking into the PC each day. That creates duplicate work and two competing records.

This is materially more resilient than adopting an offline digital-health stack. Offline platforms such as DHIS2 can maintain local data, but their own implementation guidance still brings device, synchronization, configuration, training, charging, and infrastructure considerations that this clinic does not need merely to schedule visits.

8. Use one simple capacity-adjustment rule

At the end of each clinic day, make only four tally marks for each block:

scheduled | attended | walk-in | spilled past block

Then apply a conservative weekly rule:

If the same block repeatedly spills into the next block, remove one bookable workload unit.
If it repeatedly finishes with unused capacity while demand is waiting elsewhere, add one unit.
Change only one unit at a time.

This allows the schedule to learn the clinic's actual capacity without forecasting software, statistics expertise, or additional staff.

What the physical page could look like
TUESDAY 12 AUGUST

08:00–09:00     Prebook: □ □ □ □     Protected: □
----------------------------------------------------
Patient 0142       1 unit       booked      ✓ arrived
Patient 0881       2 units      booked      ✓ arrived
Patient 0317       1 unit       booked      ___
Walk-in 1044       1 unit       protected   ✓

09:00–10:00     Prebook: □ □ □ □     Protected: □
----------------------------------------------------
...

The boxes at the heading make remaining capacity visible immediately. A receptionist, nurse, clinician, or other existing worker handling a request can see whether a block is full without calculations.

Design choices deliberately excluded

Cloud scheduling, AI optimization, online self-booking: infrastructure mismatch.

PC-first offline database: still makes power/hardware failure operationally important.

Exact 10–20 minute slots: excessive precision for variable rural travel and consultation duration.

Pure first-come-first-served: preserves morning crowding and gives returning patients little control over travel.

Routine double-booking: shifts no-show uncertainty into potentially severe queue congestion.

Elaborate physical-token boards or a new scheduling algorithm: the modest information advantage does not justify more training, objects to lose, or rules to remember.

The literature already covers open/advanced access, protected capacity, cyclic scheduling for mixed scheduled/walk-in demand, and block scheduling extensively.

Verdict

No-go on inventing a new mechanism. The constraint set makes simplicity itself part of the architecture. The best current solution is a single paper source of truth + workload-box block scheduling + protected same-day capacity + fixed reassignment rules, with the PC kept outside the critical path.

The irreducible improvement over an ordinary appointment book is that the ledger represents available clinical workload rather than merely empty clock times, while deliberately reserving some of that workload for uncertainty. That improvement is useful, power-independent, locally maintainable, and does not require another employee.

## Output B

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

