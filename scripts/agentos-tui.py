#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE / "renderers") not in sys.path:
    sys.path.insert(0, str(HERE / "renderers"))

from plain_status_renderer import render_status_view_model as plain_render  # type: ignore
try:
    from rich_status_renderer import render_status_view_model as rich_render  # type: ignore
except Exception:
    rich_render = None


def now_iso():
    return datetime.now().astimezone().isoformat(timespec="seconds")


def run_json(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode not in (0, 1):
        raise RuntimeError(p.stderr.strip() or "command failed")
    return json.loads(p.stdout)


def load_inputs(args, root: Path):
    warnings = []
    errors = []
    vm = None
    ex = None
    ns = None

    try:
        if args.from_view_model_json:
            vm = json.loads(Path(args.from_view_model_json).read_text(encoding="utf-8"))
        else:
            vm = run_json([sys.executable, str(root / "scripts/agentos-view-model.py"), "--json"])
    except Exception:
        errors.append({"code": "VIEW_MODEL_MALFORMED", "message": "View Model недоступен."})

    try:
        if args.from_explanation_json:
            ex = json.loads(Path(args.from_explanation_json).read_text(encoding="utf-8"))
        else:
            ex = run_json([sys.executable, str(root / "scripts/agentos-explain.py"), "--json"])
    except Exception:
        warnings.append({"code": "EXPLANATION_DATA_MISSING", "message": "Explanation JSON недоступен."})

    try:
        if args.from_next_step_json:
            ns = json.loads(Path(args.from_next_step_json).read_text(encoding="utf-8"))
        else:
            ns = run_json([sys.executable, str(root / "scripts/agentos-next-step.py"), "--json"])
    except Exception:
        warnings.append({"code": "NEXT_STEP_DATA_MISSING", "message": "Next Step JSON недоступен."})

    return vm, ex, ns, warnings, errors


def build_dashboard(vm, ex, ns, warnings, errors):
    if not vm:
        return {
            "overall_status": "AGENTOS_STATUS_UNKNOWN",
            "top_status_code": "STATUS_SOURCE_DAMAGED",
            "severity": "UNKNOWN",
            "authority": "SYSTEM_BLOCKED",
            "title": "Статус неизвестен",
            "summary": "Нет данных View Model.",
            "next_step_label": "",
            "next_step_command": "",
            "source": "",
            "freshness": "unknown",
            "human_gate_required": False,
            "owner_review_required": False,
            "blocked_actions": ["Продолжать нельзя без проверки."]
        }

    if ex and any(vm.get(k) != ex.get(k) for k in ["overall_status", "top_status_code", "severity", "authority"]):
        warnings.append({"code": "DASHBOARD_INPUT_MISMATCH", "message": "View Model и Explanation расходятся."})

    if ns and any(vm.get(k) != ns.get(k) for k in ["overall_status", "top_status_code", "severity", "authority"]):
        warnings.append({"code": "DASHBOARD_INPUT_MISMATCH", "message": "View Model и Next Step расходятся."})

    selected = (ns or {}).get("selected_step") or {}
    return {
        "overall_status": vm.get("overall_status", "AGENTOS_STATUS_UNKNOWN"),
        "top_status_code": vm.get("top_status_code", "STATUS_SOURCE_DAMAGED"),
        "severity": vm.get("severity", "UNKNOWN"),
        "authority": vm.get("authority", "SYSTEM_BLOCKED"),
        "title": vm.get("title", "Статус неизвестен"),
        "summary": (ex or {}).get("what_happened", vm.get("summary", "")),
        "next_step_label": selected.get("label", ""),
        "next_step_command": selected.get("command", ""),
        "source": (vm.get("source") or {}).get("report", ""),
        "freshness": (vm.get("source") or {}).get("freshness", "unknown"),
        "human_gate_required": bool((vm.get("flags") or {}).get("requires_human_gate", False) or vm.get("authority") == "HUMAN_GATE_REQUIRED"),
        "owner_review_required": bool((vm.get("flags") or {}).get("requires_owner_review", False) or vm.get("authority") == "OWNER_REVIEW_REQUIRED"),
        "blocked_actions": vm.get("blocked_actions", [])
    }


def snapshot_write(path: Path, root: Path, composed: dict):
    safe = (root / path).resolve() if not path.is_absolute() else path.resolve()
    if not str(safe).startswith(str(root)):
        raise ValueError("unsafe snapshot path")
    safe.parent.mkdir(parents=True, exist_ok=True)
    safe.write_text(
        "# M31 Dashboard Snapshot\n\n"
        f"generated_at: {composed['generated_at']}\n"
        f"overall_status: {composed['dashboard']['overall_status']}\n"
        f"top_status_code: {composed['dashboard']['top_status_code']}\n"
        f"severity: {composed['dashboard']['severity']}\n"
        f"authority: {composed['dashboard']['authority']}\n\n"
        "This dashboard snapshot is not approval.\n",
        encoding="utf-8"
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ascii", action="store_true")
    ap.add_argument("--no-color", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--snapshot", nargs="?", const="reports/m31-dashboard-snapshot.md")
    ap.add_argument("--from-view-model-json")
    ap.add_argument("--from-explanation-json")
    ap.add_argument("--from-next-step-json")
    ap.add_argument("--root", default=".")
    ap.add_argument("--source-summary", action="store_true")
    ap.add_argument("--debug-data", action="store_true")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    vm, ex, ns, warnings, errors = load_inputs(args, root)
    dash = build_dashboard(vm, ex, ns, warnings, errors)

    composed = {
        "schema_version": "1.0",
        "generated_at": now_iso(),
        "live_status": bool((vm or {}).get("live_status", False)),
        "status_view_model": vm or {},
        "tutor_explanation": ex or {},
        "next_safe_step": ns or {},
        "dashboard": dash,
        "warnings": warnings,
        "errors": errors
    }

    if args.snapshot:
        try:
            snapshot_write(Path(args.snapshot), root, composed)
        except Exception:
            composed["errors"].append({"code": "UNSAFE_SNAPSHOT_PATH", "message": "Небезопасный путь snapshot."})
            if args.json:
                print(json.dumps(composed, ensure_ascii=False, indent=2))
            else:
                print("❓ Snapshot path unsafe")
            return 1

    if args.json:
        print(json.dumps(composed, ensure_ascii=False, indent=2))
        return 0 if not errors else 1

    # Render summary block
    base = {
        "icon": "🔎" if dash["severity"] in {"NEEDS_REVIEW", "WARNING"} else ("⛔" if dash["severity"] == "BLOCKED" else ("❓" if dash["severity"] == "UNKNOWN" else "✅")),
        "ascii_label": "[REVIEW]" if dash["severity"] in {"NEEDS_REVIEW", "WARNING"} else ("[BLOCKED]" if dash["severity"] == "BLOCKED" else ("[UNKNOWN]" if dash["severity"] == "UNKNOWN" else "[OK]")),
        "title": dash["title"],
        "summary": dash["summary"],
        "overall_status": dash["overall_status"],
        "top_status_code": dash["top_status_code"],
        "source": {"report": dash["source"]}
    }

    text = ""
    if args.ascii or args.no_color or rich_render is None:
        text = plain_render(base, ascii=args.ascii, no_color=args.no_color)
        if rich_render is None and not args.ascii:
            warnings.append({"code": "RICH_UNAVAILABLE_USING_PLAIN", "message": "Rich недоступен, используем plain renderer."})
    else:
        try:
            text = rich_render(base, ascii=args.ascii, no_color=args.no_color)
        except Exception:
            warnings.append({"code": "RICH_RENDERER_FAILED_USING_PLAIN", "message": "Rich renderer упал, используем plain renderer."})
            text = plain_render(base, ascii=True, no_color=True)

    print(text)
    print("\nNext safe step:")
    print(dash["next_step_command"] or "Следующий безопасный шаг не найден.")
    if dash["blocked_actions"]:
        print("\nBlocked actions:")
        for b in dash["blocked_actions"]:
            print(f"- {b}")
    if dash["human_gate_required"]:
        print("\n👤 Нужно решение человека. Этот экран не является подтверждением.")
    if dash["owner_review_required"]:
        print("\n🔒 Нужен владелец.")
    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(f"- {w['code']}: {w['message']}")
    if errors:
        print("\nErrors:")
        for e in errors:
            print(f"- {e['code']}: {e['message']}")

    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
