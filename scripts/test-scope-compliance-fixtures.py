#!/usr/bin/env python3
import json
import subprocess
import sys
import os
from pathlib import Path
from tempfile import TemporaryDirectory


REQUIRED_JSON_KEYS = [
    "result",
    "changed_files_count",
    "violations_count",
    "warnings_count",
    "human_action_required",
    "changed_files",
    "violations",
    "warnings",
]

FIXTURES_ROOT_LITERAL = "tests/fixtures/scope-compliance"


def run(cmd, cwd):
    return subprocess.run(cmd, cwd=str(cwd), text=True, capture_output=True)


def ensure_parent(path):
    parent = path.parent
    if not parent.exists():
        parent.mkdir(parents=True, exist_ok=True)


def write_text(path, content):
    ensure_parent(path)
    path.write_text(content, encoding="utf-8")


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def discover_fixtures(fixtures_root):
    result = []
    for path in sorted(fixtures_root.rglob("fixture.json")):
        fixture_dir = path.parent
        task_path = fixture_dir / "task.md"
        if task_path.exists():
            result.append((fixture_dir, path, task_path))
    return result


def apply_operation(op, repo):
    action = op.get("action")
    if action == "write":
        rel = op.get("path")
        content = op.get("content", "")
        if not isinstance(rel, str):
            raise RuntimeError("write operation missing path")
        write_text(repo / rel, content)
        return
    if action == "delete":
        rel = op.get("path")
        if not isinstance(rel, str):
            raise RuntimeError("delete operation missing path")
        target = repo / rel
        if target.exists():
            target.unlink()
        return
    if action == "rename":
        rel_from = op.get("from")
        rel_to = op.get("to")
        if not isinstance(rel_from, str) or not isinstance(rel_to, str):
            raise RuntimeError("rename operation missing from/to")
        src = repo / rel_from
        dst = repo / rel_to
        ensure_parent(dst)
        src.rename(dst)
        return
    if action == "stage":
        rel = op.get("path")
        if rel == ".":
            proc = run(["git", "add", "-A"], repo)
        elif isinstance(rel, str):
            proc = run(["git", "add", rel], repo)
        else:
            raise RuntimeError("stage operation missing path")
        if proc.returncode != 0:
            raise RuntimeError("stage operation failed")
        return
    raise RuntimeError("unknown operation action")


def extract_human_result(text):
    for line in text.splitlines():
        if line.startswith("Scope Compliance:"):
            value = line.split(":", 1)[1].strip()
            if value in ["PASS", "FAIL", "WARN", "ERROR"]:
                return value
    return None


def setup_temp_repo(temp_repo, fixture, task_source):
    proc = run(["git", "init"], temp_repo)
    if proc.returncode != 0:
        raise RuntimeError("git init failed")

    proc = run(["git", "config", "user.email", "fixture@example.local"], temp_repo)
    if proc.returncode != 0:
        raise RuntimeError("git config user.email failed")
    proc = run(["git", "config", "user.name", "Fixture Runner"], temp_repo)
    if proc.returncode != 0:
        raise RuntimeError("git config user.name failed")

    for rel, content in fixture.get("initial_files", {}).items():
        write_text(temp_repo / rel, content)

    write_text(temp_repo / "task.md", task_source.read_text(encoding="utf-8"))
    proc = run(["git", "add", "-A"], temp_repo)
    if proc.returncode != 0:
        raise RuntimeError("baseline add failed")
    proc = run(["git", "commit", "-m", "baseline"], temp_repo)
    if proc.returncode != 0:
        raise RuntimeError("baseline commit failed")


