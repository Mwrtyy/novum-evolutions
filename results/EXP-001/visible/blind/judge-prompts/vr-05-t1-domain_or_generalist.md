# EXP-001 Blind Judge — vr-05-t1-domain_or_generalist

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
  "pair_id": "vr-05-t1",
  "evaluator_id": "vr-05-t1-domain_or_generalist",
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

# Blind pair vr-05-t1

## Task

A small school wants a breakthrough AI system to reduce teacher administrative reporting workload by 80%, but most reports duplicate information teachers already entered elsewhere. Find the best intervention.

## Output A

Best intervention: Reportless Reporting — a Once-Only Evidence Compiler

Do not build an AI that helps teachers write reports faster. Build a system in which teachers do not create reports at all unless genuinely new judgment is required.

The governing methodology points toward reframing around the measurable outcome rather than the requested object, and toward rejecting “existing product + generic AI” as fake novelty.

1. Problem reframing

Reduce teacher administrative reporting time by 80% while retaining accuracy, accountability and required human judgment, by eliminating repeated entry of information that already exists elsewhere.

The key insight is that the report is not the work product. The underlying evidence is the work product. A report is merely one presentation of that evidence.

That distinction matters because current AI report tools mostly accelerate prose generation. MagicSchool already offers an AI report-card-comment generator, and Twinkl offers AI-assisted report writing from teacher-supplied details. That is therefore a crowded, incremental mechanism.

There is also institutional evidence that excessive data collection itself should be attacked rather than simply automated: England's Teacher Workload Advisory Group focused specifically on eliminating unnecessary data and evidence collection, while subsequent workload guidance includes auditing data collection and removing disproportionate practices.

2. The opportunity gap

The pieces required for a better architecture now exist, but they are usually used separately.

Education interoperability is mature enough to retrieve much existing information. OneRoster exchanges rosters, courses, assessments and grades between educational systems, while Ed-Fi provides a wider student-centric data model covering academic performance, attendance, discipline and related records.

AI is becoming useful for the messy mapping problem. Recent LLM schema-integration work addresses automatically matching semantically equivalent fields across heterogeneous databases and tables—the precise problem encountered when one system says attainment_level, another says current_grade, and a report asks for “achievement.”

And there is a strong mechanism transfer from another domain: modern compliance systems map requirements to common evidence once and reuse that evidence across multiple reports or frameworks instead of repeatedly collecting it.

The neglected combination is: apply that continuous-evidence model to school reporting, with the teacher acting only on exceptions.

3. Mechanism portfolio
Candidate	Core mechanism	Decision
AI report writer	Teacher supplies facts; LLM writes prose	Reject — familiar and leaves duplicate input intact
Comment-bank generator	Reuse standard narrative fragments	Reject — optimizes writing, not reporting
RPA form filler	Copy fields mechanically between systems	Reject — brittle when forms/schemas change
Replace everything with one SIS	Put all activity into one platform	Reject for a small school — migration is the intervention
Classroom-listening admin agent	Capture new evidence automatically	Reject — creates a surveillance/data-capture problem when the evidence already exists
Change-only reports	Teacher records only changes since previous period	Survives
Reporting-field sunset	Delete fields with no identifiable consumer/action	Survives
Once-Only Evidence Compiler	Turn every report requirement into a query against existing evidence; ask humans only for gaps	Winner

The strongest candidate survives because its advantage comes from changing the control policy: the normal state changes from “teacher must complete this report” to “the system must prove why teacher input is necessary.”

4. Winning architecture
Reportless Reporting

Every reporting requirement is decomposed into atomic claims:

student + period + requested fact + acceptable source + transformation rule

For example:

Report asks: “Current mathematics attainment.”

Instead of presenting a text box, the system finds:

Gradebook → Mathematics → current assessment aggregate → B

and creates:

Mathematics attainment: B
Source: Gradebook / Term 2 / calculated 4 Aug 2026

No teacher action occurs.

If the report asks:

“Has the pupil become more confident contributing verbally?”

and no existing source can establish that, then the teacher receives one small request:

“Any material change in oral participation since the last report?”

The answer becomes reusable evidence rather than disappearing into that particular report.

Architecture

1. Requirement compiler
Reads every internal, parent, governing-body or regulatory report template and turns its fields into machine-readable evidence requirements.

2. Read-only source adapters
Connect to the school's SIS/MIS, gradebook, attendance, behaviour system, LMS, pastoral notes and approved spreadsheets. OneRoster or Ed-Fi should be used where systems support them; CSV imports are a perfectly reasonable fallback for a small school.

3. Semantic mapping layer
AI proposes that differently named fields represent the same concept. A human approves mappings once rather than teachers reconciling them repeatedly.

