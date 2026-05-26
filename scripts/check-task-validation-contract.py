#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
import sys

RESULT_PASS = "M63_CONTRACT_VALIDATION_PASS"
RESULT_WARN = "M63_CONTRACT_VALIDATION_PASS_WITH_WARNINGS"
RESULT_BLOCKED = "M63_CONTRACT_VALIDATION_BLOCKED"

ALLOWED_TOP = {
    "TASK_VALIDATION_PASS",
    "TASK_VALIDATION_PASS_WITH_WARNINGS",
    "TASK_VALIDATION_BLOCKED",
    "TASK_VALIDATION_NOT_ENOUGH_EVIDENCE",
}

ALLOWED_SUB = {"PASS", "PASS_WITH_WARNINGS", "BLOCKED", "NOT_ENOUGH_EVIDENCE", "NOT_RUN"}

REQUIRED_BOUNDARY = [
    "TASK_VALIDATION_PASS is not approval.",
    "TASK_VALIDATION_PASS does not complete the task.",
    "TASK_VALIDATION_PASS does not replace human review.",
    "TASK_VALIDATION_PASS does not authorize merge, push, or release.",
    "Human review remains required.",
]

FORBIDDEN_CLAIMS = [
    "approved",
    "approval granted",
    "task approved",
    "task is approved",
    "task completion approved",
    "complete without review",
    "human review not required",
    "human_review_required: false",
    "human review can be skipped",
    "merged",
    "released",
    "pushed",
    "deployment authorized",
    "merge authorized",
    "push authorized",
    "release authorized",
    "lifecycle mutated",
    "completion gate passed",
    "production task acceptance gate passed",
    "m64 started automatically",
]

M64_M67_SCOPE_PHRASES = [
    "full task output evidence model",
    "agent evidence schema",
    "acceptance criteria checker",
    "unified agent task validation runner",
    "false pass resistance suite",
    "completion gate integration",
    "production task acceptance gate",
]

SAFE_CONTEXT_KEYS = {
    "declared_forbidden_changes",
    "forbidden_claims",
    "forbidden_operations",
    "non_authority_boundary",
}


def parse_args():
    p = argparse.ArgumentParser(description="M63 task validation contract checker")
    p.add_argument("--package", required=True, help="Path to task validation package JSON")
    p.add_argument("--result", required=True, help="Path to task validation result JSON")
    p.add_argument("--strict", action="store_true", help="Record strict mode (no remapping in 63.6)")
    p.add_argument("--json", action="store_true", help="Output JSON")
    return p.parse_args()


def add_warning(payload, msg):
    payload["warnings"].append(str(msg))


def add_blocker(payload, msg):
    payload["blockers"].append(str(msg))


def make_payload(strict):
    return {
        "result": RESULT_BLOCKED,
        "strict": bool(strict),
        "package_checked": False,
        "result_checked": False,
        "package_json_valid": False,
        "result_json_valid": False,
        "package_required_fields_present": False,
        "result_required_fields_present": False,
        "package_required_field_types_valid": False,
        "result_required_field_types_valid": False,
        "package_type_supported": False,
        "result_type_supported": False,
        "contract_version_supported": False,
        "task_id_match": False,
        "package_valid_claim_checked": False,
        "package_valid_claim_consistent": False,
        "task_validation_result_value": "",
        "subresults_valid": False,
        "human_review_required": True,
        "input_attempted_to_disable_human_review": False,
        "non_authority_boundary_present": False,
        "required_non_authority_statements_present": False,
        "forbidden_claims_found": False,
        "m64_m67_scope_absorption_found": False,
        "warnings": [],
        "blockers": [],
    }


def load_json(path: Path):
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return None, None
    try:
        return json.loads(text), text
    except Exception:
        return None, text


def check_required_fields(obj, required):
    return all(k in obj for k in required)


def is_real_bool(v):
    return type(v) is bool


def check_package_types(pkg):
    req = {
        "contract_version": str,
        "package_type": str,
        "task_id": str,
        "task_brief_path": str,
        "declared_scope": dict,
        "declared_forbidden_changes": dict,
        "expected_artifacts": list,
        "changed_files": list,
        "diff_reference": str,
        "agent_evidence_ref": dict,
        "validation_claims_ref": dict,
    }
    for k, t in req.items():
        if k not in pkg or not isinstance(pkg[k], t):
            return False
    if "human_review_required" not in pkg or not is_real_bool(pkg["human_review_required"]):
        return False
    return True


