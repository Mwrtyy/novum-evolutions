# EXP-001 final protocol audit

Status: `COMPLETE`

## Conclusion

The hidden holdout is usable as strict within-system confirmatory evidence. It is not external replication and it is not pristine byte-for-byte execution because prompt materialization added a trailing line feed. No detected issue invalidates the hidden A/B result. The original visible 15–6 result is superseded for confirmatory interpretation by the 72-context rerun.

## Audit table

| Check | Evidence | Classification | Effect |
|---|---|---|---|
| Candidate freeze | Candidate SHA `ad61ff…` matched all 21 candidate runs | harmless | Frozen mutation identity preserved |
| Baseline freeze | Canonical archive SHA `e38cd4…`; skill SHA `1d6dea…`; validator and self-tests passed | harmless | Accepted baseline identity preserved |
| Judge packet freeze | Exact packet SHA `babae4…` used for hidden judging | harmless | Scoring dimensions unchanged |
| Visible prompt deviation | vr-05 through vr-08 used declared post-hoc near-equivalent prompts | material threat | Visible must be split; never call all 48 exact |
| Original visible judging | Three persistent same-model contexts handled 24 packets each | invalidating for per-packet independence claims | Historical 15–6 retained but superseded |
| Corrected visible rerun | 72 assignments, 72 fresh contexts, lock before mapping | limitation: same family | Usable internal rerun; result 11–11–2 |
| Holdout timing | Candidate and judge bytes frozen before exact holdout tasks | harmless | Candidate could not adapt to exact tasks |
| Holdout structure timing | 7-domain × 3-trial design and semantic prompt selection finalized after visible analysis | material threat, mitigated | Selector was isolated from visible results; not pre-visible preregistration |
| Holdout overlap | Visible prompt text used only to reject overlap; selector received no visible outputs/results | harmless | No detected lightly reworded visible task |
| Holdout task freeze | Task SHA `819f17…`; freeze manifest SHA `6e3d48…` before first run | harmless | Immutable during generation |
| Prompt bytes | Materialized files added exactly one trailing LF | harmless deviation | No lexical content changed; exact-byte claim withdrawn |
| Model/config parity | Same declared model/configuration within every pair | limitation: self-reported | No detected asymmetric model change |
| Tool parity | Same tools and query/source caps; actual use varied naturally | limitation: self-reported | No evidence of arm-specific access |
| Installed-skill isolation | Explicit local-only instruction; no OS-level global-skill exclusion | limitation | Model-level non-exposure cannot be proven |
| Generation independence | 42 accepted runs, 42 unique fresh contexts | limitation: same family | Not external replication |
| Generation retries | Two invalid first-attempt pairs discarded; both mates rerun before blinding | limitation | Symmetric pair-level retry avoided output cherry-picking |
| Missing/duplicate generation | Validator found exact 42-run coverage | harmless | None missing/duplicated |
| A/B secrecy | Private salt outside evaluator-accessible files until lock | harmless | No mapping existed during judging |
| Hidden judge independence | 63 assignments, 63 unique contexts | limitation: same family | No cross-packet context reuse |
| Judgment schema normalization | 13 keys renamed before lock; no score/preference edits | harmless | Lock covers canonical records |
| Judgment completeness | 21 pairs × 3 roles × 9 dimensions | harmless | Complete coverage |
| Scoring drift | Frozen dimensions/roles retained; no new role weights | harmless | No detected rubric mutation |
| Lock/reveal order | Judgment SHA `80009c…`; lock SHA `ee8f1e…` before reveal | harmless | Irreversible boundary respected |
| Analysis drift | Same lock/aggregate code for visible rerun and hidden; 10,000 pair bootstraps | limitation: code written after visible | No post-hidden-reveal metric selection detected |
| Cherry-picking | All frozen domains, trials, arms, and roles included | harmless | No accepted pair dropped |

## Classification summary

- Invalidating for hidden holdout: none detected.
- Material threats: post-visible holdout structure/semantic selection; mitigated but not erased. The visible near-equivalent-prompt amendment remains material for exact visible reproducibility.
- Limitations: same model family, self-reported runtime/tool metadata, no OS-level exclusion of the global skill, two symmetric pair retries, post-visible analysis-code timing.
- Harmless deviations: one trailing LF per prompt file and schema-only key normalizations before lock.

## Claims permitted

Accurate: the corrected visible rerun was neutral; the strict hidden holdout favored baseline 14–7; every accepted generation and judgment used a fresh same-model context; A/B was revealed only after lock; EXP-001 does not support promotion.

Inaccurate: external replication; all visible prompts exact; hidden prompts preregistered before visible results; proof that four candidates are universally worse; physical inaccessibility of the global installed skill.
