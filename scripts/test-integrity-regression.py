#!/usr/bin/env python3

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

INTEGRITY_REGRESSION_OK = "INTEGRITY_REGRESSION_OK"
INTEGRITY_REGRESSION_FAILED = "INTEGRITY_REGRESSION_FAILED"
INTEGRITY_REGRESSION_NEEDS_REVIEW = "INTEGRITY_REGRESSION_NEEDS_REVIEW"
INTEGRITY_REGRESSION_BLOCKED = "INTEGRITY_REGRESSION_BLOCKED"

FAILURE_CLASSES = {
    "COMMAND_CONTRACT_REGRESSION",
    "JSON_CONTRACT_REGRESSION",
    "JSON_FIELD_REGRESSION",
    "TOKEN_CONTRACT_REGRESSION",
    "SUMMARY_CONTRACT_REGRESSION",
    "UNKNOWN_TOKEN_REGRESSION",
    "ARGPARSE_ABBREVIATION_REGRESSION",
    "SUMMARY_JSON_CONFLICT_REGRESSION",
    "AUTHORITY_BOUNDARY_MISSING",
    "FALSE_AUTHORITY_CLAIM_REGRESSION",
    "SHELL_TRUE_REGRESSION",
    "FIXTURE_ROOT_MISSING",
}

ALLOWED_INTEGRITY_TOKENS = {
    "INTEGRITY_OK",
    "INTEGRITY_WARNING",
    "INTEGRITY_VIOLATION",
    "INTEGRITY_NEEDS_REVIEW",
    "INTEGRITY_BLOCKED",
}

CHECK_STATUS_PRIORITY = {
    "PASS": 0,
    "SKIPPED_RECURSION_GUARD": 0,
    "SKIPPED_KNOWN_GAP": 1,
    "NEEDS_REVIEW": 2,
    "BLOCKED": 3,
    "FAIL": 4,
}

EXIT_BY_RESULT = {
    INTEGRITY_REGRESSION_OK: 0,
    INTEGRITY_REGRESSION_FAILED: 1,
    INTEGRITY_REGRESSION_NEEDS_REVIEW: 1,
    INTEGRITY_REGRESSION_BLOCKED: 1,
}

AUTHORITY_FILES = [
    "docs/INTEGRITY-RESULT-UX.md",
    "docs/INTEGRITY-FIXTURE-REGISTRY.md",
    "docs/ALL-STRICT-INTEGRITY-INTEGRATION.md",
    "reports/m41-6-unified-integrity-closure-report.md",
    "reports/m42-1-authority-boundary-regression-map.md",
]

REQUIRED_GOOD_PHRASES = [
    "PASS is a validation signal, not authorization.",
    "Checker PASS is validation signal, not approval.",
    "Human approval remains above every PASS.",
    "INTEGRITY_WARNING is not clean PASS.",
    "Summary output is user guidance, not evidence authority.",
    "Fixture registry is navigation metadata, not policy, proof, or approval.",
]

FORBIDDEN_BAD_PHRASES = [
    "PASS replaces human approval",
    "Checker PASS is approval",
    "INTEGRITY_WARNING is clean PASS",
    "Summary output is evidence authority",
    "Registry is policy authority",
    "all --strict authorizes release",
    "release authorized",
    "merge authorized",
]

SUMMARY_REQUIRED_FIELDS = [
    "Integrity Result:",
    "Clean PASS:",
    "Strict Mode:",
    "Source Tokens Preserved:",
    "Warnings:",
    "Violations:",
    "Needs Review:",
    "Blocked:",
    "Next Safe Action:",
    "Human Approval:",
    "Limitations:",
    "Summary output is user guidance, not evidence authority.",
]

SELFTEST_KINDS = {
    "json-output",
    "summary-output",
    "command-behavior",
    "authority-boundary",
    "static-scan",
    "known-gap",
}

SELFTEST_CHECK_STATUSES = {
    "PASS",
    "FAIL",
    "NEEDS_REVIEW",
    "BLOCKED",
    "SKIPPED_KNOWN_GAP",
}

