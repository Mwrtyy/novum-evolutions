# EXP-001 Visible Judging Independence Audit and Corrected Rerun

Status: `VISIBLE_RERUN_LOCKED_REVEALED_HIDDEN_HOLDOUT_IN_PROGRESS`

## Finding

The original visible judging used three persistent evaluator contexts, one for each role, with 24 sequential packet judgments per context. It did **not** use 72 independent model invocations.

Evidence:

- `results/EXP-001/visible/JUDGING_EXECUTION.md` assigns 24 packets to each of `hostile_regression-01`, `simplicity-01`, and `domain_or_generalist-01`.
- Earlier judgments therefore shared conversational calibration and fixed within-role order.
- A/B identities were still hidden and the private mapping was not given to those evaluators.
- The frozen judging packet required a fresh evaluator context but did not explicitly require a different evaluator context per packet. The implementation was therefore protocol-compatible under a weak reading, but scientifically dependent and materially weaker than per-packet isolation.

Because the current environment supported cleaner execution, all 72 visible judgments were rerun.

## Corrected execution

- 24 public blinded pairs.
- 3 frozen roles per pair.
- 72 separately spawned fresh contexts; one packet and one role per context.
- No context reuse.
- No prior judgments, visible aggregate, experiment hypothesis, or private mapping supplied.
- Same model family; this is context isolation, not external replication.
- 72 unique evaluator IDs.
- Zero missing or invalid records.

The corrected judgment set was validated and locked before the mapping was fetched.

- Judgment-set SHA-256: `353bd6562048e9d911398a528e21b7def7386a7541a541f33d76eb6d9a36aca7`
- Lock-file SHA-256: `9edacda3d15103cad4155213c7452512ba185f3ca0324e3e8411340e62cd3af7`
- Mapping used during validation or lock: **no**

## Corrected visible result

| Measure | Candidate | Baseline | Tie |
|---|---:|---:|---:|
| Pair majorities | 11 | 11 | 2 |
| Judge preferences | 34 | 34 | 4 |

Tie-adjusted candidate preference rate: **50.0%**. The earlier persistent-context result (15–6–3 pairs and 43–22–7 votes) does not replicate under per-packet context isolation.

| Dimension | Mean delta C−B | Paired dz | Pair-cluster bootstrap 95% interval |
|---|---:|---:|---:|
| mechanism_novelty | +0.083 | +0.114 | [−0.182, +0.364] |
| mechanistic_depth | +0.000 | +0.000 | [−0.160, +0.161] |
| constraint_fit | −0.049 | −0.114 | [−0.214, +0.096] |
| usefulness | +0.014 | +0.027 | [−0.164, +0.185] |
| evidence_calibration | +0.122 | +0.244 | [−0.042, +0.300] |
| falsifiability | +0.365 | +0.306 | [−0.082, +0.817] |
| prior_art_awareness | +0.176 | +0.286 | [−0.029, +0.408] |
| simpler_substitute_discipline | +0.062 | +0.053 | [−0.308, +0.426] |
| clarity | −0.111 | −0.193 | [−0.315, +0.075] |

No dimension interval excludes zero.

## Heterogeneity

| Case | Candidate votes | Baseline votes | Ties | Pair majorities C/B/tie | Mean delta across dimensions |
|---|---:|---:|---:|---:|---:|
| vr-01 | 3 | 6 | 0 | 1/2/0 | −0.241 |
| vr-02 | 4 | 5 | 0 | 2/1/0 | +0.031 |
| vr-03 | 7 | 2 | 0 | 2/1/0 | +0.507 |
| vr-04 | 8 | 1 | 0 | 3/0/0 | +0.414 |
| vr-05 | 1 | 8 | 0 | 0/3/0 | −0.301 |
| vr-06 | 1 | 5 | 3 | 0/2/1 | −0.210 |
| vr-07 | 4 | 4 | 1 | 1/1/1 | +0.105 |
| vr-08 | 6 | 3 | 0 | 2/1/0 | +0.285 |

The exact frozen-prompt half (`vr-01`–`vr-04`) favored the candidate: 8/12 candidate pair wins and 22–14 judge votes. The post-hoc adopted near-equivalent half (`vr-05`–`vr-08`) favored baseline: 3/12 candidate pair wins, 7/12 baseline wins, 2 ties, and 12–20–4 judge votes. This split is descriptive and cannot establish that wording caused the reversal, but it makes Protocol Amendment 001 materially relevant.

By role, mean deltas remained small: hostile regression +0.050, simplicity +0.065, domain/generalist +0.106. Trial mean deltas were +0.071, +0.044, and +0.106. Fleiss' kappa was 0.294; 11 pairs were unanimous and 13 split.

## Interpretation boundary

The corrected visible evidence is neutral overall and heterogeneous by task family and prompt-status stratum. It provides no robust visible support for a universal exactly-four portfolio rule. It does preserve directional hints in falsifiability and prior-art awareness, alongside possible regressions in constraint fit and clarity.

The historical three-context analysis remains preserved as exploratory evidence. It is superseded for confirmatory visible interpretation by this per-packet rerun.

No final EXP-001 verdict is authorized until the frozen hidden holdout is generated, blind-judged, locked, revealed, and audited.

