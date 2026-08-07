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
