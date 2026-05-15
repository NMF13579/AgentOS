#!/usr/bin/env python3

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

PASS = "PASS"
FAIL = "FAIL"
WARN = "WARN"
ERROR = "ERROR"
NOT_RUN = "NOT_RUN"

CONTROL_READY = "CONTROL_READY"
READY_WITH_WARNINGS = "READY_WITH_WARNINGS"
NEEDS_REVIEW = "NEEDS_REVIEW"
NOT_READY = "NOT_READY"

RESULT_TO_EXIT = {
    PASS: 0,
    FAIL: 1,
    WARN: 2,
    ERROR: 3,
    NOT_RUN: 3,
}

HONEST_PASS_OK = "HONEST_PASS_OK"
HONEST_PASS_VIOLATION = "HONEST_PASS_VIOLATION"
HONEST_PASS_NEEDS_REVIEW = "HONEST_PASS_NEEDS_REVIEW"

HONEST_PRIORITY = {
    HONEST_PASS_OK: 0,
    HONEST_PASS_NEEDS_REVIEW: 1,
    HONEST_PASS_VIOLATION: 2,
}

INTEGRITY_OK = "INTEGRITY_OK"
INTEGRITY_WARNING = "INTEGRITY_WARNING"
INTEGRITY_VIOLATION = "INTEGRITY_VIOLATION"
INTEGRITY_NEEDS_REVIEW = "INTEGRITY_NEEDS_REVIEW"
INTEGRITY_BLOCKED = "INTEGRITY_BLOCKED"
INTEGRITY_REGRESSION_OK = "INTEGRITY_REGRESSION_OK"
INTEGRITY_REGRESSION_FAILED = "INTEGRITY_REGRESSION_FAILED"
INTEGRITY_REGRESSION_NEEDS_REVIEW = "INTEGRITY_REGRESSION_NEEDS_REVIEW"
INTEGRITY_REGRESSION_BLOCKED = "INTEGRITY_REGRESSION_BLOCKED"

INTEGRITY_PRIORITY = {
    INTEGRITY_OK: 0,
    INTEGRITY_WARNING: 1,
    INTEGRITY_NEEDS_REVIEW: 2,
    INTEGRITY_BLOCKED: 3,
    INTEGRITY_VIOLATION: 4,
}

INTEGRITY_EXIT = {
    INTEGRITY_OK: 0,
    INTEGRITY_WARNING: 0,
    INTEGRITY_VIOLATION: 1,
    INTEGRITY_NEEDS_REVIEW: 1,
    INTEGRITY_BLOCKED: 1,
}

SOURCE_TO_INTEGRITY = {
    "HONEST_PASS_OK": INTEGRITY_OK,
    "HONEST_PASS_VIOLATION": INTEGRITY_VIOLATION,
    "HONEST_PASS_NEEDS_REVIEW": INTEGRITY_NEEDS_REVIEW,
    "HONEST_PASS_FIXTURES_OK": INTEGRITY_OK,
    "HONEST_PASS_FIXTURES_FAILED": INTEGRITY_VIOLATION,
    "HONEST_PASS_FIXTURES_NEEDS_REVIEW": INTEGRITY_NEEDS_REVIEW,
    "BYPASS_TEST_PASS": INTEGRITY_OK,
    "BYPASS_TEST_PASS_WITH_WARNINGS": INTEGRITY_WARNING,
    "BYPASS_TEST_FAIL": INTEGRITY_VIOLATION,
    "BYPASS_TEST_NEEDS_REVIEW": INTEGRITY_NEEDS_REVIEW,
    "VALIDATOR_AUTHORITY_OK": INTEGRITY_OK,
    "VALIDATOR_AUTHORITY_VIOLATION": INTEGRITY_VIOLATION,
    "VALIDATOR_AUTHORITY_NEEDS_REVIEW": INTEGRITY_NEEDS_REVIEW,
    "ROLE_SEPARATION_OK": INTEGRITY_OK,
    "ROLE_SEPARATION_VIOLATION": INTEGRITY_VIOLATION,
    "ROLE_SEPARATION_NEEDS_REVIEW": INTEGRITY_NEEDS_REVIEW,
    "EVIDENCE_IMMUTABILITY_OK": INTEGRITY_OK,
    "EVIDENCE_IMMUTABILITY_VIOLATION": INTEGRITY_VIOLATION,
    "EVIDENCE_IMMUTABILITY_NEEDS_REVIEW": INTEGRITY_NEEDS_REVIEW,
    "EVIDENCE_AMENDMENT_OK": INTEGRITY_OK,
    "EVIDENCE_AMENDMENT_VIOLATION": INTEGRITY_VIOLATION,
    "EVIDENCE_AMENDMENT_NEEDS_REVIEW": INTEGRITY_NEEDS_REVIEW,
}

