#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

TASK_LINT_PASS = "TASK_LINT_PASS"
TASK_LINT_WARNING = "TASK_LINT_WARNING"
TASK_LINT_NEEDS_REVIEW = "TASK_LINT_NEEDS_REVIEW"
TASK_LINT_FAIL = "TASK_LINT_FAIL"
TASK_LINT_FAILED = "TASK_LINT_FAILED"

TASK_REQUIRED_FIELDS = [
    "contract_version",
    "task_id",
    "source_spec",
    "source_ux",
    "source_ui_contract",
    "goal",
    "expected_result",
    "in_scope",
    "out_of_scope",
    "affected_paths",
    "forbidden_paths",
    "dependencies",
    "blocked_by",
    "priority",
    "risk_level",
    "risk_reason",
    "acceptance_criteria",
    "validation_plan",
    "rollback_plan",
    "human_approval_required",
    "owner_review_required",
    "context_required",
    "created_at",
]

QUEUE_REQUIRED_FIELDS = [
    "queue_entry_version",
    "queue_entry_id",
    "task_id",
    "source_task_contract",
    "source_dependency_map",
    "queue_status",
    "queue_reason",
    "dependency_status",
    "lint_status",
    "context_status",
    "ui_contract_status",
    "approval_status",
    "owner_review_status",
    "depends_on",
    "blocked_by",
    "priority",
    "risk_level",
    "human_approval_required",
    "owner_review_required",
    "created_at",
    "non_approval_warning",
]

FORBIDDEN_EXEC_FIELDS = {
    "execution_approved",
    "execution_authorized",
    "ready_for_execution",
    "push_allowed",
    "merge_allowed",
    "deploy_allowed",
    "release_allowed",
    "approval_granted",
}

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
HEX_COLOR_RE = re.compile(r"#[A-Fa-f0-9]{6}\b")
PX_RE = re.compile(r"\b\d+px\b")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Read-only Task/Queue Linter MVP")
    p.add_argument("--target", required=True)
    p.add_argument("--kind", required=True, choices=["task", "queue", "auto"])
    p.add_argument("--json", action="store_true", dest="json_mode")
    return p.parse_args()


def add_issue(issues: list[dict[str, str]], code: str, severity: str, message: str, field: str, rule: str) -> None:
    issues.append(
        {
            "code": code,
            "severity": severity,
            "message": message,
            "field": field,
            "rule": rule,
        }
    )


def severity_rank(sev: str) -> int:
    return {"failed": 4, "fail": 3, "needs_review": 2, "warning": 1}.get(sev, 0)


def issues_to_result(issues: list[dict[str, str]]) -> str:
    if not issues:
        return TASK_LINT_PASS
    highest = max(issues, key=lambda i: severity_rank(i["severity"]))["severity"]
    if highest == "failed":
        return TASK_LINT_FAILED
    if highest == "fail":
        return TASK_LINT_FAIL
    if highest == "needs_review":
        return TASK_LINT_NEEDS_REVIEW
    return TASK_LINT_WARNING


def output(result: str, target: Path, kind: str, issues: list[dict[str, str]], json_mode: bool) -> int:
    highest = "none"
    if issues:
        highest = max(issues, key=lambda i: severity_rank(i["severity"]))["severity"]

    if json_mode:
        payload = {
            "result": result,
            "target": str(target),
            "kind": kind,
            "issues": issues,
            "issue_count": len(issues),
            "highest_severity": highest,
            "non_approval_warning": "Lint PASS is not approval and does not authorize execution.",
        }
        print(json.dumps(payload, ensure_ascii=False))
    else:
        print(f"Result: {result}")
        print(f"Target: {target}")
        print(f"Kind: {kind}")
        print(f"Issue count: {len(issues)}")
        for i in issues:
            print(f"- {i['severity']} {i['code']} field={i['field']} :: {i['message']}")
        print("Lint PASS is not approval and does not authorize execution.")

    if result == TASK_LINT_PASS:
        return 0
    if result == TASK_LINT_FAILED:
        return 2
    return 1


def parse_bool(v: Any) -> bool | None:
    if isinstance(v, bool):
        return v
    if isinstance(v, str):
        s = v.strip().lower()
        if s == "true":
            return True
        if s == "false":
            return False
    return None


