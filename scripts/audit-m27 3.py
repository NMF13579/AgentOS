#!/usr/bin/env python3
"""
Read-only full M27 audit.
This audit is not approval and does not authorize commit/push/merge/release.
Level 2 disabled is valid optional status: SKIPPED_LEVEL_2_NOT_ENABLED.
"""

import argparse
import json
import subprocess
from pathlib import Path

RESULT_L1_READY = "M27_LEVEL_1_READY_PLATFORM_OPTIONAL"
RESULT_L2_ENFORCED = "M27_LEVEL_2_PLATFORM_ENFORCED"
RESULT_L1_NOT_READY = "M27_LEVEL_1_NOT_READY"
RESULT_L2_OWNER_ACTION = "M27_LEVEL_2_NEEDS_OWNER_ACTION"
RESULT_NEEDS_REVIEW = "M27_NEEDS_REVIEW"
RESULT_INVALID = "M27_AUDIT_INVALID"


def emit(result: str, reason: str, details: list[str], as_json: bool):
    if as_json:
        print(json.dumps({"result": result, "reason": reason, "details": details}, ensure_ascii=True))
    else:
        print(f"RESULT: {result}")
        print(f"REASON: {reason}")
        if details:
            print("DETAILS:")
            for item in details:
                print(f"- {item}")


def parse_result(output: str):
    for line in output.splitlines():
        if line.startswith("RESULT:"):
            return line.split(":", 1)[1].strip()
    return None


def run_subprocess(cmd: list[str], cwd: Path):
    try:
        run = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True, check=False, timeout=60)
    except Exception as exc:
        return None, 1, str(exc)
    parsed = parse_result(run.stdout or "")
    full_out = (run.stdout or "").strip()
    if not full_out:
        full_out = (run.stderr or "").strip()
    return parsed, run.returncode, full_out


def run_level1_audit(repo_root: Path):
    script = repo_root / "scripts/audit-m27-level1.py"
    if not script.exists():
        return RESULT_L1_NOT_READY, "missing scripts/audit-m27-level1.py", []
    res, code, out = run_subprocess(["python3", str(script), "--root", str(repo_root)], repo_root)
    if res is None:
        return RESULT_NEEDS_REVIEW, "cannot parse Level 1 audit result", [out[:240]]
    if code == 0 and res in {"LEVEL_1_READY", "LEVEL_1_READY_WITH_WARNINGS"}:
        return "OK", "Level 1 audit passed", [res]
    if res == "LEVEL_1_NOT_READY":
        return RESULT_L1_NOT_READY, "Level 1 audit failed", [out[:240]]
    if res == "NEEDS_REVIEW":
        return RESULT_NEEDS_REVIEW, "Level 1 audit needs review", [out[:240]]
    return RESULT_NEEDS_REVIEW, "unknown Level 1 audit result", [f"result={res}", f"code={code}"]


def run_level1_smoke(repo_root: Path):
    script = repo_root / "scripts/test-m27-level1-fixtures.py"
    if not script.exists():
        return RESULT_L1_NOT_READY, "missing scripts/test-m27-level1-fixtures.py", []
    res, code, out = run_subprocess(["python3", str(script), "--root", str(repo_root)], repo_root)
    if res is None:
        return RESULT_NEEDS_REVIEW, "cannot parse Level 1 smoke result", [out[:240]]
    if code == 0 and res in {"LEVEL_1_SMOKE_PASS", "LEVEL_1_SMOKE_PASS_WITH_WARNINGS"}:
        return "OK", "Level 1 smoke passed", [res]
    if res == "LEVEL_1_SMOKE_FAIL":
        return RESULT_L1_NOT_READY, "Level 1 smoke failed", [out[:240]]
    if res == "LEVEL_1_SMOKE_NEEDS_REVIEW":
        return RESULT_NEEDS_REVIEW, "Level 1 smoke needs review", [out[:240]]
    return RESULT_NEEDS_REVIEW, "unknown Level 1 smoke result", [f"result={res}", f"code={code}"]


def run_level2_check(repo_root: Path, level_2_enabled: str, platform_state: str | None):
    script = repo_root / "scripts/check-github-platform-enforcement.py"
    if not script.exists():
        return RESULT_INVALID, "missing scripts/check-github-platform-enforcement.py", []

    cmd = ["python3", str(script), "check", "--level-2-enabled", level_2_enabled]
    if level_2_enabled == "true":
        if not platform_state:
            return RESULT_INVALID, "--platform-state is required when --level-2-enabled true", []
        cmd += ["--platform-state", platform_state]

    res, code, out = run_subprocess(cmd, repo_root)
    if res is None:
        return RESULT_NEEDS_REVIEW, "cannot parse Level 2 platform result", [out[:240]]

    if level_2_enabled == "false":
        if res == "SKIPPED_LEVEL_2_NOT_ENABLED" and code == 0:
            return RESULT_L1_READY, "Level 1 ready; Level 2 skipped", ["SKIPPED_LEVEL_2_NOT_ENABLED"]
        return RESULT_NEEDS_REVIEW, "unexpected Level 2 skip status", [f"result={res}", f"code={code}"]

    # level_2_enabled == true
    if res == "PLATFORM_ENFORCED" and code == 0:
        return RESULT_L2_ENFORCED, "Level 2 platform enforced", []
    if res in {"PLATFORM_PARTIAL", "NEEDS_OWNER_ACTION", "PLATFORM_NOT_ENFORCED"} and code == 1:
        return RESULT_L2_OWNER_ACTION, f"Level 2 needs owner/admin action ({res})", []
    if res == "PLATFORM_CHECK_INVALID" and code == 1:
        return RESULT_INVALID, "invalid Level 2 platform check input", []
    if res == "NEEDS_REVIEW" and code == 1:
        return RESULT_NEEDS_REVIEW, "Level 2 platform check needs review", []
    return RESULT_NEEDS_REVIEW, "unknown Level 2 platform status", [f"result={res}", f"code={code}"]


def main():
    parser = argparse.ArgumentParser(description="Read-only full M27 audit")
    parser.add_argument("--root", default=".")
    parser.add_argument("--level-2-enabled", choices=["true", "false"], default="false")
    parser.add_argument("--platform-state")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--explain", action="store_true")
    args = parser.parse_args()

    repo_root = Path(args.root).resolve()
    if not repo_root.exists() or not repo_root.is_dir():
        emit(RESULT_INVALID, "invalid --root path", [str(repo_root)], args.json)
        return 1

    details = [f"root={repo_root}"] if args.explain else []

    l1_audit_result, l1_audit_reason, l1_audit_details = run_level1_audit(repo_root)
    details.extend([f"level1_audit={l1_audit_reason}"] + l1_audit_details)
    if l1_audit_result != "OK":
        emit(l1_audit_result, l1_audit_reason, details, args.json)
        return 1

    l1_smoke_result, l1_smoke_reason, l1_smoke_details = run_level1_smoke(repo_root)
    details.extend([f"level1_smoke={l1_smoke_reason}"] + l1_smoke_details)
    if l1_smoke_result != "OK":
        emit(l1_smoke_result, l1_smoke_reason, details, args.json)
        return 1

    final_result, final_reason, level2_details = run_level2_check(
        repo_root, args.level_2_enabled, args.platform_state
    )
    details.extend(level2_details)

    emit(final_result, final_reason, details, args.json)
    return 0 if final_result in {RESULT_L1_READY, RESULT_L2_ENFORCED} else 1


if __name__ == "__main__":
    raise SystemExit(main())
