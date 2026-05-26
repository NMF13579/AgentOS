#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

RESULT_VALID = "EXECUTION_VERIFICATION_CHAIN_VALID"
RESULT_WARN = "EXECUTION_VERIFICATION_CHAIN_VALID_WITH_WARNINGS"
RESULT_INVALID = "EXECUTION_VERIFICATION_CHAIN_INVALID"

CHECKS = [
    "registry",
    "non-authority",
    "source-artifact-existence",
    "no-premature-downstream-artifacts",
    "schema-json-validity",
    "policy-version-presence",
    "final-status-presence",
]

REQUIRED_NON_AUTH = [
    "Execution verification registry is not approval.",
    "Execution verification registry does not start cleanup execution.",
    "Execution verification registry does not mutate lifecycle state.",
    "Execution verification registry does not authorize merge, push, or release.",
    "Execution verification registry does not change M56–M59 safety semantics.",
    "Execution verification registry does not override canonical contracts, policies, schemas, CLI behavior, fixture oracles, or completion reviews.",
    "Execution verification registry does not delete, rename, move, archive, deprecate, or consolidate artifacts.",
    "Execution verification registry does not authorize starting 60.7 automatically.",
]

SELF_NON_AUTH = [
    "Execution verification reusable checks are not approval.",
    "Execution verification reusable checks do not start cleanup execution.",
    "Execution verification reusable checks do not mutate lifecycle state.",
    "Execution verification reusable checks do not authorize merge, push, or release.",
    "Execution verification reusable checks do not change M56–M59 safety semantics.",
    "Execution verification reusable checks do not replace human review.",
    "Execution verification reusable checks do not verify a real execution result.",
    "Execution verification reusable checks do not authorize starting 60.9 automatically.",
]

PHASE_GATED_ARTIFACTS = [
    "reports/m60-documentation-pruning-plan.md",
    "reports/m60-documentation-consolidation-report.md",
    "scripts/check-execution-verification-regression.py",
    "docs/EXECUTION-VERIFICATION-REGRESSION-RUNNER.md",
    "reports/m60-cleanup-integration-summary.md",
    "reports/m60-cleanup-action-review.json",
    "reports/m60-cleanup-evidence-report.md",
    "reports/m60-completion-review.md",
]

ALWAYS_FORBIDDEN_UNTIL_LATER = [
]

SOURCE_PATHS = [
    "docs/AGENTOS-EXECUTION-VERIFICATION-REGISTRY-CONTRACT.md",
    "docs/EXECUTION-VERIFICATION-SOURCE-OF-TRUTH.md",
    "reports/m60-artifact-inventory.md",
    "reports/m60-duplication-drift-audit.md",
]

FINAL_STATUS_EXPECTED = {
    "reports/m60-m59-completion-intake.md": [
        "FINAL_STATUS: M60_INTAKE_READY",
        "FINAL_STATUS: M60_INTAKE_READY_WITH_WARNINGS",
    ],
    "docs/REPOSITORY-CLEANUP-CONSOLIDATION-ARCHITECTURE.md": [
        "FINAL_STATUS: M60_CLEANUP_ARCHITECTURE_DEFINED",
    ],
    "reports/m60-artifact-inventory.md": [
        "FINAL_STATUS: M60_ARTIFACT_INVENTORY_COMPLETE",
        "FINAL_STATUS: M60_ARTIFACT_INVENTORY_COMPLETE_WITH_WARNINGS",
    ],
    "docs/EXECUTION-VERIFICATION-SOURCE-OF-TRUTH.md": [
        "FINAL_STATUS: M60_SOURCE_OF_TRUTH_CLASSIFICATION_COMPLETE",
        "FINAL_STATUS: M60_SOURCE_OF_TRUTH_CLASSIFICATION_COMPLETE_WITH_WARNINGS",
    ],
    "reports/m60-duplication-drift-audit.md": [
        "FINAL_STATUS: M60_DUPLICATION_DRIFT_AUDIT_COMPLETE",
        "FINAL_STATUS: M60_DUPLICATION_DRIFT_AUDIT_COMPLETE_WITH_WARNINGS",
    ],
    "docs/AGENTOS-EXECUTION-VERIFICATION-REGISTRY-CONTRACT.md": [
        "FINAL_STATUS: M60_REGISTRY_CONTRACT_DEFINED",
    ],
    "docs/EXECUTION-VERIFICATION-REGISTRY.md": [
        "FINAL_STATUS: M60_REGISTRY_BUILDER_VALIDATOR_DEFINED",
    ],
    "reports/m60-validator-consolidation-plan.md": [
        "FINAL_STATUS: M60_VALIDATOR_CONSOLIDATION_PLAN_COMPLETE",
        "FINAL_STATUS: M60_VALIDATOR_CONSOLIDATION_PLAN_COMPLETE_WITH_WARNINGS",
    ],
}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def add_warning(state, check, msg):
    state["warnings"].append(msg)
    if check not in state["warning_checks"]:
        state["warning_checks"].append(check)


