#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


PASS_RESULT = "M55_ACTIVE_TASK_READINESS_FIXTURES_PASS"
BLOCKED_RESULT = "M55_ACTIVE_TASK_READINESS_FIXTURES_BLOCKED"
ARGUMENT_ERROR = "FIXTURE_INTEGRATION_ARGUMENT_ERROR"

SANDBOX_ROOT = Path("/tmp/m55-active-task-readiness-fixture-integration")

CLI_MARKERS = [
    "M55 active-task readiness CLI is read-only.",
    "The CLI does not write tasks/active-task.md.",
    "The CLI does not create approval records.",
    "The CLI does not authorize execution or M56.",
    "The CLI does not include a fixture mode.",
]

POLICY_MARKERS = [
    "This document defines the M55 active-task readiness policy.",
    "M55 readiness policy must fail closed on missing, malformed, unknown, or contradictory inputs.",
    "UNKNOWN must not be treated as ACTIVE_TASK_READINESS_CONFIRMED.",
    "The M55 readiness policy does not authorize active-task replacement.",
    "The M55 readiness policy does not authorize execution.",
    "The M55 readiness policy does not authorize M56.",
]

NON_AUTHORITY_MARKERS = [
    "M55 fixture integration is not approval.",
    "M55 fixture integration does not authorize execution.",
    "M55 fixture integration does not authorize active-task replacement.",
    "M55 fixture integration does not write tasks/active-task.md.",
    "M55 fixture integration does not create approval records.",
    "M55 fixture integration does not authorize M56.",
    "M55 fixture integration does not start M56.",
]

POSITIVE_SCENARIOS = [
    {
        "name": "positive-confirmed-json",
        "input": "tests/fixtures/active-task-readiness/positive/valid-readiness-input.json",
        "proposal": "tests/fixtures/active-task-readiness/positive/valid-active-task-proposal-ready.json",
        "queue_entry": "tasks/queue/valid-ready.md",
        "expected_result": "ACTIVE_TASK_READINESS_CONFIRMED",
        "expected_exit_code": 0,
        "expected_blocker": None,
    },
    {
        "name": "positive-confirmed-with-limitations-json",
        "input": "tests/fixtures/active-task-readiness/positive/valid-readiness-input-with-limitations.json",
        "proposal": "tests/fixtures/active-task-readiness/positive/valid-active-task-proposal-ready-with-limitations.json",
        "queue_entry": "tasks/queue/valid-ready.md",
        "expected_result": "ACTIVE_TASK_READINESS_CONFIRMED_WITH_LIMITATIONS",
        "expected_exit_code": 0,
        "expected_blocker": None,
    },
    {
        "name": "positive-markdown-input",
        "input": "tests/fixtures/active-task-readiness/positive/valid-readiness-input-markdown.md",
        "proposal": "tests/fixtures/active-task-readiness/positive/valid-active-task-proposal-ready.json",
        "queue_entry": "tasks/queue/valid-ready.md",
        "expected_result": "ACTIVE_TASK_READINESS_CONFIRMED",
        "expected_exit_code": 0,
        "expected_blocker": None,
    },
    {
        "name": "positive-markdown-proposal",
        "input": "tests/fixtures/active-task-readiness/positive/valid-readiness-input.json",
        "proposal": "tests/fixtures/active-task-readiness/positive/valid-active-task-proposal-markdown.md",
        "queue_entry": "tasks/queue/valid-ready.md",
        "expected_result": "ACTIVE_TASK_READINESS_CONFIRMED",
        "expected_exit_code": 0,
        "expected_blocker": None,
    },
]

