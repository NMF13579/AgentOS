#!/usr/bin/env python3
"""Select task-relevant context from generated context index."""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

RESULT_SELECTED = "CONTEXT_SELECTED"
RESULT_SELECTED_WITH_WARNINGS = "CONTEXT_SELECTED_WITH_WARNINGS"
RESULT_NEEDS_REVIEW = "CONTEXT_NEEDS_REVIEW"
RESULT_INVALID = "CONTEXT_INVALID"

EXIT_BY_RESULT = {
    RESULT_SELECTED: 0,
    RESULT_SELECTED_WITH_WARNINGS: 0,
    RESULT_NEEDS_REVIEW: 1,
    RESULT_INVALID: 1,
}

NON_AUTH_BLOCK = [
    "Context Pack is not approval.",
    "Context Pack does not authorize commit, push, merge, release, deployment, or protected changes.",
    "Context Pack does not replace M27 runtime enforcement.",
    "Context Pack does not replace Human Gate approval.",
    "Freshness check is not approval.",
    "Integrity check is not approval.",
]

KEYWORDS_RE = re.compile(r"[a-zA-Z0-9_-]{3,}")


@dataclass
class SelectReport:
    result: str
    task_path: str
    context_pack_path: str
    selection_record_path: str
    candidate_count: int
    selected_count: int
    excluded_count: int
    warnings: list[str]
    errors: list[str]


def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Select M28 task context from data/context-index.json.")
    p.add_argument("task_path", help="Task file path")
    p.add_argument("--json", action="store_true", help="Print machine-readable JSON result")
    p.add_argument("--dry-run", action="store_true", help="Do not write reports")
    p.add_argument("--root", default=".", help="Repository root")
    return p.parse_args(argv)


def sha256_text(text: str) -> str:
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()


def git_head(root: Path) -> tuple[str | None, str | None]:
    try:
        proc = subprocess.run(["git", "rev-parse", "HEAD"], cwd=str(root), capture_output=True, text=True, check=False)
    except FileNotFoundError:
        return None, "git_not_found"
    if proc.returncode != 0:
        return None, "git_rev_parse_failed"
    head = proc.stdout.strip()
    if not head:
        return None, "git_head_empty"
    return head, None


def read_task(task_path: Path) -> tuple[dict[str, Any] | None, str, list[str]]:
    warnings: list[str] = []
    if not task_path.exists():
        return None, "", ["task_missing"]
    text = task_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        warnings.append("task_missing_frontmatter")
        return {}, text, warnings
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        warnings.append("task_frontmatter_unclosed")
        return {}, text, warnings
    block = "\n".join(lines[1:end])
    try:
        fm = yaml.safe_load(block)
    except Exception:
        warnings.append("task_frontmatter_yaml_invalid")
        fm = {}
    if not isinstance(fm, dict):
        fm = {}
    return fm, text, warnings


def infer_keywords(text: str) -> list[str]:
    words = [w.lower() for w in KEYWORDS_RE.findall(text)]
    stop = {
        "the",
        "and",
        "for",
        "with",
        "from",
        "that",
        "this",
        "task",
        "must",
        "not",
        "are",
        "was",
        "were",
        "into",
        "when",
        "what",
        "where",
        "have",
        "has",
        "had",
        "will",
        "should",
        "could",
        "would",
        "context",
        "module",
        "goal",
        "expected",
        "select",
        "selection",
        "relevant",
        "example",
    }
    uniq: list[str] = []
    seen = set()
    for w in words:
        if w in stop:
            continue
        if w not in seen:
            seen.add(w)
            uniq.append(w)
    return uniq[:40]


