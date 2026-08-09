#!/usr/bin/env python3
"""Lock blinded judgments and aggregate only after an explicit reveal."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
import math
from pathlib import Path
import random
import statistics
import sys

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
PREFS = ("A", "B", "tie")
INDEPENDENCE = {
    "same_context",
    "separate_context_same_model",
    "separate_context_same_model_per_packet",
    "human_or_external",
    "separate_model_family",
}


class ValidationError(ValueError):
    pass


def canonical(value) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def expected_assignments(pair_ids):
    return {(pair_id, role) for pair_id in pair_ids for role in ROLES}


def validate_record(record, expected):
    required = {
        "pair_id", "evaluator_id", "evaluator_role", "independence",
        "scores", "preference", "critical_flags", "rationale",
    }
    if set(record) != required:
        raise ValidationError(f"field mismatch for {record.get('evaluator_id')}: {set(record) ^ required}")
    assignment = (record["pair_id"], record["evaluator_role"])
    if assignment not in expected:
        raise ValidationError(f"unexpected assignment {assignment}")
    if not isinstance(record["evaluator_id"], str) or not record["evaluator_id"].strip():
        raise ValidationError(f"empty evaluator_id for {assignment}")
    if record["independence"] not in INDEPENDENCE:
        raise ValidationError(f"invalid independence for {assignment}")
    if record["preference"] not in PREFS:
        raise ValidationError(f"invalid preference for {assignment}")
    if not isinstance(record["critical_flags"], list) or not all(isinstance(x, str) for x in record["critical_flags"]):
        raise ValidationError(f"invalid critical_flags for {assignment}")
    if not isinstance(record["rationale"], str) or not record["rationale"].strip():
        raise ValidationError(f"empty rationale for {assignment}")
    if set(record["scores"]) != {"A", "B"}:
        raise ValidationError(f"score arms mismatch for {assignment}")
    for arm in ("A", "B"):
        scores = record["scores"][arm]
        if set(scores) != set(DIMS):
            raise ValidationError(f"dimension mismatch for {assignment}/{arm}")
        for dim, value in scores.items():
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise ValidationError(f"nonnumeric score for {assignment}/{arm}/{dim}")
            if not math.isfinite(value) or not 0 <= value <= 10:
                raise ValidationError(f"out-of-range score for {assignment}/{arm}/{dim}")
    return assignment


def read_judgments(directory: Path, pair_ids):
    expected = expected_assignments(pair_ids)
    records = []
    seen_assignments = set()
    seen_evaluators = set()
    for path in sorted(directory.glob("*.json")):
        if path.name.endswith("MANIFEST.json") or path.name == "LOCK.json":
            continue
        record = load_json(path)
        assignment = validate_record(record, expected)
        if assignment in seen_assignments:
            raise ValidationError(f"duplicate assignment {assignment}")
        if record["evaluator_id"] in seen_evaluators:
            raise ValidationError(f"duplicate evaluator_id {record['evaluator_id']}")
        seen_assignments.add(assignment)
        seen_evaluators.add(record["evaluator_id"])
        records.append(record)
    missing = expected - seen_assignments
    extra = seen_assignments - expected
    if missing or extra:
        raise ValidationError(f"coverage mismatch missing={sorted(missing)} extra={sorted(extra)}")
    records.sort(key=lambda x: (x["pair_id"], ROLES.index(x["evaluator_role"])))
    return records


def cmd_lock(args):
    pair_ids = load_json(args.pair_ids)
    if not isinstance(pair_ids, list) or len(pair_ids) != len(set(pair_ids)):
        raise ValidationError("pair_ids must be a unique JSON list")
    records = read_judgments(args.judgments_dir, pair_ids)
    payload = b"".join(canonical(x) for x in records)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    locked_path = args.output_dir / "JUDGMENTS_LOCKED.jsonl"
    locked_path.write_bytes(payload)
    lock = {
        "schema_version": 1,
        "experiment_id": "EXP-001",
        "phase": args.phase,
        "status": "JUDGMENTS_LOCKED_MAPPING_NOT_USED",
        "pair_count": len(pair_ids),
        "judgment_count": len(records),
        "roles": list(ROLES),
        "dimensions": list(DIMS),
        "judgment_set_sha256": sha256_bytes(payload),
        "pair_ids_sha256": sha256_file(args.pair_ids),
        "mapping_used_during_validation_or_lock": False,
        "independence_counts": dict(Counter(x["independence"] for x in records)),
    }
    lock_path = args.output_dir / "LOCK.json"
    lock_path.write_text(json.dumps(lock, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"valid": True, **lock, "lock_file_sha256": sha256_file(lock_path)}, indent=2))


def verify_lock(locked_path, lock_path):
    lock = load_json(lock_path)
    if sha256_file(locked_path) != lock["judgment_set_sha256"]:
        raise ValidationError("locked judgment set hash mismatch")
    records = [json.loads(line) for line in locked_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if len(records) != lock["judgment_count"]:
        raise ValidationError("locked judgment count mismatch")
    return lock, records


def mean(values):
    return statistics.fmean(values) if values else None


def sample_sd(values):
    return statistics.stdev(values) if len(values) > 1 else 0.0


def percentile(values, p):
    values = sorted(values)
    pos = (len(values) - 1) * p
    lo, hi = math.floor(pos), math.ceil(pos)
    if lo == hi:
        return values[lo]
    return values[lo] + (values[hi] - values[lo]) * (pos - lo)


def bootstrap(records, fn, seed=1001001, iterations=10000):
    by_pair = defaultdict(list)
    for record in records:
        by_pair[record["pair_id"]].append(record)
    ids = sorted(by_pair)
    rng = random.Random(seed)
    estimates = []
    for _ in range(iterations):
        sample = []
        for pair_id in rng.choices(ids, k=len(ids)):
            sample.extend(by_pair[pair_id])
        estimates.append(fn(sample))
    return [percentile(estimates, 0.025), percentile(estimates, 0.975)]


def win_value(record):
    return 1.0 if record["preference"] == "candidate" else 0.5 if record["preference"] == "tie" else 0.0


def group_summary(records):
    prefs = Counter(x["preference"] for x in records)
    decided = prefs["candidate"] + prefs["baseline"]
    return {
        "judgments": len(records),
        "preferences": {k: prefs[k] for k in ("candidate", "baseline", "tie")},
        "tie_adjusted_candidate_win_rate": mean([win_value(x) for x in records]),
        "candidate_win_rate_excluding_ties": prefs["candidate"] / decided if decided else None,
        "mean_scores": {
            arm: {dim: mean([x[f"{arm}_scores"][dim] for x in records]) for dim in DIMS}
            for arm in ("candidate", "baseline")
        },
        "mean_candidate_minus_baseline": {
            dim: mean([x["delta"][dim] for x in records]) for dim in DIMS
        },
    }


def fleiss_kappa(records):
    by_pair = defaultdict(Counter)
    for record in records:
        by_pair[record["pair_id"]][record["preference"]] += 1
    if not by_pair or any(sum(x.values()) != 3 for x in by_pair.values()):
        return None
    categories = ("candidate", "baseline", "tie")
    observed = mean([
        sum(counts[c] * (counts[c] - 1) for c in categories) / 6
        for counts in by_pair.values()
    ])
    totals = Counter()
    for counts in by_pair.values():
        totals.update(counts)
    denom = len(by_pair) * 3
    expected = sum((totals[c] / denom) ** 2 for c in categories)
    return (observed - expected) / (1 - expected) if expected < 1 else None


def cmd_aggregate(args):
    lock, blinded = verify_lock(args.locked, args.lock)
    mapping = load_json(args.mapping)
    metadata = load_json(args.pair_metadata)
    expected_pairs = {x["pair_id"] for x in metadata}
    if set(mapping) != expected_pairs:
        raise ValidationError("mapping coverage mismatch")
    meta = {x["pair_id"]: x for x in metadata}
    records = []
    for judgment in blinded:
        pair_map = mapping[judgment["pair_id"]]
        if {pair_map["A"], pair_map["B"]} != {"baseline", "candidate"}:
            raise ValidationError(f"invalid mapping for {judgment['pair_id']}")
        candidate_arm = "A" if pair_map["A"] == "candidate" else "B"
        baseline_arm = "B" if candidate_arm == "A" else "A"
        pref = judgment["preference"]
        translated = "tie" if pref == "tie" else "candidate" if pref == candidate_arm else "baseline"
        candidate_scores = judgment["scores"][candidate_arm]
        baseline_scores = judgment["scores"][baseline_arm]
        item = {
            **judgment,
            **{k: v for k, v in meta[judgment["pair_id"]].items() if k != "pair_id"},
            "preference": translated,
            "candidate_scores": candidate_scores,
            "baseline_scores": baseline_scores,
            "delta": {dim: candidate_scores[dim] - baseline_scores[dim] for dim in DIMS},
        }
        records.append(item)
    overall = group_summary(records)
    overall["tie_adjusted_candidate_win_rate_cluster_bootstrap_95ci"] = bootstrap(
        records, lambda xs: mean([win_value(x) for x in xs])
    )
    by_pair = defaultdict(list)
    for record in records:
        by_pair[record["pair_id"]].append(record)
    pairs = {}
    for pair_id, values in sorted(by_pair.items()):
        prefs = Counter(x["preference"] for x in values)
        winner = "candidate" if prefs["candidate"] > prefs["baseline"] else "baseline" if prefs["baseline"] > prefs["candidate"] else "tie"
        pairs[pair_id] = {
            "case_id": values[0]["case_id"],
            "trial": values[0]["trial"],
            "majority_winner": winner,
            "preference_votes": {k: prefs[k] for k in ("candidate", "baseline", "tie")},
            "mean_candidate_minus_baseline": {
                dim: mean([x["delta"][dim] for x in values]) for dim in DIMS
            },
            "unanimous_preference": max(prefs.values()) == 3,
        }
    pair_majorities = Counter(x["majority_winner"] for x in pairs.values())
    decided_pairs = pair_majorities["candidate"] + pair_majorities["baseline"]
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
            "cluster_bootstrap_mean_delta_95ci": bootstrap(
                records, lambda xs, d=dim: mean([x["delta"][d] for x in xs])
            )
        }
    result = {
        "schema_version": 1,
        "experiment_id": "EXP-001",
        "phase": args.phase,
        "irreversible_transition": "A/B revealed only after verified judgment lock",
        "lock": lock,
        "mapping_sha256": sha256_file(args.mapping),
        "pairs": len(pairs),
        "judgments": len(records),
        "overall": overall,
        "pair_majority_counts": {k: pair_majorities[k] for k in ("candidate", "baseline", "tie")},
        "pair_majority_candidate_win_rate_excluding_ties": pair_majorities["candidate"] / decided_pairs if decided_pairs else None,
        "pair_majority_tie_adjusted_candidate_win_rate": (pair_majorities["candidate"] + .5 * pair_majorities["tie"]) / len(pairs),
        "effect_sizes": effect_sizes,
        "uncertainty": uncertainty,
        "by_case": {
            case: {
                **group_summary([x for x in records if x["case_id"] == case]),
                "pair_majorities": dict(Counter(
                    pairs[pair_id]["majority_winner"]
                    for pair_id in pairs if pairs[pair_id]["case_id"] == case
                )),
            }
            for case in sorted({x["case_id"] for x in records})
        },
        "by_trial": {
            str(trial): group_summary([x for x in records if x["trial"] == trial])
            for trial in sorted({x["trial"] for x in records})
        },
        "by_role": {
            role: group_summary([x for x in records if x["evaluator_role"] == role])
            for role in ROLES
        },
        "by_prompt_status": {
            status: group_summary([x for x in records if x.get("prompt_status") == status])
            for status in sorted({x.get("prompt_status") for x in records if x.get("prompt_status")})
        },
        "inter_judge_disagreement": {
            "fleiss_kappa_preference_three_categories": fleiss_kappa(records),
            "unanimous_preference_pairs": sum(x["unanimous_preference"] for x in pairs.values()),
            "split_preference_pairs": sum(not x["unanimous_preference"] for x in pairs.values()),
        },
        "regressions": {
            "negative_mean_delta_dimensions": [
                dim for dim in DIMS if overall["mean_candidate_minus_baseline"][dim] < 0
            ],
            "baseline_majority_pairs": [
                pair_id for pair_id, value in pairs.items() if value["majority_winner"] == "baseline"
            ],
        },
        "critical_flags": [
            {"pair_id": x["pair_id"], "role": x["evaluator_role"], "items": x["critical_flags"]}
            for x in records if x["critical_flags"]
        ],
        "pairs_detail": pairs,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "pair_majority_counts": result["pair_majority_counts"],
        "preferences": overall["preferences"],
        "tie_adjusted_candidate_win_rate": overall["tie_adjusted_candidate_win_rate"],
        "negative_mean_delta_dimensions": result["regressions"]["negative_mean_delta_dimensions"],
        "analysis_sha256": sha256_file(args.output),
    }, indent=2))


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    lock = sub.add_parser("lock")
    lock.add_argument("--phase", required=True)
    lock.add_argument("--judgments-dir", type=Path, required=True)
    lock.add_argument("--pair-ids", type=Path, required=True)
    lock.add_argument("--output-dir", type=Path, required=True)
    lock.set_defaults(func=cmd_lock)
    aggregate = sub.add_parser("aggregate")
    aggregate.add_argument("--phase", required=True)
    aggregate.add_argument("--locked", type=Path, required=True)
    aggregate.add_argument("--lock", type=Path, required=True)
    aggregate.add_argument("--mapping", type=Path, required=True)
    aggregate.add_argument("--pair-metadata", type=Path, required=True)
    aggregate.add_argument("--output", type=Path, required=True)
    aggregate.set_defaults(func=cmd_aggregate)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    try:
        main()
    except ValidationError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2)
