#!/usr/bin/env python3
"""
audit-pre-merge-corridor.py
M26 Pre-Merge Corridor Audit Script
Task: 26.10.1

READ-ONLY. This script does not modify files, commit, push, approve,
self-heal, or rewrite evidence.

CORRIDOR_READY is not approval.
CORRIDOR_READY does not authorize commit, push, merge, or release.
This audit does not override M25.
"""

import argparse
import json
import os
import sys

# ---------------------------------------------------------------------------
# Result states
# ---------------------------------------------------------------------------
CORRIDOR_READY = "CORRIDOR_READY"
READY_WITH_WARNINGS = "READY_WITH_WARNINGS"
NEEDS_REVIEW = "NEEDS_REVIEW"
NOT_READY = "NOT_READY"

RESULT_PRIORITY = {
    NOT_READY: 3,
    NEEDS_REVIEW: 2,
    READY_WITH_WARNINGS: 1,
    CORRIDOR_READY: 0,
}

# ---------------------------------------------------------------------------
# Required artifacts
# ---------------------------------------------------------------------------
REQUIRED_ARTIFACTS = [
    "docs/PRE-MERGE-EXECUTION-CORRIDOR.md",
    "docs/AGENT-PERMISSION-MODEL.md",
    "docs/COMMAND-ALLOWLIST-POLICY.md",
    "docs/WRITE-ALLOWLIST-POLICY.md",
    "docs/NO-DIRECT-PUSH-POLICY.md",
    "docs/AGENT-VIOLATION-POLICY.md",
    "docs/BOUNDED-RETRY-POLICY.md",
    "templates/pre-merge-execution-review.md",
    "templates/agent-permission-record.md",
    "templates/command-approval-record.md",
    "templates/write-scope-record.md",
    "templates/push-request-record.md",
    "templates/agent-violation-record.md",
    "templates/retry-attempt-record.md",
    "scripts/check-pre-merge-scope.py",
    "scripts/check-commit-push-preconditions.py",
    "reports/milestone-26-evidence-report.md",
]

# ---------------------------------------------------------------------------
# Required evidence report entries
# ---------------------------------------------------------------------------
REQUIRED_EVIDENCE_ENTRIES = [
    "26.1.1",
    "26.2.1",
    "26.3.1",
    "26.4.1",
    "26.5.1",
    "26.6.1",
    "26.7.1",
    "26.8.1",
    "26.9.1",
    "26.10.1",
]

# ---------------------------------------------------------------------------
# Required safety phrases: (file, phrase, is_boundary)
# ---------------------------------------------------------------------------
REQUIRED_SAFETY_PHRASES = [
    ("docs/PRE-MERGE-EXECUTION-CORRIDOR.md", "CI PASS is not approval", True),
    ("docs/PRE-MERGE-EXECUTION-CORRIDOR.md", "Evidence report is not approval", True),
    ("docs/PRE-MERGE-EXECUTION-CORRIDOR.md", "Auto-merge is forbidden", True),
    ("docs/PRE-MERGE-EXECUTION-CORRIDOR.md", "Automatic approval is forbidden", True),
    ("docs/AGENT-VIOLATION-POLICY.md", "Violation record is evidence, not approval", True),
    ("docs/AGENT-VIOLATION-POLICY.md", "Agent cannot clear its own violation", True),
    ("docs/NO-DIRECT-PUSH-POLICY.md", "Agent must not push directly to dev or main", True),
    ("docs/BOUNDED-RETRY-POLICY.md", "Retry is not approval", True),
    ("scripts/check-pre-merge-scope.py", "SCOPE_OK is not approval", True),
    ("scripts/check-commit-push-preconditions.py", "COMMIT_ALLOWED is not merge approval", True),
    ("scripts/check-commit-push-preconditions.py", "PUSH_ALLOWED is not merge approval", True),
    ("scripts/check-commit-push-preconditions.py", "PUSH_ALLOWED does not bypass M25", True),
]

