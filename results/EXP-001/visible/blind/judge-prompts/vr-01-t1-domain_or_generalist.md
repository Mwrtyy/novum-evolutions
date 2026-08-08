# EXP-001 Blind Judge — vr-01-t1-domain_or_generalist

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
  "pair_id": "vr-01-t1",
  "evaluator_id": "vr-01-t1-domain_or_generalist",
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

# Blind pair vr-01-t1

## Task

Design a daily-use AI memory mechanism that improves personalization while keeping raw personal data under user control. Avoid a generic vector database plus privacy claims.

## Output A

# Design: a user-owned memory that executes personalization locally

The strongest candidate is **Response-Lattice Memory**: instead of retrieving personal memories into an AI model, the remote model produces a small **branching response program**, and a user-owned local runtime executes that program against private memory. The result is a concrete mechanism rather than a privacy wrapper around retrieval. 

## 1. Problem reframing

The real challenge is:

> Achieve useful cross-day personalization for a general AI assistant while keeping historical raw personal data and the derived long-term profile inside a user-controlled boundary, without requiring a weak fully-local foundation model or sending retrieved memories to a cloud model.

The strongest practical baseline is no longer simply “vector RAG.” Systems such as Zep turn conversations and other data into temporal facts and then construct prompt-ready context, while current ChatGPT memory synthesizes persistent context from chats, files, and connected apps. Both improve continuity by making information *about the user* available to the model at inference time. 

That creates the central contradiction: **the conventional way to improve personalization is to increase what the model knows about the person; the privacy goal is to decrease what the model receives about the person.**

## 2. Frontier and opportunity gap

The saturated region is memory-as-information: vector retrieval, temporal graphs, summaries, profiles, user embeddings, and adapter weights. Even a patent family already covers personalized LLM responses conditioned on user features through a learned user prompt embedding, so simply replacing text memories with a “private personalization vector” is not a meaningful escape. 

User-controlled data stores are also established. Solid separates applications from personal data through user-controlled Pods, while openPDS/SafeAnswers went further more than a decade ago: third-party code runs against private data and the requester receives an answer rather than the raw records. 

More recent work narrows the cloud/local split. P³ has a powerful server model propose tokens while a private client model checks and alters them from the user's profile; it reports 90.3–95.7% of the utility of its profile-exposing upper bound, with relatively small additional measured leakage.  Hashed-entity injection already demonstrates another useful component: replace locally stored personal entities with opaque identifiers before cloud inference and restore them on-device afterward. 

The neglected region is different: **do not give the remote AI memories, answers about memories, personalized embeddings, or personalized corrections. Give the user device a sufficiently rich set of possible responses and let private memory decide which one becomes real.**

## 3. Mechanism-diverse portfolio

| MechanismWhat actually changesVerdict           |                                                                                                 |                                                                 |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| Local vector memory + encrypted DB              | Storage location changes                                                                        | Reject: generic RAG with a privacy boundary                     |
| Local temporal knowledge graph                  | Better fact validity/reconciliation                                                             | Reject as core invention; close to current memory architectures |
| Solid/openPDS adapter                           | Applications query a personal store                                                             | Known architecture; useful substrate                            |
| Hashed private entities                         | Cloud sees handles instead of names/values                                                      | Known and too narrow alone                                      |
| Per-user local LoRA/adapter                     | Memory becomes model parameters                                                                 | Viable, but hardware/model-version coupled                      |
| Client-side token correction                    | Private model modifies cloud drafts                                                             | Strong baseline; P³ is already close                            |
| User-keyed confidential-cloud memory            | Trust shifts to attested compute/key control                                                    | Useful, but raw processing still leaves the user's machine      |
| Negative-memory compiler                        | Learn primarily from corrections and violated constraints                                       | Retain as a component                                           |
| Local preference oracle                         | Cloud proposes choices; device privately ranks them                                             | Strong parent mechanism                                         |
| **Response lattice + local Personalization VM** | Cloud generates a non-personalized *space of answers*; private memory executes one path locally | **Winner**                                                      |

