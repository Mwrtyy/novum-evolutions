# Canonical research vocabulary

These meanings are load-bearing. Keep them stable unless a documented decision changes them.

- **Invention** — a proposed intervention with an irreducible mechanism delta from the strongest practical baseline and a plausible path to a valued outcome.
- **Mechanism** — the causal process by which the intervention changes an observable relative to baseline. Implementation detail alone is not a mechanism.
- **Baseline** — the strongest practical existing approach for the task under the stated constraints, not a straw man.
- **Substitute** — a simpler or cheaper intervention that can plausibly achieve the same outcome. If it dominates, invention is unnecessary.
- **Candidate** — a frozen experimental mutation of NOVUM or a candidate invention produced by a run. State which meaning is intended when ambiguity matters.
- **Innovation delta** — the smallest material mechanism difference between candidate and strongest baseline.
- **Prior-art collision** — evidence that materially similar mechanism(s) have already been disclosed, deployed, standardized, or made obvious by nearby systems.
- **Novelty** — degree of material mechanism differentiation after reasonable collision search. Search failure is not proof of novelty.
- **Mechanistic depth** — specificity and causal adequacy of the path from intervention to observable advantage, including confounders and boundary conditions.
- **Causal claim** — a claim that changing X changes Y through a stated mechanism. A useful causal claim implies an intervention, ablation, perturbation, comparison, or counterfactual.
- **Assumption** — a proposition that must hold for the mechanism or claimed advantage to survive.
- **Evidence** — an observation or source that constrains a claim. Model-authored assertions are not external evidence.
- **Falsification** — an observation or result that would count against the central mechanism or advantage claim.
- **Behavioral failure** — a concrete, reproducible undesirable output behavior, not a stylistic complaint.
- **Reproduction** — a task/configuration that causes the failure often enough to study.
- **Mutation** — the smallest deliberate change to NOVUM intended to address one stated hypothesis.
- **Experiment** — a pre-registered comparison that can support, reject, or leave a mutation inconclusive.
- **Visible regression** — a known task available during development to prevent reintroducing known failures.
- **Holdout** — an evaluation task unavailable to candidate-development reasoning until after mutation freeze.
- **Adversarial benchmark** — tasks designed to attack a failure family without simply repeating development examples.
- **Evaluator** — the agent, model, or human assigning behavioral judgments to blinded outputs.
- **Independence** — evaluator/generator separation sufficient to reduce shared-context or shared-model bias; state the actual level rather than using the label loosely.
- **Promotion** — replacing the accepted NOVUM baseline after precommitted behavioral evidence supports the change.
- **Rollback** — restoring the exact prior accepted baseline when promotion evidence fails or later regressions emerge.