def parse_frontmatter_md(path: Path) -> tuple[dict[str, Any], str, str | None]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, "", "missing_frontmatter_start"

    end_idx = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end_idx = idx
            break
    if end_idx is None:
        return {}, "", "missing_frontmatter_end"

    fm_lines = lines[1:end_idx]
    body = "\n".join(lines[end_idx + 1 :])
    data: dict[str, Any] = {}
    i = 0
    while i < len(fm_lines):
        line = fm_lines[i]
        if not line.strip():
            i += 1
            continue
        if ":" not in line:
            i += 1
            continue
        key, raw = line.split(":", 1)
        key = key.strip()
        val = raw.strip()

        if val == "[]":
            data[key] = []
            i += 1
            continue

        if val:
            if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                val = val[1:-1]
            data[key] = val
            i += 1
            continue

        items: list[str] = []
        j = i + 1
        while j < len(fm_lines):
            s = fm_lines[j].strip()
            if not s:
                j += 1
                continue
            if s.startswith("- "):
                items.append(s[2:].strip())
                j += 1
                continue
            break
        data[key] = items if items else ""
        i = j

    return data, body, None


def ensure_list_str(v: Any) -> list[str] | None:
    if isinstance(v, list):
        out: list[str] = []
        for x in v:
            if not isinstance(x, str):
                return None
            out.append(x)
        return out
    return None


def normalize_ascii_task_id(task_id: str) -> str:
    lowered = task_id.lower()
    chunks: list[str] = []
    for ch in lowered:
        if ch.isascii() and ch.isalnum():
            chunks.append(ch)
        else:
            chunks.append("_")
    s = "".join(chunks)
    s = re.sub(r"_+", "_", s).strip("_")
    return s


def detect_ui_task(frontmatter: dict[str, Any], body: str) -> bool:
    tc = str(frontmatter.get("task_category", "")).strip()
    src_ui = str(frontmatter.get("source_ui_contract", "")).strip()
    req = parse_bool(frontmatter.get("ui_contract_required"))
    checks = [
        tc == "app_feature_ui",
        tc == "agentos_control_ui",
        tc.startswith("ui_"),
        bool(src_ui and src_ui != "TODO"),
        req is True,
        "UI Contract Boundary" in body,
    ]
    return any(checks)