INTEGRITY_EXPLANATION_MAP = {
    INTEGRITY_OK: {
        "meaning": "All executed integrity checks returned OK.",
        "clean_pass": True,
        "next_safe_action": "Continue to normal validation or maintainer review.",
        "does_not_mean": "INTEGRITY_OK is not human approval.",
    },
    INTEGRITY_WARNING: {
        "meaning": "Checks completed but at least one warning or controlled smoke finding exists.",
        "clean_pass": False,
        "next_safe_action": "Review warnings and limitations before claiming completion.",
        "does_not_mean": "INTEGRITY_WARNING is not clean PASS.",
    },
    INTEGRITY_VIOLATION: {
        "meaning": "At least one check found a blocking integrity violation.",
        "clean_pass": False,
        "next_safe_action": "Stop clean completion, inspect failure class, correct cause, then rerun.",
        "does_not_mean": "A violation does not authorize any state transition.",
    },
    INTEGRITY_NEEDS_REVIEW: {
        "meaning": "Checker could not determine integrity safely.",
        "clean_pass": False,
        "next_safe_action": "Require maintainer or human review before proceeding.",
        "does_not_mean": "Needs-review is not a pass result.",
    },
    INTEGRITY_BLOCKED: {
        "meaning": "Integrity command could not safely complete due to missing dependency, invalid registry, unparseable output, or unsafe state.",
        "clean_pass": False,
        "next_safe_action": "Fix blocked precondition or dependency before rerun.",
        "does_not_mean": "Blocked execution does not provide integrity evidence.",
    },
}

INTEGRITY_STRICT_FIXTURES_JSON_CMD_TEXT = "integrity --strict --fixtures --json"
INTEGRITY_REGRESSION_JSON_CMD_TEXT = "integrity-regression --json --skip-all-strict-check"

PRIORITY = {
    PASS: 0,
    WARN: 1,
    NOT_RUN: 2,
    FAIL: 3,
    ERROR: 4,
}


def generated_at_utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def summary_tail(stdout_text, stderr_text):
    combined = f"{stdout_text}{stderr_text}"
    return combined[-500:]


def parse_cli(argv):
    parser = argparse.ArgumentParser(prog="agentos-validate.py", allow_abbrev=False)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--summary", action="store_true")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--fixtures", action="store_true")
    parser.add_argument("--explain-results", action="store_true")
    parser.add_argument("--explain-result")
    parser.add_argument("--trace")
    parser.add_argument("--binding")
    parser.add_argument("--private-evaluator")
    parser.add_argument("--canary")
    parser.add_argument("--input")
    parser.add_argument("--registry")
    parser.add_argument("--list-fixtures", action="store_true")
    parser.add_argument("--self-test-fixtures", action="store_true")
    parser.add_argument("--skip-all-strict-check", action="store_true")
    parser.add_argument("--fixture-root")
    parser.add_argument(
        "command",
        nargs="?",
        choices=[
            "scope",
            "scope-fixtures",
            "execution-audit",
            "readiness-assertions",
            "single-role",
            "honest-pass",
            "runtime-bypass-smoke",
            "validator-authority",
            "role-separation",
            "evidence-immutability",
            "evidence-amendments",
            "integrity",
            "integrity-regression",
            "all",
        ],
    )
    parser.add_argument("--task")
    args = parser.parse_args(argv)

    if args.command is None:
        args.command = "all"
    if args.command == "scope" and not args.task:
        raise ValueError("scope requires --task")
    if args.command in ["scope-fixtures", "execution-audit"] and args.task:
        raise ValueError("--task is only allowed with scope")
    if args.command == "all" and args.task:
        raise ValueError("--task is not supported with all")

    hp_flags = any([args.fixtures, args.trace, args.binding, args.private_evaluator, args.canary])
    if args.command not in ["honest-pass", "integrity"] and hp_flags:
        raise ValueError("honest-pass flags are only valid with honest-pass/integrity command")

    if args.command in [
        "validator-authority",
        "role-separation",
        "evidence-immutability",
        "evidence-amendments",
    ] and any([args.trace, args.binding, args.private_evaluator, args.canary]):
        raise ValueError("trace/binding/private-evaluator/canary flags are not valid for this command")

    if args.summary and args.command != "integrity":
        raise ValueError("--summary is only valid with integrity command")
    if (args.explain_results or args.explain_result) and args.command != "integrity":
        raise ValueError("--explain-results/--explain-result are only valid with integrity command")
    if args.explain_results and args.explain_result:
        raise ValueError("Use either --explain-results or --explain-result, not both.")
    if args.self_test_fixtures and args.command != "integrity-regression":
        raise ValueError("--self-test-fixtures is only valid with integrity-regression command")
    if args.skip_all_strict_check and args.command != "integrity-regression":
        raise ValueError("--skip-all-strict-check is only valid with integrity-regression command")
    if args.list_fixtures and args.command != "integrity":
        raise ValueError("--list-fixtures is only valid with integrity command")
    if args.registry and args.command not in ["integrity", "integrity-regression"]:
        raise ValueError("--registry is only valid with integrity/integrity-regression command")
    if args.fixture_root and args.command != "integrity-regression":
        raise ValueError("--fixture-root is only valid with integrity-regression command")

    return args


