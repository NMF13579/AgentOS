#!/usr/bin/env python3
import argparse
import json
import pathlib
import re
import subprocess
import sys

TOKEN_READY = "PRODUCT_SPEC_READINESS_READY"
TOKEN_NOT_READY = "PRODUCT_SPEC_READINESS_NOT_READY"
TOKEN_BLOCKED = "PRODUCT_SPEC_READINESS_BLOCKED"

VALIDATOR_OK = "PRODUCT_SPEC_VALIDATION_OK"
VALIDATOR_FAILED = "PRODUCT_SPEC_VALIDATION_FAILED"
VALIDATOR_BLOCKED = "PRODUCT_SPEC_VALIDATION_BLOCKED"

EXIT_CODES = {
    TOKEN_READY: 0,
    TOKEN_NOT_READY: 1,
    TOKEN_BLOCKED: 2,
}

ALLOWED_TARGETS = {"task-generation", "execution-planning"}
ALLOWED_LIFECYCLE = {
    "DRAFT",
    "INTERVIEWING",
    "NEEDS_CLARIFICATION",
    "REVIEW",
    "APPROVED",
    "EXECUTION_READY",
    "ARCHIVED",
}

FOUNDATION_FILES = [
    "docs/PRODUCT-SPEC-ARCHITECTURE.md",
    "docs/PRODUCT-SPEC-LIFECYCLE.md",
    "docs/PRODUCT-SPEC-TRANSITION-POLICY.md",
    "docs/SPEC-TO-TASK-LINEAGE.md",
    "docs/PRODUCT-SPEC-VALIDATION.md",
    "schemas/product-spec.schema.json",
    "schemas/spec-lineage.schema.json",
    "scripts/validate-product-spec.py",
    "templates/PRODUCT-SPEC.md",
    "examples/product-spec-example.md",
]

FIXTURE_EXPECTATIONS = {
    "approved-for-task-generation.md": {
        "task-generation": TOKEN_READY,
        "execution-planning": TOKEN_NOT_READY,
    },
    "execution-ready-for-execution-planning.md": {
        "task-generation": TOKEN_READY,
        "execution-planning": TOKEN_READY,
    },
    "draft-not-ready.md": {
        "task-generation": TOKEN_NOT_READY,
        "execution-planning": TOKEN_NOT_READY,
    },
    "review-not-ready.md": {
        "task-generation": TOKEN_NOT_READY,
        "execution-planning": TOKEN_NOT_READY,
    },
    "approved-not-ready-for-execution-planning.md": {
        "task-generation": TOKEN_READY,
        "execution-planning": TOKEN_NOT_READY,
    },
    "archived-not-ready.md": {
        "task-generation": TOKEN_NOT_READY,
        "execution-planning": TOKEN_NOT_READY,
    },
    "execution-ready-validator-failed.md": {
        "task-generation": TOKEN_NOT_READY,
        "execution-planning": TOKEN_NOT_READY,
    },
    "malformed-frontmatter-block.md": {
        "task-generation": TOKEN_BLOCKED,
        "execution-planning": TOKEN_BLOCKED,
    },
    "validator-blocked-malformed-spec.md": {
        "task-generation": TOKEN_BLOCKED,
        "execution-planning": TOKEN_BLOCKED,
    },
}


def build_result(token, target, lifecycle_status, validator_result, reason, errors=None, warnings=None):
    return {
        "result": token,
        "file": target,
        "target": lifecycle_status,
        "lifecycle_status": validator_result,
        "validator_result": reason,
        "errors": errors or [],
        "warnings": warnings or [],
    }


def print_result(token, file_path, target, lifecycle_status, validator_result, reason, errors=None, warnings=None, as_json=False):
    payload = {
        "result": token,
        "file": file_path,
        "target": target,
        "lifecycle_status": lifecycle_status,
        "validator_result": validator_result,
        "reason": reason,
        "errors": errors or [],
        "warnings": warnings or [],
    }
    if as_json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"{token} :: {file_path}")
        print(f"target: {target}")
        print(f"lifecycle_status: {lifecycle_status}")
        print(f"validator_result: {validator_result}")
        print(f"reason: {reason}")
        if payload["errors"]:
            print("errors:")
            for e in payload["errors"]:
                print(f"- {e}")
        if payload["warnings"]:
            print("warnings:")
            for w in payload["warnings"]:
                print(f"- {w}")


def check_foundation(root):
    missing = []
    for rel in FOUNDATION_FILES:
        if not (root / rel).is_file():
            missing.append(rel)
    return missing


def extract_lifecycle_status(text):
    match = re.search(r"^\s*lifecycle_status\s*:\s*\"?([A-Za-z_]+)\"?\s*$", text, re.MULTILINE)
    if not match:
        return None
    return match.group(1).strip()


def run_validator(root, file_path):
    validator = root / "scripts/validate-product-spec.py"
    cmd = [sys.executable, str(validator), "--file", str(file_path)]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True)
    except Exception as exc:
        return None, f"validator execution failed: {exc}", ""

    output = (proc.stdout or "") + (proc.stderr or "")
    if VALIDATOR_OK in output:
        return VALIDATOR_OK, "validator passed", output
    if VALIDATOR_FAILED in output:
        return VALIDATOR_FAILED, "validator failed", output
    if VALIDATOR_BLOCKED in output:
        return VALIDATOR_BLOCKED, "validator blocked", output
    return None, "validator returned unknown output", output