def check_task(path: Path, issues: list[dict[str, str]]) -> None:
    # 1-2 parse
    front, body, err = parse_frontmatter_md(path)
    if err:
        add_issue(issues, "TASK_LINT_FRONTMATTER_MALFORMED", "fail", err, "frontmatter", "Malformed frontmatter must fail closed")
        return

    # 3-4 schema path resolution
    script_path = Path(__file__).resolve()
    repo_root = script_path.parent.parent
    schema_path = repo_root / "schemas/task-contract-v2.schema.json"
    if not schema_path.exists():
        add_issue(issues, "TASK_LINT_SCHEMA_MISSING", "failed", "task-contract-v2 schema missing", "schema", "Schema path resolution")
        return

    # 5 schema alignment required list only
    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        schema_required = schema.get("required", [])
        if not isinstance(schema_required, list):
            raise ValueError("required not list")
        if set(schema_required) != set(TASK_REQUIRED_FIELDS):
            add_issue(
                issues,
                "TASK_LINT_SCHEMA_MISMATCH_DETECTED",
                "failed",
                "required field list mismatch between linter and schema",
                "schema.required",
                "Schema alignment mismatch is intentionally blocking",
            )
            return
    except Exception as e:
        add_issue(issues, "TASK_LINT_SCHEMA_MISSING", "failed", f"schema read/parse failure: {e}", "schema", "Schema path resolution")
        return

    # 6 forbidden execution fields frontmatter keys only
    for k in front.keys():
        if k in FORBIDDEN_EXEC_FIELDS:
            add_issue(issues, "TASK_LINT_FORBIDDEN_EXECUTION_AUTHORITY_FIELD", "fail", f"forbidden key: {k}", k, "Forbidden execution-authority fields")

    # 7 required fields
    for k in TASK_REQUIRED_FIELDS:
        if k not in front:
            add_issue(issues, "TASK_LINT_MISSING_REQUIRED_FIELD", "fail", f"missing required field {k}", k, "Task Contract Required Fields")

    if any(i["severity"] == "fail" and i["code"] == "TASK_LINT_MISSING_REQUIRED_FIELD" for i in issues):
        return

    # 8 types/enums
    if str(front.get("contract_version", "")).strip() != "2":
        add_issue(issues, "TASK_LINT_INVALID_FIELD", "fail", "contract_version must be 2", "contract_version", "Task Contract Required Fields")

    if str(front.get("priority", "")).strip() not in {"high", "normal", "low"}:
        add_issue(issues, "TASK_LINT_INVALID_FIELD", "fail", "invalid priority", "priority", "Task Contract Required Fields")

    risk_level = str(front.get("risk_level", "")).strip()
    if risk_level not in {"LOW", "MEDIUM", "HIGH", "CRITICAL"}:
        add_issue(issues, "TASK_LINT_INVALID_FIELD", "fail", "invalid risk_level", "risk_level", "Task Contract Required Fields")

    for b in ["human_approval_required", "owner_review_required", "context_required"]:
        if parse_bool(front.get(b)) is None:
            add_issue(issues, "TASK_LINT_INVALID_FIELD", "fail", f"{b} must be boolean", b, "Task Contract Required Fields")

    list_fields = [
        "in_scope",
        "out_of_scope",
        "affected_paths",
        "forbidden_paths",
        "dependencies",
        "blocked_by",
        "acceptance_criteria",
        "validation_plan",
    ]
    for lf in list_fields:
        if ensure_list_str(front.get(lf)) is None:
            add_issue(issues, "TASK_LINT_INVALID_FIELD", "fail", f"{lf} must be list", lf, "Task Contract Required Fields")

    # 9 created_at
    created_at = str(front.get("created_at", "")).strip()
    if not DATE_RE.match(created_at):
        add_issue(issues, "TASK_LINT_INVALID_CREATED_AT", "fail", "invalid created_at format", "created_at", "Task Contract Required Fields")

    # 10 rollback TODO rule after risk check
    if risk_level in {"MEDIUM", "HIGH", "CRITICAL"}:
        rp = str(front.get("rollback_plan", "")).strip()
        if rp == "TODO":
            add_issue(issues, "TASK_LINT_TODO_NEEDS_REVIEW", "needs_review", "rollback_plan TODO for MEDIUM/HIGH/CRITICAL", "rollback_plan", "Task Contract Needs Review Rules")

    # 11-12 UI detection and rules
    is_ui = detect_ui_task(front, body)
    if is_ui:
        src_ui = str(front.get("source_ui_contract", "")).strip()
        if not src_ui or src_ui == "TODO":
            add_issue(issues, "TASK_LINT_UI_MISSING_CONTRACT", "fail", "UI task missing source_ui_contract", "source_ui_contract", "UI Task Lint Rules")

        req = parse_bool(front.get("ui_contract_required"))
        present = parse_bool(front.get("ui_contract_present"))
        if req is True and present is not True:
            add_issue(
                issues,
                "TASK_LINT_UI_MISSING_CONTRACT",
                "fail",
                "ui_contract_required is true and ui_contract_present is absent or false",
                "ui_contract_present",
                "UI Task Lint Rules",
            )

        if "components/ui/" in body:
            add_issue(issues, "TASK_LINT_UI_RAW_IMPORT", "fail", "raw components/ui import found in body", "body", "UI Task Lint Rules")
        if "@radix-ui/" in body:
            add_issue(issues, "TASK_LINT_UI_DIRECT_LIBRARY_IMPORT", "fail", "direct @radix-ui import found in body", "body", "UI Task Lint Rules")
        if HEX_COLOR_RE.search(body) or PX_RE.search(body) or "hardcoded" in body.lower():
            add_issue(issues, "TASK_LINT_UI_HARDCODED_VISUAL_STYLE", "fail", "hardcoded visual style pattern found", "body", "UI Task Lint Rules")
        if "new design token without review" in body.lower():
            add_issue(issues, "TASK_LINT_UI_SILENT_TOKEN_EXPANSION", "fail", "silent token expansion pattern found", "body", "UI Task Lint Rules")

    # 13 TODO readiness placeholders
    def is_todo_scalar(k: str) -> bool:
        return str(front.get(k, "")).strip() == "TODO"

    if is_todo_scalar("source_spec"):
        add_issue(issues, "TASK_LINT_TODO_NEEDS_REVIEW", "needs_review", "source_spec TODO", "source_spec", "Task Contract Needs Review Rules")
    if is_todo_scalar("source_ux"):
        add_issue(issues, "TASK_LINT_TODO_NEEDS_REVIEW", "needs_review", "source_ux TODO", "source_ux", "Task Contract Needs Review Rules")
    if is_ui and is_todo_scalar("source_ui_contract"):
        add_issue(issues, "TASK_LINT_TODO_NEEDS_REVIEW", "needs_review", "source_ui_contract TODO for UI task", "source_ui_contract", "Task Contract Needs Review Rules")

    ap = ensure_list_str(front.get("affected_paths"))
    if ap is not None and any(x.strip() == "TODO" for x in ap):
        add_issue(issues, "TASK_LINT_TODO_NEEDS_REVIEW", "needs_review", "affected_paths contains TODO", "affected_paths", "Task Contract Needs Review Rules")

    vp = ensure_list_str(front.get("validation_plan"))
    if vp is not None and any(x.strip() == "TODO" for x in vp):
        add_issue(issues, "TASK_LINT_TODO_NEEDS_REVIEW", "needs_review", "validation_plan contains TODO", "validation_plan", "Task Contract Needs Review Rules")


