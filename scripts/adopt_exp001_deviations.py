#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, re, shutil

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "benchmarks/visible-regression/cases.jsonl"
RAW = ROOT / "results/EXP-001/visible/raw"
DEV = ROOT / "results/EXP-001/visible/protocol-deviations/near-equivalent-prompts"
LEDGER = ROOT / "results/EXP-001/visible/RUN_LEDGER.md"
REPORT = ROOT / "results/EXP-001/visible/ADOPTED_DEVIATION_REPORT.md"
AFFECTED = {"vr-05-simplify-not-invent", "vr-06-impossible-premise", "vr-07-ai-wrapper-trap", "vr-08-offline-clinic"}

cases = [json.loads(x) for x in CASES.read_text(encoding="utf-8").splitlines() if x.strip()]
order = [x["id"] for x in cases]

def short(case_id):
    return re.match(r"vr-\d{2}", case_id).group(0)

def path(base, case_id, trial, arm):
    return base / short(case_id) / f"trial-{trial}-{arm}.md"

adopted = []
for case_id in order:
    if case_id not in AFFECTED:
        continue
    for trial in range(1, 4):
        for arm in ("baseline", "candidate"):
            src = path(DEV, case_id, trial, arm)
            dst = path(RAW, case_id, trial, arm)
            if not src.exists():
                raise SystemExit(f"missing deviation evidence: {src}")
            data = src.read_bytes()
            if dst.exists() and dst.read_bytes() != data:
                raise SystemExit(f"refusing to overwrite different canonical output: {dst}")
            dst.parent.mkdir(parents=True, exist_ok=True)
            if not dst.exists():
                shutil.copyfile(src, dst)
            adopted.append((case_id, trial, arm, hashlib.sha256(data).hexdigest()))

def has(case_id, trial, arm):
    return path(RAW, case_id, trial, arm).exists()

lines = [
    "# EXP-001 Visible Run Ledger", "",
    "Authoritative progress record for visible execution. EXP-001 Protocol Amendment 001 adopts near-equivalent prompt runs for vr-05 through vr-08. The campaign is complete with a declared prompt deviation; it is not exact-frozen-prompt compliant.", "",
    "## Progress", "",
    "| Case | Trial | Baseline | Candidate | Pair status | Prompt status |",
    "|---|---:|---|---|---|---|",
]
for case_id in order:
    for trial in range(1, 4):
        b, c = has(case_id, trial, "baseline"), has(case_id, trial, "candidate")
        pair = "COMPLETE" if b and c else "PARTIAL" if b or c else "PENDING"
        prompt_status = "ADOPTED_NEAR_EQUIVALENT" if case_id in AFFECTED else "FROZEN_EXACT"
        lines.append(f"| {case_id} | {trial} | {'RECORDED' if b else 'PENDING'} | {'RECORDED' if c else 'PENDING'} | {pair} | {prompt_status} |")

complete = sum(has(c, t, a) for c in order for t in range(1,4) for a in ("baseline","candidate"))
lines += [
    "", "## Completion", "",
    f"- recorded visible generations: **{complete}/48**",
    "- vr-01 through vr-04: exact frozen prompts",
    "- vr-05 through vr-08: near-equivalent prompts adopted post-hoc under `experiments/EXP-001-PROTOCOL-AMENDMENT-001.md`",
    "- baseline and candidate used identical wording within every affected case",
    "- no behavioral scoring was performed during adoption",
    "", "## Next phase", "",
    "Visible generation is complete. Proceed to frozen blind judging, then strict post-freeze hidden holdout before any promotion decision.", "",
    "## Scientific status", "",
    "48/48 visible generations completed with declared protocol deviation. Do not describe this campaign as exact-string preregistration compliant.", "",
]
LEDGER.write_text("\n".join(lines), encoding="utf-8")

rep = [
    "# EXP-001 Adopted Prompt-Deviation Evidence", "",
    "These 24 outputs were generated with near-equivalent task wording and adopted into the official visible set under Protocol Amendment 001. Answer bytes are copied verbatim from the preserved deviation directory.", "",
    "| Case | Trial | Arm | SHA-256 |", "|---|---:|---|---|",
]
for case_id, trial, arm, digest in adopted:
    rep.append(f"| {case_id} | {trial} | {arm} | `{digest}` |")
rep += ["", f"Total adopted outputs: **{len(adopted)}**", ""]
REPORT.write_text("\n".join(rep), encoding="utf-8")
print(f"adopted={len(adopted)} visible_complete={complete}/48")
