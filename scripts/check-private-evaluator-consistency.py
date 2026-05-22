#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
import sys

OK = "HONEST_PASS_OK"
VIOL = "HONEST_PASS_VIOLATION"
REVIEW = "HONEST_PASS_NEEDS_REVIEW"


def out(result, failure_class, message, checked_path, details, as_json):
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


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def resolve_paths(inp: Path):
    if inp.is_dir():
        return inp / "public-rules.json", inp / "private-checklist.json"
    return inp.parent / "public-rules.json", inp


def main():
    p = argparse.ArgumentParser(description="Check private evaluator consistency.")
    p.add_argument("path", nargs="?", help="Fixture directory or private-checklist.json")
    p.add_argument("--json", action="store_true", dest="as_json")
    args = p.parse_args()

    if not args.path:
        p.print_help()
        return 0

    target = Path(args.path)
    pub_path, prv_path = resolve_paths(target)

    if not pub_path.exists() or not prv_path.exists():
        return out(REVIEW, "RUNNER_PROOF_NOT_VERIFIED", "Required input files missing.", target, [], args.as_json)

    try:
        pub = load_json(pub_path)
        prv = load_json(prv_path)
    except Exception as e:
        return out(VIOL, "TRACE_INVALID", f"Invalid JSON: {e}", target, [], args.as_json)

    public_rules = {r.get("id"): r for r in pub.get("public_rules", []) if isinstance(r, dict)}
    checks = prv.get("private_checks", [])
    if not isinstance(checks, list):
        return out(VIOL, "TRACE_INVALID", "private_checks must be a list.", target, [], args.as_json)

    details = []
    for c in checks:
        if not isinstance(c, dict):
            return out(VIOL, "TRACE_INVALID", "private_check item must be object.", target, details, args.as_json)
        if c.get("hidden_requirement") is True:
            return out(VIOL, "HIDDEN_REQUIREMENT_DETECTED", "hidden_requirement=true is forbidden.", target, details, args.as_json)
        map_id = c.get("maps_to_public_rule")
        if not map_id or map_id not in public_rules:
            return out(VIOL, "PRIVATE_CHECK_UNMAPPED", "Private check is not mapped to existing public rule.", target, details, args.as_json)
        if not c.get("failure_class"):
            return out(VIOL, "PRIVATE_CHECK_UNMAPPED", "Private check missing failure_class.", target, details, args.as_json)
        rule_text = str(public_rules.get(map_id, {}).get("text", "")).lower()
        declared = str(c.get("required_behavior", "")).lower()
        if declared and declared not in rule_text:
            return out(VIOL, "HIDDEN_REQUIREMENT_DETECTED", "Private check introduces hidden requirement.", target, details, args.as_json)
        details.append({"check_id": c.get("id"), "mapped_rule": map_id})

    return out(OK, None, "Private evaluator checks map to public rules.", target, details, args.as_json)


if __name__ == "__main__":
    sys.exit(main())
