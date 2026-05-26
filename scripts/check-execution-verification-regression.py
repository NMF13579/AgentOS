#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
from pathlib import Path

RESULT_PASS = "EXECUTION_VERIFICATION_REGRESSION_PASS"
RESULT_WARN = "EXECUTION_VERIFICATION_REGRESSION_PASS_WITH_WARNINGS"
RESULT_BLOCKED = "EXECUTION_VERIFICATION_REGRESSION_BLOCKED"

ALLOWED_CHECKS = [
    "all",
    "m56-artifacts",
    "m57-artifacts",
    "m58-artifacts",
    "m59-artifacts",
    "m60-artifacts",
    "registry",
    "reusable-chain",
    "non-authority",
    "final-status",
    "no-premature-downstream",
]

RUN_CHECKS = [c for c in ALLOWED_CHECKS if c != "all"]

NON_AUTHORITY_STATEMENTS = [
    "Execution verification regression runner is not approval.",
    "Execution verification regression runner does not verify a real execution result.",
    "Execution verification regression runner does not start cleanup execution.",
    "Execution verification regression runner does not mutate lifecycle state.",
    "Execution verification regression runner does not authorize merge, push, or release.",
    "Execution verification regression runner does not change M56–M59 safety semantics.",
    "Execution verification regression runner does not replace human review.",
    "Execution verification regression runner does not start M61 or M62.",
    "Execution verification regression runner does not authorize starting 60.12 automatically.",
]

M59_REQUIRED = [
    "reports/m59-completion-review.md",
    "reports/m59-execution-result-verification-evidence-report.md",
    "reports/m59-execution-result-verification-action-review.json",
    "reports/m59-execution-result-verification-integration.md",
    "scripts/check-m59-execution-result-verification-fixtures.py",
    "docs/EXECUTION-RESULT-VERIFICATION-FIXTURE-RUNNER.md",
    "docs/EXECUTION-RESULT-VERIFICATION-CLI.md",
    "docs/EXECUTION-RESULT-VERIFICATION-POLICY.md",
]

M60_REQUIRED = [
    "reports/m60-m59-completion-intake.md",
    "docs/REPOSITORY-CLEANUP-CONSOLIDATION-ARCHITECTURE.md",
    "reports/m60-artifact-inventory.md",
    "docs/EXECUTION-VERIFICATION-SOURCE-OF-TRUTH.md",
    "reports/m60-duplication-drift-audit.md",
    "docs/AGENTOS-EXECUTION-VERIFICATION-REGISTRY-CONTRACT.md",
    "schemas/execution-verification-registry.schema.json",
    "data/execution-verification-registry.json",
    "scripts/build-execution-verification-registry.py",
    "scripts/check-execution-verification-registry.py",
    "docs/EXECUTION-VERIFICATION-REGISTRY.md",
    "reports/m60-validator-consolidation-plan.md",
    "scripts/check-execution-verification-chain.py",
    "docs/EXECUTION-VERIFICATION-REUSABLE-CHECKS.md",
    "reports/m60-documentation-pruning-plan.md",
    "reports/m60-documentation-consolidation-report.md",
]