def add_blocker(state, check, msg):
    state["blockers"].append(msg)
    if check not in state["blocked_checks"]:
        state["blocked_checks"].append(check)


def run_registry(state, root, registry_path, schema_path):
    check = "registry"
    try:
        reg = load_json(registry_path)
    except Exception as exc:
        add_blocker(state, check, f"registry JSON parse failed: {exc}")
        return
    try:
        schema = load_json(schema_path)
    except Exception as exc:
        add_blocker(state, check, f"schema JSON parse failed: {exc}")
        return

    if reg.get("registry_version") != "M60.1":
        add_blocker(state, check, "registry_version must be M60.1")

    artifacts = reg.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        add_blocker(state, check, "artifacts must be non-empty array")
        return

    seen = set()
    for i, e in enumerate(artifacts):
        if not isinstance(e, dict):
            add_blocker(state, check, f"artifact entry {i} not object")
            continue
        aid = e.get("artifact_id")
        if not isinstance(aid, str) or not aid:
            add_blocker(state, check, f"artifact entry {i} invalid artifact_id")
        elif aid in seen:
            add_blocker(state, check, f"duplicate artifact_id: {aid}")
        else:
            seen.add(aid)

        if e.get("replacement_path") is not None and not isinstance(e.get("replacement_path"), str):
            add_blocker(state, check, f"artifact {aid}: replacement_path must be null or string")
        if not isinstance(e.get("notes"), str):
            add_blocker(state, check, f"artifact {aid}: notes must be string")
        if not isinstance(e.get("deprecated"), bool):
            add_blocker(state, check, f"artifact {aid}: deprecated must be boolean")
        if not isinstance(e.get("do_not_delete"), bool):
            add_blocker(state, check, f"artifact {aid}: do_not_delete must be boolean")
        if not isinstance(e.get("depends_on"), list):
            add_blocker(state, check, f"artifact {aid}: depends_on must be array")
        if not isinstance(e.get("validated_by"), list):
            add_blocker(state, check, f"artifact {aid}: validated_by must be array")

        p = str(e.get("path", "")).lower()
        if "m61" in p or "m62" in p:
            add_blocker(state, check, f"artifact {aid}: M61/M62 path not allowed")

    # benign use to ensure schema has expected keys
    if schema.get("type") != "object":
        add_blocker(state, check, "schema top-level type must be object")


def run_non_authority(state, root):
    check = "non-authority"
    reg_doc = root / "docs/EXECUTION-VERIFICATION-REGISTRY.md"
    text = reg_doc.read_text(encoding="utf-8") if reg_doc.exists() else ""
    for stmt in REQUIRED_NON_AUTH:
        if stmt not in text:
            add_warning(state, check, f"non-authority statement missing in registry doc: {stmt}")
    state["non_authority"] = SELF_NON_AUTH.copy()


def run_source_artifact_existence(state, root, reg):
    check = "source-artifact-existence"
    for p in SOURCE_PATHS:
        if not (root / p).exists():
            add_blocker(state, check, f"required source missing: {p}")

    # Validate top-level source references from the provided registry payload.
    for key in (
        "source_contract",
        "source_classification",
        "source_inventory",
        "source_duplication_drift_audit",
    ):
        p = reg.get(key)
        if not isinstance(p, str) or not p:
            add_blocker(state, check, f"registry {key} missing or invalid")
            continue
        if not (root / p).exists():
            add_blocker(state, check, f"registry source path missing: {p}")

    for e in reg.get("artifacts", []):
        if e.get("status") == "present":
            p = e.get("path")
            if not isinstance(p, str) or not (root / p).exists():
                add_blocker(state, check, f"present artifact path missing: {p}")


