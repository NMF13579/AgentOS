#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
from pathlib import Path

RESULT_PASS = "M61_HARDENING_REGRESSION_PASS"
RESULT_WARN = "M61_HARDENING_REGRESSION_PASS_WITH_WARNINGS"
RESULT_BLOCKED = "M61_HARDENING_REGRESSION_BLOCKED"

PREMATURE_M61 = [
    "reports/m61-hardening-integration-summary.md",
    "reports/m61-hardening-action-review.json",
    "reports/m61-hardening-evidence-report.md",
    "reports/m61-completion-review.md",
]

M62_ACCEPTANCE_ARTIFACTS = [
    "scripts/check-agent-task-result.py",
    "scripts/check-task-acceptance.py",
    "schemas/task-result.schema.json",
    "schemas/agent-evidence.schema.json",
    "docs/TASK-VALIDATION-CONTRACT.md",
    "docs/TASK-OUTPUT-EVIDENCE-MODEL.md",
    "docs/ACCEPTANCE-CRITERIA-CHECKER.md",
]

REQUIRED_REPORTS_WITH_STATUS = {
    "reports/m60-completion-review.md": "m60_completion_review_checked",
    "reports/m60-cleanup-evidence-report.md": "m60_evidence_report_checked",
    "reports/m60-cleanup-integration-summary.md": "m60_integration_summary_checked",
    "reports/m61-m60-completion-intake.md": "m61_intake_checked",
    "docs/POST-M60-HARDENING-ARCHITECTURE.md": "m61_architecture_checked",
    "reports/m61-false-pass-risk-map.md": "m61_false_pass_risk_map_checked",
    "reports/m61-checker-hardening-plan.md": "m61_checker_hardening_plan_checked",
    "reports/m61-negative-fixture-gap-map.md": "m61_negative_fixture_gap_map_checked",
    "reports/m61-checker-repair-report.md": "m61_checker_repair_report_checked",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def add_warning(payload: dict, msg: str) -> None:
    payload["warnings"].append(msg)


def add_blocker(payload: dict, msg: str) -> None:
    payload["blockers"].append(msg)


def has_final_status(text: str) -> bool:
    return "FINAL_STATUS:" in text


def safe_run_json(cmd: list[str], timeout: int = 30) -> dict | None:
    proc = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=timeout,
        shell=False,
    )
    try:
        return json.loads(proc.stdout)
    except Exception:
        return None


def safe_run_help(cmd: list[str], timeout: int = 30) -> bool:
    proc = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=timeout,
        shell=False,
    )
    return proc.returncode == 0


def check_required_reports(root: Path, payload: dict) -> None:
    for rel, flag in REQUIRED_REPORTS_WITH_STATUS.items():
        p = root / rel
        if not p.exists():
            add_blocker(payload, f"missing required artifact: {rel}")
            payload[flag] = False
            continue
        text = read_text(p)
        if not has_final_status(text):
            add_blocker(payload, f"missing FINAL_STATUS in required artifact: {rel}")
            payload[flag] = False
            continue
        payload[flag] = True


def check_action_review(root: Path, payload: dict) -> None:
    p = root / "reports/m60-cleanup-action-review.json"
    if not p.exists():
        add_blocker(payload, "missing required artifact: reports/m60-cleanup-action-review.json")
        payload["m60_action_review_json_checked"] = False
        return
    try:
        data = json.loads(read_text(p))
    except Exception as exc:
        add_blocker(payload, f"malformed required JSON: reports/m60-cleanup-action-review.json ({exc})")
        payload["m60_action_review_json_checked"] = False
        return

    payload["m60_action_review_json_checked"] = True
    # M60 action review is required to parse; boundary-field checks belong to
    # the M61 repair report and are validated separately.


