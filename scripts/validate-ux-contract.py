#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

VOCABULARY_VERSION = "1.0.0"
# TODO: Load allowed UX elements from docs/UX-ELEMENT-VOCABULARY.md after the vocabulary format is stabilized.
ALLOWED_UX_ELEMENTS = {
    "summary_card",
    "risk_banner",
    "approval_card",
    "decision_card",
    "status_badge",
    "review_panel",
    "task_card",
    "checklist",
    "timeline",
    "empty_state",
    "error_state",
    "blocked_state",
    "confirmation_notice",
    "audit_note",
    "non_authority_notice",
}

RESULT_OK = "UX_CONTRACT_VALIDATION_OK"
RESULT_FAILED = "UX_CONTRACT_VALIDATION_FAILED"
RESULT_BLOCKED = "UX_CONTRACT_VALIDATION_BLOCKED"

MAX_SIZE_BYTES = 1024 * 1024

REQUIRED_FRONTMATTER_KEYS = [
    "type",
    "status",
    "authority",
    "ux_contract_id",
    "ux_contract_version",
    "spec_id",
    "spec_version",
    "product_spec_path",
    "execution_locked",
    "created",
    "owner",
]

ALLOWED_STATUS = {
    "draft",
    "review",
    "structure_review_complete",
    "needs_changes",
    "blocked",
    "deprecated",
}

REQUIRED_SECTIONS = [
    "## Source Product Spec",
    "## UX Goal",
    "## Screens",
    "## Flows",
    "## States",
    "## UX Elements",
    "## User Actions",
    "## Risk / Approval Points",
    "## Edge Cases",
    "## Accessibility Notes",
    "## Non-Goals",
    "## Open UX Questions",
    "## Traceability",
    "## Non-Authority Boundary",
]

REQUIRED_STATES = [
    "normal",
    "loading",
    "empty",
    "error",
    "blocked",
    "needs_clarification",
    "approval_required",
    "execution_not_authorized",
]

REQUIRED_SAFETY_STATES = [
    "blocked",
    "needs_clarification",
    "approval_required",
    "execution_not_authorized",
]

REQUIRED_BOUNDARY_STATEMENTS = [
    "UX Contract is not Product Spec.",
    "UX Contract is not approval.",
    "UX Contract does not authorize task generation.",
    "UX Contract does not authorize execution planning.",
    "UX Contract does not authorize implementation.",
    "UX Contract does not authorize commit, push, merge, deploy, or release.",
    "HTML Preview is optional visual explanation only.",
    "UX Visual Approval Snapshot approves visual direction only.",
    "UX Contract describes user-facing structure.",
    "UX Contract does not implement UI.",
    "HTML Preview is not source of truth.",
    "UX Visual Approval Snapshot is supporting evidence only.",
]

FORBIDDEN_CLAIMS = [
    "ux contract authorizes execution",
    "ux contract approves implementation",
    "ux contract authorizes implementation",
    "ux contract authorizes task generation",
    "ux contract authorizes execution planning",
    "html preview is source of truth",
    "html preview is implementation",
    "snapshot authorizes implementation",
    "snapshot authorizes task generation",
    "structure_review_complete authorizes implementation",
    "structure_review_complete authorizes task generation",
    "structure_review_complete authorizes execution",
]

FORBIDDEN_IMPL_FIELDS = [
    "react_component",
    "vue_component",
    "svelte_component",
    "css_class",
    "api_endpoint",
    "database_table",
    "backend_service",
    "deploy_target",
    "runtime_command",
]

REQUIRED_APPROVAL_TERMS = [
    "action_summary",
    "risk_level",
    "human_owner",
    "consequences",
    "approve_label",
    "decline_label",
    "non_authority_notice",
]

REQUIRED_RISK_TERMS = ["risk_level", "affected_scope", "non_authority_notice"]

REQUIRED_SOURCE_FILES = [
    "schemas/ux-contract.schema.json",
    "docs/UX-ELEMENT-VOCABULARY.md",
]


class ValidationResult:
    def __init__(self, result: str, errors: Optional[List[str]] = None, warnings: Optional[List[str]] = None):
        self.result = result
        self.errors = errors or []
        self.warnings = warnings or []