def file_contains_any(path_obj: Path, markers):
    if not path_obj.exists():
        return False
    txt = path_obj.read_text(encoding="utf-8", errors="ignore")
    return any(m in txt for m in markers)


def detect_m60_phase(root: Path):
    phase = {
        "m60_9_complete": False,
        "m60_10_complete": False,
        "m60_11_complete": False,
        "m60_12_created": False,
        "m60_13_created": False,
        "m60_14_created": False,
        "m60_15_created": False,
    }
    phase["m60_9_complete"] = file_contains_any(
        root / "reports/m60-documentation-pruning-plan.md",
        [
            "FINAL_STATUS: M60_DOCUMENTATION_PRUNING_PLAN_COMPLETE",
            "FINAL_STATUS: M60_DOCUMENTATION_PRUNING_PLAN_COMPLETE_WITH_WARNINGS",
        ],
    )
    phase["m60_10_complete"] = file_contains_any(
        root / "reports/m60-documentation-consolidation-report.md",
        [
            "FINAL_STATUS: M60_DOCUMENTATION_CONSOLIDATION_COMPLETE",
            "FINAL_STATUS: M60_DOCUMENTATION_CONSOLIDATION_COMPLETE_WITH_WARNINGS",
        ],
    )
    phase["m60_11_complete"] = file_contains_any(
        root / "docs/EXECUTION-VERIFICATION-REGRESSION-RUNNER.md",
        ["FINAL_STATUS: M60_REGRESSION_RUNNER_DEFINED"],
    )
    phase["m60_12_created"] = file_contains_any(
        root / "reports/m60-cleanup-integration-summary.md",
        [
            "FINAL_STATUS: M60_INTEGRATION_PASS",
            "FINAL_STATUS: M60_INTEGRATION_PASS_WITH_WARNINGS",
            "FINAL_STATUS: M60_INTEGRATION_BLOCKED",
        ],
    )
    action_review = root / "reports/m60-cleanup-action-review.json"
    if action_review.exists():
        try:
            review = load_json(action_review)
            phase["m60_13_created"] = review.get("final_status") in {
                "M60_CLEANUP_ACTION_REVIEW_PASS",
                "M60_CLEANUP_ACTION_REVIEW_PASS_WITH_WARNINGS",
                "M60_CLEANUP_ACTION_REVIEW_BLOCKED",
            }
        except Exception:
            phase["m60_13_created"] = False

    evidence_report = root / "reports/m60-cleanup-evidence-report.md"
    phase["m60_14_created"] = file_contains_any(
        evidence_report,
        [
            "FINAL_STATUS: M60_CLEANUP_EVIDENCE_COMPLETE",
            "FINAL_STATUS: M60_CLEANUP_EVIDENCE_COMPLETE_WITH_WARNINGS",
            "FINAL_STATUS: M60_CLEANUP_EVIDENCE_BLOCKED",
        ],
    )
    completion_review = root / "reports/m60-completion-review.md"
    phase["m60_15_created"] = file_contains_any(
        completion_review,
        [
            "FINAL_STATUS: M60_CLEANUP_COMPLETE",
            "FINAL_STATUS: M60_CLEANUP_COMPLETE_WITH_WARNINGS",
            "FINAL_STATUS: M60_CLEANUP_BLOCKED",
        ],
    )
    return phase


def is_legacy_exempt(path: str):
    if path.startswith("reports/"):
        p = path[len("reports/"):]
        if p.startswith("milestone-10") or p.startswith("agentos-validate-cli"):
            return True
        if len(p) >= 3 and p[0] == "m" and p[1:3].isdigit():
            n = int(p[1:3])
            if 0 <= n <= 49:
                return True
    if path.startswith("docs/HONEST-PASS-"):
        return True
    if path.startswith("tasks/queue/"):
        return True
    return False


