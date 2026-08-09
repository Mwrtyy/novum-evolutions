#!/usr/bin/env python3
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("exp001_judging", ROOT / "scripts/exp001_judging.py")
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def valid_record(item):
    return {
        "pair_id": item["pair_id"],
        "evaluator_id": f"{item['role']}-test",
        "evaluator_role": item["role"],
        "independence": "separate_context_same_model",
        "scores": {
            arm: {dim: 5.0 for dim in MOD.DIMS}
            for arm in ("A", "B")
        },
        "preference": "tie",
        "critical_flags": [],
        "rationale": "Both outputs are behaviorally equivalent on the frozen rubric.",
    }


class Exp001JudgingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = MOD.load_manifest()

    def test_visible_integrity(self):
        audit = MOD.audit_visible(write_manifest=False)
        self.assertEqual(audit["official_output_count"], 48)
        self.assertEqual(audit["pair_count"], 24)
        self.assertEqual(audit["judge_assignment_count"], 72)
        self.assertEqual(audit["adopted_preserved_copy_checks"], 24)

    def test_complete_jsonl_validates(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "judgments.jsonl"
            path.write_text(
                "\n".join(json.dumps(valid_record(item)) for item in self.manifest) + "\n",
                encoding="utf-8",
            )
            records = MOD.validate_judgments(path)
            self.assertEqual(len(records), 72)

    def test_missing_assignment_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "judgments.jsonl"
            path.write_text(
                "\n".join(json.dumps(valid_record(item)) for item in self.manifest[:-1]) + "\n",
                encoding="utf-8",
            )
            with self.assertRaises(MOD.ValidationError):
                MOD.validate_judgments(path)

    def test_duplicate_assignment_fails(self):
        records = [valid_record(item) for item in self.manifest]
        records[-1] = copy.deepcopy(records[0])
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "judgments.jsonl"
            path.write_text("\n".join(json.dumps(x) for x in records) + "\n", encoding="utf-8")
            with self.assertRaises(MOD.ValidationError):
                MOD.validate_judgments(path)

    def test_invalid_score_fails(self):
        record = valid_record(self.manifest[0])
        record["scores"]["A"]["clarity"] = 10.1
        with self.assertRaises(MOD.ValidationError):
            MOD.validate_record(record, self.manifest[0])

    def test_missing_dimension_fails(self):
        record = valid_record(self.manifest[0])
        del record["scores"]["B"]["falsifiability"]
        with self.assertRaises(MOD.ValidationError):
            MOD.validate_record(record, self.manifest[0])

    def test_invalid_preference_fails(self):
        record = valid_record(self.manifest[0])
        record["preference"] = "candidate"
        with self.assertRaises(MOD.ValidationError):
            MOD.validate_record(record, self.manifest[0])

    def test_empty_evaluator_id_fails(self):
        record = valid_record(self.manifest[0])
        record["evaluator_id"] = ""
        with self.assertRaises(MOD.ValidationError):
            MOD.validate_record(record, self.manifest[0])


if __name__ == "__main__":
    unittest.main()
