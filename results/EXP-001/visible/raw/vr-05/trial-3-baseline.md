1. Problem reframing

Best intervention: stop treating reports as new data-entry exercises. Build an Once-Only Exception Reporting layer that turns each required report into a view over information already recorded in the school’s systems. Teachers supply only genuinely new professional judgment or resolve exceptions.

The target becomes: reduce teacher active reporting time by at least 80%, without reducing required information, inventing facts, or creating another place teachers must maintain. This follows the attached NOVUM instruction to reframe around the measurable outcome rather than the requested object.

This framing is supported by existing workload evidence. A UK Department for Education review found data recording/input/monitoring burdensome and described data work as frequently perceived as wasteful when its purpose is unclear.

2. Frontier and opportunity gap

The obvious solution—an AI report writer—is already crowded. Current products take teacher-written bullets, ratings, or criteria and turn them into polished comments; some explicitly market very large time savings. That improves writing speed, but teachers still have to retrieve and re-enter the underlying information.

Automatic population is also known: school-reporting products already advertise pulling data from student-information systems, gradebooks, and attendance systems. And interoperability itself is not new: OneRoster standardizes exchange of rosters and grades, while Ed-Fi provides a broader K–12 data model for interoperable systems.

The neglected opportunity is therefore not better prose generation. It is changing the reporting control loop so that teachers are never asked for information the school can lawfully and reliably retrieve elsewhere. That resembles the established “once-only” principle in public administration, where information already available for reuse should not be requested again.

3. Assumption graph and key contradiction

The critical inherited assumption is: “Every reporting cycle requires the teacher to complete the report.” That is a convention, not a fundamental requirement.

The actual functions are different: the school needs trustworthy facts, occasional professional judgments, recipient-specific presentation, and accountability. None requires teachers to retype grades, attendance, behaviour records, interventions, previous targets, or other already-recorded facts.

The key contradiction is therefore comprehensive reporting versus zero duplicate entry. The intervention resolves it by making the report a generated view of evidence, while making the teacher interface an exception queue.

This also matches established workload guidance: schools are advised to make collection proportionate, examine the time cost of each stage, question practices that do not help pupil progress, and automate suitable processes.

4. Mechanism-diverse candidate portfolio
Candidate	Core mechanism	Verdict
Generic AI report writer	Teacher supplies bullets; LLM expands them	Reject: optimizes typing, not duplication
Voice-to-report AI	Teacher dictates observations	Reject: faster duplicate entry
Browser/RPA form-filling bot	Copies fields between screens	Repair: useful but brittle
Central reporting warehouse	Consolidates source systems	Survivor, but heavier than necessary
Once-Only Exception Reporting	Reuse/derive existing evidence; ask teachers only for deltas	Winner
Report deletion governor	Delete fields with no action owner	Incorporate into winner
Parent live dashboard	Replace periodic reports with continuous access	Constrain: formal reports may remain required
Classroom-listening copilot	Automatically captures classroom events	Reject: privacy/trust/data-generation burden
Student-authored reporting	Students draft; teachers attest	Reject as primary mechanism
Autonomous cross-app agent	AI operates SIS/LMS/forms like a human	Reject: hidden errors and brittle interfaces
5. Prior-art and anti-fake-novelty verdict

The innovation delta is narrow but consequential:

For every requested report field, the system must either reuse an authoritative existing value, derive it deterministically, request only a genuinely new teacher judgment, or delete the field. The teacher never reviews the whole report unless exceptions require it.

Neither “AI writing,” interoperability, automatic data population, the once-only principle, nor exception reporting is novel individually. The differentiated architecture is their application as a mandatory field-level control policy with provenance and abstention, rather than as optional productivity features.

That distinction matters because existing education guidance has already demonstrated substantial savings from redesigning and automating data processes; one cited school-network case replaced a paper absence process involving five staff and roughly a school day of work with automated reporting.