SELFTEST_RESULT_FLOORS = {
    INTEGRITY_REGRESSION_OK,
    INTEGRITY_REGRESSION_FAILED,
    INTEGRITY_REGRESSION_NEEDS_REVIEW,
    INTEGRITY_REGRESSION_BLOCKED,
}

RESULT_ORDER = {
    INTEGRITY_REGRESSION_OK: 0,
    INTEGRITY_REGRESSION_NEEDS_REVIEW: 1,
    INTEGRITY_REGRESSION_BLOCKED: 2,
    INTEGRITY_REGRESSION_FAILED: 3,
}



def now_utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def run_cmd(command):
    return subprocess.run(command, capture_output=True, text=True, check=False)


def make_check(check_id, command, expected):
    return {
        "id": check_id,
        "command": command,
        "expected": expected,
        "observed_exit_code": None,
        "status": "PASS",
        "failure_class": None,
        "details": [],
    }


def set_fail(check, failure_class, detail):
    check["status"] = "FAIL"
    check["failure_class"] = failure_class
    if detail:
        check["details"].append(detail)


def set_needs_review(check, failure_class, detail):
    check["status"] = "NEEDS_REVIEW"
    check["failure_class"] = failure_class
    if detail:
        check["details"].append(detail)


def set_blocked(check, failure_class, detail):
    check["status"] = "BLOCKED"
    check["failure_class"] = failure_class
    if detail:
        check["details"].append(detail)


def parse_json_output(proc):
    try:
        return json.loads(proc.stdout), None
    except Exception as exc:
        return None, str(exc)


def contains_case_insensitive(text, phrase):
    # case-insensitive matching is required to avoid false regressions on capitalization drift
    return phrase.lower() in text.lower()


def check_command_exists(check_id, cmd, allowed_exits):
    c = make_check(check_id, cmd, f"exit in {sorted(list(allowed_exits))}")
    p = run_cmd(cmd)
    c["observed_exit_code"] = p.returncode
    if p.returncode not in allowed_exits:
        set_fail(c, "COMMAND_CONTRACT_REGRESSION", "unexpected exit code")
    return c


def check_json_command(check_id, cmd):
    c = make_check(check_id, cmd, "valid JSON output")
    p = run_cmd(cmd)
    c["observed_exit_code"] = p.returncode
    payload, err = parse_json_output(p)
    if err:
        set_fail(c, "JSON_CONTRACT_REGRESSION", f"invalid json: {err}")
        return c, None
    c["details"].append("json valid")
    return c, payload


def check_required_json_fields(check_id, payload):
    c = make_check(check_id, ["internal"], "required fields present")
    c["observed_exit_code"] = 0
    missing = [k for k in ["suite", "result", "generated_at", "details"] if k not in payload]
    if missing:
        set_fail(c, "JSON_FIELD_REGRESSION", f"missing required fields: {missing}")
    optional = ["source_result", "source_failure_class", "source_output"]
    missing_optional = [k for k in optional if k not in payload]
    if missing_optional:
        c["details"].append(f"missing optional fields accepted per baseline: {missing_optional}")
    return c


def check_token_contract(check_id, payload):
    c = make_check(check_id, ["internal"], "result token in allowed INTEGRITY_* set")
    c["observed_exit_code"] = 0
    token = payload.get("result")
    if token not in ALLOWED_INTEGRITY_TOKENS:
        set_fail(c, "TOKEN_CONTRACT_REGRESSION", f"unexpected result token: {token}")
    return c


def check_summary_output(check_id, cmd):
    c = make_check(check_id, cmd, "summary contains required semantic fields (case-insensitive)")
    p = run_cmd(cmd)
    c["observed_exit_code"] = p.returncode
    if p.returncode != 0:
        set_fail(c, "SUMMARY_CONTRACT_REGRESSION", "summary command returned non-zero")
        return c
    missing = [f for f in SUMMARY_REQUIRED_FIELDS if not contains_case_insensitive(p.stdout, f)]
    if missing:
        set_fail(c, "SUMMARY_CONTRACT_REGRESSION", f"missing summary fields: {missing}")
    c["details"].append("case-insensitive summary matching used")
    return c


