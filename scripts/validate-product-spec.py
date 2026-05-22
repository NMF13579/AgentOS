#!/usr/bin/env python3
import argparse
import json
import pathlib
import re
import sys
from datetime import datetime, timezone

TOKEN_OK = "PRODUCT_SPEC_VALIDATION_OK"
TOKEN_FAILED = "PRODUCT_SPEC_VALIDATION_FAILED"
TOKEN_BLOCKED = "PRODUCT_SPEC_VALIDATION_BLOCKED"

EXIT_BY_TOKEN = {
    TOKEN_OK: 0,
    TOKEN_FAILED: 1,
    TOKEN_BLOCKED: 2,
}

ALLOWED_FRONTMATTER_STATUS = {
    "draft", "active", "canonical", "archived", "deprecated", "unknown"
}
FORBIDDEN_FRONTMATTER_STATUS = {
    "DRAFT", "INTERVIEWING", "NEEDS_CLARIFICATION", "REVIEW",
    "APPROVED", "EXECUTION_READY", "ARCHIVED"
}
ALLOWED_LIFECYCLE = {
    "DRAFT", "INTERVIEWING", "NEEDS_CLARIFICATION", "REVIEW",
    "APPROVED", "EXECUTION_READY", "ARCHIVED"
}
REQUIRED_FRONTMATTER_FIELDS = [
    "type", "module", "status", "authority", "created", "last_validated", "spec_id"
]
REQUIRED_HEADINGS = [
    "Problem", "Users", "Jobs-To-Be-Done", "Goals", "Non-Goals", "Constraints",
    "Risks", "Success Metrics", "Acceptance Criteria", "Dependencies", "Open Questions"
]
FORBIDDEN_PHRASES = [
    "Product Spec authorizes execution",
    "Product Spec authorizes deployment",
    "Product Spec authorizes commit",
    "Product Spec authorizes push",
    "Product Spec authorizes merge",
    "Product Spec creates approval",
    "Product Spec replaces human gate",
    "Product Spec overrides runtime enforcement",
    "AI may approve Product Specs",
    "AI may mark Product Specs as EXECUTION_READY",
]
FOUNDATION_FILES = [
    "docs/PRODUCT-SPEC-ARCHITECTURE.md",
    "docs/PRODUCT-SPEC-LIFECYCLE.md",
    "docs/PRODUCT-SPEC-TRANSITION-POLICY.md",
    "docs/SPEC-TO-TASK-LINEAGE.md",
    "schemas/product-spec.schema.json",
    "schemas/spec-lineage.schema.json",
    "templates/PRODUCT-SPEC.md",
    "examples/product-spec-example.md",
]


def build_result(token, target, errors=None, warnings=None):
    return {
        "result": token,
        "file": target,
        "errors": errors or [],
        "warnings": warnings or [],
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    }


def print_result(payload, as_json=False):
    if as_json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return
    print(f"{payload['result']} :: {payload['file']}")
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


def extract_frontmatter(text):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, None, "frontmatter opening delimiter '---' is missing"

    end_index = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_index = i
            break
    if end_index is None:
        return None, None, "frontmatter closing delimiter '---' is missing"

    raw = lines[1:end_index]
    data = {}
    kv_pattern = re.compile(r"^([A-Za-z0-9_-]+):\s*(.*)$")
    for line in raw:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        m = kv_pattern.match(line)
        if not m:
            continue
        key = m.group(1).strip()
        value = m.group(2).strip().strip('"').strip("'")
        data[key] = value

    body = "\n".join(lines[end_index + 1:])
    return data, body, None


def section_exists(body, name):
    pattern = re.compile(rf"^###?\s+{re.escape(name)}\s*$", re.MULTILINE)
    return bool(pattern.search(body))


def find_section_content(body, heading):
    lines = body.splitlines()
    start = None
    header_re = re.compile(rf"^###?\s+{re.escape(heading)}\s*$")
    next_header_re = re.compile(r"^###?\s+")
    for idx, line in enumerate(lines):
        if header_re.match(line.strip()):
            start = idx + 1
            break
    if start is None:
        return ""
    out = []
    for idx in range(start, len(lines)):
        line = lines[idx]
        if next_header_re.match(line.strip()):
            break
        out.append(line)
    return "\n".join(out).strip()


def parse_lifecycle_status(body):
    m = re.search(r"^\s*lifecycle_status\s*:\s*\"?([A-Za-z_]+)\"?\s*$", body, re.MULTILINE)
    if not m:
        return None
    return m.group(1).strip()