4. Provenance registry
The system stores a pointer to where every fact came from, its timestamp and any transformation applied. It preferably does not create another unnecessary master copy of every student record.

5. Deterministic evidence engine
Structured facts are calculated using rules rather than generated by an LLM. If two systems disagree, the conflict is exposed rather than silently resolved.

6. Teacher exception inbox
Teachers never receive blank reports. They receive only:

missing information,
contradictory records,
genuinely qualitative judgments,
facts whose confidence is below the school's threshold.

7. Rendering layer
The same evidence can produce a parent report, safeguarding summary, management report or other required format.

8. Reporting-sunset rule
Every requested field must have a named purpose or recipient. If nobody can state what decision a field supports, remove it rather than automating it.

5. The decisive design change

The initial concept could have been a central AI school-data warehouse. That carries unnecessary migration and privacy costs.

The stronger design makes three mutations:

Central warehouse → source-linked evidence layer. Keep authoritative data in the systems that already own it and store mappings/provenance.

Full-report teacher approval → exception-only attestation. Requiring teachers to read and approve every automatically generated report would simply replace typing workload with checking workload.

Generative reporting → evidence-first reporting. The LLM may improve wording, but it is forbidden from supplying facts. Every factual sentence must resolve to explicit evidence.

The irreducible innovation delta is therefore:

A report becomes an executable evidence request, and human attention is invoked only when existing evidence cannot satisfy that request.

That is materially different from an AI report writer.

6. The 80% threshold

There is a useful mathematical constraint here.

Let:

r = proportion of current reporting time caused by repeating/reformatting existing information;
c = proportion of that repeated work the system can reuse automatically;
h = new review/exception overhead as a proportion of today's reporting time.

Maximum reduction is approximately:

r × c − h

So, for example, an 80% reduction is structurally possible if:

0.90 × 0.95 − 0.05 = 80.5%

But if only 70% of reporting time actually consists of duplicate work, no AI implementation of this mechanism can reach 80% without also eliminating or redesigning additional reporting requirements.

That makes the first go/no-go condition straightforward: determine the fraction of reporting minutes spent on information that already exists somewhere else.

7. Main failure modes

The largest risk is not AI capability. It is inaccessible or contradictory source data. A beautifully designed system fails if critical information lives in incompatible products with no usable export/API.

The other important risks are manageable by architecture: prohibit unsupported generated facts; expose source conflicts; retain role-based access; avoid classroom surveillance; maintain field-level provenance; and do not let administrators quietly add new reporting requirements without identifying their source and purpose.

There is also a behavioral failure mode: once automatic reporting becomes cheap, administrators may request more reports. The reporting-sunset rule therefore belongs inside the system rather than being merely a policy suggestion.

Kill conditions

Do not pursue this architecture as the route to the 80% target if either of these is true:

substantially less than roughly 90% of current reporting time is duplicate/reformatting work; or
the school's existing systems cannot provide reliable machine-readable access to most of the duplicated evidence.

In that case, the better intervention is primarily report abolition and process simplification, not more AI.

Verdict

Differentiated architecture, worth pursuing.

The novel-looking part is not generative AI. Education already has interoperability standards, AI report writers already exist, and “collect evidence once, reuse it repeatedly” already exists in adjacent compliance systems.

What is differentiated is applying those components around a strict school-workflow invariant:

Teachers never report a fact twice.

If information already exists, the system retrieves it with provenance. If it does not exist, the teacher supplies it once. Future reports consume that evidence automatically.

For this school's stated problem, that is the best intervention because it attacks the causal source of the workload rather than making duplicate reporting more efficient.

## Output B

Using the attached NOVUM methodology—reframing around the outcome rather than the requested object, and requiring a precise, falsifiable mechanism—the strongest intervention is not an AI report writer. It is a Once-Only Reporting Compiler: make the school’s existing records the evidence base, compile reports from them automatically, and ask teachers only for information that genuinely does not exist elsewhere.

1. Problem reframing

The challenge is:

Reduce active teacher time spent on administrative reporting by at least 80%, while preserving teacher judgment, factual accuracy, auditability, and existing school systems—without making teachers re-enter information the school already possesses.

The strongest practical baseline is a combination of SIS-generated reports plus an AI assistant that drafts comments. That baseline can make writing faster, but it leaves the deeper process intact: teachers still gather, reconcile, paste, review, and certify information.

This matters because administrative work remains a substantial source of teacher stress: OECD TALIS 2024 reports that 52% of teachers identify general administrative work as a source of stress.

2. Frontier and opportunity gap

The current frontier separates into four patterns:

Area	Current state	Gap
AI report/comment writing	Already common; AI produces prose from prompts or teacher inputs	Accelerates authorship rather than eliminating redundant reporting
SIS automation	Mature systems already generate grades, attendance and some reports from stored information	Usually bounded to information inside that particular system
Education interoperability	OneRoster exchanges rosters, grades and related data; Ed-Fi provides a broad K–12 data model and APIs	Moves information between systems but does not decide whether a teacher should be asked for it again
Once-only/compliance architectures	Other domains encode rules and reuse existing authoritative evidence	Rarely applied to school reporting as an exception-only human workflow

OneRoster explicitly aims to reduce manual effort by automatically exchanging information between educational applications, while Ed-Fi provides a common model for data such as students, teachers, attendance and assessments.

The important collision is older than AI: education systems have long been capable of generating reports automatically from stored baseline data. A 2004 education-system patent, for example, describes state reports generated from information already stored in the system. So “AI automatically generates reports” is not the invention.

The neglected opportunity is to make the reporting obligation itself executable.

3. Assumption graph and key contradiction

Today the implicit workflow is:

existing facts → teacher retrieves facts → teacher translates them into report fields → teacher rewrites narrative → school stores another copy

The hidden assumptions are different kinds of constraints:

Assumption	Classification	NOVUM treatment
Teachers must complete every report field	Convention	Remove
A report must be authored as a separate document	Convention	Remove
Existing systems cannot be replaced	Soft/hard operational constraint	Preserve them through adapters
Teachers must remain accountable for professional judgments	Hard constraint	Preserve human attestation
Student information requires controlled access	Hard constraint	Enforce field-level permissions and provenance
Existing records may disagree or be stale	Technical reality	Surface conflicts rather than silently reconcile them
AI needs broad access and autonomous judgment to save time	Belief	Reject

The core contradiction is therefore: the school wants teacher accountability, but has implemented accountability as repeated data entry.

Those are not the same thing.

The intervention should separate attestation from authorship.

4. Mechanism-diverse candidate portfolio
Candidate	Mechanism	Human role	Verdict
A. AI Report Writer	LLM reads existing records and drafts completed reports	Edit and approve prose	Reject as primary intervention
B. RPA Report Copier	Bots copy fields from SIS/LMS into existing forms	Handle failures and verify	Useful bridge, not breakthrough
C. Unified Evidence Warehouse	Centralize school data, then generate every report as a database view	Correct source data	Strong but integration-heavy for a small school
D. Once-Only Reporting Compiler	Convert each reporting requirement into an executable claim; resolve it against existing evidence and send only unresolved claims to teachers	Supply genuinely new judgment and attest exceptions	Winner

Candidate D differs from the others in what controls the workflow. It is neither the database nor the language model. The reporting requirement controls it.

5. Prior-art and anti-fake-novelty verdict

AI drafting fails the anti-fake-novelty gate. Existing teachers already use AI to turn bullet points or stored information into report comments, and contemporary school AI products increasingly target administrative time savings. Editing and contextual alignment remain recurring limitations.

Simple data synchronization is also established. OneRoster and Ed-Fi are strong evidence that interoperable school-data infrastructure is not itself novel.

The useful transfer comes from the once-only principle used in digital government: authorities should not request information again when they already possess admissible evidence for it. Policy-as-code supplies another established building block: requirements can be represented as machine-readable rules rather than passive documents.

Innovation delta: after removing AI branding, interoperability, templates and conventional automation, the irreducible difference is:

Every report requirement becomes a typed claim specifying what evidence may satisfy it, which source has authority, how fresh that evidence must be, how conflicts are handled, and whether human judgment is mandatory. The teacher is contacted only when that claim cannot already be satisfied.

That survives the novelty gate as a differentiated architecture, not as a claim that automated reporting itself is new.

6. Red-team and rejected ledger

The AI-writer approach is rejected because it optimizes the last step while preserving information gathering, duplication and review. It can even create extra verification work when polished text contains an unsupported inference.

RPA copying remains useful only as an adapter for legacy systems. UI changes, authentication and field changes make it brittle.

A central evidence warehouse could work, but for a small school it creates unnecessary migration and governance overhead before delivering value.

The winning architecture survives with constraints. It must never silently resolve conflicting grades, dates or narrative observations; those become exceptions. Subjective professional judgments must be explicitly tagged as human-only. Student-data connectors must use least-privilege access. The language model may render approved claims into readable prose, but it cannot invent factual claims or convert missing evidence into confident text.

7. Evolution lineage

The first form of the winning concept used a central evidence repository. That dependency was removed: the better form keeps existing SIS/LMS systems authoritative and uses federated read-only adapters, normalizing only the fields required for reporting.