def run_child(repo_root, command_name, command_list):
    child_script = command_list[1] if len(command_list) > 1 else ""
    if child_script and child_script.endswith(".py"):
        if not (repo_root / child_script).is_file():
            return {
                "name": command_name,
                "command": " ".join(command_list),
                "exit_code": 3,
                "result": ERROR,
                "output_summary": f"missing child script: {child_script}",
                "human_action_required": True,
                "ran": True,
            }

    try:
        proc = subprocess.run(
            command_list,
            cwd=str(repo_root),
            capture_output=True,
            text=True,
        )
    except Exception as exc:
        return {
            "name": command_name,
            "command": " ".join(command_list),
            "exit_code": 3,
            "result": ERROR,
            "output_summary": f"subprocess failure: {exc}",
            "human_action_required": True,
            "ran": True,
        }

    mapped_result = {
        0: PASS,
        1: FAIL,
        2: WARN,
        3: ERROR,
    }.get(proc.returncode, ERROR)

    out_sum = summary_tail(proc.stdout, proc.stderr)

    if command_name == "execution-audit":
        combined = f"{proc.stdout}\n{proc.stderr}"
        mapped_from_output = None
        if CONTROL_READY in combined:
            mapped_from_output = PASS
        elif READY_WITH_WARNINGS in combined:
            mapped_from_output = WARN
        elif NEEDS_REVIEW in combined:
            mapped_from_output = FAIL
        elif NOT_READY in combined:
            mapped_from_output = FAIL

        if mapped_from_output is not None:
            if mapped_from_output != mapped_result:
                out_sum = (out_sum + "\n" + "conflict: output mapping overrides child exit mapping")[-500:]
            mapped_result = mapped_from_output
        elif proc.returncode not in [0, 1, 2, 3]:
            mapped_result = ERROR

    return {
        "name": command_name,
        "command": " ".join(command_list),
        "exit_code": RESULT_TO_EXIT[mapped_result],
        "result": mapped_result,
        "output_summary": out_sum,
        "human_action_required": mapped_result in [FAIL, ERROR, NOT_RUN],
        "ran": True,
    }


def not_run_check(name, command_text, reason):
    return {
        "name": name,
        "command": command_text,
        "exit_code": 3,
        "result": NOT_RUN,
        "output_summary": reason,
        "human_action_required": True,
        "ran": False,
    }


def aggregate(checks):
    overall = PASS
    for item in checks:
        if PRIORITY[item["result"]] > PRIORITY[overall]:
            overall = item["result"]

    if checks and all(item["result"] == NOT_RUN for item in checks):
        overall = NOT_RUN

    commands_run = sum(1 for item in checks if item.get("ran", False))
    commands_not_run = sum(1 for item in checks if item["result"] == NOT_RUN)
    commands_passed = sum(1 for item in checks if item["result"] == PASS)
    commands_warned = sum(1 for item in checks if item["result"] == WARN)
    commands_failed = sum(1 for item in checks if item["result"] in [FAIL, ERROR])

    any_blocking = any(item["result"] in [FAIL, ERROR, NOT_RUN] for item in checks)
    if overall == WARN and not any_blocking:
        human_action_required = False
    elif overall == PASS:
        human_action_required = False
    else:
        human_action_required = any_blocking

    return {
        "result": overall,
        "commands_run": commands_run,
        "commands_passed": commands_passed,
        "commands_failed": commands_failed,
        "commands_warned": commands_warned,
        "commands_not_run": commands_not_run,
        "human_action_required": human_action_required,
        "checks": [
            {
                "name": item["name"],
                "command": item["command"],
                "exit_code": item["exit_code"],
                "result": item["result"],
                "output_summary": item["output_summary"],
                "human_action_required": item["human_action_required"],
            }
            for item in checks
        ],
    }


def run_scope(repo_root, task_path):
    cmd = [sys.executable, "scripts/check-scope-compliance.py", "--task", task_path]
    return [run_child(repo_root, "scope", cmd)]


def run_scope_fixtures(repo_root):
    cmd = [sys.executable, "scripts/test-scope-compliance-fixtures.py"]
    return [run_child(repo_root, "scope-fixtures", cmd)]


def run_execution_audit(repo_root):
    cmd = [sys.executable, "scripts/audit-execution-control.py"]
    return [run_child(repo_root, "execution-audit", cmd)]


def run_readiness_assertions(repo_root):
    cmd = [sys.executable, "scripts/check-readiness-assertions.py"]
    return [run_child(repo_root, "readiness-assertions", cmd)]


def run_single_role(repo_root, task_path):
    cmd = [sys.executable, "scripts/check-single-role-execution.py", task_path, "--strict"]
    return [run_child(repo_root, "single-role", cmd)]


def run_all(repo_root):
    checks = []
    default_task = repo_root / "tasks/active-task.md"

    if default_task.is_file():
        checks.extend(run_scope(repo_root, "tasks/active-task.md"))
    else:
        checks.append(
            not_run_check(
                "scope",
                f"{sys.executable} scripts/check-scope-compliance.py --task tasks/active-task.md",
                "default task file is missing",
            )
        )

    checks.extend(run_scope_fixtures(repo_root))
    checks.extend(run_execution_audit(repo_root))
    checks.extend(run_readiness_assertions(repo_root))
    checks.extend(run_single_role(repo_root, "tasks/active-task.md"))
    return checks


def _load_json_text(text):
    try:
        return json.loads(text)
    except Exception:
        return None


def _honest_exit(result):
    return 0 if result == HONEST_PASS_OK else 1