def check_queue(path: Path, issues: list[dict[str, str]]) -> None:
    # 1-2 load and parse
    try:
        obj = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        add_issue(issues, "TASK_LINT_JSON_MALFORMED", "failed", f"malformed json: {e}", "json", "Malformed JSON must fail closed")
        return

    if not isinstance(obj, dict):
        add_issue(issues, "TASK_LINT_JSON_MALFORMED", "failed", "queue entry must be object", "json", "Queue Entry Required Fields")
        return

    # 3 forbidden fields as top-level json keys
    for k in obj.keys():
        if k in FORBIDDEN_EXEC_FIELDS:
            add_issue(issues, "TASK_LINT_FORBIDDEN_EXECUTION_AUTHORITY_FIELD", "fail", f"forbidden key: {k}", k, "Forbidden execution-authority fields")

    # 4 required fields
    for k in QUEUE_REQUIRED_FIELDS:
        if k not in obj:
            add_issue(issues, "TASK_LINT_MISSING_REQUIRED_FIELD", "fail", f"missing required field {k}", k, "Queue Entry Required Fields")
    if any(i["severity"] == "fail" and i["code"] == "TASK_LINT_MISSING_REQUIRED_FIELD" for i in issues):
        return

    # 5 types and enums
    if obj.get("queue_entry_version") != 1:
        add_issue(issues, "TASK_LINT_INVALID_FIELD", "fail", "queue_entry_version must be 1", "queue_entry_version", "Queue Entry Required Fields")

    if not isinstance(obj.get("task_id"), str):
        add_issue(issues, "TASK_LINT_INVALID_FIELD", "fail", "task_id must be string", "task_id", "Queue Entry Required Fields")

    if not isinstance(obj.get("source_task_contract"), str):
        add_issue(issues, "TASK_LINT_INVALID_FIELD", "fail", "source_task_contract must be string", "source_task_contract", "Queue Entry Required Fields")

    if not isinstance(obj.get("source_dependency_map"), str):
        add_issue(issues, "TASK_LINT_INVALID_FIELD", "fail", "source_dependency_map must be string", "source_dependency_map", "Queue Entry Required Fields")

    q_status = obj.get("queue_status")
    allowed_q_status = {"candidate", "blocked", "ready_for_review", "queued", "rejected"}
    if q_status not in allowed_q_status:
        add_issue(issues, "TASK_LINT_QUEUE_STATUS_INCONSISTENT", "fail", "unknown queue_status", "queue_status", "Queue Status Consistency Rules")

    q_reason = obj.get("queue_reason")
    allowed_q_reason = {
        "created_from_candidate_task",
        "dependency_satisfied",
        "blocked_by_dependency",
        "blocked_by_approval",
        "blocked_by_owner_review",
        "blocked_by_context",
        "blocked_by_ui_contract",
        "blocked_by_lint",
        "invalid_contract",
        "rejected_by_owner",
        "manual_queue_hold",
    }
    if q_reason not in allowed_q_reason:
        add_issue(issues, "TASK_LINT_QUEUE_STATUS_INCONSISTENT", "fail", "unknown queue_reason", "queue_reason", "Queue Status Consistency Rules")

    dep_status = obj.get("dependency_status")
    lint_status = obj.get("lint_status")
    context_status = obj.get("context_status")
    ui_contract_status = obj.get("ui_contract_status")
    approval_status = obj.get("approval_status")
    owner_review_status = obj.get("owner_review_status")

    if dep_status not in {"satisfied", "blocked", "invalid", "not_checked"}:
        add_issue(issues, "TASK_LINT_QUEUE_STATUS_INCONSISTENT", "fail", "unknown dependency_status", "dependency_status", "Queue Status Consistency Rules")
    if lint_status not in {"pass", "warning", "fail", "not_run"}:
        add_issue(issues, "TASK_LINT_QUEUE_STATUS_INCONSISTENT", "fail", "unknown lint_status", "lint_status", "Queue Status Consistency Rules")
    if context_status not in {"present", "missing", "stale", "not_required", "not_checked"}:
        add_issue(issues, "TASK_LINT_QUEUE_STATUS_INCONSISTENT", "fail", "unknown context_status", "context_status", "Queue Status Consistency Rules")
    if ui_contract_status not in {"present", "missing", "not_required", "not_checked"}:
        add_issue(issues, "TASK_LINT_QUEUE_STATUS_INCONSISTENT", "fail", "unknown ui_contract_status", "ui_contract_status", "Queue Status Consistency Rules")
    if approval_status not in {"approved", "required_missing", "not_required", "not_checked"}:
        add_issue(issues, "TASK_LINT_QUEUE_STATUS_INCONSISTENT", "fail", "unknown approval_status", "approval_status", "Queue Status Consistency Rules")
    if owner_review_status not in {"approved", "required_missing", "not_required", "not_checked"}:
        add_issue(issues, "TASK_LINT_QUEUE_STATUS_INCONSISTENT", "fail", "unknown owner_review_status", "owner_review_status", "Queue Status Consistency Rules")

    if obj.get("priority") not in {"high", "normal", "low"}:
        add_issue(issues, "TASK_LINT_INVALID_FIELD", "fail", "invalid priority", "priority", "Queue Entry Required Fields")
    if obj.get("risk_level") not in {"LOW", "MEDIUM", "HIGH", "CRITICAL"}:
        add_issue(issues, "TASK_LINT_INVALID_FIELD", "fail", "invalid risk_level", "risk_level", "Queue Entry Required Fields")

    for lf in ["depends_on", "blocked_by"]:
        val = obj.get(lf)
        if not isinstance(val, list) or any(not isinstance(x, str) for x in val):
            add_issue(issues, "TASK_LINT_INVALID_FIELD", "fail", f"{lf} must be list[str]", lf, "Queue Entry Required Fields")

    if not isinstance(obj.get("human_approval_required"), bool):
        add_issue(issues, "TASK_LINT_INVALID_FIELD", "fail", "human_approval_required must be bool", "human_approval_required", "Queue Entry Required Fields")
    if not isinstance(obj.get("owner_review_required"), bool):
        add_issue(issues, "TASK_LINT_INVALID_FIELD", "fail", "owner_review_required must be bool", "owner_review_required", "Queue Entry Required Fields")

    # 6 queue_entry_id normalization
    task_id = obj.get("task_id", "")
    if isinstance(task_id, str):
        normalized = normalize_ascii_task_id(task_id)
        expected = f"queue_{normalized}" if normalized else ""
        qid = obj.get("queue_entry_id")
        if not normalized or qid != expected:
            add_issue(issues, "TASK_LINT_INVALID_QUEUE_ENTRY_ID", "fail", "queue_entry_id does not match queue_<normalized_task_id>", "queue_entry_id", "Queue Entry ID Normalization Rules")
    else:
        add_issue(issues, "TASK_LINT_INVALID_QUEUE_ENTRY_ID", "fail", "task_id must be string for normalization", "task_id", "Queue Entry ID Normalization Rules")

    # 7 created_at
    created_at = obj.get("created_at")
    if not isinstance(created_at, str) or not DATE_RE.match(created_at):
        add_issue(issues, "TASK_LINT_INVALID_CREATED_AT", "fail", "created_at invalid", "created_at", "Queue Entry Required Fields")

    # 8 non_approval_warning substrings
    naw = obj.get("non_approval_warning", "")
    if not isinstance(naw, str) or ("not approval" not in naw.lower()) or ("does not authorize execution" not in naw.lower()):
        add_issue(issues, "TASK_LINT_INVALID_FIELD", "fail", "non_approval_warning missing required substrings", "non_approval_warning", "Queue Entry Required Fields")

    # 9 status consistency
    blocked_by = obj.get("blocked_by", []) if isinstance(obj.get("blocked_by"), list) else []
    if q_status == "ready_for_review":
        if blocked_by:
            add_issue(issues, "TASK_LINT_QUEUE_BLOCKED_BUT_READY", "fail", "ready_for_review with blockers", "blocked_by", "Queue Status Consistency Rules")
        if dep_status in {"blocked", "invalid"} or lint_status in {"fail", "not_run"} or context_status in {"missing", "stale"} or ui_contract_status == "missing" or approval_status == "required_missing" or owner_review_status == "required_missing":
            add_issue(issues, "TASK_LINT_QUEUE_STATUS_INCONSISTENT", "fail", "ready_for_review has blocking gate status", "queue_status", "Queue Status Consistency Rules")

    if q_status == "queued":
        if dep_status in {"blocked", "invalid"} or lint_status in {"fail", "not_run"} or context_status in {"missing", "stale"} or ui_contract_status == "missing" or approval_status == "required_missing" or owner_review_status == "required_missing":
            add_issue(issues, "TASK_LINT_QUEUE_QUEUED_WITH_BLOCKERS", "fail", "queued with blockers", "queue_status", "Queue Status Consistency Rules")

    if q_status == "blocked" and q_reason not in {
        "blocked_by_dependency",
        "blocked_by_approval",
        "blocked_by_owner_review",
        "blocked_by_context",
        "blocked_by_ui_contract",
        "blocked_by_lint",
    }:
        add_issue(issues, "TASK_LINT_QUEUE_STATUS_INCONSISTENT", "fail", "blocked must use blocking queue_reason", "queue_reason", "Queue Status Consistency Rules")

    if q_status == "rejected" and q_reason not in {"rejected_by_owner", "manual_queue_hold"}:
        add_issue(issues, "TASK_LINT_QUEUE_STATUS_INCONSISTENT", "fail", "rejected must use rejected_by_owner or manual_queue_hold", "queue_reason", "Queue Status Consistency Rules")


