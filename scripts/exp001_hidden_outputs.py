#!/usr/bin/env python3
"""Validate hidden arm outputs, blind them without persisting the mapping, and reveal later."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys

ARMS = ("baseline", "candidate")
SKILL_SHA = {
    "baseline": "1d6dea7cdb5343aad114ad48fa9f010ea88bd8bf1ccb6c45059f88e1bfa4c4a6",
    "candidate": "ad61ff084f482d9e06b3398970be565bdd5d7d29c132b1a3dfd0c45bd88a4688",
}


class ValidationError(ValueError):
    pass


def canonical(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def sha_file(path):
    return sha(path.read_bytes())


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def expected(tasks):
    return {(case["id"], trial, arm) for case in tasks["cases"] for trial in range(1, 4) for arm in ARMS}


def validate(args):
    tasks = load(args.tasks)
    freeze = load(args.freeze)
    if sha_file(args.tasks) != freeze["holdout_tasks"]["sha256"]:
        raise ValidationError("holdout task bytes changed after freeze")
    cases = {x["id"]: x for x in tasks["cases"]}
    expected_runs = expected(tasks)
    seen = set()
    contexts = set()
    records = []
    prompt_hash_modes = Counter()
    allowed = {
        "case_id", "trial", "arm", "model_identity", "model_configuration",
        "skill_sha256", "prompt_sha256", "generation_context_id",
        "independence", "tool_access", "tool_call_count", "search_queries",
        "run_started_utc", "run_finished_utc", "output_text",
    }
    for path in sorted(args.runs.glob("*.json")):
        record = load(path)
        if set(record) != allowed:
            raise ValidationError(f"field mismatch in {path.name}: {set(record) ^ allowed}")
        key = (record["case_id"], record["trial"], record["arm"])
        if key not in expected_runs or key in seen:
            raise ValidationError(f"unexpected or duplicate run {key}")
        seen.add(key)
        if record["generation_context_id"] in contexts:
            raise ValidationError(f"reused generation context {record['generation_context_id']}")
        contexts.add(record["generation_context_id"])
        if record["independence"] != "fresh_context_same_model_per_run":
            raise ValidationError(f"wrong independence for {key}")
        if record["skill_sha256"] != SKILL_SHA[record["arm"]]:
            raise ValidationError(f"skill identity mismatch for {key}")
        prompt = cases[record["case_id"]]["prompt"]
        frozen_prompt_sha = sha(prompt.encode())
        materialized_lf_sha = sha((prompt + "\n").encode())
        if record["prompt_sha256"] == frozen_prompt_sha:
            prompt_hash_modes["exact_frozen_json_string"] += 1
        elif record["prompt_sha256"] == materialized_lf_sha:
            prompt_hash_modes["materialized_with_one_trailing_lf"] += 1
        else:
            raise ValidationError(f"prompt hash mismatch for {key}")
        if not isinstance(record["trial"], int) or record["trial"] not in (1, 2, 3):
            raise ValidationError(f"invalid trial for {key}")
        if not isinstance(record["output_text"], str) or len(record["output_text"].split()) < 100:
            raise ValidationError(f"empty or truncated output for {key}")
        if not isinstance(record["tool_call_count"], int) or record["tool_call_count"] < 0:
            raise ValidationError(f"invalid tool count for {key}")
        if not isinstance(record["search_queries"], list) or not all(isinstance(x, str) for x in record["search_queries"]):
            raise ValidationError(f"invalid search queries for {key}")
        records.append(record)
    if seen != expected_runs:
        raise ValidationError(f"missing runs: {sorted(expected_runs - seen)}")
    by_pair = {}
    for case_id, trial, _ in sorted(expected_runs):
        pair = [x for x in records if x["case_id"] == case_id and x["trial"] == trial]
        if len(pair) != 2:
            continue
        if len({x["model_identity"] for x in pair}) != 1 or len({x["model_configuration"] for x in pair}) != 1:
            raise ValidationError(f"model mismatch in {case_id}/t{trial}")
        if len({x["tool_access"] for x in pair}) != 1:
            raise ValidationError(f"tool-access mismatch in {case_id}/t{trial}")
        by_pair[f"{case_id}-t{trial}"] = True
    records.sort(key=lambda x: (x["case_id"], x["trial"], ARMS.index(x["arm"])))
    args.output_dir.mkdir(parents=True, exist_ok=True)
    manifest = {
        "schema_version": 1,
        "experiment_id": "EXP-001",
        "phase": "hidden_generation",
        "status": "42_OF_42_VALIDATED_NOT_BLINDED",
        "holdout_tasks_sha256": sha_file(args.tasks),
        "freeze_manifest_sha256": sha_file(args.freeze),
        "output_count": len(records),
        "pair_count": len(by_pair),
        "generation_context_count": len(contexts),
        "model_identities": sorted({x["model_identity"] for x in records}),
        "model_configurations": sorted({x["model_configuration"] for x in records}),
        "tool_access": sorted({x["tool_access"] for x in records}),
        "prompt_materialization": {
            "hash_modes": dict(prompt_hash_modes),
            "assessment": "The execution prompt files contained the exact frozen JSON prompt text plus one trailing LF. This byte-level materialization deviation is preserved and disclosed; no lexical prompt content changed.",
        },
        "outputs": [{
            "case_id": x["case_id"],
            "trial": x["trial"],
            "arm": x["arm"],
            "generation_context_id": x["generation_context_id"],
            "frozen_prompt_sha256": sha(cases[x["case_id"]]["prompt"].encode()),
            "prompt_sha256": x["prompt_sha256"],
            "skill_sha256": x["skill_sha256"],
            "output_sha256": sha(x["output_text"].encode()),
            "words": len(x["output_text"].split()),
            "tool_call_count": x["tool_call_count"],
        } for x in records],
    }
    for arm in ARMS:
        payload = b"".join(canonical(x) for x in records if x["arm"] == arm)
        (args.output_dir / f"RAW_{arm.upper()}.jsonl").write_bytes(payload)
        manifest[f"raw_{arm}_jsonl_sha256"] = sha(payload)
    path = args.output_dir / "OUTPUT_MANIFEST.json"
    path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({**{k: manifest[k] for k in ("status", "output_count", "pair_count", "generation_context_count")}, "manifest_sha256": sha_file(path)}, indent=2))


def load_validated(output_dir):
    records = []
    for arm in ARMS:
        records.extend(json.loads(line) for line in (output_dir / f"RAW_{arm.upper()}.jsonl").read_text(encoding="utf-8").splitlines() if line)
    return records


def orientation(salt, pair_id):
    return "candidate" if hashlib.sha256(f"{salt}|{pair_id}".encode()).digest()[0] & 1 == 0 else "baseline"


def blind(args):
    tasks = load(args.tasks)
    cases = {x["id"]: x for x in tasks["cases"]}
    records = load_validated(args.output_dir)
    by_key = {(x["case_id"], x["trial"], x["arm"]): x for x in records}
    args.public_dir.mkdir(parents=True, exist_ok=True)
    pair_ids = []
    metadata = []
    public_bundle = []
    for case in tasks["cases"]:
        for trial in range(1, 4):
            pair_id = f"{case['id']}-t{trial}"
            arm_a = orientation(args.salt, pair_id)
            arm_b = "baseline" if arm_a == "candidate" else "candidate"
            item = {
                "pair_id": pair_id,
                "case_id": case["id"],
                "trial": trial,
                "task": case["prompt"],
                "Output A": by_key[(case["id"], trial, arm_a)]["output_text"],
                "Output B": by_key[(case["id"], trial, arm_b)]["output_text"],
            }
            pair_ids.append(pair_id)
            metadata.append({"pair_id": pair_id, "case_id": case["id"], "trial": trial})
            public_bundle.append(item)
            text = f"# Blind pair {pair_id}\n\n## Task\n\n{item['task']}\n\n## Output A\n\n{item['Output A']}\n\n## Output B\n\n{item['Output B']}\n"
            (args.public_dir / f"{pair_id}.md").write_text(text, encoding="utf-8")
    (args.public_dir / "PUBLIC_BLIND_BUNDLE.json").write_text(json.dumps(public_bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (args.public_dir / "PAIR_IDS.json").write_text(json.dumps(pair_ids, indent=2) + "\n", encoding="utf-8")
    (args.public_dir / "PAIR_METADATA.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    manifest = {
        "schema_version": 1,
        "status": "21_PAIRS_BLINDED_MAPPING_NOT_PERSISTED",
        "pair_count": len(pair_ids),
        "public_bundle_sha256": sha_file(args.public_dir / "PUBLIC_BLIND_BUNDLE.json"),
        "pair_ids_sha256": sha_file(args.public_dir / "PAIR_IDS.json"),
        "pair_metadata_sha256": sha_file(args.public_dir / "PAIR_METADATA.json"),
        "orientation_method": "SHA-256(private_random_salt|pair_id), low bit; salt retained outside evaluator-accessible filesystem until judgment lock",
    }
    path = args.public_dir / "BLIND_MANIFEST.json"
    path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({**manifest, "blind_manifest_sha256": sha_file(path)}, indent=2))


def reveal(args):
    pair_ids = load(args.pair_ids)
    metadata = {x["pair_id"]: x for x in load(args.pair_metadata)}
    mapping = {}
    for pair_id in pair_ids:
        arm_a = orientation(args.salt, pair_id)
        mapping[pair_id] = {
            "A": arm_a,
            "B": "baseline" if arm_a == "candidate" else "candidate",
            **metadata[pair_id],
        }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(mapping, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    reveal = {
        "schema_version": 1,
        "status": "REVEALED_AFTER_JUDGMENT_LOCK",
        "salt": args.salt,
        "mapping_sha256": sha_file(args.output),
        "pair_count": len(mapping),
    }
    args.output.with_name("REVEAL_RECORD.json").write_text(json.dumps(reveal, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(reveal, indent=2))


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    v = sub.add_parser("validate")
    v.add_argument("--tasks", type=Path, required=True)
    v.add_argument("--freeze", type=Path, required=True)
    v.add_argument("--runs", type=Path, required=True)
    v.add_argument("--output-dir", type=Path, required=True)
    v.set_defaults(func=validate)
    b = sub.add_parser("blind")
    b.add_argument("--tasks", type=Path, required=True)
    b.add_argument("--output-dir", type=Path, required=True)
    b.add_argument("--public-dir", type=Path, required=True)
    b.add_argument("--salt", required=True)
    b.set_defaults(func=blind)
    r = sub.add_parser("reveal")
    r.add_argument("--pair-ids", type=Path, required=True)
    r.add_argument("--pair-metadata", type=Path, required=True)
    r.add_argument("--salt", required=True)
    r.add_argument("--output", type=Path, required=True)
    r.set_defaults(func=reveal)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    try:
        main()
    except ValidationError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2)