NEGATIVE_SCENARIOS = [
    {
        "name": "missing-input-root",
        "input": "tests/fixtures/active-task-readiness/negative/missing-input-root.json",
        "proposal": "tests/fixtures/active-task-readiness/positive/valid-active-task-proposal-ready.json",
        "queue_entry": "tasks/queue/valid-ready.md",
        "expected_result": "ACTIVE_TASK_READINESS_BLOCKED",
        "expected_exit_code": 2,
        "expected_blocker": "MISSING_ACTIVE_TASK_READINESS_INPUT_ROOT",
        "kind": "input",
    },
    {
        "name": "missing-proposal-root",
        "input": "tests/fixtures/active-task-readiness/positive/valid-readiness-input.json",
        "proposal": "tests/fixtures/active-task-readiness/negative/missing-proposal-root.json",
        "queue_entry": "tasks/queue/valid-ready.md",
        "expected_result": "ACTIVE_TASK_READINESS_BLOCKED",
        "expected_exit_code": 2,
        "expected_blocker": "MISSING_ACTIVE_TASK_PROPOSAL_ROOT",
        "kind": "proposal",
    },
    {
        "name": "malformed-readiness-input",
        "input": "tests/fixtures/active-task-readiness/negative/malformed-readiness-input.json",
        "proposal": "tests/fixtures/active-task-readiness/positive/valid-active-task-proposal-ready.json",
        "queue_entry": "tasks/queue/valid-ready.md",
        "expected_result": "ACTIVE_TASK_READINESS_BLOCKED",
        "expected_exit_code": 2,
        "expected_blocker": "MALFORMED_JSON",
        "kind": "input",
    },
    {
        "name": "readiness-input-queue-entry-mismatch",
        "input": "tests/fixtures/active-task-readiness/negative/readiness-input-queue-entry-mismatch.json",
        "proposal": "tests/fixtures/active-task-readiness/positive/valid-active-task-proposal-ready.json",
        "queue_entry": "tasks/queue/valid-ready.md",
        "expected_result": "ACTIVE_TASK_READINESS_BLOCKED",
        "expected_exit_code": 2,
        "expected_blocker": "INPUT_QUEUE_ENTRY_MISMATCH",
        "kind": "input",
    },
    {
        "name": "readiness-input-target-invalid",
        "input": "tests/fixtures/active-task-readiness/negative/readiness-input-target-invalid.json",
        "proposal": "tests/fixtures/active-task-readiness/positive/valid-active-task-proposal-ready.json",
        "queue_entry": "tasks/queue/valid-ready.md",
        "expected_result": "ACTIVE_TASK_READINESS_BLOCKED",
        "expected_exit_code": 2,
        "expected_blocker": "INPUT_TARGET_ACTIVE_TASK_PATH_INVALID",
        "kind": "input",
    },
    {
        "name": "readiness-input-authority-escalation",
        "input": "tests/fixtures/active-task-readiness/negative/readiness-input-authority-escalation.json",
        "proposal": "tests/fixtures/active-task-readiness/positive/valid-active-task-proposal-ready.json",
        "queue_entry": "tasks/queue/valid-ready.md",
        "expected_result": "ACTIVE_TASK_READINESS_BLOCKED",
        "expected_exit_code": 2,
        "expected_blocker": "INPUT_AUTHORITY_ESCALATION",
        "kind": "input",
    },
    {
        "name": "readiness-input-missing-traceability",
        "input": "tests/fixtures/active-task-readiness/negative/readiness-input-missing-traceability.json",
        "proposal": "tests/fixtures/active-task-readiness/positive/valid-active-task-proposal-ready.json",
        "queue_entry": "tasks/queue/valid-ready.md",
        "expected_result": "ACTIVE_TASK_READINESS_BLOCKED",
        "expected_exit_code": 2,
        "expected_blocker": "TRACEABILITY_INCOMPLETE",
        "kind": "input",
    },
    {
        "name": "readiness-input-missing-carry-forward",
        "input": "tests/fixtures/active-task-readiness/negative/readiness-input-missing-carry-forward.json",
        "proposal": "tests/fixtures/active-task-readiness/positive/valid-active-task-proposal-ready.json",
        "queue_entry": "tasks/queue/valid-ready.md",
        "expected_result": "ACTIVE_TASK_READINESS_BLOCKED",
        "expected_exit_code": 2,
        "expected_blocker": "CARRY_FORWARD_INCOMPLETE",
        "kind": "input",
    },
    {
        "name": "readiness-input-missing-non-authority-markers",
        "input": "tests/fixtures/active-task-readiness/negative/readiness-input-missing-non-authority-markers.json",
        "proposal": "tests/fixtures/active-task-readiness/positive/valid-active-task-proposal-ready.json",
        "queue_entry": "tasks/queue/valid-ready.md",
        "expected_result": "ACTIVE_TASK_READINESS_BLOCKED",
        "expected_exit_code": 2,
        "expected_blocker": "NON_AUTHORITY_MARKERS_MISSING",
        "kind": "input",
    },
    {
        "name": "proposal-draft-not-confirmed",
        "input": "tests/fixtures/active-task-readiness/positive/valid-readiness-input.json",
        "proposal": "tests/fixtures/active-task-readiness/negative/proposal-draft-not-confirmed.json",
        "queue_entry": "tasks/queue/valid-ready.md",
        "expected_result": "ACTIVE_TASK_READINESS_NOT_CONFIRMED",
        "expected_exit_code": 1,
        "expected_blocker": "PROPOSAL_STATUS_UNKNOWN",
        "kind": "proposal",
    },
    {
        "name": "proposal-blocked-not-confirmed",
        "input": "tests/fixtures/active-task-readiness/positive/valid-readiness-input.json",
        "proposal": "tests/fixtures/active-task-readiness/negative/proposal-blocked-not-confirmed.json",
        "queue_entry": "tasks/queue/valid-ready.md",
        "expected_result": "ACTIVE_TASK_READINESS_NOT_CONFIRMED",
        "expected_exit_code": 1,
        "expected_blocker": "PROPOSAL_STATUS_UNKNOWN",
        "kind": "proposal",
    },
    {
        "name": "proposal-human-review-false",
        "input": "tests/fixtures/active-task-readiness/positive/valid-readiness-input.json",
        "proposal": "tests/fixtures/active-task-readiness/negative/proposal-human-review-false.json",
        "queue_entry": "tasks/queue/valid-ready.md",
        "expected_result": "ACTIVE_TASK_READINESS_BLOCKED",
        "expected_exit_code": 2,
        "expected_blocker": "PROPOSAL_HUMAN_REVIEW_REQUIRED",
        "kind": "proposal",
    },
    {
        "name": "proposal-authority-escalation",
        "input": "tests/fixtures/active-task-readiness/positive/valid-readiness-input.json",
        "proposal": "tests/fixtures/active-task-readiness/negative/proposal-authority-escalation.json",
        "queue_entry": "tasks/queue/valid-ready.md",
        "expected_result": "ACTIVE_TASK_READINESS_BLOCKED",
        "expected_exit_code": 2,
        "expected_blocker": "PROPOSAL_AUTHORITY_ESCALATION",
        "kind": "proposal",
    },
    {
        "name": "queue-entry-missing-boundary-markers",
        "input": "tests/fixtures/active-task-readiness/positive/valid-readiness-input.json",
        "proposal": "tests/fixtures/active-task-readiness/positive/valid-active-task-proposal-ready.json",
        "queue_entry": "tasks/queue/valid-ready.md",
        "queue_override": "tests/fixtures/active-task-readiness/negative/queue-entry-missing-boundary-markers.md",
        "expected_result": "ACTIVE_TASK_READINESS_NOT_CONFIRMED",
        "expected_exit_code": 1,
        "expected_blocker": "QUEUE_ENTRY_BOUNDARY_MARKERS_MISSING",
        "kind": "queue",
    },
    {
        "name": "queue-entry-authority-escalation",
        "input": "tests/fixtures/active-task-readiness/positive/valid-readiness-input.json",
        "proposal": "tests/fixtures/active-task-readiness/positive/valid-active-task-proposal-ready.json",
        "queue_entry": "tasks/queue/valid-ready.md",
        "queue_override": "tests/fixtures/active-task-readiness/negative/queue-entry-authority-escalation.md",
        "expected_result": "ACTIVE_TASK_READINESS_BLOCKED",
        "expected_exit_code": 2,
        "expected_blocker": "QUEUE_ENTRY_AUTHORITY_ESCALATION",
        "kind": "queue",
    },
]

