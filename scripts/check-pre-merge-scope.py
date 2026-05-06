#!/usr/bin/env python3
"""
check-pre-merge-scope.py — M26 Scope-Bound Diff Checker

Read-only. Does not stage, commit, push, edit files, or approve anything.
SCOPE_OK is not approval. SCOPE_OK does not authorize commit, push, or merge.
This checker does not override M25.
"""

import argparse
import fnmatch
import json
import subprocess
import sys
from pathlib import Path

import yaml


RESULT_OK = "SCOPE_OK"
RESULT_WARNING = "SCOPE_WARNING"
RESULT_VIOLATION = "SCOPE_VIOLATION"
RESULT_NEEDS_REVIEW = "NEEDS_REVIEW"

SUPPORTED_STATUSES = {"A", "M", "D", "R"}

# Hard-blocked paths. Explicit task scope must not downgrade these to OK.
ALWAYS_BLOCKED_PATTERNS = [
    ".github/workflows/",
    "reports/milestone-25-*",
    "reports/platform-required-checks-evidence.md",
]

# High-risk paths. If explicitly declared + allowed, they produce warning, not OK.
PROTECTED_BY_DEFAULT_PATTERNS = [
    "scripts/",
    "tests/",
    "docs/PRE-MERGE-EXECUTION-CORRIDOR.md",
    "docs/AGENT-PERMISSION-MODEL.md",
    "docs/COMMAND-ALLOWLIST-POLICY.md",
    "docs/WRITE-ALLOWLIST-POLICY.md",
    "docs/ENFORCEMENT-OVERRIDE-POLICY.md",
    "templates/enforcement-review.md",
]

TEMP_ARTIFACT_PATTERNS = [
    ".coverage",
    "htmlcov/",
    ".pytest_cache/",
    "__pycache__/",
    "*.pyc",
    "*.tmp",
    "*.log",
]


def normalize_path(path: str) -> str:
    value = str(path).strip().replace("\\", "/")
    while value.startswith("./"):
        value = value[2:]
    return value


def match_path(file_path: str, pattern: str) -> bool:
    file_path = normalize_path(file_path)
    pattern = normalize_path(pattern)

    if pattern.endswith("/"):
        return file_path.startswith(pattern) or file_path == pattern.rstrip("/")

    if "*" in pattern:
        return fnmatch.fnmatch(file_path, pattern)

    return file_path == pattern


def matches_any(file_path: str, patterns: list) -> bool:
    return any(match_path(file_path, pattern) for pattern in (patterns or []))


def validate_pattern_list(field_name: str, patterns: list) -> list:
    errors = []

    if not isinstance(patterns, list):
        return [f"{field_name} must be a list."]

    for index, pattern in enumerate(patterns):
        if not isinstance(pattern, str):
            errors.append(f"{field_name}[{index}] must be a string.")
            continue

        normalized = normalize_path(pattern)

        if not normalized:
            errors.append(f"{field_name}[{index}] is empty.")
        if normalized.startswith("/"):
            errors.append(f"{field_name}[{index}] must be repository-relative, not absolute.")
        if ".." in normalized.split("/"):
            errors.append(f"{field_name}[{index}] must not contain '..'.")
        if "**" in normalized:
            errors.append(f"{field_name}[{index}] contains unsupported recursive glob '**'.")

    return errors


def load_scope(scope_file: str) -> tuple:
    path = Path(scope_file)

    if not path.exists():
        return None, f"Scope file not found: {scope_file}"
    if not path.is_file():
        return None, f"Scope file is not a file: {scope_file}"

    try:
        with path.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
    except yaml.YAMLError as exc:
        return None, f"Invalid YAML in scope file: {exc}"

    if not isinstance(data, dict):
        return None, "Scope file must be a YAML mapping."

    declared_scope = data.get("declared_scope")
    allowed_write_paths = data.get("allowed_write_paths")

    if not declared_scope:
        return None, "Scope file missing or empty 'declared_scope'."
    if not isinstance(declared_scope, list):
        return None, "'declared_scope' must be a list."

    if not allowed_write_paths:
        return None, "Scope file missing or empty 'allowed_write_paths'."
    if not isinstance(allowed_write_paths, list):
        return None, "'allowed_write_paths' must be a list."

    optional_fields = [
        "conditional_write_paths",
        "forbidden_write_paths",
        "protected_zones",
        "deletions_allowed",
        "evidence_artifacts",
    ]

    for field in optional_fields:
        if field not in data or data[field] is None:
            data[field] = []
        if not isinstance(data[field], list):
            return None, f"'{field}' must be a list."

    pattern_errors = []
    for field in [
        "declared_scope",
        "allowed_write_paths",
        "conditional_write_paths",
        "forbidden_write_paths",
        "protected_zones",
        "deletions_allowed",
        "evidence_artifacts",
    ]:
        pattern_errors.extend(validate_pattern_list(field, data.get(field, [])))

    if pattern_errors:
        return None, "Ambiguous or invalid path pattern(s): " + "; ".join(pattern_errors)

    return data, None