def run_honest_pass(repo_root, args):
    details = []
    mode = "artifacts"

    if args.fixtures:
        mode = "fixtures"
        proc = subprocess.run(
            [sys.executable, "scripts/test-honest-pass-fixtures.py", "--json"],
            cwd=str(repo_root),
            capture_output=True,
            text=True,
            check=False,
        )
        payload = _load_json_text(proc.stdout.strip())
        if payload is None or "result" not in payload:
            result = HONEST_PASS_VIOLATION
            failure_class = "TRACE_INVALID"
            message = "Failed to parse fixture runner JSON."
            fixture_runner = None
        else:
            fixture_runner = payload
            fr = payload.get("result")
            if fr == "HONEST_PASS_FIXTURES_OK":
                result = HONEST_PASS_OK
            elif fr == "HONEST_PASS_FIXTURES_NEEDS_REVIEW":
                result = HONEST_PASS_NEEDS_REVIEW
            elif fr == "HONEST_PASS_FIXTURES_FAILED":
                result = HONEST_PASS_VIOLATION
            else:
                result = HONEST_PASS_VIOLATION
            failure_class = None
            message = "Fixture run completed."

        out = {
            "suite": "honest-pass",
            "result": result,
            "strict": bool(args.strict),
            "mode": mode,
            "exit_code": _honest_exit(result),
            "failure_class": failure_class,
            "message": message,
            "details": details,
            "fixture_runner": fixture_runner,
        }
        return out

    provided = []
    if args.trace:
        provided.append(("trace", "scripts/check-process-trace.py", args.trace))
    if args.binding:
        provided.append(("binding", "scripts/check-evidence-binding.py", args.binding))
    if args.private_evaluator:
        provided.append(("private-evaluator", "scripts/check-private-evaluator-consistency.py", args.private_evaluator))
    if args.canary:
        provided.append(("canary", "scripts/check-canary-integrity.py", args.canary))

    if not provided:
        return {
            "suite": "honest-pass",
            "result": HONEST_PASS_NEEDS_REVIEW,
            "strict": bool(args.strict),
            "mode": mode,
            "exit_code": 1,
            "failure_class": "NEEDS_HUMAN_REVIEW",
            "message": "No Honest PASS proof inputs provided.",
            "details": [],
        }

    if args.strict and (not args.trace or not args.binding):
        return {
            "suite": "honest-pass",
            "result": HONEST_PASS_VIOLATION,
            "strict": True,
            "mode": mode,
            "exit_code": 1,
            "failure_class": "PASS_WITHOUT_PROOF",
            "message": "Strict mode requires both --trace and --binding.",
            "details": [],
        }

    worst = HONEST_PASS_OK
    for name, checker, path_arg in provided:
        proc = subprocess.run(
            [sys.executable, checker, path_arg, "--json"],
            cwd=str(repo_root),
            capture_output=True,
            text=True,
            check=False,
        )
        payload = _load_json_text(proc.stdout.strip())
        if payload is None:
            token = HONEST_PASS_VIOLATION
            failure = "TRACE_INVALID"
            msg = "Invalid checker JSON output."
        else:
            token = payload.get("result", HONEST_PASS_VIOLATION)
            failure = payload.get("failure_class")
            msg = payload.get("message", "")
        details.append(
            {
                "input": name,
                "path": path_arg,
                "checker": checker,
                "result": token,
                "failure_class": failure,
                "message": msg,
            }
        )
        if HONEST_PRIORITY.get(token, 2) > HONEST_PRIORITY.get(worst, 0):
            worst = token

    return {
        "suite": "honest-pass",
        "result": worst,
        "strict": bool(args.strict),
        "mode": mode,
        "exit_code": _honest_exit(worst),
        "details": details,
    }


def _map_source_to_integrity(source_token):
    if source_token in INTEGRITY_PRIORITY:
        return source_token
    return SOURCE_TO_INTEGRITY.get(source_token, INTEGRITY_NEEDS_REVIEW)


def _integrity_envelope(suite, source_result, source_failure_class, source_output, message):
    mapped = _map_source_to_integrity(source_result)
    return {
        "suite": suite,
        "result": mapped,
        "source_result": source_result,
        "source_failure_class": source_failure_class,
        "source_output": source_output,
        "message": message,
        "exit_code": INTEGRITY_EXIT[mapped],
        "generated_at": generated_at_utc(),
        "details": [],
    }


def _blocked_envelope(suite, message, parse_error=None):
    details = []
    if parse_error:
        details.append({"parse_error": parse_error})
    return {
        "suite": suite,
        "result": INTEGRITY_BLOCKED,
        "source_result": None,
        "source_failure_class": None,
        "source_output": None,
        "message": message,
        "exit_code": 1,
        "generated_at": generated_at_utc(),
        "details": details,
    }


def _needs_review_envelope(suite, message):
    return {
        "suite": suite,
        "result": INTEGRITY_NEEDS_REVIEW,
        "source_result": None,
        "source_failure_class": None,
        "source_output": None,
        "message": message,
        "exit_code": 1,
        "generated_at": generated_at_utc(),
        "details": [],
    }