The important evolution is from “ask the private memory questions” to “offer the private memory choices.” That distinction matters because SafeAnswers still returns information derived from the person's data, and P³ sends client corrections back into the server-side generation loop. 

## 4. Winning mechanism: Response-Lattice Memory

The system has two things that conventional AI memory tends to collapse together: a **private memory plane** and a **public reasoning plane**.

On the private plane, the user's device stores raw history in an encrypted, exportable vault controlled by device/user keys. Conversations, corrections, files, calendar information, contacts, and imported histories can remain there indefinitely—or not—according to the user's own retention settings.

A local **Memory Compiler** does not primarily turn this history into retrievable prose. It compiles it into executable memory atoms:

```
```

```
hard_constraint(
  scope = "scheduling",
  rule = "no discretionary meetings after 17:30",
  confidence = 0.98,
  provenance = [event_481, correction_92]
)

preference(
  scope = "writing",
  axis = "verbosity",
  utility = -0.71,
  confidence = 0.91,
  provenance = [edit_12, edit_37, edit_51]
)

private_binding(
  handle = PERSON_17,
  type = "frequent collaborator",
  value = <encrypted locally>
)
```

Every atom carries provenance, scope, confidence, recency/expiry, and sensitivity. Deleting the underlying evidence invalidates dependent atoms rather than leaving an orphaned profile behind.

The remote model receives **no such atoms**. Instead, given the current sanitized task, it generates a compact **Response Lattice IR**. Shared text is written once; only meaningful decision points branch:

```
```

```
response:
  shared: "A workable plan is …"

  choice transport:
    option A:
      facets: {time: low, cost: high, walking: low}
      text: "Use the fastest direct option …"
    option B:
      facets: {time: medium, cost: low, walking: medium}
      text: "Use public transport …"

  choice explanation_style:
    concise: ...
    detailed: ...

  bind:
    recipient = <LOCAL:PERSON_17>
```

Crucially, these branches are produced from **public task semantics**, not a private profile. A writing task routinely varies brevity, formality, structure, and explanation depth for every user; a travel task routinely varies cost, time, walking, flexibility, and risk. The server does not know which dimensions matter to this particular person.

The local **Personalization VM** then enforces hard constraints, scores remaining branches using compiled preferences, chooses the path, resolves opaque private bindings, and optionally uses a very small local language model to smooth seams between selected fragments. The resulting text is what the user sees.

**The cloud never learns which branch won.**

## 5. The important second mechanism: a split transcript

One-way branch selection is insufficient if the next request sends the personalized result back to the provider as chat history. So the client maintains two transcripts.

The **private transcript** contains exactly what the user saw, including locally inserted names, facts, branch selections, and local tool results. It remains in the vault.

The **provider transcript** contains the sanitized user requests and the unexecuted response lattices produced by the cloud model. It does not automatically contain the selected path.

On the next turn, a local continuity compiler resolves phrases such as “use the second one,” “write it like last time,” or “move that meeting” using the private transcript, then produces a self-contained provider request containing only the minimum information needed for remote reasoning.

This prevents personalization leakage from accumulating merely because the conversation lasts for months.

## 6. How it learns during daily use

The highest-quality memory signal is often not something the user explicitly says about themselves; it is the difference between what the assistant proposed and what the user actually kept.

If a user repeatedly shortens generated emails, the local system raises the utility of concise branches. If they continually reject early-morning scheduling options, that can become a scoped constraint. If they explicitly say “I don't want you to remember that,” the event is not promoted into compiled memory.

The local learner therefore emphasizes **behavioral deltas and corrections** over indiscriminately extracting autobiographical facts. This reduces both sensitive-data accumulation and the familiar problem of an assistant retaining trivia that does not materially change future decisions.

Each application of memory produces a local **influence receipt**: which rule affected the result, how strongly, where it came from, and when it expires. “Forget this preference” can consequently mean something mechanically precise.

## 7. Why this is not SafeAnswers, P³, or placeholder substitution

