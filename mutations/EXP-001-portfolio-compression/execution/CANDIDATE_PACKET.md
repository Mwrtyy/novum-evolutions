# Visible execution packet

Use this packet in a fresh generation context. Do not provide experiment history or expected outcomes.

## Skill source

- Runtime instructions: `mutations/EXP-001-portfolio-compression/candidate-SKILL.md`
- Required SHA-256: `ad61ff084f482d9e06b3398970be565bdd5d7d29c132b1a3dfd0c45bd88a4688`
- Parent package anchor: accepted NOVUM Innovation 2.0.0 archive SHA-256 `e38cd4e62439c5759bf99bf2fc72e165abf2876f75396c170f445d6a3c529dda`
- All references/assets/scripts: use the same immutable NOVUM 2.0.0 package at source commit `e591937931d2a04f2b308e23f2edca488bea9fcd`; do not modify them.

## Common execution contract

Follow `mutations/EXP-001-portfolio-compression/execution/GENERATION_PROTOCOL.md` exactly.

- Model: GPT-5.6 Sol
- Visible task set: `benchmarks/visible-regression/cases.jsonl`
- Trials: 3 per case
- Fresh context: required per case/trial
- Tool/evidence access: identical to the paired arm
- External reasoning/output limits: identical to the paired arm
- Output capture: verbatim JSONL under the common schema

The generation context receives only the verified skill instructions, unchanged NOVUM 2.0 support files, and one task prompt.
