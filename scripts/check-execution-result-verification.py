#!/usr/bin/env python3
"""
Execution Result Verification CLI Foundation

This script serves as the foundation for the M59 execution result verification CLI.
It is a read-only, deterministic utility that parses verification input, preconditions,
git diff scope, validation evidence, and result/output JSON artifacts.

M59 CLI foundation does not approve task completion.
M59 CLI does not create approval.
M59 CLI does not authorize merge, push, or release.
M59 CLI does not mutate lifecycle state.
M59 CLI does not replace human review.
M59 CLI only classifies execution result verification state for human review handoff.
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


def check_path_safety(path_str, root_dir):
    """
    Checks if the resolved path is contained within the resolved root_dir.
    Returns (is_safe, resolved_path).
    """
    try:
        resolved_root = Path(root_dir).resolve()
        resolved_path = Path(path_str).resolve()
        is_safe = (resolved_path == resolved_root or resolved_root in resolved_path.parents)
        return is_safe, resolved_path
    except Exception:
        return False, None


def load_json_artifact(path_str, root_dir, name):
    """
    Safely resolves, validates, and loads a JSON artifact within root_dir.
    Returns (data, error_message).
    """
    is_safe, resolved_path = check_path_safety(path_str, root_dir)
    if not is_safe:
        return None, f"Path safety violation: {name} path resolves outside repository root."
    
    if resolved_path is None or not resolved_path.is_file():
        return None, f"Missing file: {name} artifact does not exist."
    
    try:
        with open(resolved_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data, None
    except Exception as e:
        return None, f"Malformed JSON in {name} artifact: {str(e)}"


def print_explain():
    """
    Prints human-readable explanation of CLI role and non-authority boundaries.
    """
    explanation = """Execution Result Verification CLI - Explain Mode

This CLI evaluates whether the result of a controlled execution session satisfies the M59 verification policies.

Policy Rules Overview:
1. Upstream validation layers (preconditions, git diff and scope, validation evidence) are authoritative for safety classification.
2. The verification result/output (59.6) acts as a consistency signal.
3. Verification is not approval. Human review remains mandatory and cannot be bypassed.

