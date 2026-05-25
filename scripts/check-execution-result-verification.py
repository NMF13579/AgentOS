#!/usr/bin/env python3
"""
Execution Result Verification CLI

This CLI evaluates whether the result of a controlled execution session satisfies the M59 verification policies.

M59 CLI classifies execution result verification state.
M59 CLI does not approve task completion.
M59 CLI does not create approval.
M59 CLI does not authorize merge, push, or release.
M59 CLI does not mutate lifecycle state.
M59 CLI does not replace human review.
M59 CLI does not start M60 cleanup.
M59 CLI does not create fixtures.
M59 CLI does not perform human review.
"""

import sys
import json
import argparse
from pathlib import Path

# Policy decision constants
M59_VERIFICATION_POLICY_VERIFIED = "M59_VERIFICATION_POLICY_VERIFIED"
M59_VERIFICATION_POLICY_VERIFIED_WITH_WARNINGS = "M59_VERIFICATION_POLICY_VERIFIED_WITH_WARNINGS"
M59_VERIFICATION_POLICY_NOT_VERIFIED = "M59_VERIFICATION_POLICY_NOT_VERIFIED"
M59_VERIFICATION_POLICY_BLOCKED = "M59_VERIFICATION_POLICY_BLOCKED"

# Result values constants
EXECUTION_RESULT_VERIFIED = "EXECUTION_RESULT_VERIFIED"
EXECUTION_RESULT_VERIFIED_WITH_WARNINGS = "EXECUTION_RESULT_VERIFIED_WITH_WARNINGS"
EXECUTION_RESULT_NOT_VERIFIED = "EXECUTION_RESULT_NOT_VERIFIED"
EXECUTION_RESULT_BLOCKED = "EXECUTION_RESULT_BLOCKED"

# Non-authority statements
NON_AUTHORITY_STATEMENTS = [
    "M59 CLI does not approve task completion.",
    "M59 CLI does not create approval.",
    "M59 CLI does not authorize merge, push, or release.",
    "M59 CLI does not mutate lifecycle state.",
    "M59 CLI does not replace human review.",
    "M59 CLI only classifies execution result verification state for human review handoff."
]


def check_and_resolve_path(path_str, root_dir):
    """
    Checks path safety by resolving it and confirming it resolves under root_dir.
    Returns (is_safe, resolved_path).
    """
    try:
        resolved_root = Path(root_dir).resolve()
        path_obj = Path(path_str)
        if path_obj.is_absolute():
            resolved_path = path_obj.resolve()
        else:
            resolved_path = (resolved_root / path_obj).resolve()
        is_safe = (resolved_path == resolved_root or resolved_root in resolved_path.parents)
        return is_safe, resolved_path
    except Exception:
        return False, None


def check_json_fields_recursively(data, blockers_list, authority_claims_set):
    """
    Recursively scans parsed JSON node for authority claims and human review handoff issues.
    """
    authority_keys = {
        "task_complete", "task_approved", "human_review_replaced",
        "merge_allowed", "push_allowed", "release_allowed",
        "lifecycle_mutation_allowed", "m60_cleanup_started",
        "approval_created_by_m59"
    }
    
    def recurse(node):
        if isinstance(node, dict):
            for k, v in node.items():
                if k in authority_keys and v is True:
                    authority_claims_set.add(k)
                    blockers_list.append(f"Authority claim detected: key '{k}' set to true.")
                if k == "human_review_required" and v is False:
                    blockers_list.append("Blocker: human_review_required is set to false.")
                if k == "human_review_handoff_required" and v is False:
                    blockers_list.append("Blocker: human_review_handoff_required is set to false.")
                recurse(v)
        elif isinstance(node, list):
            for item in node:
                recurse(item)
                
    recurse(data)


