#!/usr/bin/env python3
"""
check-commit-push-preconditions.py — M26 Commit / Push Precondition Checker

Read-only. Does not run git commit, git push, modify files, self-heal, or
approve anything. COMMIT_ALLOWED is not approval. PUSH_ALLOWED is not approval.
This checker does not override M25.
"""

import argparse
import json
import sys
from pathlib import Path

import yaml


RESULT_COMMIT_ALLOWED = "COMMIT_ALLOWED"
RESULT_PUSH_ALLOWED = "PUSH_ALLOWED"
RESULT_NEEDS_APPROVAL = "NEEDS_APPROVAL"
RESULT_BLOCKED = "BLOCKED"
RESULT_NEEDS_REVIEW = "NEEDS_REVIEW"

ALLOWED_OPERATIONS = {"COMMIT", "PUSH"}
ALLOWED_PERMISSIONS = {
    "COMMIT_REQUEST",
    "PUSH_REQUEST",
    "LOCAL_EDIT",
    "LOCAL_TEST",
    "READ_ONLY",
    "PATCH_PROPOSE",
    "BLOCKED",
}
ALLOWED_SCOPE_RESULTS = {
    "SCOPE_OK",
    "SCOPE_WARNING",
    "SCOPE_VIOLATION",
    "NEEDS_REVIEW",
    "NOT_RUN",
}
ALLOWED_M25_RESULTS = {
    "PASS",
    "WARN",
    "FAIL",
    "ERROR",
    "NOT_RUN",
    "INCOMPLETE",
}
ALLOWED_PUSH_DECISIONS = {
    "PUSH_APPROVED",
    "PUSH_APPROVED_WITH_CONDITIONS",
    "NEEDS_HUMAN_REVIEW",
    "PUSH_DENIED",
    "PUSH_BLOCKED",
    "NOT_REQUESTED",
}
ALLOWED_PUSH_TYPES = {
    "FEATURE_BRANCH_PUSH",
    "REMOTE_BRANCH_CREATE",
    "TAG_PUSH",
    "FORCE_PUSH",
    "PROTECTED_BRANCH_PUSH",
    "REMOTE_BRANCH_DELETE",
    "UNKNOWN",
}

DISCLAIMER = (
    "COMMIT_ALLOWED is not merge approval.\n"
    "COMMIT_ALLOWED does not authorize push.\n"
    "PUSH_ALLOWED is not merge approval.\n"
    "PUSH_ALLOWED is not release approval.\n"
    "PUSH_ALLOWED does not bypass M25.\n"
    "PASS is not approval.\n"
    "Scope checker result is not approval.\n"
    "Push request record alone is not approval.\n"
    "This checker is read-only and does not execute commit or push.\n"
    "This checker does not modify files.\n"
    "This checker does not self-heal."
)


def read_yaml_request(path_text: str):
    path = Path(path_text)
    if not path.exists() or not path.is_file():
        return None, [{
            "code": "REQUEST_FILE_MISSING",
            "detail": f"Request file not found: {path_text}",
        }]

    try:
        with path.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
    except yaml.YAMLError as exc:
        return None, [{
            "code": "INVALID_YAML",
            "detail": f"Invalid YAML in request file: {exc}",
        }]

    if not isinstance(data, dict):
        return None, [{
            "code": "INVALID_YAML",
            "detail": "Request file must be a YAML mapping.",
        }]

    return data, []


def get_path(data, path):
    node = data
    for part in path:
        if not isinstance(node, dict) or part not in node:
            return False, None
        node = node[part]
    return True, node


def path_label(path):
    return ".".join(path)


def add_reason(bucket, code, detail):
    bucket.append({"code": code, "detail": detail})


def normalize_text(value):
    if isinstance(value, str):
        text = value.strip()
        return text if text else None
    return None


def normalize_yes_no(value):
    if isinstance(value, bool):
        return "yes" if value else "no"
    if isinstance(value, str):
        text = value.strip().lower()
        if text in {"yes", "no"}:
            return text
    return None


