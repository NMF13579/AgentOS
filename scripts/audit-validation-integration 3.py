#!/usr/bin/env python3
import json
import re
import subprocess
import sys
from pathlib import Path

STATUS_READY = "VALIDATION_FOUNDATION_READY"
STATUS_WARN = "READY_WITH_WARNINGS"
STATUS_REVIEW = "NEEDS_REVIEW"
STATUS_NOT_READY = "NOT_READY"

REQUIRED_ARTIFACTS = [
    "scripts/agentos-validate.py",
    ".github/workflows/agentos-validate.yml",
    "docs/CI-ADVISORY-MODE.md",
    "docs/REQUIRED-CHECKS-POLICY.md",
    "docs/CI-EVIDENCE-ARTIFACTS.md",
    "templates/ci-validation-summary.md",
    "docs/AGENTOS-VALIDATE-JSON-CONTRACT.md",
    "tests/fixtures/ci-advisory/",
    "tests/fixtures/ci-advisory/valid/advisory-workflow.yml",
    "scripts/test-ci-advisory-config.py",
]

DOC_CHECKS = {
    "docs/CI-ADVISORY-MODE.md": [
        "Advisory CI provides visibility, not enforcement.",
        "CI evidence is not approval.",
        "NOT_RUN is not PASS.",
        "ERROR requires human review.",
        "FAIL requires human review.",
    ],
    "docs/REQUIRED-CHECKS-POLICY.md": [
        "M24 defines required checks policy; M24 does not enforce required checks.",
        "Required checks are documented in M24, not enforced.",
        "M25 may introduce enforced required checks.",
    ],
    "docs/CI-EVIDENCE-ARTIFACTS.md": [
        "CI evidence is review input, not approval.",
        "CI evidence is not approval.",
        "M24 does not enforce required checks.",
        "M24 does not enforce protected branches.",
    ],
    "docs/AGENTOS-VALIDATE-JSON-CONTRACT.md": [
        "JSON output is automation evidence, not approval.",
        "JSON mode must output valid JSON only.",
        "JSON mode must not mix human-readable text with JSON.",
        "PASS does not prove implementation correctness.",
    ],
}

WORKFLOW_FORBIDDEN = [
    r"protected branch",
    r"required check",
    r"branch protection",
    r"codeowners enforcement",
    r"git\s+push",
    r"gh\s+pr\s+merge",
    r"gh\s+pr\s+review\s+--approve",
    r"auto-merge",
    r"deploy",
    r"deployment",
    r"release",
    r"secrets\.",
    r"contents:\s*write",
    r"pull-requests:\s*write",
    r"issues:\s*write",
    r"actions:\s*write",
    r"checks:\s*write",
    r"permissions:\s*write-all",
]


def clean_yaml_exec_lines(text):
    out = []
    for raw in text.splitlines():
        if not raw.strip():
            continue
        s = raw.lstrip()
        if s.startswith("#"):
            continue
        if "#" in raw:
            raw = raw.split("#", 1)[0]
        if raw.strip():
            out.append(raw.rstrip())
    return out


def run_cmd(cmd):
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True)
        combined = (proc.stdout or "") + (proc.stderr or "")
        return proc.returncode, combined
    except Exception as exc:
        return 3, str(exc)


def check_artifacts(root):
    missing = []
    found = []
    for rel in REQUIRED_ARTIFACTS:
        p = root / rel
        if rel.endswith("/"):
            ok = p.is_dir()
        else:
            ok = p.is_file()
        if ok:
            found.append(rel)
        else:
            missing.append(rel)
    return found, missing


def check_docs_content(root):
    failures = []
    for rel, lines in DOC_CHECKS.items():
        p = root / rel
        if not p.is_file():
            failures.append(f"missing file for content check: {rel}")
            continue
        text = p.read_text(encoding="utf-8")
        for line in lines:
            if line not in text:
                failures.append(f"missing required line in {rel}: {line}")
    return failures


