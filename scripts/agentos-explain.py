#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def now_iso():
    return datetime.now().astimezone().isoformat(timespec="seconds")


def load_vm(args, root: Path):
    if args.from_view_model_json:
        return json.loads(Path(args.from_view_model_json).read_text(encoding="utf-8"))
    cmd = [sys.executable, str(root / "scripts/agentos-view-model.py"), "--json"]
    if args.status:
        cmd += ["--status", args.status]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode not in (0, 1):
        raise RuntimeError("view-model failed")
    return json.loads(proc.stdout)


def bad_phrase(text: str):
    forbidden = ["Не волнуйтесь, всё безопасно.", "Можно просто продолжить.", "Это не страшно."]
    return any(p in text for p in forbidden)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("status_arg", nargs="?")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--details", action="store_true")
    ap.add_argument("--ascii", action="store_true")
    ap.add_argument("--no-color", action="store_true")
    ap.add_argument("--status")
    ap.add_argument("--from-view-model-json")
    ap.add_argument("--root", default=".")
    ap.add_argument("--validate-language", action="store_true")
    args = ap.parse_args()
    if args.status_arg and not args.status:
        args.status = args.status_arg

    root = Path(args.root).resolve()
    warnings = []
    errors = []

    try:
        vm = load_vm(args, root)
    except Exception:
        vm = {
            "live_status": False,
            "overall_status": "AGENTOS_STATUS_UNKNOWN",
            "top_status_code": "STATUS_SOURCE_DAMAGED",
            "severity": "UNKNOWN",
            "authority": "SYSTEM_BLOCKED",
            "title": "Статус неизвестен",
            "summary": "AgentOS не смог прочитать статус.",
            "why": "Продолжать без проверки нельзя.",
            "source": {"report": "", "checker": "", "freshness": "unknown"},
            "next_safe_step": None,
            "blocked_actions": ["Продолжать без проверки нельзя."],
            "details": {"technical_status": "STATUS_SOURCE_DAMAGED", "technical_reason": "view model unavailable"},
            "icon": "❓",
            "ascii_label": "[UNKNOWN]",
            "color": "gray",
            "flags": {"requires_human_gate": False, "requires_owner_review": False}
        }
        errors.append({"code": "VIEW_MODEL_MISSING", "message": "View model недоступен."})

    sev = vm.get("severity", "UNKNOWN")
    auth = vm.get("authority", "SYSTEM_BLOCKED")
    blocked = vm.get("blocked_actions") or []
    next_step = vm.get("next_safe_step")
    if not next_step:
        warnings.append({"code": "NEXT_SAFE_STEP_MISSING", "message": "Следующий безопасный шаг не найден."})

    if sev in {"BLOCKED", "UNKNOWN"} and not blocked:
        errors.append({"code": "BLOCKED_ACTIONS_REQUIRED", "message": "Для этого статуса нужны blocked_actions."})
        blocked = ["Продолжать без проверки нельзя."]

    if sev == "UNKNOWN":
        if "неизвест" not in vm.get("title", "").lower():
            errors.append({"code": "EXPLANATION_VIEW_MODEL_MISMATCH", "message": "UNKNOWN не должен звучать как OK."})

    text_bundle = "\n".join([vm.get("title", ""), vm.get("summary", ""), vm.get("why", "")])
    if bad_phrase(text_bundle):
        errors.append({"code": "UNSAFE_LANGUAGE", "message": "Найдена запрещённая успокаивающая фраза."})

    hr_required = auth == "HUMAN_GATE_REQUIRED" or vm.get("flags", {}).get("requires_human_gate", False)
    owner_required = auth == "OWNER_REVIEW_REQUIRED" or vm.get("flags", {}).get("requires_owner_review", False)

    out = {
        "schema_version": "1.0",
        "generated_at": now_iso(),
        "live_status": bool(vm.get("live_status", False)),
        "overall_status": vm.get("overall_status", "AGENTOS_STATUS_UNKNOWN"),
        "top_status_code": vm.get("top_status_code", "STATUS_SOURCE_DAMAGED"),
        "severity": sev,
        "authority": auth,
        "title": vm.get("title", "Статус неизвестен"),
        "what_happened": vm.get("summary", ""),
        "why_it_matters": vm.get("why", ""),
        "what_to_check": (vm.get("source") or {}).get("report", ""),
        "next_safe_step": next_step,
        "blocked_actions": blocked,
        "human_review": {
            "required": hr_required,
            "owner_required": owner_required,
            "reason": "Нужно подтверждение человека." if hr_required or owner_required else ""
        },
        "source": {
            "report": (vm.get("source") or {}).get("report", ""),
            "checker": (vm.get("source") or {}).get("checker", ""),
            "freshness": (vm.get("source") or {}).get("freshness", "unknown")
        },
        "display": {
            "icon": vm.get("icon", "❓"),
            "ascii_label": vm.get("ascii_label", "[UNKNOWN]"),
            "color": vm.get("color", "gray")
        },
        "details": vm.get("details", {}),
        "warnings": warnings,
        "errors": errors
    }

    if args.validate_language:
        print("PASS" if not errors else "FAIL")
        return 0 if not errors else 1

    if args.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        lead = out["display"]["ascii_label"] if args.ascii else out["display"]["icon"]
        print(f"{lead} {out['title']}\n")
        print("Что случилось:")
        print(out["what_happened"])
        print("\nПочему это важно:")
        print(out["why_it_matters"])
        print("\n📄 Проверь:")
        print(out["what_to_check"])
        print("\n🧪 Следующий безопасный шаг:")
        print(out["next_safe_step"]["command"] if out["next_safe_step"] else "Следующий безопасный шаг не найден.")
        if out["blocked_actions"]:
            print("\n🚫 Нельзя:")
            for b in out["blocked_actions"]:
                print(b)
        if out["human_review"]["required"]:
            print("\n👤 Нужно решение человека:")
            print("Этот экран не является подтверждением.")
        if out["human_review"]["owner_required"]:
            print("\n🔒 Нужен владелец:")
            print("Это действие может разрешить только владелец.")
        if args.details:
            print("\n--- details ---")
            print(json.dumps(out, ensure_ascii=False, indent=2))

    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
