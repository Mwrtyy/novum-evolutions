#!/usr/bin/env python3
from pathlib import Path
import json, os, re, time, urllib.request, urllib.error

ROOT = Path(__file__).resolve().parents[1]
BLIND = ROOT / "results/EXP-001/visible/blind"
MANIFEST = BLIND / "JUDGE_MANIFEST.json"
OUT = ROOT / "results/EXP-001/visible/judgments"
MODEL = os.environ.get("JUDGE_MODEL", "openai/gpt-4.1")
TOKEN = os.environ.get("GITHUB_TOKEN")
API = "https://models.github.ai/inference/chat/completions"
DIMS = [
    "mechanism_novelty", "mechanistic_depth", "constraint_fit", "usefulness",
    "evidence_calibration", "falsifiability", "prior_art_awareness",
    "simpler_substitute_discipline", "clarity"
]

if not TOKEN:
    raise SystemExit("GITHUB_TOKEN is required")

OUT.mkdir(parents=True, exist_ok=True)
manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))


def parse_json(text):
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start, end = text.find("{"), text.rfind("}")
        if start >= 0 and end > start:
            return json.loads(text[start:end+1])
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
    obj["judge_provider"] = "github_models"
    obj["judge_model"] = MODEL
    obj["prompt_status"] = item["prompt_status"]
    return obj


def infer(prompt):
    payload = json.dumps({
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1,
    }).encode()
    req = urllib.request.Request(
        API,
        data=payload,
        method="POST",
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
            "Accept": "application/vnd.github+json",
            "User-Agent": "novum-evolutions-exp001-judge",
        },
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        body = json.loads(resp.read().decode())
    return body["choices"][0]["message"]["content"]


completed = 0
skipped = 0
failed = []
for index, item in enumerate(manifest, 1):
    out_path = OUT / f"{item['judge_id']}.json"
    if out_path.exists():
        try:
            validate(json.loads(out_path.read_text(encoding="utf-8")), item)
            skipped += 1
            print(f"[{index}/{len(manifest)}] skip {item['judge_id']}", flush=True)
            continue
        except Exception:
            pass

    prompt = (ROOT / item["prompt_path"]).read_text(encoding="utf-8")
    ok = False
    last_error = None
    for attempt in range(1, 7):
        try:
            raw = infer(prompt)
            obj = validate(parse_json(raw), item)
            out_path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            completed += 1
            ok = True
            print(f"[{index}/{len(manifest)}] done {item['judge_id']} attempt={attempt}", flush=True)
            break
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, json.JSONDecodeError, ValueError, KeyError) as exc:
            last_error = repr(exc)
            delay = min(60, 2 ** attempt)
            print(f"[{index}/{len(manifest)}] retry {item['judge_id']} attempt={attempt} error={last_error}", flush=True)
            time.sleep(delay)
    if not ok:
        failed.append({"judge_id": item["judge_id"], "error": last_error})

status = {
    "model": MODEL,
    "provider": "github_models",
    "expected": len(manifest),
    "completed_this_run": completed,
    "already_present": skipped,
    "total_present": len(list(OUT.glob("*.json"))) - 1 if (OUT / "AUTO_JUDGE_STATUS.json").exists() else len(list(OUT.glob("*.json"))),
    "failed": failed,
}
(OUT / "AUTO_JUDGE_STATUS.json").write_text(json.dumps(status, indent=2) + "\n", encoding="utf-8")
print(json.dumps(status), flush=True)
if failed:
    raise SystemExit(f"{len(failed)} judgments failed")
