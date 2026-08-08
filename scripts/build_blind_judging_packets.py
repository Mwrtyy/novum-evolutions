#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, re

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "results/EXP-001/visible/raw"
OUT = ROOT / "results/EXP-001/visible/blind"
PACKETS = OUT / "packets"
PROMPTS = OUT / "judge-prompts"
PRIVATE = OUT / "private"
CASES_FILE = ROOT / "benchmarks/visible-regression/cases.jsonl"

cases = [json.loads(x) for x in CASES_FILE.read_text(encoding="utf-8").splitlines() if x.strip()]
case_by_id = {x["id"]: x for x in cases}

# Adopted post-hoc prompt wording actually used for vr-05..vr-08.
adopted_prompts = {
    "vr-05-simplify-not-invent": "A small school wants a breakthrough AI system to reduce teacher administrative reporting workload by 80%, but most reports duplicate information teachers already entered elsewhere. Find the best intervention.",
    "vr-06-impossible-premise": "Invent a passive household device that produces continuous net energy indefinitely, with no fuel and no energy input from the environment, while delivering more energy than it consumes.",
    "vr-07-ai-wrapper-trap": "Create a revolutionary hiring platform for small restaurants using AI agents, blockchain, and a marketplace. The main operational bottleneck is that hired workers frequently do not show up for scheduled shifts.",
    "vr-08-offline-clinic": "Improve scheduling for a rural clinic with intermittent power, no reliable cloud access, one low-end PC, and no budget for additional staff. Invent a new mechanism only if it clearly beats a simpler workflow.",
}

roles = ["hostile_regression", "simplicity", "domain_or_generalist"]
dims = [
    "mechanism_novelty", "mechanistic_depth", "constraint_fit", "usefulness",
    "evidence_calibration", "falsifiability", "prior_art_awareness",
    "simpler_substitute_discipline", "clarity"
]


def short_id(case_id):
    return re.match(r"vr-\d{2}", case_id).group(0)


def raw_path(case_id, trial, arm):
    return RAW / short_id(case_id) / f"trial-{trial}-{arm}.md"


def orientation(pair_id):
    # Frozen, deterministic pseudo-random orientation; no result inspection involved.
    b = hashlib.sha256(("EXP-001-BLIND-V1|" + pair_id).encode()).digest()[0]
    return "baseline_A" if b % 2 == 0 else "candidate_A"


def role_focus(role):
    if role == "hostile_regression":
        return "Act as a hostile regression judge. Search aggressively for hidden regressions, fake novelty, unsupported claims, broken constraints, weak causal mechanisms, and failures of falsification. Do not reward verbosity."
    if role == "simplicity":
        return "Act as a simplicity judge. Prefer the smallest intervention that solves the real problem. Penalize unnecessary invention, technology stacking, needless complexity, and failure to recognize a stronger simple substitute."
    return "Act as a domain-or-generalist judge. Evaluate technical plausibility, mechanism quality, usefulness, constraint fit, evidence calibration, and whether the answer would actually help a competent practitioner."

PACKETS.mkdir(parents=True, exist_ok=True)
PROMPTS.mkdir(parents=True, exist_ok=True)
PRIVATE.mkdir(parents=True, exist_ok=True)

mapping = {}
manifest = []