def extract_task_signals(task_fm: dict[str, Any], task_text: str, task_path: str) -> tuple[dict[str, Any], list[str], list[str]]:
    warnings: list[str] = []
    context_risks: list[str] = []

    nested = task_fm.get("task") if isinstance(task_fm.get("task"), dict) else {}

    task_id = task_fm.get("task_id") or nested.get("id")
    goal = nested.get("goal")
    risk_level = nested.get("risk_level")
    in_scope = nested.get("in_scope") if isinstance(nested.get("in_scope"), list) else []
    out_of_scope = nested.get("out_of_scope") if isinstance(nested.get("out_of_scope"), list) else []
    affected_paths = nested.get("files_or_areas") if isinstance(nested.get("files_or_areas"), list) else []
    acceptance = nested.get("acceptance_criteria") if isinstance(nested.get("acceptance_criteria"), list) else []
    verification_plan = nested.get("verification_plan") if isinstance(nested.get("verification_plan"), list) else []

    tags = [str(x).lower() for x in (task_fm.get("tags") or []) if isinstance(x, str)]
    module = task_fm.get("module") or ""
    keywords = infer_keywords(task_text)

    if not task_id:
        warnings.append("missing_task_id")
    if not goal:
        warnings.append("missing_goal")
    if not affected_paths:
        warnings.append("missing_affected_paths")
        context_risks.append("task lacks affected_paths")

    return {
        "task_id": str(task_id) if task_id else "task-unknown",
        "goal": str(goal) if goal else "goal-missing",
        "risk_level": str(risk_level) if risk_level else "UNKNOWN",
        "in_scope": in_scope,
        "out_of_scope": out_of_scope,
        "affected_paths": affected_paths,
        "acceptance_criteria": acceptance,
        "validation_plan": verification_plan,
        "tags": tags,
        "module": str(module) if module else "",
        "keywords": keywords,
        "task_path": task_path,
        "task_lint_status": "UNKNOWN",
    }, warnings, context_risks


