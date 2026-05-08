#!/usr/bin/env python3
"""Build and check M28 generated context index."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

import yaml

RESULT_BUILT = "CONTEXT_INDEX_BUILT"
RESULT_OK = "CONTEXT_INDEX_OK"
RESULT_STALE = "CONTEXT_INDEX_STALE"
RESULT_INVALID = "CONTEXT_INDEX_INVALID"
RESULT_NEEDS_REVIEW = "CONTEXT_INDEX_NEEDS_REVIEW"

EXIT_BY_RESULT = {
    RESULT_BUILT: 0,
    RESULT_OK: 0,
    RESULT_STALE: 1,
    RESULT_INVALID: 1,
    RESULT_NEEDS_REVIEW: 1,
}

SCHEMA_VERSION = "1.0.0"
GENERATOR = "scripts/build-context-index.py"
GENERATOR_VERSION = "0.1.0"
INDEX_REL_PATH = Path("data/context-index.json")
SCHEMA_REL_PATH = Path("schemas/context-index.schema.json")
SOURCE_INDEX_REL_PATH = Path("data/index.json")
HASH_PATTERN_PREFIX = "sha256:"

ELIGIBLE_EXTENSIONS = {".md", ".yaml", ".yml"}
EXCLUDED_PARTS = {
    ".git",
    ".agentos",
    "node_modules",
    ".venv",
    "venv",
    "__pycache__",
    "tests",
}

REQUIRED_FIELDS = (
    "type",
    "module",
    "status",
    "authority",
    "created",
    "last_validated",
    "tags",
    "context_role",
    "summary",
)

OPTIONAL_FIELDS = (
    "applies_to",
    "excludes",
    "owner",
    "version",
    "related_tasks",
    "related_lessons",
)

GENERATED_METADATA_KEYS = {
    "source_hash",
    "repo_commit_hash",
    "generated_at",
    "indexed_at",
    "generator_version",
    "source_index_hash",
}

NONCRITICAL_PREFIXES = (
    "missing_frontmatter:",
    "missing_or_invalid_field:",
    "invalid_frontmatter_yaml:",
    "proof:",
)

ALLOWED_TYPES = {
    "policy",
    "spec",
    "lesson",
    "decision",
    "task",
    "report",
    "template",
    "doc",
    "guide",
    "architecture",
}
ALLOWED_STATUS = {"draft", "active", "canonical", "archived", "deprecated"}
ALLOWED_AUTHORITY = {"canonical", "supporting", "context"}
ALLOWED_CONTEXT_ROLE = {"required_when_relevant", "supporting", "optional", "exclude_by_default"}


@dataclass
class BuildReport:
    result: str
    index_path: str
    entries_count: int
    warnings: list[str]
    errors: list[str]
    skipped_files: list[str]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build M28 data/context-index.json from context frontmatter.")
    parser.add_argument("--check", action="store_true", help="Validate existing index and freshness without rewriting.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON result.")
    parser.add_argument("--root", default=".", help="Repository root path.")
    return parser.parse_args(argv)


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_text(text: str) -> str:
    return HASH_PATTERN_PREFIX + hashlib.sha256(text.encode("utf-8")).hexdigest()


def is_excluded(rel_path: Path) -> bool:
    parts = set(rel_path.parts)
    if parts & EXCLUDED_PARTS:
        return True
    return rel_path.as_posix() == INDEX_REL_PATH.as_posix()


def find_eligible_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(root)
        if is_excluded(rel):
            continue
        if p.suffix.lower() in ELIGIBLE_EXTENSIONS:
            files.append(p)
    return sorted(files, key=lambda p: p.relative_to(root).as_posix())


def parse_markdown_frontmatter(text: str) -> tuple[dict[str, Any] | None, str | None]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, "missing_frontmatter"
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None, "missing_frontmatter_closing_delimiter"
    block = "\n".join(lines[1:end])
    try:
        data = yaml.safe_load(block)
    except Exception as exc:  # pragma: no cover
        return None, f"invalid_frontmatter_yaml:{exc}"
    if not isinstance(data, dict):
        return None, "frontmatter_not_object"
    return data, None


def parse_source_metadata(path: Path) -> tuple[dict[str, Any] | None, str | None]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".md":
        return parse_markdown_frontmatter(text)
    try:
        data = yaml.safe_load(text)
    except Exception as exc:
        return None, f"invalid_yaml:{exc}"
    if not isinstance(data, dict):
        return None, "yaml_not_object"
    return data, None


def require_string(metadata: dict[str, Any], field: str, issues: list[str], rel_path: str) -> str | None:
    value = metadata.get(field)
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if not isinstance(value, str) or not value.strip():
        issues.append(f"{rel_path}:missing_or_invalid_field:{field}")
        return None
    return value.strip()


def normalize_string_array(value: Any, field: str, issues: list[str], rel_path: str) -> list[str] | None:
    if not isinstance(value, list) or not all(isinstance(x, str) for x in value):
        issues.append(f"{rel_path}:missing_or_invalid_field:{field}")
        return None
    return value


def validate_allowed_values(entry: dict[str, Any], issues: list[str], rel_path: str) -> None:
    if entry["type"] not in ALLOWED_TYPES:
        issues.append(f"{rel_path}:invalid_type:{entry['type']}")
    if entry["status"] not in ALLOWED_STATUS:
        issues.append(f"{rel_path}:invalid_status:{entry['status']}")
    if entry["authority"] not in ALLOWED_AUTHORITY:
        issues.append(f"{rel_path}:invalid_authority:{entry['authority']}")
    if entry["context_role"] not in ALLOWED_CONTEXT_ROLE:
        issues.append(f"{rel_path}:invalid_context_role:{entry['context_role']}")


def git_head_commit(root: Path) -> tuple[str | None, str | None]:
    try:
        proc = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=str(root),
            check=False,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        return None, "git_not_found"
    if proc.returncode != 0:
        return None, "git_rev_parse_failed"
    value = proc.stdout.strip()
    if not value:
        return None, "git_head_empty"
    return value, None


def build_index_document(root: Path) -> tuple[dict[str, Any] | None, list[str], list[str], list[str]]:
    warnings: list[str] = []
    errors: list[str] = []
    skipped_counts: dict[str, int] = {}
    skipped_examples: dict[str, str] = {}

    def add_skip(reason: str, rel_path: str) -> None:
        skipped_counts[reason] = skipped_counts.get(reason, 0) + 1
        skipped_examples.setdefault(reason, rel_path)

    repo_commit_hash, git_err = git_head_commit(root)
    if git_err or repo_commit_hash is None:
        errors.append("repo_commit_hash_unavailable")
        warnings.append(f"warning:{git_err or 'unknown_git_error'}")
        return None, warnings, errors, []

    indexed_at = now_utc()
    entries: list[dict[str, Any]] = []

    for path in find_eligible_files(root):
        rel_path = path.relative_to(root).as_posix()
        metadata, parse_issue = parse_source_metadata(path)
        if parse_issue:
            add_skip(parse_issue, rel_path)
            continue
        assert metadata is not None

        entry_warnings: list[str] = []

        # Detect fields that should never be semantic frontmatter.
        bad_generated_keys = sorted(k for k in metadata.keys() if k in GENERATED_METADATA_KEYS)
        if bad_generated_keys:
            entry_warnings.append(
                "generated_metadata_in_frontmatter:" + ",".join(bad_generated_keys)
            )
            warnings.append(f"{rel_path}:generated_metadata_in_frontmatter")

        if "risk_level" in metadata:
            entry_warnings.append("unsupported_field:risk_level")
            warnings.append(f"{rel_path}:unsupported_field:risk_level")

        field_issues: list[str] = []
        entry: dict[str, Any] = {}
        for field in ("type", "module", "status", "authority", "created", "last_validated", "context_role", "summary"):
            value = require_string(metadata, field, field_issues, rel_path)
            if value is not None:
                entry[field] = value

        tags = normalize_string_array(metadata.get("tags"), "tags", field_issues, rel_path)
        if tags is not None:
            entry["tags"] = tags

        if field_issues:
            for issue in field_issues:
                _, reason = issue.split(":", 1)
                add_skip(reason, rel_path)
            continue

        for field in OPTIONAL_FIELDS:
            if field not in metadata:
                continue
            value = metadata[field]
            if field in {"applies_to", "excludes", "related_tasks", "related_lessons"}:
                arr = normalize_string_array(value, field, field_issues, rel_path)
                if arr is not None:
                    entry[field] = arr
            else:
                if isinstance(value, str):
                    entry[field] = value
                else:
                    add_skip(f"invalid_optional_field:{field}", rel_path)

        if field_issues:
            for issue in field_issues:
                _, reason = issue.split(":", 1)
                add_skip(reason, rel_path)
            continue

        validate_allowed_values(entry, field_issues, rel_path)
        if field_issues:
            for issue in field_issues:
                _, reason = issue.split(":", 1)
                add_skip(reason, rel_path)
            continue

        source_hash = sha256_text(path.read_text(encoding="utf-8"))
        entry_out: dict[str, Any] = {
            "path": rel_path,
            "type": entry["type"],
            "module": entry["module"],
            "status": entry["status"],
            "authority": entry["authority"],
            "created": entry["created"],
            "last_validated": entry["last_validated"],
            "tags": entry["tags"],
            "context_role": entry["context_role"],
            "summary": entry["summary"],
            "source_hash": source_hash,
            "indexed_at": indexed_at,
        }
        for field in OPTIONAL_FIELDS:
            if field in entry:
                entry_out[field] = entry[field]
        if entry_warnings:
            entry_out["warnings"] = sorted(entry_warnings)
        entries.append(entry_out)

    entries = sorted(entries, key=lambda e: e["path"])

    source_index_path: str | None = None
    source_index_hash: str | None = None
    source_index_file = root / SOURCE_INDEX_REL_PATH
    if source_index_file.exists():
        source_index_path = SOURCE_INDEX_REL_PATH.as_posix()
        source_index_hash = sha256_text(source_index_file.read_text(encoding="utf-8"))

    doc: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": indexed_at,
        "generator": GENERATOR,
        "generator_version": GENERATOR_VERSION,
        "repo_commit_hash": repo_commit_hash,
        "source_index_path": source_index_path,
        "source_index_hash": source_index_hash,
        "entries": entries,
    }
    skipped_files = [
        f"{reason}:count={count}:example={skipped_examples.get(reason, '-')}"
        for reason, count in sorted(skipped_counts.items())
    ]
    return doc, warnings, errors, skipped_files


def validate_schema_if_possible(index_doc: dict[str, Any], root: Path) -> tuple[bool | None, list[str], list[str]]:
    warnings: list[str] = []
    errors: list[str] = []
    schema_path = root / SCHEMA_REL_PATH
    if not schema_path.exists():
        errors.append("schema_missing")
        return False, warnings, errors
    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"schema_invalid_json:{exc}")
        return False, warnings, errors

    try:
        import jsonschema  # type: ignore
    except Exception:
        warnings.append("jsonschema_unavailable")
        return None, warnings, errors

    try:
        jsonschema.validate(index_doc, schema)  # type: ignore[attr-defined]
    except Exception as exc:
        errors.append(f"schema_validation_failed:{exc}")
        return False, warnings, errors
    return True, warnings, errors


def write_index(root: Path, index_doc: dict[str, Any]) -> None:
    out_path = root / INDEX_REL_PATH
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(index_doc, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def read_existing_index(root: Path) -> tuple[dict[str, Any] | None, list[str]]:
    issues: list[str] = []
    p = root / INDEX_REL_PATH
    if not p.exists():
        issues.append("context_index_missing")
        return None, issues
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception as exc:
        issues.append(f"context_index_invalid_json:{exc}")
        return None, issues
    if not isinstance(data, dict):
        issues.append("context_index_not_object")
        return None, issues
    return data, issues


def check_mode(root: Path) -> BuildReport:
    warnings: list[str] = []
    errors: list[str] = []
    skipped_files: list[str] = []

    existing, read_issues = read_existing_index(root)
    if read_issues:
        return BuildReport(
            result=RESULT_INVALID,
            index_path=INDEX_REL_PATH.as_posix(),
            entries_count=0,
            warnings=warnings,
            errors=read_issues,
            skipped_files=skipped_files,
        )
    assert existing is not None

    schema_ok, schema_warnings, schema_errors = validate_schema_if_possible(existing, root)
    warnings.extend(schema_warnings)
    errors.extend(schema_errors)

    stale_reasons: list[str] = []
    rebuilt, build_warnings, build_errors, build_skips = build_index_document(root)
    warnings.extend(build_warnings)
    skipped_files.extend(build_skips)
    if build_errors:
        errors.extend(build_errors)
        return BuildReport(
            result=RESULT_NEEDS_REVIEW,
            index_path=INDEX_REL_PATH.as_posix(),
            entries_count=len(existing.get("entries", [])) if isinstance(existing.get("entries"), list) else 0,
            warnings=warnings,
            errors=errors,
            skipped_files=skipped_files,
        )
    assert rebuilt is not None

    if existing.get("repo_commit_hash") != rebuilt.get("repo_commit_hash"):
        stale_reasons.append("repo_commit_hash_mismatch")

    existing_entries = existing.get("entries")
    rebuilt_entries = rebuilt.get("entries")
    if not isinstance(existing_entries, list):
        errors.append("entries_missing_or_invalid")
    elif not isinstance(rebuilt_entries, list):
        errors.append("rebuilt_entries_invalid")
    else:
        ex_map = {e.get("path"): e for e in existing_entries if isinstance(e, dict) and "path" in e}
        rb_map = {e.get("path"): e for e in rebuilt_entries if isinstance(e, dict) and "path" in e}
        if set(ex_map.keys()) != set(rb_map.keys()):
            stale_reasons.append("entry_path_set_changed")
        for p, rb_entry in rb_map.items():
            ex_entry = ex_map.get(p)
            if not isinstance(ex_entry, dict):
                stale_reasons.append(f"missing_entry:{p}")
                continue
            if ex_entry.get("source_hash") != rb_entry.get("source_hash"):
                stale_reasons.append(f"source_hash_mismatch:{p}")

    source_index_path = existing.get("source_index_path")
    source_index_hash = existing.get("source_index_hash")
    if source_index_path:
        source_index_file = root / str(source_index_path)
        if source_index_file.exists():
            actual = sha256_text(source_index_file.read_text(encoding="utf-8"))
            if source_index_hash != actual:
                stale_reasons.append("source_index_hash_mismatch")
        else:
            stale_reasons.append("source_index_missing")

    if schema_ok is False:
        return BuildReport(
            result=RESULT_INVALID,
            index_path=INDEX_REL_PATH.as_posix(),
            entries_count=len(existing_entries) if isinstance(existing_entries, list) else 0,
            warnings=warnings,
            errors=errors,
            skipped_files=skipped_files,
        )

    if stale_reasons:
        return BuildReport(
            result=RESULT_STALE,
            index_path=INDEX_REL_PATH.as_posix(),
            entries_count=len(existing_entries) if isinstance(existing_entries, list) else 0,
            warnings=warnings,
            errors=errors + stale_reasons,
            skipped_files=skipped_files,
        )

    if schema_ok is None:
        warnings.append("schema_validation_skipped")
        return BuildReport(
            result=RESULT_NEEDS_REVIEW,
            index_path=INDEX_REL_PATH.as_posix(),
            entries_count=len(existing_entries) if isinstance(existing_entries, list) else 0,
            warnings=warnings,
            errors=errors,
            skipped_files=skipped_files,
        )

    return BuildReport(
        result=RESULT_OK,
        index_path=INDEX_REL_PATH.as_posix(),
        entries_count=len(existing_entries) if isinstance(existing_entries, list) else 0,
        warnings=warnings,
        errors=errors,
        skipped_files=skipped_files,
    )


def build_mode(root: Path) -> BuildReport:
    doc, warnings, errors, skipped_files = build_index_document(root)
    if errors or doc is None:
        return BuildReport(
            result=RESULT_NEEDS_REVIEW,
            index_path=INDEX_REL_PATH.as_posix(),
            entries_count=0,
            warnings=warnings,
            errors=errors,
            skipped_files=skipped_files,
        )

    schema_ok, schema_warnings, schema_errors = validate_schema_if_possible(doc, root)
    warnings.extend(schema_warnings)
    errors.extend(schema_errors)

    if schema_ok is False:
        return BuildReport(
            result=RESULT_INVALID,
            index_path=INDEX_REL_PATH.as_posix(),
            entries_count=len(doc.get("entries", [])),
            warnings=warnings,
            errors=errors,
            skipped_files=skipped_files,
        )

    write_index(root, doc)
    if schema_ok is None:
        warnings.append("schema_validation_skipped")
        return BuildReport(
            result=RESULT_NEEDS_REVIEW,
            index_path=INDEX_REL_PATH.as_posix(),
            entries_count=len(doc.get("entries", [])),
            warnings=warnings,
            errors=errors,
            skipped_files=skipped_files,
        )

    # Needs review if risky frontmatter patterns were detected.
    if any("generated_metadata_in_frontmatter" in w for w in warnings):
        return BuildReport(
            result=RESULT_NEEDS_REVIEW,
            index_path=INDEX_REL_PATH.as_posix(),
            entries_count=len(doc.get("entries", [])),
            warnings=warnings,
            errors=errors,
            skipped_files=skipped_files,
        )

    return BuildReport(
        result=RESULT_BUILT,
        index_path=INDEX_REL_PATH.as_posix(),
        entries_count=len(doc.get("entries", [])),
        warnings=warnings,
        errors=errors,
        skipped_files=skipped_files,
    )


def print_report(report: BuildReport, as_json: bool) -> None:
    payload = {
        "result": report.result,
        "index_path": report.index_path,
        "entries_count": report.entries_count,
        "warnings": report.warnings,
        "errors": report.errors,
        "skipped_files": report.skipped_files,
    }
    if as_json:
        print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
        return
    print(report.result)
    print(f"index_path={report.index_path}")
    print(f"entries_count={report.entries_count}")
    if report.warnings:
        print("warnings:")
        for w in report.warnings:
            print(f"- {w}")
    if report.errors:
        print("errors:")
        for e in report.errors:
            print(f"- {e}")
    if report.skipped_files:
        print("skipped_files:")
        for item in report.skipped_files:
            print(f"- {item}")


def is_missing_frontmatter_only(report: BuildReport) -> bool:
    if report.result != RESULT_NEEDS_REVIEW:
        return False
    if report.errors:
        return False
    if not report.skipped_files:
        return False
    for item in report.skipped_files:
        if not any(item.startswith(p) for p in NONCRITICAL_PREFIXES):
            return False
    return True


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    root = Path(args.root).resolve()
    if not root.exists() or not root.is_dir():
        report = BuildReport(
            result=RESULT_INVALID,
            index_path=INDEX_REL_PATH.as_posix(),
            entries_count=0,
            warnings=[],
            errors=[f"invalid_root:{root}"],
            skipped_files=[],
        )
        print_report(report, as_json=args.json)
        return EXIT_BY_RESULT[report.result]

    report = check_mode(root) if args.check else build_mode(root)

    if is_missing_frontmatter_only(report):
        report.warnings.append("missing_frontmatter_only_non_critical")
        print_report(report, as_json=args.json)
        return 0

    print_report(report, as_json=args.json)
    return EXIT_BY_RESULT[report.result]


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
