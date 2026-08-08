#!/usr/bin/env python3
from pathlib import Path
from collections import defaultdict, Counter
import json, statistics

ROOT = Path(__file__).resolve().parents[1]
BLIND = ROOT / "results/EXP-001/visible/blind"
JUDGMENTS = ROOT / "results/EXP-001/visible/judgments-copilot"
MAPPING = BLIND / "private/AB_MAPPING.json"
MANIFEST = BLIND / "JUDGE_MANIFEST.json"
OUT = ROOT / "results/EXP-001/visible/analysis"
DIMS = [
    "mechanism_novelty", "mechanistic_depth", "constraint_fit", "usefulness",
    "evidence_calibration", "falsifiability", "prior_art_awareness",
    "simpler_substitute_discipline", "clarity"
]

mapping = json.loads(MAPPING.read_text(encoding="utf-8"))
manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
records = []
missing = []

for item in manifest:
    p = JUDGMENTS / f"{item['judge_id']}.json"
    if not p.exists():
        missing.append(item['judge_id'])
        continue
    j = json.loads(p.read_text(encoding="utf-8"))
    m = mapping[item["pair_id"]]
    side_candidate = "A" if m["A"] == "candidate" else "B"
    side_baseline = "B" if side_candidate == "A" else "A"
    pref = j["preference"]
    if pref == "tie":
        translated_pref = "tie"
    elif pref == side_candidate:
        translated_pref = "candidate"
    else:
        translated_pref = "baseline"
    delta = {
        d: float(j["scores"][side_candidate][d]) - float(j["scores"][side_baseline][d])
        for d in DIMS
    }
    records.append({
        "pair_id": item["pair_id"],
        "case_id": m["case_id"],
        "trial": m["trial"],
        "role": item["role"],
        "prompt_status": m["prompt_status"],
        "preference": translated_pref,
        "delta": delta,
        "judge_model": j.get("judge_model"),
        "judge_provider": j.get("judge_provider"),
    })

if missing:
    raise SystemExit(f"Cannot aggregate: {len(missing)} judgments missing")
if len(records) != 72:
    raise SystemExit(f"Expected 72 judgments, got {len(records)}")

OUT.mkdir(parents=True, exist_ok=True)

def mean(xs):
    return sum(xs) / len(xs) if xs else 0.0

pref_counts = Counter(r["preference"] for r in records)
dim_means = {d: mean([r["delta"][d] for r in records]) for d in DIMS}

# Pair-majority preference from the three locked evaluator roles.
by_pair = defaultdict(list)
for r in records:
    by_pair[r["pair_id"]].append(r)
pair_results = []
for pair_id, rs in sorted(by_pair.items()):
    votes = Counter(r["preference"] for r in rs)
    c, b = votes["candidate"], votes["baseline"]
    winner = "candidate" if c > b else "baseline" if b > c else "tie"
    pair_delta = {d: mean([r["delta"][d] for r in rs]) for d in DIMS}
    pair_results.append({
        "pair_id": pair_id,
        "case_id": rs[0]["case_id"],
        "prompt_status": rs[0]["prompt_status"],
        "winner": winner,
        "votes": dict(votes),
        "mean_candidate_minus_baseline": pair_delta,
    })
pair_counts = Counter(x["winner"] for x in pair_results)

by_role = {}
for role in sorted(set(r["role"] for r in records)):
    rs = [r for r in records if r["role"] == role]
    by_role[role] = {
        "preferences": dict(Counter(r["preference"] for r in rs)),
        "mean_candidate_minus_baseline": {d: mean([r["delta"][d] for r in rs]) for d in DIMS},
    }

by_case = {}
for case_id in sorted(set(r["case_id"] for r in records)):
    rs = [r for r in records if r["case_id"] == case_id]
    ps = [p for p in pair_results if p["case_id"] == case_id]
    by_case[case_id] = {
        "prompt_status": rs[0]["prompt_status"],
        "judge_preferences": dict(Counter(r["preference"] for r in rs)),
        "pair_majority": dict(Counter(p["winner"] for p in ps)),
        "mean_candidate_minus_baseline": {d: mean([r["delta"][d] for r in rs]) for d in DIMS},
    }

summary = {
    "experiment": "EXP-001",
    "phase": "visible_blind_judging",
    "judgments": len(records),
    "pairs": len(pair_results),
    "judge_models": sorted(set(r["judge_model"] for r in records)),
    "judge_providers": sorted(set(r["judge_provider"] for r in records)),
    "judge_preference_counts": dict(pref_counts),
    "pair_majority_counts": dict(pair_counts),
    "mean_candidate_minus_baseline": dim_means,
    "by_role": by_role,
    "by_case": by_case,
    "pairs_detail": pair_results,
    "protocol_note": "vr-05 through vr-08 use the adopted near-equivalent prompt wording declared in Protocol Amendment 001.",
    "decision_note": "Visible results alone are not a promotion decision; strict hidden holdout remains required.",
}
(OUT / "VISIBLE_JUDGING_SUMMARY.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

lines = [
    "# EXP-001 Visible Blind-Judging Summary", "",
    f"- Locked judgments: **{len(records)}/72**",
    f"- Blinded pairs: **{len(pair_results)}/24**",
    f"- Judge provider/model: `{', '.join(summary['judge_providers'])}` / `{', '.join(summary['judge_models'])}`",
    "- A/B mapping was applied only after all 72 judgment files existed.",
    "- vr-05 through vr-08 retain the declared near-equivalent-prompt protocol deviation.", "",
    "## Pair-majority result", "",
    f"- Candidate wins: **{pair_counts['candidate']}**",
    f"- Baseline wins: **{pair_counts['baseline']}**",
    f"- Ties: **{pair_counts['tie']}**", "",
    "## Mean score delta (candidate - baseline)", "",
    "| Dimension | Delta |",
    "|---|---:|",
]
for d in DIMS:
    lines.append(f"| {d} | {dim_means[d]:+.3f} |")
lines += ["", "## Judge-level preferences", "", f"- Candidate: {pref_counts['candidate']}", f"- Baseline: {pref_counts['baseline']}", f"- Tie: {pref_counts['tie']}", "", "## Per case", "", "| Case | Prompt status | Candidate pair wins | Baseline pair wins | Ties |", "|---|---|---:|---:|---:|"]
for case_id, data in by_case.items():
    pc = data["pair_majority"]
    lines.append(f"| {case_id} | {data['prompt_status']} | {pc.get('candidate',0)} | {pc.get('baseline',0)} | {pc.get('tie',0)} |")
lines += ["", "## Interpretation boundary", "", "This is visible-set evidence, not a promotion decision. Run the strict post-freeze hidden holdout before retaining or promoting the mutation.", ""]
(OUT / "VISIBLE_JUDGING_SUMMARY.md").write_text("\n".join(lines), encoding="utf-8")
print(json.dumps({"pairs": len(pair_results), "pair_majority": dict(pair_counts), "dimension_delta": dim_means}, indent=2))