def _run_json_subprocess(repo_root, cmd_list):
    proc = subprocess.run(
        cmd_list,
        cwd=str(repo_root),
        capture_output=True,
        text=True,
        check=False,
    )
    payload = _load_json_text(proc.stdout.strip())
    if payload is None:
        return None, f"Failed to parse JSON from {' '.join(cmd_list[:3])}"
    return payload, None


def run_runtime_bypass_smoke(repo_root):
    payload, err = _run_json_subprocess(repo_root, [sys.executable, "scripts/test-m40-runtime-bypass-smoke.py", "--json"])
    if err:
        return _blocked_envelope("runtime-bypass-smoke", "Wrapped runtime bypass output is invalid JSON.", err)
    return _integrity_envelope(
        "runtime-bypass-smoke",
        payload.get("result"),
        payload.get("failure_class"),
        payload,
        "runtime-bypass-smoke completed",
    )


def _run_input_checker(repo_root, suite_name, checker_script, input_path, missing_message):
    if not input_path:
        return _needs_review_envelope(suite_name, missing_message)
    payload, err = _run_json_subprocess(repo_root, [sys.executable, checker_script, input_path, "--json"])
    if err:
        return _blocked_envelope(suite_name, "Wrapped checker output is invalid JSON.", err)
    return _integrity_envelope(
        suite_name,
        payload.get("result"),
        payload.get("failure_class"),
        payload,
        f"{suite_name} completed",
    )


def _integrity_aggregate(subchecks):
    worst = INTEGRITY_OK
    for s in subchecks:
        if INTEGRITY_PRIORITY[s["result"]] > INTEGRITY_PRIORITY[worst]:
            worst = s["result"]
    return worst


def _integrity_explain_text(token=None):
    lines = []
    if token is not None:
        info = INTEGRITY_EXPLANATION_MAP.get(token)
        if info is None:
            return None
        lines.append(f"Integrity Result: {token}")
        lines.append(f"Meaning: {info['meaning']}")
        lines.append(f"Clean PASS: {'yes' if info['clean_pass'] else 'no'}")
        lines.append(f"Next Safe Action: {info['next_safe_action']}")
        lines.append(f"What this does not mean: {info['does_not_mean']}")
        lines.append("Human approval remains above every PASS.")
        return "\n".join(lines)

    for key in [INTEGRITY_OK, INTEGRITY_WARNING, INTEGRITY_VIOLATION, INTEGRITY_NEEDS_REVIEW, INTEGRITY_BLOCKED]:
        info = INTEGRITY_EXPLANATION_MAP[key]
        lines.append(f"[{key}]")
        lines.append(f"- Meaning: {info['meaning']}")
        lines.append(f"- Clean PASS: {'yes' if info['clean_pass'] else 'no'}")
        lines.append(f"- Next Safe Action: {info['next_safe_action']}")
        lines.append(f"- Not meaning: {info['does_not_mean']}")
        lines.append("")
    lines.append("PASS is a validation signal, not authorization.")
    lines.append("Checker PASS is validation signal, not approval.")
    lines.append("Human approval remains above every PASS.")
    return "\n".join(lines)


def _integrity_summary_text(payload):
    result = payload.get("result", INTEGRITY_BLOCKED)
    strict_mode = bool(payload.get("strict", False))
    subchecks = payload.get("subchecks", [])

    counts = {
        INTEGRITY_WARNING: 0,
        INTEGRITY_VIOLATION: 0,
        INTEGRITY_NEEDS_REVIEW: 0,
        INTEGRITY_BLOCKED: 0,
    }
    source_tokens_preserved = True
    for sub in subchecks:
        sub_res = sub.get("result")
        if sub_res in counts:
            counts[sub_res] += 1
        if sub.get("source_result") is None:
            source_tokens_preserved = False

    info = INTEGRITY_EXPLANATION_MAP.get(
        result,
        {
            "clean_pass": False,
            "next_safe_action": "Require maintainer review.",
            "does_not_mean": "Unknown result token.",
        },
    )
    clean_pass = "yes" if info["clean_pass"] else "no"

    limitations = [
        "Summary output is user guidance, not evidence authority.",
        "Unified status is navigation metadata, not replacement for source token.",
    ]
    if strict_mode:
        limitations.append("INTEGRITY_WARNING is not clean PASS.")

    lines = [
        "Integrity Result Summary",
        f"Integrity Result: {result}",
        f"Clean PASS: {clean_pass}",
        f"Strict Mode: {'true' if strict_mode else 'false'}",
        f"Source Tokens Preserved: {'yes' if source_tokens_preserved else 'no'}",
        f"Warnings: {counts[INTEGRITY_WARNING]}",
        f"Violations: {counts[INTEGRITY_VIOLATION]}",
        f"Needs Review: {counts[INTEGRITY_NEEDS_REVIEW]}",
        f"Blocked: {counts[INTEGRITY_BLOCKED]}",
        f"Next Safe Action: {info['next_safe_action']}",
        "Human Approval: Human approval remains above every PASS.",
        f"Limitations: {' '.join(limitations)}",
    ]
    return "\n".join(lines)


def _registry_path(args):
    return args.registry or "tests/fixtures/integrity-fixture-registry.json"