def check_readiness(root, file_path, target):
    missing = check_foundation(root)
    if missing:
        return TOKEN_BLOCKED, "unknown", "unknown", f"missing required foundation artifact(s): {', '.join(missing)}", []

    p = pathlib.Path(file_path)
    if not p.is_absolute():
        p = root / p

    if not p.is_file():
        return TOKEN_BLOCKED, "unknown", "unknown", "file does not exist", []

    validator_result, validator_reason, validator_output = run_validator(root, p)
    if validator_result is None:
        return TOKEN_BLOCKED, "unknown", "unknown", validator_reason, [validator_output]

    if validator_result == VALIDATOR_BLOCKED:
        return TOKEN_BLOCKED, "unknown", validator_result, "validator blocked; readiness cannot proceed", [validator_output]

    if validator_result == VALIDATOR_FAILED:
        return TOKEN_NOT_READY, "unknown", validator_result, "validator failed; readiness denied", [validator_output]

    try:
        text = p.read_text(encoding="utf-8")
    except Exception as exc:
        return TOKEN_BLOCKED, "unknown", validator_result, f"file is not readable after validator OK: {exc}", [validator_output]

    lifecycle = extract_lifecycle_status(text)
    if lifecycle is None:
        return TOKEN_BLOCKED, "unknown", validator_result, "missing body lifecycle_status after validator OK", [validator_output]
    if lifecycle not in ALLOWED_LIFECYCLE:
        return TOKEN_BLOCKED, lifecycle, validator_result, "invalid body lifecycle_status after validator OK", [validator_output]

    if target == "task-generation":
        if lifecycle in {"APPROVED", "EXECUTION_READY"}:
            return TOKEN_READY, lifecycle, validator_result, "target requirements satisfied", [validator_output]
        return TOKEN_NOT_READY, lifecycle, validator_result, "lifecycle does not satisfy task-generation target", [validator_output]

    if target == "execution-planning":
        if lifecycle == "EXECUTION_READY":
            return TOKEN_READY, lifecycle, validator_result, "target requirements satisfied", [validator_output]
        return TOKEN_NOT_READY, lifecycle, validator_result, "lifecycle does not satisfy execution-planning target", [validator_output]

    return TOKEN_BLOCKED, lifecycle, validator_result, "unknown target", [validator_output]


def run_fixtures(root, as_json=False):
    base = root / "tests/fixtures/product-spec-readiness"
    ready_dir = base / "ready"
    not_ready_dir = base / "not-ready"
    blocked_dir = base / "blocked"

    if not base.is_dir() or not ready_dir.is_dir() or not not_ready_dir.is_dir() or not blocked_dir.is_dir():
        print_result(
            TOKEN_BLOCKED,
            str(base),
            "fixtures",
            "unknown",
            "unknown",
            "fixtures directory is missing or unreadable",
            as_json=as_json,
        )
        return EXIT_CODES[TOKEN_BLOCKED]

    failures = []
    for fixture_name, target_map in sorted(FIXTURE_EXPECTATIONS.items()):
        fixture_path = None
        for sub in (ready_dir, not_ready_dir, blocked_dir):
            candidate = sub / fixture_name
            if candidate.is_file():
                fixture_path = candidate
                break
        if fixture_path is None:
            failures.append(f"missing fixture file: {fixture_name}")
            continue

        for target, expected in target_map.items():
            actual, lifecycle, validator_result, reason, details = check_readiness(root, fixture_path, target)
            if actual != expected:
                failures.append(
                    f"{fixture_name} [{target}] expected {expected} but got {actual} (lifecycle={lifecycle}, validator={validator_result}, reason={reason})"
                )

    if failures:
        print_result(
            TOKEN_NOT_READY,
            str(base),
            "fixtures",
            "suite",
            "mixed",
            "fixture suite failed (this means test suite is not deterministic/pass)",
            errors=failures,
            as_json=as_json,
        )
        return EXIT_CODES[TOKEN_NOT_READY]

    print_result(
        TOKEN_READY,
        str(base),
        "fixtures",
        "suite",
        "deterministic",
        "fixture suite passed (this READY means the readiness test suite passed)",
        as_json=as_json,
    )
    return EXIT_CODES[TOKEN_READY]


def main():
    parser = argparse.ArgumentParser(description="Deterministic Product Spec readiness gate")
    parser.add_argument("--file", help="Path to Product Spec markdown file")
    parser.add_argument("--target", choices=sorted(ALLOWED_TARGETS), help="Readiness target")
    parser.add_argument("--fixtures", action="store_true", help="Run readiness fixtures")
    parser.add_argument("--json", action="store_true", help="Print JSON output")
    args = parser.parse_args()

    root = pathlib.Path(__file__).resolve().parents[1]

    if args.fixtures:
        if args.file or args.target:
            print_result(
                TOKEN_BLOCKED,
                "cli",
                "fixtures",
                "unknown",
                "unknown",
                "--fixtures cannot be combined with --file/--target",
                as_json=args.json,
            )
            return EXIT_CODES[TOKEN_BLOCKED]
        return run_fixtures(root, as_json=args.json)

    if not args.file or not args.target:
        print_result(
            TOKEN_BLOCKED,
            "cli",
            "unknown",
            "unknown",
            "unknown",
            "use --file <path> and --target <task-generation|execution-planning>, or use --fixtures",
            as_json=args.json,
        )
        return EXIT_CODES[TOKEN_BLOCKED]

    token, lifecycle, validator_result, reason, details = check_readiness(root, args.file, args.target)
    print_result(
        token,
        args.file,
        args.target,
        lifecycle,
        validator_result,
        reason,
        warnings=details,
        as_json=args.json,
    )
    return EXIT_CODES[token]


if __name__ == "__main__":
    sys.exit(main())
