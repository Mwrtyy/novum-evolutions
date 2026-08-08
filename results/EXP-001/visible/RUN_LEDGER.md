# EXP-001 Visible Run Ledger

Authoritative progress record for visible execution. Raw outputs are preserved under `raw/` and must not be judged before blinding.

## Progress

| Case | Trial | Baseline | Candidate | Pair status |
|---|---:|---|---|---|
| vr-01-private-memory | 1 | RECORDED | RECORDED | COMPLETE |
| vr-01-private-memory | 2 | RECORDED | RECORDED | COMPLETE |
| vr-01-private-memory | 3 | PENDING | PENDING | PENDING |
| vr-02-waterless-cooling | 1 | RECORDED | RECORDED | COMPLETE |
| vr-02-waterless-cooling | 2 | RECORDED | RECORDED | COMPLETE |
| vr-02-waterless-cooling | 3 | RECORDED | RECORDED | COMPLETE |
| vr-03-false-novelty | 1 | PENDING | PENDING | PENDING |
| vr-03-false-novelty | 2 | PENDING | PENDING | PENDING |
| vr-03-false-novelty | 3 | PENDING | PENDING | PENDING |
| vr-04-battery-detection | 1 | PENDING | PENDING | PENDING |
| vr-04-battery-detection | 2 | PENDING | PENDING | PENDING |
| vr-04-battery-detection | 3 | PENDING | PENDING | PENDING |
| vr-05-simplify-not-invent | 1 | PENDING | PENDING | PENDING |
| vr-05-simplify-not-invent | 2 | PENDING | PENDING | PENDING |
| vr-05-simplify-not-invent | 3 | PENDING | PENDING | PENDING |
| vr-06-impossible-premise | 1 | PENDING | PENDING | PENDING |
| vr-06-impossible-premise | 2 | PENDING | PENDING | PENDING |
| vr-06-impossible-premise | 3 | PENDING | PENDING | PENDING |
| vr-07-ai-wrapper-trap | 1 | PENDING | PENDING | PENDING |
| vr-07-ai-wrapper-trap | 2 | PENDING | PENDING | PENDING |
| vr-07-ai-wrapper-trap | 3 | PENDING | PENDING | PENDING |
| vr-08-offline-clinic | 1 | PENDING | PENDING | PENDING |
| vr-08-offline-clinic | 2 | PENDING | PENDING | PENDING |
| vr-08-offline-clinic | 3 | PENDING | PENDING | PENDING |

## Recorded raw-output identities

- `vr-01 / trial 1 / baseline`
  - path: `results/EXP-001/visible/raw/vr-01/trial-1-baseline.md`
  - local capture SHA-256: `4ed35b9c04d4b1e8d7dbe13d4568ca0de0cacfdff0ce9bb684a463ce3467c34e`
  - source supplied by user as a copied ChatGPT Web answer
- `vr-01 / trial 1 / candidate`
  - path: `results/EXP-001/visible/raw/vr-01/trial-1-candidate.md`
  - local capture SHA-256: `9989c4e19dbe05052678f7f0599e340547ad4241799efc7d22212dc645f5ff32`
  - source supplied by user as a copied ChatGPT Web answer
- `vr-01 / trial 2 / candidate`
  - path: `results/EXP-001/visible/raw/vr-01/trial-2-candidate.md`
  - local capture SHA-256: `7b21bef6a4651ff9f08aea777fba6f7ad909c08426060638e5b67ec2df0640e2`
  - source supplied by user as a copied ChatGPT Web answer
- `vr-01 / trial 2 / baseline`
  - path: `results/EXP-001/visible/raw/vr-01/trial-2-baseline.md`
  - local capture SHA-256: `461512f9fdcf895f2c3bc5bc81795e6566e82e86803f29cde03243d3a2703f9a`
  - source supplied by user as a copied ChatGPT Web answer

### vr-02 batch

- `vr-02 / trial 1 / baseline`
  - path: `results/EXP-001/visible/raw/vr-02/trial-1-baseline.md`
  - source upload: `vr02-t1-baseline.md`
- `vr-02 / trial 1 / candidate`
  - path: `results/EXP-001/visible/raw/vr-02/trial-1-candidate.md`
  - source upload: `vr02-t1-candidate.md`
- `vr-02 / trial 2 / baseline`
  - path: `results/EXP-001/visible/raw/vr-02/trial-2-baseline.md`
  - source upload: `vr02-t2-baseline.md`
- `vr-02 / trial 2 / candidate`
  - path: `results/EXP-001/visible/raw/vr-02/trial-2-candidate.md`
  - source upload: `vr02-t2-candidate.md`
- `vr-02 / trial 3 / baseline`
  - path: `results/EXP-001/visible/raw/vr-02/trial-3-baseline.md`
  - source upload: `vr02-t3-baseline.md`
- `vr-02 / trial 3 / candidate`
  - path: `results/EXP-001/visible/raw/vr-02/trial-3-candidate.md`
  - source upload: `vr02-t3-candidate.md`

Model-run timestamps/tool-call metadata were not separately supplied for these runs and therefore are not invented here.

## Execution note for vr-02

The six vr-02 outputs were supplied as one parallel batch: three baseline and three candidate runs. The intended isolation was separate ChatGPT runs, but exact launch timestamps and temporal odd/even interleaving order were not supplied. This is recorded as an execution-order deviation rather than silently treating the batch as sequential. No result-based adaptation occurred in this ledger update.

## Current next run

The earliest incomplete frozen-protocol slot is:

`vr-01-private-memory / trial 3 / baseline`

Then run `vr-01-private-memory / trial 3 / candidate`.

After vr-01 is complete, continue with the three baseline/candidate pairs for `vr-03-false-novelty`.

## Scientific status

No behavioral judgment has been made. Recorded outputs remain raw evidence and are unscored until the visible generation set is complete and the frozen judging process begins.