def read_utf8_file(path: Path) -> Tuple[Optional[str], Optional[str]]:
    if not path.exists() or not path.is_file():
        return None, f"Missing contract file: {path}"
    try:
        size = path.stat().st_size
    except OSError:
        return None, f"Unable to stat contract file: {path}"
    if size > MAX_SIZE_BYTES:
        return None, f"File larger than 1 MB safety limit: {path}"
    if path.suffix.lower() != ".md":
        return None, f"Contract must be Markdown (.md): {path}"
    try:
        return path.read_text(encoding="utf-8-sig"), None
    except UnicodeDecodeError:
        return None, f"Non-UTF-8 contract file: {path}"
    except OSError:
        return None, f"Unable to read contract file: {path}"


def parse_frontmatter(text: str) -> Tuple[Optional[Dict[str, str]], Optional[str], str]:
    if not text.startswith("---\n"):
        return None, "Missing opening frontmatter marker", text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, "Missing closing frontmatter marker", text
    raw = text[4:end]
    body = text[end + 5 :]
    fm: Dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            return None, f"Malformed frontmatter line: {line}", body
        key, value = line.split(":", 1)
        fm[key.strip()] = value.strip()
    return fm, None, body


def extract_ux_elements(text: str) -> List[str]:
    found: List[str] = []

    section_text = extract_ux_elements_section(text)
    if section_text:
        for m in re.finditer(r"^### UX Element:\s*([a-zA-Z0-9_-]+)\s*$", section_text, re.MULTILINE):
            found.append(m.group(1))
        for m in re.finditer(r"^\s*element_type:\s*([a-zA-Z0-9_-]+)\s*$", section_text, re.MULTILINE):
            found.append(m.group(1))
        for m in re.finditer(r"^\s*-\s*([a-zA-Z0-9_-]+)\s*$", section_text, re.MULTILINE):
            found.append(m.group(1))

    uniq = []
    seen = set()
    for item in found:
        if item not in seen:
            seen.add(item)
            uniq.append(item)
    return uniq


def extract_ux_elements_section(text: str) -> str:
    section_match = re.search(r"^## UX Elements\s*$", text, re.MULTILINE)
    if not section_match:
        return ""
    start = section_match.end()
    tail = text[start:]
    next_section = re.search(r"^## ", tail, re.MULTILINE)
    return tail[: next_section.start()] if next_section else tail


def extract_ux_elements_for_required_field_checks(text: str) -> List[str]:
    section_text = extract_ux_elements_section(text)
    if not section_text:
        return []

    found: List[str] = []
    # MVP: only deterministic declarations inside UX Elements section.
    for m in re.finditer(r"^\s*element_type:\s*([a-zA-Z0-9_-]+)\s*$", section_text, re.MULTILINE):
        found.append(m.group(1))
    for m in re.finditer(r"^\s*-\s*([a-zA-Z0-9_-]+)\s*$", section_text, re.MULTILINE):
        found.append(m.group(1))

    uniq = []
    seen = set()
    for item in found:
        if item not in seen:
            seen.add(item)
            uniq.append(item)
    return uniq


def extract_ux_elements_headings_in_section(text: str) -> List[str]:
    section_text = extract_ux_elements_section(text)
    if not section_text:
        return []
    found = []
    for m in re.finditer(r"^### UX Element:\s*([a-zA-Z0-9_-]+)\s*$", section_text, re.MULTILINE):
        found.append(m.group(1))
    uniq = []
    seen = set()
    for item in found:
        if item not in seen:
            seen.add(item)
            uniq.append(item)
    return uniq


def extract_section_block(text: str, section_heading: str) -> str:
    pattern = rf"^{re.escape(section_heading)}\s*$([\s\S]*?)(?=^## |\Z)"
    m = re.search(pattern, text, re.MULTILINE)
    if not m:
        return ""
    return m.group(1)


def extract_mapping_block(section_text: str, root_key: str) -> str:
    lines = section_text.splitlines()
    root_idx = -1
    root_indent = 0
    for i, line in enumerate(lines):
        m = re.match(rf"^(\s*){re.escape(root_key)}:\s*$", line)
        if m:
            root_idx = i
            root_indent = len(m.group(1))
            break
    if root_idx == -1:
        return ""

    block_lines: List[str] = []
    for line in lines[root_idx + 1 :]:
        if not line.strip():
            block_lines.append(line)
            continue
        indent = len(line) - len(line.lstrip(" "))
        if indent <= root_indent:
            break
        block_lines.append(line)
    return "\n".join(block_lines)