def load_and_scan_artifact(path_str, root_dir, name, loader_errors_list, blockers_list, authority_claims_set):
    """
    Resolves a path, checks safety containment, reads raw text to scan for uppercase claims,
    parses JSON, and recursively scans fields for authority/handoff violations.
    """
    is_safe, resolved_path = check_and_resolve_path(path_str, root_dir)
    if not is_safe:
        loader_errors_list.append(f"Path safety violation: {name} path resolves outside repository root.")
        return None
    
    if resolved_path is None or not resolved_path.is_file():
        loader_errors_list.append(f"Missing file: {name} artifact does not exist.")
        return None
    
    # Read raw content to check for uppercase claims
    try:
        raw_content = resolved_path.read_text(encoding="utf-8")
    except Exception as e:
        loader_errors_list.append(f"Failed to read file {name}: {str(e)}")
        return None

    # Scan uppercase claim patterns in serialized JSON
    uppercase_to_lowercase = {
        "TASK_COMPLETE: true": "task_complete",
        "TASK_APPROVED: true": "task_approved",
        "HUMAN_REVIEW_REPLACED: true": "human_review_replaced",
        "MERGE_ALLOWED: true": "merge_allowed",
        "PUSH_ALLOWED: true": "push_allowed",
        "RELEASE_ALLOWED: true": "release_allowed",
        "LIFECYCLE_MUTATION_ALLOWED: true": "lifecycle_mutation_allowed",
        "M60_CLEANUP_STARTED: true": "m60_cleanup_started",
        "APPROVAL_CREATED_BY_M59: true": "approval_created_by_m59"
    }
    for claim, key_name in uppercase_to_lowercase.items():
        if claim in raw_content:
            authority_claims_set.add(key_name)
            blockers_list.append(f"Authority claim detected in {name} raw JSON: {claim}")

    # Parse JSON content
    try:
        data = json.loads(raw_content)
    except Exception as e:
        loader_errors_list.append(f"Malformed JSON in {name} artifact: {str(e)}")
        return None

    # Recursively check fields
    check_json_fields_recursively(data, blockers_list, authority_claims_set)

    return data


def extract_warnings(data):
    """
    Extracts warnings from common keys.
    """
    warnings_list = []
    for field in ["warnings", "warning", "advisory_warnings", "integrity_warnings"]:
        if field in data:
            val = data[field]
            if isinstance(val, list):
                warnings_list.extend([str(item) for item in val])
            elif val:
                warnings_list.append(str(val))
    return warnings_list


def extract_blockers(data):
    """
    Extracts blockers from common keys.
    """
    blockers_list = []
    for field in ["blockers", "blocker", "errors", "violations"]:
        if field in data:
            val = data[field]
            if isinstance(val, list):
                blockers_list.extend([str(item) for item in val])
            elif val:
                blockers_list.append(str(val))
    return blockers_list


def classify_layer_status(status):
    """
    Maps M59 layer statuses to corresponding upstream state classification.
    """
    verified_statuses = {
        "EXECUTION_RESULT_PRECONDITIONS_READY",
        "SCOPE_VERIFICATION_PASS",
        "VALIDATION_EVIDENCE_CONFIRMED"
    }
    warnings_statuses = {
        "EXECUTION_RESULT_PRECONDITIONS_READY_WITH_WARNINGS",
        "SCOPE_VERIFICATION_PASS_WITH_WARNINGS",
        "VALIDATION_EVIDENCE_CONFIRMED_WITH_WARNINGS"
    }
    not_ready_statuses = {
        "EXECUTION_RESULT_PRECONDITIONS_NOT_READY",
        "SCOPE_VERIFICATION_NOT_READY",
        "VALIDATION_EVIDENCE_NOT_CONFIRMED"
    }
    blocked_statuses = {
        "EXECUTION_RESULT_PRECONDITIONS_BLOCKED",
        "SCOPE_VERIFICATION_BLOCKED",
        "VALIDATION_EVIDENCE_BLOCKED"
    }
    
    if status in verified_statuses:
        return "VERIFIED"
    elif status in warnings_statuses:
        return "VERIFIED_WITH_WARNINGS"
    elif status in not_ready_statuses:
        return "NOT_READY"
    elif status in blocked_statuses:
        return "BLOCKED"
    else:
        return "BLOCKED"  # Missing/unknown/malformed resolves to BLOCKED


def classify_output_status(status):
    """
    Maps M59 verification result status to corresponding output state classification.
    """
    if status == "EXECUTION_RESULT_VERIFIED":
        return "VERIFIED"
    elif status == "EXECUTION_RESULT_VERIFIED_WITH_WARNINGS":
        return "VERIFIED_WITH_WARNINGS"
    elif status == "EXECUTION_RESULT_NOT_VERIFIED":
        return "NOT_VERIFIED"
    elif status == "EXECUTION_RESULT_BLOCKED":
        return "BLOCKED"
    else:
        return "BLOCKED"


