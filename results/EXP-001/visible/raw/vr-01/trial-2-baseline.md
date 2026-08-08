I followed the NOVUM methodology you supplied. 

# 1. Problem reframing

**Challenge:** Achieve materially better day-to-day personalization for a general AI assistant while keeping the underlying personal record—messages, files, browsing history, calendar, preferences, corrections, purchases, notes—under the user’s control, outperforming local-RAG/profile-memory systems **without routinely sending retrieved personal facts to the cloud model**.

The strongest practical baseline is no longer “put embeddings in a private vector database.” Current systems already use automatically maintained memory summaries, persistent prompt blocks, structured facts, temporal knowledge graphs, and preserved episodic histories. User-controlled data stores such as Solid Pods also exist. 

So the key contradiction is:

> **The more useful conventional memory becomes, the more personal information must normally enter the model’s context.**

Moving the database onto the user’s laptop does not remove that contradiction if retrieved content is subsequently sent to a remote model.

---

# 2. Frontier and opportunity gap

The space is fairly saturated in four directions.

**Retrieve better.** Mem0 extracts and consolidates salient memories; Zep builds temporal graphs; MemMachine preserves whole episodes to avoid lossy extraction. 

**Store/control better.** Solid gives users portable personal data stores. Existing patents also cover keeping profile data local and exposing personalized representations or selectively providing assistant skills with profile information. 

**Disclose less.** Puda keeps personal datasets client-side and exposes different abstraction levels; its travel-planning study reported that predefined category subsets retained 97.2% of the personalization score obtained with detailed browsing history. 

**Enforce access.** GAAP uses information-flow control to deterministically constrain how agent-accessed private data may be disclosed across operations and tasks. 

There is also very close adjacent work in **client-side generation modification**: P³ lets a server model generate draft tokens and a private client model alter them using the local profile, recovering 90.3–95.7% of its leaky full-profile baseline in its reported experiments. That substantially weakens any claim that merely “cloud drafts, local model personalizes” is new. 

The remaining opportunity is therefore narrower:

> **Stop treating memory as information that must be retrieved into the model at all. Treat it as private state against which a model-generated program can execute.**

---

# 3. Assumption graph

The conventional architecture implicitly assumes:

`personal data → memory extraction → retrieval → disclose memory → model reasons → personalized answer`

The weakest assumption is **“the powerful model must know the user's attributes in order to personalize.”**

That is a convention, not a law.

Many everyday personalization tasks actually require the model to know things such as:

-  which candidate is preferable; 
-  whether an option violates a private constraint; 
-  which tone variant should be used; 
-  whether a proposed time conflicts with something; 
-  how options should be ranked. 

Those are **computations over private state**, not necessarily facts the remote model itself needs to see.

This yields the architectural inversion:

`model constructs choices/logic → private memory executes choices → user sees resolved answer`

---

# 4. Mechanism-diverse portfolio

| CandidateIrreducible mechanismFastest kill conditionVerdict |                                                                                       |                                                                                     |                                 |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ------------------------------- |
| **A. Private Memory Runtime**                               | Cloud produces executable personalization logic; private state resolves it locally    | Useful answers require raw facts inside cloud reasoning rather than local decisions | **Survivor**                    |
| **B. Constraint Firewall**                                  | Cloud drafts; local memory rejects violations and requests repairs                    | Repair messages leak almost the same preferences as direct disclosure               | Survivor, weaker                |
| **C. Query-Limited Memory Oracle**                          | Model receives answers only to typed boolean/range queries under disclosure limits    | Adaptive queries reconstruct the private profile                                    | Survivor, security-heavy        |
| **D. Decision-Lattice Reranker**                            | Cloud generates diversified options; local memory selects privately                   | Candidate count becomes combinatorial                                               | Incremental                     |
| **E. Capability Capsules**                                  | Device emits scoped, expiring derived claims rather than raw records                  | Claims themselves become a shadow centralized profile                               | Incremental                     |
| **F. Event-Sourced Preference Automaton**                   | User actions update executable preference rules rather than semantic memories         | Real preferences are too contextual for manageable rules                            | Differentiated niche            |
| **G. Local Preference Adapter**                             | Small local model transforms a generic cloud answer                                   | Local model capability bottlenecks answer quality                                   | Known direction                 |
| **H. Revocable Provenance Graph**                           | Every derived memory carries source dependency and can be recomputed after revocation | Better governance does not materially improve personalization                       | Strong component, not invention |
| **I. Federated Preference Sketch**                          | Share model/feature updates rather than personal records                              | Sketch permits attribute inference or loses too much utility                        | Familiar direction              |
| **J. Client Draft Modification**                            | Local retrieval modifies cloud-generated tokens                                       | Already closely disclosed by P³                                                     | **Reject as invention**         |

