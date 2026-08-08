# EXP-001 Blind Judge — vr-01-t3-simplicity

You are evaluating two anonymized answers to the same task. You must not infer or speculate about which system produced A or B. Judge only the text shown.

Evaluator role: `simplicity`
Independence level for this run: `separate_context_same_model`

Act as a simplicity judge. Prefer the smallest intervention that solves the real problem. Penalize unnecessary invention, technology stacking, needless complexity, and failure to recognize a stronger simple substitute.

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
  "pair_id": "vr-01-t3",
  "evaluator_id": "vr-01-t3-simplicity",
  "evaluator_role": "simplicity",
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

# Blind pair vr-01-t3

## Task

Design a daily-use AI memory mechanism that improves personalization while keeping raw personal data under user control. Avoid a generic vector database plus privacy claims.

## Output A

I used the attached NOVUM instructions as the governing methodology for this run.

1. Problem reframing

The challenge is:

Achieve useful day-to-day personalization across AI interactions for an individual, while keeping the raw historical evidence that defines the person in user-controlled storage, outperforming provider-held memory and local-RAG approaches without requiring the user to manually curate a profile or accept a weak fully-local model.

The strongest practical baselines pull in opposite directions. Products such as ChatGPT and Gemini can personalize from saved information and prior conversations, but their memory mechanisms are integrated with provider services rather than being a user-owned computational boundary. At the other extreme, personal data stores such as Databox/Solid-style systems improve custody but do not themselves solve how a powerful remote model should use that data safely and efficiently.

The central contradiction is therefore:

The better the model knows the user, the more private state conventional architectures tend to put into the model's context.

That assumption—not the database—is what needs to be removed.

2. Frontier and opportunity gap

The saturated region is memory-as-content: chat-history retrieval, extracted facts, summaries, embeddings, vector search, and knowledge graphs. Mem0, for example, extracts and consolidates conversational information and also explores graph memory; this substantially improves long-term recall but still treats memory primarily as information to retrieve.

The emerging frontier is more interesting. MemPrivacy performs sensitive-span handling at the edge before cloud memory processing; P³ keeps a private profile client-side and modifies server-generated speculative text locally; Mi-Memory emphasizes typed evidence, provenance, lifecycle management, and deployment; and User as Code represents users as typed executable state rather than bags of retrieved facts.

That leaves a narrower neglected gap:

Can the remote model produce useful intelligence without ever consuming the user's memory at all—by making the memory act on the model's output instead?

That is the opening worth pursuing.

3. Assumption graph

The conventional pipeline assumes that personalization works by moving relevant user information toward generation:

private history
     ↓
extract / embed / summarize
     ↓
retrieve relevant memory
     ↓
put memory into model context
     ↓
personalized generation

Three assumptions are conventions rather than laws: that memories must be represented as descriptive facts, that relevant memories must become model inputs, and that the generative model must itself perform the final personalization decision.

Recent executable-memory work already breaks the first assumption. P³ partially breaks the second by keeping the profile client-side, but uses an interactive token-modification process between local personalization and server generation.

The remaining bottleneck is the third assumption.

4. Mechanism-diverse candidate portfolio
Candidate	Mechanism	Irreducible difference	Prior-art verdict
A. Profile Oracle	Convert history into typed local state and executable functions; cloud AI calls predicates/aggregates rather than retrieving text.	Memory becomes computation rather than documents.	Collision. User as Code already establishes executable typed user memory; generic function calling is mature.
B. Local Draft Personalizer	Cloud creates an ordinary answer; a private local model rewrites it using user history.	Personalization occurs after remote generation.	Kill. This is too close to P³'s private client-side modification of server-generated text.
C. Memory Leases	Local vault exposes signed, purpose-limited, expiring derived views rather than raw history.	Disclosure is capability-bound and temporary.	Incremental. Personal data stores, selective views, purpose-bound access, and edge redaction already cover much of the mechanism space.
D. Output-Side Memory VM	The cloud produces a personalization-neutral answer program containing choices, slots and alternatives. User-owned memory executes locally as acceptance tests, utility functions and slot-fillers over that program.	Memory never becomes model context; it determines which model outputs survive.	Survivor. Components exist separately, but I found no close match for this one-way memory-as-output-test architecture.