def check_result_types(res):
    req = {
        "contract_version": str,
        "result_type": str,
        "task_id": str,
        "result": str,
        "schema_result": str,
        "scope_result": str,
        "evidence_ref_result": str,
        "validation_claims_result": str,
        "warnings": list,
        "blockers": list,
        "non_authority_boundary": list,
    }
    for k, t in req.items():
        if k not in res or not isinstance(res[k], t):
            return False
    if "package_valid" not in res or not is_real_bool(res["package_valid"]):
        return False
    if "human_review_required" not in res or not is_real_bool(res["human_review_required"]):
        return False
    if not res["non_authority_boundary"] or not all(isinstance(x, str) for x in res["non_authority_boundary"]):
        return False
    if not all(isinstance(x, str) for x in res["warnings"]):
        return False
    if not all(isinstance(x, str) for x in res["blockers"]):
        return False
    return True


def scan_strings(value, path=()):
    out = []
    if isinstance(value, str):
        out.append((path, value))
    elif isinstance(value, dict):
        for k, v in value.items():
            out.extend(scan_strings(v, path + (k,)))
    elif isinstance(value, list):
        for i, v in enumerate(value):
            out.extend(scan_strings(v, path + (str(i),)))
    return out


def in_safe_context(path):
    return any(p in SAFE_CONTEXT_KEYS for p in path)


