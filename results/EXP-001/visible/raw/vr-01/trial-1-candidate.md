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