def is_none_marker(value):
    return isinstance(value, str) and value.strip().upper() == "NONE"


def require_text(data, path, review_reasons, allow_none_marker=False):
    exists, value = get_path(data, path)
    if not exists or value is None:
        add_reason(review_reasons, "MISSING_FIELD", f"Missing required field: {path_label(path)}")
        return None

    text = normalize_text(value)
    if text is None:
        add_reason(review_reasons, "INVALID_VALUE", f"{path_label(path)} must be a non-empty string.")
        return None

    if allow_none_marker and text.upper() == "NONE":
        return "NONE"

    return text


def require_enum(data, path, allowed_values, review_reasons):
    text = require_text(data, path, review_reasons)
    if text is None:
        return None

    if text not in allowed_values:
        add_reason(
            review_reasons,
            "INVALID_VALUE",
            f"{path_label(path)} must be one of {sorted(allowed_values)}.",
        )
        return None

    return text


def require_yes_no(data, path, review_reasons):
    exists, value = get_path(data, path)
    if not exists or value is None:
        add_reason(review_reasons, "MISSING_FIELD", f"Missing required field: {path_label(path)}")
        return None

    normalized = normalize_yes_no(value)
    if normalized is None:
        add_reason(review_reasons, "INVALID_VALUE", f"{path_label(path)} must be yes or no.")
        return None

    return normalized


def require_list_of_text(data, path, review_reasons):
    exists, value = get_path(data, path)
    if not exists or value is None:
        add_reason(review_reasons, "MISSING_FIELD", f"Missing required field: {path_label(path)}")
        return None

    if not isinstance(value, list):
        add_reason(review_reasons, "INVALID_VALUE", f"{path_label(path)} must be a list.")
        return None

    if not value:
        add_reason(review_reasons, "INVALID_VALUE", f"{path_label(path)} must not be empty.")
        return None

    normalized = []
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            add_reason(
                review_reasons,
                "INVALID_VALUE",
                f"{path_label(path)}[{index}] must be a non-empty string.",
            )
            return None
        normalized.append(item.strip())

    return normalized


def require_commit_message(data, review_reasons):
    exists, value = get_path(data, ["commit", "commit_message"])
    if not exists or value is None:
        add_reason(review_reasons, "MISSING_FIELD", "Missing required field: commit.commit_message")
        return None, "missing"

    if not isinstance(value, str):
        add_reason(review_reasons, "INVALID_VALUE", "commit.commit_message must be a string.")
        return None, "invalid"

    text = value.strip()
    if not text:
        return "", "empty"

    return text, "ok"


def require_mapping(data, path, review_reasons):
    exists, value = get_path(data, path)
    if not exists or value is None:
        add_reason(review_reasons, "MISSING_FIELD", f"Missing required field: {path_label(path)}")
        return None

    if not isinstance(value, dict):
        add_reason(review_reasons, "INVALID_VALUE", f"{path_label(path)} must be a mapping.")
        return None

    return value