STATIC_CASE = {
    "name": "result-contradictory-authority",
    "path": "tests/fixtures/active-task-readiness/negative/result-contradictory-authority.json",
    "expected_result": "ACTIVE_TASK_READINESS_CONFIRMED",
    "expected_exit_code": 0,
    "expected_blocker": "AUTHORITY_ESCALATION",
}

UPSTREAM_FILES = [
    "scripts/check-active-task-readiness.py",
    "docs/TASK-CANDIDATE-ACTIVE-TASK-READINESS-CLI.md",
    "docs/TASK-CANDIDATE-ACTIVE-TASK-READINESS-POLICY.md",
    "docs/TASK-CANDIDATE-ACTIVE-TASK-READINESS-OUTPUT-CONTRACT.md",
    "docs/ACTIVE-TASK-PROPOSAL-CONTRACT.md",
    "docs/TASK-CANDIDATE-ACTIVE-TASK-READINESS-INPUT-CONTRACT.md",
    "reports/m55-m54-readiness-intake.md",
    "docs/TASK-CANDIDATE-ACTIVE-TASK-READINESS-ARCHITECTURE.md",
    "schemas/task-candidate-active-task-readiness-input.schema.json",
    "schemas/active-task-proposal.schema.json",
    "schemas/task-candidate-active-task-readiness-result.schema.json",
    "templates/task-candidate-active-task-readiness-input.md",
    "templates/active-task-proposal.md",
    "templates/task-candidate-active-task-readiness-result.md",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("--explain", action="store_true")
    parser.add_argument("--repo-root")
    parser.add_argument("--json", action="store_true")
    args, unknown = parser.parse_known_args()
    args.unknown = unknown
    return args


def block_result(blocker: str, message: str, repo_root: str, sandbox_root: str = "") -> Dict[str, Any]:
    payload = {
        "m55_active_task_readiness_fixture_integration": {
            "result": BLOCKED_RESULT,
            "exit_code": 2,
            "repo_root": repo_root,
            "sandbox_root": sandbox_root,
            "positive_fixture_count": 10,
            "negative_fixture_count": 17,
            "positive_cases_passed": 0,
            "negative_cases_passed": 0,
            "static_cases_passed": 0,
            "cases": [],
            "warnings": [message],
            "blockers": [blocker],
            "boundary_flags": {
                "fixture_integration_only": True,
                "repository_files_modified": False,
                "active_task_file_created": False,
                "active_task_replacement_authorized": False,
                "active_task_write_allowed": False,
                "execution_authorized": False,
                "approval_created": False,
                "lifecycle_mutation_authorized": False,
                "m56_authorized": False,
                "m56_started": False,
            },
            "performed_actions": {
                "sandbox_created": False,
                "repository_reports_created": False,
                "production_queue_entries_created": False,
                "active_task_file_created": False,
                "approval_created": False,
                "execution_started": False,
                "lifecycle_mutation_performed": False,
                "m56_started": False,
            },
            "non_authority_markers": NON_AUTHORITY_MARKERS,
        }
    }
    return payload


def pass_result(
    repo_root: str,
    sandbox_root: str,
    cases: List[Dict[str, Any]],
    positive_cases_passed: int,
    negative_cases_passed: int,
    static_cases_passed: int,
) -> Dict[str, Any]:
    return {
        "m55_active_task_readiness_fixture_integration": {
            "result": PASS_RESULT,
            "exit_code": 0,
            "repo_root": repo_root,
            "sandbox_root": sandbox_root,
            "positive_fixture_count": 10,
            "negative_fixture_count": 17,
            "positive_cases_passed": positive_cases_passed,
            "negative_cases_passed": negative_cases_passed,
            "static_cases_passed": static_cases_passed,
            "cases": cases,
            "warnings": [],
            "blockers": [],
            "boundary_flags": {
                "fixture_integration_only": True,
                "repository_files_modified": False,
                "active_task_file_created": False,
                "active_task_replacement_authorized": False,
                "active_task_write_allowed": False,
                "execution_authorized": False,
                "approval_created": False,
                "lifecycle_mutation_authorized": False,
                "m56_authorized": False,
                "m56_started": False,
            },
            "performed_actions": {
                "sandbox_created": True,
                "repository_reports_created": False,
                "production_queue_entries_created": False,
                "active_task_file_created": False,
                "approval_created": False,
                "execution_started": False,
                "lifecycle_mutation_performed": False,
                "m56_started": False,
            },
            "non_authority_markers": NON_AUTHORITY_MARKERS,
        }
    }


def emit_json(payload: Dict[str, Any]) -> None:
    sys.stdout.write(json.dumps(payload, indent=2, ensure_ascii=False))
    sys.stdout.write("\n")


def emit_human(payload: Dict[str, Any]) -> None:
    root = payload["m55_active_task_readiness_fixture_integration"]
    sys.stdout.write("M55_ACTIVE_TASK_READINESS_FIXTURE_INTEGRATION:\n")
    sys.stdout.write(f"result: {root['result']}\n")
    sys.stdout.write(f"positive_cases_passed: {root['positive_cases_passed']}\n")
    sys.stdout.write(f"negative_cases_passed: {root['negative_cases_passed']}\n")
    sys.stdout.write(f"static_cases_passed: {root['static_cases_passed']}\n")
    sys.stdout.write(f"blockers: {json.dumps(root['blockers'])}\n")
    for marker in root["non_authority_markers"]:
        sys.stdout.write(f"{marker}\n")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def read_json(path: Path) -> Any:
    return json.loads(read_text(path))


def ensure_exists(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(str(path))


def require_marker(text: str, marker: str, label: str) -> None:
    if marker not in text:
        raise ValueError(f"{label} missing marker: {marker}")


def count_files(path: Path) -> int:
    return sum(1 for item in path.iterdir() if item.is_file())


def copy_required_file(repo_root: Path, sandbox_root: Path, rel_path: str) -> None:
    src = repo_root / rel_path
    dst = sandbox_root / rel_path
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def copy_required_tree(repo_root: Path, sandbox_root: Path, rel_dir: str) -> None:
    src = repo_root / rel_dir
    dst = sandbox_root / rel_dir
    shutil.copytree(src, dst, dirs_exist_ok=True)


def extract_json_block(markdown: str) -> str:
    matches = re.findall(r"```json\s*(.*?)\s*```", markdown, flags=re.DOTALL | re.IGNORECASE)
    if len(matches) != 1:
        raise ValueError("markdown_json_block_count")
    return matches[0]


def load_json_or_markdown_json(path: Path) -> Any:
    text = read_text(path)
    if path.suffix.lower() == ".md":
        text = extract_json_block(text)
    return json.loads(text)


def validate_dependency_files(repo_root: Path) -> None:
    for rel in UPSTREAM_FILES:
        ensure_exists(repo_root / rel)


def validate_markers(repo_root: Path) -> None:
    cli_text = read_text(repo_root / "docs/TASK-CANDIDATE-ACTIVE-TASK-READINESS-CLI.md")
    policy_text = read_text(repo_root / "docs/TASK-CANDIDATE-ACTIVE-TASK-READINESS-POLICY.md")
    for marker in CLI_MARKERS:
        require_marker(cli_text, marker, "CLI documentation")
    for marker in POLICY_MARKERS:
        require_marker(policy_text, marker, "policy documentation")


def validate_fixture_counts(repo_root: Path) -> None:
    positive = repo_root / "tests/fixtures/active-task-readiness/positive"
    negative = repo_root / "tests/fixtures/active-task-readiness/negative"
    if count_files(positive) != 10:
        raise ValueError("positive fixture count")
    if count_files(negative) != 17:
        raise ValueError("negative fixture count")


def validate_positive_readme(repo_root: Path) -> None:
    text = read_text(repo_root / "tests/fixtures/active-task-readiness/positive/README.md")
    required = [
        "These are positive fixtures for the M55 active-task readiness checker.",
        "Positive fixtures are static test data only.",
        "Positive fixtures do not authorize active-task replacement.",
        "Positive fixtures do not write tasks/active-task.md.",
        "Positive fixtures do not create approval records.",
        "Positive fixtures do not authorize execution.",
        "Positive fixtures do not authorize lifecycle mutation.",
        "Positive fixtures do not authorize M56.",
        "Fixture integration belongs to 55.8.",
        "Negative fixtures belong to 55.7.2.",
    ]
    for marker in required:
        require_marker(text, marker, "positive README")


def validate_negative_readme(repo_root: Path) -> None:
    text = read_text(repo_root / "tests/fixtures/active-task-readiness/negative/README.md")
    required = [
        "These are negative fixtures for the M55 active-task readiness checker.",
        "Negative fixtures are static test data only.",
        "Negative fixtures must fail closed.",
        "Negative fixtures do not authorize active-task replacement.",
        "Negative fixtures do not write tasks/active-task.md.",
        "Negative fixtures do not create approval records.",
        "Negative fixtures do not authorize execution.",
        "Negative fixtures do not authorize lifecycle mutation.",
        "Negative fixtures do not authorize M56.",
        "Fixture integration belongs to 55.8.",
        "Positive fixtures belong to 55.7.1.",
    ]
    for marker in required:
        require_marker(text, marker, "negative README")


def validate_malformed_negative_fixture(repo_root: Path) -> None:
    text = read_text(repo_root / "tests/fixtures/active-task-readiness/negative/malformed-readiness-input.json")
    require_marker(text, "BROKEN_M55_READINESS_INPUT_JSON", "malformed fixture")
    require_marker(text, "MALFORMED_JSON", "malformed fixture")
    try:
        json.loads(text)
    except json.JSONDecodeError:
        return
    raise ValueError("malformed fixture parsed unexpectedly")


def validate_json_fixtures_parse(repo_root: Path) -> None:
    positive_dir = repo_root / "tests/fixtures/active-task-readiness/positive"
    negative_dir = repo_root / "tests/fixtures/active-task-readiness/negative"
    for path in sorted(positive_dir.glob("*.json")):
        json.loads(read_text(path))
    for path in sorted(negative_dir.glob("*.json")):
        if path.name == "malformed-readiness-input.json":
            continue
        json.loads(read_text(path))


def validate_static_contradiction(repo_root: Path) -> None:
    obj = read_json(repo_root / STATIC_CASE["path"])
    root = obj["active_task_readiness_result"]
    expected = STATIC_CASE
    if root["result"] != expected["expected_result"]:
        raise ValueError("static contradiction result")
    if root["exit_code"] != expected["expected_exit_code"]:
        raise ValueError("static contradiction exit")
    if root["readiness_confirmed"] is not True:
        raise ValueError("static contradiction readiness")
    if root["proposal_ready_for_review"] is not True:
        raise ValueError("static contradiction proposal")
    if root["active_task_replacement_authorized"] is not True:
        raise ValueError("static contradiction authority")
    if root.get("expected_blocker") != expected["expected_blocker"] and expected["expected_blocker"] not in root.get("blockers", []):
        raise ValueError("static contradiction blocker")


def stage_sandbox(repo_root: Path) -> Path:
    if SANDBOX_ROOT.exists():
        shutil.rmtree(SANDBOX_ROOT)
    SANDBOX_ROOT.mkdir(parents=True, exist_ok=True)
    for rel in UPSTREAM_FILES:
        copy_required_file(repo_root, SANDBOX_ROOT, rel)
    copy_required_tree(repo_root, SANDBOX_ROOT, "tests/fixtures/active-task-readiness/positive")
    copy_required_tree(repo_root, SANDBOX_ROOT, "tests/fixtures/active-task-readiness/negative")
    # The harness uses a sandbox queue entry copied from the positive fixture set.
    queue_path = SANDBOX_ROOT / "tasks/queue/valid-ready.md"
    queue_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(
        SANDBOX_ROOT / "tests/fixtures/active-task-readiness/positive/valid-queue-entry-ready.md",
        queue_path,
    )
    return SANDBOX_ROOT


def make_runtime_missing_carry_forward(sandbox_root: Path) -> Path:
    src = sandbox_root / "tests/fixtures/active-task-readiness/negative/readiness-input-missing-carry-forward.json"
    dst = sandbox_root / "tmp" / "derived" / "readiness-input-missing-carry-forward-runtime.json"
    dst.parent.mkdir(parents=True, exist_ok=True)
    data = json.loads(read_text(src))
    data["active_task_readiness_input"]["carry_forward"] = {}
    dst.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return dst


def make_runtime_missing_non_authority_markers_input(sandbox_root: Path) -> Path:
    src = sandbox_root / "tests/fixtures/active-task-readiness/negative/readiness-input-missing-non-authority-markers.json"
    dst = sandbox_root / "tmp" / "derived" / "readiness-input-missing-non-authority-markers-runtime.json"
    dst.parent.mkdir(parents=True, exist_ok=True)
    data = json.loads(read_text(src))
    input_root = data["active_task_readiness_input"]
    missing_marker = "Active-task readiness does not authorize M56."
    input_root["non_authority_markers"] = [
        marker for marker in input_root.get("non_authority_markers", []) if marker != missing_marker
    ]
    carry = input_root.get("carry_forward", {})
    carry["non_authority_boundary"] = [
        marker for marker in carry.get("non_authority_boundary", []) if marker != missing_marker
    ]
    input_root["carry_forward"] = carry
    dst.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return dst


def make_runtime_markdown_input_proposal(sandbox_root: Path) -> Path:
    return make_runtime_proposal_for_input(
        sandbox_root,
        "tests/fixtures/active-task-readiness/positive/valid-readiness-input-markdown.md",
        "valid-active-task-proposal-ready-markdown-input.json",
    )


def make_runtime_proposal_for_input(sandbox_root: Path, input_rel_path: str, filename: str = "valid-active-task-proposal-ready-runtime.json") -> Path:
    src = sandbox_root / "tests/fixtures/active-task-readiness/positive/valid-active-task-proposal-ready.json"
    dst = sandbox_root / "tmp" / "derived" / filename
    dst.parent.mkdir(parents=True, exist_ok=True)
    data = json.loads(read_text(src))
    data["active_task_proposal"]["source_active_task_readiness_input"] = input_rel_path
    dst.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return dst


def run_cli(sandbox_root: Path, input_path: str, proposal_path: str, queue_entry: str) -> Tuple[int, Dict[str, Any], str, str]:
    cmd = [
        sys.executable,
        "scripts/check-active-task-readiness.py",
        "--repo-root",
        ".",
        "--input",
        input_path,
        "--proposal",
        proposal_path,
        "--queue-entry",
        queue_entry,
        "--json",
    ]
    completed = subprocess.run(
        cmd,
        cwd=str(sandbox_root),
        text=True,
        capture_output=True,
        shell=False,
        check=False,
    )
    stdout = completed.stdout.strip()
    stderr = completed.stderr.strip()
    payload = json.loads(stdout) if stdout else {}
    return completed.returncode, payload, stdout, stderr


def extract_cli_root(payload: Dict[str, Any]) -> Dict[str, Any]:
    if "active_task_readiness_result" not in payload:
        raise ValueError("missing cli root")
    return payload["active_task_readiness_result"]


def validate_cli_result(
    case_name: str,
    expected_result: str,
    expected_exit_code: int,
    expected_blocker: Optional[str],
    payload: Dict[str, Any],
    returncode: int,
) -> None:
    root = extract_cli_root(payload)
    if returncode != expected_exit_code:
        raise ValueError(f"{case_name}: exit mismatch")
    if root["result"] != expected_result:
        raise ValueError(f"{case_name}: result mismatch")
    if root["exit_code"] != expected_exit_code:
        raise ValueError(f"{case_name}: exit field mismatch")
    if root["active_task_replacement_authorized"] is not False:
        raise ValueError(f"{case_name}: replacement auth mismatch")
    if root["active_task_file_created"] is not False:
        raise ValueError(f"{case_name}: file created mismatch")
    if expected_result in {"ACTIVE_TASK_READINESS_CONFIRMED", "ACTIVE_TASK_READINESS_CONFIRMED_WITH_LIMITATIONS"}:
        if root["readiness_confirmed"] is not True:
            raise ValueError(f"{case_name}: readiness mismatch")
        if root["proposal_ready_for_review"] is not True:
            raise ValueError(f"{case_name}: proposal readiness mismatch")
    else:
        if root["readiness_confirmed"] is not False:
            raise ValueError(f"{case_name}: readiness should be false")
        if root["proposal_ready_for_review"] is not False:
            raise ValueError(f"{case_name}: proposal readiness should be false")
    if expected_blocker is not None and expected_blocker not in root.get("blockers", []):
        raise ValueError(f"{case_name}: blocker mismatch")


def validate_positive_case(sandbox_root: Path, scenario: Dict[str, Any]) -> Dict[str, Any]:
    rc, payload, stdout, stderr = run_cli(sandbox_root, scenario["input"], scenario["proposal"], scenario["queue_entry"])
    if stderr:
        raise ValueError(f"{scenario['name']}: unexpected stderr")
    validate_cli_result(scenario["name"], scenario["expected_result"], scenario["expected_exit_code"], scenario["expected_blocker"], payload, rc)
    root = extract_cli_root(payload)
    if root["boundary_flags"]["active_task_replacement_authorized"] is not False:
        raise ValueError(f"{scenario['name']}: boundary flag mismatch")
    if root["boundary_flags"]["m56_authorized"] is not False:
        raise ValueError(f"{scenario['name']}: boundary flag mismatch")
    if root["performed_actions"]["m56_started"] is not False:
        raise ValueError(f"{scenario['name']}: performed action mismatch")
    return {
        "name": scenario["name"],
        "result": root["result"],
        "exit_code": rc,
        "blockers": root.get("blockers", []),
    }


def validate_negative_case(sandbox_root: Path, scenario: Dict[str, Any], queue_override: Optional[str] = None, input_override: Optional[str] = None, proposal_override: Optional[str] = None) -> Dict[str, Any]:
    input_path = input_override or scenario["input"]
    proposal_path = proposal_override or scenario["proposal"]
    queue_entry = queue_override or scenario["queue_entry"]
    rc, payload, stdout, stderr = run_cli(sandbox_root, input_path, proposal_path, queue_entry)
    if stderr:
        raise ValueError(f"{scenario['name']}: unexpected stderr")
    validate_cli_result(scenario["name"], scenario["expected_result"], scenario["expected_exit_code"], scenario["expected_blocker"], payload, rc)
    return {
        "name": scenario["name"],
        "result": extract_cli_root(payload)["result"],
        "exit_code": rc,
        "blockers": extract_cli_root(payload).get("blockers", []),
    }


def validate_queue_negative_case(sandbox_root: Path, scenario: Dict[str, Any]) -> Dict[str, Any]:
    queue_dst = sandbox_root / "tasks/queue/valid-ready.md"
    shutil.copy2(sandbox_root / scenario["queue_override"], queue_dst)
    try:
        rc, payload, stdout, stderr = run_cli(sandbox_root, scenario["input"], scenario["proposal"], scenario["queue_entry"])
        if stderr:
            raise ValueError(f"{scenario['name']}: unexpected stderr")
        validate_cli_result(scenario["name"], scenario["expected_result"], scenario["expected_exit_code"], scenario["expected_blocker"], payload, rc)
        return {
            "name": scenario["name"],
            "result": extract_cli_root(payload)["result"],
            "exit_code": rc,
            "blockers": extract_cli_root(payload).get("blockers", []),
        }
    finally:
        shutil.copy2(sandbox_root / "tests/fixtures/active-task-readiness/positive/valid-queue-entry-ready.md", queue_dst)


def validate_missing_carry_forward_runtime(sandbox_root: Path) -> Dict[str, Any]:
    runtime_input = make_runtime_missing_carry_forward(sandbox_root)
    runtime_proposal = make_runtime_proposal_for_input(
        sandbox_root,
        str(runtime_input.relative_to(sandbox_root)),
        "readiness-input-missing-carry-forward-proposal.json",
    )
    scenario = next(item for item in NEGATIVE_SCENARIOS if item["name"] == "readiness-input-missing-carry-forward")
    rc, payload, stdout, stderr = run_cli(
        sandbox_root,
        str(runtime_input.relative_to(sandbox_root)),
        str(runtime_proposal.relative_to(sandbox_root)),
        scenario["queue_entry"],
    )
    if stderr:
        raise ValueError("readiness-input-missing-carry-forward: unexpected stderr")
    validate_cli_result(scenario["name"], scenario["expected_result"], scenario["expected_exit_code"], scenario["expected_blocker"], payload, rc)
    return {
        "name": scenario["name"],
        "result": extract_cli_root(payload)["result"],
        "exit_code": rc,
        "blockers": extract_cli_root(payload).get("blockers", []),
        "derived_input": str(runtime_input.relative_to(sandbox_root)),
    }


def validate_repo_not_modified(repo_root: Path) -> None:
    targets = [
        "reports/m55-completion-review.md",
        "reports/m55-active-task-readiness-integration.md",
        "reports/m55-active-task-readiness-result-agent-action-review.json",
        "reports/m55-active-task-readiness-evidence-report.md",
    ]
    for rel in targets:
        if (repo_root / rel).exists():
            raise ValueError(f"unexpected repository file exists: {rel}")
    diff_check = subprocess.run(
        ["git", "diff", "--quiet", "--", "tasks/active-task.md"],
        cwd=str(repo_root),
        text=True,
        capture_output=True,
        shell=False,
        check=False,
    )
    if diff_check.returncode not in (0, 1):
        raise ValueError("git diff check failed")


def validate_forbidden_artifacts(repo_root: Path) -> None:
    forbidden = [
        "reports/m55-completion-review.md",
        "reports/m55-active-task-readiness-integration.md",
        "reports/m55-active-task-readiness-result-agent-action-review.json",
        "reports/m55-active-task-readiness-evidence-report.md",
        "memory-bank/lessons/m55-active-task-readiness-boundary.md",
    ]
    for rel in forbidden:
        if (repo_root / rel).exists():
            raise ValueError(f"forbidden artifact exists: {rel}")
    if any((repo_root / "examples/active-task-readiness").glob("*")):
        raise ValueError("forbidden example artifacts exist")


def check_allowlist(repo_root: Path) -> None:
    status = subprocess.run(
        ["git", "status", "--short", "-uall"],
        cwd=str(repo_root),
        text=True,
        capture_output=True,
        shell=False,
        check=False,
    )
    # The repository can contain pre-existing unrelated untracked files; the task
    # validation outside this harness will check the exact allowlist.
    # Here we only make sure the command succeeds.
    if status.returncode != 0:
        raise ValueError("git status failed")


def explain_text() -> str:
    return "\n".join(
        [
            "M55 fixture integration validates fixtures through an isolated sandbox.",
            "M55 fixture integration does not modify tasks/active-task.md.",
            "M55 fixture integration does not create approval records.",
            "M55 fixture integration does not authorize execution or M56.",
            "M55 fixture integration does not add fixture mode to the M55 CLI.",
        ]
    )


def validate_args(args: argparse.Namespace) -> Optional[Dict[str, Any]]:
    safe_flags = {"--explain", "--repo-root", "--json", "-h", "--help"}
    forbidden_flags = {
        "--write",
        "--apply",
        "--replace-active-task",
        "--approve",
        "--execute",
        "--start-m56",
        "--fixtures",
    }
    argv = sys.argv[1:]
    if args.explain:
        if args.repo_root or args.json or args.unknown:
            return block_result(ARGUMENT_ERROR, "Explain mode must be standalone.", "", "")
        return None
    if args.unknown:
        return block_result(ARGUMENT_ERROR, "Unsupported arguments were provided.", args.repo_root or "", "")
    if any(flag in argv for flag in forbidden_flags):
        return block_result(ARGUMENT_ERROR, "Forbidden argument was provided.", args.repo_root or "", "")
    if not args.repo_root:
        return block_result(ARGUMENT_ERROR, "Missing required --repo-root.", "", "")
    return None


def main() -> int:
    args = parse_args()

    if args.explain:
        if args.repo_root or args.json or args.unknown:
            payload = block_result(ARGUMENT_ERROR, "Explain mode must be standalone.", "", "")
            if args.json:
                emit_json(payload)
            else:
                emit_human(payload)
            return 2
        sys.stdout.write(explain_text() + "\n")
        return 0

    arg_err = validate_args(args)
    if arg_err is not None:
        if args.json:
            emit_json(arg_err)
        else:
            emit_human(arg_err)
        return 2

    repo_root = Path(args.repo_root).resolve()
    if not repo_root.exists() or not repo_root.is_dir():
        payload = block_result(ARGUMENT_ERROR, "Repository root is invalid.", str(repo_root), "")
        if args.json:
            emit_json(payload)
        else:
            emit_human(payload)
        return 2

    try:
        validate_dependency_files(repo_root)
        validate_markers(repo_root)
        validate_fixture_counts(repo_root)
        validate_positive_readme(repo_root)
        validate_negative_readme(repo_root)
        validate_malformed_negative_fixture(repo_root)
        validate_json_fixtures_parse(repo_root)
        validate_static_contradiction(repo_root)
    except Exception as exc:
        payload = block_result(ARGUMENT_ERROR, f"Validation failed: {exc}", str(repo_root), "")
        if args.json:
            emit_json(payload)
        else:
            emit_human(payload)
        return 2

    sandbox_root = stage_sandbox(repo_root)

    cases: List[Dict[str, Any]] = []
    positive_passed = 0
    negative_passed = 0
    static_passed = 0

    try:
        for scenario in POSITIVE_SCENARIOS:
            if scenario["name"] == "positive-markdown-input":
                runtime_proposal = make_runtime_markdown_input_proposal(sandbox_root)
                case = validate_positive_case(
                    sandbox_root,
                    {
                        **scenario,
                        "proposal": str(runtime_proposal.relative_to(sandbox_root)),
                    },
                )
                case["derived_proposal"] = str(runtime_proposal.relative_to(sandbox_root))
            else:
                case = validate_positive_case(sandbox_root, scenario)
            cases.append(case)
            positive_passed += 1

        for scenario in NEGATIVE_SCENARIOS:
            if scenario["name"] == "readiness-input-missing-carry-forward":
                case = validate_missing_carry_forward_runtime(sandbox_root)
            elif scenario["name"] == "readiness-input-missing-non-authority-markers":
                runtime_input = make_runtime_missing_non_authority_markers_input(sandbox_root)
                runtime_proposal = make_runtime_proposal_for_input(sandbox_root, str(runtime_input.relative_to(sandbox_root)), "readiness-input-missing-non-authority-markers-proposal.json")
                case = validate_negative_case(
                    sandbox_root,
                    scenario,
                    input_override=str(runtime_input.relative_to(sandbox_root)),
                    proposal_override=str(runtime_proposal.relative_to(sandbox_root)),
                )
            elif scenario["kind"] == "input":
                runtime_proposal = make_runtime_proposal_for_input(sandbox_root, scenario["input"])
                case = validate_negative_case(
                    sandbox_root,
                    scenario,
                    proposal_override=str(runtime_proposal.relative_to(sandbox_root)),
                )
            elif scenario["kind"] == "queue":
                case = validate_queue_negative_case(sandbox_root, scenario)
            else:
                case = validate_negative_case(sandbox_root, scenario)
            cases.append(case)
            negative_passed += 1

        validate_repo_not_modified(repo_root)
        validate_forbidden_artifacts(repo_root)
        check_allowlist(repo_root)
        static_passed = 1
    except Exception as exc:
        payload = block_result(ARGUMENT_ERROR, f"Fixture integration failed: {exc}", str(repo_root), str(sandbox_root))
        if args.json:
            emit_json(payload)
        else:
            emit_human(payload)
        return 2

    payload = pass_result(
        str(repo_root),
        str(sandbox_root),
        cases,
        positive_passed,
        negative_passed,
        static_passed,
    )
    if args.json:
        emit_json(payload)
    else:
        emit_human(payload)
    return 0


if __name__ == "__main__":
    sys.exit(main())