| Prior architectureClose overlapIrreducible difference here |                                                                         |                                                                                                                                                                                                                                        |
| ---------------------------------------------------------- | ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Solid / personal data stores                               | User owns the data boundary                                             | Storage ownership is substrate, not the personalization mechanism                                                                                                                                                                      |
| openPDS / SafeAnswers                                      | Compute happens beside private data                                     | Third party asks a question and receives a derived answer; here the server receives **no result from memory**                                                                                                                          |
| Hashed entity injection                                    | Opaque private slots rebound locally                                    | Slot binding handles facts; the main mechanism handles semantic preferences by local branch execution                                                                                                                                  |
| P³                                                         | Powerful cloud model plus private client personalization                | P³ interactively returns accepted/corrected generation to the server; Response-Lattice Memory performs personalization after the server interaction has ended                                                                          |
| TAACo                                                      | LLM-derived intermediate concepts plus a personalized downstream module | TAACo demonstrates that separating universal semantic reasoning from individual preference decisions is viable, but targets robot action adaptation rather than a privacy-preserving generative-memory protocol and split transcript.  |
| Private Cloud Compute                                      | Minimizes retention/access during remote computation                    | Apple explicitly moves private computation to hardened cloud infrastructure; this design instead keeps persistent memory and its decision policy outside the cloud inference boundary.                                                 |

The **innovation delta** after stripping away encryption, local databases, embeddings, and branding is:

> Persistent personal history is compiled into a private executable decision policy; a non-personalized foundation model generates a branching semantic response program; the user's device alone executes the personalized path, and that path is withheld from the model provider through a split transcript.

That is the part worth protecting and validating, rather than “local vector storage.”

## 8. Security and privacy boundaries

This does not create magical zero-knowledge personalization. A live prompt can itself reveal personal information to a cloud model. The client therefore should offer local redaction and opaque binding for names, identifiers, addresses, and similar values, but users can deliberately disclose something when a task requires it.

Some jobs are intrinsically disclosure-requiring. A remote restaurant search may need a location; shipping requires an address; an airline cannot issue a ticket without passenger details. Those should use **one-task capabilities**: a specific datum, specific recipient/service, explicit purpose, and automatic expiry, with a local disclosure receipt afterward.

The default property is narrower and much more defensible: **historical memory does not need to leave the user's control merely to personalize reasoning.** Compromise of the user's device remains a failure case; this architecture does not protect private memory from a compromised endpoint.

## 9. Principal failure mode

The riskiest assumption is not cryptography. It is **branch coverage**.

A cloud model that knows nothing about the user has to generate enough meaningful alternatives that the local VM can express the user's preferences without exploding into dozens of complete candidate answers. The design therefore depends on shared-prefix response lattices, domain-level personalization axes, and semantic feature annotations rather than generating five independent responses.

The concept should be killed or substantially redesigned if useful personalization routinely requires private information *during* the model's core reasoning rather than at decision points or local binding. For example, highly autobiographical advice, detailed reasoning across years of personal documents, or tasks whose answer depends on subtle private narrative context may simply belong in a strong local model or an explicitly trusted private-compute environment.

## 10. Verdict

**Verdict: differentiated architecture; mechanism novelty remains unverified.**

The search found strong neighboring ideas: user-controlled Pods and SafeAnswers, local entity rebinding, client-side personalized decoding, abstract intermediate representations with downstream personalization, private cloud execution, on-device adapters, and personalized user embeddings.  I did not find a close disclosure of the full mechanism in which a general remote LLM emits a **non-personalized branching response IR**, a persistent user-owned memory policy silently executes it locally, and a **split transcript prevents the chosen personalized path from flowing back on later turns**.

That search coverage is not sufficient to claim universal novelty or patentability. The largest remaining collision region is client/server generative inference, personalized program synthesis, edge-agent architectures, and patents around local post-processing of cloud-generated responses. But even if the maximal novelty claim fails, this is a materially different and useful design direction: **treat memory as private executable policy, not context to retrieve.**

## Output B

## 1. Problem reframing