def element_heading_blocks_in_ux_elements_section(text: str) -> Dict[str, List[str]]:
    section_text = extract_ux_elements_section(text)
    if not section_text:
        return {}
    lines = section_text.splitlines()
    blocks: Dict[str, List[str]] = {}

    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^### UX Element:\s*([a-zA-Z0-9_-]+)\s*$", line)
        if not m:
            i += 1
            continue
        element = m.group(1)
        i += 1
        buf: List[str] = []
        while i < len(lines):
            nxt = lines[i]
            if re.match(r"^###\s+", nxt) or re.match(r"^##\s+", nxt):
                break
            buf.append(nxt)
            i += 1
        blocks.setdefault(element, []).append("\n".join(buf))
    return blocks


def traceability_source_sections_has_items(text: str) -> bool:
    traceability_section = extract_section_block(text, "## Traceability")
    if not traceability_section:
        return False

    section_text = traceability_section
    lines = section_text.splitlines()
    source_idx = -1
    source_indent = 0
    for i, line in enumerate(lines):
        m = re.match(r"^(\s*)source_sections:\s*$", line)
        if m:
            source_idx = i
            source_indent = len(m.group(1))
            break
    if source_idx == -1:
        return False

    for line in lines[source_idx + 1 :]:
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        if indent <= source_indent:
            break
        if re.match(r"^\s*-\s*\S+", line):
            return True
    return False


