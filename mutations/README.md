# Mutations

Store only frozen, experiment-linked NOVUM mutations here.

Every mutation must include:

- parent identity and SHA-256;
- exact diff or reconstructable patch;
- hypothesis/experiment ID;
- artifact SHA-256 after freeze;
- measured complexity delta;
- final retain/reject decision.

Do not add a mutation merely because an idea sounds promising.

## Current state

`EXP-001-portfolio-compression` is frozen for visible execution. Its candidate/runtime, generation, and blind-judging artifacts were frozen at commit `a5fbd315401340486895384607b7ed92a33a05be`. No behavioral result exists yet, and the exact hidden holdout has not been generated, selected, or exposed.