Candidate D is structurally different on the important axes: memory representation, insertion point, disclosure unit, control locus, and generation interface.

5. Anti-fake-novelty gate

Removing branding and familiar components, the surviving innovation delta is:

Represent personal memory primarily as a user-owned executable test suite over proposed AI outputs, while forcing the remote model to return a composable, personalization-neutral answer program rather than a personalized final response.

The local system resolves that program privately. It does not retrieve personal memories into the remote prompt, send profile summaries, reveal executable rules, or report which alternative the user-specific engine chose.

This matters because simply saying “local,” “encrypted,” or “user-owned” is insufficient: recent work explicitly argues that on-device deployment alone does not control derived state, information flows, authority, or telemetry.

6. Red-team and rejected ledger
Attack	Disposition
The cloud's alternatives may not contain anything appropriate for this particular person.	Repair: require a structured answer language with composable branches rather than several complete drafts; a small local composer may combine compatible branches.
Executable memory itself collides with User as Code.	Constrain: executable memory is not the novelty claim. The claimed delta is applying private memory as an output acceptance/runtime layer while the remote model remains memory-blind.
Local rewriting collapses back into P³.	Constrain: no token-by-token feedback loop to the server. The normal path is one remote generation followed by entirely local resolution.
A malicious provider could infer memory from which revision the client requests.	Repair: remove personalized retry feedback. If the candidate space is insufficient, local generation handles the repair or the client requests a generic larger candidate space independent of the failed private rule.
Automatic memory extraction may learn false beliefs about the user.	Repair: every executable rule carries provenance, confidence, expiry and counter-evidence. Third-party statements cannot silently become identity-level rules.
Open-ended creative tasks cannot always be reduced to predicates.	Constrain: the strongest operating regime is decisions, recommendations, planning, recurring workflows, formatting/style adaptation, commitments and personal-state constraints. Deep reasoning over private prose routes to a capable local model or explicit selective disclosure.
The approach could create enormous cloud outputs.	Test: daily-use viability is conditional on a compact answer bytecode producing sufficient diversity without roughly doubling inference cost.

The rejected mechanisms remain rejected: adding vectors, moving RAG to localhost, wrapping memory in encryption, and ordinary profile summarization do not return under new names.

7. Evolution lineage

The survivor improves in two mutations.

D0 — Output verifier. The remote model creates several candidate answers and private rules rank them locally. This is useful but wasteful.

D1 — One-way personalization. Remove all personalized feedback to the remote model. The cloud sees neither memory contents nor the chosen candidate. This creates a much cleaner privacy boundary, but candidate coverage becomes the weak assumption.

D2 — Answer Bytecode + Memory Test VM. Replace whole candidate answers with a compact intermediate representation. The cloud returns clauses, alternatives, typed slots and public metadata; the local runtime executes private constraints and utilities to select, fill and compose them.

D2 is the winner.

8. Winning invention: Memory Test VM

The system has five principal components.

                USER-CONTROLLED DOMAIN
┌──────────────────────────────────────────────────────────┐
│ Raw Evidence Vault                                      │
│ chats • calendar • files • feedback • app events        │
│              ↓                                           │
│ Memory Compiler                                          │
│ evidence → state + tests + utilities + provenance       │
│              ↓                                           │
│          Memory Test VM  ←──── Answer Bytecode ─────┐    │
│              ↓                                      │    │
│       Local Surface Composer                        │    │
│              ↓                                      │    │
│       personalized final answer                     │    │
└─────────────────────────────────────────────────────│────┘
                                                      │
                                             REMOTE MODEL
                                         current task only
                                         → Answer Bytecode

A memory is not principally stored as:

"User prefers quiet hotels."

It becomes something closer to:

rule HOTEL_NOISE:
  applies_when: task.category == "lodging"
  evidence: [E184, E921, E1042]
  confidence: 0.91
  expires_if: counterevidence >= 2
  score(candidate):
      quiet_room_confirmed    +3
      nightlife_district      -2
      known_street_noise      -3

Another memory may be a hard acceptance test:

rule SCHEDULING:
  reject(event) if overlaps(committed_calendar_block)