def validate_common_fields(data, review_reasons):
    task_id = require_text(data, ["task_id"], review_reasons)
    operation = require_enum(data, ["operation"], ALLOWED_OPERATIONS, review_reasons)
    active_task = require_yes_no(data, ["active_task"], review_reasons)
    permission_current = require_enum(data, ["permission", "current"], ALLOWED_PERMISSIONS, review_reasons)
    scope_result = require_enum(data, ["scope_check", "result"], ALLOWED_SCOPE_RESULTS, review_reasons)
    scope_warning_resolved = require_yes_no(
        data, ["scope_check", "warning_conditions_resolved"], review_reasons
    )
    m25_result = require_enum(data, ["m25_validation", "result"], ALLOWED_M25_RESULTS, review_reasons)
    m25_override_record = require_text(
        data, ["m25_validation", "override_record"], review_reasons, allow_none_marker=True
    )
    m25_override_valid = require_yes_no(data, ["m25_validation", "override_valid"], review_reasons)
    forbidden_files_changed = require_yes_no(data, ["commit", "forbidden_files_changed"], review_reasons)
    evidence_tampering = require_yes_no(data, ["commit", "evidence_tampering_detected"], review_reasons)
    workflow_files_changed = require_yes_no(data, ["commit", "workflow_files_changed"], review_reasons)
    scripts_changed = require_yes_no(data, ["commit", "scripts_changed"], review_reasons)
    tests_changed = require_yes_no(data, ["commit", "tests_changed"], review_reasons)
    violations_open = require_yes_no(data, ["violations", "open"], review_reasons)

    return {
        "task_id": task_id,
        "operation": operation,
        "active_task": active_task,
        "permission_current": permission_current,
        "scope_result": scope_result,
        "scope_warning_resolved": scope_warning_resolved,
        "m25_result": m25_result,
        "m25_override_record": m25_override_record,
        "m25_override_valid": m25_override_valid,
        "forbidden_files_changed": forbidden_files_changed,
        "evidence_tampering": evidence_tampering,
        "workflow_files_changed": workflow_files_changed,
        "scripts_changed": scripts_changed,
        "tests_changed": tests_changed,
        "violations_open": violations_open,
    }


def validate_commit_fields(data, review_reasons):
    protected_change_approval = require_mapping(data, ["protected_change_approval"], review_reasons)
    if protected_change_approval is None:
        return None

    scripts_approved = require_yes_no(
        data, ["protected_change_approval", "scripts_approved"], review_reasons
    )
    tests_approved = require_yes_no(
        data, ["protected_change_approval", "tests_approved"], review_reasons
    )
    approval_record = require_text(
        data, ["protected_change_approval", "approval_record"], review_reasons, allow_none_marker=True
    )
    commit_message, commit_message_state = require_commit_message(data, review_reasons)
    changed_files = require_list_of_text(data, ["commit", "changed_files"], review_reasons)

    return {
        "scripts_approved": scripts_approved,
        "tests_approved": tests_approved,
        "approval_record": approval_record,
        "commit_message": commit_message,
        "commit_message_state": commit_message_state,
        "changed_files": changed_files,
    }


def validate_push_fields(data, review_reasons):
    push_request_record = require_text(
        data, ["push", "push_request_record"], review_reasons, allow_none_marker=True
    )
    push_decision = require_enum(data, ["push", "push_decision"], ALLOWED_PUSH_DECISIONS, review_reasons)
    protected_branch_target = require_yes_no(data, ["push", "protected_branch_target"], review_reasons)
    target_branch = require_text(data, ["push", "target_branch"], review_reasons)
    target_remote = require_text(data, ["push", "target_remote"], review_reasons)
    push_type = require_enum(data, ["push", "push_type"], ALLOWED_PUSH_TYPES, review_reasons)
    approval_expired = require_yes_no(data, ["push", "approval_expired"], review_reasons)

    tag_push_authorized = None
    if push_type == "TAG_PUSH":
        tag_push_authorized = require_yes_no(data, ["push", "tag_push_authorized"], review_reasons)

    return {
        "push_request_record": push_request_record,
        "push_decision": push_decision,
        "protected_branch_target": protected_branch_target,
        "target_branch": target_branch,
        "target_remote": target_remote,
        "push_type": push_type,
        "approval_expired": approval_expired,
        "tag_push_authorized": tag_push_authorized,
    }


def m25_has_valid_override(context):
    override_record = context["m25_override_record"]
    override_valid = context["m25_override_valid"]
    return override_record != "NONE" and override_valid == "yes"