Safety Boundaries & Non-Authority rules:
- M59 CLI does not approve task completion.
- M59 CLI does not create approval.
- M59 CLI does not authorize merge, push, or release.
- M59 CLI does not mutate lifecycle state.
- M59 CLI does not replace human review.
- M59 CLI only classifies execution result verification state for human review handoff.
"""
    print(explanation)


def main():
    parser = argparse.ArgumentParser(
        description="Execution Result Verification CLI Foundation",
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

    # If --help is called, argparse handles it without side effects.
    args = parser.parse_args()

    if args.explain:
        print_explain()
        sys.exit(0)

    # 1. Resolve root
    try:
        resolved_root = Path(args.root).resolve()
    except Exception as e:
        # Fail closed if root cannot be resolved
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

    blockers = []
    warnings = []
    not_verified_reasons = []

    # 2. Load artifacts
    input_data, input_err = load_json_artifact(args.input, resolved_root, "input")
    pre_data, pre_err = load_json_artifact(args.preconditions, resolved_root, "preconditions")
    diff_data, diff_err = load_json_artifact(args.diff_scope, resolved_root, "diff-scope")
    val_data, val_err = load_json_artifact(args.validation_evidence, resolved_root, "validation-evidence")
    res_data, res_err = load_json_artifact(args.result_output, resolved_root, "result-output")

    # Collect errors as blockers
    for err in [input_err, pre_err, diff_err, val_err, res_err]:
        if err:
            blockers.append(err)

    input_status = None
    preconditions_status = None
    diff_scope_status = None
    validation_evidence_status = None
    verification_result_status = None

    if not blockers:
        # Extract status fields
        input_status = input_data.get("input_status")
        preconditions_status = pre_data.get("preconditions_status")
        diff_scope_status = diff_data.get("diff_scope_status")
        validation_evidence_status = val_data.get("validation_evidence_status")
        verification_result_status = res_data.get("verification_result_status")

        # Basic validation checks
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

    # Determine decision using CLI foundation rules
    if blockers:
        result = EXECUTION_RESULT_BLOCKED
        policy_decision = M59_VERIFICATION_POLICY_BLOCKED
        exit_code = 2
        upstream_state = "UNKNOWN"
        output_state = "UNKNOWN"
    else:
        # Basic state classification
        # Upstream state
        upstream_blocked = (
            preconditions_status == "EXECUTION_RESULT_PRECONDITIONS_BLOCKED" or
            diff_scope_status == "SCOPE_VERIFICATION_BLOCKED" or
            validation_evidence_status == "VALIDATION_EVIDENCE_BLOCKED"
        )
        upstream_not_ready = (
            preconditions_status == "EXECUTION_RESULT_PRECONDITIONS_NOT_READY" or
            diff_scope_status == "SCOPE_VERIFICATION_NOT_READY" or
            validation_evidence_status == "VALIDATION_EVIDENCE_NOT_CONFIRMED"
        )
        upstream_warnings = (
            preconditions_status == "EXECUTION_RESULT_PRECONDITIONS_READY_WITH_WARNINGS" or
            diff_scope_status == "SCOPE_VERIFICATION_PASS_WITH_WARNINGS" or
            validation_evidence_status == "VALIDATION_EVIDENCE_CONFIRMED_WITH_WARNINGS"
        )

        if upstream_blocked:
            upstream_state = "BLOCKED"
        elif upstream_not_ready:
            upstream_state = "NOT_READY"
        elif upstream_warnings:
            upstream_state = "READY_WITH_WARNINGS"
        else:
            upstream_state = "READY"

        # Output state
        if verification_result_status == "EXECUTION_RESULT_BLOCKED":
            output_state = "BLOCKED"
        elif verification_result_status == "EXECUTION_RESULT_NOT_VERIFIED":
            output_state = "NOT_VERIFIED"
        elif verification_result_status == "EXECUTION_RESULT_VERIFIED_WITH_WARNINGS":
            output_state = "VERIFIED_WITH_WARNINGS"
        elif verification_result_status == "EXECUTION_RESULT_VERIFIED":
            output_state = "VERIFIED"
        else:
            output_state = "UNKNOWN"

        # Apply basic priority order mapping
        if upstream_state == "BLOCKED" or output_state == "BLOCKED":
            result = EXECUTION_RESULT_BLOCKED
            policy_decision = M59_VERIFICATION_POLICY_BLOCKED
            exit_code = 2
        elif upstream_state == "NOT_READY" or output_state == "NOT_VERIFIED":
            result = EXECUTION_RESULT_NOT_VERIFIED
            policy_decision = M59_VERIFICATION_POLICY_NOT_VERIFIED
            exit_code = 1
            if upstream_state == "NOT_READY":
                not_verified_reasons.append("Upstream verification layer is not ready.")
            if output_state == "NOT_VERIFIED":
                not_verified_reasons.append("Verification output indicates not verified.")
        elif upstream_state == "READY_WITH_WARNINGS" or output_state == "VERIFIED_WITH_WARNINGS":
            result = EXECUTION_RESULT_VERIFIED_WITH_WARNINGS
            policy_decision = M59_VERIFICATION_POLICY_VERIFIED_WITH_WARNINGS
            exit_code = 0
            warnings.append("Warnings present in verification layers.")
        else:
            result = EXECUTION_RESULT_VERIFIED
            policy_decision = M59_VERIFICATION_POLICY_VERIFIED
            exit_code = 0

    # Strict mode handling
    strict_upgrades_applied = 0
    if args.strict and result == EXECUTION_RESULT_VERIFIED_WITH_WARNINGS:
        result = EXECUTION_RESULT_BLOCKED
        policy_decision = M59_VERIFICATION_POLICY_BLOCKED
        exit_code = 2
        blockers.append("Strict mode: verification upgraded to blocked due to warnings.")
        strict_upgrades_applied = 1

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
        print(f"STRICT: {str(output['strict'])}")
        print(f"WARNINGS: {str(output['warnings'])}")
        print(f"BLOCKERS: {str(output['blockers'])}")
        print(f"NOT_VERIFIED_REASONS: {str(output['not_verified_reasons'])}")

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