def run_fixture(fixture_dir, fixture_json_path, task_path, repo_root, validator_path):
    fixture = load_json(fixture_json_path)
    expected_result = fixture.get("expected_result")
    expected_exit_code = fixture.get("expected_exit_code")

    if expected_result not in ["PASS", "FAIL", "WARN", "ERROR"]:
        return {
            "status": "ERROR",
            "fixture": str(fixture_dir),
            "message": "invalid expected_result",
        }
    if not isinstance(expected_exit_code, int):
        return {
            "status": "ERROR",
            "fixture": str(fixture_dir),
            "message": "invalid expected_exit_code",
        }

    with TemporaryDirectory(prefix="scope-fixture-") as tmp:
        temp_repo = Path(tmp)

        try:
            setup_temp_repo(temp_repo, fixture, task_path)

            for op in fixture.get("operations", []):
                apply_operation(op, temp_repo)

            human_cmd = [
                sys.executable,
                str(validator_path),
                "--repo-root",
                str(temp_repo),
                "--task",
                str(temp_repo / "task.md"),
            ]
            human_proc = run(human_cmd, repo_root)
            human_result = extract_human_result(human_proc.stdout)

            json_cmd = human_cmd + ["--json"]
            json_proc = run(json_cmd, repo_root)

            parsed_json = None
            json_result = None
            json_ok = False
            try:
                parsed_json = json.loads(json_proc.stdout)
                json_ok = True
                json_result = parsed_json.get("result")
            except Exception:
                json_ok = False

            json_keys_ok = False
            if json_ok:
                json_keys_ok = True
                for key in REQUIRED_JSON_KEYS:
                    if key not in parsed_json:
                        json_keys_ok = False
                        break

            ok = True
            if human_proc.returncode != expected_exit_code:
                ok = False
            if human_result != expected_result:
                ok = False
            if json_proc.returncode != expected_exit_code:
                ok = False
            if json_result != expected_result:
                ok = False
            if not json_ok or not json_keys_ok:
                ok = False

            return {
                "status": "PASS" if ok else "FAIL",
                "fixture": str(fixture_dir),
                "expected_result": expected_result,
                "actual_result": human_result,
                "expected_exit_code": expected_exit_code,
                "actual_exit_code": human_proc.returncode,
                "json_result": json_result,
                "json_exit_code": json_proc.returncode,
                "human_stdout": human_proc.stdout,
                "human_stderr": human_proc.stderr,
                "json_stdout": json_proc.stdout,
                "json_stderr": json_proc.stderr,
                "json_keys_ok": json_keys_ok,
            }
        except Exception as exc:
            return {
                "status": "ERROR",
                "fixture": str(fixture_dir),
                "message": str(exc),
            }


def main():
    repo_root = Path(__file__).resolve().parent.parent
    fixtures_root = repo_root / FIXTURES_ROOT_LITERAL
    validator_path = repo_root / "scripts" / "check-scope-compliance.py"

    if not fixtures_root.exists() or not validator_path.exists():
        print("Scope Compliance Fixtures: ERROR")
        print("Fixtures total: 0")
        print("Fixtures passed: 0")
        print("Fixtures failed: 0")
        return 3

    fixtures = discover_fixtures(fixtures_root)
    if not fixtures:
        print("Scope Compliance Fixtures: ERROR")
        print("Fixtures total: 0")
        print("Fixtures passed: 0")
        print("Fixtures failed: 0")
        return 3

    results = []
    had_error = False
    for fixture_dir, fixture_json_path, task_path in fixtures:
        res = run_fixture(fixture_dir, fixture_json_path, task_path, repo_root, validator_path)
        results.append(res)
        if res["status"] == "ERROR":
            had_error = True

    total = len(results)
    passed = sum(1 for r in results if r.get("status") == "PASS")
    failed = sum(1 for r in results if r.get("status") in ["FAIL", "ERROR"])

    overall = "PASS"
    if had_error:
        overall = "ERROR"
    elif failed > 0:
        overall = "FAIL"

    print(f"Scope Compliance Fixtures: {overall}")
    print(f"Fixtures total: {total}")
    print(f"Fixtures passed: {passed}")
    print(f"Fixtures failed: {failed}")

    for res in results:
        if res["status"] == "ERROR":
            print(f"[ERROR] {res['fixture']}")
            print("expected_result: ERROR")
            print("actual_result: ERROR")
            print("expected_exit_code: 3")
            print("actual_exit_code: 3")
            print("json_result: ERROR")
            print("json_exit_code: 3")
            print(f"message: {res.get('message', '')}")
            continue

        print(f"[{res['status']}] {res['fixture']}")
        print(f"expected_result: {res['expected_result']}")
        print(f"actual_result: {res['actual_result']}")
        print(f"expected_exit_code: {res['expected_exit_code']}")
        print(f"actual_exit_code: {res['actual_exit_code']}")
        print(f"json_result: {res['json_result']}")
        print(f"json_exit_code: {res['json_exit_code']}")

    if overall == "PASS":
        return 0
    if overall == "FAIL":
        return 1
    return 3


if __name__ == "__main__":
    sys.exit(main())
