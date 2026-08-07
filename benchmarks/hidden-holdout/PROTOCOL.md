# Post-freeze holdout protocol

This directory intentionally contains **no final holdout prompts**.

A promotion holdout is valid only when candidate-development reasoning cannot inspect the exact tasks before candidate bytes are frozen.

## Sequence

1. Freeze candidate artifact bytes and record SHA-256.
2. Freeze the evaluation rubric/judge instructions separately.
3. Only after steps 1–2, select or generate holdout tasks from the problem grammar.
4. Record task-set owner/process, generation seed or selection procedure, timestamp, and hash.
5. Keep exact task text outside candidate-development context until generation begins.
6. Run baseline and candidate under equivalent model/tool/evidence budgets.
7. Blind identities before judging.
8. Preserve public blind bundle, private mapping, judgments, raw outputs, and aggregation separately.
9. Reveal identities only after judgments are locked.

## Invalid holdouts

A task is not a holdout if:

- it was stored in the repository before candidate freeze;
- it was used during mutation design;
- it is a lightly reworded visible regression example;
- the candidate author selected it after seeing candidate outputs;
- exact prompts leaked through logs, issues, commits, or evaluator context.

If secrecy cannot be established, call the set `visible` or `adversarial`, not `hidden`.
