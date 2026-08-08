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