def check_workflow(root):
    failures = []
    workflow = root / ".github/workflows/agentos-validate.yml"
    if not workflow.is_file():
        return ["workflow file missing"], []

    text = workflow.read_text(encoding="utf-8")
    lines = clean_yaml_exec_lines(text)
    blob = "\n".join(lines)

    required_patterns = [
        (r"\bpull_request\s*:", "missing pull_request trigger"),
        (r"\bpush\s*:", "missing push trigger"),
        (r"-\s*dev\b|\[\s*dev\s*\]", "missing push trigger for dev"),
        (r"python\s+scripts/agentos-validate\.py\s+all(\s|$)", "missing all command"),
        (r"python\s+scripts/agentos-validate\.py\s+all\s+--json", "missing all --json command"),
        (r"reports/ci/agentos-validate\.json", "missing json output path"),
        (r"agentos-validation-evidence", "missing artifact name"),
        (r"if\s*:\s*always\(\)", "missing if: always()"),
    ]

    for pattern, msg in required_patterns:
        if not re.search(pattern, blob, flags=re.IGNORECASE):
            failures.append(msg)

    # explicit upload step requires if: always()
    upload_step_ok = False
    blocks = blob.split("\n      - ")
    for block in blocks:
        if re.search(r"actions/upload-artifact", block, flags=re.IGNORECASE):
            if re.search(r"if\s*:\s*always\(\)", block, flags=re.IGNORECASE):
                upload_step_ok = True
    if not upload_step_ok:
        failures.append("artifact upload step missing explicit if: always()")

    # json after human with continue-on-error true
    human_idx = next((i for i, l in enumerate(lines) if re.search(r"python\s+scripts/agentos-validate\.py\s+all(\s|$)", l, flags=re.IGNORECASE)), -1)
    json_idx = next((i for i, l in enumerate(lines) if re.search(r"python\s+scripts/agentos-validate\.py\s+all\s+--json", l, flags=re.IGNORECASE)), -1)
    has_human_continue = bool(re.search(r"id\s*:\s*validate_human[\s\S]*?continue-on-error\s*:\s*true", blob, flags=re.IGNORECASE))
    if human_idx == -1 or json_idx == -1 or not (json_idx > human_idx and has_human_continue):
        failures.append("JSON evidence generation is not preserved after human validation failure")

    if re.search(r"\|\|\s*true", blob, flags=re.IGNORECASE):
        failures.append("silent failure ignoring detected (|| true)")

    for pat in WORKFLOW_FORBIDDEN:
        if re.search(pat, blob, flags=re.IGNORECASE):
            failures.append(f"forbidden workflow pattern detected: {pat}")

    return failures, []


def check_cli_contract(root, warnings, failures, not_run):
    cli = root / "scripts/agentos-validate.py"
    if not cli.is_file():
        not_run.append("cli checks not run: scripts/agentos-validate.py missing")
        return

    py = sys.executable or "python3"

    code, out = run_cmd([py, str(cli), "--help"])
    if code != 0:
        failures.append("agentos-validate --help failed")
    else:
        required = ["scope", "scope-fixtures", "execution-audit", "all"]
        for cmd in required:
            if cmd not in out:
                failures.append(f"missing command in --help: {cmd}")
        # Проверяем только список позиционных команд в help.
        lower = out.lower()
        m = re.search(r"\{([^}]*)\}", lower)
        cmd_blob = m.group(1) if m else ""
        legacy = ["template", "task", "queue", "audit", "state", "review", "trace"]
        for bad in legacy:
            if re.search(rf"(^|,)\s*{bad}\s*(,|$)", cmd_blob):
                failures.append(f"legacy command exposed: {bad}")

    code, out = run_cmd([py, str(cli), "all", "--json"])
    if code in (0, 1, 2, 3):
        try:
            data = json.loads(out)
            if not isinstance(data, dict):
                failures.append("all --json output is not object")
            else:
                required_keys = [
                    "result",
                    "commands_run",
                    "commands_passed",
                    "commands_failed",
                    "commands_warned",
                    "commands_not_run",
                    "human_action_required",
                    "checks",
                ]
                for k in required_keys:
                    if k not in data:
                        failures.append(f"all --json missing key: {k}")
        except Exception:
            failures.append("all --json is not valid JSON")
    else:
        failures.append("all --json execution error")


