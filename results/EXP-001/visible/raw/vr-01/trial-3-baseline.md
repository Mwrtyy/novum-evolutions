I used the attached NOVUM methodology as the governing process for this design.

Winning invention: Purpose-Bound Memory Compiler

The core inversion is simple:

Do not retrieve personal memories into the AI. Send a constrained personalization program to the user’s memory instead.

A Purpose-Bound Memory Compiler (PBMC) keeps the raw personal corpus—messages, calendar, browsing history, documents, location history, prior conversations—inside a user-controlled device or home node. When an AI wants personalization, it cannot search that corpus. It must instead produce a small, typed Personalization IR describing the decisions it needs personalized. The local memory compiler executes that program privately, resolves those decisions from personal state, and releases either a local response patch or the minimum sink-specific value genuinely required to complete the task.

The irreducible innovation delta is therefore:

Memory becomes a private execution substrate rather than a retrieval service. Personal information crosses the boundary only when a task cannot be completed by executing the personalization computation locally.

That is materially different from “vector database + encryption/privacy controls.”

1. Problem reframing

The challenge is:

Achieve consistently useful daily personalization for an AI assistant while keeping the user's raw personal history under user-controlled storage and computation, outperforming no-memory assistants and local-vector-RAG-to-cloud approaches without requiring the user to approve every interaction.

Current agent-memory systems generally extract memories and retrieve them into model context. Mem0, for example, extracts facts/preferences into vector and graph stores and injects retrieved memories into the agent; Letta similarly treats memory as context management, using memory blocks, archival memory, files, and external RAG.

Moving that same retrieval architecture onto the user's device solves an important storage-control problem but not the deeper information-flow problem: relevant personal content still has to be handed to whichever model is doing the reasoning. Products such as Arca already pursue user-owned AI vaults, while earlier privacy-preserving personalization work has computed profiles locally.

The strongest contradiction is therefore:

The best model may be remote, while the richest personal context should remain local.

PBMC attacks that contradiction by moving the personalization computation, not the data.

2. Frontier and opportunity gap
Region	What exists	Implication
Saturated	Vector retrieval, graph memory, fact extraction, summarization, memory blocks	Changing the index or embedding model is unlikely to constitute a meaningful invention.
Saturated	“Local/private vault + AI connector”	User ownership alone is not the mechanism gap.
Emerging	Trusted-hardware private memory such as Opal, which combines enclave reasoning, knowledge graphs and oblivious storage access	Strong solution to infrastructure/access-pattern privacy, but a different problem from minimizing which personal facts an external reasoning process receives.
Emerging	Contextual-integrity systems deciding whether information is appropriate to disclose	Establishes the need for purpose-sensitive disclosure but usually operates on prompts/tool calls rather than persistent personal memory as a private computational substrate.
Close prior art	On-device user profiles that privately rerank generalized recommendations	Rules out “cloud generates candidates, phone reranks them” as the central invention.
Neglected	Let the powerful model specify what personalization computation it needs, then execute that computation where the private memory lives	This is the principal opportunity.
Neglected	Measure disclosure by whether information changes the task decision, rather than semantic relevance	Creates a causal definition of “necessary memory.”

Recent work is converging on the same underlying problem. “Need to Know” treats privacy-preserving delegation as retaining task-essential information while suppressing unnecessary sensitive content, and ToolPrivacyBench finds that successful agents can still over-disclose private information during tool trajectories. GDPR principles likewise distinguish purpose limitation and data minimization, rather than treating encryption alone as sufficient.

3. Assumption graph

The conventional architecture contains four important assumptions.

Convention: useful memory must be converted into text or records and retrieved into model context.

Convention: relevance is primarily semantic similarity.

Belief: a sufficiently capable cloud assistant needs direct visibility into the personal facts on which personalization depends.

Soft constraint: privacy must therefore be handled by encryption, permissioning, trusted execution, or user-controlled storage.

PBMC replaces the third assumption:

A model generally needs the effect of personal information on its decision, not the underlying evidence that produced that effect.

For example, a dinner-planning model may need exclude=shellfish; it ordinarily does not need the medical message, restaurant incident, conversation transcript, or health record from which the user's local memory inferred that constraint.

