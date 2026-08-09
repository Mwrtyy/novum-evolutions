#!/usr/bin/env python3
"""Mechanical integrity, locking, and post-lock aggregation for EXP-001."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
import math
from pathlib import Path
import random
import re
import statistics
import sys


ROOT = Path(__file__).resolve().parents[1]
VISIBLE = ROOT / "results/EXP-001/visible"
RAW = VISIBLE / "raw"
DEVIATION_RAW = VISIBLE / "protocol-deviations/near-equivalent-prompts"
BLIND = VISIBLE / "blind"
MANIFEST_PATH = BLIND / "JUDGE_MANIFEST.json"
MAPPING_PATH = BLIND / "private/AB_MAPPING.json"
INBOX_PATH = VISIBLE / "judgments-inbox.jsonl"
LOCKED_DIR = VISIBLE / "judgments-locked"
LOCK_PATH = LOCKED_DIR / "LOCK.json"
ANALYSIS_DIR = VISIBLE / "analysis"
OUTPUT_MANIFEST_PATH = VISIBLE / "VISIBLE_OUTPUT_MANIFEST.json"

DIMS = (
    "mechanism_novelty",
    "mechanistic_depth",
    "constraint_fit",
    "usefulness",
    "evidence_calibration",
    "falsifiability",
    "prior_art_awareness",
    "simpler_substitute_discipline",
    "clarity",
)
ROLES = ("hostile_regression", "simplicity", "domain_or_generalist")
PREFERENCES = ("A", "B", "tie")
INDEPENDENCE = (
    "same_context",
    "separate_context_same_model",
    "separate_model_family",
    "human_or_external",
)
EXPECTED_CASES = tuple(f"vr-{i:02d}" for i in range(1, 9))


class ValidationError(ValueError):
    pass


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def canonical_json_bytes(value) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def load_manifest() -> list[dict]:
    data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    if not isinstance(data, list) or len(data) != 72:
        raise ValidationError(f"judge manifest must contain 72 assignments, got {len(data) if isinstance(data, list) else 'non-list'}")
    seen = set()
    coverage = Counter()
    for item in data:
        required = {"judge_id", "pair_id", "role", "prompt_path", "pair_path", "prompt_status"}
        if set(item) != required:
            raise ValidationError(f"manifest fields mismatch for {item.get('judge_id')}")
        assignment = (item["pair_id"], item["role"])
        if assignment in seen:
            raise ValidationError(f"duplicate manifest assignment {assignment}")
        seen.add(assignment)
        coverage[item["pair_id"]] += 1
        if item["role"] not in ROLES:
            raise ValidationError(f"invalid manifest role {item['role']}")
        prompt_path = ROOT / item["prompt_path"]
        pair_path = ROOT / item["pair_path"]
        if not prompt_path.is_file() or not pair_path.is_file():
            raise ValidationError(f"missing public blind material for {item['judge_id']}")
        prompt = prompt_path.read_text(encoding="utf-8")
        if "## Output A" not in prompt or "## Output B" not in prompt:
            raise ValidationError(f"judge prompt missing A/B outputs: {item['judge_id']}")
    if len(coverage) != 24 or set(coverage.values()) != {3}:
        raise ValidationError(f"manifest coverage is not 24 pairs x 3 roles: {dict(coverage)}")
    return data


def audit_visible(write_manifest: bool = False) -> dict:
    raw_paths = sorted(RAW.glob("vr-*/trial-*-*.md"))
    expected_paths = [
        RAW / case / f"trial-{trial}-{arm}.md"
        for case in EXPECTED_CASES
        for trial in range(1, 4)
        for arm in ("baseline", "candidate")
    ]
    if raw_paths != sorted(expected_paths):
        missing = sorted(str(p.relative_to(ROOT)) for p in set(expected_paths) - set(raw_paths))
        extra = sorted(str(p.relative_to(ROOT)) for p in set(raw_paths) - set(expected_paths))
        raise ValidationError(f"raw layout mismatch; missing={missing}, extra={extra}")

    entries = []
    for path in raw_paths:
        data = path.read_bytes()
        text = data.decode("utf-8")
        if not text.strip() or len(text.split()) < 100:
            raise ValidationError(f"empty or implausibly short official output: {path.relative_to(ROOT)}")
        case = path.parent.name
        prompt_status = "FROZEN_EXACT" if case in EXPECTED_CASES[:4] else "ADOPTED_NEAR_EQUIVALENT"
        entries.append({
            "path": str(path.relative_to(ROOT)),
            "sha256": sha256_bytes(data),
            "bytes": len(data),
            "words": len(text.split()),
            "prompt_status": prompt_status,
        })

    adopted_checks = []
    for case in EXPECTED_CASES[4:]:
        for trial in range(1, 4):
            for arm in ("baseline", "candidate"):
                official = RAW / case / f"trial-{trial}-{arm}.md"
                source = DEVIATION_RAW / case / f"trial-{trial}-{arm}.md"
                if not source.is_file():
                    raise ValidationError(f"missing preserved adopted source: {source.relative_to(ROOT)}")
                identical = official.read_bytes() == source.read_bytes()
                if not identical:
                    raise ValidationError(f"adopted raw copy differs from preserved source: {official.relative_to(ROOT)}")
                adopted_checks.append({
                    "official_path": str(official.relative_to(ROOT)),
                    "preserved_source_path": str(source.relative_to(ROOT)),
                    "identical": True,
                })

    manifest = load_manifest()
    packet_hashes = {
        item["pair_path"]: sha256_file(ROOT / item["pair_path"])
        for item in manifest
    }
    prompt_hashes = {
        item["prompt_path"]: sha256_file(ROOT / item["prompt_path"])
        for item in manifest
    }
    result = {
        "schema_version": 1,
        "experiment_id": "EXP-001",
        "phase": "visible_generation_integrity",
        "official_output_count": len(entries),
        "pair_count": len(packet_hashes),
        "judge_assignment_count": len(prompt_hashes),
        "exact_prompt_output_count": sum(x["prompt_status"] == "FROZEN_EXACT" for x in entries),
        "adopted_near_equivalent_output_count": sum(x["prompt_status"] == "ADOPTED_NEAR_EQUIVALENT" for x in entries),
        "adopted_preserved_copy_checks": len(adopted_checks),
        "official_outputs": entries,
        "blind_packet_sha256": packet_hashes,
        "judge_prompt_sha256": prompt_hashes,
        "protocol_deviation": "vr-05 through vr-08 use near-equivalent prompts adopted post-hoc under EXP-001-PROTOCOL-AMENDMENT-001; the visible campaign is not exact-string preregistration compliant.",
    }
    if write_manifest:
        OUTPUT_MANIFEST_PATH.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return result


def read_jsonl(path: Path) -> list[dict]:
    records = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValidationError(f"invalid JSON on line {line_no}: {exc}") from exc
        if not isinstance(value, dict):
            raise ValidationError(f"line {line_no} is not a JSON object")
        records.append(value)
    return records


def validate_record(record: dict, assignment: dict) -> dict:
    required = {
        "pair_id", "evaluator_id", "evaluator_role", "scores",
        "preference", "critical_flags", "rationale",
    }
    allowed = required | {"independence", "judge_provider", "judge_model", "notes"}
    missing = required - set(record)
    unknown = set(record) - allowed
    if missing:
        raise ValidationError(f"{assignment['judge_id']}: missing fields {sorted(missing)}")
    if unknown:
        raise ValidationError(f"{assignment['judge_id']}: unknown fields {sorted(unknown)}")
    if record["pair_id"] != assignment["pair_id"]:
        raise ValidationError(f"{assignment['judge_id']}: pair_id mismatch")
    if record["evaluator_role"] != assignment["role"] or record["evaluator_role"] not in ROLES:
        raise ValidationError(f"{assignment['judge_id']}: evaluator_role mismatch")
    if not isinstance(record["evaluator_id"], str) or not record["evaluator_id"].strip():
        raise ValidationError(f"{assignment['judge_id']}: evaluator_id must be non-empty")
    if record["preference"] not in PREFERENCES:
        raise ValidationError(f"{assignment['judge_id']}: invalid preference")
    if not isinstance(record["critical_flags"], list) or not all(isinstance(x, str) and x.strip() for x in record["critical_flags"]):
        raise ValidationError(f"{assignment['judge_id']}: critical_flags must be a list of non-empty strings")
    if not isinstance(record["rationale"], str) or not record["rationale"].strip():
        raise ValidationError(f"{assignment['judge_id']}: rationale must be non-empty")
    independence = record.get("independence", "separate_context_same_model")
    if independence not in INDEPENDENCE:
        raise ValidationError(f"{assignment['judge_id']}: invalid independence")
    scores = record["scores"]
    if not isinstance(scores, dict) or set(scores) != {"A", "B"}:
        raise ValidationError(f"{assignment['judge_id']}: scores must contain exactly A and B")
    normalized_scores = {}
    for arm in ("A", "B"):
        arm_scores = scores[arm]
        if not isinstance(arm_scores, dict) or set(arm_scores) != set(DIMS):
            raise ValidationError(f"{assignment['judge_id']}: {arm} dimensions mismatch")
        normalized_scores[arm] = {}
        for dim in DIMS:
            value = arm_scores[dim]
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(float(value)):
                raise ValidationError(f"{assignment['judge_id']}: {arm}.{dim} must be a finite number")
            value = float(value)
            if not 0 <= value <= 10:
                raise ValidationError(f"{assignment['judge_id']}: {arm}.{dim} out of range")
            normalized_scores[arm][dim] = value
    normalized = {
        "pair_id": record["pair_id"],
        "assignment_id": assignment["judge_id"],
        "evaluator_id": record["evaluator_id"].strip(),
        "evaluator_role": record["evaluator_role"],
        "independence": independence,
        "scores": normalized_scores,
        "preference": record["preference"],
        "critical_flags": record["critical_flags"],
        "rationale": record["rationale"].strip(),
        "prompt_status": assignment["prompt_status"],
    }
    for key in ("judge_provider", "judge_model", "notes"):
        if key in record:
            normalized[key] = record[key]
    return normalized


def validate_judgments(path: Path) -> list[dict]:
    manifest = load_manifest()
    submitted = read_jsonl(path)
    if len(submitted) != 72:
        raise ValidationError(f"expected exactly 72 judgment records, got {len(submitted)}")
    by_assignment = {}
    for record in submitted:
        key = (record.get("pair_id"), record.get("evaluator_role"))
        if key in by_assignment:
            raise ValidationError(f"duplicate judgment assignment {key}")
        by_assignment[key] = record
    normalized = []
    for item in manifest:
        key = (item["pair_id"], item["role"])
        if key not in by_assignment:
            raise ValidationError(f"missing judgment assignment {key}")
        normalized.append(validate_record(by_assignment[key], item))
    return normalized


def lock_judgments(path: Path) -> dict:
    audit_visible(write_manifest=True)
    normalized = validate_judgments(path)
    canonical = b"".join(canonical_json_bytes(x) for x in normalized)
    set_hash = sha256_bytes(canonical)
    if LOCK_PATH.exists():
        existing = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
        if existing.get("judgment_set_sha256") == set_hash:
            return existing
        raise ValidationError("a different judgment set is already locked; frozen judgments cannot be overwritten")

    LOCKED_DIR.mkdir(parents=True, exist_ok=True)
    for record in normalized:
        path_out = LOCKED_DIR / f"{record['assignment_id']}.json"
        path_out.write_bytes(canonical_json_bytes(record))
    evaluator_load = Counter(x["evaluator_id"] for x in normalized)
    lock = {
        "schema_version": 1,
        "experiment_id": "EXP-001",
        "phase": "visible_blind_judgments_locked",
        "judgment_count": len(normalized),
        "pair_count": len({x["pair_id"] for x in normalized}),
        "assignment_count": len({x["assignment_id"] for x in normalized}),
        "judgment_set_sha256": set_hash,
        "judge_manifest_sha256": sha256_file(MANIFEST_PATH),
        "visible_output_manifest_sha256": sha256_file(OUTPUT_MANIFEST_PATH),
        "independence_counts": dict(Counter(x["independence"] for x in normalized)),
        "evaluator_load": dict(evaluator_load),
        "mapping_reveal_allowed": True,
        "mapping_used_during_validation_or_lock": False,
        "limitation": "Fresh evaluator contexts from the same model family are not external replication.",
    }
    LOCK_PATH.write_bytes(canonical_json_bytes(lock))
    return lock


def verify_lock() -> tuple[dict, list[dict]]:
    if not LOCK_PATH.is_file():
        raise ValidationError("no judgment lock exists")
    lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    manifest = load_manifest()
    records = []
    for item in manifest:
        path = LOCKED_DIR / f"{item['judge_id']}.json"
        if not path.is_file():
            raise ValidationError(f"locked judgment missing: {item['judge_id']}")
        records.append(json.loads(path.read_text(encoding="utf-8")))
    canonical = b"".join(canonical_json_bytes(x) for x in records)
    if sha256_bytes(canonical) != lock.get("judgment_set_sha256"):
        raise ValidationError("locked judgment hash mismatch")
    if sha256_file(MANIFEST_PATH) != lock.get("judge_manifest_sha256"):
        raise ValidationError("judge manifest changed after lock")
    if sha256_file(OUTPUT_MANIFEST_PATH) != lock.get("visible_output_manifest_sha256"):
        raise ValidationError("visible output manifest changed after lock")
    return lock, records


def mean(values):
    return statistics.fmean(values) if values else None


def sample_sd(values):
    return statistics.stdev(values) if len(values) > 1 else 0.0


def percentile(sorted_values, p):
    if not sorted_values:
        return None
    pos = (len(sorted_values) - 1) * p
    lo, hi = math.floor(pos), math.ceil(pos)
    if lo == hi:
        return sorted_values[lo]
    return sorted_values[lo] + (sorted_values[hi] - sorted_values[lo]) * (pos - lo)


def bootstrap_ci(records, value_fn, seed=1001001, iterations=10000):
    by_pair = defaultdict(list)
    for record in records:
        by_pair[record["pair_id"]].append(record)
    pair_ids = sorted(by_pair)
    rng = random.Random(seed)
    estimates = []
    for _ in range(iterations):
        sample = []
        for pair_id in rng.choices(pair_ids, k=len(pair_ids)):
            sample.extend(by_pair[pair_id])
        estimates.append(value_fn(sample))
    estimates.sort()
    return [percentile(estimates, 0.025), percentile(estimates, 0.975)]


def preference_win_value(record):
    return 1.0 if record["preference"] == "candidate" else 0.5 if record["preference"] == "tie" else 0.0


def group_summary(records: list[dict]) -> dict:
    prefs = Counter(x["preference"] for x in records)
    decided = prefs["candidate"] + prefs["baseline"]
    result = {
        "judgments": len(records),
        "preferences": {k: prefs.get(k, 0) for k in ("candidate", "baseline", "tie")},
        "tie_adjusted_candidate_win_rate": mean([preference_win_value(x) for x in records]),
        "candidate_win_rate_excluding_ties": prefs["candidate"] / decided if decided else None,
        "mean_scores": {
            "candidate": {d: mean([x["candidate_scores"][d] for x in records]) for d in DIMS},
            "baseline": {d: mean([x["baseline_scores"][d] for x in records]) for d in DIMS},
        },
        "mean_candidate_minus_baseline": {d: mean([x["delta"][d] for x in records]) for d in DIMS},
    }
    return result


def fleiss_kappa(records: list[dict]) -> float | None:
    by_pair = defaultdict(Counter)
    for record in records:
        by_pair[record["pair_id"]][record["preference"]] += 1
    if not by_pair or any(sum(counts.values()) != 3 for counts in by_pair.values()):
        return None
    categories = ("candidate", "baseline", "tie")
    n = 3
    observed = mean([
        sum(counts[c] * (counts[c] - 1) for c in categories) / (n * (n - 1))
        for counts in by_pair.values()
    ])
    totals = Counter()
    for counts in by_pair.values():
        totals.update(counts)
    denom = len(by_pair) * n
    expected = sum((totals[c] / denom) ** 2 for c in categories)
    return (observed - expected) / (1 - expected) if expected < 1 else None


def translate_flags(flag: str, mapping: dict) -> list[dict]:
    # Preserve flags exactly while splitting only explicit "A: ...; B: ..." targets.
    parts = re.split(r";\s*(?=[AB]\s*:)", flag, flags=re.IGNORECASE)
    translated = []
    for part in parts:
        match = re.match(r"^\s*([AB])\s*:\s*(.*)$", part, flags=re.IGNORECASE)
        if not match:
            translated.append({"target": "unspecified_or_both", "text": part})
        else:
            arm = match.group(1).upper()
            translated.append({"target": mapping[arm], "text": match.group(2)})
    return translated


def aggregate() -> dict:
    lock, locked = verify_lock()
    mapping = json.loads(MAPPING_PATH.read_text(encoding="utf-8"))
    if set(mapping) != {f"vr-{case:02d}-t{trial}" for case in range(1, 9) for trial in range(1, 4)}:
        raise ValidationError("private mapping does not cover exactly 24 expected pairs")

    manifest_by_assignment = {x["judge_id"]: x for x in load_manifest()}
    records = []
    translated_flags = []
    for judgment in locked:
        item = manifest_by_assignment[judgment["assignment_id"]]
        pair_map = mapping[judgment["pair_id"]]
        if {pair_map.get("A"), pair_map.get("B")} != {"baseline", "candidate"}:
            raise ValidationError(f"invalid A/B mapping for {judgment['pair_id']}")
        candidate_arm = "A" if pair_map["A"] == "candidate" else "B"
        baseline_arm = "B" if candidate_arm == "A" else "A"
        pref = judgment["preference"]
        translated_pref = "tie" if pref == "tie" else "candidate" if pref == candidate_arm else "baseline"
        candidate_scores = judgment["scores"][candidate_arm]
        baseline_scores = judgment["scores"][baseline_arm]
        record = {
            "assignment_id": judgment["assignment_id"],
            "pair_id": judgment["pair_id"],
            "case_id": pair_map["case_id"],
            "trial": pair_map["trial"],
            "role": item["role"],
            "evaluator_id": judgment["evaluator_id"],
            "independence": judgment["independence"],
            "prompt_status": pair_map["prompt_status"],
            "preference": translated_pref,
            "candidate_scores": candidate_scores,
            "baseline_scores": baseline_scores,
            "delta": {d: candidate_scores[d] - baseline_scores[d] for d in DIMS},
            "critical_flags": [
                translated
                for flag in judgment["critical_flags"]
                for translated in translate_flags(flag, pair_map)
            ],
            "rationale": judgment["rationale"],
        }
        translated_flags.extend({"pair_id": judgment["pair_id"], "role": item["role"], **flag} for flag in record["critical_flags"])
        records.append(record)

    overall = group_summary(records)
    overall["tie_adjusted_candidate_win_rate_cluster_bootstrap_95ci"] = bootstrap_ci(
        records, lambda xs: mean([preference_win_value(x) for x in xs])
    )
    effect_sizes = {}
    uncertainty = {}
    for dim in DIMS:
        deltas = [x["delta"][dim] for x in records]
        sd = sample_sd(deltas)
        effect_sizes[dim] = {
            "paired_standardized_mean_difference_dz": mean(deltas) / sd if sd else None,
            "delta_sample_sd": sd,
        }
        uncertainty[dim] = {
            "cluster_bootstrap_mean_delta_95ci": bootstrap_ci(records, lambda xs, d=dim: mean([x["delta"][d] for x in xs])),
        }

    by_pair_records = defaultdict(list)
    for record in records:
        by_pair_records[record["pair_id"]].append(record)
    pairs = {}
    for pair_id, values in sorted(by_pair_records.items()):
        prefs = Counter(x["preference"] for x in values)
        c, b = prefs["candidate"], prefs["baseline"]
        winner = "candidate" if c > b else "baseline" if b > c else "tie"
        overall_delta_by_role = [mean(list(x["delta"].values())) for x in values]
        pairs[pair_id] = {
            "case_id": values[0]["case_id"],
            "trial": values[0]["trial"],
            "prompt_status": values[0]["prompt_status"],
            "majority_winner": winner,
            "preference_votes": {k: prefs.get(k, 0) for k in ("candidate", "baseline", "tie")},
            "mean_candidate_minus_baseline": {d: mean([x["delta"][d] for x in values]) for d in DIMS},
            "overall_delta_range_across_roles": max(overall_delta_by_role) - min(overall_delta_by_role),
            "unanimous_preference": max(prefs.values()) == 3,
        }
    pair_majorities = Counter(x["majority_winner"] for x in pairs.values())
    decided_pairs = pair_majorities["candidate"] + pair_majorities["baseline"]

    by_case = {}
    for case_id in sorted({x["case_id"] for x in records}):
        subset = [x for x in records if x["case_id"] == case_id]
        summary = group_summary(subset)
        case_pair_ids = sorted({x["pair_id"] for x in subset})
        summary["pair_majorities"] = dict(Counter(pairs[pair_id]["majority_winner"] for pair_id in case_pair_ids))
        summary["prompt_status"] = subset[0]["prompt_status"]
        by_case[case_id] = summary
    by_trial = {str(trial): group_summary([x for x in records if x["trial"] == trial]) for trial in range(1, 4)}
    by_role = {role: group_summary([x for x in records if x["role"] == role]) for role in ROLES}
    by_prompt_status = {
        status: group_summary([x for x in records if x["prompt_status"] == status])
        for status in ("FROZEN_EXACT", "ADOPTED_NEAR_EQUIVALENT")
    }

    regression_dimensions = [d for d in DIMS if overall["mean_candidate_minus_baseline"][d] < 0]
    baseline_winning_pairs = [pair_id for pair_id, value in pairs.items() if value["majority_winner"] == "baseline"]
    disagreement = {
        "fleiss_kappa_preference_three_categories": fleiss_kappa(records),
        "unanimous_preference_pairs": sum(x["unanimous_preference"] for x in pairs.values()),
        "split_preference_pairs": sum(not x["unanimous_preference"] for x in pairs.values()),
        "mean_overall_delta_range_across_roles": mean([x["overall_delta_range_across_roles"] for x in pairs.values()]),
        "interpretation": "Role judgments are separate fresh contexts from the same model family; disagreement is informative but not external-replication variance.",
    }

    result = {
        "schema_version": 1,
        "experiment_id": "EXP-001",
        "phase": "visible_blind_judging_revealed_after_lock",
        "lock": lock,
        "judgments": len(records),
        "pairs": len(pairs),
        "overall": overall,
        "pair_majority_counts": {k: pair_majorities.get(k, 0) for k in ("candidate", "baseline", "tie")},
        "pair_majority_candidate_win_rate_excluding_ties": pair_majorities["candidate"] / decided_pairs if decided_pairs else None,
        "pair_majority_tie_adjusted_candidate_win_rate": (
            pair_majorities["candidate"] + 0.5 * pair_majorities["tie"]
        ) / len(pairs),
        "effect_sizes": effect_sizes,
        "uncertainty": uncertainty,
        "by_case": by_case,
        "by_trial": by_trial,
        "by_role": by_role,
        "by_prompt_status": by_prompt_status,
        "inter_judge_disagreement": disagreement,
        "regressions": {
            "negative_mean_delta_dimensions": regression_dimensions,
            "baseline_majority_pairs": baseline_winning_pairs,
        },
        "critical_flags": {
            "count": len(translated_flags),
            "by_target": dict(Counter(x["target"] for x in translated_flags)),
            "items": translated_flags,
        },
        "pairs_detail": pairs,
        "protocol_deviation": "vr-05 through vr-08 used post-hoc adopted near-equivalent prompts. Visible evidence is not exact-string preregistration compliant.",
        "decision_boundary": "No PROMOTE/PARTIAL WIN/REJECT/INCONCLUSIVE decision is authorized from the visible set alone. A strict post-freeze hidden holdout and protocol audit remain required.",
        "replication_boundary": "All three role evaluators used separate fresh contexts in the same model family. This is not external replication.",
    }
    ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)
    (ANALYSIS_DIR / "VISIBLE_JUDGING_ANALYSIS.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_markdown_analysis(result)
    return result


def fmt(value, digits=3):
    return "n/a" if value is None else f"{value:.{digits}f}"


def write_markdown_analysis(result: dict) -> None:
    overall = result["overall"]
    pc = result["pair_majority_counts"]
    prefs = overall["preferences"]
    lines = [
        "# EXP-001 Visible Blind-Judging Analysis", "",
        "Status: `VISIBLE_JUDGING_COMPLETE_HIDDEN_HOLDOUT_REQUIRED`", "",
        f"- Locked judgments: **{result['judgments']}/72** across **{result['pairs']}/24** blinded pairs.",
        f"- Pair-majority: candidate **{pc['candidate']}**, baseline **{pc['baseline']}**, tie **{pc['tie']}**.",
        f"- Judge preferences: candidate **{prefs['candidate']}**, baseline **{prefs['baseline']}**, tie **{prefs['tie']}**.",
        f"- Tie-adjusted candidate judge win rate: **{overall['tie_adjusted_candidate_win_rate']:.1%}** (pair-cluster bootstrap 95% CI {overall['tie_adjusted_candidate_win_rate_cluster_bootstrap_95ci'][0]:.1%}–{overall['tie_adjusted_candidate_win_rate_cluster_bootstrap_95ci'][1]:.1%}).", "",
        "## Scores and deltas", "",
        "| Dimension | Baseline mean | Candidate mean | Delta C−B | dz | Cluster-bootstrap 95% CI |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for dim in DIMS:
        ci = result["uncertainty"][dim]["cluster_bootstrap_mean_delta_95ci"]
        dz = result["effect_sizes"][dim]["paired_standardized_mean_difference_dz"]
        lines.append(
            f"| {dim} | {overall['mean_scores']['baseline'][dim]:.3f} | {overall['mean_scores']['candidate'][dim]:.3f} | {overall['mean_candidate_minus_baseline'][dim]:+.3f} | {fmt(dz)} | [{ci[0]:+.3f}, {ci[1]:+.3f}] |"
        )
    lines += ["", "## Results by case", "", "| Case | Prompt status | Candidate prefs | Baseline prefs | Ties | Pair majorities C/B/tie | Mean delta across dimensions |", "|---|---|---:|---:|---:|---:|---:|"]
    for case_id, data in result["by_case"].items():
        p = data["preferences"]
        delta = mean(list(data["mean_candidate_minus_baseline"].values()))
        pm = data["pair_majorities"]
        lines.append(f"| {case_id} | {data['prompt_status']} | {p['candidate']} | {p['baseline']} | {p['tie']} | {pm.get('candidate', 0)}/{pm.get('baseline', 0)}/{pm.get('tie', 0)} | {delta:+.3f} |")
    lines += ["", "## Results by trial", "", "| Trial | Candidate prefs | Baseline prefs | Ties | Mean delta across dimensions |", "|---:|---:|---:|---:|---:|"]
    for trial, data in result["by_trial"].items():
        p = data["preferences"]
        delta = mean(list(data["mean_candidate_minus_baseline"].values()))
        lines.append(f"| {trial} | {p['candidate']} | {p['baseline']} | {p['tie']} | {delta:+.3f} |")
    lines += ["", "## Results by evaluator role", "", "| Role | Candidate prefs | Baseline prefs | Ties | Mean delta across dimensions |", "|---|---:|---:|---:|---:|"]
    for role, data in result["by_role"].items():
        p = data["preferences"]
        delta = mean(list(data["mean_candidate_minus_baseline"].values()))
        lines.append(f"| {role} | {p['candidate']} | {p['baseline']} | {p['tie']} | {delta:+.3f} |")
    disagreement = result["inter_judge_disagreement"]
    lines += [
        "", "## Disagreement, regressions, and flags", "",
        f"- Fleiss’ kappa over candidate/baseline/tie preferences: **{fmt(disagreement['fleiss_kappa_preference_three_categories'])}**.",
        f"- Unanimous pairs: **{disagreement['unanimous_preference_pairs']}**; split pairs: **{disagreement['split_preference_pairs']}**.",
        f"- Dimensions with negative mean delta: **{', '.join(result['regressions']['negative_mean_delta_dimensions']) or 'none'}**.",
        f"- Baseline-majority pairs: **{', '.join(result['regressions']['baseline_majority_pairs']) or 'none'}**.",
        f"- Critical flags preserved: **{result['critical_flags']['count']}**; arm-prefixed flags were translated only after reveal.", "",
        "### Candidate-targeted critical flags", "",
    ]
    candidate_flags = [x for x in result["critical_flags"]["items"] if x["target"] == "candidate"]
    lines.extend(f"- \x60{x['pair_id']}\x60 / \x60{x['role']}\x60 — {x['text']}" for x in candidate_flags)
    if not candidate_flags:
        lines.append("- None.")
    lines += [
        "", "All baseline-targeted and unspecified/both flags remain preserved in \x60VISIBLE_JUDGING_ANALYSIS.json\x60.", "",
        "## Limits and interpretation boundary", "",
        "- `vr-01`–`vr-04` used exact frozen prompts; `vr-05`–`vr-08` used near-equivalent prompts adopted post-hoc. The campaign is not exact-string preregistration compliant.",
        "- Evaluators were fresh contexts from the same model family. This reduces shared conversation context but is not independent external replication.",
        "- The 72 judgments are nested within 24 pairs; cluster-bootstrap intervals account for pair clustering, but eight visible cases remain a small, development-visible sample.",
        "- Effect sizes are descriptive paired dz values across judge records, not population guarantees.",
        "- No promotion decision is authorized from the visible set alone. The next evidentiary phase is the strict post-freeze hidden holdout, followed by a protocol audit.", "",
    ]
    (ANALYSIS_DIR / "VISIBLE_JUDGING_ANALYSIS.md").write_text("\n".join(lines), encoding="utf-8")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    audit_parser = sub.add_parser("audit-visible")
    audit_parser.add_argument("--write-manifest", action="store_true")
    validate_parser = sub.add_parser("validate")
    validate_parser.add_argument("path", nargs="?", type=Path, default=INBOX_PATH)
    lock_parser = sub.add_parser("lock")
    lock_parser.add_argument("path", nargs="?", type=Path, default=INBOX_PATH)
    sub.add_parser("aggregate")
    args = parser.parse_args(argv)
    if args.command == "audit-visible":
        result = audit_visible(write_manifest=args.write_manifest)
        print(json.dumps({k: result[k] for k in ("official_output_count", "pair_count", "judge_assignment_count", "exact_prompt_output_count", "adopted_near_equivalent_output_count", "adopted_preserved_copy_checks")}, indent=2))
    elif args.command == "validate":
        records = validate_judgments(args.path)
        print(json.dumps({"valid": True, "judgments": len(records), "pairs": len({x['pair_id'] for x in records})}, indent=2))
    elif args.command == "lock":
        print(json.dumps(lock_judgments(args.path), indent=2))
    else:
        result = aggregate()
        print(json.dumps({"pair_majority_counts": result["pair_majority_counts"], "tie_adjusted_candidate_win_rate": result["overall"]["tie_adjusted_candidate_win_rate"], "negative_mean_delta_dimensions": result["regressions"]["negative_mean_delta_dimensions"]}, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValidationError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2)