def check_repair_report_fields(root: Path, payload: dict) -> None:
    p = root / "reports/m61-checker-repair-report.md"
    if not p.exists():
        return
    text = read_text(p)
    required_lines = [
        "m62_artifacts_created: false",
        "task_acceptance_logic_created: false",
        "human_review_required: true",
        "m60_docs_modified: false",
    ]
    for line in required_lines:
        if line not in text:
            add_blocker(payload, f"m61 checker repair report missing required line: {line}")


def check_premature_artifacts(root: Path, payload: dict) -> None:
    found_m61 = []
    for rel in PREMATURE_M61:
        if (root / rel).exists():
            found_m61.append(rel)
    payload["premature_m61_artifacts_found"] = bool(found_m61)
    if found_m61:
        add_blocker(payload, f"premature M61 artifacts found: {', '.join(found_m61)}")

    found_m62 = []
    for rel in M62_ACCEPTANCE_ARTIFACTS:
        if (root / rel).exists():
            found_m62.append(rel)

    # Also detect any path containing m62 in monitored roots.
    for top in ["reports", "docs", "scripts", "tests", "templates", "schemas", "data"]:
        base = root / top
        if not base.exists():
            continue
        for fp in base.rglob("*"):
            if not fp.is_file():
                continue
            rel = fp.relative_to(root).as_posix()
            if "m62" in rel.lower() and rel not in found_m62:
                found_m62.append(rel)

    payload["premature_m62_artifacts_found"] = bool(found_m62)
    payload["m62_artifacts_found"] = bool(found_m62)
    payload["task_acceptance_logic_found"] = bool(
        any((root / rel).exists() for rel in M62_ACCEPTANCE_ARTIFACTS)
    )
    if found_m62:
        add_blocker(payload, f"M62 artifacts found: {', '.join(sorted(found_m62))}")


def run_optional_m60_checkers(root: Path, payload: dict) -> None:
    registry = root / "scripts/check-execution-verification-registry.py"
    chain = root / "scripts/check-execution-verification-chain.py"
    regression = root / "scripts/check-execution-verification-regression.py"

    payload["registry_checker_result"] = "NOT_RUN_UNSUPPORTED"
    payload["reusable_chain_checker_result"] = "NOT_RUN_UNSUPPORTED"
    payload["regression_runner_result"] = "NOT_RUN_UNSUPPORTED"

    # help checks (safe baseline)
    for p in (registry, chain, regression):
        if p.exists() and not safe_run_help([sys.executable, str(p), "--help"]):
            add_warning(payload, f"optional checker help failed: {p.name}")

    if registry.exists():
        data = safe_run_json([sys.executable, str(registry), "--json"])
        if data is None:
            add_warning(payload, "registry checker JSON unsupported or malformed")
        else:
            status = str(data.get("result") or data.get("status") or "")
            if status == "EXECUTION_VERIFICATION_REGISTRY_VALID":
                payload["registry_checker_result"] = "PASS"
            elif status == "EXECUTION_VERIFICATION_REGISTRY_VALID_WITH_WARNINGS":
                payload["registry_checker_result"] = "PASS_WITH_WARNINGS"
                add_warning(payload, "registry checker returned warnings")
            elif status == "EXECUTION_VERIFICATION_REGISTRY_INVALID":
                payload["registry_checker_result"] = "BLOCKED"
                add_blocker(payload, "registry checker reported invalid")
            else:
                payload["registry_checker_result"] = "NOT_RUN_UNSUPPORTED"
                add_warning(payload, f"registry checker returned unknown status: {status}")

    if chain.exists():
        data = safe_run_json([sys.executable, str(chain), "--json"])
        if data is None:
            add_warning(payload, "reusable chain checker JSON unsupported or malformed")
        else:
            status = str(data.get("result") or "")
            if status == "EXECUTION_VERIFICATION_CHAIN_VALID":
                payload["reusable_chain_checker_result"] = "PASS"
            elif status == "EXECUTION_VERIFICATION_CHAIN_VALID_WITH_WARNINGS":
                payload["reusable_chain_checker_result"] = "PASS_WITH_WARNINGS"
                add_warning(payload, "reusable chain checker returned warnings")
            elif status == "EXECUTION_VERIFICATION_CHAIN_INVALID":
                payload["reusable_chain_checker_result"] = "BLOCKED"
                add_blocker(payload, "reusable chain checker reported invalid")
            else:
                payload["reusable_chain_checker_result"] = "NOT_RUN_UNSUPPORTED"
                add_warning(payload, f"reusable chain checker returned unknown status: {status}")

    if regression.exists():
        data = safe_run_json([sys.executable, str(regression), "--json"])
        if data is None:
            add_warning(payload, "regression runner JSON unsupported or malformed")
        else:
            status = str(data.get("result") or "")
            if status == "EXECUTION_VERIFICATION_REGRESSION_PASS":
                payload["regression_runner_result"] = "PASS"
            elif status == "EXECUTION_VERIFICATION_REGRESSION_PASS_WITH_WARNINGS":
                payload["regression_runner_result"] = "PASS_WITH_WARNINGS"
                add_warning(payload, "regression runner returned warnings")
            elif status == "EXECUTION_VERIFICATION_REGRESSION_BLOCKED":
                payload["regression_runner_result"] = "BLOCKED"
                add_blocker(payload, "regression runner reported blocked")
            else:
                payload["regression_runner_result"] = "NOT_RUN_UNSUPPORTED"
                add_warning(payload, f"regression runner returned unknown status: {status}")


