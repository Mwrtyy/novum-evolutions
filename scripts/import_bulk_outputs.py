#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, re

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "bulk md all answer"
CASES = ROOT / "benchmarks/visible-regression/cases.jsonl"
OUT = ROOT / "results/EXP-001/visible/raw"
LEDGER = ROOT / "results/EXP-001/visible/RUN_LEDGER.md"
REPORT = ROOT / "results/EXP-001/visible/BULK_IMPORT_REPORT.md"

cases = [json.loads(x) for x in CASES.read_text(encoding="utf-8").splitlines() if x.strip()]
prompt_to_case = {x["prompt"].strip(): x["id"] for x in cases}
order = [x["id"] for x in cases]
text = SRC.read_text(encoding="utf-8")
headers = list(re.finditer(r"(?m)^(baseline|candidate)-SKILL\.md\s*$", text))
records = []


def path_for(case_id, trial, arm):
    short = re.match(r"vr-\d{2}", case_id).group(0)
    return OUT / short / f"trial-{trial}-{arm}.md"

for i, h in enumerate(headers):
    arm = h.group(1)
    end = headers[i + 1].start() if i + 1 < len(headers) else len(text)
    chunk = text[h.end():end]
    tm = re.search(r"(?m)^TASK:\s*\n([^\n]+?)\s*$", chunk)
    rm = re.search(r"(?m)^Réfléchi pendant[^\n]*\n", chunk)
    if not tm or not rm:
        raise SystemExit(f"cannot parse segment {i+1}")
    prompt = tm.group(1).strip()
    case_id = prompt_to_case.get(prompt)
    if not case_id:
        raise SystemExit(f"unknown task in segment {i+1}: {prompt}")
    answer = chunk[rm.end():].lstrip("\n").rstrip() + "\n"
    digest = hashlib.sha256(answer.encode()).hexdigest()

    matched = None
    for trial in range(1, 4):
        p = path_for(case_id, trial, arm)
        if p.exists() and p.read_text(encoding="utf-8") == answer:
            matched = trial
            break
    if matched is not None:
        records.append((i+1, case_id, arm, matched, "matched_existing", digest))
        continue

    free = [t for t in range(1, 4) if not path_for(case_id, t, arm).exists()]
    if not free:
        records.append((i+1, case_id, arm, None, "extra_unassigned", digest))
        continue
    trial = free[0]
    p = path_for(case_id, trial, arm)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(answer, encoding="utf-8")
    records.append((i+1, case_id, arm, trial, "imported", digest))


def has(case_id, trial, arm):
    return path_for(case_id, trial, arm).exists()

lines = [
    "# EXP-001 Visible Run Ledger", "",
    "Authoritative progress record for visible execution. Raw outputs are preserved under `raw/` and remain unjudged until blinding.", "",
    "## Progress", "",
    "| Case | Trial | Baseline | Candidate | Pair status |",
    "|---|---:|---|---|---|",
]
for case_id in order:
    for trial in range(1, 4):
        b, c = has(case_id, trial, "baseline"), has(case_id, trial, "candidate")
        pair = "COMPLETE" if b and c else "PARTIAL" if b or c else "PENDING"
        lines.append(f"| {case_id} | {trial} | {'RECORDED' if b else 'PENDING'} | {'RECORDED' if c else 'PENDING'} | {pair} |")

next_run = None
for case_id in order:
    for trial in range(1, 4):
        arms = ("baseline", "candidate") if trial % 2 else ("candidate", "baseline")
        for arm in arms:
            if not has(case_id, trial, arm):
                next_run = (case_id, trial, arm)
                break
        if next_run: break
    if next_run: break

source_sha = hashlib.sha256(SRC.read_bytes()).hexdigest()
lines += ["", "## Latest bulk import", "", f"- source SHA-256: `{source_sha}`", f"- parsed runs: {len(records)}", f"- newly imported: {sum(r[4]=='imported' for r in records)}", f"- matched existing: {sum(r[4]=='matched_existing' for r in records)}", f"- extra/unassigned: {sum(r[4]=='extra_unassigned' for r in records)}", "- parallel-run ordering is recorded as unavailable; trial assignment for unmatched outputs follows source appearance within each arm.", "- no scoring or behavioral judgment was performed.", "", "## Current next run", ""]
if next_run:
    lines += [f"`{next_run[0]} / trial {next_run[1]} / {next_run[2]}`", ""]
else:
    lines += ["All 48 visible generations are recorded.", ""]
lines += ["## Scientific status", "", "Generation evidence only. Judging remains deferred until the visible set is complete and blinded.", ""]
LEDGER.write_text("\n".join(lines), encoding="utf-8")

rep = ["# EXP-001 Bulk Import Report", "", f"Source SHA-256: `{source_sha}`", "", "| # | Case | Arm | Trial | Status | SHA-256 |", "|---:|---|---|---:|---|---|"]
for n, case_id, arm, trial, status, digest in records:
    rep.append(f"| {n} | {case_id} | {arm} | {trial or '—'} | {status} | `{digest}` |")
rep += ["", "## Missing slots", ""]
for case_id in order:
    for trial in range(1, 4):
        for arm in ("baseline", "candidate"):
            if not has(case_id, trial, arm):
                rep.append(f"- `{case_id} / trial {trial} / {arm}`")
REPORT.write_text("\n".join(rep) + "\n", encoding="utf-8")
print(f"parsed={len(records)} imported={sum(r[4]=='imported' for r in records)}")