def evaluate_commit(context, commit_context):
    blocking = []
    approval = []

    if context["active_task"] == "no":
        add_reason(blocking, "INACTIVE_TASK", "active_task is no.")
    if context["permission_current"] == "BLOCKED":
        add_reason(blocking, "BLOCKED_PERMISSION", "permission.current is BLOCKED.")
    if context["scope_result"] in {"SCOPE_VIOLATION", "NEEDS_REVIEW", "NOT_RUN"}:
        add_reason(blocking, "SCOPE_BLOCK", f"scope_check.result is {context['scope_result']}.")
    if context["m25_result"] in {"FAIL", "WARN", "ERROR", "NOT_RUN", "INCOMPLETE"} and not m25_has_valid_override(context):
        add_reason(
            blocking,
            "M25_BLOCK",
            f"m25_validation.result is {context['m25_result']} without a valid override.",
        )
    if context["forbidden_files_changed"] == "yes":
        add_reason(blocking, "FORBIDDEN_FILES_CHANGED", "forbidden_files_changed is yes.")
    if context["evidence_tampering"] == "yes":
        add_reason(blocking, "EVIDENCE_TAMPERING", "evidence_tampering_detected is yes.")
    if context["workflow_files_changed"] == "yes":
        add_reason(blocking, "WORKFLOW_FILES_CHANGED", "workflow_files_changed is yes.")
    if context["violations_open"] == "yes":
        add_reason(blocking, "OPEN_VIOLATIONS", "violations.open is yes.")

    commit_message = commit_context["commit_message"]
    if commit_message is None:
        add_reason(blocking, "MISSING_COMMIT_MESSAGE", "commit.commit_message is missing or empty.")
    elif context["task_id"] not in commit_message:
        add_reason(
            blocking,
            "TASK_ID_MISSING_FROM_MESSAGE",
            "commit.commit_message does not contain task_id as a case-sensitive substring.",
        )

    if blocking:
        return blocking, approval

    if commit_context["commit_message_state"] == "empty":
        add_reason(blocking, "EMPTY_COMMIT_MESSAGE", "commit.commit_message is empty.")

    if blocking:
        return blocking, approval

    if context["permission_current"] != "COMMIT_REQUEST":
        add_reason(
            approval,
            "PERMISSION_NOT_COMMIT_REQUEST",
            f"permission.current is {context['permission_current']}, not COMMIT_REQUEST.",
        )
    if context["scope_result"] == "SCOPE_WARNING" and context["scope_warning_resolved"] == "no":
        add_reason(
            approval,
            "SCOPE_WARNING_UNRESOLVED",
            "scope_check.result is SCOPE_WARNING and warning_conditions_resolved is no.",
        )
    if context["scripts_changed"] == "yes" and commit_context["scripts_approved"] == "no":
        add_reason(
            approval,
            "SCRIPTS_NEED_APPROVAL",
            "scripts_changed is yes and protected_change_approval.scripts_approved is no.",
        )
    if context["tests_changed"] == "yes" and commit_context["tests_approved"] == "no":
        add_reason(
            approval,
            "TESTS_NEED_APPROVAL",
            "tests_changed is yes and protected_change_approval.tests_approved is no.",
        )

    if approval:
        return blocking, approval

    return blocking, approval