# ---------------------------------------------------------------------------
# Required enum checks: (file, enums_list)
# ---------------------------------------------------------------------------
REQUIRED_ENUMS = [
    (
        "docs/AGENT-PERMISSION-MODEL.md",
        [
            "READ_ONLY",
            "PATCH_PROPOSE",
            "LOCAL_EDIT",
            "LOCAL_TEST",
            "COMMIT_REQUEST",
            "PUSH_REQUEST",
            "BLOCKED",
        ],
    ),
    (
        "docs/COMMAND-ALLOWLIST-POLICY.md",
        [
            "SAFE_READ",
            "SAFE_VALIDATE",
            "SAFE_TEST",
            "WRITE_LOCAL",
            "GIT_LOCAL",
            "GIT_REMOTE",
            "DANGEROUS",
            "FORBIDDEN",
        ],
    ),
    (
        "docs/WRITE-ALLOWLIST-POLICY.md",
        [
            "ALLOWED_WRITE_PATH",
            "CONDITIONAL_WRITE_PATH",
            "FORBIDDEN_WRITE_PATH",
            "PROTECTED_ZONE",
            "EVIDENCE_ARTIFACT",
            "GENERATED_ARTIFACT",
            "TEMP_ARTIFACT",
        ],
    ),
    (
        "scripts/check-pre-merge-scope.py",
        ["SCOPE_OK", "SCOPE_WARNING", "SCOPE_VIOLATION", "NEEDS_REVIEW"],
    ),
    (
        "scripts/check-commit-push-preconditions.py",
        ["COMMIT_ALLOWED", "PUSH_ALLOWED", "NEEDS_APPROVAL", "BLOCKED", "NEEDS_REVIEW"],
    ),
    (
        "docs/AGENT-VIOLATION-POLICY.md",
        [
            "SCOPE_VIOLATION",
            "FORBIDDEN_COMMAND",
            "FORBIDDEN_WRITE",
            "UNAPPROVED_PUSH",
            "DIRECT_PROTECTED_BRANCH_PUSH",
            "FORCE_PUSH_ATTEMPT",
            "REMOTE_BRANCH_DELETE_ATTEMPT",
            "VALIDATION_BYPASS",
            "EVIDENCE_TAMPERING",
            "PERMISSION_ESCALATION_ATTEMPT",
            "APPROVAL_SIMULATION",
            "AUTO_MERGE_ATTEMPT",
            "REPEATED_FAILURE",
            "UNBOUNDED_RETRY",
            "UNKNOWN_VIOLATION",
        ],
    ),
    (
        "docs/BOUNDED-RETRY-POLICY.md",
        [
            "RETRY_ALLOWED",
            "RETRY_ALLOWED_WITH_CONDITIONS",
            "NEEDS_HUMAN_REVIEW",
            "RETRY_BLOCKED",
            "RETRY_EXHAUSTED",
        ],
    ),
]

# ---------------------------------------------------------------------------
# Cross-consistency checks: (file, phrases_that_must_exist)
# ---------------------------------------------------------------------------
CROSS_CONSISTENCY_CHECKS = [
    ("docs/PRE-MERGE-EXECUTION-CORRIDOR.md", ["M25", "M26"]),
    ("docs/NO-DIRECT-PUSH-POLICY.md", ["dev", "main"]),
]

# ---------------------------------------------------------------------------
# Forbidden language checks
# ---------------------------------------------------------------------------
NEGATION_MARKERS = [
    "not",
    "no",
    "never",
    "forbidden",
    "must not",
    "is not",
    "does not",
    "cannot",
    "disallowed",
    "prohibited",
    "do not",
    "must never",
    "are not",
    "will not",
]

FORBIDDEN_PATTERNS = [
    "auto-merge allowed",
    "automatic approval allowed",
    "ci pass is approval",
    "evidence report is approval",
    "scope_ok authorizes commit",
    "scope_ok authorizes push",
    "commit_allowed authorizes merge",
    "push_allowed authorizes merge",
    "push_allowed bypasses m25",
    "retry authorizes merge",
    "violation record clears violation",
    "agent may clear its own violation",
]

