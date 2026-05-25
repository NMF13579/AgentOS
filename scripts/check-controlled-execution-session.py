#!/usr/bin/env python3
"""
M58 Controlled Execution Session CLI.
Classifies controlled execution session readiness.

M58 CLI does not open an execution session.
M58 CLI does not authorize task completion.
M58 CLI does not verify execution result.
M58 CLI does not create approval.
M58 CLI does not authorize merge, push, or release.
M58 CLI does not mutate lifecycle state.
M58 CLI only classifies controlled execution session readiness.
"""

import argparse
import json
import pathlib
import sys

# Exact non-authority statements for output
JSON_NON_AUTHORITY = [
    "M58 CLI does not open an execution session.",
    "M58 CLI does not authorize task completion.",
    "M58 CLI does not verify execution result.",
    "M58 CLI does not create approval.",
    "M58 CLI does not authorize merge, push, or release.",
    "M58 CLI does not mutate lifecycle state."
]

def emit_result(result, policy_decision, exit_code, blockers, warnings, inputs_dict, statuses_dict, json_mode, explain_mode, strict_mode):
    if json_mode:
        output = {
            "result": result,
            "policy_decision": policy_decision,
            "exit_code": exit_code,
            "warnings": warnings,
            "blockers": blockers,
            "inputs": {
                "request": inputs_dict.get("request") or "",
                "preconditions": inputs_dict.get("preconditions") or "",
                "boundary": inputs_dict.get("boundary") or "",
                "record": inputs_dict.get("record") or ""
            },
            "non_authority": JSON_NON_AUTHORITY
        }
        print(json.dumps(output, indent=2))
    else:
        print(f"RESULT: {result}")
        print(f"POLICY_DECISION: {policy_decision}")
        print(f"EXIT_CODE: {exit_code}")
        print(f"WARNINGS: {len(warnings)}")
        print(f"BLOCKERS: {len(blockers)}")
        print("\n--- Non-Authority Statements ---")
        for statement in JSON_NON_AUTHORITY:
            print(statement)
        print("M58 CLI only classifies controlled execution session readiness.")
        
        if explain_mode:
            print("\n--- Explanation ---")
            print(f"Classification Result: {result} ({policy_decision})")
            print("Why was this selected?")
            if blockers:
                print("- Blocker(s) were detected. According to priority rules, any blocker results in BLOCKED.")
                for b in blockers:
                    print(f"  * {b}")
            elif result == "CONTROLLED_EXECUTION_SESSION_NOT_READY":
                print("- Incomplete or draft status detected without safety hazards. Result is NOT_READY.")
            elif result == "CONTROLLED_EXECUTION_SESSION_READY_WITH_WARNINGS":
                print("- Valid structural configuration, but non-blocking warnings are present.")
                for w in warnings:
                    print(f"  * {w}")
            else:
                print("- All layer checks passed, no warnings or blockers present. Result is READY.")
                
            print("\nLayer statuses evaluated:")
            print(f"- Request layer status: {statuses_dict.get('request_status', 'UNKNOWN/MISSING')}")
            print(f"- Preconditions layer status: {statuses_dict.get('preconditions_status', 'UNKNOWN/MISSING')}")
            print(f"- Boundary layer status: {statuses_dict.get('boundary_status', 'UNKNOWN/MISSING')}")
            print(f"- Record/output layer status: {statuses_dict.get('record_status', 'UNKNOWN/MISSING')}")
            
            print("\nM59 Handoff Preservation:")
            print("- M59 handoff remains required and is preserved in all structures.")
            
            print("\nWhy this is not approval or verification:")
            print("- This result is structural classification only. It is not approval.")
            print("- This result is not result verification.")
            print("- M58 CLI does not authorize task completion and does not verify execution results.")

    sys.exit(exit_code)