FINAL_STATUS_RULES = {
    "reports/m60-m59-completion-intake.md": [
        "FINAL_STATUS: M60_INTAKE_READY",
        "FINAL_STATUS: M60_INTAKE_READY_WITH_WARNINGS",
    ],
    "docs/REPOSITORY-CLEANUP-CONSOLIDATION-ARCHITECTURE.md": [
        "FINAL_STATUS: M60_CLEANUP_ARCHITECTURE_DEFINED",
    ],
    "reports/m60-artifact-inventory.md": [
        "FINAL_STATUS: M60_ARTIFACT_INVENTORY_COMPLETE",
        "FINAL_STATUS: M60_ARTIFACT_INVENTORY_COMPLETE_WITH_WARNINGS",
    ],
    "docs/EXECUTION-VERIFICATION-SOURCE-OF-TRUTH.md": [
        "FINAL_STATUS: M60_SOURCE_OF_TRUTH_CLASSIFICATION_COMPLETE",
        "FINAL_STATUS: M60_SOURCE_OF_TRUTH_CLASSIFICATION_COMPLETE_WITH_WARNINGS",
    ],
    "reports/m60-duplication-drift-audit.md": [
        "FINAL_STATUS: M60_DUPLICATION_DRIFT_AUDIT_COMPLETE",
        "FINAL_STATUS: M60_DUPLICATION_DRIFT_AUDIT_COMPLETE_WITH_WARNINGS",
    ],
    "docs/AGENTOS-EXECUTION-VERIFICATION-REGISTRY-CONTRACT.md": [
        "FINAL_STATUS: M60_REGISTRY_CONTRACT_DEFINED",
    ],
    "docs/EXECUTION-VERIFICATION-REGISTRY.md": [
        "FINAL_STATUS: M60_REGISTRY_BUILDER_VALIDATOR_DEFINED",
    ],
    "reports/m60-validator-consolidation-plan.md": [
        "FINAL_STATUS: M60_VALIDATOR_CONSOLIDATION_PLAN_COMPLETE",
        "FINAL_STATUS: M60_VALIDATOR_CONSOLIDATION_PLAN_COMPLETE_WITH_WARNINGS",
    ],
    "docs/EXECUTION-VERIFICATION-REUSABLE-CHECKS.md": [
        "FINAL_STATUS: M60_REUSABLE_CHECKS_DEFINED",
    ],
    "reports/m60-documentation-pruning-plan.md": [
        "FINAL_STATUS: M60_DOCUMENTATION_PRUNING_PLAN_COMPLETE",
        "FINAL_STATUS: M60_DOCUMENTATION_PRUNING_PLAN_COMPLETE_WITH_WARNINGS",
    ],
    "reports/m60-documentation-consolidation-report.md": [
        "FINAL_STATUS: M60_DOCUMENTATION_CONSOLIDATION_COMPLETE",
        "FINAL_STATUS: M60_DOCUMENTATION_CONSOLIDATION_COMPLETE_WITH_WARNINGS",
    ],
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def add_warning(state: dict, check: str, msg: str) -> None:
    state["warnings"].append(msg)
    if check not in state["warning_checks"]:
        state["warning_checks"].append(check)


def add_blocker(state: dict, check: str, msg: str) -> None:
    state["blockers"].append(msg)
    if check not in state["blocked_checks"]:
        state["blocked_checks"].append(check)


def is_legacy_exempt(path: str) -> bool:
    if path.startswith("reports/"):
        tail = path[len("reports/"):]
        if tail.startswith("milestone-10") or tail.startswith("agentos-validate-cli"):
            return True
        if len(tail) >= 3 and tail[0] == "m" and tail[1:3].isdigit():
            n = int(tail[1:3])
            if 0 <= n <= 49:
                return True
    if path.startswith("docs/HONEST-PASS-"):
        return True
    if path.startswith("tasks/queue/"):
        return True
    return False


def run_subprocess_json(cmd: list[str], check: str, state: dict) -> dict | None:
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30,
            shell=False,
        )
    except Exception as exc:
        add_blocker(state, check, f"subprocess failed: {exc}")
        return None

    try:
        data = json.loads(proc.stdout)
    except Exception as exc:
        add_blocker(state, check, f"subprocess returned invalid JSON: {exc}")
        return None
    return data


def check_m56_m57_m58(root: Path, state: dict, check: str) -> None:
    inventory = root / "reports/m60-artifact-inventory.md"
    registry = root / "data/execution-verification-registry.json"
    found_signal = False

    if inventory.exists():
        txt = read_text(inventory).lower()
        if check.split("-")[0] in txt:
            found_signal = True
    if registry.exists():
        try:
            reg = json.loads(read_text(registry))
            if isinstance(reg.get("artifacts"), list):
                marker = check.split("-")[0]
                for entry in reg["artifacts"]:
                    if isinstance(entry, dict) and marker in str(entry.get("path", "")).lower():
                        found_signal = True
                        break
        except Exception:
            pass

    if not found_signal:
        add_warning(state, check, f"{check} paths not deterministically discoverable from current canonical sources")


def run_check_m59(root: Path, state: dict) -> None:
    check = "m59-artifacts"
    for rel in M59_REQUIRED:
        if not (root / rel).exists():
            add_blocker(state, check, f"missing required M59 artifact: {rel}")


def run_check_m60(root: Path, state: dict) -> None:
    check = "m60-artifacts"
    for rel in M60_REQUIRED:
        if not (root / rel).exists():
            add_blocker(state, check, f"missing required M60 artifact: {rel}")


def run_check_registry(root: Path, state: dict) -> str:
    check = "registry"
    data = run_subprocess_json(
        [sys.executable, str(root / "scripts/check-execution-verification-registry.py"), "--json"],
        check,
        state,
    )
    if data is None:
        return "blocked"
    result = str(data.get("result") or data.get("status") or "")
    if result not in {"EXECUTION_VERIFICATION_REGISTRY_VALID", "EXECUTION_VERIFICATION_REGISTRY_VALID_WITH_WARNINGS"}:
        add_blocker(state, check, f"invalid registry checker result: {result}")
        return "blocked"
    if result.endswith("WITH_WARNINGS"):
        add_warning(state, check, "registry checker returned warnings")
    return result


