# EXP-001 static hostile isolation review

Status: `PASS_FOR_FREEZE` on intervention isolation only. This is **not** behavioral evidence.

Review target: diff from accepted NOVUM 2.0.0 `SKILL.md` to the EXP-001 overlay.

## Attack question

Can the diff plausibly be said to test anything besides portfolio breadth/depth allocation?

## Checks

| Potential accidental intervention | Result | Evidence |
|---|---|---|
| H2 independent generation contexts/subagents | absent | No context, agent, branch, or subagent instruction is added. Baseline's existing “independent mechanisms” wording is unchanged. |
| H3 late scoring | absent | Scoring section and timing are byte-identical to baseline. |
| H4 new simpler-substitute methodology | absent | Existing simpler-substitute consideration is only named as a destination for released budget; no new gate, rule, or threshold is added. |
| H5 new causal-ablation requirement | absent | Causal and falsification requirements are byte-identical to baseline. |
| H6 new prior-art/search methodology | absent | No query representation, source requirement, search sequence, or search-specific budget is changed. Existing prior-art work is only one of several existing depth destinations. |
| altered novelty scoring | absent | Evaluation rubric/scoring dimensions and weights are unchanged. |
| altered promotion criteria | absent | Mutation touches only runtime `SKILL.md`; Evolution Lab promotion protocol is unchanged. |
| altered research-source requirements | absent | Research protocol/reference files are unchanged. |
| additional validators/schemas/artifacts required by NOVUM | absent | No baseline package validator, schema, ledger, or output requirement is changed. |
| evaluator knowledge or benchmark-specific hints | absent | Candidate skill contains no EXP-001 hypothesis, expected winner, case IDs, prompts, or judging rubric. |

## Diff-specific hostile reading

The phrase “mechanically distinct” does not introduce H2: NOVUM 2.0 already requires a mechanism-diverse portfolio and mechanically distinct candidates. The depth destinations named in the new sentence are pre-existing NOVUM 2.0 mechanisms; none receives a new procedure. The sentence explicitly blocks adding mechanisms and blocks increasing the total run budget.

## Conclusion

The defensible causal description is one conceptual intervention: **compress Standard initial breadth to four and reallocate the saved breadth budget across existing depth mechanisms**. If future execution requires changing any other runtime mechanism, EXP-001 must stop and be versioned rather than silently broadened.