def main():
    try:
        root = Path.cwd()
        py = sys.executable or "python3"

        warnings = []
        failures = []
        not_run = []
        command_results = []

        found, missing = check_artifacts(root)
        if missing:
            failures.extend([f"missing artifact: {m}" for m in missing])

        # required command checks
        commands = [
            [py, "-m", "py_compile", "scripts/agentos-validate.py"],
            [py, "-m", "py_compile", "scripts/test-ci-advisory-config.py"],
            [py, "scripts/test-ci-advisory-config.py"],
        ]

        for c in commands:
            rel = " ".join(c)
            rc, out = run_cmd(c)
            command_results.append((rel, rc, out[-300:]))
            if rc != 0:
                failures.append(f"required command failed: {rel} (exit {rc})")

        optional = [
            [py, "scripts/agentos-validate.py", "--help"],
            [py, "scripts/agentos-validate.py", "all", "--json"],
        ]
        for c in optional:
            rel = " ".join(c)
            if not (root / "scripts/agentos-validate.py").is_file():
                not_run.append(f"optional command not run: {rel}")
                continue
            rc, out = run_cmd(c)
            command_results.append((rel, rc, out[-300:]))
            if rc == 3:
                warnings.append(f"optional command returned ERROR-like exit: {rel}")

        doc_failures = check_docs_content(root)
        failures.extend(doc_failures)

        wf_failures, _ = check_workflow(root)
        failures.extend(wf_failures)

        check_cli_contract(root, warnings, failures, not_run)

        enforcement_detected = any("forbidden workflow pattern detected" in x for x in failures)

        if enforcement_detected:
            final = STATUS_NOT_READY
            exit_code = 1
        elif missing:
            final = STATUS_NOT_READY
            exit_code = 1
        elif failures:
            final = STATUS_REVIEW
            exit_code = 1
        elif not_run:
            final = STATUS_REVIEW
            exit_code = 1
        elif warnings:
            final = STATUS_WARN
            exit_code = 2
        else:
            final = STATUS_READY
            exit_code = 0

        human_action_required = "NO" if final == STATUS_READY else "YES"

        print(f"Final result: {final}")
        print("Artifact inventory:")
        print(f"- found: {len(found)}")
        print(f"- missing: {len(missing)}")
        if missing:
            for m in missing:
                print(f"  - {m}")

        print("Command evidence:")
        for name, rc, summary in command_results:
            print(f"- {name}")
            print(f"  exit_code: {rc}")
            print(f"  output_summary: {summary.strip() if summary.strip() else 'EMPTY'}")

        print("Content check summary:")
        print(f"- failures: {len(doc_failures)}")

        print("Workflow advisory check summary:")
        wf_count = len(wf_failures)
        print(f"- failures: {wf_count}")

        forbidden_count = len([x for x in failures if "forbidden workflow pattern detected" in x])
        print("Forbidden behavior check summary:")
        print(f"- detected: {forbidden_count}")

        print("Warnings:")
        if warnings:
            for w in warnings:
                print(f"- {w}")
        else:
            print("- NONE")

        print("Failures:")
        if failures:
            for f in failures:
                print(f"- {f}")
        else:
            print("- NONE")

        print("Not run checks:")
        if not_run:
            for n in not_run:
                print(f"- {n}")
        else:
            print("- NONE")

        print(f"human_action_required: {human_action_required}")
        print("next step: 24.9.1")

        return exit_code
    except Exception as exc:
        print("Final result: NOT_READY")
        print(f"internal error: {exc}")
        return 3


if __name__ == "__main__":
    sys.exit(main())