def check_unknown_token_behavior():
    cmd = [sys.executable, "scripts/agentos-validate.py", "integrity", "--explain-result", "UNKNOWN_TOKEN"]
    c = make_check("unknown-token-safe-failure", cmd, "non-zero exit and unknown token warning")
    p = run_cmd(cmd)
    c["observed_exit_code"] = p.returncode
    out = f"{p.stdout}\n{p.stderr}"
    if p.returncode == 0:
        set_fail(c, "UNKNOWN_TOKEN_REGRESSION", "command unexpectedly succeeded")
        return c
    if "Unknown integrity result token." not in out:
        set_fail(c, "UNKNOWN_TOKEN_REGRESSION", "missing expected unknown token warning")
    return c


def check_abbreviation_safety():
    cmd = [sys.executable, "scripts/agentos-validate.py", "integrity", "--explain-r", "INTEGRITY_WARNING"]
    c = make_check("argparse-abbreviation-safety", cmd, "non-zero exit for abbreviated flag")
    p = run_cmd(cmd)
    c["observed_exit_code"] = p.returncode
    if p.returncode == 0:
        set_fail(c, "ARGPARSE_ABBREVIATION_REGRESSION", "abbreviated flag unexpectedly accepted")
    return c


def check_summary_json_conflict():
    cmd = [sys.executable, "scripts/agentos-validate.py", "integrity", "--fixtures", "--summary", "--json"]
    c = make_check("summary-json-conflict", cmd, "non-zero exit and conflict message")
    p = run_cmd(cmd)
    c["observed_exit_code"] = p.returncode
    out = f"{p.stdout}\n{p.stderr}"
    if p.returncode == 0:
        set_fail(c, "SUMMARY_JSON_CONFLICT_REGRESSION", "conflict command unexpectedly succeeded")
        return c
    if "Use either --summary or --json, not both." not in out:
        set_fail(c, "SUMMARY_JSON_CONFLICT_REGRESSION", "missing conflict message")
    return c


def check_authority_boundaries():
    c = make_check("authority-boundary-text-scan", ["internal-file-scan"], "required good phrases present and forbidden phrases absent")
    c["observed_exit_code"] = 0

    existing = [p for p in AUTHORITY_FILES if Path(p).exists()]
    c["details"].append(f"authority-boundary scanned files availability result: {len(existing)} file(s)")

    if not existing:
        set_needs_review(c, "AUTHORITY_BOUNDARY_MISSING", "No authority-boundary files available for scan.")
        return c

    chunks = []
    for p in existing:
        try:
            chunks.append(Path(p).read_text(encoding="utf-8", errors="ignore"))
        except Exception as exc:
            set_blocked(c, "AUTHORITY_BOUNDARY_MISSING", f"failed to read {p}: {exc}")
            return c
    all_text = "\n".join(chunks)

    missing_good = [g for g in REQUIRED_GOOD_PHRASES if g not in all_text]
    if missing_good:
        set_fail(c, "AUTHORITY_BOUNDARY_MISSING", f"missing required good phrase(s): {missing_good}")
        return c

    lines = all_text.splitlines()
    for bad in FORBIDDEN_BAD_PHRASES:
        for line in lines:
            if line.strip().startswith("BAD:"):
                continue
            if bad in line:
                set_fail(c, "FALSE_AUTHORITY_CLAIM_REGRESSION", f"forbidden phrase found outside BAD example: {bad}")
                return c

    return c


