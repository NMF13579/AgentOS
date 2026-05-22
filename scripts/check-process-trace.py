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


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    h.update(p.read_bytes())
    return "sha256:" + h.hexdigest()


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


def load_trace(path: Path):
    if path.is_dir():
        f = path / "trace.json"
    else:
        f = path
    return f, json.loads(f.read_text(encoding="utf-8"))


def main():
    ap = argparse.ArgumentParser(description="Check process trace integrity.")
    ap.add_argument("path", nargs="?", help="Fixture directory or trace.json")
    ap.add_argument("--json", action="store_true", dest="as_json")
    args = ap.parse_args()
    if not args.path:
        ap.print_help()
        return 0

    target = Path(args.path)
    try:
        trace_file, data = load_trace(target)
    except Exception as e:
        return emit(VIOL, "TRACE_INVALID", f"Invalid input: {e}", target, [], args.as_json)

    root = trace_file.parent
    result_claim = data.get("result_claim")
    trace = data.get("execution_trace")
    if result_claim == "PASS" and (not isinstance(trace, list) or not trace):
        return emit(VIOL, "TRACE_MISSING", "PASS claim without execution_trace.", target, [], args.as_json)
    if not isinstance(trace, list):
        trace = []

    details = []
    for item in trace:
        if not item.get("command") or "exit_code" not in item or not item.get("output_artifact"):
            return emit(VIOL, "TRACE_INVALID", "Trace item missing required fields.", target, details, args.as_json)
        art = root / item["output_artifact"]
        if not art.exists():
            return emit(VIOL, "ARTIFACT_MISSING", "Output artifact missing.", target, details, args.as_json)
        got_hash = sha256_file(art)
        if got_hash != item.get("output_hash"):
            return emit(VIOL, "HASH_MISMATCH", "Output hash mismatch.", target, details, args.as_json)
        src = item.get("validation_source_id")
        if not src or src not in KNOWN_SOURCES:
            return emit(REVIEW, "RUNNER_PROOF_NOT_VERIFIED", "Validation source missing or unknown.", target, details, args.as_json)
        if item.get("trace_writable_by_execution_agent") is True:
            return emit(REVIEW, "RUNNER_PROOF_NOT_VERIFIED", "Trace writable by execution agent.", target, details, args.as_json)
        if result_claim == "PASS" and item.get("runner_generated") is not True:
            return emit(VIOL, "RUNNER_PROOF_NOT_VERIFIED", "Clean PASS requires runner_generated=true.", target, details, args.as_json)
        details.append({"command": item.get("command"), "artifact": item.get("output_artifact")})

    if result_claim == "PASS" and not details:
        return emit(VIOL, "TRACE_MISSING", "PASS claim without verifiable trace.", target, details, args.as_json)
    return emit(OK, None, "Trace verified.", target, details, args.as_json)


if __name__ == "__main__":
    sys.exit(main())
