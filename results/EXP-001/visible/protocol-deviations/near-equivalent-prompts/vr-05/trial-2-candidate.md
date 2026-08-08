Best intervention: Proof-Carrying No-Form Reporting

The strongest intervention is not an AI that writes teachers’ reports faster. It is a reporting layer that makes most reports disappear as teacher tasks.

Instead of presenting teachers with forms, the system treats each reporting requirement as an executable specification. It pulls facts already recorded in the SIS, gradebook, attendance, assessment, behaviour and pastoral systems; attaches provenance to every populated field; and asks the teacher only about information that is genuinely missing, contradictory, stale, or requires professional judgment.

That direction follows the attached NOVUM requirement to compare exactly four mechanically distinct candidates and end with a falsifiable candidate rather than generic recommendations.

1. Problem reframing

Challenge: Achieve ≥80% reduction in teacher time spent on administrative reporting for a small school, while retaining report accuracy, accountability and required human judgments, outperforming AI-assisted report writing without creating a new verification burden.

The need is credible. OECD TALIS 2024 reports that 52% of teachers across participating systems identify general administrative work as a source of stress. More importantly, education workload guidance has explicitly argued that unnecessary data collection should be minimized or eliminated rather than merely processed faster.

The crucial observation supplied in the problem is stronger: most requested information already exists. That makes the bottleneck duplicate information movement, not teacher writing speed.

2. Frontier and opportunity gap

The obvious territory is already crowded. Modern SIS products can generate report cards from grades, standards and attendance already in their databases, while generative-AI products increasingly help teachers draft educational material and comments. Yet AI-generated educational content still commonly needs teacher review and correction.

Interoperability is also technically plausible: Ed-Fi already defines shared K–12 representations covering assessments, report-card information, enrollment, attendance, discipline and related student data. Automated SIS-driven synchronization is routine for other school workflows such as rostering and identity provisioning.

The neglected opportunity is the intersection of three established ideas: education interoperability, the public-sector once-only principle, and compliance systems that automatically collect evidence with lineage. The EU’s once-only model explicitly aims for information to be supplied once and subsequently reused; continuous-compliance systems similarly map many requirements onto shared evidence and automatically assemble audit-ready records.

Opportunity gap: apply that architecture to teacher reporting, with the teacher becoming an exception handler rather than a report author.

3. Assumption graph and key contradiction

The existing workflow effectively says:

teacher activity → operational record → reporting deadline → teacher finds same information → recopies/rephrases it → administrator verifies it

Several constraints masquerade as necessities. “A report must be a form” is a convention. “The teacher must re-enter every field” is a convention. “Different reports require separate evidence” is often a convention. Some teacher attestation and professional judgment may be genuine hard constraints.

The key contradiction is therefore auditability versus workload. Schools recreate data partly because the recipient wants confidence in it. The solution is not eliminating accountability; it is making provenance replace re-entry.

4. Four mechanism-diverse candidates
Candidate	Core mechanism	Assumption replaced	Fastest way it fails
A. Proof-Carrying Report Compiler	Convert every required report into a machine-readable contract; derive fields from existing systems and attach source provenance; ask teachers only for exceptions.	Reports must be manually authored.	Existing source data cannot reliably satisfy enough report fields.
B. Obligation Deduplicator	AI decomposes all school reporting requirements into atomic information requests, identifies semantic duplicates, and consolidates or removes redundant collections.	Every existing report requirement deserves to survive.	Most requirements turn out to contain genuinely unique information.
C. Ambient Evidence Ledger	Continuously convert routine assessment, attendance and pastoral activity into structured evidence usable later for reporting.	Reporting evidence must be collected at reporting time.	Collection becomes surveillance-heavy or adds another workflow.
D. Administrative Delegation Router	Classify every reporting task by required authority and route clerical work to automation/support staff, preserving teacher-only judgments.	Teachers are the appropriate actor for the entire workflow.	Teacher-only judgment dominates the actual time burden.

Candidate A has the strongest causal route to the 80% target because its workload scales with new information, rather than with the number and length of reports.

5. Prior-art and anti-fake-novelty verdict