def _load_registry(path_text):
    p = Path(path_text)
    if not p.exists():
        return None, "INTEGRITY_REGISTRY_MISSING", f"Registry missing: {path_text}", None
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception as exc:
        return None, "INTEGRITY_REGISTRY_INVALID", f"Registry invalid JSON: {exc}", None
    if not isinstance(data, dict) or not isinstance(data.get("entries"), list):
        return None, "INTEGRITY_REGISTRY_INVALID", "Registry must contain entries array.", None
    return data, None, None, p


def _list_registry(args):
    reg_path = _registry_path(args)
    reg, err_fc, err_msg, _ = _load_registry(reg_path)
    if err_fc:
        return {
            "suite": "integrity-fixture-registry",
            "result": INTEGRITY_BLOCKED,
            "source_result": None,
            "source_failure_class": err_fc,
            "registry_path": reg_path,
            "entries": [],
            "exit_code": 1,
            "generated_at": generated_at_utc(),
            "details": [err_msg],
        }
    return {
        "suite": "integrity-fixture-registry",
        "result": INTEGRITY_OK,
        "source_result": None,
        "source_failure_class": None,
        "registry_path": reg_path,
        "entries": reg.get("entries", []),
        "exit_code": 0,
        "generated_at": generated_at_utc(),
        "details": [],
    }


def _build_registry_subcommand(entry):
    command = entry.get("command")
    if command in ["integrity", "all"]:
        return None, "INTEGRITY_REGISTRY_RECURSION_FORBIDDEN", f"Registry command forbidden: {command}"

    allowed = {
        "honest-pass",
        "runtime-bypass-smoke",
        "validator-authority",
        "role-separation",
        "evidence-immutability",
        "evidence-amendments",
    }
    if command not in allowed:
        return None, "INTEGRITY_REGISTRY_COMMAND_UNKNOWN", f"Unknown registry command: {command}"

    args = entry.get("args", [])
    if not isinstance(args, list) or any(not isinstance(x, str) for x in args):
        return None, "INTEGRITY_REGISTRY_INVALID", "Registry entry args must be string array."

    cmd = [sys.executable, "scripts/agentos-validate.py", command]
    input_path = entry.get("input_path")
    if input_path is not None:
        ip = Path(input_path)
        if not ip.exists():
            return None, "INTEGRITY_REGISTRY_INPUT_MISSING", f"Registry input path missing: {input_path}"
        cmd.extend(["--input", input_path])
    cmd.extend(args)
    return cmd, None, None


def run_integrity(repo_root, args):
    if args.summary and args.json:
        return _blocked_envelope("integrity", "Use either --summary or --json, not both.")

    if args.list_fixtures:
        return _list_registry(args)

    if not args.fixtures:
        return _needs_review_envelope("integrity", "integrity requires --fixtures")

    reg_path = _registry_path(args)
    reg, err_fc, err_msg, _ = _load_registry(reg_path)
    if err_fc:
        out = _blocked_envelope("integrity", err_msg)
        out["source_failure_class"] = err_fc
        out["details"].append("Registry-driven integrity checks must not call integrity recursively.")
        return out

    subchecks = []
    for entry in reg.get("entries", []):
        cmd, fc, msg = _build_registry_subcommand(entry)
        if fc:
            blocked = _blocked_envelope(entry.get("suite", "integrity-entry"), msg)
            blocked["source_failure_class"] = fc
            blocked["details"].append({"entry_id": entry.get("id")})
            subchecks.append(blocked)
            continue

        payload, parse_err = _run_json_subprocess(repo_root, cmd)
        if parse_err:
            blocked = _blocked_envelope(entry.get("suite", "integrity-entry"), "Wrapped subcommand output is invalid JSON.", parse_err)
            blocked["source_failure_class"] = "INTEGRITY_REGISTRY_INVALID"
            blocked["details"].append({"entry_id": entry.get("id")})
            subchecks.append(blocked)
            continue

        check = _integrity_envelope(
            entry.get("suite", cmd[2]),
            payload.get("result"),
            payload.get("failure_class"),
            payload,
            f"{entry.get('id', cmd[2])} completed",
        )
        check["details"].append({"entry_id": entry.get("id"), "command": cmd[2]})
        subchecks.append(check)

    agg = _integrity_aggregate(subchecks)
    details = [
        "Hardcoded fixture paths in integrity --fixtures are an M41.2 MVP limitation.",
        "M41.3 replaces hardcoded fixture paths with deterministic registry-driven fixture discovery.",
    ]
    if args.strict and agg == INTEGRITY_WARNING:
        details.append("INTEGRITY_WARNING is not clean PASS.")

    return {
        "suite": "integrity",
        "result": agg,
        "source_result": None,
        "source_failure_class": None,
        "exit_code": INTEGRITY_EXIT[agg],
        "strict": bool(args.strict),
        "mode": "fixtures",
        "registry_path": reg_path,
        "generated_at": generated_at_utc(),
        "details": details,
        "subchecks": subchecks,
    }


