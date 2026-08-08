# EXP-001 Blind Judge — vr-01-t2-domain_or_generalist

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
  "pair_id": "vr-01-t2",
  "evaluator_id": "vr-01-t2-domain_or_generalist",
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

# Blind pair vr-01-t2

## Task

Design a daily-use AI memory mechanism that improves personalization while keeping raw personal data under user control. Avoid a generic vector database plus privacy claims.

## Output A

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

## Output B

## Invention candidate: **Personal Memory ABI**

Build AI memory as a **user-owned execution boundary**, not as a database the model can search.

The remote AI is never given a `search_memory()` primitive. Instead, it can invoke a small set of typed **memory functions**—such as rank, verify, constrain, resolve, or personalize—which execute against raw personal data inside a user-controlled local vault. Wherever possible, the result of that computation is applied locally to the AI’s draft, so even the derived personal fact never needs to leave the device.

This follows NOVUM’s requirement that the result be a precise mechanism rather than a feature bundle or generic advice. 

### 1. Problem reframing

Achieve **continuously useful personalization across everyday AI interactions** while keeping **long-lived raw personal history under the user’s custody**, outperforming provider-managed memories and local RAG without requiring every useful AI model to run locally.

The central contradiction is:

> Good personalization seemingly requires giving the model more persistent personal context, while meaningful user control requires giving outside models less persistent personal context.

Existing approaches mostly choose a point on that trade-off. Current ChatGPT memory, for example, maintains memories separately from chat history and automatically updates what it considers important; Gemini can personalize from past Gemini chats when its memory/activity features are enabled. 

Agent-memory systems move the storage architecture but retain the same basic information flow. Mem0 extracts memories and commonly uses embeddings plus optional graph relationships; Zep/Graphiti builds evolving temporal graphs from episodic data. 

The invention changes the information flow itself.

---

## 2. Frontier and opportunity gap

**Saturated:** store conversations or extracted facts, retrieve relevant pieces, and place them back into model context. Vector memory, temporal graphs, saved-memory summaries, and conversation-history personalization occupy this territory. 

**Also saturated:** put the data locally, encrypt it, or let users grant applications access. Local-first architectures establish a strong ownership principle, and Solid separates applications from user-controlled Pods. But once an application receives plaintext, storage ownership does not prevent it from copying or transmitting that information elsewhere—an issue explicitly recognized in Solid discussions. 

**Emerging:** edge/cloud collaboration, where private context stays on a device while a stronger cloud model contributes reasoning. SpecSteer is a recent example, using local personalized drafting and cloud verification. 

**Neglected opening:** let powerful outside models **compute with personal memory without being allowed to browse personal memory**.

That distinction matters because research on data minimization finds that LLMs themselves are poor judges of exactly how much private information they need and tend to overshare rather than discover the minimum disclosure automatically. 

---

## 3. The four mechanism families

| CandidateMemory is…What outside AI receivesMain weakness |                                         |                                                                         |                                                                            |
| -------------------------------------------------------- | --------------------------------------- | ----------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Purpose capsules                                         | A locally generated temporary summary   | Minimal task-specific facts                                             | Still discloses a profile, just a smaller one                              |
| Preference oracle                                        | A private utility/ranking function      | Rankings or selected option IDs                                         | Excellent for preferences, weak for episodic recall                        |
| Capability leases                                        | Individually permissioned memory claims | Time/scoped facts                                                       | Permissions do not prevent copying after disclosure                        |
| **Personal Memory ABI**                                  | **A set of bounded computations**       | **Function outputs—or nothing when personalization is applied locally** | Requires the AI interaction to be split into reasoning and personalization |

The last mechanism survives because the others ultimately retain **data disclosure** as the primary personalization mechanism.

---

# 4. Personal Memory ABI architecture

Think of this as a tiny operating-system kernel for personal context.

### A. User Memory Vault

The authoritative raw memory lives on the user's device or user-selected self-hosted storage:

-  conversations the user elects to retain; 
-  contacts and relationships; 
-  calendar history; 
-  notes; 
-  preferences and corrections; 
-  purchasing or browsing records; 
-  application state; 
-  other explicitly connected sources. 

Encryption keys belong to the user. Multi-device synchronization can use end-to-end encrypted replication; a cloud AI provider is not the authoritative copy.