def validate_file(path, root):
    missing_foundation = check_foundation(root)
    if missing_foundation:
        return build_result(
            TOKEN_BLOCKED,
            str(path),
            ["missing required foundation artifact(s): " + ", ".join(missing_foundation)],
        )

    p = pathlib.Path(path)
    if not p.is_absolute():
        p = root / p

    if not p.is_file():
        return build_result(TOKEN_BLOCKED, str(path), ["file does not exist"])

    try:
        text = p.read_text(encoding="utf-8")
    except Exception as exc:
        return build_result(TOKEN_BLOCKED, str(path), [f"file is not readable: {exc}"])

    frontmatter, body, fm_error = extract_frontmatter(text)
    if fm_error:
        return build_result(TOKEN_BLOCKED, str(path), [fm_error])

    errors = []
    warnings = []

    for key in REQUIRED_FRONTMATTER_FIELDS:
        value = frontmatter.get(key, "")
        if not value:
            errors.append(f"missing required frontmatter field: {key}")

    status = frontmatter.get("status", "")
    if status and status not in ALLOWED_FRONTMATTER_STATUS:
        errors.append(f"invalid frontmatter status: {status}")
    if status in FORBIDDEN_FRONTMATTER_STATUS:
        errors.append("frontmatter status uses Product Spec lifecycle value in uppercase")

    lifecycle = parse_lifecycle_status(body)
    if lifecycle is None:
        errors.append("missing body lifecycle_status")
    elif lifecycle not in ALLOWED_LIFECYCLE:
        errors.append(f"invalid lifecycle_status: {lifecycle}")

    for heading in REQUIRED_HEADINGS:
        if not section_exists(body, heading):
            errors.append(f"missing required section heading: {heading}")

    if not section_exists(body, "Goals"):
        errors.append("missing Goals section")
    if not section_exists(body, "Success Metrics"):
        errors.append("missing Success Metrics section")
    if not section_exists(body, "Non-Goals"):
        errors.append("missing Non-Goals section")

    open_questions = find_section_content(body, "Open Questions")
    if not open_questions:
        warnings.append("Open Questions section is present but appears empty")
    open_text_lower = open_questions.lower()
    unresolved = bool(open_questions) and ("none" not in open_text_lower and "resolved" not in open_text_lower)

    ack_marker = re.search(r"^\s*open_questions_acknowledged_by_human\s*:\s*true\s*$", body, re.MULTILINE)
    block_marker = re.search(r"^\s*open_questions_block_execution_ready\s*:\s*true\s*$", body, re.MULTILINE)

    if lifecycle == "APPROVED" and unresolved and not ack_marker:
        errors.append("APPROVED with unresolved Open Questions requires open_questions_acknowledged_by_human: true")

    if lifecycle == "EXECUTION_READY" and unresolved and block_marker:
        errors.append("EXECUTION_READY with blocking unresolved Open Questions is not allowed")

    if not section_exists(body, "Lineage"):
        errors.append("missing Lineage section")
    if "lineage:" not in body:
        errors.append("missing lineage placeholder block")
    if "source_interview_id:" not in body:
        errors.append("missing lineage field: source_interview_id")
    if "generated_task_graphs:" not in body:
        errors.append("missing lineage field: generated_task_graphs")
    if "generated_task_contracts:" not in body:
        errors.append("missing lineage field: generated_task_contracts")

    for phrase in FORBIDDEN_PHRASES:
        if phrase in text:
            errors.append(f"forbidden authority claim found: {phrase}")

    if errors:
        return build_result(TOKEN_FAILED, str(path), errors, warnings)
    return build_result(TOKEN_OK, str(path), [], warnings)


def run_fixtures(root, as_json=False):
    fixture_root = root / "tests/fixtures/product-spec"
    valid_dir = fixture_root / "valid"
    invalid_dir = fixture_root / "invalid"

    if not fixture_root.is_dir() or not valid_dir.is_dir() or not invalid_dir.is_dir():
        payload = build_result(TOKEN_BLOCKED, str(fixture_root), ["fixtures directory is missing or unreadable"])
        print_result(payload, as_json=as_json)
        return EXIT_BY_TOKEN[TOKEN_BLOCKED]

    valid_files = sorted(valid_dir.glob("*.md"))
    invalid_files = sorted(invalid_dir.glob("*.md"))
    if not valid_files or not invalid_files:
        payload = build_result(TOKEN_BLOCKED, str(fixture_root), ["fixtures are incomplete"])
        print_result(payload, as_json=as_json)
        return EXIT_BY_TOKEN[TOKEN_BLOCKED]

    failures = []
    for file_path in valid_files:
        result = validate_file(file_path, root)
        if result["result"] != TOKEN_OK:
            failures.append(f"valid fixture expected {TOKEN_OK} but got {result['result']}: {file_path.name}")

    for file_path in invalid_files:
        result = validate_file(file_path, root)
        if result["result"] != TOKEN_FAILED:
            failures.append(f"invalid fixture expected {TOKEN_FAILED} but got {result['result']}: {file_path.name}")

    if failures:
        payload = build_result(TOKEN_FAILED, str(fixture_root), failures)
        print_result(payload, as_json=as_json)
        return EXIT_BY_TOKEN[TOKEN_FAILED]

    payload = build_result(TOKEN_OK, str(fixture_root), [], ["all fixtures returned expected tokens"])
    print_result(payload, as_json=as_json)
    return EXIT_BY_TOKEN[TOKEN_OK]


def main():
    parser = argparse.ArgumentParser(description="Deterministic Product Spec structural validator")
    parser.add_argument("--file", help="Path to Product Spec markdown file")
    parser.add_argument("--fixtures", action="store_true", help="Run deterministic fixtures")
    parser.add_argument("--strict", action="store_true", help="Reserved flag for future use")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON")
    args = parser.parse_args()

    if bool(args.file) == bool(args.fixtures):
        payload = build_result(
            TOKEN_BLOCKED,
            "cli",
            ["use exactly one mode: --file <path> OR --fixtures"],
        )
        print_result(payload, as_json=args.json)
        return EXIT_BY_TOKEN[TOKEN_BLOCKED]

    root = pathlib.Path(__file__).resolve().parents[1]

    if args.fixtures:
        return run_fixtures(root, as_json=args.json)

    result = validate_file(args.file, root)
    print_result(result, as_json=args.json)
    return EXIT_BY_TOKEN[result["result"]]


if __name__ == "__main__":
    sys.exit(main())