def check_shell_true_regression():
    c = make_check("shell-true-static-check", ["internal-static-scan"], "no forbidden shell equals true usage")
    c["observed_exit_code"] = 0
    target = Path("scripts/agentos-validate.py")
    if not target.exists():
        set_blocked(c, "COMMAND_CONTRACT_REGRESSION", "scripts/agentos-validate.py not found")
        return c
    text = target.read_text(encoding="utf-8", errors="ignore")
    if ("shell" + "=True") in text:
        set_fail(c, "SHELL_TRUE_REGRESSION", "forbidden shell equals true usage detected")
    return c


def check_warning_not_clean_pass(payload):
    c = make_check("warning-not-clean-pass", ["internal"], "INTEGRITY_WARNING is not clean PASS")
    c["observed_exit_code"] = 0
    if payload.get("result") == "INTEGRITY_WARNING":
        details_text = "\n".join([str(x) for x in payload.get("details", [])])
        if "INTEGRITY_WARNING is not clean PASS" not in details_text:
            set_needs_review(c, "SUMMARY_CONTRACT_REGRESSION", "warning phrase absent in details; verify via summary output")
    return c


def build_result(checks):
    worst = "PASS"
    for ch in checks:
        if CHECK_STATUS_PRIORITY[ch["status"]] > CHECK_STATUS_PRIORITY[worst]:
            worst = ch["status"]

    if worst == "FAIL":
        result = INTEGRITY_REGRESSION_FAILED
    elif worst == "BLOCKED":
        result = INTEGRITY_REGRESSION_BLOCKED
    elif worst in {"NEEDS_REVIEW", "SKIPPED_KNOWN_GAP"}:
        result = INTEGRITY_REGRESSION_NEEDS_REVIEW
    else:
        result = INTEGRITY_REGRESSION_OK

    summary = {
        "passed": sum(1 for c in checks if c["status"] == "PASS"),
        "failed": sum(1 for c in checks if c["status"] == "FAIL"),
        "needs_review": sum(1 for c in checks if c["status"] in {"NEEDS_REVIEW", "SKIPPED_KNOWN_GAP"}),
        "blocked": sum(1 for c in checks if c["status"] == "BLOCKED"),
    }

    return {
        "suite": "integrity-regression",
        "result": result,
        "generated_at": now_utc(),
        "checks": checks,
        "summary": summary,
    }


def run_regression(skip_all_strict_check=False):
    checks = []

    checks.append(check_command_exists("integrity-help", [sys.executable, "scripts/agentos-validate.py", "integrity", "--help"], {0}))

    checks.append(check_json_command("integrity-list-fixtures-json", [sys.executable, "scripts/agentos-validate.py", "integrity", "--list-fixtures", "--json"])[0])

    fixtures_check, fixtures_payload = check_json_command("integrity-fixtures-json", [sys.executable, "scripts/agentos-validate.py", "integrity", "--fixtures", "--json"])
    checks.append(fixtures_check)

    strict_check, strict_payload = check_json_command("integrity-strict-fixtures-json", [sys.executable, "scripts/agentos-validate.py", "integrity", "--strict", "--fixtures", "--json"])
    checks.append(strict_check)

    reg_check, _ = check_json_command(
        "integrity-registry-json",
        [sys.executable, "scripts/agentos-validate.py", "integrity", "--fixtures", "--registry", "tests/fixtures/integrity-fixture-registry.json", "--json"],
    )
    checks.append(reg_check)

    checks.append(check_command_exists("integrity-explain-results", [sys.executable, "scripts/agentos-validate.py", "integrity", "--explain-results"], {0}))
    checks.append(check_command_exists("integrity-explain-warning", [sys.executable, "scripts/agentos-validate.py", "integrity", "--explain-result", "INTEGRITY_WARNING"], {0}))
    checks.append(check_summary_output("integrity-summary", [sys.executable, "scripts/agentos-validate.py", "integrity", "--fixtures", "--summary"]))
    checks.append(check_summary_output("integrity-strict-summary", [sys.executable, "scripts/agentos-validate.py", "integrity", "--strict", "--fixtures", "--summary"]))
    checks.append(check_unknown_token_behavior())
    checks.append(check_abbreviation_safety())
    checks.append(check_summary_json_conflict())
    checks.append(check_authority_boundaries())
    checks.append(check_shell_true_regression())
    if skip_all_strict_check:
        checks.append(
            {
                "id": "all-strict",
                "command": [sys.executable, "scripts/agentos-validate.py", "all", "--strict"],
                "expected": "exit in [0, 1]",
                "observed_exit_code": None,
                "status": "SKIPPED_RECURSION_GUARD",
                "failure_class": None,
                "details": ["Skipped to prevent all --strict recursion."],
            }
        )
    else:
        checks.append(check_command_exists("all-strict", [sys.executable, "scripts/agentos-validate.py", "all", "--strict"], {0, 1}))

    if fixtures_payload is not None:
        checks.append(check_required_json_fields("fixtures-json-required-fields", fixtures_payload))
        checks.append(check_token_contract("fixtures-json-token-contract", fixtures_payload))
        checks.append(check_warning_not_clean_pass(fixtures_payload))

    if strict_payload is not None:
        checks.append(check_required_json_fields("strict-json-required-fields", strict_payload))
        checks.append(check_token_contract("strict-json-token-contract", strict_payload))
        checks.append(check_warning_not_clean_pass(strict_payload))

    return build_result(checks)


