# Visible generation protocol — frozen execution conditions

This protocol prepares generation only. It contains no result and no hidden holdout.

## Task set

Use exactly `benchmarks/visible-regression/cases.jsonl` at its frozen repository hash. Execute all eight cases in ascending case ID order. Do not add, rewrite, or omit tasks.

## Trials

Run **3 trials per case per arm** (24 outputs per arm). Every `case × trial × arm` run must start in a fresh model context. Fresh experimental runs do not mean independent candidate branches inside NOVUM; the runtime skill itself remains unchanged except for the EXP-001 overlay.

To reduce time-order bias, interleave paired runs:

- odd-numbered trials: arm 1, then arm 2;
- even-numbered trials: arm 2, then arm 1.

Do not expose the other arm's output to a generation context.

## Model requirement

Use **GPT-5.6 Sol** for both arms. Use the same visible reasoning/configuration setting for all paired runs. If the exact model/configuration is unavailable for one member of a pair, do not compare that unmatched pair; rerun both under the same available configuration and record the change.

## Context and prompt contract

For each run:

1. Start a fresh context.
2. Load only the designated NOVUM skill instructions plus the unchanged NOVUM 2.0 package references/assets/scripts as needed.
3. Supply exactly one visible-regression prompt as the user task.
4. Do not mention the experiment hypothesis, expected winner, other arm, or prior outputs.
5. Do not add follow-up steering. If the model asks the one clarification allowed by NOVUM, answer only when the task itself supplies the fact; otherwise instruct it to state a reasonable assumption and proceed, matching both arms.

## Tool and evidence equivalence

- Provide the same web/search/tool availability to both arms.
- Do not manually inject extra evidence, search terms, sources, or hints into either arm.
- Searches initiated by NOVUM are allowed under the same runtime capabilities.
- If material tool access fails for one arm but not its paired run, mark the pair invalid and rerun both under matched availability.
- Record actual tool/search usage; do not “top up” the candidate or baseline after generation.

## Reasoning/output budget equivalence

Use the same model configuration and any client-exposed reasoning/output limits for both arms. Do not grant continuation turns, extra search rounds, or a larger response ceiling to one arm. Where hidden reasoning budget is not directly controllable, record it as `uncontrolled_same_configuration`; the intended experimental manipulation is the skill's internal breadth→depth allocation, not a larger external budget.

## Output capture

Store raw outputs separately by arm as JSONL. Preserve text exactly as produced. Each row must include at least:

```json
{
  "case_id": "vr-01-private-memory",
  "trial": 1,
  "model_identity": "GPT-5.6 Sol",
  "model_configuration": "record visible setting/build if exposed",
  "run_started_utc": "RFC3339 timestamp",
  "run_finished_utc": "RFC3339 timestamp",
  "tool_access": "description",
  "tool_call_count": 0,
  "search_queries": [],
  "output_text": "verbatim model output"
}
```

The existing harness requires `case_id`, `trial`, and `output_text`; the additional fields preserve execution equivalence evidence.

## Stopping rule

After exactly 24 valid outputs exist for each arm, stop visible generation. Do not inspect results to change candidate bytes, evaluator instructions, task wording, or trial count.