def main():
    parser = argparse.ArgumentParser(
        description="M58 Controlled Execution Session CLI. "
                    "M58 CLI only classifies controlled execution session readiness."
    )
    parser.add_argument("--request", help="Path to request contract artifact")
    parser.add_argument("--preconditions", help="Path to preconditions result artifact")
    parser.add_argument("--boundary", help="Path to boundary result artifact")
    parser.add_argument("--record", help="Path to record/output artifact")
    parser.add_argument("--json", action="store_true", help="Emit output in JSON format")
    parser.add_argument("--explain", action="store_true", help="Explain the classification result")
    parser.add_argument("--strict", action="store_true", help="Enable strict mode checks")
    parser.add_argument("--root", help="Override the repository root directory")
    
    args = parser.parse_args()
    
    inputs_dict = {
        "request": args.request,
        "preconditions": args.preconditions,
        "boundary": args.boundary,
        "record": args.record
    }
    
    # 1. Root and path safety setup
    try:
        root_dir = pathlib.Path(args.root or ".").resolve()
    except Exception as e:
        emit_result("CONTROLLED_EXECUTION_SESSION_BLOCKED", "M58_SESSION_POLICY_BLOCKED", 2,
                    blockers=[f"Repository root path resolve failed: {str(e)}"],
                    warnings=[], inputs_dict=inputs_dict, statuses_dict={},
                    json_mode=args.json, explain_mode=args.explain, strict_mode=args.strict)
                    
    # Validate each path resolves inside the repository root
    resolved_paths = {}
    for name, path_str in inputs_dict.items():
        if not path_str:
            emit_result("CONTROLLED_EXECUTION_SESSION_BLOCKED", "M58_SESSION_POLICY_BLOCKED", 2,
                        blockers=[f"Missing required input argument: --{name}"],
                        warnings=[], inputs_dict=inputs_dict, statuses_dict={},
                        json_mode=args.json, explain_mode=args.explain, strict_mode=args.strict)
            
        p = pathlib.Path(path_str)
        try:
            resolved_p = p.resolve()
        except Exception as e:
            emit_result("CONTROLLED_EXECUTION_SESSION_BLOCKED", "M58_SESSION_POLICY_BLOCKED", 2,
                        blockers=[f"Unable to resolve path for {name}: {path_str}. Error: {str(e)}"],
                        warnings=[], inputs_dict=inputs_dict, statuses_dict={},
                        json_mode=args.json, explain_mode=args.explain, strict_mode=args.strict)
            
        try:
            resolved_p.relative_to(root_dir)
        except ValueError:
            emit_result("CONTROLLED_EXECUTION_SESSION_BLOCKED", "M58_SESSION_POLICY_BLOCKED", 2,
                        blockers=[f"Path safety violation: input path for {name} ({path_str}) resolves outside repository root ({root_dir})"],
                        warnings=[], inputs_dict=inputs_dict, statuses_dict={},
                        json_mode=args.json, explain_mode=args.explain, strict_mode=args.strict)
            
        if not resolved_p.exists():
            emit_result("CONTROLLED_EXECUTION_SESSION_BLOCKED", "M58_SESSION_POLICY_BLOCKED", 2,
                        blockers=[f"Input file does not exist for {name}: {path_str}"],
                        warnings=[], inputs_dict=inputs_dict, statuses_dict={},
                        json_mode=args.json, explain_mode=args.explain, strict_mode=args.strict)
            
        resolved_paths[name] = resolved_p

    # 2. Reading and parsing JSON artifacts
    parsed_data = {}
    for name, resolved_path in resolved_paths.items():
        try:
            content = resolved_path.read_text(encoding="utf-8")
        except Exception as e:
            emit_result("CONTROLLED_EXECUTION_SESSION_BLOCKED", "M58_SESSION_POLICY_BLOCKED", 2,
                        blockers=[f"Unable to read file for {name}: {str(e)}"],
                        warnings=[], inputs_dict=inputs_dict, statuses_dict={},
                        json_mode=args.json, explain_mode=args.explain, strict_mode=args.strict)
            
        try:
            data = json.loads(content)
            parsed_data[name] = (data, content)
        except Exception as e:
            emit_result("CONTROLLED_EXECUTION_SESSION_BLOCKED", "M58_SESSION_POLICY_BLOCKED", 2,
                        blockers=[f"Input file for {name} is malformed JSON: {str(e)}"],
                        warnings=[], inputs_dict=inputs_dict, statuses_dict={},
                        json_mode=args.json, explain_mode=args.explain, strict_mode=args.strict)

    blockers = []
    warnings = []
    
    req_data, req_content = parsed_data["request"]
    prec_data, prec_content = parsed_data["preconditions"]
    bound_data, bound_content = parsed_data["boundary"]
    rec_data, rec_content = parsed_data["record"]

    # 3. Consistency checks across artifacts
    task_ids = {}
    for name, data in [("request", req_data), ("preconditions", prec_data), ("boundary", bound_data), ("record", rec_data)]:
        t_id = data.get("task_id")
        if t_id:
            task_ids[name] = t_id
    if len(set(task_ids.values())) > 1:
        blockers.append(f"task_id consistency check failed: got {task_ids}")

    req_ids = {}
    for name, data in [("request", req_data), ("preconditions", prec_data), ("boundary", bound_data), ("record", rec_data)]:
        r_id = data.get("request_id")
        if r_id:
            req_ids[name] = r_id
    if len(set(req_ids.values())) > 1:
        blockers.append(f"request_id consistency check failed: got {req_ids}")

    prec_ids = {}
    for name, data in [("preconditions", prec_data), ("boundary", bound_data), ("record", rec_data)]:
        p_id = data.get("preconditions_id")
        if p_id:
            prec_ids[name] = p_id
    if len(set(prec_ids.values())) > 1:
        blockers.append(f"preconditions_id consistency check failed: got {prec_ids}")

    bound_ids = {}
    for name, data in [("boundary", bound_data), ("record", rec_data)]:
        b_id = data.get("boundary_id")
        if b_id:
            bound_ids[name] = b_id
    if len(set(bound_ids.values())) > 1:
        blockers.append(f"boundary_id consistency check failed: got {bound_ids}")

    # 4. Warnings and blockers aggregation
    for name, data in [("request", req_data), ("preconditions", prec_data), ("boundary", bound_data), ("record", rec_data)]:
        item_warnings = data.get("warnings")
        if isinstance(item_warnings, list):
            for w in item_warnings:
                warnings.append(f"[{name}] {w}")
        item_blockers = data.get("blockers")
        if isinstance(item_blockers, list):
            for b in item_blockers:
                blockers.append(f"[{name}] {b}")

    # 5. Unsafe claim detection via text scanning
    unsafe_phrases = [
        "task complete", "task is complete",
        "result verified", "result is verified",
        "task approved", "task is approved",
        "execution authorized", "execution is authorized",
        "m59 verification optional", "m59 is optional",
        "push allowed", "push is allowed",
        "merge allowed", "merge is allowed",
        "release allowed", "release is allowed",
        "lifecycle mutation allowed", "lifecycle state may be mutated"
    ]
    for name, content in [("request", req_content), ("preconditions", prec_content), ("boundary", bound_content), ("record", rec_content)]:
        content_lower = content.lower()
        for phrase in unsafe_phrases:
            if phrase in content_lower:
                blockers.append(f"Unsafe claim detected in {name}: '{phrase}'")

    # 6. Performed Actions check
    disallowed_actions = [
        "execution_session_started", "execution_session_opened", "execution_performed",
        "task_marked_done", "result_verified", "approval_record_created",
        "lifecycle_mutation_performed", "commit_created", "push_performed",
        "merge_performed", "m59_artifact_created"
    ]
    for name, data in [("request", req_data), ("preconditions", prec_data), ("record", rec_data)]:
        perf_actions = data.get("performed_actions")
        if isinstance(perf_actions, dict):
            for action in disallowed_actions:
                if perf_actions.get(action) is True:
                    blockers.append(f"Forbidden performed action in {name}: {action} is true")

    # 7. Forbidden Action check
    disallowed_forbidden = [
        "approval_creation", "lifecycle_mutation", "task_completion_claim",
        "result_verification_claim", "commit", "push", "merge", "release",
        "m59_artifact_creation", "protected_path_violation", "raw_dangerous_command"
    ]
    for name, data in [("request", req_data), ("preconditions", prec_data), ("boundary", bound_data), ("record", rec_data)]:
        for key in ["forbidden_actions", "forbidden_action_checks"]:
            forb = data.get(key)
            if isinstance(forb, dict):
                for f_act in disallowed_forbidden:
                    if forb.get(f_act) is True:
                        blockers.append(f"Forbidden action check failed in {name}: {f_act} is true")

    # 8. M59 Handoff check
    if "handoff_to_m59_required" not in req_data:
        blockers.append("handoff_to_m59_required is missing in request")
    elif req_data.get("handoff_to_m59_required") is not True:
        blockers.append("handoff_to_m59_required is not true in request")
        
    rec_handoff = rec_data.get("m59_handoff")
    if not rec_handoff:
        blockers.append("m59_handoff is missing in record")
    elif not isinstance(rec_handoff, dict):
        blockers.append("m59_handoff in record is invalid")
    else:
        if "handoff_required" not in rec_handoff:
            blockers.append("handoff_required is missing in m59_handoff")
        elif rec_handoff.get("handoff_required") is not True:
            blockers.append("handoff_required is not true in m59_handoff")

    # 9. Session close claim checks
    rec_close = rec_data.get("session_close")
    if isinstance(rec_close, dict):
        if rec_close.get("task_completion_claimed") is not False:
            blockers.append("task_completion_claimed is not false in session_close")
        if rec_close.get("result_verification_claimed") is not False:
            blockers.append("result_verification_claimed is not false in session_close")
        if rec_close.get("lifecycle_mutation_claimed") is not False:
            blockers.append("lifecycle_mutation_claimed is not false in session_close")

    # 10. Status interpretation
    req_status = req_data.get("request_status")
    prec_status = prec_data.get("preconditions_status")
    bound_status = bound_data.get("boundary_status")
    rec_status = rec_data.get("record_status")
    
    statuses_dict = {
        "request_status": req_status,
        "preconditions_status": prec_status,
        "boundary_status": bound_status,
        "record_status": rec_status
    }
    
    decisions = []
    
    if req_status == "EXECUTION_SESSION_REQUEST_READY_FOR_PRECONDITIONS":
        decisions.append("READY")
    elif req_status == "EXECUTION_SESSION_REQUEST_DRAFT":
        decisions.append("NOT_READY")
    else:
        decisions.append("BLOCKED")
        blockers.append(f"Request status is invalid: {req_status}")
        
    if prec_status == "EXECUTION_SESSION_PRECONDITIONS_READY":
        decisions.append("READY")
    elif prec_status == "EXECUTION_SESSION_PRECONDITIONS_READY_WITH_WARNINGS":
        decisions.append("READY_WITH_WARNINGS")
    elif prec_status == "EXECUTION_SESSION_PRECONDITIONS_NOT_READY":
        decisions.append("NOT_READY")
    else:
        decisions.append("BLOCKED")
        blockers.append(f"Preconditions status is invalid: {prec_status}")
        
    if bound_status == "EXECUTION_SESSION_BOUNDARY_SATISFIED":
        decisions.append("READY")
    elif bound_status == "EXECUTION_SESSION_BOUNDARY_SATISFIED_WITH_WARNINGS":
        decisions.append("READY_WITH_WARNINGS")
    elif bound_status == "EXECUTION_SESSION_BOUNDARY_NOT_SATISFIED":
        decisions.append("NOT_READY")
    else:
        decisions.append("BLOCKED")
        blockers.append(f"Boundary status is invalid: {bound_status}")
        
    if rec_status in ["EXECUTION_SESSION_RECORD_READY_FOR_POLICY", "EXECUTION_SESSION_RECORD_CLOSED_PENDING_M59_VERIFICATION"]:
        decisions.append("READY")
    elif rec_status == "EXECUTION_SESSION_RECORD_DRAFT":
        decisions.append("NOT_READY")
    else:
        decisions.append("BLOCKED")
        blockers.append(f"Record status is invalid: {rec_status}")

    # 11. Strict mode warning escalation
    if args.strict and warnings:
        blockers.append("Strict mode: warnings are elevated to blockers.")

    # 12. Combined result calculation
    if blockers or "BLOCKED" in decisions:
        result = "CONTROLLED_EXECUTION_SESSION_BLOCKED"
        policy_decision = "M58_SESSION_POLICY_BLOCKED"
        exit_code = 2
    elif "NOT_READY" in decisions:
        result = "CONTROLLED_EXECUTION_SESSION_NOT_READY"
        policy_decision = "M58_SESSION_POLICY_NOT_READY"
        exit_code = 1
    elif "READY_WITH_WARNINGS" in decisions or warnings:
        result = "CONTROLLED_EXECUTION_SESSION_READY_WITH_WARNINGS"
        policy_decision = "M58_SESSION_POLICY_READY_WITH_WARNINGS"
        exit_code = 0
    else:
        result = "CONTROLLED_EXECUTION_SESSION_READY"
        policy_decision = "M58_SESSION_POLICY_READY"
        exit_code = 0

    emit_result(result, policy_decision, exit_code, blockers, warnings, inputs_dict, statuses_dict,
                json_mode=args.json, explain_mode=args.explain, strict_mode=args.strict)

if __name__ == "__main__":
    main()
