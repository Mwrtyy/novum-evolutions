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