def evaluate_push(context, push_context):
    blocking = []
    approval = []

    branch = push_context["target_branch"].strip().lower()

    if context["active_task"] == "no":
        add_reason(blocking, "INACTIVE_TASK", "active_task is no.")
    if context["permission_current"] == "BLOCKED":
        add_reason(blocking, "BLOCKED_PERMISSION", "permission.current is BLOCKED.")
    if context["scope_result"] in {"SCOPE_VIOLATION", "NEEDS_REVIEW", "NOT_RUN"}:
        add_reason(blocking, "SCOPE_BLOCK", f"scope_check.result is {context['scope_result']}.")
    if context["m25_result"] in {"FAIL", "WARN", "ERROR", "NOT_RUN", "INCOMPLETE"} and not m25_has_valid_override(context):
        add_reason(
            blocking,
            "M25_BLOCK",
            f"m25_validation.result is {context['m25_result']} without a valid override.",
        )
    if push_context["push_decision"] in {"PUSH_DENIED", "PUSH_BLOCKED"}:
        add_reason(
            blocking,
            "PUSH_DECISION_BLOCK",
            f"push.push_decision is {push_context['push_decision']}.",
        )
    if push_context["protected_branch_target"] == "yes" or branch in {"dev", "main"}:
        add_reason(
            blocking,
            "PROTECTED_BRANCH_TARGET",
            "Protected branch target or direct push to dev/main is blocked.",
        )
    if push_context["push_type"] in {"PROTECTED_BRANCH_PUSH", "FORCE_PUSH", "REMOTE_BRANCH_DELETE"}:
        add_reason(
            blocking,
            "BLOCKED_PUSH_TYPE",
            f"push.push_type is {push_context['push_type']}.",
        )
    if push_context["approval_expired"] == "yes":
        add_reason(blocking, "APPROVAL_EXPIRED", "approval_expired is yes.")
    if context["violations_open"] == "yes":
        add_reason(blocking, "OPEN_VIOLATIONS", "violations.open is yes.")
    if context["evidence_tampering"] == "yes":
        add_reason(blocking, "EVIDENCE_TAMPERING", "evidence_tampering_detected is yes.")
    if context["forbidden_files_changed"] == "yes":
        add_reason(blocking, "FORBIDDEN_FILES_CHANGED", "forbidden_files_changed is yes.")
    if context["workflow_files_changed"] == "yes":
        add_reason(blocking, "WORKFLOW_FILES_CHANGED", "workflow_files_changed is yes.")

    if blocking:
        return blocking, approval

    if context["permission_current"] != "PUSH_REQUEST":
        add_reason(
            approval,
            "PERMISSION_NOT_PUSH_REQUEST",
            f"permission.current is {context['permission_current']}, not PUSH_REQUEST.",
        )
    if push_context["push_request_record"] == "NONE":
        add_reason(approval, "MISSING_PUSH_REQUEST_RECORD", "push.push_request_record is NONE.")
    if push_context["push_decision"] in {"NOT_REQUESTED", "NEEDS_HUMAN_REVIEW"}:
        add_reason(
            approval,
            "PUSH_DECISION_NEEDS_APPROVAL",
            f"push.push_decision is {push_context['push_decision']}.",
        )
    if context["scope_result"] == "SCOPE_WARNING" and context["scope_warning_resolved"] == "no":
        add_reason(
            approval,
            "SCOPE_WARNING_UNRESOLVED",
            "scope_check.result is SCOPE_WARNING and warning_conditions_resolved is no.",
        )
    if push_context["push_type"] == "UNKNOWN":
        add_reason(approval, "UNKNOWN_PUSH_TYPE", "push.push_type is UNKNOWN.")
    if push_context["push_type"] == "TAG_PUSH" and push_context["tag_push_authorized"] == "no":
        add_reason(
            approval,
            "TAG_PUSH_NOT_AUTHORIZED",
            "push.push_type is TAG_PUSH and tag_push_authorized is no.",
        )

    return blocking, approval


def build_report(operation, result, reasons, blocking, approval, review):
    return {
        "result": result,
        "operation": operation,
        "reasons": reasons,
        "blocking_reasons": blocking,
        "approval_reasons": approval,
        "review_reasons": review,
        "disclaimer": DISCLAIMER,
    }


def format_human(report):
    lines = [
        f"Result: {report['result']}",
        f"Operation: {report['operation']}",
        "",
    ]

    for title, key in [
        ("Reasons", "reasons"),
        ("Blocking reasons", "blocking_reasons"),
        ("Approval reasons", "approval_reasons"),
        ("Review reasons", "review_reasons"),
    ]:
        items = report[key]
        if not items:
            continue
        lines.append(f"{title} ({len(items)}):")
        for item in items:
            lines.append(f"  - [{item['code']}] {item['detail']}")
        lines.append("")

    lines.append("Disclaimer:")
    for line in report["disclaimer"].splitlines():
        lines.append(f"  {line}")

    return "\n".join(lines)