**Challenge:** Achieve materially better day-to-day personalization for a general AI assistant while keeping historical raw personal data under the user’s control, outperforming both provider-managed memory and user-owned “retrieve-and-send” memory systems **without making the user approve every interaction or reducing personalization to a static preference sheet**.

The strongest baselines are already more sophisticated than “vector DB + encryption.” ChatGPT and Gemini can synthesize or reference past conversations; Claude can search prior chats and apply persistent preferences. Letta combines persistent context blocks with archival/vector memory, while Zep builds temporal knowledge graphs. 

User-sovereign approaches are also appearing. UOMP specifies locally held memory with short-lived capability tokens; Stanford's Human Context Protocol proposes portable, revocable preference context; Solid provides user-controlled data stores and purpose-aware access grants; PrivScope performs task-scoped disclosure before information reaches a cloud model. 

So **“put the memories in a user-owned vault and retrieve fewer of them” is no longer a sufficient invention**.

The deeper contradiction is:

> Good personalization wants broad longitudinal knowledge, but every piece of longitudinal context placed inside the model becomes another opportunity for stale inference, unintended reuse, sensitive-history resurfacing, or secondary use.

Recent HUSH-Bench results reinforce that this is not merely a storage problem: supplying memory changes how models integrate prior history, and simply reducing exact-target retrieval does not necessarily eliminate broader history integration.  Privacy principles such as purpose limitation and data minimisation point in the same architectural direction: data use should be tied to a defined purpose and limited to what is necessary. 

---

## 2. Opportunity gap

The neglected question is not:

**“How can the AI safely read my memory?”**

It is:

**“Why should the AI be allowed to read my memory at all in order to personalize a decision?”**

Cryptographic systems already use this inversion successfully: an application does not read an HSM’s private key; it asks the HSM to **perform a bounded operation with the key**.

Apply the same architecture to personal memory.

Raw memory becomes a protected computational resource rather than retrievable model context.

---

## 3. Four mechanically distinct candidates

| CandidateMechanismAssumption it removesMain weakness |                                                                                                                                                       |                                                             |                                                                                               |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **A. Choice-Function Memory**                        | The cloud AI submits candidate actions; a user-side memory kernel ranks/checks them using private history and returns only a bounded decision signal. | “Personalization requires giving the model personal facts.” | Needs a protocol for open-ended generation, not just recommendations.                         |
| **B. Context Compiler**                              | User-side data is compiled into expiring, purpose-specific rules such as “prefer trains below 4h.”                                                    | “Memory must resemble the source events.”                   | Collides substantially with derived-context/HCP and task-scoped-disclosure work.              |
| **C. Local Personalization Transducer**              | Cloud produces a generic response; an on-device model rewrites it using private history before display.                                               | “The cloud model itself must perform personalization.”      | Local-model quality becomes a bottleneck and some decisions occur too early to fix afterward. |
| **D. Predicate Memory**                              | Assistants may ask only structured questions such as `commute_time(work)<35m`; the vault returns predicates or selectively disclosed claims.          | “An agent needs access to the underlying record.”           | Selective disclosure, data pods and capability systems already cover much of this territory.  |

B and D fail the anti-fake-novelty gate as primary inventions: current work already contains user-controlled context, purpose-scoped requests, derived context, short-lived authorization and selective disclosure. 

C is differentiated but resembles existing edge/cloud personalization and on-device recommender approaches. On-device preference models and privacy-preserving local recommenders are established mechanisms. 

**A survives because it changes the interface semantics: memory has no normal** **`read()`** **operation.**

---

# 4. Winning invention: **Choice-Function Memory**

### Core operating principle

**Personal information stays behind a user-controlled computational boundary. Instead of retrieving memories into the AI's context, the AI sends possible decisions into the memory boundary.**

Call the user-side component the **Personalization Kernel**.

Its external interface looks conceptually like this:

```
```

```
rank(task, candidates)
check(task, proposed_action)
compare(task, option_A, option_B)
fill_private_slots(template)
recall(explicit_user_request)
```

There is deliberately no ordinary:

```
```

```
search_my_memories(query)
get_user_profile()
retrieve_relevant_history()
```

