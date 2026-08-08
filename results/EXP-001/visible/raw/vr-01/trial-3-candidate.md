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