def print_explain(args):
    """
    Prints human-readable explanation of how the CLI classifies states and resolves consistency.
    """
    explanation = """Execution Result Verification CLI - Explain Mode

This CLI evaluates whether the result of a controlled execution session satisfies the M59 verification policies.

Artifacts read:
- Input contract: {}
- Preconditions: {}
- Git diff/scope: {}
- Validation evidence: {}
- Result/output: {}

Upstream Classification:
- Upstream verification layers (preconditions, git diff and scope, validation evidence) are authoritative.
- Their statuses are extracted and classified into a composite upstream state.
- Priority order: BLOCKED > NOT_VERIFIED > VERIFIED_WITH_WARNINGS > VERIFIED.

Result / Output Consistency Rule:
- The result/output status (59.6) acts as a consistency signal.
- The consistency table resolves mixed upstream/output states.
- A final decision is selected based on consistency rules.

Safety Boundaries & Non-Authority Rules:
- A successful verification result is not approval.
- Human review remains required and cannot be replaced.
- This script does not authorize commit, merge, push, release, or lifecycle mutation.
""".format(args.input, args.preconditions, args.diff_scope, args.validation_evidence, args.result_output)
    print(explanation)


def main():
    parser = argparse.ArgumentParser(
        description="Execution Result Verification CLI",
        add_help=True
    )
    parser.add_argument("--root", default=".", help="Repository root directory")
    parser.add_argument("--input", required=True, help="Path to input contract JSON")
    parser.add_argument("--preconditions", required=True, help="Path to preconditions JSON")
    parser.add_argument("--diff-scope", required=True, help="Path to diff/scope JSON")
    parser.add_argument("--validation-evidence", required=True, help="Path to validation evidence JSON")
    parser.add_argument("--result-output", required=True, help="Path to result output JSON")
    parser.add_argument("--json", action="store_true", help="Output JSON only to stdout")
    parser.add_argument("--explain", action="store_true", help="Print explain output and exit")
    parser.add_argument("--strict", action="store_true", help="Enable strict mode")

    args = parser.parse_args()

    if args.explain:
        print_explain(args)
        sys.exit(0)

    # 1. Resolve root directory
    try:
        resolved_root = Path(args.root or ".").resolve()
    except Exception as e:
        output = {
            "result": EXECUTION_RESULT_BLOCKED,
            "policy_decision": M59_VERIFICATION_POLICY_BLOCKED,
            "exit_code": 2,
            "strict": args.strict,
            "strict_upgrades_applied": 0,
            "upstream_state": "UNKNOWN",
            "output_state": "UNKNOWN",
            "input_status": None,
            "preconditions_status": None,
            "diff_scope_status": None,
            "validation_evidence_status": None,
            "verification_result_status": None,
            "warnings": [],
            "blockers": [f"Failed to resolve root directory: {str(e)}"],
            "not_verified_reasons": [],
            "authority_claims_detected": [],
            "non_authority": NON_AUTHORITY_STATEMENTS
        }
        if args.json:
            print(json.dumps(output, indent=2))
        else:
            print(f"RESULT: {output['result']}")
            print(f"POLICY_DECISION: {output['policy_decision']}")
            print(f"EXIT_CODE: {output['exit_code']}")
            print(f"UPSTREAM_STATE: {output['upstream_state']}")
            print(f"OUTPUT_STATE: {output['output_state']}")
            print(f"STRICT: {output['strict']}")
            print(f"WARNINGS: {output['warnings']}")
            print(f"BLOCKERS: {output['blockers']}")
            print(f"NOT_VERIFIED_REASONS: {output['not_verified_reasons']}")
        sys.exit(2)

    loader_errors = []
    blockers = []
    warnings = []
    not_verified_reasons = []
    authority_claims = set()

    # 2. Load and scan artifacts
    input_data = load_and_scan_artifact(args.input, resolved_root, "input", loader_errors, blockers, authority_claims)
    pre_data = load_and_scan_artifact(args.preconditions, resolved_root, "preconditions", loader_errors, blockers, authority_claims)
    diff_data = load_and_scan_artifact(args.diff_scope, resolved_root, "diff-scope", loader_errors, blockers, authority_claims)
    val_data = load_and_scan_artifact(args.validation_evidence, resolved_root, "validation-evidence", loader_errors, blockers, authority_claims)
    res_data = load_and_scan_artifact(args.result_output, resolved_root, "result-output", loader_errors, blockers, authority_claims)

    input_status = None
    preconditions_status = None
    diff_scope_status = None
    validation_evidence_status = None
    verification_result_status = None

    if loader_errors:
        # If loader failed, we can't extract state or run policy logic
        all_blockers = loader_errors + blockers
        output = {
            "result": EXECUTION_RESULT_BLOCKED,
            "policy_decision": M59_VERIFICATION_POLICY_BLOCKED,
            "exit_code": 2,
            "strict": args.strict,
            "strict_upgrades_applied": 0,
            "upstream_state": "UNKNOWN",
            "output_state": "UNKNOWN",
            "input_status": None,
            "preconditions_status": None,
            "diff_scope_status": None,
            "validation_evidence_status": None,
            "verification_result_status": None,
            "warnings": warnings,
            "blockers": all_blockers,
            "not_verified_reasons": not_verified_reasons,
            "authority_claims_detected": sorted(list(authority_claims)),
            "non_authority": NON_AUTHORITY_STATEMENTS
        }
        if args.json:
            print(json.dumps(output, indent=2))
        else:
            print(f"RESULT: {output['result']}")
            print(f"POLICY_DECISION: {output['policy_decision']}")
            print(f"EXIT_CODE: {output['exit_code']}")
            print(f"UPSTREAM_STATE: {output['upstream_state']}")
            print(f"OUTPUT_STATE: {output['output_state']}")
            print(f"STRICT: {str(output['strict'])}")
            print(f"WARNINGS: {str(output['warnings'])}")
            print(f"BLOCKERS: {str(output['blockers'])}")
            print(f"NOT_VERIFIED_REASONS: {str(output['not_verified_reasons'])}")
        sys.exit(2)

    # 3. Extract status fields
    input_status = input_data.get("input_status")
    preconditions_status = pre_data.get("preconditions_status")
    diff_scope_status = diff_data.get("diff_scope_status")
    validation_evidence_status = val_data.get("validation_evidence_status")
    verification_result_status = res_data.get("verification_result_status")

    # Validate existence of status fields
    if not input_status:
        blockers.append("Missing field: input_status in input artifact")
    if not preconditions_status:
        blockers.append("Missing field: preconditions_status in preconditions artifact")
    if not diff_scope_status:
        blockers.append("Missing field: diff_scope_status in diff-scope artifact")
    if not validation_evidence_status:
        blockers.append("Missing field: validation_evidence_status in validation-evidence artifact")
    if not verification_result_status:
        blockers.append("Missing field: verification_result_status in result-output artifact")

    # Collect blockers/warnings defined in the JSON files themselves
    for data in [input_data, pre_data, diff_data, val_data, res_data]:
        if data:
            blockers.extend(extract_blockers(data))
            warnings.extend(extract_warnings(data))

    # Composite upstream state classification
    pre_class = classify_layer_status(preconditions_status)
    diff_class = classify_layer_status(diff_scope_status)
    val_class = classify_layer_status(validation_evidence_status)
    
    upstream_priority = ["VERIFIED", "VERIFIED_WITH_WARNINGS", "NOT_READY", "BLOCKED"]
    max_idx = max(
        upstream_priority.index(pre_class),
        upstream_priority.index(diff_class),
        upstream_priority.index(val_class)
    )
    upstream_state = upstream_priority[max_idx]

    # Output state classification
    output_state = classify_output_status(verification_result_status)

    # Result Output Consistency Table Evaluation
    if upstream_state == "BLOCKED" or output_state == "BLOCKED" or blockers or len(authority_claims) > 0:
        result = EXECUTION_RESULT_BLOCKED
        policy_decision = M59_VERIFICATION_POLICY_BLOCKED
        exit_code = 2
        if not blockers and not authority_claims:
            blockers.append("Upstream or output state is BLOCKED.")
    elif upstream_state == "NOT_READY":
        if output_state == "VERIFIED":
            result = EXECUTION_RESULT_NOT_VERIFIED
            policy_decision = M59_VERIFICATION_POLICY_NOT_VERIFIED
            exit_code = 1
            not_verified_reasons.append("Upstream NOT_READY while output claims VERIFIED.")
        elif output_state == "NOT_VERIFIED":
            result = EXECUTION_RESULT_NOT_VERIFIED
            policy_decision = M59_VERIFICATION_POLICY_NOT_VERIFIED
            exit_code = 1
            not_verified_reasons.append("Upstream NOT_READY and output is NOT_VERIFIED.")
        else:
            result = EXECUTION_RESULT_BLOCKED
            policy_decision = M59_VERIFICATION_POLICY_BLOCKED
            exit_code = 2
            blockers.append(f"Inconsistent state classification: upstream NOT_READY + output {output_state}")
    elif upstream_state == "VERIFIED_WITH_WARNINGS":
        if output_state in ("VERIFIED", "VERIFIED_WITH_WARNINGS"):
            result = EXECUTION_RESULT_VERIFIED_WITH_WARNINGS
            policy_decision = M59_VERIFICATION_POLICY_VERIFIED_WITH_WARNINGS
            exit_code = 0
        elif output_state == "NOT_VERIFIED":
            result = EXECUTION_RESULT_NOT_VERIFIED
            policy_decision = M59_VERIFICATION_POLICY_NOT_VERIFIED
            exit_code = 1
            not_verified_reasons.append("Output indicates NOT_VERIFIED while upstream has warnings.")
        else:
            result = EXECUTION_RESULT_BLOCKED
            policy_decision = M59_VERIFICATION_POLICY_BLOCKED
            exit_code = 2
            blockers.append(f"Inconsistent state classification: upstream VERIFIED_WITH_WARNINGS + output {output_state}")
    elif upstream_state == "VERIFIED":
        if output_state == "VERIFIED":
            result = EXECUTION_RESULT_VERIFIED
            policy_decision = M59_VERIFICATION_POLICY_VERIFIED
            exit_code = 0
        elif output_state == "VERIFIED_WITH_WARNINGS":
            result = EXECUTION_RESULT_VERIFIED_WITH_WARNINGS
            policy_decision = M59_VERIFICATION_POLICY_VERIFIED_WITH_WARNINGS
            exit_code = 0
        elif output_state == "NOT_VERIFIED":
            result = EXECUTION_RESULT_NOT_VERIFIED
            policy_decision = M59_VERIFICATION_POLICY_NOT_VERIFIED
            exit_code = 1
            not_verified_reasons.append("Output indicates NOT_VERIFIED while upstream is VERIFIED.")
        else:
            result = EXECUTION_RESULT_BLOCKED
            policy_decision = M59_VERIFICATION_POLICY_BLOCKED
            exit_code = 2
            blockers.append(f"Inconsistent state classification: upstream VERIFIED + output {output_state}")

    # Downgrade clean VERIFIED if warnings exist
    if result == EXECUTION_RESULT_VERIFIED and warnings:
        result = EXECUTION_RESULT_VERIFIED_WITH_WARNINGS
        policy_decision = M59_VERIFICATION_POLICY_VERIFIED_WITH_WARNINGS

    # Strict mode warning upgrades
    strict_upgrades_applied = 0
    if args.strict and result in (EXECUTION_RESULT_VERIFIED, EXECUTION_RESULT_VERIFIED_WITH_WARNINGS):
        strict_upgrade_needed = False
        strict_phrases = [
            "source integrity uncertainty",
            "evidence freshness uncertainty",
            "path safety uncertainty",
            "unknown authority claims",
            "human review handoff uncertainty"
        ]
        for w in warnings:
            for phrase in strict_phrases:
                if phrase in w.lower():
                    strict_upgrade_needed = True
                    blockers.append(f"Strict mode blocker: warning matches '{phrase}'.")
                    strict_upgrades_applied += 1
        
        if strict_upgrade_needed:
            result = EXECUTION_RESULT_BLOCKED
            policy_decision = M59_VERIFICATION_POLICY_BLOCKED
            exit_code = 2

    # Prepare output dictionary
    output = {
        "result": result,
        "policy_decision": policy_decision,
        "exit_code": exit_code,
        "strict": args.strict,
        "strict_upgrades_applied": strict_upgrades_applied,
        "upstream_state": upstream_state,
        "output_state": output_state,
        "input_status": input_status,
        "preconditions_status": preconditions_status,
        "diff_scope_status": diff_scope_status,
        "validation_evidence_status": validation_evidence_status,
        "verification_result_status": verification_result_status,
        "warnings": warnings,
        "blockers": blockers,
        "not_verified_reasons": not_verified_reasons,
        "authority_claims_detected": sorted(list(authority_claims)),
        "non_authority": NON_AUTHORITY_STATEMENTS
    }

    if args.json:
        print(json.dumps(output, indent=2))
    else:
        print(f"RESULT: {output['result']}")
        print(f"POLICY_DECISION: {output['policy_decision']}")
        print(f"EXIT_CODE: {output['exit_code']}")
        print(f"UPSTREAM_STATE: {output['upstream_state']}")
        print(f"OUTPUT_STATE: {output['output_state']}")
        print(f"STRICT: {str(output['strict'])}")
        print(f"WARNINGS: {str(output['warnings'])}")
        print(f"BLOCKERS: {str(output['blockers'])}")
        print(f"NOT_VERIFIED_REASONS: {str(output['not_verified_reasons'])}")

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