The vault's internal implementation can use SQL, files, graphs, embeddings, or none of these. **That is deliberately not the invention.** No external model gets access to the storage interface.

### B. Local evidence layer

A lightweight local process converts raw events into user-owned evidence objects:

```
```

```
claim:
    "prefers quiet restaurants"
evidence:
    3 accepted recommendations
    1 explicit user statement
validity:
    current
confidence:
    medium
sensitivity:
    ordinary preference
```

These are not automatically exported memories.

Time is first-class. A newer correction can supersede an earlier inference without destroying historical evidence.

For example:

```
```

```
2025: "Runs most mornings"
2026-07: "Currently avoiding running"
```

A memory function operating today sees the active state rather than blindly retrieving the highest-similarity historical statement.

### C. The Memory ABI

AI providers see only a constrained tool interface.

There is intentionally **no**:

```
```

```
search_memory("tell me everything relevant about this user")
```

Instead:

```
```

```
preference.rank(candidates, domain)
constraint.check(candidate, domain)
history.verify(proposition)
history.abstract(topic, granularity)
identity.resolve(slot, disclosure_level)
style.transform(draft, channel)
```

Every function has a bounded output schema.

For example:

```
```

```
preference.rank(
  candidates=[A,B,C,D],
  domain="restaurant"
)
→ [C,A,D,B]
```

The provider learns the ranking, not the meals the user ordered during the previous five years.

Or:

```
```

```
constraint.check(
  candidate="recipe_4",
  domain="food"
)
→ false
```

The model need not learn *why* it failed.

That is personalization through **computation rather than retrieval**.

---

## 5. The crucial second path: local-only personalization

The strongest part of the architecture is that memory functions do not always return anything to the cloud.

The remote model can produce:

```
```

```
DRAFT:
"I'd recommend OPTION_A because REASON_A..."
```

plus a personalization plan:

```
```

```
1. rank these three options
2. reject anything violating hard constraints
3. rewrite to user's preferred communication style
```

The local Memory ABI executes those instructions and renders the final response.

So:

```
```

```
user → cloud reasoning → generic draft
                         ↓
                 personalization plan
                         ↓
               USER MEMORY KERNEL
                         ↓
              personalized final answer
                         ↓
                       user
```

The cloud may never see the preference that caused option B to beat option A.

This is the architectural inversion: **instead of sending memories into the model, bring part of the model's unfinished answer to the memory.**

Recent work such as GRAG has independently explored separating generic response generation from personalization, which makes this decomposition technically credible, although its mechanism and purpose differ: GRAG focuses on personalization architectures for smaller models rather than a user-controlled memory access boundary. 

---

## 6. Disclosure modes

Each memory call is automatically executed in one of three modes.

**Zero disclosure.** The computation runs locally. Only the final rendered response changes.

Example: rank five gift ideas using the recipient's locally stored interests.

**Coarse disclosure.** The cloud receives the minimum categorical information needed.

Example:

```
```

```
dietary_constraint = "vegetarian"
```

rather than purchase records, restaurant history, and past conversations from which that conclusion was inferred.

**Exact disclosure.** Used only when the task intrinsically requires the actual value.

Example: filling a shipping address.

Sensitive exact disclosures can require explicit user approval; ordinary rankings and local transformations should not, avoiding daily consent fatigue.

---

## 7. Preventing the obvious attack

A seemingly constrained API is still vulnerable if a model can make thousands of clever queries:

```
```

```
Does user like X?
Does user like Y?
Does user know person Z?
...
```

It could reconstruct the profile one bit at a time.

So the ABI includes a **cumulative disclosure accountant**.

It records information released to each provider across calls, not merely permissions on individual calls.

If a provider repeatedly probes one topic, the kernel can:

-  collapse queries into an already released coarse category; 
-  switch to local-only ranking; 
-  reduce granularity; 
-  deny further extraction. 

Thus privacy enforcement happens on the **information-flow boundary**, rather than being a prompt saying "please respect privacy."

This is also where contextual-integrity ideas fit naturally: the appropriateness of releasing information depends on the purpose, recipient, and context rather than simply whether the underlying datum exists. 

---

## 8. What daily use feels like

Suppose the user asks:

**“What should I cook tonight?”**

