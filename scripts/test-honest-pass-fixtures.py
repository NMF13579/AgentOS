#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
import subprocess
import sys

OK = "HONEST_PASS_FIXTURES_OK"
FAILED = "HONEST_PASS_FIXTURES_FAILED"
NEEDS_REVIEW = "HONEST_PASS_FIXTURES_NEEDS_REVIEW"

MAPPING = [
    ("tests/fixtures/private-evaluator", "scripts/check-private-evaluator-consistency.py"),
    ("tests/fixtures/canary-integrity", "scripts/check-canary-integrity.py"),
    ("tests/fixtures/process-trace", "scripts/check-process-trace.py"),
    ("tests/fixtures/evidence-binding", "scripts/check-evidence-binding.py"),
]

EXPECTED = {
    "positive": ("HONEST_PASS_OK", 0),
    "negative": ("HONEST_PASS_VIOLATION", 1),
    "needs-review": ("HONEST_PASS_NEEDS_REVIEW", 1),
}


def run_case(checker, fixture):
    proc = subprocess.run(
        [sys.executable, checker, str(fixture), "--json"],
        capture_output=True,
        text=True,
        check=False,
    )
    try:
        payload = json.loads(proc.stdout.strip())
    except Exception:
        return False, {"fixture": str(fixture), "error": "invalid_json", "stdout": proc.stdout[:200]}

    kind = fixture.parent.name
    exp_token, exp_code = EXPECTED[kind]
    got_token = payload.get("result")
    ok = (proc.returncode == exp_code) and (got_token == exp_token)
    return ok, {
        "fixture": str(fixture),
        "expected_token": exp_token,
        "expected_code": exp_code,
        "got_token": got_token,
        "got_code": proc.returncode,
    }


def main():
    ap = argparse.ArgumentParser(description="Run Honest PASS fixtures.")
    ap.add_argument("--json", action="store_true", dest="as_json")
    args = ap.parse_args()

    all_results = []
    failures = []

    for base, checker in MAPPING:
        root = Path(base)
        for kind in ["positive", "negative", "needs-review"]:
            d = root / kind
            if not d.exists():
                continue
            for fixture in sorted([p for p in d.iterdir() if p.is_dir()]):
                ok, rec = run_case(checker, fixture)
                all_results.append(rec)
                if not ok:
                    failures.append(rec)

    if failures:
        token = FAILED
        code = 1
    else:
        token = OK
        code = 0

    payload = {
        "suite": "honest-pass-fixtures",
        "result": token,
        "cases": all_results,
        "failed_cases": failures,
    }

    if args.as_json:
        print(json.dumps(payload, ensure_ascii=True))
    else:
        print(f"{token}: total={len(all_results)} failed={len(failures)}")

    return code


if __name__ == "__main__":
    sys.exit(main())