for case in cases:
    case_id = case["id"]
    task = adopted_prompts.get(case_id, case["prompt"])
    prompt_status = "ADOPTED_NEAR_EQUIVALENT" if case_id in adopted_prompts else "FROZEN_EXACT"
    for trial in range(1, 4):
        pair_id = f"{short_id(case_id)}-t{trial}"
        bp = raw_path(case_id, trial, "baseline")
        cp = raw_path(case_id, trial, "candidate")
        if not bp.exists() or not cp.exists():
            raise SystemExit(f"missing raw pair {pair_id}")
        baseline = bp.read_text(encoding="utf-8").rstrip()
        candidate = cp.read_text(encoding="utf-8").rstrip()
        orient = orientation(pair_id)
        if orient == "baseline_A":
            A, B = baseline, candidate
            map_a, map_b = "baseline", "candidate"
        else:
            A, B = candidate, baseline
            map_a, map_b = "candidate", "baseline"

        mapping[pair_id] = {
            "A": map_a,
            "B": map_b,
            "case_id": case_id,
            "trial": trial,
            "prompt_status": prompt_status,
            "baseline_sha256": hashlib.sha256((baseline + "\n").encode()).hexdigest(),
            "candidate_sha256": hashlib.sha256((candidate + "\n").encode()).hexdigest(),
        }

        packet = f"""# Blind pair {pair_id}\n\n## Task\n\n{task}\n\n## Output A\n\n{A}\n\n## Output B\n\n{B}\n"""
        packet_path = PACKETS / f"{pair_id}.md"
        packet_path.write_text(packet, encoding="utf-8")

        for role in roles:
            judge_id = f"{pair_id}-{role}"
            score_template_a = ",\n      ".join(f'"{d}": 0.0' for d in dims)
            score_template_b = ",\n      ".join(f'"{d}": 0.0' for d in dims)
            judge_prompt = f"""# EXP-001 Blind Judge — {judge_id}\n\nYou are evaluating two anonymized answers to the same task. You must not infer or speculate about which system produced A or B. Judge only the text shown.\n\nEvaluator role: `{role}`\nIndependence level for this run: `separate_context_same_model`\n\n{role_focus(role)}\n\nScore BOTH A and B from 0 to 10 on every dimension:\n- mechanism_novelty\n- mechanistic_depth\n- constraint_fit\n- usefulness\n- evidence_calibration\n- falsifiability\n- prior_art_awareness\n- simpler_substitute_discipline\n- clarity\n\nChoose preference `A`, `B`, or `tie`. Use critical_flags for concrete serious issues. Keep rationale evidence-based and concise.\n\nReturn ONLY one valid JSON object with this exact structure and every score populated:\n\n```json\n{{\n  "pair_id": "{pair_id}",\n  "evaluator_id": "{judge_id}",\n  "evaluator_role": "{role}",\n  "independence": "separate_context_same_model",\n  "scores": {{\n    "A": {{\n      {score_template_a}\n    }},\n    "B": {{\n      {score_template_b}\n    }}\n  }},\n  "preference": "A",\n  "critical_flags": [],\n  "rationale": ""\n}}\n```\n\n---\n\n{packet}\n"""
            prompt_path = PROMPTS / f"{judge_id}.md"
            prompt_path.write_text(judge_prompt, encoding="utf-8")
            manifest.append({
                "judge_id": judge_id,
                "pair_id": pair_id,
                "role": role,
                "prompt_path": str(prompt_path.relative_to(ROOT)),
                "pair_path": str(packet_path.relative_to(ROOT)),
                "prompt_status": prompt_status,
            })

(PRIVATE / "AB_MAPPING.json").write_text(json.dumps(mapping, indent=2) + "\n", encoding="utf-8")
(OUT / "JUDGE_MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

readme = """# EXP-001 blind judging\n\nGenerated after visible generation completion.\n\n- 24 blinded A/B pairs\n- 3 evaluator roles per pair\n- 72 role-specific judge prompts\n- A/B orientation is frozen by SHA-256 of `EXP-001-BLIND-V1|<pair_id>` before judging.\n- Judges must not receive `private/AB_MAPPING.json`.\n- `vr-01`–`vr-04` use frozen exact task wording.\n- `vr-05`–`vr-08` use the adopted near-equivalent task wording actually shown to both generation arms.\n- Judge independence for ChatGPT Web fresh contexts must be recorded as `separate_context_same_model`, not external replication.\n\nDo not reveal the private A/B mapping until all 72 judgments are locked.\n"""
(OUT / "README.md").write_text(readme, encoding="utf-8")

print(f"pairs={len(mapping)} judge_prompts={len(manifest)}")