def run_no_premature(state, root):
    check = "no-premature-downstream-artifacts"
    phase = detect_m60_phase(root)

    for p in PHASE_GATED_ARTIFACTS:
        path_obj = root / p
        if not path_obj.exists():
            continue
        if p == "reports/m60-documentation-pruning-plan.md" and phase["m60_9_complete"]:
            continue
        if p == "reports/m60-documentation-consolidation-report.md" and phase["m60_10_complete"]:
            continue
        if p in (
            "scripts/check-execution-verification-regression.py",
            "docs/EXECUTION-VERIFICATION-REGRESSION-RUNNER.md",
        ) and phase["m60_11_complete"]:
            continue
        if p == "reports/m60-cleanup-integration-summary.md" and phase["m60_12_created"]:
            continue
        if p == "reports/m60-cleanup-action-review.json" and phase["m60_13_created"]:
            continue
        if p == "reports/m60-cleanup-evidence-report.md" and phase["m60_14_created"]:
            continue
        if p == "reports/m60-completion-review.md" and phase["m60_15_created"]:
            continue
        add_blocker(state, check, f"forbidden downstream artifact exists for current phase: {p}")

    for p in ALWAYS_FORBIDDEN_UNTIL_LATER:
        if (root / p).exists():
            add_blocker(state, check, f"forbidden downstream artifact exists before allowed phase: {p}")

    roots = ["reports", "docs", "scripts", "tests", "templates", "schemas", "data"]
    needles = ("m61", "m62")
    for base in roots:
        bpath = root / base
        if not bpath.exists():
            continue
        for fp in bpath.rglob("*"):
            if not fp.is_file():
                continue
            rel = fp.relative_to(root).as_posix()
            low = rel.lower()
            if any(n in low for n in needles) and not is_legacy_exempt(rel):
                add_blocker(state, check, f"premature artifact detected: {rel}")


def run_schema_validity(state, schema):
    check = "schema-json-validity"
    if schema.get("type") != "object":
        add_blocker(state, check, "schema.type must be object")
    if "required" not in schema or "properties" not in schema:
        add_blocker(state, check, "schema missing required/properties")
        return
    props = schema.get("properties", {})
    if props.get("artifacts", {}).get("type") != "array":
        add_blocker(state, check, "schema artifacts must be array")
        return
    items = props.get("artifacts", {}).get("items", {})
    if not items:
        add_blocker(state, check, "schema artifacts.items missing")
        return
    if schema.get("additionalProperties") is not False:
        add_blocker(state, check, "schema additionalProperties must be false")
    if items.get("additionalProperties") is not False:
        add_blocker(state, check, "artifact item additionalProperties must be false")

    rp = items.get("properties", {}).get("replacement_path", {}).get("type")
    if rp not in (["string", "null"], ["null", "string"]):
        add_blocker(state, check, "replacement_path must be nullable string")

    notes_t = items.get("properties", {}).get("notes", {}).get("type")
    if notes_t != "string":
        add_blocker(state, check, "notes must be string in schema")


def run_policy_version_presence(state, root, reg):
    check = "policy-version-presence"
    if reg.get("registry_version") != "M60.1":
        add_blocker(state, check, "registry_version missing or invalid")

    # Deterministic where present in known M59 artifacts.
    files = [
        root / "reports/m59-execution-result-verification-action-review.json",
        root / "reports/m59-execution-result-verification-evidence-report.md",
    ]
    for p in files:
        if p.exists():
            txt = p.read_text(encoding="utf-8")
            if "policy_version" in txt and "M59.1" not in txt:
                add_warning(state, check, f"policy_version present but M59.1 not found in {p.as_posix()}")


def run_final_status_presence(state, root):
    check = "final-status-presence"
    for p, markers in FINAL_STATUS_EXPECTED.items():
        fp = root / p
        if not fp.exists():
            add_blocker(state, check, f"required status source missing: {p}")
            continue
        txt = fp.read_text(encoding="utf-8")
        if not any(m in txt for m in markers):
            add_blocker(state, check, f"missing expected FINAL_STATUS family in {p}")