def finalize(payload: dict) -> tuple[str, int]:
    if payload["blockers"]:
        return RESULT_BLOCKED, 1
    if payload["warnings"]:
        return RESULT_WARN, 0
    return RESULT_PASS, 0


def build_payload(strict: bool) -> dict:
    return {
        "result": RESULT_BLOCKED,
        "strict": bool(strict),
        "m60_completion_review_checked": False,
        "m60_evidence_report_checked": False,
        "m60_action_review_json_checked": False,
        "m60_integration_summary_checked": False,
        "m61_intake_checked": False,
        "m61_architecture_checked": False,
        "m61_false_pass_risk_map_checked": False,
        "m61_checker_hardening_plan_checked": False,
        "m61_negative_fixture_gap_map_checked": False,
        "m61_checker_repair_report_checked": False,
        "registry_checker_result": "NOT_RUN_UNSUPPORTED",
        "reusable_chain_checker_result": "NOT_RUN_UNSUPPORTED",
        "regression_runner_result": "NOT_RUN_UNSUPPORTED",
        "premature_m61_artifacts_found": False,
        "premature_m62_artifacts_found": False,
        "m62_artifacts_found": False,
        "task_acceptance_logic_found": False,
        "human_review_required": True,
        "warnings": [],
        "blockers": [],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="M61 hardening regression orchestration runner (read-only)")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    parser.add_argument("--strict", action="store_true", help="Strict mode")
    args = parser.parse_args()

    payload = build_payload(args.strict)

    try:
        root = Path(__file__).resolve().parent.parent

        check_required_reports(root, payload)
        check_action_review(root, payload)
        check_repair_report_fields(root, payload)
        check_premature_artifacts(root, payload)
        run_optional_m60_checkers(root, payload)

        # strict mode: escalate warnings about unsupported optional checks
        if args.strict:
            for w in list(payload["warnings"]):
                if "unsupported" in w.lower() or "malformed" in w.lower():
                    add_blocker(payload, f"strict escalation: {w}")

        result, exit_code = finalize(payload)
        payload["result"] = result

        if args.json:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            print(result)
            for w in payload["warnings"]:
                print(f"WARN: {w}")
            for b in payload["blockers"]:
                print(f"BLOCK: {b}")

        return exit_code

    except Exception as exc:
        payload["result"] = RESULT_BLOCKED
        add_blocker(payload, f"runner error: {exc}")
        if args.json:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            print(RESULT_BLOCKED)
            print(f"BLOCK: runner error: {exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
