Best intervention: Evidence-Compiled Reporting

The school should stop treating reports as documents teachers author. Treat each report as a compiled view of evidence the school already possesses, with teachers involved only when something is missing, contradictory, or genuinely requires professional judgment.

That reframes the challenge exactly as NOVUM requires: optimize the outcome rather than optimize the requested object.

1. Problem reframing

Reduce teacher administrative reporting work by at least 80% without replacing the school's existing teaching systems, lowering report reliability, or allowing AI to invent student information.

The key observation is that writing is not the dominant causal problem; recapture is. Teachers have already recorded grades, attendance, assessment results, interventions, behaviour events, notes, accommodations, and sometimes parent communications. Reporting then asks them to reconstruct that evidence in another format.

This is a worthwhile target: TALIS 2024 reports that administrative work is a source of stress for about half of teachers across OECD systems, despite representing a relatively small share of total working time—suggesting that the disruptive, bureaucratic nature of the work matters as much as its raw duration.

2. What the frontier already does

Three obvious solutions are already well explored.

Candidate	Mechanism	Decision
AI report writer	Teacher supplies grades/notes; LLM writes polished prose	Reject as core intervention. It automates writing after teachers have gathered/re-entered the information. Products already do this.
RPA form copier	Bot copies fields from one screen/form into another	Reject as architecture. Useful tactically, but brittle when interfaces or forms change and weak on provenance.
Replace everything with one SIS	Put attendance, grades, comments, etc. into one platform and generate reports	Strong baseline, but not the best fit. Existing systems already synchronize grades/attendance and auto-generate reports, but migration forces a small school to replace working tools.
Evidence-Compiled Reporting	Existing records become authoritative evidence; reports compile automatically; teachers receive only exceptions	Survives. It directly attacks duplicate human work while preserving the existing stack.

The standards infrastructure needed for the surviving mechanism is increasingly practical. OneRoster supports exchange of roster and grade information; Ed-Fi provides a broad K–12 unifying data model; Caliper standardizes learning-activity events across applications.

3. The intervention

Call it ECR — Evidence-Compiled Reporting.

Its control loop is:

Teacher works normally → existing systems create evidence → ECR compiles required reports → teacher sees only unresolved exceptions.

The architecture has six pieces:

Read-only source adapters. Connect to the school's existing SIS, LMS, gradebook, attendance/behaviour tools and spreadsheets through APIs or scheduled CSV exports. Do not require teachers to use another application.

Evidence layer. Normalize facts into records such as:

student → mathematics attainment → 72% → source: gradebook → recorded 2026-06-18

Every fact retains its source, timestamp and authority.

Report-spec compiler. Convert each administrative reporting template into executable requirements. For example:

Attendance percentage ← attendance system
Current mathematics attainment ← gradebook
Intervention received ← support log
Narrative progress statement ← grounded synthesis of permitted evidence

Provenance-first AI. AI may interpret awkward legacy labels, propose mappings and turn verified evidence into readable prose. It cannot introduce an uncited student fact. Mapping execution and calculations remain deterministic.

Exception queue. Instead of giving a teacher a 30-field report, give them perhaps:

“28 fields resolved from existing evidence. Two require you.”

Examples are genuinely new qualitative observations, conflicting records, or a legally/institutionally required personal attestation.

Report rendering. Once exceptions are resolved, the same evidence can produce the PDF, parent report, leadership summary, regulatory form or spreadsheet required by different recipients.

This follows NOVUM's anti-fake-novelty constraint: merely putting generic AI on an existing workflow is not enough.

4. The crucial innovation delta

Strip away the LLM, dashboard and product branding and the important change remains:

A report ceases to be a data-entry surface. It becomes a compiled projection of authoritative evidence, and the system creates human work only when it cannot establish the required answer from existing evidence.

That inversion matters.

Current reporting asks:

“Teacher, complete this report.”

ECR asks:

“System, prove as much of this report as possible. Ask the teacher only for what cannot already be proved.”

There is strong adjacent precedent for the causal mechanism. Modern compliance platforms connect directly to operational systems, automatically collect evidence and surface gaps instead of repeatedly asking staff to manually prove facts already present elsewhere.

5. Why AI belongs here—but not where expected

The AI's highest-value job is semantic integration, not ghostwriting.

Suppose one report requests “engagement,” another asks for “participation,” the LMS stores assignment completion, the behaviour tool stores positive participation events, and teachers have previously written “engages consistently.”

An AI system can propose that these concepts overlap and show an administrator the evidence mapping once. Once approved, subsequent reports reuse that mapping rather than asking every teacher to reconstruct the relationship.

The architecture should therefore use:

AI for: schema matching, extracting structure from legacy report templates, grounded summarization, detecting duplicated requirements, explaining contradictions.
Deterministic software for: grades, attendance calculations, rule execution, field population, access policy and provenance.
Humans for: genuine professional judgment, disputed evidence and exceptional cases.

This division sharply limits hallucination risk.

6. Important collision with current work

The underlying idea of assembling trustworthy educational context from multiple authoritative systems is no longer untouched territory. In May 2026, 1EdTech published its draft Trusted Portable Learning Context, describing policy-aware, provenance-bearing context compiled from multiple educational source systems for AI applications.

That means the defensible distinction is not “multi-source educational context.”

The differentiated architecture is the inverse administrative workflow built on top of it:

report requirement → evidence compilation → proof of satisfied fields → exception generation → minimal human attestation.

Existing school products also demonstrate portions of the stack—automatic population from SIS/gradebooks/attendance and AI drafts based on live school data—so automatic report generation itself should not be presented as novel.

7. Failure boundaries

ECR should not automatically fill a field merely because an LLM thinks two concepts are equivalent. Every generated factual statement needs recoverable evidence. If systems do not expose usable APIs, read-only exports should be the fallback rather than screen-scraping wherever possible.

Some reporting obligations also genuinely require fresh teacher judgment. Those remain exceptions rather than being fabricated from indirect proxies. And if virtually all of the school's information already resides in one modern SIS that can generate every required report, buying/configuring that feature is simpler than building ECR.

For a typical small school with several functioning but disconnected tools, however, replacing everything is unnecessary.

Portfolio decision

Proceed with Evidence-Compiled Reporting as a differentiated architecture. Kill the standalone AI report writer and RPA approaches as primary interventions; treat an integrated SIS migration as the strongest alternative.

The decisive design principle is:

Capture once. Compile everywhere. Ask humans only for exceptions.

That is the intervention most causally aligned with an 80% workload-reduction target because it attacks the duplication that created the workload rather than merely making duplicate reporting faster. The interoperability, automatic-reporting, and cross-domain evidence-automation components are supported by existing practice; the degree to which the complete exception-only school-reporting architecture is distinctive remains appropriately classified as differentiated, not universally novel or proven.