def format_json(report):
    return json.dumps(report, indent=2)


EXIT_CODES = {
    RESULT_COMMIT_ALLOWED: 0,
    RESULT_PUSH_ALLOWED: 0,
    RESULT_NEEDS_APPROVAL: 1,
    RESULT_BLOCKED: 2,
    RESULT_NEEDS_REVIEW: 3,
}


def evaluate_request(data):
    review_reasons = []
    common = validate_common_fields(data, review_reasons)

    operation = common["operation"] if common["operation"] in ALLOWED_OPERATIONS else "UNKNOWN"
    if common["task_id"] is None:
        # task_id is required for meaningful evaluation, but missing/invalid has already
        # been recorded as a review reason.
        pass

    if review_reasons:
        return build_report(
            operation="UNKNOWN" if operation == "UNKNOWN" else operation,
            result=RESULT_NEEDS_REVIEW,
            reasons=review_reasons,
            blocking=[],
            approval=[],
            review=review_reasons,
        )

    if operation == "COMMIT":
        commit_context = validate_commit_fields(data, review_reasons)
        if review_reasons:
            return build_report(
                operation=operation,
                result=RESULT_NEEDS_REVIEW,
                reasons=review_reasons,
                blocking=[],
                approval=[],
                review=review_reasons,
            )

        blocking, approval = evaluate_commit(common, commit_context)
        if blocking:
            return build_report(operation, RESULT_BLOCKED, blocking, blocking, approval, [])
        if approval:
            return build_report(operation, RESULT_NEEDS_APPROVAL, approval, blocking, approval, [])
        return build_report(operation, RESULT_COMMIT_ALLOWED, [], blocking, approval, [])

    if operation == "PUSH":
        push_context = validate_push_fields(data, review_reasons)
        if review_reasons:
            return build_report(
                operation=operation,
                result=RESULT_NEEDS_REVIEW,
                reasons=review_reasons,
                blocking=[],
                approval=[],
                review=review_reasons,
            )

        blocking, approval = evaluate_push(common, push_context)
        if blocking:
            return build_report(operation, RESULT_BLOCKED, blocking, blocking, approval, [])
        if approval:
            # TAG_PUSH without authorization or a missing push request record may still
            # be approvable, so return NEEDS_APPROVAL.
            return build_report(operation, RESULT_NEEDS_APPROVAL, approval, blocking, approval, [])
        return build_report(operation, RESULT_PUSH_ALLOWED, [], blocking, approval, [])

    add_reason(review_reasons, "UNKNOWN_OPERATION", "operation must be COMMIT or PUSH.")
    return build_report(
        operation="UNKNOWN",
        result=RESULT_NEEDS_REVIEW,
        reasons=review_reasons,
        blocking=[],
        approval=[],
        review=review_reasons,
    )


def main():
    parser = argparse.ArgumentParser(
        description="M26 Commit / Push Precondition Checker. Read-only."
    )
    parser.add_argument("--request-file", required=True, help="Path to YAML request file.")
    parser.add_argument("--json", action="store_true", dest="output_json", help="Output JSON.")

    args = parser.parse_args()

    request_data, request_errors = read_yaml_request(args.request_file)
    if request_errors:
        report = build_report(
            operation="UNKNOWN",
            result=RESULT_NEEDS_REVIEW,
            reasons=request_errors,
            blocking=[],
            approval=[],
            review=request_errors,
        )
        print(format_json(report) if args.output_json else format_human(report))
        sys.exit(EXIT_CODES[RESULT_NEEDS_REVIEW])

    report = evaluate_request(request_data)
    print(format_json(report) if args.output_json else format_human(report))
    sys.exit(EXIT_CODES.get(report["result"], 3))


if __name__ == "__main__":
    main()
