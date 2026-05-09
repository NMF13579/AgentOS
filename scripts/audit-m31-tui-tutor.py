#!/usr/bin/env python3
import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

RESULT_PASS = "M31_SAFETY_PASS"
RESULT_WARN = "M31_SAFETY_PASS_WITH_WARNINGS"
RESULT_FAIL = "M31_SAFETY_FAIL"
RESULT_REVIEW = "M31_SAFETY_NEEDS_REVIEW"

REQ_FILES = [
    "data/explanations/status-vocabulary.yml",
    "scripts/agentos-status.py",
    "scripts/agentos-view-model.py",
    "scripts/agentos-explain.py",
    "scripts/agentos-next-step.py",
    "scripts/renderers/plain_status_renderer.py",
    "scripts/renderers/rich_status_renderer.py",
    "scripts/agentos-tui.py",
    "docs/EXPLANATION-VOCABULARY.md",
    "docs/AGENTOS-STATUS.md",
    "docs/STATUS-VIEW-MODEL.md",
    "docs/AGENTOS-WHY.md",
    "docs/NEXT-SAFE-STEP.md",
    "docs/M31-RENDERER-ARCHITECTURE.md",
    "docs/AGENTOS-TUI.md",
]

FORBIDDEN_ACTIVE = [
    "Не волнуйтесь, всё безопасно.",
    "Можно просто продолжить.",
    "Это не страшно.",
    "approval granted",
    "можно выполнять",
]


def now_iso():
    return datetime.now().astimezone().isoformat(timespec="seconds")


def check_files(root: Path):
    checks = []
    errs = []
    for p in REQ_FILES:
        ok = (root / p).exists()
        checks.append({"id": "M31-FILE-001", "name": p, "result": "PASS" if ok else "FAIL", "message": "" if ok else "missing"})
        if not ok:
            errs.append({"code": "M31_REQUIRED_FILE_MISSING", "message": p})
    return checks, errs


def scan_text(path: Path):
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ""


def check_language(root: Path):
    targets = [root / "data/explanations/status-vocabulary.yml", root / "templates/tutor-explanation-card.md", root / "templates/next-safe-step-card.md"]
    checks = []
    warns = []
    for t in targets:
        if not t.exists():
            continue
        txt = scan_text(t)
        for phrase in FORBIDDEN_ACTIVE:
            if phrase in txt:
                checks.append({"id": "M31-LANG-001", "name": f"forbidden phrase in {t}", "result": "FAIL", "message": phrase})
                warns.append({"code": "M31_LANGUAGE_WARNING", "message": f"forbidden phrase in {t.name}: {phrase}"})
    if not checks:
        checks.append({"id": "M31-LANG-001", "name": "simple language safety", "result": "PASS", "message": ""})
    return checks, warns


def check_renderer(root: Path):
    checks = []
    errs = []
    forbid = ["subprocess", "os.system", "shutil.rmtree", "requests", "urllib", "input(", "write_text(", "write_bytes("]
    for rp in [root / "scripts/renderers/plain_status_renderer.py", root / "scripts/renderers/rich_status_renderer.py"]:
        txt = scan_text(rp)
        for f in forbid:
            if f in txt:
                checks.append({"id": "M31-REN-001", "name": f"{rp.name} contains {f}", "result": "FAIL", "message": "forbidden usage"})
                errs.append({"code": "M31_RENDERER_BOUNDARY_FAIL", "message": f"{rp.name}: {f}"})
    if not checks:
        checks.append({"id": "M31-REN-001", "name": "renderer boundary", "result": "PASS", "message": ""})
    return checks, errs


def check_dashboard(root: Path):
    txt = scan_text(root / "scripts/agentos-tui.py")
    checks = []
    errs = []
    if "input(" in txt:
        checks.append({"id": "M31-DASH-001", "name": "no interactive input", "result": "FAIL", "message": "input() found"})
        errs.append({"code": "M31_DASHBOARD_BOUNDARY_FAIL", "message": "interactive input found"})
    else:
        checks.append({"id": "M31-DASH-001", "name": "no interactive input", "result": "PASS", "message": ""})
    if "reports/context-pipeline.json" in txt and "--from-view-model-json" not in txt:
        checks.append({"id": "M31-DASH-002", "name": "no raw report reads", "result": "NEEDS_REVIEW", "message": "possible raw report coupling"})
    return checks, errs


def run_section(name, fn):
    checks, items = fn()
    has_fail = any(c["result"] == "FAIL" for c in checks)
    has_review = any(c["result"] == "NEEDS_REVIEW" for c in checks)
    if has_fail:
        sec = "FAIL"
    elif has_review:
        sec = "NEEDS_REVIEW"
    else:
        sec = "PASS"
    return {"name": name, "result": sec, "checks": checks}, items


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--root", default=".")
    ap.add_argument("--fixtures", action="store_true")
    ap.add_argument("--no-fixtures", action="store_true")
    ap.add_argument("--section", choices=["language", "safety", "renderer", "dashboard"])
    args = ap.parse_args()

    root = Path(args.root).resolve()
    sections = []
    warnings = []
    errors = []

    runners = []
    if args.section == "language":
        runners = [("language", lambda: check_language(root))]
    elif args.section == "renderer":
        runners = [("renderer", lambda: check_renderer(root))]
    elif args.section == "dashboard":
        runners = [("dashboard", lambda: check_dashboard(root))]
    elif args.section == "safety":
        runners = [("files", lambda: check_files(root)), ("renderer", lambda: check_renderer(root)), ("dashboard", lambda: check_dashboard(root))]
    else:
        runners = [
            ("files", lambda: check_files(root)),
            ("language", lambda: check_language(root)),
            ("renderer", lambda: check_renderer(root)),
            ("dashboard", lambda: check_dashboard(root)),
        ]

    for name, fn in runners:
        sec, items = run_section(name, fn)
        sections.append(sec)
        for i in items:
            if i.get("code", "").startswith("M31_LANGUAGE"):
                warnings.append(i)
            else:
                errors.append(i)

    result = RESULT_PASS
    if errors:
        result = RESULT_FAIL
    elif any(s["result"] == "NEEDS_REVIEW" for s in sections):
        result = RESULT_REVIEW
    elif warnings:
        result = RESULT_WARN

    out = {
        "schema_version": "1.0",
        "generated_at": now_iso(),
        "result": result,
        "repo_root": str(root),
        "sections": sections,
        "warnings": warnings,
        "errors": errors,
    }

    if args.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        print(result)

    if args.strict:
        return 0 if result == RESULT_PASS else 1
    return 0 if result in {RESULT_PASS, RESULT_WARN} else 1


if __name__ == "__main__":
    sys.exit(main())