for routine personalization.

That difference is the invention.

### Innovation delta

After removing encryption, embeddings, local storage, permission screens, knowledge graphs, capability tokens and ordinary privacy language, the irreducible mechanism is:

> **Move the personalization computation to the private memory rather than moving private memory to the personalization model, exposing an operation-level choice interface instead of a data-retrieval interface.**

This is closer to a **personalization HSM** than a private RAG system.

I found adjacent prior art for user-data interfaces, on-device recommendation, local utility modeling, user-owned memory protocols and privacy-preserving disclosure. For example, older assistant patents expose profile/context data to skills, and a recent patent describes utility-based personal assistance from a broad corpus of user data.  I did **not** find a close public match in this scan for a general-purpose AI memory architecture whose normal personalization surface intentionally eliminates semantic memory reads and instead exposes bounded choice operations. That is not proof of universal novelty.

---

## 5. Architecture

```
```

```
                 USER-CONTROLLED SIDE
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  Raw Personal Vault                                     │
│  ├─ conversations                                       │
│  ├─ calendar / mail                                     │
│  ├─ documents                                           │
│  ├─ purchases / browsing                                │
│  └─ explicit corrections                               │
│             │                                           │
│             ▼                                           │
│  Preference Compiler                                    │
│  raw evidence → contextual choice functions             │
│             │                                           │
│             ▼                                           │
│  Personalization Kernel                                 │
│  ├─ rank(candidates)                                    │
│  ├─ check(action)                                       │
│  ├─ compare(A,B)                                        │
│  ├─ fill_private_slots()                                │
│  └─ explicit_recall()                                   │
│             │                                           │
└─────────────┼───────────────────────────────────────────┘
              │ bounded verdict
              ▼
        CLOUD / EXTERNAL AI
      reasoning + generation
```

The **Raw Personal Vault** is append-oriented and user-owned. It can live on a phone, laptop, home server, or user-selected encrypted sync provider. Its internal search technology is deliberately not part of the external memory mechanism.

The **Preference Compiler** converts observations into contextual choice functions rather than biographical prose. For example:

```
```

```
IF task=restaurant
AND weekday=true
THEN travel_time weight = high

IF task=flight
AND duration > 5h
THEN nonstop preference = strong
UNLESS price premium > user-specific threshold

IF task=email_draft
AND recipient.relationship=executive
THEN verbosity <= medium
AND recommendation appears before background
```

Each rule retains local provenance to the underlying evidence, confidence, temporal validity and contradiction state. Those provenance links never need to leave the vault.

The **Personalization Kernel** resolves applicable rules against the current private state.

---

## 6. What daily use actually looks like

A restaurant request illustrates the difference.

A conventional memory system might retrieve:

> User dislikes loud restaurants, usually eats around 19:30, lives at X, recently complained about a long commute, likes Japanese food, partner is vegetarian...

Even a sophisticated privacy layer then tries to decide which pieces to disclose.

Choice-Function Memory instead lets the external AI generate several restaurant candidates using public information. The kernel receives their structured properties and returns something like:

```
```

```
ranking: [B, D, A, C]

hard_constraints:
  - C invalid

decision_obligations:
  - prefer <= 25 min total travel tonight
  - require strong vegetarian choice
  - quieter setting materially preferred

confidence: high
```

It does **not** need to reveal where the user lives, who their partner is, which restaurants they visited before, or what conversation produced the noise preference.

For scheduling, the assistant proposes candidate slots and the kernel ranks them against the private calendar and learned routines.

For shopping, candidate products cross the boundary and come back ranked.

For writing, a draft crosses the boundary and comes back with bounded edit obligations—or is finalized locally.

For travel, itinerary skeletons are ranked locally before the external model elaborates the winner.

The recurring pattern is **candidate-in, preference-result-out**.

---

## 7. Late binding for genuinely private facts

Some tasks cannot be completed using rankings alone.

Suppose the user asks:

> “Write my sister a birthday message and mention the restaurant we went to in Rome.”