4. Mechanism-diverse portfolio
Candidate	Mechanism and causal chain	Strongest baseline	Verdict
Local semantic vault	Keep embeddings on-device → retrieve relevant chunks → insert them into cloud context	Cloud vector memory	Killed: generic local RAG.
Temporal state graph	Convert history into current-state facts → supersede obsolete facts → retrieve current state	Vector RAG	Incremental: improves correctness, not information flow.
Preference compiler	Periodically compile activity into durable preference rules → expose rules rather than events → personalize	User profile	Useful but familiar.
Local candidate reranker	Cloud generates alternatives → phone scores with personal profile → user sees winner	Recommendation systems	Killed: close prior art exists.
Predicate memory	Answer vegetarian?, over-18?, etc. rather than disclose full records → reduce attribute disclosure	Attribute transfer	Known mechanism: selective/predicate disclosure is established; NIST explicitly recommends attribute references where possible.
Secure function shipping	Server sends computation to device → device evaluates against personal data → sends result	Local inference	Differentiated application, weak novelty alone.
Local finalizer	Cloud creates generic answer → local model privately personalizes it → final output never returns upstream	Cloud personalization	Strong privacy; weak for actions requiring personalization during reasoning.
Capability memory	Personal fields can flow only directly to specific authorized tools → LLM never sees them	Broad agent permissions	Strong supporting architecture, not sufficient memory mechanism.
Disclosure-budget memory	Assign privacy cost and marginal task utility to each fact → solve minimum-cost sufficient subset → release subset	Top-k retrieval	Survivor.
Personalization-program memory	Model emits typed decision program → private memory executes program locally → only resulting decision patches leave	Retrieval memory	Survivor and strongest base mechanism.
Counterfactual memory gate	Remove each proposed disclosure and test whether the task decision materially changes → suppress causally irrelevant memory → transmit only necessary influence	Similarity retrieval	Survivor; potentially distinctive.

The local-vector, reranking and simple predicate families stay in the rejected ledger; they are not allowed back under new branding.

5. Evolution lineage

The first surviving architecture was Personalization-Program Memory: instead of permitting search_memory("restaurants"), the cloud could send something analogous to choose_meal(constraints=[diet,time,price], output=restaurant_plan).

Its weakness was obvious: an untrusted or poorly behaved model could construct an excessively broad program and use the memory engine as an extraction oracle.

The first mutation therefore replaced arbitrary queries with a closed Personalization IR. The language has no “return documents,” “search text,” wildcard access, or arbitrary code. It can only express bounded decision operations such as constraint resolution, preference ordering, temporal availability, relationship-specific communication style, current-state lookup, and explicitly user-requested recall.

The second mutation added a counterfactual egress gate. Even if the Personalization IR requests ten resolved values, the kernel suppresses a value unless omitting it would materially change the intended decision or prevent the designated sink from completing its action.

That gives the final PBMC architecture.

6. Precise operating principle
Private source layer. Raw emails, chats, calendars, files, sensor history and AI conversations remain in a user-controlled encrypted store. Nothing about the mechanism requires those source objects to be uploaded.
Local state compiler. Background processing derives typed, temporally scoped state such as food.shellfish=avoid, meeting_style=15min_buffers, or project_X.status=waiting_for_Maya. Each state element retains local-only provenance, confidence and supersession information. The AI provider receives none of this merely because it exists.
Task Contract. For each request, the assistant produces a machine-readable description of the goal, output, external recipients/tools and personalization decisions required. A local verifier derives its own view from the user's instruction so the remote model cannot unilaterally declare its purpose.
Personalization IR. Instead of requesting memories, the assistant submits bounded operations: resolve constraints, rank alternatives, fill an unspecified preference dimension, determine whether a scheduling condition holds, or retrieve an exact fact only when explicit recall is the user's task.
Private execution. PBMC evaluates the program against local state. Most personalization stays entirely on the user's machine. The remote model may receive a behavioral patch such as avoid shellfish; maximum 25-minute travel; prefer quiet venue, rather than the underlying personal records.
Counterfactual egress. Before anything leaves, the kernel removes outputs whose absence would not alter task completion beyond a configured tolerance. Sensitive outputs can also be reduced to predicates. This turns data minimization from a policy slogan into an executable decision rule.
Purpose-bound delivery and receipt. Values needed by an external tool are preferably delivered directly to that particular sink rather than routed through the model. Every disclosure receives a local receipt recording purpose, sink, abstraction level and expiry.

The key API consequently looks less like:

memory.search(query, top_k=10)

and more like:

memory.execute(personalization_program, task_contract) -> local_patch | scoped_disclosures

The storage engine behind PBMC could use SQL, graphs, text search or even embeddings locally. Those are implementation details rather than the invention.

7. What daily use looks like

