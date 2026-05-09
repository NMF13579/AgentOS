#!/usr/bin/env python3
import argparse
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ALLOWED_TYPES = {"read_only_check", "open_report", "show_explanation", "create_snapshot", "request_human_review"}
FORBIDDEN_VERBS = ["fix", "go", "approve", "ready", "commit", "push", "merge", "promote", "mark ready", "bypass", "auto-fix", "разрешить", "подтвердить", "выполнить", "смержить", "запушить"]


def now_iso():
    return datetime.now().astimezone().isoformat(timespec="seconds")


def load_vm(args, root: Path):
    if args.from_view_model_json:
        return json.loads(Path(args.from_view_model_json).read_text(encoding="utf-8"))
    cmd = [sys.executable, str(root / "scripts/agentos-view-model.py"), "--json"]
    if args.status:
        cmd += ["--status", args.status]
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode not in (0, 1):
        raise RuntimeError("view model failed")
    return json.loads(p.stdout)


def is_unsafe_text(text: str):
    low = (text or "").lower()
    return any(v in low for v in FORBIDDEN_VERBS)


def classify_step(step):
    if not isinstance(step, dict):
        return None, {"code": "NEXT_SAFE_STEP_MISSING", "message": "Следующий безопасный шаг не найден."}
    t = step.get("type", "")
    label = step.get("label", "")
    cmd = step.get("command", "")
    if t not in ALLOWED_TYPES:
        return None, {"code": "UNSAFE_STEP_TYPE", "message": "Недопустимый тип шага."}
    if is_unsafe_text(label) or is_unsafe_text(cmd):
        return None, {"code": "UNSAFE_VERB_DETECTED", "message": "Обнаружен запрещённый глагол в шаге."}
    return {
        "label": label,
        "command": cmd,
        "type": t,
        "safe_to_display": True,
        "safe_to_execute_by_m31": False
    }, None


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
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--validate-safety", action="store_true")
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
            "next_safe_steps": [],
            "next_safe_step": None,
            "blocked_actions": ["Продолжать без проверки нельзя."],
            "flags": {"requires_human_gate": False, "requires_owner_review": False},
            "source": {"report": "", "freshness": "unknown"},
            "icon": "❓",
            "ascii_label": "[UNKNOWN]",
            "color": "gray",
            "title": "Статус неизвестен"
        }
        errors.append({"code": "VIEW_MODEL_MALFORMED", "message": "View model недоступен или повреждён."})

    steps = vm.get("next_safe_steps") if isinstance(vm.get("next_safe_steps"), list) else []
    hint = vm.get("next_safe_step")
    if steps and hint and steps[0] != hint:
        warnings.append({"code": "NEXT_STEP_FIELD_MISMATCH", "message": "next_safe_steps и next_safe_step не совпадают."})

    safe_all = []
    rejected = []
    for st in (steps if steps else ([hint] if hint else [])):
        safe, err = classify_step(st)
        if safe:
            safe_all.append(safe)
        elif err:
            rejected.append(err)

    if len(safe_all) > 1:
        warnings.append({"code": "MULTIPLE_STEPS_AVAILABLE", "message": "Доступно несколько безопасных шагов."})

    selected = safe_all[0] if safe_all else None
    if selected is None:
        warnings.append({"code": "NEXT_SAFE_STEP_MISSING", "message": "Следующий безопасный шаг не найден."})

    blocked = vm.get("blocked_actions") if isinstance(vm.get("blocked_actions"), list) else []
    sev = vm.get("severity", "UNKNOWN")
    if sev in {"BLOCKED", "UNKNOWN"} and not blocked:
        errors.append({"code": "BLOCKED_ACTIONS_REQUIRED", "message": "Для рискованного статуса нужны blocked_actions."})
        blocked = ["Продолжать без проверки нельзя."]

    for e in rejected:
        errors.append({"code": "UNSAFE_NEXT_STEP", "message": e["message"]})

    dna = [
        "approval", "mark ready", "commit", "push", "merge", "protected write", "state change", "Human Gate approval", "owner approval"
    ]

    out = {
        "schema_version": "1.0",
        "generated_at": now_iso(),
        "live_status": bool(vm.get("live_status", False)),
        "overall_status": vm.get("overall_status", "AGENTOS_STATUS_UNKNOWN"),
        "top_status_code": vm.get("top_status_code", "STATUS_SOURCE_DAMAGED"),
        "severity": sev,
        "authority": vm.get("authority", "SYSTEM_BLOCKED"),
        "selected_step": selected,
        "all_steps": safe_all,
        "why_safe": "Это только проверка. Она не создаёт approval и не меняет protected files.",
        "does_not_authorize": dna,
        "blocked_actions": blocked,
        "human_review": {
            "required": bool(vm.get("flags", {}).get("requires_human_gate", False) or vm.get("authority") == "HUMAN_GATE_REQUIRED"),
            "owner_required": bool(vm.get("flags", {}).get("requires_owner_review", False) or vm.get("authority") == "OWNER_REVIEW_REQUIRED"),
            "reason": "Нужно отдельное решение человека." if (vm.get("authority") in {"HUMAN_GATE_REQUIRED", "OWNER_REVIEW_REQUIRED"}) else ""
        },
        "source": {
            "report": (vm.get("source") or {}).get("report", ""),
            "freshness": (vm.get("source") or {}).get("freshness", "unknown")
        },
        "display": {
            "icon": "▶️",
            "ascii_label": "[NEXT]",
            "color": "blue"
        },
        "warnings": warnings,
        "errors": errors
    }

    if args.validate_safety:
        result = "NEXT_STEP_SAFETY_PASS"
        if errors:
            result = "NEXT_STEP_SAFETY_FAIL"
        elif warnings:
            result = "NEXT_STEP_SAFETY_PASS_WITH_WARNINGS"
        if args.json:
            print(json.dumps({"schema_version": "1.0", "result": result, "warnings": warnings, "errors": errors}, ensure_ascii=False, indent=2))
        else:
            print(result)
        return 0 if result in {"NEXT_STEP_SAFETY_PASS", "NEXT_STEP_SAFETY_PASS_WITH_WARNINGS"} else 1

    if args.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        lead = out["display"]["ascii_label"] if args.ascii else out["display"]["icon"]
        print(f"{lead} Следующий безопасный шаг\n")
        print("Статус:")
        s_icon = vm.get("ascii_label", "[UNKNOWN]") if args.ascii else vm.get("icon", "❓")
        print(f"{s_icon} {vm.get('title','Статус неизвестен')}")
        print("\nСделай:")
        print(selected["command"] if selected else "Следующий безопасный шаг не найден.")
        print("\nПочему это безопасно:")
        print(out["why_safe"])
        print("\n🚫 Это не разрешает:")
        for x in dna[:5]:
            print(x)
        if blocked:
            print("\nНельзя:")
            for b in blocked:
                print(b)
        if out["human_review"]["required"]:
            print("\n👤 Нужно решение человека.")
            print("Этот экран не является подтверждением.")
        if out["human_review"]["owner_required"]:
            print("\n🔒 Нужен владелец.")
        if args.details or args.all:
            print("\n--- all steps ---")
            print(json.dumps(out["all_steps"], ensure_ascii=False, indent=2))

    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