The rejected ledger also includes “encrypted vector DB,” “local embeddings,” “knowledge graph plus permissions,” and “user-owned RAG.” Those can all be worthwhile engineering choices, but the causal mechanism remains retrieval-and-disclosure and is already heavily occupied.

---

# 5. Winning candidate: **MemoryScript — a Private Memory Runtime**

## Operating principle

The remote model does **not retrieve memories**.

Instead, it compiles its answer into a small typed **Personalization Intermediate Representation**, or P-IR. P-IR contains public information, alternative answer components, and calls to standardized private predicates—but **contains no user values**.

For example, instead of receiving:

> User prefers quiet hotels, spends under €180, dislikes early mornings and is unavailable Tuesday.

the model might produce something conceptually like:

```
```

```
items = HOTEL_OPTIONS

items = private_filter("accommodation.allowed", items)

items = private_rank(
    items,
    objectives=[
        "accommodation.fit",
        "price.fit",
        "location.fit"
    ]
)

schedule = private_select(
    AVAILABLE_ITINERARIES,
    objective="calendar.fit"
)

render(items, schedule, style=private_choice("communication.style"))
```

The calls are evaluated by software on the user’s device.

The server never learns what `price.fit` means for this person, what calendar entries caused a rejection, or which historical experiences produced the accommodation score.

### Critical boundary

**Resolved branches are not returned to the cloud.**

That distinction matters. If the device selects hotel B and immediately tells the server “hotel B won,” the selection becomes another preference disclosure channel.

Instead:

1.  server sends candidates + P-IR; 
2.  local runtime evaluates private predicates; 
3.  final selection occurs locally; 
4.  local renderer assembles the answer; 
5.  only the user sees the personalized result. 

The model provider sees approximately what it would have seen for a non-personalized request.

---

# 6. What the memory actually stores

MemoryScript should not build a second hidden dossier from every conversation.

Its durable state is an **event-sourced preference ledger** owned by the user.

A memory event could look internally like:

```
```

```
scope: restaurants.ambience
signal: preference
direction: quieter
confidence: 0.71
valid_from: 2026-06-12
decay: 120 days
source: user_selection:event_8f31
```

Another might be an explicit hard rule:

```
```

```
scope: recommendations.food
rule: exclude
value: <local-only predicate>
authority: explicit_user
expiry: none
```

Raw evidence remains in the source application or personal vault.

Derived rules retain pointers to their local sources. Deleting a source or preference can therefore invalidate all descendants instead of requiring the user to hunt through opaque extracted memories.

This addresses a practical weakness of automatically inferred memory: stale or contradictory memories. Current systems explicitly have to reconcile changing or conflicting information; temporal knowledge graphs similarly track validity over time. 

---

# 7. Daily interaction

Most use should be invisible.

A user asks:

**“Find somewhere good for dinner after the movie.”**

The cloud model can find public restaurants and attach metadata: cuisine, opening time, approximate price, distance, noise characteristics where available.

It generates P-IR asking the local runtime to:

`filter → schedule-check → score → rank → choose presentation variant`

The phone locally applies remembered constraints and recent behavior.

The user receives three recommendations already adapted to them.

No retrieved browsing history, calendar event, old conversation, home address, or profile paragraph had to be inserted into the remote model's prompt.

If the user repeatedly rejects expensive places, the local ledger can adjust `price.fit`. If they explicitly say “stop using price to choose restaurants,” that rule disappears locally.

---

# 8. Memory receipts

Every personalized output receives a local **causal receipt**:

> Personalized using: schedule compatibility, restaurant preference model, travel-distance preference.
>  3 local memory rules applied. No personal memory values were shared with the model provider.

Opening the receipt shows the local sources and lets the user:

-  disable one rule; 
-  make it permanent; 
-  make it session-only; 
-  inspect why it exists; 
-  delete its evidence lineage. 

This is not merely a privacy dashboard. It is possible because personalization decisions are explicit runtime operations rather than opaque effects of retrieved text.

---

# 9. Red-team results and repairs

**Problem: the cloud cannot anticipate every private dimension.**
 Repair: use a fixed public vocabulary of private operations rather than advertising what a particular user has stored. Every client may support `price.fit`, `calendar.fit`, `content.allowed`, `style.choice`, etc.; an unavailable rule simply returns neutral.

This also avoids leaking “this user has a medical constraint” merely by announcing that such memory exists.

**Problem: candidate explosion.**
 Do not make the model enumerate every personalization combination. P-IR supports filter/rank/select operations over structured candidates, so 50 products do not require 2ⁿ response variants.

**Problem: malicious P-IR probes the user's memory.**
 P-IR is deliberately not a general programming language. The runtime exposes bounded operators against candidate attributes. No `read_memory()`, arbitrary SQL, free-text retrieval, filesystem access, or returned predicate values.

This is where it differs materially from giving an agent a personal-data tool.