def validate_contract(path: Path) -> ValidationResult:
    for required_path in REQUIRED_SOURCE_FILES:
        rp = Path(required_path)
        if not rp.exists() or not rp.is_file():
            return ValidationResult(RESULT_BLOCKED, [f"Required validator source missing: {required_path}"])

    text, read_err = read_utf8_file(path)
    if read_err:
        return ValidationResult(RESULT_BLOCKED, [read_err])
    assert text is not None

    errors: List[str] = []
    frontmatter, fm_err, body = parse_frontmatter(text)
    if fm_err:
        return ValidationResult(RESULT_FAILED, [fm_err])
    assert frontmatter is not None

    for key in REQUIRED_FRONTMATTER_KEYS:
        if key not in frontmatter:
            errors.append(f"Missing frontmatter key: {key}")

    if frontmatter.get("type") != "ux-contract":
        errors.append("Frontmatter type must be ux-contract")
    if frontmatter.get("authority") != "ux-structure":
        errors.append("Frontmatter authority must be ux-structure")

    status = frontmatter.get("status", "")
    if status == "approved_for_structure":
        errors.append("Forbidden status value: approved_for_structure")
    if status and status not in ALLOWED_STATUS:
        errors.append(f"Invalid status value: {status}")

    execution_locked = frontmatter.get("execution_locked")
    if execution_locked != "true":
        errors.append("execution_locked must be true")

    for section in REQUIRED_SECTIONS:
        if section not in text:
            errors.append(f"Missing required section: {section}")

    source_product_spec_section = extract_section_block(text, "## Source Product Spec")
    if not source_product_spec_section:
        errors.append("Missing required section: ## Source Product Spec")
    source_product_spec_block = extract_mapping_block(source_product_spec_section, "source_product_spec") if source_product_spec_section else ""
    if not source_product_spec_block:
        errors.append("Missing source_product_spec block")
    for key in ["spec_id:", "spec_version:", "product_spec_path:"]:
        if key not in source_product_spec_block:
            errors.append(f"Missing required source product spec key: {key}")

    traceability_section = extract_section_block(text, "## Traceability")
    traceability_block = extract_mapping_block(traceability_section, "traceability") if traceability_section else ""
    if not traceability_block:
        errors.append("Missing traceability block")
    for key in ["spec_id:", "spec_version:", "product_spec_path:", "ux_contract_id:", "source_sections:"]:
        if key not in traceability_block:
            errors.append(f"Missing traceability key: {key}")

    if "source_section:" in text:
        errors.append("Forbidden singular traceability key used: source_section")

    if "source_sections:" in text and not traceability_source_sections_has_items(text):
        errors.append("source_sections must contain at least one list entry")

    for state in REQUIRED_STATES:
        if f"### State: {state}" not in text:
            errors.append(f"Missing required UX state: {state}")

    if len(re.findall(r"^### Screen:\s+", text, re.MULTILINE)) < 1:
        errors.append("At least one screen is required (### Screen:)")

    if len(re.findall(r"^### Flow:\s+", text, re.MULTILINE)) < 1:
        errors.append("At least one flow is required (### Flow:)")

    used_elements = extract_ux_elements(text)
    for element in used_elements:
        if element not in ALLOWED_UX_ELEMENTS:
            errors.append(f"Unknown UX element: {element}")

    lowered = text.lower()
    elements_for_required_checks = extract_ux_elements_for_required_field_checks(text)
    heading_blocks = element_heading_blocks_in_ux_elements_section(text)
    if "approval_card" in elements_for_required_checks:
        for term in REQUIRED_APPROVAL_TERMS:
            if f"{term}:" not in lowered:
                errors.append(f"approval_card requires term: {term}")
    approval_blocks = heading_blocks.get("approval_card", [])
    for idx, block_text in enumerate(approval_blocks, start=1):
        block_lower = block_text.lower()
        if len(approval_blocks) == 1:
            block_lower = block_lower + "\n" + extract_ux_elements_section(text).lower()
        for term in REQUIRED_APPROVAL_TERMS:
            if f"{term}:" not in block_lower:
                errors.append(f"approval_card requires term in block {idx}: {term}")

    if "risk_banner" in elements_for_required_checks:
        for term in REQUIRED_RISK_TERMS:
            if f"{term}:" not in lowered:
                errors.append(f"risk_banner requires term: {term}")
        if "risk_summary:" not in lowered and "risk_reason:" not in lowered:
            errors.append("risk_banner requires term: risk_summary")
    risk_blocks = heading_blocks.get("risk_banner", [])
    for idx, block_text in enumerate(risk_blocks, start=1):
        block_lower = block_text.lower()
        if len(risk_blocks) == 1:
            block_lower = block_lower + "\n" + extract_ux_elements_section(text).lower()
        for term in REQUIRED_RISK_TERMS:
            if f"{term}:" not in block_lower:
                errors.append(f"risk_banner requires term in block {idx}: {term}")
        if "risk_summary:" not in block_lower and "risk_reason:" not in block_lower:
            errors.append(f"risk_banner requires term in block {idx}: risk_summary")

    for stmt in REQUIRED_BOUNDARY_STATEMENTS:
        if stmt not in text:
            errors.append(f"Missing required boundary statement: {stmt}")

    lowered_forbidden = text.lower()
    for claim in FORBIDDEN_CLAIMS:
        if claim in lowered_forbidden:
            errors.append(f"Forbidden authority claim detected: {claim}")

    for field in FORBIDDEN_IMPL_FIELDS:
        if re.search(rf"\b{re.escape(field)}\b", text):
            errors.append(f"Forbidden implementation field detected: {field}")

    for state in REQUIRED_SAFETY_STATES:
        if f"### State: {state}" not in text:
            errors.append(f"Missing safety state (happy-path-only failure): {state}")

    if errors:
        return ValidationResult(RESULT_FAILED, errors)
    return ValidationResult(RESULT_OK, [])


def explain_payload() -> Dict[str, object]:
    return {
        "result": RESULT_OK,
        "mode": "explain",
        "rules": [
            "file_readability",
            "frontmatter_required_keys_and_values",
            "required_sections",
            "source_product_spec_block",
            "canonical_traceability_source_sections",
            "required_states",
            "screen_and_flow_presence",
            "ux_element_allowlist_patterns",
            "approval_and_risk_required_terms",
            "non_authority_boundary",
            "forbidden_authority_claims",
            "forbidden_implementation_fields",
            "execution_lock_true",
            "safety_states_for_happy_path_detection",
        ],
        "vocabulary_version": VOCABULARY_VERSION,
    }