def normalize_status(raw_status: str) -> str:
    value = raw_status.strip().upper()
    if value.startswith("R"):
        return "R"
    return value


def validate_changed_path(file_path: str):
    normalized = normalize_path(file_path)

    if not normalized:
        return "changed file path is empty"
    if normalized.startswith("/"):
        return "changed file path must be repository-relative, not absolute"
    if ".." in normalized.split("/"):
        return "changed file path must not contain '..'"

    return None


def parse_changed_line(line: str, line_num: int) -> tuple:
    parts = line.split(None, 1)
    if len(parts) != 2:
        return None, f"Line {line_num}: invalid format '{line}' (expected: STATUS path)"

    raw_status, raw_path = parts
    status = normalize_status(raw_status)

    if status not in SUPPORTED_STATUSES:
        return None, f"Line {line_num}: unsupported change status '{raw_status}' in '{line}'"

    raw_path = raw_path.strip()

    if status == "R":
        if " -> " in raw_path:
            old_path, new_path = raw_path.split(" -> ", 1)
            old_path = normalize_path(old_path)
            new_path = normalize_path(new_path)
            old_error = validate_changed_path(old_path)
            new_error = validate_changed_path(new_path)
            if old_error or new_error:
                return None, f"Line {line_num}: invalid rename path: {old_error or new_error}"
            return ("R", f"{old_path} -> {new_path}"), None

        if "\t" in raw_path:
            rename_parts = [normalize_path(part) for part in raw_path.split("\t") if part.strip()]
            if len(rename_parts) == 2:
                old_error = validate_changed_path(rename_parts[0])
                new_error = validate_changed_path(rename_parts[1])
                if old_error or new_error:
                    return None, f"Line {line_num}: invalid rename path: {old_error or new_error}"
                return ("R", f"{rename_parts[0]} -> {rename_parts[1]}"), None

        return ("R", normalize_path(raw_path)), None

    file_path = normalize_path(raw_path)
    path_error = validate_changed_path(file_path)
    if path_error:
        return None, f"Line {line_num}: {path_error}"

    return (status, file_path), None


def load_changed_files_from_file(changed_files_path: str) -> tuple:
    path = Path(changed_files_path)

    if not path.exists():
        return None, f"Changed files input not found: {changed_files_path}"
    if not path.is_file():
        return None, f"Changed files input is not a file: {changed_files_path}"

    entries = []

    with path.open("r", encoding="utf-8") as file:
        for line_num, line in enumerate(file, 1):
            line = line.rstrip("\n").strip()
            if not line:
                continue

            entry, error = parse_changed_line(line, line_num)
            if error:
                return None, error
            entries.append(entry)

    if not entries:
        return None, "Changed files input is empty."

    return entries, None


def run_git_command(command: list) -> tuple:
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip(), None
    except subprocess.CalledProcessError as exc:
        return "", exc.stderr.strip() or str(exc)
    except FileNotFoundError:
        return "", "git not found in PATH."


def parse_git_name_status(output: str) -> tuple:
    entries = []

    for line in output.splitlines():
        line = line.strip()
        if not line:
            continue

        parts = line.split("\t")
        raw_status = parts[0].strip().upper()
        status = normalize_status(raw_status)

        if status not in SUPPORTED_STATUSES:
            return None, f"Unsupported git status '{raw_status}' in line: '{line}'"

        if status == "R":
            if len(parts) < 3:
                return None, f"Could not parse git rename line: '{line}'"
            old_path = normalize_path(parts[1])
            new_path = normalize_path(parts[2])
            entries.append(("R", f"{old_path} -> {new_path}"))
        else:
            if len(parts) < 2:
                return None, f"Could not parse git status line: '{line}'"
            entries.append((status, normalize_path(parts[1])))

    return entries, None