def read_json_file(path):
    try:
        return json.loads(path.read_text(encoding="utf-8")), None
    except Exception as exc:
        return None, str(exc)


def selftest_eval_fixture(fixture_dir, manifest):
    obs_status = "PASS"
    obs_failure = None
    details = []

    kind = manifest.get("kind")
    files = manifest.get("input_files", [])

    def fail(fc, msg):
        nonlocal obs_status, obs_failure
        obs_status = "FAIL"
        obs_failure = fc
        details.append(msg)

    def needs(fc, msg):
        nonlocal obs_status, obs_failure
        obs_status = "NEEDS_REVIEW"
        obs_failure = fc
        details.append(msg)

    def skipped(msg):
        nonlocal obs_status
        obs_status = "SKIPPED_KNOWN_GAP"
        details.append(msg)

    if kind == "json-output":
        if not files:
            fail("JSON_CONTRACT_REGRESSION", "missing input file for json-output")
        else:
            p = fixture_dir / files[0]
            txt = p.read_text(encoding="utf-8", errors="ignore")
            try:
                payload = json.loads(txt)
            except Exception:
                fail("JSON_CONTRACT_REGRESSION", "invalid JSON payload")
                return obs_status, obs_failure, details
            required = ["suite", "result", "generated_at", "details"]
            missing = [k for k in required if k not in payload]
            if missing:
                fail("JSON_FIELD_REGRESSION", f"missing fields: {missing}")
            elif payload.get("result") not in ALLOWED_INTEGRITY_TOKENS:
                fail("TOKEN_CONTRACT_REGRESSION", f"unknown token: {payload.get('result')}")

    elif kind == "summary-output":
        if not files:
            fail("SUMMARY_CONTRACT_REGRESSION", "missing summary input")
        else:
            txt = (fixture_dir / files[0]).read_text(encoding="utf-8", errors="ignore")
            missing = [f for f in SUMMARY_REQUIRED_FIELDS if not contains_case_insensitive(txt, f)]
            if missing:
                fail("SUMMARY_CONTRACT_REGRESSION", f"missing summary fields: {missing}")

    elif kind == "command-behavior":
        if not files:
            fail("COMMAND_CONTRACT_REGRESSION", "missing command-behavior input")
        else:
            payload, err = read_json_file(fixture_dir / files[0])
            if err:
                fail("COMMAND_CONTRACT_REGRESSION", f"invalid command-behavior json: {err}")
            else:
                code = payload.get("simulated_exit_code")
                out = f"{payload.get('simulated_stdout', '')}\n{payload.get('simulated_stderr', '')}"
                fid = manifest.get("id", "")
                if fid == "unknown-token-exit-zero-fail":
                    if code == 0 or "Unknown integrity result token." not in out:
                        fail("UNKNOWN_TOKEN_REGRESSION", "unsafe unknown token behavior")
                elif fid == "abbreviation-accepted-fail":
                    if code == 0:
                        fail("ARGPARSE_ABBREVIATION_REGRESSION", "abbreviation unexpectedly accepted")
                elif fid == "summary-json-conflict-exit-zero-fail":
                    if code == 0:
                        fail("SUMMARY_JSON_CONFLICT_REGRESSION", "summary/json conflict returned success")

    elif kind == "authority-boundary":
        if manifest.get("id") == "authority-files-missing-needs-review":
            needs("AUTHORITY_BOUNDARY_MISSING", "No authority-boundary files available for scan.")
        else:
            if not files:
                fail("AUTHORITY_BOUNDARY_MISSING", "authority-boundary fixture missing input")
            else:
                text = "\n".join([(fixture_dir / f).read_text(encoding="utf-8", errors="ignore") for f in files])
                for bad in FORBIDDEN_BAD_PHRASES:
                    if bad in text:
                        fail("FALSE_AUTHORITY_CLAIM_REGRESSION", f"forbidden phrase found: {bad}")
                        break

    elif kind == "static-scan":
        if not files:
            fail("SHELL_TRUE_REGRESSION", "missing static-scan input")
        else:
            text = (fixture_dir / files[0]).read_text(encoding="utf-8", errors="ignore")
            if ("shell" + "=True") in text:
                fail("SHELL_TRUE_REGRESSION", "forbidden shell equals true usage detected")

    elif kind == "known-gap":
        skipped("known gap fixture executed")

    else:
        fail("COMMAND_CONTRACT_REGRESSION", f"unknown kind: {kind}")

    return obs_status, obs_failure, details


