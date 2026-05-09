#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

try:
    import yaml
except Exception:
    yaml = None


def now_iso():
    return datetime.now().astimezone().isoformat(timespec="seconds")


def load_vocab(path: Path):
    if not path.exists() or yaml is None:
        return None
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    statuses = data.get("statuses", []) if isinstance(data, dict) else []
    return {s.get("status_code"): s for s in statuses if isinstance(s, dict) and s.get("status_code")}


def load_status_json(args, root: Path):
    if args.from_status_json:
        return json.loads(Path(args.from_status_json).read_text(encoding="utf-8")), False
    if args.status:
        return {
            "overall_status": "AGENTOS_STATUS_UNKNOWN",
            "top_status_code": args.status,
            "severity": "UNKNOWN",
            "authority": "SYSTEM_BLOCKED",
            "is_ready": False,
            "is_blocked": True,
            "is_unknown": True,
            "sources": [],
            "warnings": ["STATUS_PREVIEW_NOT_LIVE"],
            "errors": []
        }, False
    proc = subprocess.run([sys.executable, str(root / "scripts/agentos-status.py"), "--json"], capture_output=True, text=True)
    if proc.returncode not in (0, 1):
        raise RuntimeError("aggregator failed")
    return json.loads(proc.stdout), True


def safe_step(steps):
    if isinstance(steps, list) and steps:
        return steps[0]
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--status")
    ap.add_argument("--from-status-json")
    ap.add_argument("--root", default=".")
    ap.add_argument("--ascii", action="store_true")
    ap.add_argument("--no-color", action="store_true")
    ap.add_argument("--validate-only", action="store_true")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    warnings = []
    errors = []

    try:
        status, live = load_status_json(args, root)
    except Exception:
        status = {
            "overall_status": "AGENTOS_STATUS_UNKNOWN",
            "top_status_code": "STATUS_SOURCE_DAMAGED",
            "severity": "UNKNOWN",
            "authority": "SYSTEM_BLOCKED",
            "is_ready": False,
            "is_blocked": True,
            "is_unknown": True,
            "sources": [],
            "warnings": [],
            "errors": ["aggregator source damaged"]
        }
        live = False

    vocab = load_vocab(root / "data/explanations/status-vocabulary.yml")
    top = status.get("top_status_code", "AGENTOS_STATUS_UNKNOWN")

    if not vocab:
        entry = None
        errors.append("MISSING_VOCABULARY")
    else:
        entry = vocab.get(top)
        if not entry:
            errors.append("MISSING_VOCABULARY_ENTRY")

    if entry:
        simple = entry.get("simple_ru", {})
        details = entry.get("details", {})
        next_steps = entry.get("next_safe_steps") or []
        blocked_actions = entry.get("blocked_actions") if isinstance(entry.get("blocked_actions"), list) else []
        rendering = entry.get("renderer_hints", {})
        icon = entry.get("icon", "❓")
        ascii_label = entry.get("ascii_label", "[UNKNOWN]")
        color = entry.get("color", "gray")
        source_cfg = entry.get("source", {})
        stale_after = ((entry.get("freshness") or {}).get("stale_after_seconds", 300))
    else:
        simple = {
            "title": "Статус неизвестен",
            "what_happened": "AgentOS не смог прочитать словарь статусов.",
            "why_it_matters": "Без словаря нельзя безопасно объяснить состояние системы."
        }
        details = {"technical_status": top, "technical_reason": "missing vocabulary entry"}
        next_steps = []
        blocked_actions = ["Не продолжай без проверки статуса."]
        rendering = {"preferred_panel": "danger", "show_in_dashboard": True, "show_blocked_actions": True, "show_source": True, "show_freshness": True}
        icon = "❓"
        ascii_label = "[UNKNOWN]"
        color = "gray"
        source_cfg = {}
        stale_after = 300

    sev = status.get("severity", "UNKNOWN")
    auth = status.get("authority", "SYSTEM_BLOCKED")
    if entry and (entry.get("severity") != sev or entry.get("authority") != auth):
        warnings.append("VOCABULARY_STATUS_MISMATCH")

    if sev in {"NEEDS_REVIEW", "BLOCKED", "UNKNOWN"} and not blocked_actions:
        errors.append("BLOCKED_ACTIONS_REQUIRED")
        blocked_actions = ["Продолжать без проверки нельзя."]

    if not next_steps:
        warnings.append("NEXT_SAFE_STEP_MISSING")

    src0 = (status.get("sources") or [{}])[0] if status.get("sources") else {}
    model = {
        "schema_version": "1.0",
        "generated_at": now_iso(),
        "live_status": bool(live),
        "repo_root": str(root),
        "overall_status": status.get("overall_status", "AGENTOS_STATUS_UNKNOWN"),
        "top_status_code": top,
        "severity": sev,
        "authority": auth,
        "icon": icon,
        "color": color,
        "ascii_label": ascii_label,
        "title": simple.get("title", "Статус неизвестен"),
        "summary": simple.get("what_happened", "Нет данных"),
        "why": simple.get("why_it_matters", "Нет данных"),
        "source": {
            "report": source_cfg.get("report") or src0.get("path", ""),
            "checker": source_cfg.get("checker", ""),
            "state": src0.get("state", "unknown"),
            "freshness": src0.get("freshness", "unknown")
        },
        "freshness": {
            "state": src0.get("freshness", "unknown"),
            "last_updated": "",
            "stale_after_seconds": stale_after
        },
        "next_safe_step": safe_step(next_steps),
        "next_safe_steps": next_steps,
        "blocked_actions": blocked_actions,
        "flags": {
            "is_ready": bool(status.get("is_ready", False)),
            "is_blocked": bool(status.get("is_blocked", False)),
            "is_unknown": bool(status.get("is_unknown", False)),
            "requires_human_gate": auth == "HUMAN_GATE_REQUIRED",
            "requires_owner_review": auth == "OWNER_REVIEW_REQUIRED",
            "has_blocked_actions": bool(blocked_actions),
            "has_safe_next_step": bool(next_steps)
        },
        "rendering": rendering,
        "warnings": warnings,
        "errors": errors,
        "details": details
    }

    if args.validate_only:
        print("PASS" if not errors else "FAIL")
        return 0 if not errors else 1

    if args.json:
        print(json.dumps(model, ensure_ascii=False, indent=2))
    else:
        lead = model["ascii_label"] if args.ascii else model["icon"]
        print(f"{lead} {model['title']}")
        print(model["summary"])
        print("")
        print(f"Status: {model['overall_status']}")
        print(f"Reason: {model['top_status_code']}")
        print(f"Source: {model['source']['report']}")

    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