def run_check_reusable_chain(root: Path, state: dict) -> str:
    check = "reusable-chain"
    data = run_subprocess_json(
        [sys.executable, str(root / "scripts/check-execution-verification-chain.py"), "--json"],
        check,
        state,
    )
    if data is None:
        return "blocked"
    result = str(data.get("result", ""))
    if result not in {"EXECUTION_VERIFICATION_CHAIN_VALID", "EXECUTION_VERIFICATION_CHAIN_VALID_WITH_WARNINGS"}:
        add_blocker(state, check, f"invalid reusable chain checker result: {result}")
        return "blocked"
    if result.endswith("WITH_WARNINGS"):
        add_warning(state, check, "reusable chain checker returned warnings")
    return result


def run_check_non_authority(root: Path, state: dict) -> None:
    check = "non-authority"
    doc = root / "docs/EXECUTION-VERIFICATION-REGRESSION-RUNNER.md"
    text = read_text(doc) if doc.exists() else ""
    for line in NON_AUTHORITY_STATEMENTS:
        if line not in text:
            add_blocker(state, check, f"missing non-authority statement in docs: {line}")


def run_check_final_status(root: Path, state: dict) -> None:
    check = "final-status"
    for rel, markers in FINAL_STATUS_RULES.items():
        p = root / rel
        if not p.exists():
            add_blocker(state, check, f"missing status source: {rel}")
            continue
        txt = read_text(p)
        if not any(m in txt for m in markers):
            add_blocker(state, check, f"missing expected FINAL_STATUS family in {rel}")


def run_check_no_premature(root: Path, state: dict) -> None:
    check = "no-premature-downstream"
    summary = root / "reports/m60-cleanup-integration-summary.md"
    m60_12_created = False
    if summary.exists():
        txt = read_text(summary)
        m60_12_created = any(
            marker in txt
            for marker in [
                "FINAL_STATUS: M60_INTEGRATION_PASS",
                "FINAL_STATUS: M60_INTEGRATION_PASS_WITH_WARNINGS",
                "FINAL_STATUS: M60_INTEGRATION_BLOCKED",
            ]
        )

    if summary.exists() and not m60_12_created:
        add_blocker(
            state,
            check,
            "forbidden downstream artifact exists for current phase: reports/m60-cleanup-integration-summary.md",
        )

    action_review = root / "reports/m60-cleanup-action-review.json"
    m60_13_created = False
    if action_review.exists():
        try:
            review = json.loads(read_text(action_review))
            m60_13_created = review.get("final_status") in {
                "M60_CLEANUP_ACTION_REVIEW_PASS",
                "M60_CLEANUP_ACTION_REVIEW_PASS_WITH_WARNINGS",
                "M60_CLEANUP_ACTION_REVIEW_BLOCKED",
            }
        except Exception:
            m60_13_created = False
    if action_review.exists() and not m60_13_created:
        add_blocker(
            state,
            check,
            "forbidden downstream artifact exists for current phase: reports/m60-cleanup-action-review.json",
        )

    for rel in [
        "reports/m60-cleanup-evidence-report.md",
        "reports/m60-completion-review.md",
    ]:
        if (root / rel).exists():
            add_blocker(state, check, f"forbidden downstream artifact exists before allowed phase: {rel}")

    roots = ["reports", "docs", "scripts", "tests", "templates", "schemas", "data"]
    needles = ("m61", "m62")
    for top in roots:
        base = root / top
        if not base.exists():
            continue
        for fp in base.rglob("*"):
            if not fp.is_file():
                continue
            rel = fp.relative_to(root).as_posix()
            low = rel.lower()
            if any(n in low for n in needles) and not is_legacy_exempt(rel):
                add_blocker(state, check, f"premature downstream artifact detected: {rel}")


def validate_registry_and_schema_inputs(root: Path, registry_arg: str, schema_arg: str, state: dict) -> None:
    check = "registry"
    reg = root / registry_arg
    sch = root / schema_arg
    if not reg.exists():
        add_blocker(state, check, f"registry file missing: {registry_arg}")
        return
    if not sch.exists():
        add_blocker(state, check, f"schema file missing: {schema_arg}")
        return
    try:
        json.loads(read_text(reg))
    except Exception as exc:
        add_blocker(state, check, f"registry JSON malformed: {exc}")
    try:
        json.loads(read_text(sch))
    except Exception as exc:
        add_blocker(state, check, f"schema JSON malformed: {exc}")


