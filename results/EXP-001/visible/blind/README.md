# EXP-001 blind judging

Generated after visible generation completion.

- 24 blinded A/B pairs
- 3 evaluator roles per pair
- 72 role-specific judge prompts
- A/B orientation is frozen by SHA-256 of `EXP-001-BLIND-V1|<pair_id>` before judging.
- Judges must not receive `private/AB_MAPPING.json`.
- `vr-01`–`vr-04` use frozen exact task wording.
- `vr-05`–`vr-08` use the adopted near-equivalent task wording actually shown to both generation arms.
- Judge independence for ChatGPT Web fresh contexts must be recorded as `separate_context_same_model`, not external replication.

Do not reveal the private A/B mapping until all 72 judgments are locked.