The second change replaces full-report review with a delta inbox. Instead of showing a teacher a 30-field generated report, it might say:

27 requirements already satisfied from authoritative records.
2 existing observations require confirmation.
1 new professional judgment required.

A provenance and contradiction layer is then added so that efficiency cannot hide stale or inconsistent evidence.

8. Winning invention proof stack: Once-Only Reporting Compiler

The operating principle is simple:

A school report should be compiled, not authored.

Its architecture has seven layers.

Source adapters connect read-only to the current SIS, LMS, gradebook, attendance system, behaviour records and approved forms. Existing education standards should be used where supported rather than inventing another universal school schema.

Claim registry converts every report requirement into a machine-readable specification. For example:

term_absences = SUM(authoritative_attendance_events during reporting_period)

or:

learning_progress_comment = HUMAN_JUDGMENT OR existing_teacher_observation <= 60_days_old

Evidence resolver finds already-entered evidence capable of satisfying each claim.

Provenance engine retains the exact source, timestamp, owner and transformation behind every generated field.

Conflict engine refuses automatic completion when authoritative sources disagree.

Delta inbox contains only unresolved, conflicting or explicitly human-only claims.

Renderer/exporter turns the validated claim set into whatever PDF, portal field, regulator form or parent-facing narrative the school presently requires. An LLM is useful here for linguistic transformation, but facts come solely from resolved claims.

A report might therefore behave like this:

Required item	Current teacher work	Compiler behavior
Attendance	Re-enter/count	Derived from attendance system
Current grade	Copy from gradebook	Derived
Missing assignments	Count/check LMS	Derived
Previous interventions	Search notes/forms	Retrieved with provenance
Standard progress wording	Write from scratch	Rendered from approved facts
New professional concern	Write	Teacher supplies it
Conflicting records	Manually discover	Automatically escalated

The strongest alternative is an AI copilot attached to the reporting form. The compiler can beat it because it removes teacher touches, whereas the copilot primarily shortens individual touches.

9. Smallest decisive proof

Do not begin by building a school-wide AI platform. Take the single recurring report responsible for the most teacher hours and encode its requirements.

For approximately one class or year group, build only read-only connections to the two or three systems that already contain most of the required information. Turn each report field into a claim, generate the satisfied fields automatically, and expose unresolved fields through the delta inbox.

The decisive thresholds should be fixed beforehand:

Result	Decision
≥80% reduction in active teacher reporting minutes, with no unsupported automatically generated factual claims	Proceed
60–79% reduction	Architecture works, but the 80% claim is weakened; inspect which claims remain irreducibly manual
<60% reduction	Do not scale—the school's duplication assumption was insufficient
Any systematic invention of facts or silent conflict resolution	Stop and repair the evidence/provenance mechanism

A credible first implementation is roughly 2–4 weeks for one report type if the relevant systems expose usable exports or APIs; a production rollout is more plausibly 6–12 weeks, mainly determined by integrations, permissions and the number of report families rather than by model development. The critical skills are data integration, workflow engineering and school-process ownership—not frontier model research.

10. Scores, uncertainty and verdict

Scores are 0–10; fatal risk is reversed, with 10 meaning worst.

Candidate	Novelty	Problem value	Advantage	Technical feasibility	Adoption	Testability	Defensibility	Evidence confidence	Fatal risk
AI Report Writer	2	9	4	9	8	9	2	8	4
RPA Report Copier	2	9	6	8	7	9	2	8	5
Evidence Warehouse	4	9	8	6	5	8	5	7	6
Once-Only Reporting Compiler	6	9	9	7	7	9	6	6	5

The two uncertain scores are mechanism novelty and adoption. Novelty is constrained because automated educational reporting has substantial older prior art, while adjacent once-only and compliance-as-code mechanisms are clearly established. Adoption depends heavily on whether administrators are willing to change the rule from “every teacher completes every field” to “every required claim must have accountable evidence.”

Evidence supports the existence of administrative burden, mature education-data interoperability, automated report generation, AI-assisted report drafting, and once-only/policy-as-code mechanisms.

The key inference is that because most of this school's reports duplicate existing inputs, converting reporting into evidence resolution plus exception handling attacks the dominant source of work directly.

The speculative part is the exact 80% reduction; that depends on the proportion of current teacher effort that is truly redundant rather than professional judgment.

Verdict

Differentiated architecture worth pursuing: Once-Only Reporting Compiler.

The breakthrough is not better generative AI. It is making the unit of administration a provenance-backed claim rather than a form field, and changing the teacher's job from repeatedly supplying known information to handling only the information delta.

For this school, I would spend the first engineering effort on the claim registry + delta inbox + read-only connectors, not on training or buying a more powerful language model.

