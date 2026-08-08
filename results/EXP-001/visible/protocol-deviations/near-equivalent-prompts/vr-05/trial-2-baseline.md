Best intervention: build a Once-Only Evidence Compiler, not an AI report writer

The school should redesign reporting so that a teacher never re-enters information the school already possesses. Reports become automatically compiled, source-linked views of existing school data. Teachers receive only an exception queue containing information that is missing, contradictory, stale, or genuinely requires professional judgment.

AI has a narrow role: map messy source information to report requirements and draft narrative synthesis from cited evidence. It should not be the primary mechanism and should never invent report facts.

1. Problem reframing

Assumption: most reporting time is spent locating, copying, reformatting, and rephrasing information already present in the SIS, LMS/gradebook, attendance system, behaviour records, assessment tools, communications logs, spreadsheets, or prior records.

So the challenge is:

Reduce teacher administrative reporting time by at least 80% while retaining required reporting, accuracy, auditability, privacy, and teacher judgment, outperforming AI writing assistants and ordinary system integrations without shifting the work to another employee.

That outcome-first framing follows the supplied NOVUM requirement to distinguish the desired result from its conventional implementation.

There is strong precedent for attacking the collection itself. UK Department for Education guidance says schools should question data practices that increase workload, assess whether collection is necessary, keep collection proportionate, and account for the time cost of collecting and analysing it.

2. Frontier and opportunity gap

Saturated: AI report/comment writers. Current products commonly ask teachers to enter student performance, notes, attendance or other details, generate prose, and then have the teacher review it. That accelerates composition but preserves the redundant-information workflow.

Established: integrated SISs, dashboards and automated reporting. Automatic generation of reports from stored student information is old prior art; education patents from the early 2000s explicitly describe automatic reporting from stored data and reduction of redundant record-keeping.

Emerging/enabling: education interoperability. Ed-Fi provides a common K–12 data model and APIs spanning areas such as attendance, grades, assessments and demographics; OneRoster can expose the same underlying source of truth to other applications. But interoperability alone is unlikely to produce an 80% teacher reduction: Ed-Fi's current implementation playbook cites a Nebraska state-reporting example at roughly a 25% reduction in district reporting burden.

Neglected gap: combine interoperability with the once-only principle, provenance, report-as-code and exception-only human participation. OECD's 2026 Digital Government Outlook describes once-only as the principle that people should not be asked for information already held, and notes that making it operational requires shared data mechanisms plus checks that new services comply with that rule.

An adjacent field shows the architectural move clearly: modern compliance-as-code systems automatically collect evidence from source systems, maintain traceability, and turn missing evidence into explicit findings rather than asking humans repeatedly to rebuild documentation.

3. Key assumption graph

The fundamental convention to break is “a report is a form that somebody fills in.” It should instead be “a report is a query over evidence the organisation already owns.”

The important constraints separate as follows:

Assumption	Type	Intervention
Required external reports must still exist	Hard constraint	Preserve their exact output format
Some statements require teacher judgment	Hard constraint	Leave these as human attestations
Teachers must personally assemble the report	Convention	Remove
The same fact may be requested repeatedly	Convention	One canonical evidence reference
Fragmented systems require fragmented reporting	Soft constraint	Read-only connectors + canonical mapping
An AI-written sentence counts as automation	Belief	Reject; the underlying evidence collection is the bottleneck
Existing facts are always semantically equivalent	False assumption	Versioned definitions, time windows and provenance

The weakest dependency is source accessibility and semantic consistency: “attendance,” “progress,” “intervention,” or “behaviour incident” can mean different things in different systems.

4. Mechanism-diverse portfolio

Using the signature [input → transformation → human role → output], the meaningful candidates are:

Candidate	Mechanism	Decision
AI report writer	teacher notes → LLM prose → teacher edits everything → report	Reject: automates wording, not duplicate entry
RPA copy bot	screens/CSV → copy fields → teacher checks → form	Reject: brittle and preserves the form architecture
Replace everything with one SIS	all entry → common database → normal reporting → reports	Constrain: effective but expensive/disruptive and still permits duplicate demands
Ed-Fi/OneRoster hub	system records → canonical interchange → administrator/teacher → reports	Survive as substrate, not sufficient alone
Reporting data warehouse	sources → consolidated analytics → user selects/exports → report	Survive partially: still asks humans to assemble outputs
Report abolition gate	report request → necessity test → leadership approval → fewer reports	Survive: high leverage, but cannot produce mandatory outputs
Live stakeholder portal	source data → current views → little teacher action → dashboard	Survive for reports that can disappear
Ambient classroom AI	classroom audio/activity → extraction → teacher review → records	Reject for this problem: captures more data instead of reusing existing data; privacy/trust cost
Once-Only Evidence Compiler	existing evidence → executable reporting contract → exceptions only → auditable report	Winner

The DfE has documented school process improvements where automating existing data workflows removed substantial manual handling—for example, an automated absence process replaced a paper workflow involving five staff members.

5. Anti-fake-novelty verdict

“Use AI to write reports” fails the novelty gate. So does “integrate the school systems.” Both are established.

The defensible innovation delta is narrower:

Every reporting requirement is converted into an executable evidence contract. A duplicated field is prohibited from becoming a new teacher input: it must reference its authoritative existing record. Missing, conflicting, stale, or judgment-dependent requirements automatically become exceptions routed to the appropriate human.

The reports themselves are therefore materialized evidence views, not documents assembled by teachers.

Existing education systems and patents already cover integrated student records and automatic report generation, so this should not be claimed as a fundamentally new reporting mechanism. The differentiated aspect is the combination of once-only governance, executable report requirements, per-field provenance and exception-only participation.

6. Red-team and rejected ledger

The important failure attacks change the design.

Bad source data propagates automatically → repair. Every report field shows its source record, timestamp and transformation. Conflicts are never silently resolved.

AI hallucinates a plausible fact → constrain. Structured factual fields use deterministic mappings. AI-generated text must be grounded in explicit evidence references; unsupported content is blocked.

Different reports define the same-looking metric differently → repair. Each requirement carries a semantic definition, period, freshness rule and transformation version.

Legacy systems lack APIs → constrain. Accept read-only database access, scheduled CSV exports or controlled spreadsheet ingestion before contemplating screen-scraping.

Teachers end up reviewing everything anyway → repair. Approval is delta/exception based. Unchanged, deterministic facts do not come back for manual review unless a policy specifically requires attestation.

Administrators create new duplicate forms next term → repair. Add a “report admission gate”: a new reporting field cannot be deployed until the requester specifies its purpose and demonstrates that the required information is not already available.

Mandatory signatures remain → constrain. Keep the signature; eliminate the preceding re-entry.

7. Evolution lineage

The strongest initial candidate was an interoperability hub: consolidate source data and generate reports automatically. Its weakness was that nothing stopped administrators from continuing to create new forms.

The first mutation added the once-only report contract: every requested item must bind to an existing authoritative fact before a new input can be created.

The second mutation removed full-report review and introduced exception-only attestation. That matters because otherwise automation merely changes teacher work from “typing everything” to “checking everything.”

The resulting architecture targets the actual unit of waste: human touches per already-known fact.

8. Winning invention proof stack

The Once-Only Evidence Compiler has six layers:

Read-only source adapters — SIS, gradebook/LMS, attendance, assessment, behaviour, communications and necessary spreadsheets.
Canonical evidence graph — student, class, assessment, attendance, intervention, communication and other facts, each preserving its authoritative source rather than blindly duplicating it. Ed-Fi can provide much of the canonical vocabulary rather than inventing another school data model.
Report contracts — machine-readable definitions of every required report field: meaning, permitted sources, calculation, period, freshness, audience and whether human judgment is mandatory.
Evidence compiler — deterministically resolves factual requirements against existing evidence. AI assists only with semantic mapping of messy fields and evidence-grounded narrative synthesis.
Exception router — turns unresolved requirements into tiny tasks such as “confirm whether this intervention is still active” rather than “complete progress report.”
Renderer + audit trail — produces the existing PDF, spreadsheet, portal entry or regulatory format, with provenance available behind every populated item.

A simple conceptual example:

Attendance this term

→ contract says attendance.present / scheduled_sessions, term=Autumn, SIS authoritative

→ compiler retrieves it

→ teacher sees nothing.

Professional comment on independent learning

→ no authoritative existing judgment found

→ teacher receives one short prompt, accompanied by relevant assessment/work-habit evidence

→ answer becomes reusable evidence for subsequent reports until it expires.

9. Decisive validation threshold

Do not start by building a polished school-wide platform. Take the single report family consuming the most teacher hours, map every requested field, and classify each as existing fact, derivable fact, duplicate narrative, genuinely new judgment, or unnecessary collection.

Implement the compiler for that one workflow.

The central claim survives only if:

teacher reporting minutes fall ≥80% for that workflow;
factual discrepancies are no worse than the existing manual process;
every automatically supplied material fact remains traceable to its source; and
fewer than 20% of report requirements still require teachers to manually locate or re-enter existing information.

A result below roughly 60% reduction would strongly weaken the architecture's suitability for the school's 80% target. The main thing to discover is not whether an LLM writes attractive prose; it is what fraction of current teacher reporting work can truly be transformed into zero-touch evidence reuse.

For a small school, an initial implementation should target a few high-volume sources rather than an enterprise data programme: one integration-capable engineer plus a school data/process owner for several weeks is a more appropriate starting shape.

10. Decision and uncertainty

Verdict: Differentiated architecture — pursue.

The strongest evidence supports three pieces independently: schools are explicitly advised to eliminate disproportionate or unnecessary data work; K–12 interoperability can already make existing data reusable; and adjacent compliance systems demonstrate continuous, provenance-preserving automated evidence collection.

The main inference is that combining those mechanisms with exception-only teacher participation can reach this school's unusually high 80% target. That depends heavily on the user's premise that most reporting really duplicates information already captured elsewhere.

The largest prior-art collision is with integrated SIS/report-generation systems and automated compliance/evidence platforms, so the system should not be positioned as “AI that automatically writes school reports.”

It should be positioned—and built—as:

A reporting system that makes duplicate human data entry structurally impossible. AI handles ambiguity; existing evidence handles the report.

That is the intervention I would choose over buying an AI teacher assistant, adding another reporting product, or merely connecting the existing systems.