def run_integrity_regression(repo_root, args):
    cmd = [sys.executable, "scripts/test-integrity-regression.py"]
    if args.self_test_fixtures:
        cmd.append("--self-test-fixtures")
    if args.fixture_root:
        cmd.extend(["--fixture-root", args.fixture_root])
    if args.json:
        cmd.append("--json")
    if args.skip_all_strict_check:
        cmd.append("--skip-all-strict-check")

    proc = subprocess.run(
        cmd,
        cwd=str(repo_root),
        capture_output=True,
        text=True,
        check=False,
    )

    if args.json:
        payload = _load_json_text(proc.stdout.strip())
        if payload is None:
            safe = {
                "suite": "integrity-regression-wrapper",
                "result": INTEGRITY_REGRESSION_BLOCKED,
                "failure_class": "INVALID_RUNNER_JSON",
                "error": "invalid_runner_json",
                "message": "Regression runner returned invalid JSON.",
                "source_output_available": bool((proc.stdout or "").strip() or (proc.stderr or "").strip()),
                "generated_at": generated_at_utc(),
                "details": [
                    "Regression CLI integration detects drift; it does not grant approval.",
                    "Regression runner result is validation evidence, not approval.",
                ],
            }
            return safe, 1
        return payload, proc.returncode

    text = proc.stdout if proc.stdout else proc.stderr
    if text:
        print(text, end="" if text.endswith("\n") else "\n")
    return None, proc.returncode


def print_human(summary):
    failed_names = [c["name"] for c in summary["checks"] if c["result"] in [FAIL, ERROR]]
    warn_names = [c["name"] for c in summary["checks"] if c["result"] == WARN]
    not_run_names = [c["name"] for c in summary["checks"] if c["result"] == NOT_RUN]

    print(f"Overall result: {summary['result']}")
    print(f"Checks run: {summary['commands_run']}")
    print(f"Failed checks: {len(failed_names)}")
    print(f"Warnings: {len(warn_names)}")
    print(f"Not run checks: {len(not_run_names)}")
    print(f"Human action required: {'YES' if summary['human_action_required'] else 'NO'}")

    if summary["result"] == PASS:
        print("Next step: continue normal review")
    elif summary["result"] == WARN:
        print("Next step: review warning details")
    elif summary["result"] == NOT_RUN:
        print("Next step: run missing checks")
    elif summary["result"] == FAIL:
        print("Next step: fix failing checks and rerun")
    else:
        print("Next step: investigate execution errors")


def emit_json(payload):
    text = json.dumps(payload, indent=2)
    print(text)