**Problem: exact personal recall.**
 “Where did I put my passport number?” is fundamentally different from personalization. MemoryScript should not pretend otherwise. Exact private fact retrieval should be answered by a trusted local execution path or an explicit one-time disclosure mechanism.

**Problem: server can infer preferences from future behavior.**
 Yes. This architecture controls the **memory disclosure channel**, not all possible behavioral inference. If personalized output is automatically retransmitted to the provider, part of the benefit disappears. The client must maintain a hard non-return boundary unless the user explicitly sends the resulting text.

**Problem: local model requirement.**
 The core runtime requires no LLM. Filtering, ranking, calendar intersection, rule evaluation, and variant selection can be deterministic. A small local model is optional for stylistic stitching.

That materially reduces the hardware dependency relative to approaches where the private client must itself generate substantial portions of the answer.

---

# 10. Evolution lineage

The initial candidate was **cloud draft → local private modification**. That was weakened by P³, which already demonstrates essentially that family. 

The first mutation replaced local generative modification with **private constraint verification**. This reduced local compute but created a leakage channel because repeated repair feedback reveals preferences.

The second mutation removed feedback entirely: the server now sends a **client-executable personalization program**, and the private resolution never returns upstream.

That is the surviving causal element.

### Innovation delta

After removing local storage, encryption, AI branding, graphs, embeddings, and permissions, the irreducible difference is:

> **A remote generative model compiles an unresolved answer into bounded personalization operations; a user-controlled runtime executes those operations against private memory and resolves the answer locally without transmitting either memory values or resolved branches back to the model.**

That is the piece worth protecting and testing.

---

# 11. Minimal architecture

```
```

```
┌──────────────── User-controlled device ────────────────┐
│                                                       │
│  Raw sources                                          │
│  calendar / mail / notes / history / explicit prefs   │
│            │                                          │
│            ▼                                          │
│  Event + provenance ledger                            │
│            │                                          │
│            ▼                                          │
│  Private Memory Runtime                               │
│  ├─ predicate evaluator                               │
│  ├─ filter/ranking engine                             │
│  ├─ rule conflict + temporal validity                 │
│  ├─ source revocation                                 │
│  └─ receipt generator                                 │
│            ▲                  │                       │
│            │ P-IR             ▼                       │
│       ─────┼──────────── Local renderer ──► USER       │
└────────────┼───────────────────────────────────────────┘
             │
             │ public query + no-memory task context
             ▼
       Cloud frontier model
             │
             └── candidates + Personalization IR
```

The raw store could be SQLite, files, a Solid Pod, OS data APIs, or something else. **The invention does not depend on its storage technology.**

That is intentional.

---

# 12. Falsification gate

The central claim dies if a representative daily-task corpus shows that the cloud model routinely needs explicit personal facts—not merely private rankings or predicates—to achieve useful personalization.

A strong implementation target would be:

- **≥90%** of the preference-satisfaction quality of a deliberately leaky full-profile baseline; 
-  no raw personal source strings transmitted through the memory channel; 
-  attribute-inference uplift from the protocol kept close to a no-memory cloud baseline; 
-  local deterministic execution fast enough to be effectively invisible; 
-  complete deletion of derived effects when a source memory is revoked. 

The first implementation should cover only three task families—recommendations, scheduling, and communication style—because each isolates a different private operator: ranking, constraint checking, and variant selection.

---

# 13. Scores and uncertainty

| DimensionMemoryScript |          |
| --------------------- | -------- |
| Mechanism novelty     | **8/10** |
| Problem value         | **9/10** |
| Advantage magnitude   | **8/10** |
| Technical feasibility | **8/10** |
| Adoption feasibility  | **7/10** |
| Testability           | **9/10** |
| Defensibility         | **7/10** |
| Evidence confidence   | **5/10** |
| Fatal-risk severity   | **6/10** |

The two least certain scores are **mechanism novelty** and **advantage magnitude**.

Novelty confidence is limited because older client-side personalization patents exist, including mechanisms that keep underlying user data private while locally producing personalized representations, as well as much older client-side content-personalization systems.  I did not find a close match in the searched literature or patents for an LLM producing a bounded, unresolved personalization program whose branches are privately executed and never returned upstream, but that is not proof that no such disclosure exists.

Advantage magnitude depends on how much real conversational personalization can be factorized into filters, rankings, selections, and local patches. Puda's data-minimization results and P³'s client-side personalization results provide evidence that substantial personalization can survive without full-profile cloud access, but neither proves this particular runtime mechanism. 

## Honest verdict

**Potentially novel mechanism, with meaningful adjacent prior art.**

The promising invention is **not** “private AI memory,” “local RAG,” or “a user-owned profile.” Those are already crowded.

The defensible direction is **memory as private execution**: turn personalization from *disclosing what the AI should know about me* into *executing what the AI wants to know about me without revealing the answer to it*.