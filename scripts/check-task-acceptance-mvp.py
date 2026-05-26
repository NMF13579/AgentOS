#!/usr/bin/env python3
import argparse
import json
from pathlib import Path, PurePosixPath
import re
import sys

RESULT_PASS = "TASK_VALIDATION_PASS"
RESULT_WARN = "TASK_VALIDATION_PASS_WITH_WARNINGS"
RESULT_BLOCKED = "TASK_VALIDATION_BLOCKED"
RESULT_NOT_ENOUGH = "TASK_VALIDATION_NOT_ENOUGH_EVIDENCE"

BLOCKING_FORBIDDEN_PHRASES = [
    "approval granted",
    "task completion approved",
    "human review not required",
    "human_review_required: false",
    "merge authorized",
    "push authorized",
    "release authorized",
    "deployment authorized",
    "lifecycle mutated",
    "m63 started",
    "m62 completed automatically",
    "task acceptance production gate",
    "production task validation gate",
    "task is approved",
    "completion approved",
    "merged",
    "released",
    "pushed",
    "approved",
]

FUTURE_MILESTONE_ARTIFACTS = {
    "schemas/task-result.schema.json",
    "schemas/agent-evidence.schema.json",
    "docs/TASK-VALIDATION-CONTRACT.md",
    "docs/TASK-OUTPUT-EVIDENCE-MODEL.md",
    "docs/ACCEPTANCE-CRITERIA-CHECKER.md",
    "scripts/check-agent-task-result.py",
    "scripts/check-task-acceptance.py",
}