def load_changed_files_from_git() -> tuple:
    combined = []

    for command in [
        ["git", "diff", "--name-status"],
        ["git", "diff", "--name-status", "--cached"],
    ]:
        output, error = run_git_command(command)
        if error:
            return None, f"{' '.join(command)} failed: {error}"

        parsed, parse_error = parse_git_name_status(output)
        if parse_error:
            return None, parse_error

        combined.extend(parsed)

    untracked_output, error = run_git_command(["git", "ls-files", "--others", "--exclude-standard"])
    if error:
        return None, f"git ls-files failed: {error}"

    for line in untracked_output.splitlines():
        path = normalize_path(line)
        if path:
            combined.append(("A", path))

    seen = set()
    deduped = []

    for entry in combined:
        if entry not in seen:
            seen.add(entry)
            deduped.append(entry)

    # Empty git diff is valid: no changed files means SCOPE_OK.
    return deduped, None


def parse_rename(file_path: str) -> tuple:
    if " -> " not in file_path:
        return None, None

    old_path, new_path = file_path.split(" -> ", 1)
    old_path = normalize_path(old_path)
    new_path = normalize_path(new_path)

    if not old_path or not new_path:
        return None, None

    return old_path, new_path


def check_scope(scope: dict, changed_files: list) -> dict:
    declared_scope = scope.get("declared_scope", [])
    allowed_write_paths = scope.get("allowed_write_paths", [])
    conditional_write_paths = scope.get("conditional_write_paths", [])
    forbidden_write_paths = scope.get("forbidden_write_paths", [])
    protected_zones = scope.get("protected_zones", [])
    deletions_allowed = scope.get("deletions_allowed", [])
    evidence_artifacts = scope.get("evidence_artifacts", [])

    violations = []
    warnings = []
    needs_review = []

    # Empty diff is valid: no changes = SCOPE_OK.
    for status, file_path in changed_files:
        if status == "R":
            old_path, new_path = parse_rename(file_path)

            if old_path is None:
                needs_review.append({
                    "file": file_path,
                    "reason": "rename_parse_failed",
                    "detail": "Could not parse rename format; expected 'old -> new'.",
                })
                continue

            _check_deletion(
                old_path,
                declared_scope,
                deletions_allowed,
                forbidden_write_paths,
                protected_zones,
                evidence_artifacts,
                violations,
            )
            _check_write(
                new_path,
                declared_scope,
                allowed_write_paths,
                conditional_write_paths,
                forbidden_write_paths,
                protected_zones,
                evidence_artifacts,
                violations,
                warnings,
            )
            continue

        if status == "D":
            _check_deletion(
                file_path,
                declared_scope,
                deletions_allowed,
                forbidden_write_paths,
                protected_zones,
                evidence_artifacts,
                violations,
            )
            continue

        _check_write(
            file_path,
            declared_scope,
            allowed_write_paths,
            conditional_write_paths,
            forbidden_write_paths,
            protected_zones,
            evidence_artifacts,
            violations,
            warnings,
        )

    if violations:
        result = RESULT_VIOLATION
    elif needs_review:
        result = RESULT_NEEDS_REVIEW
    elif warnings:
        result = RESULT_WARNING
    else:
        result = RESULT_OK

    return {
        "result": result,
        "violations": violations,
        "warnings": warnings,
        "needs_review": needs_review,
        "disclaimer": (
            "SCOPE_OK is not approval. "
            "SCOPE_OK does not authorize commit, push, or merge. "
            "This checker does not override M25."
        ),
    }