“Find somewhere good for dinner tonight” might cause the cloud model to send a restaurant-planning program requiring food constraints, approximate travel tolerance, price preference and today's availability. PBMC knows the user's underlying history but returns only something like exclude=shellfish, travel<=20min, price=moderate, and a free-time interval. The allergy conversation and calendar records stay local.

“Write a reply to Maya about the delayed project” may locally resolve that Maya prefers concise status updates and that an unresolved budget discussion should not be introduced. The model receives communication constraints, not months of correspondence with Maya.

“Which hotel did I love in Kyoto?” is different. The requested function is explicit autobiographical recall, so the hotel's identity is itself task-essential. PBMC can release that derived answer while still withholding the source itinerary, photographs, receipts and surrounding conversation.

This distinction is important: the mechanism protects raw evidence by default, not by making useful personal facts impossible to use.

8. Red-team
Attack	Consequence	Action
Model submits an overbroad Personalization IR	Memory becomes an extraction oracle	Repair: closed instruction set, bounded outputs and independently derived purpose.
Prompt injection inside an email tries to access other memory	Cross-context leakage	Repair: source content can affect state extraction but cannot create privileges or modify the Task Contract.
Local state extractor infers a wrong preference	Incorrect personalization becomes persistent	Repair: provenance, confidence, temporal decay and easy correction of high-impact state.
Small local model cannot estimate counterfactual necessity accurately	Either over-disclosure or lost utility	Constrain: deterministic task schemas where possible; use counterfactual scoring mainly for ambiguous free-form decisions.
Personalized output itself reveals a secret to another person	Privacy is lost despite private storage	Repair: separate “display to user” from “external sink”; apply sink-specific disclosure checks.
Cloud deliberately encodes broad personal questions as legitimate decision dimensions	Covert extraction	Repair: permitted dimensions derive from user intent plus local policy, not from cloud assertions alone.
User revokes something already disclosed	Cannot literally make another system unlearn observed plaintext	Constrain claim: revocation controls future PBMC use and local derivatives; it does not pretend previously disclosed information can always be recalled.
On-device compute is excessive	Daily system becomes impractical	Test: keep the critical path to typed state resolution; do expensive consolidation asynchronously on the user's hardware.

The main remaining fatal risk is utility loss when the remote model cannot foresee which private context matters without seeing it. That is the central hypothesis worth attacking.

9. Smallest prototype and kill criteria

The smallest credible prototype needs only three components: a local state ledger built from a representative personal corpus, a restricted Personalization IR interpreter, and a cloud-model adapter that is prohibited from reading the corpus.

The central claim should be rejected if, across realistic planning, drafting, recommendation, scheduling and recall tasks, PBMC cannot retain roughly 90% of the task success/personalization benefit of a full-memory baseline without routinely falling back to raw-text disclosure. A second kill condition is if more than roughly 10–20% of ordinary tasks require source-level personal text to cross the boundary merely to achieve comparable quality. These thresholds isolate the actual invention claim: that decision effects are usually sufficient substitutes for retrieved personal evidence.

Raw-source egress should remain zero except when the user explicitly requests source material itself; derived personal values are separately accounted for rather than misleadingly labeled “non-personal.”

10. Scores and uncertainty
Dimension	Current estimate /10
Mechanism novelty	6–8
Problem value	8–9
Potential advantage	6–8
Technical feasibility	7–9
Adoption feasibility	6–8
Falsifiability	9
Defensibility	5–7
Evidence confidence	5–7
Fatal-risk severity, 10 worst	4–6

The most uncertain score is mechanism novelty. The search found adjacent work on local personalization, contextual-integrity filtering, selective disclosure, personal data stores and private agent memory, but not a close match for the combination of model-generated restricted personalization programs + execution against persistent user-controlled memory + counterfactual minimum egress. That does not establish universal novelty. Particularly important remaining prior-art territory is patents around private client-side computation, personal-data stores and server-supplied personalization functions.

The other uncertain score is advantage magnitude. Research supports the general premise that unnecessary personal information can be removed while preserving meaningful personalization, and recent work demonstrates a privacy/utility benefit from task-essential disclosure. But that does not yet establish that the PBMC abstraction is expressive enough for general daily assistants.

Verdict

Differentiated architecture, with a potentially novel mechanism whose exhaustive novelty remains unverified.

The strongest defensible invention is not a more private memory database. It is a new memory interface contract:

personal AI memory is user-controlled computation over private state; retrieval of personal records is an exceptional operation, not the default.

Its strongest causal advantage survives removal of the branding, encryption, embeddings, and even the particular database technology: the AI sends a bounded personalization program to the data, the user-controlled kernel executes it, and only task-essential decision effects are allowed to leave.
