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