def _check_write(
    file_path,
    declared_scope,
    allowed_write_paths,
    conditional_write_paths,
    forbidden_write_paths,
    protected_zones,
    evidence_artifacts,
    violations,
    warnings,
):
    file_path = normalize_path(file_path)

    if matches_any(file_path, evidence_artifacts):
        violations.append({
            "file": file_path,
            "reason": "evidence_artifact_tampering",
            "category": "EVIDENCE_ARTIFACT",
            "detail": "Modification of evidence artifact detected.",
        })
        return

    if matches_any(file_path, ALWAYS_BLOCKED_PATTERNS):
        violations.append({
            "file": file_path,
            "reason": "baseline_blocked_path",
            "category": "FORBIDDEN_WRITE_PATH",
            "detail": "Path is in the M26 baseline blocked list.",
        })
        return

    if matches_any(file_path, forbidden_write_paths):
        violations.append({
            "file": file_path,
            "reason": "forbidden_write_path",
            "category": "FORBIDDEN_WRITE_PATH",
            "detail": "Path is listed in forbidden_write_paths in scope file.",
        })
        return

    in_declared_scope = matches_any(file_path, declared_scope)
    in_allowed_write_paths = matches_any(file_path, allowed_write_paths)
    in_conditional_write_paths = matches_any(file_path, conditional_write_paths)
    in_protected_zone = (
        matches_any(file_path, protected_zones)
        or matches_any(file_path, PROTECTED_BY_DEFAULT_PATTERNS)
    )

    if not in_declared_scope:
        violations.append({
            "file": file_path,
            "reason": "out_of_declared_scope",
            "category": "OUT_OF_SCOPE",
            "detail": "File is not within declared_scope.",
        })
        return

    if not in_allowed_write_paths:
        if in_conditional_write_paths:
            warnings.append({
                "file": file_path,
                "reason": "conditional_write_path",
                "category": "CONDITIONAL_WRITE_PATH",
                "detail": "Path is conditional; human reviewer approval required.",
            })
        else:
            detail = "File is in declared_scope but not in allowed_write_paths."
            if in_protected_zone:
                detail += " Path is also protected/high-risk; explicit allowance and owner review may be required."

            violations.append({
                "file": file_path,
                "reason": "not_in_allowed_write_paths",
                "category": "WRITE_NOT_ALLOWED",
                "detail": detail,
            })
        return

    if in_protected_zone:
        warnings.append({
            "file": file_path,
            "reason": "protected_path_explicitly_scoped",
            "category": "PROTECTED_ZONE",
            "detail": "Protected/high-risk path is explicitly scoped; owner review may still be required.",
        })
        return

    if in_conditional_write_paths:
        warnings.append({
            "file": file_path,
            "reason": "conditional_write_path",
            "category": "CONDITIONAL_WRITE_PATH",
            "detail": "Path is conditional; human reviewer approval required.",
        })
        return

    if file_path.startswith("reports/") and "milestone-25" not in file_path:
        warnings.append({
            "file": file_path,
            "reason": "reports_path_touched",
            "category": "SCOPE_WARNING",
            "detail": "Reports path touched; verify this is an authorized append if evidence-related.",
        })
        return

    if matches_any(file_path, TEMP_ARTIFACT_PATTERNS):
        warnings.append({
            "file": file_path,
            "reason": "temp_artifact_detected",
            "category": "TEMP_ARTIFACT",
            "detail": "Temporary/cache artifact detected; must remain uncommitted and documented.",
        })


def _check_deletion(
    file_path,
    declared_scope,
    deletions_allowed,
    forbidden_write_paths,
    protected_zones,
    evidence_artifacts,
    violations,
):
    file_path = normalize_path(file_path)

    if matches_any(file_path, evidence_artifacts):
        violations.append({
            "file": file_path,
            "reason": "evidence_artifact_deletion",
            "category": "EVIDENCE_ARTIFACT",
            "detail": "Deletion of evidence artifact is forbidden.",
        })
        return

    if matches_any(file_path, ALWAYS_BLOCKED_PATTERNS):
        violations.append({
            "file": file_path,
            "reason": "baseline_blocked_path_deletion",
            "category": "FORBIDDEN_WRITE_PATH",
            "detail": "Deletion of baseline blocked path is not allowed.",
        })
        return

    if matches_any(file_path, forbidden_write_paths):
        violations.append({
            "file": file_path,
            "reason": "forbidden_write_path_deletion",
            "category": "FORBIDDEN_WRITE_PATH",
            "detail": "Deletion of forbidden write path is not allowed.",
        })
        return

    if matches_any(file_path, protected_zones) or matches_any(file_path, PROTECTED_BY_DEFAULT_PATTERNS):
        violations.append({
            "file": file_path,
            "reason": "protected_path_deletion",
            "category": "PROTECTED_ZONE",
            "detail": "Deletion of protected/high-risk path requires owner-controlled review.",
        })
        return

    if not matches_any(file_path, deletions_allowed):
        violations.append({
            "file": file_path,
            "reason": "unapproved_deletion",
            "category": "DELETION_NOT_ALLOWED",
            "detail": "Deletion not listed in deletions_allowed in scope file.",
        })
        return

    if not matches_any(file_path, declared_scope):
        violations.append({
            "file": file_path,
            "reason": "out_of_scope_deletion",
            "category": "OUT_OF_SCOPE",
            "detail": "Deletion target is not within declared_scope.",
        })


