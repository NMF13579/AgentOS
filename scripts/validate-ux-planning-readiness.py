#!/usr/bin/env python3
"""
Deterministic validator for UX Planning Readiness reports (M48).
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

# TODO: Load readiness decision values and gap classes from canonical M48 policy documents after formats stabilize.
# --json mode must write only valid JSON to stdout; all non-JSON output, diagnostics, warnings, and tracebacks must go to stderr.

RESULT_OK = "UX_PLANNING_READINESS_VALIDATION_OK"
RESULT_FAILED = "UX_PLANNING_READINESS_VALIDATION_FAILED"
RESULT_BLOCKED = "UX_PLANNING_READINESS_VALIDATION_BLOCKED"

EXIT_BY_RESULT = {
    RESULT_OK: 0,
    RESULT_FAILED: 1,
    RESULT_BLOCKED: 2,
}

MAX_FILE_SIZE_BYTES = 1024 * 1024

ALLOWED_READINESS_DECISIONS = {
    "UX_PLANNING_READY",
    "UX_PLANNING_READY_WITH_LIMITATIONS",
    "UX_PLANNING_NOT_READY",
    "UX_PLANNING_BLOCKED",
}

ALLOWED_VALIDATION_RESULTS = {
    "UX_CONTRACT_VALIDATION_OK",
    "UX_CONTRACT_VALIDATION_FAILED",
    "UX_CONTRACT_VALIDATION_BLOCKED",
}

ALLOWED_GAP_CLASSES = {
    "UX_GAP_BLOCKING",
    "UX_GAP_MAJOR",
    "UX_GAP_MINOR",
    "UX_GAP_ACCEPTED_LIMITATION",
    "UX_GAP_NOT_APPLICABLE",
}

REQUIRED_FRONTMATTER_LINES = [
    "type: ux-planning-readiness-report",
    "milestone: M48",
    "authority: readiness-review",
    "decision:",
    "reviewed_by:",
    "reviewed_at:",
]

REQUIRED_SECTIONS = [
    "## Source References",
    "## Validation Inputs",
    "## Supporting Evidence",
    "## Readiness Decision",
    "## Criteria Review",
    "## Blocking Gaps",
    "## Major Gaps",
    "## Minor Gaps",
    "## Accepted Limitations",
    "## Not Applicable Items",
    "## Open Questions",
    "## Downstream Limits",
    "## Non-Authority Boundary",
]

REQUIRED_RECORD_FIELDS = [
    "ux_planning_readiness:",
    "source_product_spec:",
    "source_ux_contract:",
    "validation_result:",
    "source_preview:",
    "preview_required:",
    "preview_path:",
    "source_visual_snapshot:",
    "snapshot_required:",
    "snapshot_path:",
    "readiness_decision:",
    "criteria_review:",
    "blocking_gaps:",
    "major_gaps:",
    "minor_gaps:",
    "accepted_limitations:",
    "not_applicable_items:",
    "downstream_limits:",
    "reviewed_by:",
    "reviewed_at:",
]

REQUIRED_DOWNSTREAM_LIMITS = [
    "No task generation authorized.",
    "No implementation authorized.",
    "No execution planning authorized.",
    "No commit, push, merge, deploy, or release authorized.",
    "Future UX-to-task decomposition requires a separate authorized task contract.",
    "Future frontend implementation requires separate authorized task contracts.",
]

REQUIRED_NON_AUTHORITY_LINES = [
    "UX Planning Readiness Report is not task generation.",
    "UX Planning Readiness Report is not implementation approval.",
    "UX Planning Readiness Report does not authorize task generation.",
    "UX Planning Readiness Report does not authorize implementation.",
    "UX Planning Readiness Report does not authorize execution planning.",
    "UX Planning Readiness Report does not authorize commit, push, merge, deploy, or release.",
    "UX Planning Readiness Report may inform future planning only.",
    "Future task generation requires a separate authorized task contract.",
    "Future implementation requires separate authorized task contracts.",
]

FORBIDDEN_AUTHORITY_PATTERNS = [
    r"UX Planning Readiness Report authorizes task generation",
    r"UX Planning Readiness Report authorizes implementation",
    r"UX Planning Readiness Report authorizes execution",
    r"UX_PLANNING_READY authorizes task generation",
    r"UX_PLANNING_READY authorizes implementation",
    r"UX_PLANNING_READY authorizes execution",
    r"readiness report approves implementation",
    r"readiness report approves task generation",
    r"validator\\s+pass\\s+authorizes\\s+task generation",
    r"validator\\s+pass\\s+authorizes\\s+implementation",
    r"validator\\s+pass\\s+authorizes\\s+execution",
]

EXPLAIN_RULES = [
    "Check report file existence and readability.",
    "Check maximum file size <= 1 MB.",
    "Check frontmatter markers and required frontmatter fields.",
    "Check required report sections.",
    "Check required record fields.",
    "Validate readiness_decision allowlist.",
    "Validate validation_result allowlist.",
    "Enforce UX_CONTRACT_VALIDATION_OK for READY and READY_WITH_LIMITATIONS.",
    "Reject READY if blocking or major gaps are present.",
    "Require carry-forward markers when limitations exist.",
    "Check accepted limitation required fields.",
    "Check not applicable required fields.",
    "Check optional evidence sentinel behavior.",
    "Check required downstream limits.",
    "Check required non-authority boundary lines.",
    "Reject forbidden authority claim patterns.",
]


class ValidationOutcome:
    def __init__(self, result: str, mode: str, report: Optional[str] = None) -> None:
        self.result = result
        self.mode = mode
        self.report = report
        self.errors: List[str] = []
        self.warnings: List[str] = []

    def add_error(self, message: str) -> None:
        self.errors.append(message)

    def add_warning(self, message: str) -> None:
        self.warnings.append(message)

    def to_json_obj(self) -> Dict[str, object]:
        obj: Dict[str, object] = {
            "result": self.result,
            "mode": self.mode,
            "errors": self.errors,
            "warnings": self.warnings,
        }
        if self.report is not None:
            obj["report"] = self.report
        return obj


def read_text_with_bom(path: Path) -> str:
    data = path.read_bytes()
    return data.decode("utf-8-sig")


def extract_frontmatter(text: str) -> Optional[str]:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    return text[4:end]


def has_line(text: str, expected_line: str) -> bool:
    pattern = re.compile(r"^" + re.escape(expected_line) + r"$", re.MULTILINE)
    return bool(pattern.search(text))


def find_field_value(text: str, field_name: str) -> Optional[str]:
    # matches yaml-ish scalar lines
    m = re.search(r"^\s*" + re.escape(field_name) + r"\s*:\s*(.+?)\s*$", text, re.MULTILINE)
    if not m:
        return None
    return m.group(1).strip()


def find_block(text: str, block_name: str) -> List[str]:
    # minimal indented block extraction
    lines = text.splitlines()
    block_header = re.compile(r"^\s*" + re.escape(block_name) + r"\s*:\s*$")
    start = -1
    indent = 0

    for idx, line in enumerate(lines):
        if block_header.match(line):
            start = idx
            indent = len(line) - len(line.lstrip(" "))
            break

    if start == -1:
        return []

    collected: List[str] = []
    for line in lines[start + 1 :]:
        if line.strip() == "":
            collected.append(line)
            continue
        current_indent = len(line) - len(line.lstrip(" "))
        if current_indent <= indent:
            break
        collected.append(line)
    return collected


def contains_any_case_insensitive(text: str, patterns: Sequence[str]) -> Optional[str]:
    for pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return pattern
    return None


def count_list_items_in_block(block_lines: Sequence[str]) -> int:
    count = 0
    for line in block_lines:
        if re.match(r"^\s*-\s*\S", line):
            count += 1
    return count


def parse_bool_like(text: Optional[str]) -> Optional[bool]:
    if text is None:
        return None
    value = text.strip().lower()
    if value == "true":
        return True
    if value == "false":
        return False
    return None


def validate_report(path: Path) -> ValidationOutcome:
    outcome = ValidationOutcome(result=RESULT_OK, mode="report", report=str(path))

    if not path.exists():
        outcome.result = RESULT_BLOCKED
        outcome.add_error(f"report file does not exist: {path}")
        return outcome

    if not path.is_file():
        outcome.result = RESULT_BLOCKED
        outcome.add_error(f"report path is not a file: {path}")
        return outcome

    try:
        size = path.stat().st_size
    except OSError as exc:
        outcome.result = RESULT_BLOCKED
        outcome.add_error(f"unable to read report file metadata: {exc}")
        return outcome

    if size > MAX_FILE_SIZE_BYTES:
        outcome.result = RESULT_BLOCKED
        outcome.add_error("report file is larger than 1 MB")
        return outcome

    try:
        text = read_text_with_bom(path)
    except Exception as exc:  # pylint: disable=broad-except
        outcome.result = RESULT_BLOCKED
        outcome.add_error(f"unable to read report file as UTF-8: {exc}")
        return outcome

    # Check frontmatter
    frontmatter = extract_frontmatter(text)
    if frontmatter is None:
        outcome.add_error("missing or invalid frontmatter")
    else:
        for required_line in REQUIRED_FRONTMATTER_LINES:
            if required_line.endswith(":"):
                key = required_line[:-1]
                value = find_field_value(frontmatter, key)
                if value is None or value == "":
                    outcome.add_error(f"missing frontmatter field: {key}")
            else:
                if not has_line(frontmatter, required_line):
                    outcome.add_error(f"missing required frontmatter line: {required_line}")

    # Required sections
    for section in REQUIRED_SECTIONS:
        if not re.search(r"^" + re.escape(section) + r"\s*$", text, re.MULTILINE):
            outcome.add_error(f"missing required section: {section}")

    # Required fields
    for field in REQUIRED_RECORD_FIELDS:
        if field.endswith(":"):
            if re.search(r"^\s*" + re.escape(field) + r"\s*$", text, re.MULTILINE) is None and re.search(
                r"^\s*" + re.escape(field[:-1]) + r"\s*:\s*.+$", text, re.MULTILINE
            ) is None:
                outcome.add_error(f"missing required record field: {field}")

    # Allowed readiness decision
    readiness_decision = find_field_value(text, "readiness_decision")
    if readiness_decision is None:
        outcome.add_error("missing readiness_decision")
    elif readiness_decision not in ALLOWED_READINESS_DECISIONS:
        outcome.add_error(f"invalid readiness_decision: {readiness_decision}")

    # Allowed validation result
    validation_result = find_field_value(text, "validation_result")
    if validation_result is None:
        outcome.add_error("missing validation_result")
    elif validation_result not in ALLOWED_VALIDATION_RESULTS:
        outcome.add_error(f"invalid validation_result: {validation_result}")

    # Decision consistency
    if readiness_decision in {"UX_PLANNING_READY", "UX_PLANNING_READY_WITH_LIMITATIONS"}:
        if validation_result != "UX_CONTRACT_VALIDATION_OK":
            outcome.add_error("UX_CONTRACT_VALIDATION_OK is required for READY and READY_WITH_LIMITATIONS")

    blocking_block = find_block(text, "blocking_gaps")
    major_block = find_block(text, "major_gaps")
    accepted_block = find_block(text, "accepted_limitations")

    blocking_count = count_list_items_in_block(blocking_block)
    major_count = count_list_items_in_block(major_block)
    accepted_count = count_list_items_in_block(accepted_block)

    if readiness_decision == "UX_PLANNING_READY":
        if blocking_count > 0:
            outcome.add_error("UX_PLANNING_READY must not contain blocking gaps")
        if major_count > 0:
            outcome.add_error("UX_PLANNING_READY must not contain major gaps")

    if readiness_decision == "UX_PLANNING_READY_WITH_LIMITATIONS":
        if accepted_count > 0 and "carry_forward_required: true" not in text:
            outcome.add_error("READY_WITH_LIMITATIONS must carry limitations forward")

    # Accepted limitation required fields
    if not _accepted_limitation_fields_present(text):
        required_limitation_lines = [
            "gap_class: UX_GAP_ACCEPTED_LIMITATION",
            "rationale:",
            "downstream_risk:",
            "owner:",
            "carry_forward_required: true",
        ]
        for marker in required_limitation_lines:
            outcome.add_error(f"accepted limitation missing required field: {marker}")

    # Validate accepted limitations list items include expected class when inline
    for line in text.splitlines():
        if "UX_GAP_" in line and "gap_class:" in line:
            class_value = line.split("gap_class:", 1)[1].strip()
            if class_value and class_value not in ALLOWED_GAP_CLASSES:
                outcome.add_error(f"invalid gap class: {class_value}")

    # NOT_APPLICABLE item required fields
    if not _not_applicable_fields_present(text):
        required_na_lines = ["criterion:", "rationale:", "owner:"]
        for marker in required_na_lines:
            outcome.add_error(f"not_applicable item missing required field: {marker}")

    # Optional evidence sentinel rules
    preview_required_value = find_field_value(text, "preview_required")
    preview_required_bool = parse_bool_like(preview_required_value)
    preview_path = find_field_value(text, "preview_path")
    if preview_required_bool is False and preview_path != "<path-to-preview-or-NOT_APPLICABLE>" and preview_path != "NOT_APPLICABLE":
        outcome.add_error("preview_required=false requires preview_path NOT_APPLICABLE")

    snapshot_required_value = find_field_value(text, "snapshot_required")
    snapshot_required_bool = parse_bool_like(snapshot_required_value)
    snapshot_path = find_field_value(text, "snapshot_path")
    if snapshot_required_bool is False and snapshot_path != "<path-to-snapshot-or-NOT_APPLICABLE>" and snapshot_path != "NOT_APPLICABLE":
        outcome.add_error("snapshot_required=false requires snapshot_path NOT_APPLICABLE")

    # Downstream limits
    for required_limit in REQUIRED_DOWNSTREAM_LIMITS:
        if required_limit not in text:
            outcome.add_error(f"missing downstream limit line: {required_limit}")

    # Non-authority boundary lines
    for required_line in REQUIRED_NON_AUTHORITY_LINES:
        if required_line not in text:
            outcome.add_error(f"missing non-authority boundary line: {required_line}")

    # Forbidden authority claims
    found_pattern = contains_any_case_insensitive(text, FORBIDDEN_AUTHORITY_PATTERNS)
    if found_pattern is not None:
        outcome.add_error(f"forbidden authority claim matched: {found_pattern}")

    # Additional deterministic checks aligned to constraints
    if "source_ux_contract:" not in text:
        outcome.add_error("missing source_ux_contract block")
    if "ux_contract_path:" not in text:
        outcome.add_error("missing ux_contract_path")

    # Ensure missing validation result is caught if placeholder removed
    if re.search(r"^\s*validation_result\s*:\s*$", text, re.MULTILINE):
        outcome.add_error("validation_result must not be empty")

    # Ensure readiness decision is not empty
    if re.search(r"^\s*readiness_decision\s*:\s*$", text, re.MULTILINE):
        outcome.add_error("readiness_decision must not be empty")

    # If there are errors and not blocked, mark failed
    if outcome.result != RESULT_BLOCKED and outcome.errors:
        outcome.result = RESULT_FAILED

    return outcome


def print_text_result(outcome: ValidationOutcome) -> None:
    if outcome.mode == "report":
        print(f"Result: {outcome.result}")
        if outcome.report:
            print(f"Report: {outcome.report}")
    elif outcome.mode == "fixtures":
        print(f"Result: {outcome.result}")
    elif outcome.mode == "explain":
        print("Result: UX_PLANNING_READINESS_VALIDATION_OK")

    if outcome.errors:
        print("Errors:")
        for err in outcome.errors:
            print(f"- {err}")
    if outcome.warnings:
        print("Warnings:")
        for warn in outcome.warnings:
            print(f"- {warn}")


def write_json_stdout(payload: Dict[str, object]) -> None:
    sys.stdout.write(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def safe_stderr(message: str) -> None:
    sys.stderr.write(message + "\n")


def run_explain(as_json: bool) -> int:
    if as_json:
        payload = {
            "result": RESULT_OK,
            "mode": "explain",
            "rules": EXPLAIN_RULES,
        }
        write_json_stdout(payload)
        return EXIT_BY_RESULT[RESULT_OK]

    print("UX Planning Readiness Validation Rules")
    for idx, rule in enumerate(EXPLAIN_RULES, start=1):
        print(f"{idx}. {rule}")
    print(f"Result: {RESULT_OK}")
    return EXIT_BY_RESULT[RESULT_OK]


def fixture_dirs() -> Tuple[Path, Path]:
    base = Path("tests/fixtures/ux-planning-readiness")
    return base / "valid", base / "negative"


def list_markdown_files(path: Path) -> List[Path]:
    files = sorted(path.glob("*.md"))
    return [p for p in files if p.is_file()]


def run_fixtures(as_json: bool) -> int:
    valid_dir, negative_dir = fixture_dirs()

    if not valid_dir.exists() or not negative_dir.exists():
        outcome = {
            "result": RESULT_BLOCKED,
            "mode": "fixtures",
            "errors": ["fixture directories are missing"],
            "warnings": [],
            "fixture_summary": {
                "positive_passed": 0,
                "positive_failed": 0,
                "negative_failed_as_expected": 0,
                "negative_unexpectedly_passed": 0,
            },
        }
        if as_json:
            write_json_stdout(outcome)
        else:
            print("Result: UX_PLANNING_READINESS_VALIDATION_BLOCKED")
            print("Errors:")
            print("- fixture directories are missing")
        return EXIT_BY_RESULT[RESULT_BLOCKED]

    positives = list_markdown_files(valid_dir)
    negatives = list_markdown_files(negative_dir)

    positive_passed = 0
    positive_failed = 0
    negative_failed_as_expected = 0
    negative_unexpectedly_passed = 0

    for report in positives:
        outcome = validate_report(report)
        if outcome.result == RESULT_OK:
            positive_passed += 1
        else:
            positive_failed += 1

    for report in negatives:
        outcome = validate_report(report)
        if outcome.result == RESULT_OK:
            negative_unexpectedly_passed += 1
        else:
            negative_failed_as_expected += 1

    fixture_summary = {
        "positive_passed": positive_passed,
        "positive_failed": positive_failed,
        "negative_failed_as_expected": negative_failed_as_expected,
        "negative_unexpectedly_passed": negative_unexpectedly_passed,
    }

    if positive_failed == 0 and negative_unexpectedly_passed == 0:
        result = RESULT_OK
    else:
        result = RESULT_FAILED

    payload = {
        "result": result,
        "mode": "fixtures",
        "fixture_summary": fixture_summary,
        "errors": [],
        "warnings": [],
    }

    if as_json:
        write_json_stdout(payload)
    else:
        print(f"Result: {result}")
        print("Fixture summary:")
        print(f"- positive_passed: {positive_passed}")
        print(f"- positive_failed: {positive_failed}")
        print(f"- negative_failed_as_expected: {negative_failed_as_expected}")
        print(f"- negative_unexpectedly_passed: {negative_unexpectedly_passed}")

    return EXIT_BY_RESULT[result]


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate UX planning readiness reports.")
    parser.add_argument("--report", type=str, help="Path to one readiness report")
    parser.add_argument("--fixtures", action="store_true", help="Run fixtures")
    parser.add_argument("--explain", action="store_true", help="Explain validation rules")
    parser.add_argument("--json", action="store_true", dest="as_json", help="JSON output")
    return parser.parse_args(argv)


def validate_cli(args: argparse.Namespace) -> Optional[str]:
    selected = 0
    if args.report:
        selected += 1
    if args.fixtures:
        selected += 1
    if args.explain:
        selected += 1

    if selected != 1:
        return "exactly one mode must be selected: --report, --fixtures, or --explain"
    return None


def run_report_mode(report_path: str, as_json: bool) -> int:
    outcome = validate_report(Path(report_path))

    if as_json:
        payload = outcome.to_json_obj()
        write_json_stdout(payload)
    else:
        print_text_result(outcome)

    return EXIT_BY_RESULT[outcome.result]


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)

    cli_error = validate_cli(args)
    if cli_error:
        if args.as_json:
            payload = {
                "result": RESULT_BLOCKED,
                "mode": "cli",
                "errors": [cli_error],
                "warnings": [],
            }
            write_json_stdout(payload)
        else:
            safe_stderr("Result: UX_PLANNING_READINESS_VALIDATION_BLOCKED")
            safe_stderr(f"Error: {cli_error}")
        return EXIT_BY_RESULT[RESULT_BLOCKED]

    if args.explain:
        return run_explain(args.as_json)

    if args.fixtures:
        return run_fixtures(args.as_json)

    if args.report:
        return run_report_mode(args.report, args.as_json)

    # Defensive fallback
    if args.as_json:
        payload = {
            "result": RESULT_BLOCKED,
            "mode": "cli",
            "errors": ["no execution mode selected"],
            "warnings": [],
        }
        write_json_stdout(payload)
    else:
        safe_stderr("Result: UX_PLANNING_READINESS_VALIDATION_BLOCKED")
        safe_stderr("Error: no execution mode selected")
    return EXIT_BY_RESULT[RESULT_BLOCKED]


# Additional helper checks for deterministic behavior and explicitness.
# These functions are currently used to keep rule checks easy to extend.
def _marker_exists(text: str, marker: str) -> bool:
    return marker in text


def _extract_list_block(text: str, key: str) -> List[str]:
    return find_block(text, key)


def _has_nonempty_list_items(lines: Sequence[str]) -> bool:
    return count_list_items_in_block(lines) > 0


def _normalize_whitespace(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip())


def _is_true_literal(value: Optional[str]) -> bool:
    return parse_bool_like(value) is True


def _is_false_literal(value: Optional[str]) -> bool:
    return parse_bool_like(value) is False


def _collect_required_markers_missing(text: str, required_markers: Sequence[str]) -> List[str]:
    missing: List[str] = []
    for marker in required_markers:
        if marker not in text:
            missing.append(marker)
    return missing


def _validate_allowed_decision_value(value: Optional[str]) -> Optional[str]:
    if value is None:
        return "missing readiness_decision"
    if value not in ALLOWED_READINESS_DECISIONS:
        return f"invalid readiness_decision: {value}"
    return None


def _validate_allowed_validation_token(value: Optional[str]) -> Optional[str]:
    if value is None:
        return "missing validation_result"
    if value not in ALLOWED_VALIDATION_RESULTS:
        return f"invalid validation_result: {value}"
    return None


def _find_forbidden_authority_claim(text: str) -> Optional[str]:
    return contains_any_case_insensitive(text, FORBIDDEN_AUTHORITY_PATTERNS)


def _require_non_authority_lines(text: str) -> List[str]:
    return _collect_required_markers_missing(text, REQUIRED_NON_AUTHORITY_LINES)


def _require_downstream_lines(text: str) -> List[str]:
    return _collect_required_markers_missing(text, REQUIRED_DOWNSTREAM_LIMITS)


def _must_have_frontmatter_fields(frontmatter: str) -> List[str]:
    missing: List[str] = []
    for required_line in REQUIRED_FRONTMATTER_LINES:
        if required_line.endswith(":"):
            key = required_line[:-1]
            v = find_field_value(frontmatter, key)
            if v is None or v.strip() == "":
                missing.append(required_line)
        else:
            if not has_line(frontmatter, required_line):
                missing.append(required_line)
    return missing


def _must_have_sections(text: str) -> List[str]:
    missing: List[str] = []
    for section in REQUIRED_SECTIONS:
        if re.search(r"^" + re.escape(section) + r"\s*$", text, re.MULTILINE) is None:
            missing.append(section)
    return missing


def _must_have_record_fields(text: str) -> List[str]:
    missing: List[str] = []
    for field in REQUIRED_RECORD_FIELDS:
        if field.endswith(":"):
            if re.search(r"^\s*" + re.escape(field) + r"\s*$", text, re.MULTILINE) is None and re.search(
                r"^\s*" + re.escape(field[:-1]) + r"\s*:\s*.+$", text, re.MULTILINE
            ) is None:
                missing.append(field)
    return missing


def _decision_requires_ok_validation(decision: Optional[str], validation: Optional[str]) -> bool:
    if decision in {"UX_PLANNING_READY", "UX_PLANNING_READY_WITH_LIMITATIONS"}:
        return validation == "UX_CONTRACT_VALIDATION_OK"
    return True


def _ready_has_no_blocking_or_major(decision: Optional[str], blocking: int, major: int) -> bool:
    if decision != "UX_PLANNING_READY":
        return True
    return blocking == 0 and major == 0


def _limitations_carry_forward_when_present(decision: Optional[str], accepted_count: int, text: str) -> bool:
    if decision != "UX_PLANNING_READY_WITH_LIMITATIONS":
        return True
    if accepted_count <= 0:
        return True
    return "carry_forward_required: true" in text


def _sentinel_preview_ok(preview_required: Optional[str], preview_path: Optional[str]) -> bool:
    b = parse_bool_like(preview_required)
    if b is False:
        return preview_path in {"NOT_APPLICABLE", "<path-to-preview-or-NOT_APPLICABLE>"}
    return True


def _sentinel_snapshot_ok(snapshot_required: Optional[str], snapshot_path: Optional[str]) -> bool:
    b = parse_bool_like(snapshot_required)
    if b is False:
        return snapshot_path in {"NOT_APPLICABLE", "<path-to-snapshot-or-NOT_APPLICABLE>"}
    return True


def _accepted_limitation_fields_present(text: str) -> bool:
    if "accepted_limitation:" not in text:
        return True
    block = find_block(text, "accepted_limitation")
    if not block:
        return False
    joined = "\n".join(block)
    needed = [
        "gap_class: UX_GAP_ACCEPTED_LIMITATION",
        "rationale:",
        "downstream_risk:",
        "owner:",
        "carry_forward_required: true",
    ]
    for n in needed:
        if n not in joined:
            return False
    return True


def _not_applicable_fields_present(text: str) -> bool:
    if "not_applicable_item:" not in text:
        return True
    block = find_block(text, "not_applicable_item")
    if not block:
        return False
    joined = "\n".join(block)
    needed = ["criterion:", "rationale:", "owner:"]
    for n in needed:
        if n not in joined:
            return False
    return True


def _gap_classes_valid_when_present(text: str) -> bool:
    for line in text.splitlines():
        if "gap_class:" in line:
            val = line.split("gap_class:", 1)[1].strip()
            if val and val not in ALLOWED_GAP_CLASSES:
                return False
    return True


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except Exception as exc:  # pylint: disable=broad-except
        # In --json mode we still must keep stdout as JSON only.
        # Since parsing args may fail, fallback writes diagnostics to stderr and returns BLOCKED.
        safe_stderr(f"Result: {RESULT_BLOCKED}")
        safe_stderr(f"Unhandled error: {exc}")
        raise SystemExit(EXIT_BY_RESULT[RESULT_BLOCKED])