def finalize_result(state, strict):
    # Strict mode keeps blockers strict but does not auto-upgrade warnings.
    # This preserves deterministic behavior for reusable baseline checks.
    _ = strict
    if state["blockers"]:
        return RESULT_INVALID, 2
    if state["warnings"]:
        return RESULT_WARN, 0
    return RESULT_VALID, 0


def main():
    parser = argparse.ArgumentParser(description="Reusable execution verification chain checks (read-only)")
    parser.add_argument("--json", action="store_true", help="Output JSON only")
    parser.add_argument("--explain", action="store_true", help="Explain implemented reusable checks")
    parser.add_argument("--root", default=".", help="Repository root path")
    parser.add_argument("--registry", default="data/execution-verification-registry.json", help="Registry JSON path")
    parser.add_argument("--schema", default="schemas/execution-verification-registry.schema.json", help="Registry schema path")
    parser.add_argument("--check", action="append", choices=["all"] + CHECKS, help="Run selected check(s)")
    parser.add_argument("--strict", action="store_true", help="Strict mode")
    args = parser.parse_args()

    if args.explain and not args.json:
        print("Reusable checks for registry/safety boundaries; non-authority validation; source existence; downstream artifact guard.")
        print("This checker is read-only and does not grant approval/authorization.")

    root = Path(args.root).resolve()
    registry_path = (root / args.registry).resolve()
    schema_path = (root / args.schema).resolve()

    requested = args.check if args.check else ["all"]
    run_list = CHECKS if "all" in requested else requested

    state = {
        "checks_run": [],
        "passed_checks": [],
        "warning_checks": [],
        "blocked_checks": [],
        "warnings": [],
        "blockers": [],
        "non_authority": [],
    }

    # base parse for checks that need data/schema
    reg = None
    schema = None
    if any(c in run_list for c in ["registry", "source-artifact-existence", "policy-version-presence"]):
        try:
            reg = load_json(registry_path)
        except Exception as exc:
            if "registry" in run_list or "source-artifact-existence" in run_list or "policy-version-presence" in run_list:
                add_blocker(state, "registry", f"registry JSON parse failed: {exc}")
                reg = {}
    if any(c in run_list for c in ["registry", "schema-json-validity"]):
        try:
            schema = load_json(schema_path)
        except Exception as exc:
            add_blocker(state, "schema-json-validity", f"schema JSON parse failed: {exc}")
            schema = {}

    for check in run_list:
        state["checks_run"].append(check)
        before_w = len(state["warning_checks"])
        before_b = len(state["blocked_checks"])

        if check == "registry":
            run_registry(state, root, registry_path, schema_path)
        elif check == "non-authority":
            run_non_authority(state, root)
        elif check == "source-artifact-existence":
            run_source_artifact_existence(state, root, reg or {})
        elif check == "no-premature-downstream-artifacts":
            run_no_premature(state, root)
        elif check == "schema-json-validity":
            run_schema_validity(state, schema or {})
        elif check == "policy-version-presence":
            run_policy_version_presence(state, root, reg or {})
        elif check == "final-status-presence":
            run_final_status_presence(state, root)

        if len(state["blocked_checks"]) == before_b and len(state["warning_checks"]) == before_w:
            state["passed_checks"].append(check)

    result, exit_code = finalize_result(state, args.strict)

    payload = {
        "result": result,
        "exit_code": exit_code,
        "strict": args.strict,
        "root": args.root,
        "registry_path": args.registry,
        "schema_path": args.schema,
        "checks_requested": requested,
        "checks_run": state["checks_run"],
        "passed_checks": state["passed_checks"],
        "warning_checks": state["warning_checks"],
        "blocked_checks": state["blocked_checks"],
        "warnings": state["warnings"],
        "blockers": state["blockers"],
        "non_authority": state["non_authority"],
    }

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(result)
        if state["warnings"]:
            for w in state["warnings"]:
                print(f"WARN: {w}")
        if state["blockers"]:
            for b in state["blockers"]:
                print(f"BLOCK: {b}")

    raise SystemExit(exit_code)


if __name__ == "__main__":
    main()