def read_index(index_path: Path) -> tuple[dict[str, Any] | None, list[str]]:
    errors: list[str] = []
    if not index_path.exists():
        return None, ["context_index_missing"]
    try:
        data = json.loads(index_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return None, [f"context_index_invalid_json:{exc}"]
    if not isinstance(data, dict):
        return None, ["context_index_not_object"]
    entries = data.get("entries")
    if not isinstance(entries, list) or not entries:
        return None, ["context_index_empty_entries"]
    return data, errors


def use_fixture_local_index(task_path: Path, repo_root: Path) -> Path:
    local = task_path.parent / "context-index.json"
    if local.exists():
        return local
    return repo_root / "data/context-index.json"


def validate_index_and_freshness(index_doc: dict[str, Any], index_path: Path, root: Path) -> tuple[list[str], list[str], str]:
    warnings: list[str] = []
    errors: list[str] = []
    outcome = RESULT_SELECTED

    required_top = ["repo_commit_hash", "entries", "generated_at", "schema_version"]
    for f in required_top:
        if f not in index_doc:
            errors.append(f"index_missing_field:{f}")

    head, git_err = git_head(root)
    if git_err:
        warnings.append(git_err)
        outcome = RESULT_NEEDS_REVIEW
    else:
        if index_doc.get("repo_commit_hash") != head:
            warnings.append("stale_context_index_repo_commit_hash_mismatch")
            outcome = RESULT_NEEDS_REVIEW

    entries = index_doc.get("entries")
    if not isinstance(entries, list):
        errors.append("index_entries_invalid")
        return warnings, errors, RESULT_INVALID

    needed_entry = [
        "path",
        "type",
        "module",
        "status",
        "authority",
        "created",
        "last_validated",
        "tags",
        "context_role",
        "summary",
        "source_hash",
        "indexed_at",
    ]
    for i, e in enumerate(entries):
        if not isinstance(e, dict):
            errors.append(f"entry_not_object:{i}")
            continue
        for f in needed_entry:
            if f not in e:
                errors.append(f"entry_missing_field:{i}:{f}")

    source_index_path = index_doc.get("source_index_path")
    source_index_hash = index_doc.get("source_index_hash")
    if source_index_path:
        p = root / str(source_index_path)
        if p.exists() and source_index_hash:
            actual = sha256_text(p.read_text(encoding="utf-8"))
            if actual != source_index_hash:
                warnings.append("source_index_hash_mismatch")
                outcome = RESULT_NEEDS_REVIEW
        else:
            warnings.append("source_index_unverifiable")
            outcome = RESULT_NEEDS_REVIEW

    if errors:
        return warnings, errors, RESULT_INVALID
    return warnings, errors, outcome


def match_any_pattern(path: str, patterns: list[str]) -> bool:
    for pat in patterns:
        if fnmatch.fnmatch(path, pat):
            return True
    return False


def score_entry(entry: dict[str, Any], signals: dict[str, Any]) -> tuple[int, list[str], list[str]]:
    score = 0
    matched_signals: list[str] = []
    reasons: list[str] = []

    entry_tags = [str(t).lower() for t in entry.get("tags", []) if isinstance(t, str)]
    task_tags = set(signals.get("tags", []))
    overlap = task_tags.intersection(entry_tags)
    if overlap:
        score += 5
        matched_signals.append("tags")
        reasons.append(f"tag match: {', '.join(sorted(overlap))}")

    if signals.get("module") and str(entry.get("module", "")).lower() == str(signals.get("module", "")).lower():
        score += 4
        matched_signals.append("module")
        reasons.append("module matches task module")

    applies_to = entry.get("applies_to") if isinstance(entry.get("applies_to"), list) else []
    affected_paths = signals.get("affected_paths", [])
    if applies_to and affected_paths:
        if any(match_any_pattern(ap, applies_to) for ap in affected_paths):
            score += 4
            matched_signals.append("applies_to")
            reasons.append("affected_paths match applies_to")

    keywords = signals.get("keywords", [])
    blob = " ".join(
        [
            str(entry.get("summary", "")).lower(),
            " ".join(entry_tags),
        ]
    )
    kw_hits = [k for k in keywords if k in blob]
    if kw_hits:
        score += 3
        matched_signals.append("task keywords")
        reasons.append(f"keyword match: {', '.join(sorted(set(kw_hits[:5])))}")

    authority = str(entry.get("authority", ""))
    if authority == "canonical":
        score += 3
        matched_signals.append("authority")
        reasons.append("canonical authority")
    elif authority == "supporting":
        score += 2
        matched_signals.append("authority")
        reasons.append("supporting authority")
    elif authority == "context":
        score += 1
        matched_signals.append("authority")
        reasons.append("context authority")

    context_role = str(entry.get("context_role", ""))
    if context_role == "required_when_relevant":
        score += 3
        matched_signals.append("context_role")
        reasons.append("required_when_relevant context role")
    elif context_role == "supporting":
        score += 2
        matched_signals.append("context_role")
        reasons.append("supporting context role")
    elif context_role == "optional":
        score += 1
        matched_signals.append("context_role")
        reasons.append("optional context role")

    status = str(entry.get("status", ""))
    if status == "deprecated":
        score -= 5
        reasons.append("deprecated status penalty")
    elif status == "archived":
        score -= 3
        reasons.append("archived status penalty")

    excludes = entry.get("excludes") if isinstance(entry.get("excludes"), list) else []
    out_of_scope = signals.get("out_of_scope", [])
    if excludes and out_of_scope:
        if any(match_any_pattern(os, excludes) for os in out_of_scope):
            score -= 5
            matched_signals.append("excludes")
            reasons.append("conflict with out_of_scope/excludes")

    if context_role == "exclude_by_default":
        explicit_match = bool(overlap) or (applies_to and affected_paths and any(match_any_pattern(ap, applies_to) for ap in affected_paths))
        if not explicit_match:
            score -= 4
            reasons.append("exclude_by_default without explicit match")
        else:
            matched_signals.append("exclude_by_default explicit match")
            reasons.append("exclude_by_default selected only due to explicit match")

    return score, sorted(set(matched_signals)), reasons


def build_human_reason(reasons: list[str], score: int) -> str:
    base = "; ".join(reasons[:4])
    if not base:
        base = "Relevant by authority/context role baseline"
    return f"{base}. Final score={score}."


def select_candidates(index_doc: dict[str, Any], signals: dict[str, Any], root: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[str], list[str], str]:
    warnings: list[str] = []
    risks: list[str] = []
    entries = index_doc.get("entries", [])
    scored: list[dict[str, Any]] = []
    excluded: list[dict[str, Any]] = []

    has_canonical_candidate = False

    for e in entries:
        if not isinstance(e, dict):
            continue
        s, matched, reasons = score_entry(e, signals)
        item = {
            "entry": e,
            "score": s,
            "matched_signals": matched,
            "reason_parts": reasons,
            "reason": build_human_reason(reasons, s),
        }
        relevance_signals = {"tags", "module", "applies_to", "task keywords"}
        has_task_relevance = any(sig in relevance_signals for sig in matched)
        if str(e.get("authority")) == "canonical":
            has_canonical_candidate = True
        if s > 0 and has_task_relevance:
            scored.append(item)
        else:
            if s > 0 and not has_task_relevance:
                reasons.append("no direct task relevance signal")
            excluded.append(
                {
                    "path": e.get("path", ""),
                    "reason": build_human_reason(reasons, s),
                    "status": e.get("status", ""),
                    "authority": e.get("authority", ""),
                    "context_role": e.get("context_role", ""),
                }
            )

    if not has_canonical_candidate:
        risks.append("no canonical context found")

    if not scored:
        risks.append("no positive-scoring relevant context found")
        return [], excluded, warnings, risks, RESULT_NEEDS_REVIEW

    scored.sort(key=lambda x: (-x["score"], str(x["entry"].get("path", ""))))

    if len(scored) > 12:
        risks.append("too many matching candidates")
        return [], excluded + [
            {
                "path": x["entry"].get("path", ""),
                "reason": "excluded because candidate set too large; manual review required",
                "status": x["entry"].get("status", ""),
                "authority": x["entry"].get("authority", ""),
                "context_role": x["entry"].get("context_role", ""),
            }
            for x in scored
        ], warnings, risks, RESULT_NEEDS_REVIEW

    selected = scored[:5]
    selected_paths = {s["entry"].get("path", "") for s in selected}
    for x in scored[5:]:
        e = x["entry"]
        excluded.append(
            {
                "path": e.get("path", ""),
                "reason": "pruned to keep Context Pack minimal and explainable",
                "status": e.get("status", ""),
                "authority": e.get("authority", ""),
                "context_role": e.get("context_role", ""),
            }
        )

    for s in selected:
        rel = str(s["entry"].get("path", ""))
        p = root / rel
        if not p.exists():
            warnings.append(f"selected_missing_source:{rel}")
            risks.append("selected source_hash could not be verified")
            continue
        expected = str(s["entry"].get("source_hash", ""))
        actual = sha256_text(p.read_text(encoding="utf-8"))
        if expected != actual:
            warnings.append(f"selected_source_hash_mismatch:{rel}")
            risks.append("selected source_hash could not be verified")

    if any("warnings" in s["entry"] for s in selected):
        risks.append("selected context has warnings")

    if any(str(s["entry"].get("status")) == "deprecated" for s in selected):
        risks.append("deprecated context referenced")

    if any(str(s["entry"].get("context_role")) == "exclude_by_default" for s in selected):
        risks.append("exclude_by_default item required manual review")

    return selected, excluded, warnings, risks, RESULT_SELECTED


def render_context_pack(
    signals: dict[str, Any],
    selected: list[dict[str, Any]],
    excluded: list[dict[str, Any]],
    context_risks: list[str],
    index_path_rel: str,
    index_hash: str,
    repo_commit_hash: str,
) -> str:
    required_context: list[str] = []
    supporting_context: list[str] = []

    for s in selected:
        e = s["entry"]
        auth = str(e.get("authority", ""))
        role = str(e.get("context_role", ""))
        p = str(e.get("path", ""))
        if auth == "canonical" and role == "required_when_relevant":
            required_context.append(p)
        else:
            supporting_context.append(p)

    lines: list[str] = []
    lines.extend(
        [
            "---",
            "type: context-pack",
            f"task_id: {signals['task_id']}",
            "status: generated",
            "generated_by: select-context.py",
            f"generated_at: {index_doc_time()}",
            f"context_index_path: {index_path_rel}",
            f"context_index_hash: {index_hash}",
            f"repo_commit_hash: {repo_commit_hash}",
            "---",
            "",
            "# Context Pack",
            "",
            "## Task Summary",
            "",
            f"- task_id: {signals['task_id']}",
            f"- goal: {signals['goal']}",
            f"- risk_level: {signals['risk_level']}",
            "- affected_paths:",
        ]
    )
    if signals["affected_paths"]:
        for p in signals["affected_paths"]:
            lines.append(f"  - {p}")
    else:
        lines.append("  - unavailable")
    lines.extend(
        [
            f"- source_task_path: {signals['task_path']}",
            f"- task_lint_status: {signals['task_lint_status']}",
            "",
            "## Selected Context",
            "",
            "| Path | Type | Authority | Context Role | Reason | Must Follow |",
            "|---|---|---|---|---|---|",
        ]
    )

    for s in selected:
        e = s["entry"]
        must_follow = "Use source file as canonical; do not treat this selection as approval."
        lines.append(
            f"| {e.get('path')} | {e.get('type')} | {e.get('authority')} | {e.get('context_role')} | {s['reason']} | {must_follow} |"
        )

    lines.extend(["", "## Required Context", ""])
    if required_context:
        for p in required_context:
            lines.append(f"- {p}")
    else:
        lines.append("- none")

    lines.extend(["", "## Supporting Context", ""])
    if supporting_context:
        for p in supporting_context:
            lines.append(f"- {p}")
    else:
        lines.append("- none")

    lines.extend(["", "## Relevant Rules", ""])
    for s in selected:
        e = s["entry"]
        lines.append(f"- rule: Follow context from {e.get('path')} without overriding source authority.")
        lines.append(f"  source: {e.get('path')}")
        lines.append("  why: Selected as task-relevant context.")

    lines.extend(["", "## Relevant Lessons", ""])
    lesson_paths = [str(s["entry"].get("path")) for s in selected if str(s["entry"].get("type")) == "lesson"]
    if lesson_paths:
        for p in lesson_paths:
            lines.append(f"- lesson_summary: Use {p} to avoid repeated mistakes.")
            lines.append(f"  source: {p}")
            lines.append("  repeated_error_risk: Medium")
            lines.append("  required_behavior: Apply lesson checks in verification.")
    else:
        lines.append("- none")

    lines.extend(["", "## Relevant Policies", ""])
    policy_paths = [str(s["entry"].get("path")) for s in selected if str(s["entry"].get("type")) == "policy"]
    if policy_paths:
        for p in policy_paths:
            lines.append(f"- {p}")
    else:
        lines.append("- none")

    lines.extend(["", "## Out-of-Scope Context", ""])
    if excluded:
        for ex in excluded[:10]:
            lines.append(f"- path_or_category: {ex.get('path')}")
            lines.append(f"  reason_excluded: {ex.get('reason')}")
            lines.append("  manual_review_needed: false")
    else:
        lines.append("- none")

    lines.extend(["", "## Context Risks", ""])
    if context_risks:
        for r in sorted(set(context_risks)):
            lines.append(f"- {r}")
    else:
        lines.append("- none")

    lines.extend(["", "## Source Integrity", "", f"- context_index_path: {index_path_rel}", f"- context_index_hash: {index_hash}", f"- repo_commit_hash: {repo_commit_hash}", "- selected_source_hashes:"])
    for s in selected:
        e = s["entry"]
        lines.append(f"  - {e.get('path')}: {e.get('source_hash')}" )
    lines.extend(["- integrity_warnings: []", "", "Freshness proves alignment with source.", "Freshness does not grant approval.", "Invalid or stale derived context must never be silently upgraded into trusted context.", "", "## Non-Authorization Warning", ""])
    lines.extend(NON_AUTH_BLOCK)

    lines.extend(
        [
            "",
            "## Verification Checklist",
            "",
            "- [ ] Selected rules were acknowledged in the plan.",
            "- [ ] Selected policies were not contradicted.",
            "- [ ] Selected lessons were not repeated as mistakes.",
            "- [ ] Out-of-scope context was not touched.",
            "- [ ] Context Pack did not grant approval.",
            "- [ ] Runtime enforcement remained under M27.",
            "- [ ] Any stale or missing context was handled as NEEDS_REVIEW.",
            "",
        ]
    )
    return "\n".join(lines)


def index_doc_time() -> str:
    from datetime import datetime, timezone

    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def render_selection_record(
    result: str,
    signals: dict[str, Any],
    index_path_rel: str,
    index_hash: str,
    repo_commit_hash: str,
    selected: list[dict[str, Any]],
    excluded: list[dict[str, Any]],
    warnings: list[str],
    candidate_count: int,
) -> str:
    lines = [
        "# Context Selection Record",
        "",
        f"- task_id: {signals['task_id']}",
        f"- task_path: {signals['task_path']}",
        f"- context_index_path: {index_path_rel}",
        f"- context_index_hash: {index_hash}",
        f"- repo_commit_hash: {repo_commit_hash}",
        f"- candidate_count: {candidate_count}",
        f"- selected_count: {len(selected)}",
        f"- excluded_count: {len(excluded)}",
        f"- result: {result}",
        "",
        "Allowed result values:",
        "- CONTEXT_SELECTED",
        "- CONTEXT_SELECTED_WITH_WARNINGS",
        "- CONTEXT_NEEDS_REVIEW",
        "- CONTEXT_INVALID",
        "",
        "## selected_items",
        "",
    ]

    if selected:
        for s in selected:
            e = s["entry"]
            lines.append(f"- path: {e.get('path')}")
            lines.append(f"  score: {s.get('score')}")
            lines.append("  matched_signals:")
            for sig in s.get("matched_signals", []):
                lines.append(f"    - {sig}")
            lines.append(f"  reason: {s.get('reason')}")
            lines.append(f"  authority: {e.get('authority')}")
            lines.append(f"  context_role: {e.get('context_role')}")
            lines.append(f"  source_hash: {e.get('source_hash')}")
            lines.append("")
    else:
        lines.append("- none")
        lines.append("")

    lines.append("## excluded_items")
    lines.append("")
    if excluded:
        for ex in excluded:
            lines.append(f"- path: {ex.get('path')}")
            lines.append(f"  reason: {ex.get('reason')}")
            lines.append(f"  status: {ex.get('status')}")
            lines.append(f"  authority: {ex.get('authority')}")
            lines.append(f"  context_role: {ex.get('context_role')}")
            lines.append("")
    else:
        lines.append("- none")
        lines.append("")

    lines.append("## warnings")
    lines.append("")
    if warnings:
        for w in warnings:
            lines.append(f"- {w}")
    else:
        lines.append("- none")
    lines.append("")
    lines.append("- matched_signals are explainability metadata, not authority.")
    lines.append("- score is optional and score is not authority.")
    return "\n".join(lines) + "\n"


def run_select(task_path_raw: str, root: Path, dry_run: bool) -> SelectReport:
    task_path = Path(task_path_raw)
    if not task_path.is_absolute():
        task_path = (root / task_path).resolve()

    if not (root / "templates/context-pack.md").exists():
        return SelectReport(RESULT_INVALID, task_path_raw, "reports/context-pack.md", "reports/context-selection-record.md", 0, 0, 0, [], ["missing_template_context_pack"])
    if not (root / "templates/context-selection-record.md").exists():
        return SelectReport(RESULT_INVALID, task_path_raw, "reports/context-pack.md", "reports/context-selection-record.md", 0, 0, 0, [], ["missing_template_context_selection_record"])

    task_fm, task_text, task_warnings = read_task(task_path)
    if task_fm is None:
        return SelectReport(RESULT_INVALID, task_path_raw, "reports/context-pack.md", "reports/context-selection-record.md", 0, 0, 0, [], task_warnings)

    signals, signal_warnings, context_risks = extract_task_signals(task_fm, task_text, task_path.relative_to(root).as_posix())

    index_path = use_fixture_local_index(task_path, root)
    index_doc, index_errors = read_index(index_path)
    if index_errors or index_doc is None:
        return SelectReport(RESULT_INVALID, signals["task_path"], "reports/context-pack.md", "reports/context-selection-record.md", 0, 0, 0, task_warnings + signal_warnings, index_errors)

    index_hash = sha256_text(index_path.read_text(encoding="utf-8"))
    index_rel = index_path.relative_to(root).as_posix() if index_path.is_relative_to(root) else index_path.as_posix()

    idx_warnings, idx_errors, idx_result = validate_index_and_freshness(index_doc, index_path, root)
    if idx_errors:
        return SelectReport(RESULT_INVALID, signals["task_path"], "reports/context-pack.md", "reports/context-selection-record.md", 0, 0, 0, task_warnings + signal_warnings + idx_warnings, idx_errors)

    selected, excluded, sel_warnings, sel_risks, sel_result = select_candidates(index_doc, signals, root)
    context_risks.extend(sel_risks)

    repo_commit_hash = str(index_doc.get("repo_commit_hash", "unknown"))
    entries = index_doc.get("entries") if isinstance(index_doc.get("entries"), list) else []

    warnings = task_warnings + signal_warnings + idx_warnings + sel_warnings

    if not selected:
        result = RESULT_NEEDS_REVIEW
    else:
        result = RESULT_SELECTED

    if idx_result == RESULT_NEEDS_REVIEW and result == RESULT_SELECTED:
        result = RESULT_NEEDS_REVIEW

    if any(w in {"missing_task_id", "missing_goal"} for w in signal_warnings):
        result = RESULT_NEEDS_REVIEW

    if result == RESULT_SELECTED and warnings:
        result = RESULT_SELECTED_WITH_WARNINGS

    if result == RESULT_SELECTED_WITH_WARNINGS and not selected:
        result = RESULT_NEEDS_REVIEW

    pack_text = render_context_pack(
        signals=signals,
        selected=selected,
        excluded=excluded,
        context_risks=context_risks,
        index_path_rel=index_rel,
        index_hash=index_hash,
        repo_commit_hash=repo_commit_hash,
    )

    for s in selected:
        if not str(s.get("reason", "")).strip():
            return SelectReport(RESULT_INVALID, signals["task_path"], "reports/context-pack.md", "reports/context-selection-record.md", len(entries), len(selected), len(excluded), warnings, ["selected_item_missing_reason"])

    record_text = render_selection_record(
        result=result,
        signals=signals,
        index_path_rel=index_rel,
        index_hash=index_hash,
        repo_commit_hash=repo_commit_hash,
        selected=selected,
        excluded=excluded,
        warnings=warnings + ["matched_signals are explainability metadata, not authority", "score is optional and score is not authority"],
        candidate_count=len(entries),
    )

    if not dry_run:
        pack_path = root / "reports/context-pack.md"
        rec_path = root / "reports/context-selection-record.md"
        pack_path.parent.mkdir(parents=True, exist_ok=True)
        rec_path.parent.mkdir(parents=True, exist_ok=True)
        pack_path.write_text(pack_text, encoding="utf-8")
        rec_path.write_text(record_text, encoding="utf-8")

    return SelectReport(
        result=result,
        task_path=signals["task_path"],
        context_pack_path="reports/context-pack.md",
        selection_record_path="reports/context-selection-record.md",
        candidate_count=len(entries),
        selected_count=len(selected),
        excluded_count=len(excluded),
        warnings=warnings,
        errors=[],
    )


def print_report(report: SelectReport, as_json: bool) -> None:
    payload = {
        "result": report.result,
        "task_path": report.task_path,
        "context_pack_path": report.context_pack_path,
        "selection_record_path": report.selection_record_path,
        "candidate_count": report.candidate_count,
        "selected_count": report.selected_count,
        "excluded_count": report.excluded_count,
        "warnings": report.warnings,
        "errors": report.errors,
    }
    if as_json:
        print(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True))
        return
    print(report.result)
    print(f"task_path={report.task_path}")
    print(f"context_pack_path={report.context_pack_path}")
    print(f"selection_record_path={report.selection_record_path}")
    print(f"candidate_count={report.candidate_count}")
    print(f"selected_count={report.selected_count}")
    print(f"excluded_count={report.excluded_count}")
    if report.warnings:
        print("warnings:")
        for w in report.warnings:
            print(f"- {w}")
    if report.errors:
        print("errors:")
        for e in report.errors:
            print(f"- {e}")


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    root = Path(args.root).resolve()
    report = run_select(args.task_path, root, dry_run=args.dry_run)
    print_report(report, as_json=args.json)
    return EXIT_BY_RESULT[report.result]


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