Others are private slot functions:

slot HOME_AIRPORT() -> local state
slot NORMAL_BUDGET("dinner") -> local range
slot WRITING_FORMALITY("manager") -> 0.78

The remote model does not receive those values or rules.

Instead it might return:

PLAN
  recommendation_set:
    A {price: medium, transit: high, atmosphere: lively}
    B {price: medium, transit: medium, atmosphere: quiet}
    C {price: low, transit: high, atmosphere: casual}

  response:
    "I'd choose {{best(recommendation_set)}} because {{public_reason}}."

The Memory Test VM privately scores A/B/C, rejects rule violations, fills private variables and renders the final response.

The provider never needs to learn why B was selected—or even that B was selected.

Why this could beat the strongest alternatives

Against provider memory, the structural advantage is custody: historical evidence and derived personal state remain in the user's domain rather than becoming provider memory. Current mainstream memory systems offer deletion and control mechanisms, but their personalization still depends on provider-accessible saved information or conversation history.

Against local RAG, the advantage is that private history does not need to be retrieved and injected into a powerful cloud model.

Against fully local AI, the architecture retains access to a frontier remote model for the expensive general reasoning step.

Against P³, the difference is one-way operation: P³ repeatedly evaluates and modifies server-generated token drafts using a retrieved private profile, whereas Memory Test VM asks the server for a neutral response program and performs personalization afterward without revealing its decisions.

Against User as Code, it changes what the executable user model controls: not merely queries and state computations, but the acceptance semantics of another model's outputs.

9. Daily-use mechanics and falsification test

The raw vault should be an ordinary user-portable encrypted store, not a proprietary “AI memory database.” Connectors copy or reference permitted data; every derived rule retains pointers to evidence. Deleting a source invalidates rules that can no longer meet their evidence threshold. Corrections produce new versioned state instead of silently rewriting history.

Compilation runs incrementally when the device is idle. Normal inference requires only one cloud call plus local deterministic execution. A small local language model is optional for translating unstructured evidence into proposed rules and polishing final prose; it is not trusted as the canonical memory store.

The decisive falsification test is to implement only three daily task classes—restaurant/recommendation choice, calendar planning, and personalized writing—and compare Memory Test VM with a full-profile cloud baseline and no-memory baseline on hidden user constraints.

The architecture survives only if it can recover at least roughly 85% of the personalization benefit of the full-profile system while sending zero historical raw-memory items to the remote model, maintaining at least 95% hard-constraint compliance, and keeping cloud-output expansion below roughly 2× an ordinary answer. If personalization drops below about 70% of the full-profile baseline or adequate candidate coverage consistently requires huge branch sets, the core advantage claim is weakened enough to kill or sharply narrow the concept.

That test isolates the central assumption: does a model need to know the user, or merely generate a sufficiently expressive decision surface that user-owned memory can resolve?

10. Scores, uncertainty and verdict
Dimension	A: Oracle	B: Rewriter	C: Leases	D2: Memory Test VM
Mechanism novelty	4	2	4	7 [6–8]
Problem value	8	8	8	9
Advantage magnitude	7	7	6	8 [6–9]
Technical feasibility	8	7	8	7
Adoption feasibility	7	7	6	7
Testability	9	9	8	9
Defensibility	5	3	5	7
Evidence confidence	8	9	7	5 [4–7]
Fatal-risk severity	3	2	4	5

The two numbers most likely to move are mechanism novelty, because output-side personalization and programmable-agent literature is moving quickly, and advantage magnitude, because the answer-bytecode coverage problem is not yet demonstrated.

The calibrated verdict is potentially novel mechanism, not a universal novelty claim. Search found close ingredients—user-controlled personal data stores, executable memory, client-side personalized generation, privacy firewalls, typed lifecycle memory and purpose-bound disclosure—but not a close mechanism that makes persistent personal memory an executable, one-way acceptance runtime over a memory-blind remote model's structured output.

The largest remaining prior-art risk is research or patent work combining private preference functions with structured candidate generation or client-side output selection. If a close system already uses that same one-way architecture—not merely local reranking or rewriting—the verdict should fall to incremental recombination.

## Output B

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

