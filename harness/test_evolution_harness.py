#!/usr/bin/env python3
from pathlib import Path
import importlib.util

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("evolution_harness", HERE / "evolution_harness.py")
mod = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(mod)


def main() -> None:
    cases = HERE.parent / "benchmarks/visible-regression/cases.jsonl"
    result = mod.validate_cases(cases)
    assert result["case_count"] >= 6
    st = mod.self_test()
    assert st["status"] == "PASS"
    print("PASS — visible case contract and blind A/B harness")


if __name__ == "__main__":
    main()
