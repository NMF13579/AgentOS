#!/usr/bin/env python3
"""Read-only audit of M28 context layer structure."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

CONTEXT_LAYER_READY = "CONTEXT_LAYER_READY"
CONTEXT_LAYER_READY_WITH_WARNINGS = "CONTEXT_LAYER_READY_WITH_WARNINGS"
CONTEXT_LAYER_NOT_READY = "CONTEXT_LAYER_NOT_READY"
CONTEXT_LAYER_NEEDS_REVIEW = "CONTEXT_LAYER_NEEDS_REVIEW"

EXIT = {
    CONTEXT_LAYER_READY: 0,
    CONTEXT_LAYER_READY_WITH_WARNINGS: 1,
    CONTEXT_LAYER_NOT_READY: 1,
    CONTEXT_LAYER_NEEDS_REVIEW: 1,
}

REQUIRED_FILES = [
    "docs/M28-HYBRID-RAG-LIGHT-ARCHITECTURE.md",
    "docs/M28-CONTEXT-FRONTMATTER-STANDARD.md",
    "docs/M28-CONTEXT-INDEX-SCHEMA.md",
    "docs/M28-CONTEXT-PACK.md",
    "docs/M28-CONTEXT-REQUIRED.md",
    "docs/M28-CONTEXT-COMPLIANCE.md",
    "docs/M28-CONTEXT-AWARE-VERIFICATION.md",
    "docs/M28-LESSONS-FEEDBACK-LOOP.md",
    "schemas/context-index.schema.json",
    "templates/context-frontmatter-example.md",
    "templates/context-pack.md",
    "templates/context-selection-record.md",
    "templates/context-verification-record.md",
    "templates/lesson-candidate-record.md",
    "scripts/build-context-index.py",
    "scripts/select-context.py",
    "scripts/check-context-required.py",
    "scripts/check-context-compliance.py",
    "data/context-index.json",
]

CORE_BOUNDARY_STRINGS = [
    "M28 = context control",
    "Markdown/YAML = Semantic Source of Truth",
    "Context Pack is not approval",
    "M28 does not replace M27",
    "Human Gate remains approval authority",
]

NON_CRITICAL_BOUNDARY_STRINGS = [
    "SQLite is optional",
    "no vector db",
    "no embeddings",
    "no backend",
]

FORBIDDEN_CLAIMS = [
    "context pack approves execution",
    "context pack authorizes commit",
    "context pack authorizes push",
    "context pack authorizes merge",
    "context pack authorizes release",
    "context pack authorizes deployment",
    "context compliance approves execution",
    "verification approves protected actions",
    "lesson candidate updates canonical rules automatically",
    "sqlite is source of truth",
    "generated json is semantic source of truth",
    "m28 replaces m27",
    "m28 replaces human gate",
]

ALLOWED_NEGATIONS = [
    "does not",
    "is not",
    "must not",
]


@dataclass
class Finding:
    severity: str
    category: str
    message: str
    path: str


def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Audit M28 context layer readiness (read-only).")
    p.add_argument("--json", action="store_true")
    p.add_argument("--root", default=".")
    return p.parse_args(argv)


def combine_result(current: str, new: str) -> str:
    rank = {
        CONTEXT_LAYER_READY: 0,
        CONTEXT_LAYER_READY_WITH_WARNINGS: 1,
        CONTEXT_LAYER_NEEDS_REVIEW: 2,
        CONTEXT_LAYER_NOT_READY: 3,
    }
    return new if rank[new] > rank[current] else current


def add(f: list[Finding], severity: str, category: str, message: str, path: str) -> None:
    f.append(Finding(severity, category, message, path))


def has_text(text: str, needle: str) -> bool:
    return needle.lower() in text.lower()

def has_any(text: str, needles: list[str]) -> bool:
    low = text.lower()
    return any(n.lower() in low for n in needles)


def load_text(root: Path, rel: str) -> str:
    return (root / rel).read_text(encoding="utf-8", errors="ignore")


def find_forbidden_claims(text: str) -> list[str]:
    found: list[str] = []
    lines = text.splitlines()
    for ln in lines:
        low = ln.lower()
        for phrase in FORBIDDEN_CLAIMS:
            if phrase in low:
                # false-positive protection for negated statements
                if any(neg in low for neg in ALLOWED_NEGATIONS):
                    continue
                found.append(phrase)
    return sorted(set(found))


def check_required_files(root: Path, findings: list[Finding]) -> tuple[str, int, list[str]]:
    result = CONTEXT_LAYER_READY
    missing: list[str] = []
    checked = 0
    for rel in REQUIRED_FILES:
        p = root / rel
        checked += 1
        if not p.exists():
            missing.append(rel)
            add(findings, "error", "artifact_missing", f"required artifact missing: {rel}", rel)
            result = CONTEXT_LAYER_NOT_READY
            continue
        if p.stat().st_size == 0:
            add(findings, "error", "artifact_empty", f"required artifact exists but is empty: {rel}", rel)
            result = CONTEXT_LAYER_NOT_READY
        else:
            add(findings, "info", "artifact_present", f"{rel} exists", rel)
    return result, checked, missing


def check_schema(root: Path, findings: list[Finding]) -> str:
    rel = "schemas/context-index.schema.json"
    p = root / rel
    result = CONTEXT_LAYER_READY
    try:
        doc = json.loads(p.read_text(encoding="utf-8"))
    except Exception as exc:
        add(findings, "error", "invalid_json", f"schema json parse failed: {exc}", rel)
        return CONTEXT_LAYER_NOT_READY

    schema_uri = str(doc.get("$schema", ""))
    if not schema_uri:
        add(findings, "warning", "schema_missing_field", "$schema is missing", rel)
        result = combine_result(result, CONTEXT_LAYER_READY_WITH_WARNINGS)
    elif "draft-07" not in schema_uri and "json-schema.org/draft-07" not in schema_uri:
        add(findings, "needs_review", "schema_missing_field", "$schema is not draft-07", rel)
        result = combine_result(result, CONTEXT_LAYER_NEEDS_REVIEW)

    top_props = doc.get("properties", {}) if isinstance(doc.get("properties"), dict) else {}
    for key in ["repo_commit_hash", "generated_at", "source_index_hash", "entries", "generator_version"]:
        if key not in top_props:
            add(findings, "error", "schema_missing_field", f"schema missing key field: {key}", rel)
            result = CONTEXT_LAYER_NOT_READY

    if doc.get("additionalProperties") is not False:
        add(findings, "error", "schema_missing_field", "top-level additionalProperties must be false", rel)
        result = CONTEXT_LAYER_NOT_READY

    entries = top_props.get("entries", {})
    entry_items = entries.get("items", {}) if isinstance(entries, dict) else {}
    if entry_items.get("additionalProperties") is not False:
        add(findings, "error", "schema_missing_field", "entry-level additionalProperties must be false", rel)
        result = CONTEXT_LAYER_NOT_READY

    entry_props = entry_items.get("properties", {}) if isinstance(entry_items.get("properties"), dict) else {}
    if "source_hash" not in entry_props:
        add(findings, "error", "schema_missing_field", "entry missing source_hash", rel)
        result = CONTEXT_LAYER_NOT_READY

    return result


def check_text_requirements(root: Path, findings: list[Finding]) -> str:
    result = CONTEXT_LAYER_READY

    architecture_text = (
        load_text(root, "docs/M28-HYBRID-RAG-LIGHT-ARCHITECTURE.md")
        + "\n"
        + load_text(root, "docs/M28-CONTEXT-PACK.md")
        + "\n"
        + load_text(root, "docs/M28-CONTEXT-COMPLIANCE.md")
    )
    for s in CORE_BOUNDARY_STRINGS:
        variants = [s]
        if s == "M28 does not replace M27":
            variants.append("M28 must not become runtime authority")
        if s == "Human Gate remains approval authority":
            variants.append("Context Pack does not replace Human Gate approval")
            variants.append("Human review is required before promotion")
        if not has_any(architecture_text, variants):
            add(findings, "error", "required_text_missing", f"missing core architecture boundary statement: {s}", "docs/M28-HYBRID-RAG-LIGHT-ARCHITECTURE.md")
            result = CONTEXT_LAYER_NOT_READY
    for s in NON_CRITICAL_BOUNDARY_STRINGS:
        if not has_text(architecture_text, s):
            add(findings, "warning", "required_text_missing", f"missing non-critical boundary statement: {s}", "docs/M28-HYBRID-RAG-LIGHT-ARCHITECTURE.md")
            result = combine_result(result, CONTEXT_LAYER_READY_WITH_WARNINGS)

    # frontmatter checks
    frontmatter_text = load_text(root, "docs/M28-CONTEXT-FRONTMATTER-STANDARD.md")
    for s in [
        "type",
        "module",
        "status",
        "authority",
        "tags",
        "context_role",
        "summary",
        "last_validated",
        "No valid context frontmatter",
        "Generated integrity metadata must not be manually authored as semantic truth",
        "Context Pack must be minimal and explainable, not exhaustive",
    ]:
        if not has_text(frontmatter_text, s):
            add(findings, "error", "required_text_missing", f"frontmatter standard missing: {s}", "docs/M28-CONTEXT-FRONTMATTER-STANDARD.md")
            result = CONTEXT_LAYER_NOT_READY

    # index schema doc checks
    idx_doc = load_text(root, "docs/M28-CONTEXT-INDEX-SCHEMA.md")
    for s in [
        "data/context-index.json = generated M28 context-selection index",
        "Stale context must fail closed or require review",
        "sha256",
    ]:
        if not has_text(idx_doc, s):
            add(findings, "error", "required_text_missing", f"index schema doc missing: {s}", "docs/M28-CONTEXT-INDEX-SCHEMA.md")
            result = CONTEXT_LAYER_NOT_READY

    # script/document checks (text-verifiable and documentation-verifiable)
    build_script = load_text(root, "scripts/build-context-index.py")
    build_doc = idx_doc + "\n" + load_text(root, "docs/M28-CONTEXT-FRONTMATTER-STANDARD.md")
    for s in ["--check", "--json", "repo_commit_hash", "source_hash", "CONTEXT_INDEX_BUILT", "CONTEXT_INDEX_OK", "CONTEXT_INDEX_INVALID", "CONTEXT_INDEX_STALE", "CONTEXT_INDEX_NEEDS_REVIEW"]:
        if not has_text(build_script, s):
            add(findings, "error", "required_text_missing", f"build-context-index script missing: {s}", "scripts/build-context-index.py")
            result = CONTEXT_LAYER_NOT_READY
    for s in ["deterministic", "repository-relative", "generated metadata", "git add", "git commit", "git push"]:
        if not (has_text(build_script, s) or has_text(build_doc, s)):
            add(findings, "warning", "required_text_missing", f"build-context-index doc/script missing non-core text: {s}", "scripts/build-context-index.py")
            result = combine_result(result, CONTEXT_LAYER_READY_WITH_WARNINGS)

    select_script = load_text(root, "scripts/select-context.py")
    select_doc = load_text(root, "docs/M28-CONTEXT-PACK.md")
    for s in ["--json", "--dry-run", "CONTEXT_SELECTED", "CONTEXT_SELECTED_WITH_WARNINGS", "CONTEXT_NEEDS_REVIEW", "CONTEXT_INVALID"]:
        if not has_text(select_script, s):
            add(findings, "error", "required_text_missing", f"select-context script missing: {s}", "scripts/select-context.py")
            result = CONTEXT_LAYER_NOT_READY
    for s in ["Context Pack is not approval", "score is not authority", "matched_signals", "selected reason", "dry-run"]:
        if not (has_text(select_script, s) or has_text(select_doc, s)):
            add(findings, "error", "required_text_missing", f"select-context boundary/check missing: {s}", "scripts/select-context.py")
            result = CONTEXT_LAYER_NOT_READY
    if not has_any(select_script + "\n" + select_doc, ["<= 0", "final score <= 0", "Final score="]):
        add(findings, "error", "required_text_missing", "select-context boundary/check missing: items with final score <= 0 must not be selected", "scripts/select-context.py")
        result = CONTEXT_LAYER_NOT_READY
    if not has_any(select_script + "\n" + select_doc, ["overwrite", "overwritten on each normal run"]):
        add(findings, "warning", "required_text_missing", "select-context non-core boundary/check missing: overwrite behavior wording", "scripts/select-context.py")
        result = combine_result(result, CONTEXT_LAYER_READY_WITH_WARNINGS)
    for s in ["git add", "git commit", "git push"]:
        if not (has_text(select_script, s) or has_text(select_doc, s)):
            add(findings, "warning", "required_text_missing", f"select-context non-core boundary/check missing: {s}", "scripts/select-context.py")
            result = combine_result(result, CONTEXT_LAYER_READY_WITH_WARNINGS)

    req_script = load_text(root, "scripts/check-context-required.py")
    req_doc = load_text(root, "docs/M28-CONTEXT-REQUIRED.md")
    for s in ["CONTEXT_REQUIRED_OK", "CONTEXT_REQUIRED_MISSING", "CONTEXT_REQUIRED_INVALID", "CONTEXT_REQUIRED_NEEDS_REVIEW", "No valid Context Pack", "Context Pack is not approval", "No reason", "exact Markdown heading match", "continuous text", "task_id could not be extracted", "source_hash", "absolute paths", "sha256", "does not call select-context.py"]:
        if not (has_text(req_script, s) or has_text(req_doc, s)):
            add(findings, "error", "required_text_missing", f"context-required check missing: {s}", "scripts/check-context-required.py")
            result = CONTEXT_LAYER_NOT_READY

    comp_script = load_text(root, "scripts/check-context-compliance.py")
    comp_doc = load_text(root, "docs/M28-CONTEXT-COMPLIANCE.md")
    for s in ["CONTEXT_COMPLIANT", "CONTEXT_COMPLIANT_WITH_WARNINGS", "CONTEXT_VIOLATION", "CONTEXT_NEEDS_REVIEW", "CONTEXT_MISSING", "CONTEXT_COMPLIANT_WITH_WARNINGS => exit 1", "Missing required compliance input must return CONTEXT_MISSING", "must not infer compliance from silence", "prefer NEEDS_REVIEW", "section headers", "exact phrases", "keyword matching", "must not attempt semantic inference", "changed-files.txt must contain one repository-relative path per line", "POSIX absolute paths are invalid", "Windows absolute paths are invalid", "context compliance is not approval", "must never create validation/demo artifacts", "No-write validation snapshot"]:
        if not (has_text(comp_script, s) or has_text(comp_doc, s)):
            add(findings, "error", "required_text_missing", f"context-compliance check missing: {s}", "scripts/check-context-compliance.py")
            result = CONTEXT_LAYER_NOT_READY

    ver_doc = load_text(root, "docs/M28-CONTEXT-AWARE-VERIFICATION.md")
    ver_tpl = load_text(root, "templates/context-verification-record.md")
    for s in ["type: context-verification-record", "context_pack_hash", "repo_commit_hash", "frontmatter status must reflect", "context_pack_hash mismatch", "not_applicable requires explicit justification", "pass requires evidence", "silence about selected required context is not verification", "Test success does not authorize protected actions", "Context-aware verification is not approval", "Context-aware verification does not replace tests", "Context-aware verification does not replace M27 runtime enforcement", "Final Verification Result", "context_pack_integrity_failure"]:
        if not (has_text(ver_doc, s) or has_text(ver_tpl, s)):
            add(findings, "error", "required_text_missing", f"context-aware verification missing: {s}", "docs/M28-CONTEXT-AWARE-VERIFICATION.md")
            result = CONTEXT_LAYER_NOT_READY

    lessons_doc = load_text(root, "docs/M28-LESSONS-FEEDBACK-LOOP.md")
    lessons_tpl = load_text(root, "templates/lesson-candidate-record.md")
    needed_lessons = [
        "Agent may propose lesson",
        "Agent must not auto-update canonical rules",
        "Lesson Candidate is not approval",
        "Human review is required before promotion",
        "Do not create duplicate lessons",
        "review_required: true",
        "type: lesson-candidate",
        "status: proposed",
        "Agent must not set accepted_by_human",
        "Agent must not set rejected_by_human",
        "Agent must not set superseded",
        "Agent must not set archived",
        "one distinct issue pattern",
        "exactly one primary trigger",
        "missing evidence",
        "no evidence",
        "lesson must be directly traceable to evidence",
        "merge_with_existing_lesson requires a referenced existing lesson",
        "no evidence -> no promotion",
    ]
    for s in needed_lessons:
        if not (has_text(lessons_doc, s) or has_text(lessons_tpl, s)):
            add(findings, "error", "required_text_missing", f"lessons feedback missing: {s}", "docs/M28-LESSONS-FEEDBACK-LOOP.md")
            result = CONTEXT_LAYER_NOT_READY

    if not has_text(lessons_doc, "pending_lesson_candidates"):
        if has_text(lessons_doc, "pending lesson candidate"):
            add(findings, "warning", "required_text_missing", "pending_lesson_candidates exact token missing (equivalent concept found)", "docs/M28-LESSONS-FEEDBACK-LOOP.md")
            result = combine_result(result, CONTEXT_LAYER_READY_WITH_WARNINGS)
        else:
            add(findings, "needs_review", "required_text_missing", "pending_lesson_candidates behavior unclear", "docs/M28-LESSONS-FEEDBACK-LOOP.md")
            result = combine_result(result, CONTEXT_LAYER_NEEDS_REVIEW)

    # forbidden authority checks with false-positive protection
    targets = [
        "docs/M28-HYBRID-RAG-LIGHT-ARCHITECTURE.md",
        "docs/M28-CONTEXT-PACK.md",
        "docs/M28-CONTEXT-REQUIRED.md",
        "docs/M28-CONTEXT-COMPLIANCE.md",
        "docs/M28-CONTEXT-AWARE-VERIFICATION.md",
        "docs/M28-LESSONS-FEEDBACK-LOOP.md",
        "templates/context-pack.md",
        "templates/context-verification-record.md",
        "templates/lesson-candidate-record.md",
    ]
    for rel in targets:
        txt = load_text(root, rel)
        claims = find_forbidden_claims(txt)
        for c in claims:
            add(findings, "error", "forbidden_authority_claim", f"forbidden authority claim detected: {c}", rel)
            result = CONTEXT_LAYER_NOT_READY

    return result


def check_sqlite_boundary(root: Path, findings: list[Finding]) -> str:
    result = CONTEXT_LAYER_READY
    add(findings, "info", "optional_sqlite_absent_ok", "SQLite is optional and rebuildable", "")

    # absence is OK
    sqlite_files = []
    for ext in ("*.sqlite", "*.sqlite3", "*.db"):
        sqlite_files.extend(root.rglob(ext))
    for p in sqlite_files:
        rel = p.relative_to(root).as_posix()
        if rel.startswith(".agentos/cache/"):
            continue
        add(findings, "needs_review", "sqlite_artifact_present", f"sqlite-like artifact present outside optional cache: {rel}", rel)
        result = combine_result(result, CONTEXT_LAYER_NEEDS_REVIEW)

    return result


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    root = Path(args.root).resolve()

    findings: list[Finding] = []
    result = CONTEXT_LAYER_READY

    req_result, checked_files, missing = check_required_files(root, findings)
    result = combine_result(result, req_result)

    if req_result != CONTEXT_LAYER_NOT_READY:
        result = combine_result(result, check_schema(root, findings))
        result = combine_result(result, check_text_requirements(root, findings))
        result = combine_result(result, check_sqlite_boundary(root, findings))

    warnings = [f.message for f in findings if f.severity == "warning"]
    errors = [f.message for f in findings if f.severity == "error"]
    needs_review = [f.message for f in findings if f.severity == "needs_review"]

    payload = {
        "result": result,
        "root": args.root,
        "checked_files": checked_files,
        "missing_files": missing,
        "warnings": warnings,
        "errors": errors,
        "needs_review": needs_review,
        "findings": [asdict(f) for f in findings],
    }

    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True))
    else:
        print("M28 Context Layer Audit")
        print(f"checked_files={checked_files}")
        print(f"missing_files={len(missing)}")
        if warnings:
            print("warnings:")
            for w in warnings:
                print(f"- {w}")
        if errors:
            print("errors:")
            for e in errors:
                print(f"- {e}")
        if needs_review:
            print("needs_review:")
            for n in needs_review:
                print(f"- {n}")
        # Must be the last stdout line.
        print(result)

    return EXIT[result]


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
