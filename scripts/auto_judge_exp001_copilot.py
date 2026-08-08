#!/usr/bin/env python3
from pathlib import Path
import json, os, re, subprocess, time

ROOT = Path(__file__).resolve().parents[1]
BLIND = ROOT / "results/EXP-001/visible/blind"
MANIFEST = BLIND / "JUDGE_MANIFEST.json"
OUT = ROOT / "results/EXP-001/visible/judgments-copilot"
MODEL = os.environ.get("JUDGE_MODEL", "auto")
MAX_JUDGMENTS = int(os.environ.get("MAX_JUDGMENTS", "0"))  # 0 = all missing
MAX_AI_CREDITS = int(os.environ.get("MAX_AI_CREDITS_PER_JUDGE", "40"))
DIMS = [
    "mechanism_novelty", "mechanistic_depth", "constraint_fit", "usefulness",
    "evidence_calibration", "falsifiability", "prior_art_awareness",
    "simpler_substitute_discipline", "clarity"
]

OUT.mkdir(parents=True, exist_ok=True)
manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))


def parse_json(text: str):
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        a, b = text.find("{"), text.rfind("}")
        if a >= 0 and b > a:
            return json.loads(text[a:b+1])
        raise


def validate(obj, item):
    if obj.get("pair_id") != item["pair_id"]:
        raise ValueError("pair_id mismatch")
    if obj.get("evaluator_id") != item["judge_id"]:
        raise ValueError("evaluator_id mismatch")
    if obj.get("evaluator_role") != item["role"]:
        raise ValueError("evaluator_role mismatch")
    if obj.get("preference") not in ("A", "B", "tie"):
        raise ValueError("invalid preference")
    scores = obj.get("scores", {})
    for arm in ("A", "B"):
        if arm not in scores:
            raise ValueError(f"missing scores.{arm}")
        for dim in DIMS:
            if dim not in scores[arm]:
                raise ValueError(f"missing {arm}.{dim}")
            value = float(scores[arm][dim])
            if not 0 <= value <= 10:
                raise ValueError(f"score out of range {arm}.{dim}")
            scores[arm][dim] = value
    if not isinstance(obj.get("critical_flags", []), list):
        raise ValueError("critical_flags must be a list")
    if not isinstance(obj.get("rationale", ""), str):
        raise ValueError("rationale must be a string")
    obj["independence"] = "separate_context_same_model"
    obj["judge_provider"] = "github_copilot_cli"
    obj["judge_model_request"] = MODEL
    obj["prompt_status"] = item["prompt_status"]
    obj["max_ai_credits_per_judge"] = MAX_AI_CREDITS
    return obj


def run_copilot(prompt: str, judge_id: str):
    home = ROOT / ".copilot-runs" / judge_id
    home.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env["COPILOT_HOME"] = str(home)
    cmd = [
        "copilot",
        "-p", prompt,
        "-s",
        f"--max-ai-credits={MAX_AI_CREDITS}",
        "--no-ask-user",
        "--no-custom-instructions",
        "--no-remote",
        "--no-remote-export",
        "--stream=off",
    ]
    # Copilot Free only supports automatic model selection. Omitting --model
    # invokes that path. Paid plans may pin a concrete supported model.
    if MODEL and MODEL.lower() != "auto":
        cmd.insert(4, f"--model={MODEL}")
    proc = subprocess.run(
        cmd,
        cwd=ROOT,
        env=env,
        text=True,
        capture_output=True,
        timeout=300,
    )
    if proc.returncode != 0:
        err = (proc.stderr or proc.stdout or "Copilot CLI failed").strip()
        raise RuntimeError(err[-4000:])
    return proc.stdout


already = 0
completed = 0
failed = []
attempted = 0

for index, item in enumerate(manifest, 1):
    out_path = OUT / f"{item['judge_id']}.json"
    if out_path.exists():
        try:
            validate(json.loads(out_path.read_text(encoding="utf-8")), item)
            already += 1
            print(f"[{index}/{len(manifest)}] skip {item['judge_id']}", flush=True)
            continue
        except Exception:
            out_path.unlink(missing_ok=True)

    if MAX_JUDGMENTS and attempted >= MAX_JUDGMENTS:
        break
    attempted += 1
    prompt = (ROOT / item["prompt_path"]).read_text(encoding="utf-8")
    last_error = None
    success = False
    for attempt in range(1, 3):
        try:
            raw = run_copilot(prompt, item["judge_id"])
            obj = validate(parse_json(raw), item)
            out_path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            completed += 1
            success = True
            print(f"[{index}/{len(manifest)}] done {item['judge_id']} attempt={attempt}", flush=True)
            break
        except Exception as exc:
            last_error = str(exc)
            print(f"[{index}/{len(manifest)}] failure {item['judge_id']} attempt={attempt}: {last_error[-500:]}", flush=True)
            if "Access denied by policy settings" in last_error:
                break
            if attempt < 2:
                time.sleep(10)
    if not success:
        failed.append({"judge_id": item["judge_id"], "error": last_error})
        if last_error and "Access denied by policy settings" in last_error:
            break

result_files = [p for p in OUT.glob("*.json") if p.name != "AUTO_JUDGE_STATUS.json"]
status = {
    "provider": "github_copilot_cli",
    "model_request": MODEL,
    "max_ai_credits_per_judge": MAX_AI_CREDITS,
    "expected": len(manifest),
    "already_present_at_start": already,
    "completed_this_run": completed,
    "attempted_this_run": attempted,
    "total_present": len(result_files),
    "remaining": len(manifest) - len(result_files),
    "complete": len(result_files) == len(manifest),
    "failed": failed,
}
(OUT / "AUTO_JUDGE_STATUS.json").write_text(json.dumps(status, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps(status), flush=True)
if failed:
    raise SystemExit(f"judging incomplete: {len(failed)} failed")
