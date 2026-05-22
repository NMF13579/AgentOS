#!/usr/bin/env python3
import argparse
import hashlib
import json
from pathlib import Path
import sys

OK = "HONEST_PASS_OK"
VIOL = "HONEST_PASS_VIOLATION"
REVIEW = "HONEST_PASS_NEEDS_REVIEW"
KNOWN_SOURCES = {"agentos-runner", "ci-runner", "trusted-wrapper", "approved-entrypoint"}
KNOWN_GENERATORS = {"trusted-evaluator", "runner", "validator-wrapper", "agent"}


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    h.update(p.read_bytes())
    return "sha256:" + h.hexdigest()


def compute_binding_hash(artifacts):
    rows = []
    for a in sorted(artifacts, key=lambda x: x["path"]):
        rows.append(f"{a['path']}|{a['sha256']}")
    joined = "\n".join(rows)
    return "sha256:" + hashlib.sha256(joined.encode("utf-8")).hexdigest()


def emit(result, failure_class, message, checked_path, details, as_json):
    payload = {
        "result": result,
        "failure_class": failure_class,
        "message": message,
        "checked_path": str(checked_path),
        "details": details,
    }
    if as_json:
        print(json.dumps(payload, ensure_ascii=True))
    else:
        print(f"{result}: {message}")
    return 0 if result == OK else 1


def main():
    ap = argparse.ArgumentParser(description="Check evidence binding integrity.")
    ap.add_argument("path", nargs="?", help="Fixture directory or binding.json")
    ap.add_argument("--json", action="store_true", dest="as_json")
    args = ap.parse_args()

    if not args.path:
        ap.print_help()
        return 0

    target = Path(args.path)
    binding_file = target / "binding.json" if target.is_dir() else target
    root = binding_file.parent
    try:
        data = json.loads(binding_file.read_text(encoding="utf-8"))
    except Exception as e:
        return emit(VIOL, "BINDING_INVALID", f"Invalid input: {e}", target, [], args.as_json)

    if data.get("result_claim") == "PASS" and "evidence_binding" not in data:
        return emit(VIOL, "PASS_WITHOUT_PROOF", "PASS claim without binding.", target, [], args.as_json)

    b = data.get("evidence_binding")
    if not isinstance(b, dict):
        return emit(VIOL, "BINDING_INVALID", "Invalid evidence_binding object.", target, [], args.as_json)

    generated_by = b.get("generated_by")
    src = b.get("validation_source_id")
    if generated_by == "agent":
        return emit(VIOL, "PASS_WITHOUT_PROOF", "Agent-computed binding cannot be clean PASS.", target, [], args.as_json)
    if generated_by not in KNOWN_GENERATORS:
        return emit(REVIEW, "RUNNER_PROOF_NOT_VERIFIED", "Unknown binding generator.", target, [], args.as_json)
    if not src or src not in KNOWN_SOURCES:
        return emit(REVIEW, "RUNNER_PROOF_NOT_VERIFIED", "Unknown validation source.", target, [], args.as_json)

    artifacts = b.get("bound_artifacts", [])
    if not isinstance(artifacts, list) or not artifacts:
        return emit(VIOL, "BINDING_INVALID", "No bound artifacts.", target, [], args.as_json)

    details = []
    for a in artifacts:
        p = root / a.get("path", "")
        if not p.exists():
            return emit(VIOL, "ARTIFACT_MISSING", "Bound artifact missing.", target, details, args.as_json)
        got = sha256_file(p)
        if got != a.get("sha256"):
            return emit(VIOL, "HASH_MISMATCH", "Bound artifact hash mismatch.", target, details, args.as_json)
        details.append({"path": a.get("path"), "sha256": got})

    expected_binding = compute_binding_hash(artifacts)
    if expected_binding != b.get("binding_hash"):
        return emit(VIOL, "BINDING_INVALID", "Binding hash mismatch.", target, details, args.as_json)

    return emit(OK, None, "Evidence binding verified.", target, details, args.as_json)


if __name__ == "__main__":
    sys.exit(main())
