#!/usr/bin/env python3
"""
M57 Execution Authorization Checker CLI.
This script checks execution authorization based on M57 inputs, preconditions,
and M56 completion reviews.
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# Result Constants
EXECUTION_AUTHORIZATION_CONFIRMED = "EXECUTION_AUTHORIZATION_CONFIRMED"
EXECUTION_AUTHORIZATION_CONFIRMED_WITH_LIMITATIONS = "EXECUTION_AUTHORIZATION_CONFIRMED_WITH_LIMITATIONS"
EXECUTION_AUTHORIZATION_NOT_CONFIRMED = "EXECUTION_AUTHORIZATION_NOT_CONFIRMED"
EXECUTION_AUTHORIZATION_BLOCKED = "EXECUTION_AUTHORIZATION_BLOCKED"

# Policy Constants
EXECUTION_AUTHORIZATION_POLICY_CONFIRMED = "EXECUTION_AUTHORIZATION_POLICY_CONFIRMED"
EXECUTION_AUTHORIZATION_POLICY_CONFIRMED_WITH_LIMITATIONS = "EXECUTION_AUTHORIZATION_POLICY_CONFIRMED_WITH_LIMITATIONS"
EXECUTION_AUTHORIZATION_POLICY_NOT_CONFIRMED = "EXECUTION_AUTHORIZATION_POLICY_NOT_CONFIRMED"
EXECUTION_AUTHORIZATION_POLICY_BLOCKED = "EXECUTION_AUTHORIZATION_POLICY_BLOCKED"

# Exit Code Constants
EXIT_CONFIRMED = 0
EXIT_CONFIRMED_WITH_LIMITATIONS = 0
EXIT_NOT_CONFIRMED = 1
EXIT_BLOCKED = 2

# Boundary Markers
BOUNDARY_MARKERS = [
    "M57 CLI is read-only.",
    "M57 CLI does not authorize execution by side effect.",
    "M57 CLI does not start M58.",
    "M57 CLI does not create approval records.",
    "M57 CLI does not mutate lifecycle state.",
    "M57 CLI does not modify tasks/active-task.md.",
    "Exit code 0 is not execution.",
    "Exit code 0 does not start M58."
]

NON_AUTHORITY_MARKERS = [
    "M57 authorization result is not execution.",
    "M57 authorization result does not authorize execution.",
    "M57 authorization result does not start execution.",
    "M57 authorization result does not create approval records.",
    "M57 authorization result does not authorize lifecycle mutation.",
    "M57 authorization result does not authorize M58.",
    "M57 authorization result does not start M58.",
    "M57 authorization result does not modify tasks/active-task.md.",
    "M58 must independently validate M57 completion before any M58 planning work."
]

UNSAFE_CLAIMS = [
    "execution is approved",
    "execution is authorized",
    "M58 is authorized",
    "M58 may start",
    "M58 started",
    "approval has been created",
    "lifecycle mutation has been authorized",
    "tasks/active-task.md was modified by M57"
]

def parse_args(args_list: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="M57 Execution Authorization Checker")
    parser.add_argument("--input", type=str, help="Path to M57 authorization input")
    parser.add_argument("--preconditions", type=str, help="Path to M57 authorization preconditions")
    parser.add_argument("--m56-completion-review", type=str, help="Path to M56 completion review")
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    parser.add_argument("--explain", action="store_true", help="Explain mode")
    return parser.parse_args(args_list)

def parse_json_or_markdown_json(path_str: str) -> Dict[str, Any]:
    path = Path(path_str)
    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path_str}")
    
    content = path.read_text(encoding="utf-8")
    
    if path.suffix.lower() == ".md":
        # Extract exactly one fenced json block
        blocks = re.findall(r"```json\s*(.*?)\s*```", content, re.DOTALL)
        if len(blocks) != 1:
            raise ValueError(f"Markdown file {path_str} must contain exactly one fenced json block (found {len(blocks)})")
        json_str = blocks[0]
    else:
        json_str = content
        
    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON in {path_str}: {e}")

def parse_frontmatter_fields(path_str: str) -> Dict[str, Any]:
    path = Path(path_str)
    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path_str}")
    
    content = path.read_text(encoding="utf-8")
    # Frontmatter is between --- and --- at the start
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not match:
        raise ValueError(f"No frontmatter found in {path_str}")
    
    frontmatter_text = match.group(1)
    fields = {}
    for line in frontmatter_text.splitlines():
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip()
            # Parse booleans and strings
            if val.lower() == "true":
                fields[key] = True
            elif val.lower() == "false":
                fields[key] = False
            else:
                fields[key] = val
                
    required = [
        "m56_final_status",
        "evidence_status",
        "execution_authorized",
        "execution_started",
        "approval_created",
        "lifecycle_mutation_authorized",
        "m57_authorized",
        "m57_started"
    ]
    
    for req in required:
        if req not in fields:
            raise ValueError(f"Missing required frontmatter field '{req}' in {path_str}")
            
    # Check boundaries
    boundaries = [
        "execution_authorized",
        "execution_started",
        "approval_created",
        "lifecycle_mutation_authorized",
        "m57_authorized",
        "m57_started"
    ]
    for b in boundaries:
        if fields[b] is not False:
            raise ValueError(f"M56 boundary field '{b}' is not false in {path_str}")
            
    return fields

def scan_unsafe_claims(path_str: str) -> List[str]:
    path = Path(path_str)
    if not path.is_file():
        return []
    content = path.read_text(encoding="utf-8")
    found = []
    for line in content.splitlines():
        for claim in UNSAFE_CLAIMS:
            if claim.lower() in line.lower():
                # Ignore negative boundary statements
                lower_line = line.lower()
                is_negative = (
                    "not" in lower_line or
                    "false" in lower_line or
                    "never" in lower_line or
                    "no " in lower_line or
                    "without" in lower_line or
                    "prevent" in lower_line
                )
                if not is_negative:
                    found.append(claim)
    return list(set(found))

def validate_input_object(input_data: Dict[str, Any]) -> Dict[str, Any]:
    if "execution_authorization_input" not in input_data:
        raise ValueError("Missing 'execution_authorization_input' root object")
    
    obj = input_data["execution_authorization_input"]
    required_fields = [
        "schema_version",
        "input_id",
        "source_m56_completion_review",
        "source_m56_evidence_report",
        "source_active_task",
        "authorization_request_status",
        "requested_execution_mode",
        "expected_execution_session_type",
        "required_traceability",
        "required_boundaries",
        "boundary_flags",
        "carry_forward_limitations",
        "warnings",
        "blockers",
        "non_authority_markers"
    ]
    for f in required_fields:
        if f not in obj:
            raise ValueError(f"Missing input field '{f}'")
            
    # Check empty required structures
    for f in ["required_traceability", "required_boundaries", "non_authority_markers"]:
        if not obj[f]:
            raise ValueError(f"Input field '{f}' is empty")
            
    # Check boundary flags
    flags = obj["boundary_flags"]
    unsafe_flags = [
        "execution_authorized",
        "execution_started",
        "approval_created",
        "lifecycle_mutation_authorized",
        "m58_authorized",
        "m58_started"
    ]
    for f in unsafe_flags:
        if flags.get(f) is not False:
            raise ValueError(f"Input boundary flag '{f}' is not false")
            
    # Check status enum
    status = obj["authorization_request_status"]
    allowed_statuses = [
        "EXECUTION_AUTHORIZATION_INPUT_READY",
        "EXECUTION_AUTHORIZATION_INPUT_READY_WITH_LIMITATIONS",
        "EXECUTION_AUTHORIZATION_INPUT_NOT_READY",
        "EXECUTION_AUTHORIZATION_INPUT_BLOCKED"
    ]
    if status not in allowed_statuses:
        raise ValueError(f"Unknown input request status: {status}")
        
    return obj

def validate_preconditions_object(prec_data: Dict[str, Any]) -> Dict[str, Any]:
    if "execution_authorization_preconditions" not in prec_data:
        raise ValueError("Missing 'execution_authorization_preconditions' root object")
        
    obj = prec_data["execution_authorization_preconditions"]
    required_fields = [
        "schema_version",
        "preconditions_id",
        "source_m56_completion_review",
        "source_m56_evidence_report",
        "source_authorization_input",
        "source_active_task",
        "preconditions_status",
        "required_sources",
        "required_traceability",
        "required_boundaries",
        "boundary_flags",
        "performed_actions",
        "carry_forward_limitations",
        "warnings",
        "blockers",
        "non_authority_markers"
    ]
    for f in required_fields:
        if f not in obj:
            raise ValueError(f"Missing precondition field '{f}'")
            
    # Check empty required structures
    for f in ["required_traceability", "required_boundaries", "non_authority_markers"]:
        if not obj[f]:
            raise ValueError(f"Precondition field '{f}' is empty")
            
    # Check boundary flags
    flags = obj["boundary_flags"]
    unsafe_flags = [
        "execution_authorized",
        "execution_started",
        "approval_created",
        "lifecycle_mutation_authorized",
        "m58_authorized",
        "m58_started"
    ]
    for f in unsafe_flags:
        if flags.get(f) is not False:
            raise ValueError(f"Precondition boundary flag '{f}' is not false")
            
    # Check performed actions
    actions = obj["performed_actions"]
    unsafe_actions = [
        "active_task_modified",
        "approval_record_created",
        "lifecycle_mutation_performed",
        "execution_started",
        "m58_artifact_created",
        "m58_started"
    ]
    for f in unsafe_actions:
        if actions.get(f) is not False:
            raise ValueError(f"Precondition performed action '{f}' is not false")
            
    # Check status enum
    status = obj["preconditions_status"]
    allowed_statuses = [
        "EXECUTION_AUTHORIZATION_PRECONDITIONS_PASS",
        "EXECUTION_AUTHORIZATION_PRECONDITIONS_PASS_WITH_WARNINGS",
        "EXECUTION_AUTHORIZATION_PRECONDITIONS_NOT_READY",
        "EXECUTION_AUTHORIZATION_PRECONDITIONS_BLOCKED"
    ]
    if status not in allowed_statuses:
        raise ValueError(f"Unknown precondition status: {status}")
        
    return obj

def validate_m56_completion_review(m56_fields: Dict[str, Any]) -> None:
    final_status = m56_fields["m56_final_status"]
    evidence_status = m56_fields["evidence_status"]
    
    allowed_final = [
        "M56_EXECUTION_READINESS_COMPLETE",
        "M56_EXECUTION_READINESS_COMPLETE_WITH_LIMITATIONS",
        "M56_EXECUTION_READINESS_INCOMPLETE",
        "M56_EXECUTION_READINESS_BLOCKED"
    ]
    if final_status not in allowed_final:
        raise ValueError(f"Unknown M56 final status: {final_status}")
        
    allowed_evidence = [
        "M56_EXECUTION_READINESS_EVIDENCE_READY",
        "M56_EXECUTION_READINESS_EVIDENCE_NOT_PASSING",
        "M56_EXECUTION_READINESS_EVIDENCE_BLOCKED"
    ]
    if evidence_status not in allowed_evidence:
        raise ValueError(f"Unknown M56 evidence status: {evidence_status}")

def classify_policy(
    m56_final_status: str,
    m56_evidence_status: str,
    input_status: str,
    preconditions_status: str,
    has_unsafe_claims: bool,
    has_blockers: bool,
    has_warnings_or_limitations: bool
) -> str:
    # 1. Blocked checks
    if (
        has_unsafe_claims or
        has_blockers or
        m56_final_status == "M56_EXECUTION_READINESS_BLOCKED" or
        m56_evidence_status == "M56_EXECUTION_READINESS_EVIDENCE_BLOCKED" or
        input_status == "EXECUTION_AUTHORIZATION_INPUT_BLOCKED" or
        preconditions_status == "EXECUTION_AUTHORIZATION_PRECONDITIONS_BLOCKED"
    ):
        return EXECUTION_AUTHORIZATION_POLICY_BLOCKED
        
    # 2. Not confirmed checks
    if (
        m56_final_status == "M56_EXECUTION_READINESS_INCOMPLETE" or
        m56_evidence_status == "M56_EXECUTION_READINESS_EVIDENCE_NOT_PASSING" or
        input_status == "EXECUTION_AUTHORIZATION_INPUT_NOT_READY" or
        preconditions_status == "EXECUTION_AUTHORIZATION_PRECONDITIONS_NOT_READY"
    ):
        return EXECUTION_AUTHORIZATION_POLICY_NOT_CONFIRMED
        
    # 3. Confirmed with limitations checks
    if (
        m56_final_status == "M56_EXECUTION_READINESS_COMPLETE_WITH_LIMITATIONS" or
        input_status == "EXECUTION_AUTHORIZATION_INPUT_READY_WITH_LIMITATIONS" or
        preconditions_status == "EXECUTION_AUTHORIZATION_PRECONDITIONS_PASS_WITH_WARNINGS" or
        has_warnings_or_limitations
    ):
        return EXECUTION_AUTHORIZATION_POLICY_CONFIRMED_WITH_LIMITATIONS
        
    # 4. Confirmed checks
    if (
        m56_final_status == "M56_EXECUTION_READINESS_COMPLETE" and
        m56_evidence_status == "M56_EXECUTION_READINESS_EVIDENCE_READY" and
        input_status == "EXECUTION_AUTHORIZATION_INPUT_READY" and
        preconditions_status == "EXECUTION_AUTHORIZATION_PRECONDITIONS_PASS"
    ):
        return EXECUTION_AUTHORIZATION_POLICY_CONFIRMED
        
    return EXECUTION_AUTHORIZATION_POLICY_BLOCKED

def policy_to_result(policy: str) -> str:
    mapping = {
        EXECUTION_AUTHORIZATION_POLICY_CONFIRMED: EXECUTION_AUTHORIZATION_CONFIRMED,
        EXECUTION_AUTHORIZATION_POLICY_CONFIRMED_WITH_LIMITATIONS: EXECUTION_AUTHORIZATION_CONFIRMED_WITH_LIMITATIONS,
        EXECUTION_AUTHORIZATION_POLICY_NOT_CONFIRMED: EXECUTION_AUTHORIZATION_NOT_CONFIRMED,
        EXECUTION_AUTHORIZATION_POLICY_BLOCKED: EXECUTION_AUTHORIZATION_BLOCKED
    }
    return mapping.get(policy, EXECUTION_AUTHORIZATION_BLOCKED)

def result_to_exit_code(result: str) -> int:
    mapping = {
        EXECUTION_AUTHORIZATION_CONFIRMED: EXIT_CONFIRMED,
        EXECUTION_AUTHORIZATION_CONFIRMED_WITH_LIMITATIONS: EXIT_CONFIRMED_WITH_LIMITATIONS,
        EXECUTION_AUTHORIZATION_NOT_CONFIRMED: EXIT_NOT_CONFIRMED,
        EXECUTION_AUTHORIZATION_BLOCKED: EXIT_BLOCKED
    }
    return mapping.get(result, EXIT_BLOCKED)

def build_result_payload(
    result: str,
    exit_code: int,
    source_m56_completion_review: str,
    source_authorization_input: str,
    source_authorization_preconditions: str,
    authorization_request_status: str,
    preconditions_status: str,
    m56_final_status: str,
    m56_evidence_status: str,
    performed_actions: Dict[str, bool],
    carry_forward_limitations: List[str],
    warnings: List[str],
    blockers: List[str]
) -> Dict[str, Any]:
    return {
        "execution_authorization_result": {
            "schema_version": "1.0.0",
            "result_id": "m57-auth-result",
            "result": result,
            "exit_code": exit_code,
            "source_m56_completion_review": source_m56_completion_review,
            "source_m56_evidence_report": "reports/m56-execution-readiness-evidence-report.md",
            "source_authorization_input": source_authorization_input,
            "source_authorization_preconditions": source_authorization_preconditions,
            "source_active_task": "tasks/active-task.md",
            "authorization_request_status": authorization_request_status,
            "preconditions_status": preconditions_status,
            "m56_final_status": m56_final_status,
            "m56_evidence_status": m56_evidence_status,
            "traceability_result": {
                "m57_intake_report": "reports/m57-m56-completion-intake.md"
            },
            "boundary_result": {
                "execution_authorized": False,
                "execution_started": False,
                "approval_created": False,
                "lifecycle_mutation_authorized": False,
                "m58_authorized": False,
                "m58_started": False
            },
            "performed_actions": performed_actions,
            "carry_forward_limitations": carry_forward_limitations,
            "warnings": warnings,
            "blockers": blockers,
            "non_authority_markers": NON_AUTHORITY_MARKERS
        }
    }

def emit_json(payload: Dict[str, Any]) -> None:
    print(json.dumps(payload, indent=2))

def emit_human(payload: Dict[str, Any]) -> None:
    res = payload["execution_authorization_result"]
    print("=== M57 Execution Authorization Result ===")
    print(f"RESULT: {res['result']}")
    print(f"EXIT_CODE: {res['exit_code']}")
    print(f"M56 Final Status: {res['m56_final_status']}")
    print(f"M56 Evidence Status: {res['m56_evidence_status']}")
    print(f"Input Status: {res['authorization_request_status']}")
    print(f"Preconditions Status: {res['preconditions_status']}")
    if res["carry_forward_limitations"]:
        print("LIMITATIONS:")
        for lim in res["carry_forward_limitations"]:
            print(f"  - {lim}")
    if res["warnings"]:
        print("WARNINGS:")
        for w in res["warnings"]:
            print(f"  - {w}")
    if res["blockers"]:
        print("BLOCKERS:")
        for b in res["blockers"]:
            print(f"  - {b}")
    print("NON_AUTHORITY:")
    for marker in res["non_authority_markers"]:
        print(f"  - {marker}")

def emit_explain() -> None:
    print("M57 execution authorization CLI")
    print("This tool is read-only and classifies M57 execution authorization deterministically.")
    for marker in BOUNDARY_MARKERS:
        print(marker)

def main() -> None:
    args = parse_args(sys.argv[1:])
    
    if args.explain:
        emit_explain()
        sys.exit(0)
        
    # Check that inputs are provided if explain is not true
    if not (args.input and args.preconditions and args.m56_completion_review):
        error_msg = "Missing required arguments: --input, --preconditions, and --m56-completion-review are required."
        payload = build_result_payload(
            result=EXECUTION_AUTHORIZATION_BLOCKED,
            exit_code=EXIT_BLOCKED,
            source_m56_completion_review="",
            source_authorization_input="",
            source_authorization_preconditions="",
            authorization_request_status="EXECUTION_AUTHORIZATION_INPUT_BLOCKED",
            preconditions_status="EXECUTION_AUTHORIZATION_PRECONDITIONS_BLOCKED",
            m56_final_status="M56_EXECUTION_READINESS_BLOCKED",
            m56_evidence_status="M56_EXECUTION_READINESS_EVIDENCE_BLOCKED",
            performed_actions={
                "active_task_modified": False,
                "approval_record_created": False,
                "lifecycle_mutation_performed": False,
                "execution_started": False,
                "m58_artifact_created": False,
                "m58_started": False
            },
            carry_forward_limitations=[],
            warnings=[],
            blockers=[error_msg]
        )
        if args.json:
            emit_json(payload)
        else:
            emit_human(payload)
        sys.exit(EXIT_BLOCKED)
        
    try:
        # Load and parse files
        input_data = parse_json_or_markdown_json(args.input)
        prec_data = parse_json_or_markdown_json(args.preconditions)
        m56_fields = parse_frontmatter_fields(args.m56_completion_review)
        
        # Validate objects
        input_obj = validate_input_object(input_data)
        prec_obj = validate_preconditions_object(prec_data)
        validate_m56_completion_review(m56_fields)
        
        # Scan for unsafe claims
        unsafe_claims = []
        for path in [args.input, args.preconditions, args.m56_completion_review]:
            unsafe_claims.extend(scan_unsafe_claims(path))
        unsafe_claims = list(set(unsafe_claims))
        
        # Gather warnings and blockers
        blockers = list(set(input_obj.get("blockers", []) + prec_obj.get("blockers", [])))
        warnings = list(set(input_obj.get("warnings", []) + prec_obj.get("warnings", [])))
        carry_forward = list(set(input_obj.get("carry_forward_limitations", []) + prec_obj.get("carry_forward_limitations", [])))
        
        if unsafe_claims:
            blockers.append(f"Unsafe authority claims detected: {unsafe_claims}")
            
        # Classify policy
        policy = classify_policy(
            m56_final_status=m56_fields["m56_final_status"],
            m56_evidence_status=m56_fields["evidence_status"],
            input_status=input_obj["authorization_request_status"],
            preconditions_status=prec_obj["preconditions_status"],
            has_unsafe_claims=len(unsafe_claims) > 0,
            has_blockers=len(blockers) > 0,
            has_warnings_or_limitations=(len(warnings) > 0 or len(carry_forward) > 0)
        )
        
        result = policy_to_result(policy)
        exit_code = result_to_exit_code(result)
        
        # If we have warnings/blockers, let's reflect that in the payload
        payload = build_result_payload(
            result=result,
            exit_code=exit_code,
            source_m56_completion_review=args.m56_completion_review,
            source_authorization_input=args.input,
            source_authorization_preconditions=args.preconditions,
            authorization_request_status=input_obj["authorization_request_status"],
            preconditions_status=prec_obj["preconditions_status"],
            m56_final_status=m56_fields["m56_final_status"],
            m56_evidence_status=m56_fields["evidence_status"],
            performed_actions=prec_obj["performed_actions"],
            carry_forward_limitations=carry_forward,
            warnings=warnings,
            blockers=blockers
        )
        
        if args.json:
            emit_json(payload)
        else:
            emit_human(payload)
            
        sys.exit(exit_code)
        
    except Exception as e:
        # Fail closed
        payload = build_result_payload(
            result=EXECUTION_AUTHORIZATION_BLOCKED,
            exit_code=EXIT_BLOCKED,
            source_m56_completion_review=args.m56_completion_review or "",
            source_authorization_input=args.input or "",
            source_authorization_preconditions=args.preconditions or "",
            authorization_request_status="EXECUTION_AUTHORIZATION_INPUT_BLOCKED",
            preconditions_status="EXECUTION_AUTHORIZATION_PRECONDITIONS_BLOCKED",
            m56_final_status="M56_EXECUTION_READINESS_BLOCKED",
            m56_evidence_status="M56_EXECUTION_READINESS_EVIDENCE_BLOCKED",
            performed_actions={
                "active_task_modified": False,
                "approval_record_created": False,
                "lifecycle_mutation_performed": False,
                "execution_started": False,
                "m58_artifact_created": False,
                "m58_started": False
            },
            carry_forward_limitations=[],
            warnings=[],
            blockers=[f"An error occurred: {e}"]
        )
        if args.json:
            emit_json(payload)
        else:
            emit_human(payload)
        sys.exit(EXIT_BLOCKED)

if __name__ == "__main__":
    main()