def main():
    try:
        args = parse_args()
        payload = make_payload(args.strict)

        package_path = Path(args.package)
        result_path = Path(args.result)

        payload["package_checked"] = True
        payload["result_checked"] = True

        pkg, pkg_text = load_json(package_path)
        res, res_text = load_json(result_path)

        if pkg is None:
            add_blocker(payload, f"package file missing, unreadable, or malformed: {package_path}")
            payload["package_json_valid"] = False
        else:
            payload["package_json_valid"] = True

        if res is None:
            add_blocker(payload, f"result file missing, unreadable, or malformed: {result_path}")
            payload["result_json_valid"] = False
        else:
            payload["result_json_valid"] = True

        if pkg is not None:
            required_pkg = [
                "contract_version", "package_type", "task_id", "task_brief_path", "declared_scope",
                "declared_forbidden_changes", "expected_artifacts", "changed_files", "diff_reference",
                "agent_evidence_ref", "validation_claims_ref", "human_review_required",
            ]
            payload["package_required_fields_present"] = check_required_fields(pkg, required_pkg)
            if not payload["package_required_fields_present"]:
                add_blocker(payload, "required package field missing")

            payload["package_required_field_types_valid"] = check_package_types(pkg)
            if not payload["package_required_field_types_valid"]:
                add_blocker(payload, "required package field has wrong JSON type")

            payload["package_type_supported"] = pkg.get("package_type") == "task_validation_package"
            if not payload["package_type_supported"]:
                add_blocker(payload, "unsupported package_type")

            pkg_ver_ok = pkg.get("contract_version") == "m63.task_validation_package.v1"
            if not pkg_ver_ok:
                add_blocker(payload, "unsupported package contract_version")

            if pkg.get("human_review_required") is False:
                payload["input_attempted_to_disable_human_review"] = True
                add_blocker(payload, "package attempts to disable human review")
            if pkg.get("human_review_required") is not True:
                add_blocker(payload, "package human_review_required is missing or not true")

        pkg_valid_by_checker = pkg is not None and payload["package_required_fields_present"] and payload["package_required_field_types_valid"] and payload["package_type_supported"] and not payload["input_attempted_to_disable_human_review"]

        if res is not None:
            required_res = [
                "contract_version", "result_type", "task_id", "result", "package_valid", "schema_result",
                "scope_result", "evidence_ref_result", "validation_claims_result", "human_review_required",
                "warnings", "blockers", "non_authority_boundary",
            ]
            payload["result_required_fields_present"] = check_required_fields(res, required_res)
            if not payload["result_required_fields_present"]:
                add_blocker(payload, "required result field missing")

            payload["result_required_field_types_valid"] = check_result_types(res)
            if not payload["result_required_field_types_valid"]:
                add_blocker(payload, "required result field has wrong JSON type")

            payload["result_type_supported"] = res.get("result_type") == "task_validation_result"
            if not payload["result_type_supported"]:
                add_blocker(payload, "unsupported result_type")

            res_ver_ok = res.get("contract_version") == "m63.task_validation_result.v1"
            payload["contract_version_supported"] = bool((pkg is None or pkg.get("contract_version") == "m63.task_validation_package.v1") and res_ver_ok)
            if not res_ver_ok:
                add_blocker(payload, "unsupported result contract_version")

            payload["task_validation_result_value"] = str(res.get("result", ""))
            if res.get("result") not in ALLOWED_TOP:
                add_blocker(payload, "unknown top-level task validation result value")

            subvals = [res.get("schema_result"), res.get("scope_result"), res.get("evidence_ref_result"), res.get("validation_claims_result")]
            payload["subresults_valid"] = all(v in ALLOWED_SUB for v in subvals)
            if not payload["subresults_valid"]:
                add_blocker(payload, "unknown subresult value")

            payload["non_authority_boundary_present"] = isinstance(res.get("non_authority_boundary"), list) and len(res.get("non_authority_boundary", [])) > 0 and all(isinstance(x, str) for x in res.get("non_authority_boundary", []))
            if not payload["non_authority_boundary_present"]:
                add_blocker(payload, "non_authority_boundary is missing, empty, or invalid")

            if payload["non_authority_boundary_present"]:
                boundary_set = set(res.get("non_authority_boundary", []))
                payload["required_non_authority_statements_present"] = all(s in boundary_set for s in REQUIRED_BOUNDARY)
                if not payload["required_non_authority_statements_present"]:
                    add_blocker(payload, "required non-authority statement is missing")
            else:
                payload["required_non_authority_statements_present"] = False

            if res.get("human_review_required") is False:
                payload["input_attempted_to_disable_human_review"] = True
                add_blocker(payload, "result attempts to disable human review")
            if res.get("human_review_required") is not True:
                add_blocker(payload, "result human_review_required is missing or not true")

            payload["package_valid_claim_checked"] = True
            claim = res.get("package_valid")
            if claim is True and not pkg_valid_by_checker:
                payload["package_valid_claim_consistent"] = False
                add_blocker(payload, "package_valid contradicts validator findings")
            elif claim is False and pkg_valid_by_checker:
                payload["package_valid_claim_consistent"] = False
                add_blocker(payload, "package_valid false contradicts validator findings")
            else:
                payload["package_valid_claim_consistent"] = True

        if pkg is not None and res is not None:
            payload["task_id_match"] = pkg.get("task_id") == res.get("task_id")
            if not payload["task_id_match"]:
                add_blocker(payload, "package task_id and result task_id mismatch")

        # Recursive string-value scanning.
        forbidden_hits = []
        ambiguity = False
        for obj in [pkg if pkg is not None else {}, res if res is not None else {}]:
            for path, sval in scan_strings(obj):
                low = sval.lower()
                safe_ctx = in_safe_context(path)
                for phrase in FORBIDDEN_CLAIMS:
                    if phrase in low:
                        if safe_ctx:
                            add_warning(payload, f"forbidden phrase in safe context: {phrase}")
                        else:
                            forbidden_hits.append(f"forbidden affirmative claim candidate at {'.'.join(path)}: {phrase}")
                for phrase in M64_M67_SCOPE_PHRASES:
                    if phrase in low and not safe_ctx:
                        payload["m64_m67_scope_absorption_found"] = True

        if forbidden_hits:
            payload["forbidden_claims_found"] = True
            for hit in forbidden_hits:
                add_blocker(payload, hit)
        if payload["m64_m67_scope_absorption_found"]:
            add_blocker(payload, "package/result attempts to absorb M64-M67 responsibilities")

        # Raw hints for human review bypass.
        raw_text = (pkg_text or "") + "\n" + (res_text or "")
        raw_low = raw_text.lower()
        if "human review can be skipped" in raw_low or "human review not required" in raw_low or "human_review_required: false" in raw_low:
            payload["input_attempted_to_disable_human_review"] = True
            if "attempts to disable human review" not in " ".join(payload["blockers"]):
                add_blocker(payload, "input attempted to disable human review")

        if payload["blockers"]:
            payload["result"] = RESULT_BLOCKED
            code = 1
        elif payload["warnings"]:
            payload["result"] = RESULT_WARN
            code = 0
        else:
            payload["result"] = RESULT_PASS
            code = 0

        if args.json:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            print(payload["result"])
        return code

    except SystemExit:
        raise
    except Exception as exc:
        payload = make_payload(False)
        payload["result"] = RESULT_BLOCKED
        payload["package_checked"] = True
        payload["result_checked"] = True
        payload["package_json_valid"] = False
        payload["result_json_valid"] = False
        payload["warnings"] = []
        payload["blockers"] = [f"validator internal error: {exc}"]
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
