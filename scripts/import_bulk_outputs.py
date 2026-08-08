#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, re

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "bulk md all answer"
CASES = ROOT / "benchmarks/visible-regression/cases.jsonl"
OUT = ROOT / "results/EXP-001/visible/raw"
DEV_OUT = ROOT / "results/EXP-001/visible/protocol-deviations/near-equivalent-prompts"
LEDGER = ROOT / "results/EXP-001/visible/RUN_LEDGER.md"
REPORT = ROOT / "results/EXP-001/visible/BULK_IMPORT_REPORT.md"
DEV_REPORT = ROOT / "results/EXP-001/visible/PROTOCOL_DEVIATION_REPORT.md"

cases = [json.loads(x) for x in CASES.read_text(encoding="utf-8").splitlines() if x.strip()]
prompt_to_case = {x["prompt"].strip(): x["id"] for x in cases}
order = [x["id"] for x in cases]

# Near-equivalent prompts that were accidentally supplied for the second bulk batch.
# They are preserved as evidence but MUST NOT satisfy canonical visible-run slots.
alias_to_case = {
    "A small school wants a breakthrough AI system to reduce teacher administrative reporting workload by 80%, but most reports duplicate information teachers already entered elsewhere. Find the best intervention.": "vr-05-simplify-not-invent",
    "Invent a passive household device that produces continuous net energy indefinitely, with no fuel and no energy input from the environment, while delivering more energy than it consumes.": "vr-06-impossible-premise",
    "Create a revolutionary hiring platform for small restaurants using AI agents, blockchain, and a marketplace. The main operational bottleneck is that hired workers frequently do not show up for scheduled shifts.": "vr-07-ai-wrapper-trap",
    "Improve scheduling for a rural clinic with intermittent power, no reliable cloud access, one low-end PC, and no budget for additional staff. Invent a new mechanism only if it clearly beats a simpler workflow.": "vr-08-offline-clinic",
}

text = SRC.read_text(encoding="utf-8")
headers = list(re.finditer(r"(?m)^(baseline|candidate)-SKILL\.md\s*$", text))
records = []


def short_id(case_id):
    return re.match(r"vr-\d{2}", case_id).group(0)


def path_for(case_id, trial, arm):
    return OUT / short_id(case_id) / f"trial-{trial}-{arm}.md"


def dev_path_for(case_id, trial, arm):
    return DEV_OUT / short_id(case_id) / f"trial-{trial}-{arm}.md"


def assign_record(target_fn, case_id, arm, answer, digest, segment_no, status_prefix):
    for trial in range(1, 4):
        p = target_fn(case_id, trial, arm)
        if p.exists() and p.read_text(encoding="utf-8") == answer:
            records.append((segment_no, case_id, arm, trial, f"{status_prefix}_matched_existing", digest))
            return
    free = [t for t in range(1, 4) if not target_fn(case_id, t, arm).exists()]
    if not free:
        records.append((segment_no, case_id, arm, None, f"{status_prefix}_extra_unassigned", digest))
        return
    trial = free[0]
    p = target_fn(case_id, trial, arm)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(answer, encoding="utf-8")
    records.append((segment_no, case_id, arm, trial, f"{status_prefix}_imported", digest))


for i, h in enumerate(headers):
    arm = h.group(1)
    end = headers[i + 1].start() if i + 1 < len(headers) else len(text)
    chunk = text[h.end():end]
    tm = re.search(r"(?m)^TASK:\s*\n([^\n]+?)\s*$", chunk)
    rm = re.search(r"(?m)^Réfléchi pendant[^\n]*\n", chunk)
    if not tm or not rm:
        raise SystemExit(f"cannot parse segment {i+1}")
    prompt = tm.group(1).strip()
    answer = chunk[rm.end():].lstrip("\n").rstrip() + "\n"
    digest = hashlib.sha256(answer.encode()).hexdigest()

    if prompt in prompt_to_case:
        assign_record(path_for, prompt_to_case[prompt], arm, answer, digest, i + 1, "canonical")
    elif prompt in alias_to_case:
        assign_record(dev_path_for, alias_to_case[prompt], arm, answer, digest, i + 1, "deviation")
    else:
        raise SystemExit(f"unknown task in segment {i+1}: {prompt}")


