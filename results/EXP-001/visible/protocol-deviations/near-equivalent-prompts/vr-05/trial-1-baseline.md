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