def detect_kind(path: Path, kind: str, issues: list[dict[str, str]]) -> str | None:
    if kind in {"task", "queue"}:
        return kind
    # auto by extension only
    ext = path.suffix.lower()
    if ext == ".md":
        return "task"
    if ext == ".json":
        return "queue"
    add_issue(issues, "TASK_LINT_UNSUPPORTED_EXTENSION", "failed", "--kind auto supports only .md and .json", "target", "--kind auto must detect input kind only by file extension")
    return None


def main() -> int:
    args = parse_args()
    target = Path(args.target)
    issues: list[dict[str, str]] = []

    if not target.exists():
        add_issue(issues, "TASK_LINT_TARGET_NOT_FOUND", "failed", "target does not exist", "target", "Target must exist")
        return output(TASK_LINT_FAILED, target, args.kind, issues, args.json_mode)

    if target.is_dir():
        add_issue(issues, "TASK_LINT_DIRECTORY_NOT_SUPPORTED", "failed", "directory targets are not supported", "target", "Directory linting is out of scope")
        return output(TASK_LINT_FAILED, target, args.kind, issues, args.json_mode)

    effective_kind = detect_kind(target, args.kind, issues)
    if not effective_kind:
        return output(TASK_LINT_FAILED, target, args.kind, issues, args.json_mode)

    try:
        if effective_kind == "task":
            check_task(target, issues)
        elif effective_kind == "queue":
            check_queue(target, issues)
        else:
            add_issue(issues, "TASK_LINT_UNSUPPORTED_KIND", "failed", "unsupported kind", "kind", "Unknown kind must fail closed")
    except Exception as e:
        add_issue(issues, "TASK_LINT_RUNTIME_ERROR", "failed", f"runtime failure: {e}", "runtime", "Runtime failures must fail closed")

    result = issues_to_result(issues)
    return output(result, target, effective_kind, issues, args.json_mode)


if __name__ == "__main__":
    sys.exit(main())