FUTURE_MILESTONE_HINTS = ["/m63", "/m64", "/m65", "/m66", "/m67", "m63-", "m64-", "m65-", "m66-", "m67-"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Thin read-only MVP task acceptance runner")
    parser.add_argument("--task", required=True, help="Path to task brief file")
    parser.add_argument("--evidence", required=True, help="Path to evidence file")
    parser.add_argument("--changed-files", required=True, help="Path to changed-files JSON")
    parser.add_argument("--strict", action="store_true", help="Enable stricter checks")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    return parser.parse_args()


def new_payload(args: argparse.Namespace) -> dict:
    return {
        "result": RESULT_BLOCKED,
        "strict": bool(args.strict),
        "task_checked": False,
        "evidence_checked": False,
        "changed_files_checked": False,
        "expected_artifacts_checked": False,
        "forbidden_paths_checked": False,
        "forbidden_claims_checked": False,
        "future_milestone_artifacts_checked": False,
        "task_file": args.task,
        "evidence_file": args.evidence,
        "changed_files_file": args.changed_files,
        "changed_files": [],
        "human_review_required": True,
        "input_attempted_to_disable_human_review": False,
        "warnings": [],
        "blockers": [],
    }


def add_warning(payload: dict, msg: str) -> None:
    payload["warnings"].append(msg)


def add_blocker(payload: dict, msg: str) -> None:
    payload["blockers"].append(msg)


def add_not_enough_reason(reasons: list[str], msg: str) -> None:
    reasons.append(msg)


def read_text_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def normalize_repo_relative(raw_path: str) -> tuple[str | None, str | None]:
    candidate = raw_path.strip()
    if not candidate:
        return None, "empty path entry"
    if candidate.startswith("/"):
        return None, f"absolute path is forbidden: {raw_path}"
    if "\\" in candidate:
        candidate = candidate.replace("\\", "/")

    pure = PurePosixPath(candidate)
    parts = list(pure.parts)
    if any(p == ".." for p in parts):
        return None, f"path traversal is forbidden: {raw_path}"

    normalized = str(PurePosixPath(*parts))
    if normalized.startswith("./"):
        normalized = normalized[2:]
    if normalized == ".":
        return None, f"path is not a file path: {raw_path}"
    if normalized.startswith("../") or normalized == "..":
        return None, f"path resolves outside repository root: {raw_path}"
    if normalized.startswith("/"):
        return None, f"path resolves as absolute path: {raw_path}"

    return normalized, None


def parse_changed_files_json(path: Path, payload: dict) -> tuple[list[str], bool]:
    if not path.exists():
        add_blocker(payload, f"changed-files JSON missing: {path}")
        return [], False
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        add_blocker(payload, f"changed-files JSON malformed: {exc}")
        return [], False

    if "changed_files" not in data:
        add_blocker(payload, "changed-files JSON missing changed_files field")
        return [], False

    raw_files = data.get("changed_files")
    if not isinstance(raw_files, list):
        add_blocker(payload, "changed_files must be a list")
        return [], False

    normalized_files: list[str] = []
    for idx, item in enumerate(raw_files):
        if not isinstance(item, str):
            add_blocker(payload, f"changed_files[{idx}] must be a string")
            continue
        normalized, err = normalize_repo_relative(item)
        if err:
            add_blocker(payload, err)
            continue
        normalized_files.append(normalized)

    if payload["blockers"]:
        return normalized_files, False

    if not normalized_files:
        add_warning(payload, "changed_files is empty; allowed only for validation-only examples")

    payload["changed_files_checked"] = True
    payload["changed_files"] = normalized_files
    return normalized_files, True


def extract_task_id(text: str) -> str | None:
    patterns = [
        r"^\s*Task ID:\s*([^\n\r]+)",
        r"^\s*task_id:\s*([^\n\r]+)",
    ]
    for pat in patterns:
        m = re.search(pat, text, flags=re.IGNORECASE | re.MULTILINE)
        if m:
            return m.group(1).strip()
    return None


def extract_expected_artifacts(task_text: str) -> list[str]:
    artifacts: list[str] = []
    in_create_block = False
    for raw_line in task_text.splitlines():
        line = raw_line.strip()
        lower = line.lower()
        if lower.startswith("create:"):
            in_create_block = True
            tail = line.split(":", 1)[1].strip()
            if tail:
                artifacts.append(tail)
            continue
        if in_create_block:
            if not line:
                in_create_block = False
                continue
            if line.startswith("⸻") or re.match(r"^\d+\.", line):
                in_create_block = False
                continue
            if line.startswith("-"):
                candidate = line.lstrip("- ").strip()
            else:
                candidate = line
            if "/" in candidate or candidate.endswith(".md") or candidate.endswith(".py") or candidate.endswith(".json"):
                artifacts.append(candidate)

    seen = set()
    out = []
    for art in artifacts:
        norm, err = normalize_repo_relative(art)
        if err or norm is None:
            continue
        if norm not in seen:
            seen.add(norm)
            out.append(norm)
    return out


def extract_forbidden_paths(task_text: str) -> set[str]:
    forbidden: set[str] = set()
    patterns = [r"^\s*Do not create:\s*(.+)$", r"^\s*Do not modify:\s*(.+)$", r"^\s*Do not create, modify, delete, archive, or move any file except:\s*(.+)$"]
    for line in task_text.splitlines():
        stripped = line.strip()
        for pat in patterns:
            m = re.match(pat, stripped, flags=re.IGNORECASE)
            if m:
                candidate = m.group(1).strip()
                norm, err = normalize_repo_relative(candidate)
                if not err and norm:
                    forbidden.add(norm)
        if stripped.startswith("-"):
            item = stripped.lstrip("- ").strip()
            norm, err = normalize_repo_relative(item)
            if not err and norm and (
                norm in FUTURE_MILESTONE_ARTIFACTS
                or norm.startswith("docs/")
                or norm.startswith("scripts/")
                or norm.startswith("schemas/")
                or norm.startswith("reports/")
                or norm.startswith("tests/")
            ):
                if "Do not" in task_text[max(0, task_text.find(line)-200): task_text.find(line)+50]:
                    forbidden.add(norm)
    forbidden.update(FUTURE_MILESTONE_ARTIFACTS)
    return forbidden


def line_is_example_or_boundary(line: str, current_section: str) -> bool:
    lower = line.lower()
    section = current_section.lower()
    safe_section = any(k in section for k in ["non-authority", "forbidden", "example", "policy"])
    safe_line = any(k in lower for k in ["must not", "do not", "does not", "not approval", "forbidden", "example"])
    return safe_section or safe_line


def analyze_forbidden_claims(text: str, source_name: str) -> tuple[list[str], list[str], bool]:
    blockers: list[str] = []
    warnings: list[str] = []
    ambiguous = False
    current_section = ""

    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("#"):
            current_section = line.lstrip("# ")
            continue
        line_lower = line.lower()
        for phrase in BLOCKING_FORBIDDEN_PHRASES:
            if phrase in line_lower:
                if line_is_example_or_boundary(line, current_section):
                    warnings.append(f"forbidden phrase in example/boundary context ({source_name}): {phrase}")
                else:
                    negated = any(tok in line_lower for tok in ["not "+phrase, "no "+phrase, "without "+phrase])
                    if negated:
                        warnings.append(f"forbidden phrase in negated context ({source_name}): {phrase}")
                    else:
                        # Ambiguous if looks like quoted policy text
                        if line.startswith(">") or "\"" in line or "'" in line:
                            ambiguous = True
                        else:
                            blockers.append(f"forbidden claim detected ({source_name}): {phrase}")
    return blockers, warnings, ambiguous


def check_expected_artifacts(task_text: str, repo_root: Path, payload: dict, ne_reasons: list[str]) -> None:
    expected = extract_expected_artifacts(task_text)
    if not expected:
        add_not_enough_reason(ne_reasons, "expected artifacts cannot be determined from task file")
        payload["expected_artifacts_checked"] = False
        return

    missing = [p for p in expected if not (repo_root / p).exists()]
    if missing:
        add_blocker(payload, f"expected artifact missing: {', '.join(missing)}")
        payload["expected_artifacts_checked"] = False
        return

    payload["expected_artifacts_checked"] = True


def check_changed_files_forbidden(changed_files: list[str], forbidden_paths: set[str], payload: dict) -> None:
    hits = [p for p in changed_files if p in forbidden_paths]
    if hits:
        add_blocker(payload, f"forbidden path changed: {', '.join(sorted(set(hits)))}")
    payload["forbidden_paths_checked"] = True


def check_future_milestone_artifacts(changed_files: list[str], payload: dict) -> None:
    hits = []
    for p in changed_files:
        lower = p.lower()
        if p in FUTURE_MILESTONE_ARTIFACTS or any(h in lower for h in FUTURE_MILESTONE_HINTS):
            hits.append(p)
    if hits:
        add_blocker(payload, f"future milestone artifact in changed_files: {', '.join(sorted(set(hits)))}")
    payload["future_milestone_artifacts_checked"] = True


def finalize_result(payload: dict, not_enough_reasons: list[str]) -> int:
    if payload["input_attempted_to_disable_human_review"]:
        add_blocker(payload, "input attempted to disable required human review")

    if payload["blockers"]:
        payload["result"] = RESULT_BLOCKED
        return 1

    if not_enough_reasons:
        for r in not_enough_reasons:
            add_warning(payload, f"not-enough-evidence: {r}")
        payload["result"] = RESULT_NOT_ENOUGH
        return 1

    if payload["warnings"]:
        payload["result"] = RESULT_WARN
        return 0

    payload["result"] = RESULT_PASS
    return 0


def main() -> int:
    try:
        args = parse_args()
        payload = new_payload(args)
        not_enough_reasons: list[str] = []

        task_path = Path(args.task)
        evidence_path = Path(args.evidence)
        changed_files_path = Path(args.changed_files)

        # Required files must exist and be readable.
        if not task_path.exists():
            add_blocker(payload, f"task file missing: {task_path}")
            task_text = ""
        else:
            try:
                task_text = read_text_file(task_path)
                payload["task_checked"] = True
                if len(task_text.strip()) < 20:
                    add_not_enough_reason(not_enough_reasons, "task file text is too short for MVP extraction")
            except Exception as exc:
                task_text = ""
                add_blocker(payload, f"task file unreadable: {exc}")

        if not evidence_path.exists():
            add_blocker(payload, f"evidence file missing: {evidence_path}")
            evidence_text = ""
        else:
            try:
                evidence_text = read_text_file(evidence_path)
                payload["evidence_checked"] = True
            except Exception as exc:
                evidence_text = ""
                add_blocker(payload, f"evidence file unreadable: {exc}")

        changed_files, changed_ok = parse_changed_files_json(changed_files_path, payload)
        repo_root = Path(__file__).resolve().parent.parent

        task_id = extract_task_id(task_text) if task_text else None
        if task_text:
            forbidden_paths = extract_forbidden_paths(task_text)
            check_expected_artifacts(task_text, repo_root, payload, not_enough_reasons)
        else:
            forbidden_paths = set(FUTURE_MILESTONE_ARTIFACTS)

        if changed_ok:
            check_changed_files_forbidden(changed_files, forbidden_paths, payload)
            check_future_milestone_artifacts(changed_files, payload)

        # Evidence quality checks.
        if evidence_text:
            evidence_lower = evidence_text.lower()
            if "human_review_required: false" in evidence_lower or "human review not required" in evidence_lower or "human review can be skipped" in evidence_lower:
                payload["input_attempted_to_disable_human_review"] = True
            if "human_review_required: true" not in evidence_lower:
                add_not_enough_reason(not_enough_reasons, "evidence does not clearly assert human_review_required: true")

            if task_id and task_id.lower() not in evidence_lower:
                add_not_enough_reason(not_enough_reasons, "evidence does not correlate with task_id")
            if "summary_of_work" not in evidence_lower and "summary of work" not in evidence_lower:
                add_not_enough_reason(not_enough_reasons, "evidence missing summary_of_work")
            if "declared_changed_files" not in evidence_lower and "changed_files" not in evidence_lower:
                add_not_enough_reason(not_enough_reasons, "evidence missing declared_changed_files")
            if "declared_validation_commands" not in evidence_lower and "validation_commands" not in evidence_lower:
                add_not_enough_reason(not_enough_reasons, "evidence missing declared_validation_commands")
            if "known_limitations" in evidence_lower or "known limitations" in evidence_lower:
                add_warning(payload, "evidence declares known limitations")

            b, w, ambiguous = analyze_forbidden_claims(evidence_text, "evidence")
            for item in b:
                add_blocker(payload, item)
            for item in w:
                add_warning(payload, item)
            if ambiguous:
                add_not_enough_reason(not_enough_reasons, "cannot clearly distinguish forbidden claim from quoted/example evidence text")

        if task_text:
            b, w, ambiguous = analyze_forbidden_claims(task_text, "task")
            for item in b:
                add_blocker(payload, item)
            for item in w:
                add_warning(payload, item)
            if ambiguous:
                add_not_enough_reason(not_enough_reasons, "cannot clearly distinguish forbidden claim from example/policy text in task")

        payload["forbidden_claims_checked"] = True

        exit_code = finalize_result(payload, not_enough_reasons)

        if args.json:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            print(payload["result"])
            for w in payload["warnings"]:
                print(f"WARN: {w}")
            for b in payload["blockers"]:
                print(f"BLOCK: {b}")
        return exit_code

    except SystemExit:
        raise
    except Exception as exc:
        err = {
            "result": RESULT_BLOCKED,
            "strict": False,
            "task_checked": False,
            "evidence_checked": False,
            "changed_files_checked": False,
            "expected_artifacts_checked": False,
            "forbidden_paths_checked": False,
            "forbidden_claims_checked": False,
            "future_milestone_artifacts_checked": False,
            "task_file": "",
            "evidence_file": "",
            "changed_files_file": "",
            "changed_files": [],
            "human_review_required": True,
            "input_attempted_to_disable_human_review": False,
            "warnings": [],
            "blockers": [f"runner internal error: {exc}"],
        }
        print(json.dumps(err, ensure_ascii=False, indent=2))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