FORBIDDEN_PATTERN_FILES = [
    "docs/PRE-MERGE-EXECUTION-CORRIDOR.md",
    "docs/AGENT-PERMISSION-MODEL.md",
    "docs/COMMAND-ALLOWLIST-POLICY.md",
    "docs/WRITE-ALLOWLIST-POLICY.md",
    "docs/NO-DIRECT-PUSH-POLICY.md",
    "docs/AGENT-VIOLATION-POLICY.md",
    "docs/BOUNDED-RETRY-POLICY.md",
    "templates/pre-merge-execution-review.md",
    "templates/agent-permission-record.md",
    "templates/command-approval-record.md",
    "templates/write-scope-record.md",
    "templates/push-request-record.md",
    "templates/agent-violation-record.md",
    "templates/retry-attempt-record.md",
]

# ---------------------------------------------------------------------------
# Policy-only known limitations
# ---------------------------------------------------------------------------
KNOWN_POLICY_ONLY_GAPS = [
    "violation_enforcement_script: NOT_IMPLEMENTED",
    "retry_enforcement_script: NOT_IMPLEMENTED",
    "write_enforcement: NOT_IMPLEMENTED",
    "command_enforcement: NOT_IMPLEMENTED",
]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def find_repo_root(start: str) -> str | None:
    current = os.path.abspath(start)
    while True:
        if os.path.isdir(os.path.join(current, ".git")):
            return current
        parent = os.path.dirname(current)
        if parent == current:
            return None
        current = parent


def read_file(path: str) -> str | None:
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return None


def line_has_negation(line: str, pattern: str) -> bool:
    line_lower = line.lower()
    idx = line_lower.find(pattern.lower())
    if idx == -1:
        return False
    prefix = line_lower[:idx]
    prefix_words = prefix.split()
    window = " ".join(prefix_words[-5:]) if len(prefix_words) >= 5 else prefix
    return any(marker in window for marker in NEGATION_MARKERS)


def merge_result(current: str, new: str) -> str:
    if RESULT_PRIORITY[new] > RESULT_PRIORITY[current]:
        return new
    return current

# ---------------------------------------------------------------------------
# Check functions
# ---------------------------------------------------------------------------

def check_artifact_existence(repo_root: str, checks, warnings, failures, needs_review):
    for rel_path in REQUIRED_ARTIFACTS:
        full_path = os.path.join(repo_root, rel_path)
        if os.path.isfile(full_path):
            checks.append(f"PASS  artifact_exists: {rel_path}")
        else:
            failures.append(f"FAIL  artifact_missing: {rel_path}")


def check_required_enums(repo_root: str, checks, warnings, failures, needs_review):
    for rel_path, enums in REQUIRED_ENUMS:
        full_path = os.path.join(repo_root, rel_path)
        content = read_file(full_path)
        if content is None:
            failures.append(f"FAIL  enum_check_skipped (file unreadable): {rel_path}")
            continue
        for enum in enums:
            if enum in content:
                checks.append(f"PASS  enum_present: {enum} in {rel_path}")
            else:
                failures.append(f"FAIL  enum_missing: {enum} not found in {rel_path}")


def check_cross_consistency(repo_root: str, checks, warnings, failures, needs_review):
    for rel_path, phrases in CROSS_CONSISTENCY_CHECKS:
        full_path = os.path.join(repo_root, rel_path)
        content = read_file(full_path)
        if content is None:
            failures.append(f"FAIL  cross_consistency_skipped (file unreadable): {rel_path}")
            continue
        for phrase in phrases:
            if phrase in content:
                checks.append(f"PASS  cross_consistency: '{phrase}' in {rel_path}")
            else:
                failures.append(f"FAIL  cross_consistency_missing: '{phrase}' not in {rel_path}")


def check_safety_phrases(repo_root: str, checks, warnings, failures, needs_review):
    for rel_path, phrase, is_boundary in REQUIRED_SAFETY_PHRASES:
        full_path = os.path.join(repo_root, rel_path)
        content = read_file(full_path)
        if content is None:
            target = failures if is_boundary else needs_review
            prefix = "FAIL" if is_boundary else "NEEDS_REVIEW"
            target.append(
                f"{prefix}  safety_phrase_skipped: '{phrase}' in {rel_path}"
            )
            continue

        if phrase.lower() in content.lower():
            checks.append(f"PASS  safety_phrase: '{phrase}' in {rel_path}")
        elif is_boundary:
            failures.append(
                f"FAIL  safety_phrase_missing (boundary): '{phrase}' not found in {rel_path}"
            )
        else:
            needs_review.append(
                f"NEEDS_REVIEW  safety_phrase_missing: '{phrase}' not found in {rel_path}"
            )