Simply generating report prose with an LLM fails the novelty gate: it is existing reporting plus generic AI, and it preserves the wasteful workflow.

Candidate A contains known components. Automatically generated SIS reports are known; once-only reuse is known; data provenance is known; continuous evidence collection is known.

Its defensible innovation delta is narrower:

After removing AI branding and known reporting components, the irreducible change is that reporting obligations become executable data contracts whose satisfied requirements require zero human interaction, while provenance and exception detection determine dynamically which questions, if any, reach a teacher.

That is a differentiated architecture, not a substantiated claim of universal novelty.

6. Red-team and rejected ledger

“AI writes every report” is rejected because it attacks wording rather than duplication and can replace typing time with checking time. “Replace every school system with one new AI platform” is rejected because migration cost, retraining and operational risk are disproportionate for a small school. Candidate C is constrained because indiscriminate ambient collection creates privacy and adoption problems. Candidate D survives as an auxiliary mechanism but cannot eliminate duplication by itself.

The main threat to Candidate A is garbage-in, confidently-reused. The architecture therefore cannot allow an LLM to invent authoritative facts. AI should perform semantic mapping, requirement parsing and ambiguity detection; deterministic transformations should generate authoritative fields, with source, timestamp and transformation visible.

7. Evolution lineage

The first mutation combines A’s report compiler with the useful part of B: before automating an existing form, the system decomposes it and collapses repeated requirements into a shared obligation graph. Ten reports asking for “attendance this term” become one evidence requirement with ten permitted outputs.

The second mutation removes generative AI from the factual execution path. AI translates human-written requirements and heterogeneous field names into proposed mappings during configuration; a school administrator approves those mappings once. Thereafter, report assembly is deterministic.

This produces the stronger candidate: No-Form Reporting with Proof-Carrying Evidence.

8. Winning invention proof stack

The architecture is:

SIS/LMS/attendance/pastoral systems → canonical evidence graph → report contracts → provenance validator → exception queue → required PDF/form/API output

A report contract might state that “term attendance percentage” requires a particular date range, approved attendance source, freshness threshold and calculation rule. Once those conditions are satisfied, the teacher never sees the question.

Every generated value carries its source record, extraction time and transformation rule. Conflicts—two systems disagreeing about a grade, for example—become exceptions.

Teachers receive something more like:

“27 reports are ready. Three items require your judgment.”

rather than 27 forms.

The causal advantage is structural: adding another report that requests already-known facts adds almost no teacher workload.

9. Prototype and decisive kill criteria

For a small school, the first implementation should avoid expensive integration. Take the three highest-burden recurring reports and connect only the two or three systems containing most of their information, using APIs where convenient and scheduled CSV exports where necessary.

Run the compiler in shadow mode against previously completed reports. A worthwhile continuation requires ≥95% correct automatic population of objectively derivable fields, no material invented facts, and ≥80% reduction in median teacher minutes per report cycle, including verification time. If fewer than roughly 70% of report requirements can be reliably sourced from existing records, or if verification consumes most of the saved time, the central intervention should be killed rather than polished.

The next evidence-producing actions are: inventory every requested reporting field and its existing source; build the obligation/source graph for the three worst reports; then run a complete reporting cycle in shadow mode before exposing teachers to the interface.

10. Decision and honest verdict
Candidate	Novelty	Advantage	Technical fit	Adoption fit	Testability	Evidence confidence	Fatal risk ↓
A / evolved winner	6.5	9.5	8	8	10	7	4
B	5	8	9	6	9	8	5
C	5	7	7	5	8	6	6
D	3	6	9	8	9	8	3

Verdict: Differentiated architecture worth validating.

What is supported is that teacher administrative/data workload is a meaningful burden, existing school systems already contain much of the required information, interoperability mechanisms exist, and once-only/provenance-driven reporting is technically established in adjacent domains.

What remains uncertain is the crucial school-specific quantity: what percentage of reporting time corresponds to fields that can actually be derived with sufficient accuracy and authority from existing records.

If that percentage is as high as the task description implies, the best intervention is clear: stop helping teachers write duplicate reports. Make duplicate reports compile themselves, and interrupt teachers only when the school genuinely needs new human information.