def has(case_id, trial, arm):
    return path_for(case_id, trial, arm).exists()


lines = [
    "# EXP-001 Visible Run Ledger", "",
    "Authoritative progress record for visible execution. Only exact frozen prompts satisfy canonical slots. Raw outputs remain unjudged until blinding.", "",
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
        if next_run:
            break
    if next_run:
        break

source_sha = hashlib.sha256(SRC.read_bytes()).hexdigest()
canonical_imported = sum(r[4] == "canonical_imported" for r in records)
canonical_matched = sum(r[4] == "canonical_matched_existing" for r in records)
deviation_imported = sum(r[4] == "deviation_imported" for r in records)
deviation_matched = sum(r[4] == "deviation_matched_existing" for r in records)
extra = sum(r[4].endswith("extra_unassigned") for r in records)

lines += [
    "", "## Latest bulk import", "",
    f"- source SHA-256: `{source_sha}`",
    f"- parsed runs: {len(records)}",
    f"- canonical newly imported: {canonical_imported}",
    f"- canonical matched existing: {canonical_matched}",
    f"- near-equivalent prompt deviations preserved separately: {deviation_imported + deviation_matched}",
    f"- extra/unassigned: {extra}",
    "- near-equivalent prompt deviations do not satisfy frozen canonical slots.",
    "- parallel-run ordering is unavailable; trial assignment within each arm follows source appearance.",
    "- no scoring or behavioral judgment was performed.",
    "", "## Current next run", "",
]
if next_run:
    lines += [f"`{next_run[0]} / trial {next_run[1]} / {next_run[2]}`", ""]
else:
    lines += ["All 48 canonical visible generations are recorded.", ""]
lines += ["## Scientific status", "", "Generation evidence only. Judging remains deferred until the canonical visible set is complete and blinded.", ""]
LEDGER.write_text("\n".join(lines), encoding="utf-8")

rep = [
    "# EXP-001 Bulk Import Report", "",
    f"Source SHA-256: `{source_sha}`", "",
    "| # | Case | Arm | Trial | Status | SHA-256 |",
    "|---:|---|---|---:|---|---|",
]
for n, case_id, arm, trial, status, digest in records:
    rep.append(f"| {n} | {case_id} | {arm} | {trial or '—'} | {status} | `{digest}` |")
rep += ["", "## Missing canonical slots", ""]
for case_id in order:
    for trial in range(1, 4):
        for arm in ("baseline", "candidate"):
            if not has(case_id, trial, arm):
                rep.append(f"- `{case_id} / trial {trial} / {arm}`")
REPORT.write_text("\n".join(rep) + "\n", encoding="utf-8")

dev = [
    "# EXP-001 Protocol Deviation Report", "",
    "The second bulk batch used near-equivalent reformulations rather than the exact frozen prompts for vr-05 through vr-08.",
    "These outputs are preserved for auxiliary analysis but are excluded from the canonical 48-run visible set.", "",
    f"Source SHA-256: `{source_sha}`", "",
    "| # | Case | Arm | Trial | Status | SHA-256 |",
    "|---:|---|---|---:|---|---|",
]
for n, case_id, arm, trial, status, digest in records:
    if status.startswith("deviation_"):
        dev.append(f"| {n} | {case_id} | {arm} | {trial or '—'} | {status} | `{digest}` |")
dev += ["", "## Canonical prompt rule", "", "Only exact prompt strings from `benchmarks/visible-regression/cases.jsonl` count toward canonical completion.", ""]
DEV_REPORT.write_text("\n".join(dev), encoding="utf-8")

print(
    f"parsed={len(records)} canonical_imported={canonical_imported} "
    f"deviations={deviation_imported + deviation_matched}"
)