def format_human(report: dict) -> str:
    lines = [f"Result: {report['result']}", ""]

    if report["violations"]:
        lines.append(f"Violations ({len(report['violations'])}):")
        for violation in report["violations"]:
            lines.append(f"  VIOLATION  [{violation['category']}]  {violation['file']}")
            lines.append(f"             {violation['reason']}: {violation['detail']}")
        lines.append("")

    if report["warnings"]:
        lines.append(f"Warnings ({len(report['warnings'])}):")
        for warning in report["warnings"]:
            lines.append(f"  WARNING    [{warning['category']}]  {warning['file']}")
            lines.append(f"             {warning['reason']}: {warning['detail']}")
        lines.append("")

    if report["needs_review"]:
        lines.append(f"Needs Review ({len(report['needs_review'])}):")
        for item in report["needs_review"]:
            lines.append(f"  REVIEW     {item.get('file', '(unknown)')}")
            lines.append(f"             {item['reason']}: {item['detail']}")
        lines.append("")

    lines.append(f"Notice: {report['disclaimer']}")
    return "\n".join(lines)


def format_json(report: dict) -> str:
    return json.dumps(report, indent=2)


EXIT_CODES = {
    RESULT_OK: 0,
    RESULT_WARNING: 1,
    RESULT_VIOLATION: 2,
    RESULT_NEEDS_REVIEW: 3,
}


def make_needs_review_report(file_path: str, reason: str, detail: str) -> dict:
    return {
        "result": RESULT_NEEDS_REVIEW,
        "error": detail,
        "violations": [],
        "warnings": [],
        "needs_review": [{
            "file": file_path,
            "reason": reason,
            "detail": detail,
        }],
        "disclaimer": (
            "SCOPE_OK is not approval. "
            "SCOPE_OK does not authorize commit, push, or merge. "
            "This checker does not override M25."
        ),
    }


def main():
    parser = argparse.ArgumentParser(
        description="M26 Scope-Bound Diff Checker. Read-only. SCOPE_OK is not approval."
    )
    parser.add_argument("--scope-file", required=True, help="Path to YAML scope file.")
    parser.add_argument("--changed-files", help="Path to changed files list.")
    parser.add_argument(
        "--git",
        action="store_true",
        help="Load changed files from git diff, cached diff, and untracked files.",
    )
    parser.add_argument("--json", action="store_true", dest="output_json", help="Output JSON.")

    args = parser.parse_args()

    if not args.changed_files and not args.git:
        report = make_needs_review_report(
            "(none)",
            "missing_changed_files_input",
            "Must provide --changed-files or --git.",
        )
        print(format_json(report) if args.output_json else format_human(report))
        sys.exit(EXIT_CODES[RESULT_NEEDS_REVIEW])

    scope, scope_error = load_scope(args.scope_file)
    if scope_error:
        report = make_needs_review_report(args.scope_file, "scope_load_error", scope_error)
        print(format_json(report) if args.output_json else format_human(report))
        sys.exit(EXIT_CODES[RESULT_NEEDS_REVIEW])

    if args.git:
        changed_files, changed_error = load_changed_files_from_git()
    else:
        changed_files, changed_error = load_changed_files_from_file(args.changed_files)

    if changed_error:
        report = make_needs_review_report(
            str(args.changed_files),
            "changed_files_load_error",
            changed_error,
        )
        print(format_json(report) if args.output_json else format_human(report))
        sys.exit(EXIT_CODES[RESULT_NEEDS_REVIEW])

    report = check_scope(scope, changed_files)
    print(format_json(report) if args.output_json else format_human(report))
    sys.exit(EXIT_CODES.get(report["result"], EXIT_CODES[RESULT_NEEDS_REVIEW]))


if __name__ == "__main__":
    main()