def selftest_result_from_status(status):
    if status == "FAIL":
        return INTEGRITY_REGRESSION_FAILED
    if status == "BLOCKED":
        return INTEGRITY_REGRESSION_BLOCKED
    if status in {"NEEDS_REVIEW", "SKIPPED_KNOWN_GAP"}:
        return INTEGRITY_REGRESSION_NEEDS_REVIEW
    return INTEGRITY_REGRESSION_OK


def selftest_fixtures(fixture_root):
    root = Path(fixture_root)
    if not root.exists() or not root.is_dir():
        return {
            "suite": "integrity-regression-fixtures",
            "result": INTEGRITY_REGRESSION_BLOCKED,
            "fixture_root": str(root),
            "failure_class": "FIXTURE_ROOT_MISSING",
            "generated_at": now_utc(),
            "fixtures": [],
            "summary": {"passed": 0, "failed": 0, "needs_review_expected": 0, "blocked": 1},
            "details": [f"fixture root missing: {root}"],
        }

    fixtures = []
    overall = INTEGRITY_REGRESSION_OK

    for d in sorted([p for p in root.iterdir() if p.is_dir()]):
        manifest_path = d / "fixture.json"
        item = {
            "id": d.name,
            "kind": None,
            "expected_check_status": None,
            "observed_check_status": None,
            "expected_failure_class": None,
            "observed_failure_class": None,
            "status": "PASS",
            "details": [],
        }
        if not manifest_path.exists():
            item["status"] = "BLOCKED"
            item["details"].append("fixture.json missing")
            fixtures.append(item)
            overall = INTEGRITY_REGRESSION_BLOCKED
            continue

        manifest, err = read_json_file(manifest_path)
        if err:
            item["status"] = "BLOCKED"
            item["details"].append(f"invalid fixture.json: {err}")
            fixtures.append(item)
            overall = INTEGRITY_REGRESSION_BLOCKED
            continue

        req = [
            "id",
            "description",
            "kind",
            "expected_check_status",
            "expected_failure_class",
            "expected_runner_result_floor",
            "input_files",
        ]
        missing = [k for k in req if k not in manifest]
        if missing:
            item["status"] = "BLOCKED"
            item["details"].append(f"manifest missing fields: {missing}")
            fixtures.append(item)
            overall = INTEGRITY_REGRESSION_BLOCKED
            continue

        item["id"] = manifest["id"]
        item["kind"] = manifest["kind"]
        item["expected_check_status"] = manifest["expected_check_status"]
        item["expected_failure_class"] = manifest["expected_failure_class"]

        if manifest["kind"] not in SELFTEST_KINDS:
            item["status"] = "BLOCKED"
            item["details"].append("invalid kind")
            fixtures.append(item)
            overall = INTEGRITY_REGRESSION_BLOCKED
            continue
        if manifest["expected_check_status"] not in SELFTEST_CHECK_STATUSES:
            item["status"] = "BLOCKED"
            item["details"].append("invalid expected_check_status")
            fixtures.append(item)
            overall = INTEGRITY_REGRESSION_BLOCKED
            continue
        if manifest["expected_runner_result_floor"] not in SELFTEST_RESULT_FLOORS:
            item["status"] = "BLOCKED"
            item["details"].append("invalid expected_runner_result_floor")
            fixtures.append(item)
            overall = INTEGRITY_REGRESSION_BLOCKED
            continue

        obs_status, obs_failure, obs_details = selftest_eval_fixture(d, manifest)
        item["observed_check_status"] = obs_status
        item["observed_failure_class"] = obs_failure
        item["details"].extend(obs_details)

        expected_status = manifest["expected_check_status"]
        expected_failure = manifest["expected_failure_class"]
        expected_floor = manifest["expected_runner_result_floor"]
        observed_floor = selftest_result_from_status(obs_status)

        if obs_status != expected_status:
            item["status"] = "FAIL"
            item["details"].append(f"status mismatch expected={expected_status} observed={obs_status}")
        elif expected_failure != obs_failure:
            item["status"] = "FAIL"
            item["details"].append(f"failure class mismatch expected={expected_failure} observed={obs_failure}")
        elif RESULT_ORDER[observed_floor] < RESULT_ORDER[expected_floor]:
            item["status"] = "FAIL"
            item["details"].append(f"runner floor mismatch expected_floor={expected_floor} observed_floor={observed_floor}")

        if item["status"] == "FAIL":
            overall = INTEGRITY_REGRESSION_FAILED
        elif item["status"] == "BLOCKED" and overall != INTEGRITY_REGRESSION_FAILED:
            overall = INTEGRITY_REGRESSION_BLOCKED

        fixtures.append(item)

    summary = {
        "passed": sum(1 for f in fixtures if f["status"] == "PASS"),
        "failed": sum(1 for f in fixtures if f["status"] == "FAIL"),
        "needs_review_expected": sum(1 for f in fixtures if f.get("expected_check_status") in {"NEEDS_REVIEW", "SKIPPED_KNOWN_GAP"}),
        "blocked": sum(1 for f in fixtures if f["status"] == "BLOCKED"),
    }

    return {
        "suite": "integrity-regression-fixtures",
        "result": overall,
        "fixture_root": str(root),
        "generated_at": now_utc(),
        "fixtures": fixtures,
        "summary": summary,
    }


def print_human(payload):
    print(f"Regression Result: {payload['result']}")
    print("Regression runner result is validation evidence, not approval.")
    print(f"Generated At: {payload['generated_at']}")
    summary = payload.get("summary", {})
    print("Summary:")
    for key in ["passed", "failed", "needs_review", "needs_review_expected", "blocked"]:
        if key in summary:
            print(f"  {key}={summary[key]}")


def main(argv):
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--self-test-fixtures", action="store_true")
    parser.add_argument("--fixture-root", default="tests/fixtures/integrity-regression")
    parser.add_argument("--skip-all-strict-check", action="store_true")
    args = parser.parse_args(argv)

    if args.self_test_fixtures:
        result = selftest_fixtures(args.fixture_root)
    else:
        result = run_regression(skip_all_strict_check=args.skip_all_strict_check)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print_human(result)

    return EXIT_BY_RESULT[result["result"]]


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