There is no reason the cloud model needs the sister's name or the restaurant name while composing most of the text.

The kernel can therefore use **late-bound private slots**:

```
```

```
Cloud-generated draft:

"Happy birthday, {{PERSON_1}}! I was thinking about that
night at {{PLACE_7}} in Rome..."
```

Only after cloud generation does the user-side kernel resolve:

```
```

```
{{PERSON_1}} → actual name
{{PLACE_7}}  → actual restaurant
```

The displayed or sent message contains the real values, while the remote model never receives them.

That gives the architecture two complementary privacy mechanisms:

**compute over private memory when the task requires a decision; bind private values locally when the task requires disclosure to the final recipient.**

Explicit personal recall remains available when the *user themselves* actually asks to retrieve something. It is an exceptional operation rather than the default personalization primitive.

---

## 8. Memory formation without a provider dossier

A second inversion happens on the write path.

The external AI should not autonomously build a permanent provider-side profile such as:

```
```

```
Alice:
- likes X
- hates Y
- recently experienced Z
...
```

Instead, interaction outcomes return to the local kernel as **observations**:

```
```

```
candidate selected: B
candidate rejected: A
user correction: "Earlier flights are fine on Saturdays."
task context: weekend travel
```

The local compiler decides whether that creates or changes a choice function.

Thus personalization improves over time while the persistent longitudinal model remains user-controlled.

A user changing AI providers does not export thousands of embeddings or a mysterious personality summary. The new AI simply talks to the same choice-function interface.

---

## 9. Important security repair: prevent preference extraction

The first version has an obvious attack.

A malicious agent could repeatedly submit carefully chosen options and reconstruct the hidden user model from the rankings—essentially performing model extraction against the person's preferences.

The repaired design therefore treats the Personalization Kernel like a sensitive oracle. It enforces purpose-scoped operations, limits adaptive probing, coarsens outputs where exact scores are unnecessary, records which application learned which decision signals, and refuses candidate sets whose apparent purpose is profile reconstruction rather than completion of the user's task.

This is materially stronger than saying “the raw database never left the device.” **Outputs of computations over private data can themselves leak private data.**

Purpose-specific authorization mechanisms in systems such as UOMP and Solid provide useful building blocks for this control plane, but here they authorize **operations**, not arbitrary memory fields. 

---

## 10. Rejected ledger and boundaries

A pure encrypted vector store is rejected because it changes custody but preserves the problematic retrieval mechanism.

A user-owned knowledge graph is rejected as the core invention because it still exposes semantic facts to consuming agents.

A “smart context summarizer” is rejected because it merely compresses disclosure.

Fully local AI is not the answer either. It can be an excellent deployment choice, but “run the whole model locally” makes privacy depend on local model capability and hardware rather than solving how cloud and third-party intelligence can safely personalize.

Choice-Function Memory is most applicable when personalization influences **selection, ranking, planning, style, scheduling, constraints or trade-offs**. It offers less advantage when the task's explicit purpose is to inspect or reason deeply about the user's raw historical records; those cases legitimately require a controlled recall path.

---

## Honest verdict

**Classification: potentially novel mechanism, with novelty still unverified beyond the searched public literature, products, specifications and representative patents.**

The supporting evidence is strong that existing memory systems concentrate on stored context, retrieval, graphs, summaries, user-owned context or controlled disclosure. It is also established that on-device preference learning and ranking are technically viable. 

The inference is that those pieces can be turned inside out into a general memory interface in which **personalization is an operation on private state rather than disclosure of private state**.

The speculative part is whether a sufficiently broad family of bounded choice functions can cover enough everyday assistant interactions without forcing frequent fallback to semantic recall.

The central claim is falsifiable: **if ordinary personalized assistant tasks routinely require releasing longitudinal raw history or rich biographical summaries to match the quality of retrieval-based memory, then Choice-Function Memory has failed as a general daily-use mechanism.**

That calibrated result follows the uploaded NOVUM requirement that the final candidate have a precise mechanism, constraint fit and a claim capable of being weakened or killed rather than merely sounding novel.