def run_fixtures() -> Tuple[ValidationResult, Dict[str, object]]:
    root = Path("tests/fixtures/ux-contract")
    valid_file = root / "valid" / "valid-agent-action-review.md"
    negative_dir = root / "negative"
    required_negatives = [
        negative_dir / "missing-required-section.md",
        negative_dir / "missing-source-product-spec.md",
        negative_dir / "source-section-singular.md",
        negative_dir / "unknown-ux-element.md",
        negative_dir / "approval-card-missing-owner.md",
        negative_dir / "approval-card-missing-required-fields.md",
        negative_dir / "approval-card-heading-only.md",
        negative_dir / "forbidden-authority-claim.md",
        negative_dir / "missing-required-state.md",
        negative_dir / "execution-locked-false.md",
        negative_dir / "implementation-field.md",
        negative_dir / "happy-path-only.md",
        negative_dir / "source-sections-empty.md",
        negative_dir / "risk-banner-heading-only.md",
        negative_dir / "source-product-spec-empty-block.md",
        negative_dir / "traceability-keys-in-frontmatter-only.md",
    ]

    if not root.exists() or not valid_file.exists() or not negative_dir.exists():
        return ValidationResult(RESULT_BLOCKED, ["Fixture structure missing"]), {}
    for f in required_negatives:
        if not f.exists():
            return ValidationResult(RESULT_BLOCKED, [f"Missing required fixture file: {f}"]), {}

    errors: List[str] = []

    positive = validate_contract(valid_file)
    positive_passed = 1 if positive.result == RESULT_OK else 0
    positive_failed = 0 if positive.result == RESULT_OK else 1
    if positive.result != RESULT_OK:
        errors.append(f"Positive fixture failed: {valid_file}")
        errors.extend(positive.errors)

    negative_total = 0
    negative_failed_as_expected = 0
    negative_unexpectedly_passed = 0
    negative_blocked_count = 0

    for f in sorted(negative_dir.glob("*.md")):
        negative_total += 1
        res = validate_contract(f)
        if res.result == RESULT_FAILED:
            negative_failed_as_expected += 1
        elif res.result == RESULT_OK:
            negative_unexpectedly_passed += 1
            errors.append(f"Negative fixture unexpectedly passed: {f}")
        else:
            negative_blocked_count += 1
            errors.append(f"Negative fixture blocked unexpectedly: {f}")
            errors.extend(res.errors)

    summary = {
        "positive_passed": positive_passed,
        "positive_failed": positive_failed,
        "negative_total": negative_total,
        "negative_failed_as_expected": negative_failed_as_expected,
        "negative_unexpectedly_passed": negative_unexpectedly_passed,
        "negative_blocked_count": negative_blocked_count,
    }

    if positive_failed or negative_unexpectedly_passed or negative_blocked_count:
        return ValidationResult(RESULT_FAILED, errors), summary
    return ValidationResult(RESULT_OK, errors), summary


def print_result(result: ValidationResult, json_mode: bool, contract: Optional[str] = None, mode: Optional[str] = None, fixture_summary: Optional[Dict[str, object]] = None) -> None:
    if json_mode:
        payload: Dict[str, object] = {
            "result": result.result,
            "errors": result.errors,
            "warnings": result.warnings,
            "vocabulary_version": VOCABULARY_VERSION,
        }
        if contract is not None:
            payload["contract"] = contract
        if mode is not None:
            payload["mode"] = mode
        if fixture_summary is not None:
            payload["fixture_summary"] = fixture_summary
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(result.result)
        for err in result.errors:
            print(f"ERROR: {err}")


def exit_code_for_result(result_token: str) -> int:
    if result_token == RESULT_OK:
        return 0
    if result_token == RESULT_FAILED:
        return 1
    return 2


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate UX Contract markdown files.")
    parser.add_argument("--contract", type=str, help="Path to one UX Contract markdown file")
    parser.add_argument("--fixtures", action="store_true", help="Run positive and negative fixtures")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    parser.add_argument("--explain", action="store_true", help="Explain validation rules")
    args = parser.parse_args()

    mode_count = int(bool(args.contract)) + int(bool(args.fixtures)) + int(bool(args.explain))
    if mode_count != 1:
        result = ValidationResult(RESULT_BLOCKED, ["Choose exactly one mode: --contract, --fixtures, or --explain"])
        print_result(result, args.json)
        return exit_code_for_result(result.result)

    if args.explain:
        payload = explain_payload()
        result = ValidationResult(RESULT_OK, [])
        if args.json:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            print(RESULT_OK)
            print("Validator rules are available.")
        return 0

    if args.contract:
        path = Path(args.contract)
        result = validate_contract(path)
        print_result(result, args.json, contract=args.contract)
        return exit_code_for_result(result.result)

    fixture_result, summary = run_fixtures()
    print_result(fixture_result, args.json, fixture_summary=summary)
    return exit_code_for_result(fixture_result.result)


if __name__ == "__main__":
    sys.exit(main())