def check_forbidden_language(repo_root: str, checks, warnings, failures, needs_review):
    for rel_path in FORBIDDEN_PATTERN_FILES:
        full_path = os.path.join(repo_root, rel_path)
        content = read_file(full_path)
        if content is None:
            continue

        file_clean = True
        for line_num, line in enumerate(content.splitlines(), 1):
            line_lower = line.lower()
            for pattern in FORBIDDEN_PATTERNS:
                if pattern in line_lower:
                    if line_has_negation(line, pattern):
                        checks.append(
                            f"PASS  forbidden_language_negated: '{pattern}' "
                            f"line {line_num} in {rel_path}"
                        )
                    else:
                        failures.append(
                            f"FAIL  forbidden_language: '{pattern}' "
                            f"line {line_num} in {rel_path}"
                        )
                        file_clean = False

        if file_clean:
            checks.append(f"PASS  forbidden_language_clean: {rel_path}")


def check_evidence_entries(repo_root: str, checks, warnings, failures, needs_review):
    rel_path = "reports/milestone-26-evidence-report.md"
    full_path = os.path.join(repo_root, rel_path)
    content = read_file(full_path)
    if content is None:
        failures.append(f"FAIL  evidence_report_unreadable: {rel_path}")
        return

    for task_id in REQUIRED_EVIDENCE_ENTRIES:
        marker = f"task_id: {task_id}"
        if marker in content:
            checks.append(f"PASS  evidence_entry_present: {task_id}")
        else:
            needs_review.append(
                f"NEEDS_REVIEW  evidence_entry_missing: {task_id} not found in {rel_path}"
            )


def check_policy_only_gaps(repo_root: str, checks, warnings, failures, needs_review):
    rel_path = "reports/milestone-26-evidence-report.md"
    full_path = os.path.join(repo_root, rel_path)
    content = read_file(full_path)
    if content is None:
        return

    for gap in KNOWN_POLICY_ONLY_GAPS:
        if gap in content:
            warnings.append(
                f"WARNING  policy_only_gap: '{gap}' in {rel_path}"
            )
        else:
            checks.append(f"PASS  policy_only_gap_not_present: '{gap}'")


def check_script_read_only(repo_root: str, checks, warnings, failures, needs_review):
    """
    Conservative self-check.

    This avoids scanning for plain text phrases like 'git push' because those
    phrases can legitimately appear in comments, documentation strings, or the
    scan rules themselves. Instead it looks for obvious mutating call snippets.
    This is not full static analysis.
    """
    script_path = os.path.join(repo_root, "scripts/audit-pre-merge-corridor.py")
    content = read_file(script_path)
    if content is None:
        needs_review.append(
            "NEEDS_REVIEW  script_self_check_skipped: cannot read own source"
        )
        return

    forbidden_snippets = [
        '["git", "commit"]',
        "['git', 'commit']",
        '["git", "push"]',
        "['git', 'push']",
        '["git", "merge"]',
        "['git', 'merge']",
        "os.system(",
        "subprocess.run(",
        ".write_text(",
        ".unlink(",
        ".rename(",
        ".replace(",
        "shutil.rmtree(",
        "shutil.move(",
    ]

    found = False
    for snippet in forbidden_snippets:
        if snippet in content:
            failures.append(f"FAIL  script_contains_mutating_snippet: {snippet}")
            found = True

    if not found:
        checks.append("PASS  script_self_check: no mutating snippets found")

# ---------------------------------------------------------------------------
# Result computation
# ---------------------------------------------------------------------------

def compute_result(checks, warnings, failures, needs_review) -> str:
    result = CORRIDOR_READY
    if warnings:
        result = merge_result(result, READY_WITH_WARNINGS)
    if needs_review:
        result = merge_result(result, NEEDS_REVIEW)
    if failures:
        result = merge_result(result, NOT_READY)
    return result

# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

DISCLAIMER = (
    "This audit is read-only. "
    "CORRIDOR_READY is not approval. "
    "CORRIDOR_READY does not authorize commit, push, merge, or release. "
    "This audit does not override M25."
)


def output_human(result, checks, warnings, failures, needs_review):
    print("=" * 70)
    print("M26 Pre-Merge Corridor Audit — Task 26.10.1")
    print("=" * 70)
    print()

    if checks:
        print(f"--- PASSED ({len(checks)}) ---")
        for c in checks:
            print(f"  {c}")
        print()

    if warnings:
        print(f"--- WARNINGS ({len(warnings)}) ---")
        for w in warnings:
            print(f"  {w}")
        print()

    if needs_review:
        print(f"--- NEEDS REVIEW ({len(needs_review)}) ---")
        for n in needs_review:
            print(f"  {n}")
        print()

    if failures:
        print(f"--- FAILURES ({len(failures)}) ---")
        for f in failures:
            print(f"  {f}")
        print()

    print("=" * 70)
    print(f"RESULT: {result}")
    print("=" * 70)
    print()
    print(f"DISCLAIMER: {DISCLAIMER}")
    print()


def output_json(result, checks, warnings, failures, needs_review):
    data = {
        "result": result,
        "checks": {
            "passed": checks,
            "warnings": warnings,
            "failures": failures,
            "needs_review": needs_review,
        },
        "summary": {
            "passed_count": len(checks),
            "warnings_count": len(warnings),
            "failures_count": len(failures),
            "needs_review_count": len(needs_review),
        },
        "disclaimer": DISCLAIMER,
    }
    print(json.dumps(data, indent=2))

# ---------------------------------------------------------------------------
# Exit code
# ---------------------------------------------------------------------------

def get_exit_code(result: str, strict: bool) -> int:
    if strict:
        return 0 if result == CORRIDOR_READY else 1
    if result == CORRIDOR_READY:
        return 0
    if result == READY_WITH_WARNINGS:
        return 0
    if result == NEEDS_REVIEW:
        return 1
    if result == NOT_READY:
        return 2
    return 2

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="M26 Pre-Merge Corridor Audit Script (read-only)"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output JSON instead of human-readable report",
    )
    parser.add_argument(
        "--repo-root",
        default=None,
        help="Path to repository root (default: auto-detect from cwd)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero for READY_WITH_WARNINGS and NEEDS_REVIEW",
    )
    args = parser.parse_args()

    if args.repo_root:
        repo_root = os.path.abspath(args.repo_root)
        if not os.path.isdir(repo_root):
            print(f"ERROR: --repo-root path does not exist: {repo_root}", file=sys.stderr)
            sys.exit(2)
    else:
        repo_root = find_repo_root(os.getcwd())
        if repo_root is None:
            print(
                "ERROR: REPO_ROOT_NOT_FOUND — could not find .git directory "
                "from current working directory. Use --repo-root to specify path.",
                file=sys.stderr,
            )
            sys.exit(2)

    checks = []
    warnings = []
    failures = []
    needs_review = []

    check_artifact_existence(repo_root, checks, warnings, failures, needs_review)
    check_required_enums(repo_root, checks, warnings, failures, needs_review)
    check_cross_consistency(repo_root, checks, warnings, failures, needs_review)
    check_safety_phrases(repo_root, checks, warnings, failures, needs_review)
    check_forbidden_language(repo_root, checks, warnings, failures, needs_review)
    check_evidence_entries(repo_root, checks, warnings, failures, needs_review)
    check_policy_only_gaps(repo_root, checks, warnings, failures, needs_review)
    check_script_read_only(repo_root, checks, warnings, failures, needs_review)

    result = compute_result(checks, warnings, failures, needs_review)

    if args.json:
        output_json(result, checks, warnings, failures, needs_review)
    else:
        output_human(result, checks, warnings, failures, needs_review)

    sys.exit(get_exit_code(result, args.strict))


if __name__ == "__main__":
    main()