def finalize(strict: bool, state: dict) -> tuple[str, int]:
    if strict and state["warnings"]:
        for w in list(state["warnings"]):
            wl = w.lower()
            if any(k in wl for k in [
                "missing required",
                "missing status",
                "non-authority",
                "registry json malformed",
                "schema json malformed",
                "premature",
                "malformed",
            ]):
                add_blocker(state, "strict", f"strict escalation: {w}")

    if state["blockers"]:
        return RESULT_BLOCKED, 2
    if state["warnings"]:
        return RESULT_WARN, 0
    return RESULT_PASS, 0


def explain_text() -> str:
    return (
        "Regression runner for M56-M59/M60 preservation checks. "
        "It validates artifacts, final statuses, non-authority boundaries, and downstream safety. "
        "It is read-only and does not approve execution results."
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="M60 regression validation runner (read-only)")
    parser.add_argument("--json", action="store_true", help="Output JSON only")
    parser.add_argument("--explain", action="store_true", help="Explain implemented regression checks")
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument("--strict", action="store_true", help="Strict mode")
    parser.add_argument("--check", action="append", help="Check(s) to run")
    parser.add_argument("--registry", default="data/execution-verification-registry.json", help="Registry JSON path")
    parser.add_argument("--schema", default="schemas/execution-verification-registry.schema.json", help="Schema path")
    args = parser.parse_args()

    requested = args.check if args.check else ["all"]
    unknown = [c for c in requested if c not in ALLOWED_CHECKS]

    state = {
        "checks_run": [],
        "passed_checks": [],
        "warning_checks": [],
        "blocked_checks": [],
        "warnings": [],
        "blockers": [],
        "non_authority": NON_AUTHORITY_STATEMENTS.copy(),
        "m56_status": "checked",
        "m57_status": "checked",
        "m58_status": "checked",
        "m59_status": "checked",
        "m60_status": "checked",
        "registry_result": "not_run",
        "reusable_chain_result": "not_run",
    }

    if unknown:
        add_blocker(state, "input", f"unknown --check value(s): {', '.join(unknown)}")

    root = Path(args.root).resolve()
    validate_registry_and_schema_inputs(root, args.registry, args.schema, state)

    run_list = RUN_CHECKS if ("all" in requested and not unknown) else [c for c in requested if c in RUN_CHECKS]

    for check in run_list:
        state["checks_run"].append(check)
        before_w = len(state["warning_checks"])
        before_b = len(state["blocked_checks"])

        if check == "m56-artifacts":
            check_m56_m57_m58(root, state, check)
        elif check == "m57-artifacts":
            check_m56_m57_m58(root, state, check)
        elif check == "m58-artifacts":
            check_m56_m57_m58(root, state, check)
        elif check == "m59-artifacts":
            run_check_m59(root, state)
        elif check == "m60-artifacts":
            run_check_m60(root, state)
        elif check == "registry":
            state["registry_result"] = run_check_registry(root, state)
        elif check == "reusable-chain":
            state["reusable_chain_result"] = run_check_reusable_chain(root, state)
        elif check == "non-authority":
            run_check_non_authority(root, state)
        elif check == "final-status":
            run_check_final_status(root, state)
        elif check == "no-premature-downstream":
            run_check_no_premature(root, state)

        if len(state["warning_checks"]) == before_w and len(state["blocked_checks"]) == before_b:
            state["passed_checks"].append(check)

    result, exit_code = finalize(args.strict, state)

    payload = {
        "result": result,
        "exit_code": exit_code,
        "strict": bool(args.strict),
        "root": args.root,
        "registry_path": args.registry,
        "schema_path": args.schema,
        "checks_requested": requested,
        "checks_run": state["checks_run"],
        "passed_checks": state["passed_checks"],
        "warning_checks": state["warning_checks"],
        "blocked_checks": state["blocked_checks"],
        "warnings": state["warnings"],
        "blockers": state["blockers"],
        "m56_status": state["m56_status"],
        "m57_status": state["m57_status"],
        "m58_status": state["m58_status"],
        "m59_status": state["m59_status"],
        "m60_status": state["m60_status"],
        "registry_result": state["registry_result"],
        "reusable_chain_result": state["reusable_chain_result"],
        "non_authority": state["non_authority"],
    }

    if args.explain and not args.json:
        print(explain_text())

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(result)
        for w in state["warnings"]:
            print(f"WARN: {w}")
        for b in state["blockers"]:
            print(f"BLOCK: {b}")

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