def main(argv):
    try:
        args = parse_cli(argv)
    except Exception as exc:
        payload = {
            "result": ERROR,
            "commands_run": 0,
            "commands_passed": 0,
            "commands_failed": 1,
            "commands_warned": 0,
            "commands_not_run": 0,
            "human_action_required": True,
            "checks": [
                {
                    "name": "argument-error",
                    "command": "agentos-validate",
                    "exit_code": 3,
                    "result": ERROR,
                    "output_summary": str(exc),
                    "human_action_required": True,
                }
            ],
        }
        if "--json" in argv:
            emit_json(payload)
        else:
            print_human(payload)
        return 3

    repo_root = Path(os.getcwd()).resolve()

    if args.command == "honest-pass":
        hp = run_honest_pass(repo_root, args)
        if args.json:
            emit_json(hp)
        else:
            print(f"{hp['result']}: {hp.get('message', 'Honest PASS run completed.')}")
        return hp["exit_code"]

    if args.command == "runtime-bypass-smoke":
        out = run_runtime_bypass_smoke(repo_root)
        if args.json:
            emit_json(out)
        else:
            print(f"{out['result']}: {out['message']}")
        return out["exit_code"]

    if args.command == "validator-authority":
        out = _run_input_checker(
            repo_root,
            "validator-authority",
            "scripts/check-validator-authority-boundary.py",
            args.input,
            "validator-authority requires --input",
        )
        if args.json:
            emit_json(out)
        else:
            print(f"{out['result']}: {out['message']}")
        return out["exit_code"]

    if args.command == "role-separation":
        out = _run_input_checker(
            repo_root,
            "role-separation",
            "scripts/check-role-separation.py",
            args.input,
            "role-separation requires --input",
        )
        if args.json:
            emit_json(out)
        else:
            print(f"{out['result']}: {out['message']}")
        return out["exit_code"]

    if args.command == "evidence-immutability":
        out = _run_input_checker(
            repo_root,
            "evidence-immutability",
            "scripts/check-evidence-immutability.py",
            args.input,
            "evidence-immutability requires --input",
        )
        if args.json:
            emit_json(out)
        else:
            print(f"{out['result']}: {out['message']}")
        return out["exit_code"]

    if args.command == "evidence-amendments":
        out = _run_input_checker(
            repo_root,
            "evidence-amendments",
            "scripts/check-evidence-amendments.py",
            args.input,
            "evidence-amendments requires --input",
        )
        if args.json:
            emit_json(out)
        else:
            print(f"{out['result']}: {out['message']}")
        return out["exit_code"]

    if args.command == "integrity":
        if args.explain_results:
            print(_integrity_explain_text())
            return 0
        if args.explain_result:
            explained = _integrity_explain_text(args.explain_result)
            if explained is None:
                print("Unknown integrity result token.")
                return 1
            print(explained)
            return 0

        out = run_integrity(repo_root, args)
        if args.summary:
            print(_integrity_summary_text(out))
        elif args.json:
            emit_json(out)
        else:
            print(f"{out['result']}: integrity run completed")
        return out["exit_code"]

    if args.command == "integrity-regression":
        payload, code = run_integrity_regression(repo_root, args)
        if args.json:
            emit_json(payload)
        return code

    if args.command == "scope":
        checks = run_scope(repo_root, args.task)
    elif args.command == "scope-fixtures":
        checks = run_scope_fixtures(repo_root)
    elif args.command == "execution-audit":
        checks = run_execution_audit(repo_root)
    elif args.command == "readiness-assertions":
        checks = run_readiness_assertions(repo_root)
    elif args.command == "single-role":
        checks = run_single_role(repo_root, args.task or "tasks/active-task.md")
    else:
        checks = run_all(repo_root)
        if args.strict:
            integ_cmd = [
                sys.executable,
                "scripts/agentos-validate.py",
                "integrity",
                "--strict",
                "--fixtures",
                "--json",
            ]
            integ, parse_err = _run_json_subprocess(repo_root, integ_cmd)
            if parse_err:
                mapped = FAIL
                integ_result = INTEGRITY_BLOCKED
                out_summary = "integrity json parse failed"
            else:
                integ_result = integ.get("result", INTEGRITY_BLOCKED)
                if integ_result == INTEGRITY_OK:
                    mapped = PASS
                elif integ_result == INTEGRITY_WARNING:
                    mapped = WARN
                else:
                    mapped = FAIL
                warn_count = 0
                violation_count = 0
                needs_review_count = 0
                blocked_count = 0
                source_tokens = []
                for sub in integ.get("subchecks", []):
                    sr = sub.get("result")
                    if sr == INTEGRITY_WARNING:
                        warn_count += 1
                    elif sr == INTEGRITY_VIOLATION:
                        violation_count += 1
                    elif sr == INTEGRITY_NEEDS_REVIEW:
                        needs_review_count += 1
                    elif sr == INTEGRITY_BLOCKED:
                        blocked_count += 1
                    src = sub.get("source_result")
                    if src is not None:
                        source_tokens.append(src)
                next_safe_action = INTEGRITY_EXPLANATION_MAP.get(
                    integ_result, {}
                ).get("next_safe_action", "Require maintainer review.")
                out_summary = (
                    f"{integ_result}; warnings={warn_count}; violations={violation_count}; "
                    f"needs_review={needs_review_count}; blocked={blocked_count}; "
                    f"source_tokens={','.join(source_tokens) if source_tokens else 'none'}; "
                    f"next_safe_action={next_safe_action}"
                )
            if integ_result == INTEGRITY_OK:
                mapped = PASS
            elif integ_result == INTEGRITY_WARNING:
                mapped = WARN
            else:
                mapped = FAIL
            checks.append(
                {
                    "name": "integrity-strict-fixtures",
                    "command": f"{sys.executable} scripts/agentos-validate.py {INTEGRITY_STRICT_FIXTURES_JSON_CMD_TEXT}",
                    "exit_code": 0 if mapped in [PASS, WARN] else 1,
                    "result": mapped,
                    "output_summary": out_summary,
                    "human_action_required": mapped == FAIL,
                    "ran": True,
                }
            )
            regression_cmd = [
                sys.executable,
                "scripts/agentos-validate.py",
                "integrity-regression",
                "--json",
                "--skip-all-strict-check",
            ]
            reg_payload, reg_parse_err = _run_json_subprocess(repo_root, regression_cmd)
            if reg_parse_err:
                reg_mapped = FAIL
                reg_summary = "regression json parse failed"
                reg_result = INTEGRITY_REGRESSION_BLOCKED
            else:
                reg_result = reg_payload.get("result", INTEGRITY_REGRESSION_BLOCKED)
                reg_details = reg_payload.get("summary", {})
                reg_summary = (
                    f"{reg_result}; passed={reg_details.get('passed', 0)}; "
                    f"failed={reg_details.get('failed', 0)}; "
                    f"needs_review={reg_details.get('needs_review', 0)}; "
                    f"blocked={reg_details.get('blocked', 0)}; "
                    "Skipped to prevent all --strict recursion."
                )
                if reg_result == INTEGRITY_REGRESSION_OK:
                    reg_mapped = PASS
                elif reg_result == INTEGRITY_REGRESSION_NEEDS_REVIEW:
                    reg_mapped = FAIL
                elif reg_result == INTEGRITY_REGRESSION_BLOCKED:
                    reg_mapped = FAIL
                else:
                    reg_mapped = FAIL

            checks.append(
                {
                    "name": "integrity-regression-strict",
                    "command": f"{sys.executable} scripts/agentos-validate.py {INTEGRITY_REGRESSION_JSON_CMD_TEXT}",
                    "exit_code": 0 if reg_mapped == PASS else 1,
                    "result": reg_mapped,
                    "output_summary": reg_summary,
                    "human_action_required": reg_mapped == FAIL,
                    "ran": True,
                }
            )

    summary = aggregate(checks)

    if args.json:
        emit_json(summary)
    else:
        print_human(summary)

    return RESULT_TO_EXIT[summary["result"]]


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