Novelty verdict: differentiated architecture, not a substantiated first-of-kind claim. The largest remaining prior-art region is proprietary SIS/MIS reporting functionality and school-specific integrations that are not publicly documented.

6. Red-team and rejected ledger

The largest technical risk is conflicting or stale information across systems. The repair is field-level source-of-record rules, timestamps, and abstention: conflicting evidence becomes an exception rather than allowing AI to guess.

The largest adoption risk is that administrators keep every existing field “just in case.” The repair is structural: every reporting field needs a named recipient, intended action, source, and retention rationale. No action owner means the field is removed unless legally required. This is consistent with DfE guidance that schools should start with the intended action and determine whether collection is actually necessary.

A generic LLM should not receive unrestricted student records. Current DfE guidance explicitly identifies data-protection risks in generative-AI use by schools. The factual pipeline should therefore be deterministic and operate inside approved school infrastructure; generative AI is optional and downstream.

7. Evolution lineage

The first useful ancestor is the RPA copy bot: it eliminates retyping, but breaks when interfaces change and gives weak provenance. Replace screen automation with read-only source adapters using APIs, standard exports, OneRoster/Ed-Fi where supported, or scheduled CSV ingestion.

The second mutation removes the biggest residual workload: do not ask teachers to proofread every automatically generated report. Automatically clear fields whose source, freshness, and consistency checks pass. Surface only missing data, conflicts, genuinely new judgments, and unusual cases.

The final mutation incorporates report deletion: a report field that repeatedly produces no action is challenged for removal rather than automated forever.

8. Winning invention proof stack

The resulting architecture is:

Source systems → evidence registry → deterministic report compiler → exception engine → optional constrained AI prose layer → teacher approval.

Each report field has four possible states: Reuse, Derive, Ask, Delete.

“Reuse” retrieves an existing authoritative value. “Derive” calculates something mechanically from approved data. “Ask” is reserved for information that genuinely exists only in the teacher’s current professional judgment. “Delete” removes information whose collection has no justified purpose.

AI belongs primarily at the seams: mapping messy local field names during setup, spotting likely semantic matches, explaining inconsistencies, and optionally converting verified structured evidence into natural-language prose. It should not be the authority for attendance, grades, incidents, interventions, or other factual claims.

The causal advantage is straightforward: today, workload scales roughly with report size × number of pupils. Under this architecture, teacher workload scales with new judgments + discrepancies + approvals.

9. Prototype and falsification plan

Start with one high-burden recurring report, not a new school-wide platform. Take the last reporting cycle and classify every teacher-entered field as Reuse, Derive, Ask, or Delete. Connect only the two or three systems that contain most reused information.

Produce the same report automatically, but present teachers with only an exception screen. The decisive gate is teacher active time: the mechanism survives only if teachers can complete the reporting cycle in 20% or less of the previous active time, while required factual fields remain traceable to their source and unsupported factual generation is zero.

If the school cannot reach that threshold because too much information is genuinely new professional judgment, the 80% target is not achievable through duplicate-data elimination alone; report scope must be reduced rather than disguised with more AI.

10. Scores, uncertainty, and verdict

For Once-Only Exception Reporting, my current 0–10 assessment is: mechanism novelty 6, problem value 10, advantage magnitude 9, technical feasibility 8, adoption feasibility 7, testability 9, defensibility 6, evidence confidence 7, fatal-risk severity 4.

The two most uncertain scores are advantage magnitude and adoption feasibility. Advantage depends on how much teacher time, rather than merely report content, is actually duplicate work. Adoption depends on whether school leadership is willing to delete unnecessary fields instead of merely automating them.

Verdict

Build the reporting system that asks teachers almost nothing. Do not begin by buying an AI report-writing product. First impose the Reuse / Derive / Ask / Delete rule on every report field, automatically compile everything already known, and make teachers handle exceptions only.

For this particular school, that is the intervention with the strongest causal path to an 80% workload reduction—and it remains valuable even if the AI component turns out to be minimal.
*
