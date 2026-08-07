#!/usr/bin/env python3
"""Minimal blind A/B harness for NOVUM behavioral experiments.

The harness deliberately does not judge semantic invention quality. It validates
coverage, blinds identity, and aggregates already-locked evaluator judgments.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import statistics
import tempfile
from collections import defaultdict
from pathlib import Path

DIMENSIONS = (
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
ROLES = {"hostile_regression", "simplicity", "domain_or_generalist"}


def load_jsonl(path: Path) -> list[dict]:
    rows = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{n}: invalid JSON: {exc}") from exc
    return rows


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def validate_cases(path: Path) -> dict:
    rows = load_jsonl(path)
    seen = set()
    for row in rows:
        required = {"id", "domain", "prompt", "known_failure_families", "judge_focus"}
        missing = required - set(row)
        if missing:
            raise ValueError(f"case {row.get('id')!r} missing {sorted(missing)}")
        if row["id"] in seen:
            raise ValueError(f"duplicate case id: {row['id']}")
        seen.add(row["id"])
        if not row["prompt"].strip() or not row["judge_focus"]:
            raise ValueError(f"case {row['id']} lacks behavioral content")
    return {"status": "PASS", "case_count": len(rows)}


def _index_outputs(path: Path) -> dict[tuple[str, int], dict]:
    rows = load_jsonl(path)
    out = {}
    for row in rows:
        for key in ("case_id", "trial", "output_text"):
            if key not in row:
                raise ValueError(f"{path}: output row missing {key}")
        k = (str(row["case_id"]), int(row["trial"]))
        if k in out:
            raise ValueError(f"{path}: duplicate output key {k}")
        if not str(row["output_text"]).strip():
            raise ValueError(f"{path}: empty output for {k}")
        out[k] = row
    return out


def blind(baseline_path: Path, candidate_path: Path, seed: str, public_path: Path, private_path: Path) -> dict:
    baseline = _index_outputs(baseline_path)
    candidate = _index_outputs(candidate_path)
    if set(baseline) != set(candidate):
        only_b = sorted(set(baseline) - set(candidate))
        only_c = sorted(set(candidate) - set(baseline))
        raise ValueError(f"coverage mismatch; baseline_only={only_b}, candidate_only={only_c}")
    rng = random.Random(seed)
    public_items, mappings = [], []
    for case_id, trial in sorted(baseline):
        pair_id = hashlib.sha256(f"{seed}|{case_id}|{trial}".encode()).hexdigest()[:20]
        swap = bool(rng.getrandbits(1))
        if swap:
            a, b = candidate[(case_id, trial)], baseline[(case_id, trial)]
            mapping = {"A": "candidate", "B": "baseline"}
        else:
            a, b = baseline[(case_id, trial)], candidate[(case_id, trial)]
            mapping = {"A": "baseline", "B": "candidate"}
        public_items.append({
            "pair_id": pair_id,
            "case_id": case_id,
            "trial": trial,
            "output_A": a["output_text"],
            "output_B": b["output_text"],
        })
        mappings.append({"pair_id": pair_id, "case_id": case_id, "trial": trial, "mapping": mapping})
    public = {"schema_version": 1, "blinding": "identity-hidden", "items": public_items}
    private = {"schema_version": 1, "seed": seed, "mappings": mappings}
    write_json(public_path, public)
    write_json(private_path, private)
    return {"status": "PASS", "pairs": len(public_items)}


def _validate_score_map(scores: dict, label: str) -> None:
    if set(scores) != set(DIMENSIONS):
        missing = sorted(set(DIMENSIONS) - set(scores))
        extra = sorted(set(scores) - set(DIMENSIONS))
        raise ValueError(f"{label}: dimensions mismatch missing={missing} extra={extra}")
    for d, value in scores.items():
        if not isinstance(value, (int, float)) or not (0 <= value <= 10):
            raise ValueError(f"{label}: {d} score must be 0..10")


def aggregate(public_path: Path, private_path: Path, judgments_path: Path, output_path: Path) -> dict:
    public = json.loads(public_path.read_text(encoding="utf-8"))
    private = json.loads(private_path.read_text(encoding="utf-8"))
    judgments = load_jsonl(judgments_path)
    public_ids = {x["pair_id"] for x in public["items"]}
    mappings = {x["pair_id"]: x for x in private["mappings"]}
    if public_ids != set(mappings):
        raise ValueError("public/private pair mismatch")

    seen_judge = set()
    by_pair_roles: dict[str, set[str]] = defaultdict(set)
    dim_values = {"baseline": defaultdict(list), "candidate": defaultdict(list)}
    overall_values = {"baseline": [], "candidate": []}
    prefs = defaultdict(int)
    case_deltas: dict[str, list[float]] = defaultdict(list)

    for row in judgments:
        pair_id = row.get("pair_id")
        if pair_id not in public_ids:
            raise ValueError(f"unknown pair_id {pair_id}")
        role = row.get("evaluator_role")
        evaluator_id = row.get("evaluator_id")
        if role not in ROLES:
            raise ValueError(f"unsupported evaluator role {role}")
        key = (pair_id, evaluator_id)
        if key in seen_judge:
            raise ValueError(f"duplicate evaluator judgment {key}")
        seen_judge.add(key)
        by_pair_roles[pair_id].add(role)
        pref = row.get("preference")
        if pref not in {"A", "B", "tie"}:
            raise ValueError(f"invalid preference {pref}")
        scores = row.get("scores", {})
        if set(scores) != {"A", "B"}:
            raise ValueError("scores must contain exactly A and B")
        _validate_score_map(scores["A"], f"{pair_id}/A")
        _validate_score_map(scores["B"], f"{pair_id}/B")
        mapping = mappings[pair_id]["mapping"]
        label_for = {system: label for label, system in mapping.items()}
        for system in ("baseline", "candidate"):
            label = label_for[system]
            vals = scores[label]
            for d, v in vals.items():
                dim_values[system][d].append(float(v))
            overall_values[system].append(statistics.fmean(vals.values()))
        if pref == "tie":
            prefs["tie"] += 1
        else:
            prefs[mapping[pref]] += 1
        b_mean = statistics.fmean(scores[label_for["baseline"]].values())
        c_mean = statistics.fmean(scores[label_for["candidate"]].values())
        case_deltas[mappings[pair_id]["case_id"]].append(c_mean - b_mean)

    for pair_id in public_ids:
        missing_roles = ROLES - by_pair_roles[pair_id]
        if missing_roles:
            raise ValueError(f"pair {pair_id} missing evaluator roles {sorted(missing_roles)}")

    dim_summary = {}
    for d in DIMENSIONS:
        b = statistics.fmean(dim_values["baseline"][d])
        c = statistics.fmean(dim_values["candidate"][d])
        dim_summary[d] = {"baseline": b, "candidate": c, "delta": c - b}
    b_overall = statistics.fmean(overall_values["baseline"])
    c_overall = statistics.fmean(overall_values["candidate"])

    public_by_pair = {x["pair_id"]: x for x in public["items"]}
    words = {"baseline": [], "candidate": []}
    for pair_id, meta in mappings.items():
        item = public_by_pair[pair_id]
        for label, system in meta["mapping"].items():
            words[system].append(len(item[f"output_{label}"].split()))
    b_words = statistics.fmean(words["baseline"])
    c_words = statistics.fmean(words["candidate"])

    result = {
        "schema_version": 1,
        "status": "ANALYSIS_ONLY_NOT_PROMOTION_DECISION",
        "pair_count": len(public_ids),
        "judgment_count": len(judgments),
        "preferences": {k: prefs.get(k, 0) for k in ("baseline", "candidate", "tie")},
        "overall": {"baseline": b_overall, "candidate": c_overall, "delta": c_overall - b_overall},
        "dimensions": dim_summary,
        "case_deltas": {k: statistics.fmean(v) for k, v in sorted(case_deltas.items())},
        "output_words": {
            "baseline_mean": b_words,
            "candidate_mean": c_words,
            "ratio": c_words / b_words if b_words else None,
        },
        "note": "This harness aggregates locked judgments; it does not establish evaluator independence, statistical significance, or promotion eligibility by itself.",
    }
    write_json(output_path, result)
    return result


def self_test() -> dict:
    with tempfile.TemporaryDirectory(prefix="novum-evolution-selftest-") as td:
        root = Path(td)
        b = root / "baseline.jsonl"
        c = root / "candidate.jsonl"
        b.write_text(json.dumps({"case_id":"x","trial":1,"output_text":"ordinary control answer"})+"\n", encoding="utf-8")
        c.write_text(json.dumps({"case_id":"x","trial":1,"output_text":"deeper candidate mechanism"})+"\n", encoding="utf-8")
        pub, priv = root / "public.json", root / "private.json"
        blind(b, c, "seed", pub, priv)
        p = json.loads(pub.read_text(encoding="utf-8"))
        m = json.loads(priv.read_text(encoding="utf-8"))["mappings"][0]
        assert "baseline" not in json.dumps(p).lower()
        pair = p["items"][0]["pair_id"]
        candidate_label = next(k for k,v in m["mapping"].items() if v == "candidate")
        rows=[]
        for i, role in enumerate(sorted(ROLES),1):
            scores={}
            for label in ("A","B"):
                value = 8.0 if label == candidate_label else 6.0
                scores[label]={d:value for d in DIMENSIONS}
            rows.append({"pair_id":pair,"evaluator_id":f"e{i}","evaluator_role":role,"scores":scores,"preference":candidate_label,"critical_flags":[],"rationale":"fixture"})
        jp=root/"judgments.jsonl"
        jp.write_text("".join(json.dumps(r)+"\n" for r in rows),encoding="utf-8")
        result=aggregate(pub,priv,jp,root/"analysis.json")
        assert result["overall"]["delta"] > 0
        assert result["preferences"]["candidate"] == 3
        return {"status":"PASS","checks":["identity blinding","coverage binding","required roles","dimension validation","unblinding aggregation"]}


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("self-test")
    v = sub.add_parser("validate-cases"); v.add_argument("path")
    b = sub.add_parser("blind")
    b.add_argument("baseline"); b.add_argument("candidate"); b.add_argument("seed"); b.add_argument("public"); b.add_argument("private")
    a = sub.add_parser("aggregate")
    a.add_argument("public"); a.add_argument("private"); a.add_argument("judgments"); a.add_argument("output")
    args = parser.parse_args()
    if args.cmd == "self-test": result = self_test()
    elif args.cmd == "validate-cases": result = validate_cases(Path(args.path))
    elif args.cmd == "blind": result = blind(Path(args.baseline),Path(args.candidate),args.seed,Path(args.public),Path(args.private))
    else: result = aggregate(Path(args.public),Path(args.private),Path(args.judgments),Path(args.output))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