The cloud model can generate several broadly good candidates. Locally, the Memory ABI knows pantry state, repeatedly rejected foods, household preferences, recent meals, and dietary constraints.

It can rank and filter the candidates without sending those records upstream. Only if no suitable option remains might it disclose one coarse constraint and request another set.

For:

**“What did we decide about the kitchen renovation?”**

local memory performs the retrieval and temporal reconciliation. It might release three derived conclusions:

```
```

```
Cabinet finish: oak
Budget ceiling: €18k
Island: rejected due to clearance
```

rather than sending six months of conversations and notes.

For:

**“Write this the way I normally would.”**

the cloud produces the substantive draft and the local style function rewrites it. Personal writing history never needs to enter the provider's context.

This makes memory useful not only for factual recall but also for **selection, constraints, relationships, continuity, and behavioral personalization**.

---

# 9. User-control mechanism

Every answer gets an optional **memory receipt** generated locally:

```
```

```
PERSONALIZATION USED

✓ Food constraint
  Applied locally
  Data disclosed: none

✓ Recent meal pattern
  Used to rank candidates
  Data disclosed: none

✓ Cooking time preference
  Sent as: "< 30 minutes"

Sources remain on this device.
```

A user can tap a line and:

-  inspect its evidence; 
-  correct it; 
-  disable that memory function; 
-  forbid a source; 
-  delete the underlying raw material; 
-  prevent a provider from receiving outputs from that category. 

Deleting source data invalidates dependent local evidence automatically.

One unavoidable limit should be explicit: **information previously disclosed in plaintext cannot technically be clawed back from a recipient.** Storage ownership and deletion interfaces cannot repeal that fact. The architecture therefore minimizes disclosure before it happens.

---

## 10. Anti-fake-novelty check

Several nearby ideas substantially overlap parts of this design.

A Microsoft patent describes computing a personalized profile locally and controlling exposure of that representation to applications.  Another assistant patent describes exposing user information to third-party skills according to permissions and privacy settings.  Databox research has also long explored keeping personal data locally while executing applications and computations at the edge. 

So **“local personal data + controlled access” is not the innovation**.

The irreducible delta here is:

> **Replace record/profile access with a purpose-bounded, typed computational ABI; allow many personalization operations to return no personal information at all by applying them locally to a cloud-generated draft; and account for cumulative information disclosure across repeated calls.**

Remove any of those three pieces and the design starts collapsing toward existing personal-data stores, local profiles, privacy filters, or ordinary RAG.

---

# 11. Rejected ledger and refinement

**Temporary personalized summaries** were rejected as the core mechanism because they still make "what personal information should we disclose?" the central problem.

**Pure on-device personalization** was rejected because it unnecessarily gives up cloud-scale reasoning capability. On-device personalization research shows the direction is viable, but full local generation is a different trade-off. 

**Permissioned personal-data APIs** were rejected because permission to read does not constrain subsequent copying.

**PII masking/firewalls** were rejected as the memory mechanism because masking protects identifiers but does not solve persistent personalization; current tools largely redact or tokenize content before it reaches an AI service. 

The surviving architecture therefore combines the strongest element of the preference-oracle idea—**answers instead of records**—with a local response-composition path and cumulative disclosure control.

---

# 12. Honest verdict

**Classification: Differentiated architecture.**

There is strong evidence for all of its enabling components: user-controlled/local-first stores, local processing, data-minimizing interfaces, edge/cloud model collaboration, post-generation personalization, temporal memory, and contextual privacy controls already exist separately. 

The less-established claim is the architecture-level combination: **a vendor-independent Personal Memory ABI whose default primitive is execution over private memory rather than retrieval from it, including local-only answer personalization and cross-call disclosure accounting**. The searches surfaced close pieces but not enough evidence to claim universal novelty.

Its central claim is falsifiable: if useful everyday personalization generally requires exposing rich personal records to the reasoning model rather than rankings, constraints, abstractions, verification results, or local response transformations, then the architecture loses its principal advantage and becomes a complicated version of ordinary memory retrieval.

The strongest product form would be an **OS-level or user-owned Personal Memory Service**, shared across AI providers. Switching from one model vendor to another would then change the intelligence engine—not erase the user's memory, transfer custody of their personal history, or force that history into another vendor's vector database.

