#!/usr/bin/env python3
"""
M68 read-only scanner.
This is a read-only scanner, not a validator, not a cleanup tool,
not an approval tool, and not a lifecycle mutation tool.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import subprocess
from pathlib import Path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Read-only repository scanner for M68.0")
    p.add_argument("--root", required=True)
    p.add_argument("--tree-txt", required=True)
    p.add_argument("--tree-json", required=True)
    p.add_argument("--inventory", required=True)
    p.add_argument("--duplicates", required=True)
    p.add_argument("--owners", required=True)
    p.add_argument("--protected", required=True)
    p.add_argument("--drift", required=True)
    p.add_argument("--prompt-metrics", required=True)
    p.add_argument("--anomaly-grep", required=True)
    return p.parse_args()


def run_git(args: list[str], cwd: Path) -> tuple[bool, str]:
    try:
        cp = subprocess.run(
            args,
            cwd=str(cwd),
            capture_output=True,
            text=True,
            check=False,
        )
        if cp.returncode != 0:
            return False, "GIT_METADATA_UNAVAILABLE"
        return True, cp.stdout.strip()
    except Exception:
        return False, "GIT_METADATA_UNAVAILABLE"


def safe_text_read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ""


def file_hash(path: Path) -> str:
    try:
        h = hashlib.sha256()
        with path.open("rb") as f:
            while True:
                chunk = f.read(8192)
                if not chunk:
                    break
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return ""


def rel(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    reports_dir = (root / "reports").resolve()
    now = dt.datetime.now(dt.timezone.utc).isoformat()

    output_paths = {
        "tree_txt": Path(args.tree_txt),
        "tree_json": Path(args.tree_json),
        "inventory": Path(args.inventory),
        "duplicates": Path(args.duplicates),
        "owners": Path(args.owners),
        "protected": Path(args.protected),
        "drift": Path(args.drift),
        "prompt_metrics": Path(args.prompt_metrics),
        "anomaly_grep": Path(args.anomaly_grep),
    }

    resolved_outputs: dict[str, Path] = {}
    for key, out in output_paths.items():
        if out.is_absolute():
            print("SCAN_STATUS: BLOCKED")
            print(f"BLOCKED_REASON: output path must be relative ({key})")
            return 2
        resolved = (root / out).resolve()
        try:
            resolved.relative_to(reports_dir)
        except ValueError:
            print("SCAN_STATUS: BLOCKED")
            print(f"BLOCKED_REASON: output path outside reports/ ({key})")
            return 2
        resolved_outputs[key] = resolved

    all_paths = sorted(
        [p for p in root.rglob("*") if ".git" not in p.parts],
        key=lambda p: p.as_posix(),
    )
    dirs = [p for p in all_paths if p.is_dir()]
    files = [p for p in all_paths if p.is_file()]

    ok_branch, branch = run_git(["git", "branch", "--show-current"], root)
    ok_sha, sha = run_git(["git", "rev-parse", "HEAD"], root)
    ok_status, git_status = run_git(["git", "status", "--short"], root)
    if not ok_status:
        git_status = "GIT_STATUS_UNAVAILABLE"

    active_task_file = root / "tasks/active-task.md"
    active_task_text = safe_text_read(active_task_file)
    active_task_id = "UNKNOWN"
    for line in active_task_text.splitlines():
        if line.startswith("id: "):
            active_task_id = line.replace("id: ", "").strip()
            break

    tree_lines = ["."] + [rel(root, p) for p in all_paths]
    resolved_outputs["tree_txt"].write_text("\n".join(tree_lines) + "\n", encoding="utf-8")
    resolved_outputs["tree_json"].write_text(
        json.dumps(
            {"generated_at": now, "root": root.name, "paths": tree_lines},
            indent=2,
            ensure_ascii=False,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )

    file_type_summary: dict[str, int] = {}
    for f in files:
        ext = f.suffix.lower() if f.suffix else "<no_ext>"
        file_type_summary[ext] = file_type_summary.get(ext, 0) + 1

    expected = [
        "docs",
        "scripts",
        "schemas",
        "templates",
        "tests",
        "reports",
        "tasks",
        "workflow",
        "policies",
        "security",
        "quality",
        "memory-bank",
        "data",
        ".github",
        "README.md",
    ]
    missing_expected = []
    for x in expected:
        if not (root / x).exists():
            missing_expected.append(x)

    inventory = {
        "scan_status": "SCAN_STATUS: COMPLETE",
        "active_task_id": active_task_id,
        "branch": branch if ok_branch else "GIT_METADATA_UNAVAILABLE",
        "commit_sha": sha if ok_sha else "GIT_METADATA_UNAVAILABLE",
        "generated_at": now,
        "root": root.name,
        "directories": sorted([rel(root, d) for d in dirs]),
        "files": sorted([rel(root, f) for f in files]),
        "file_type_summary": dict(sorted(file_type_summary.items())),
        "missing_expected_paths": missing_expected,
        "notes": [
            "raw inventory only",
            "not approval",
            "not lifecycle mutation",
        ],
    }
    resolved_outputs["inventory"].write_text(
        json.dumps(inventory, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    dup_signals = []
    stems: dict[str, list[str]] = {}
    for f in files:
        r = rel(root, f)
        low = r.lower()
        if any(t in low for t in ["backup", ".bak", ".old", "~"]):
            dup_signals.append({"category": "backup_name_signal", "path": r})
        if "copy" in low:
            dup_signals.append({"category": "copy_name_signal", "path": r})
        if any(f" {n}" in low for n in ["2", "3", "4", "5"]):
            dup_signals.append({"category": "numbered_variant_signal", "path": r})
        if "__pycache__" in low:
            dup_signals.append({"category": "cache_signal", "path": r})
        stems.setdefault(f.stem.lower(), []).append(r)
    for stem, paths in sorted(stems.items()):
        if len(paths) > 1:
            dup_signals.append({"category": "same_stem_signal", "stem": stem, "paths": sorted(paths)})
    resolved_outputs["duplicates"].write_text(
        json.dumps({"signals": dup_signals}, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    codeowners_path = root / ".github/CODEOWNERS"
    codeowners_exists = codeowners_path.exists()
    owner_text = safe_text_read(codeowners_path) if codeowners_exists else ""
    owner_placeholder_signals = []
    for i, line in enumerate(owner_text.splitlines(), start=1):
        if "@OWNER_OR_ADMIN_REPLACE_ME" in line or "TODO" in line:
            owner_placeholder_signals.append({"line": i, "text": line.strip()})

    protected_paths = [
        "schemas/task-validation-package.schema.json",
        "schemas/task-validation-result.schema.json",
        "scripts/check-task-validation-contract.py",
        "schemas/agent-task-output-evidence.schema.json",
        "scripts/check-agent-task-evidence.py",
        "schemas/acceptance-criteria-check-package.schema.json",
        "scripts/check-acceptance-criteria.py",
        "schemas/unified-runner-input.schema.json",
        "scripts/run-task-validation.py",
        "scripts/check-false-pass-resistance.py",
        "tests/fixtures/m67-false-pass-resistance/",
        "docs/COMPLETION-GATE-HARDENING-CONTRACT.md",
        "reports/m63-completion-review.md",
        "reports/m64-completion-review.md",
        "reports/m65-completion-review.md",
        "reports/m66-completion-review.md",
        "reports/m67-completion-review.md",
    ]
    protected_presence = []
    uncovered = []
    for p in protected_paths:
        abs_p = root / p
        exists = abs_p.exists()
        ftype = "directory" if abs_p.is_dir() else ("file" if abs_p.is_file() else "missing")
        owner_signal = "unknown"
        if codeowners_exists and exists and owner_text:
            owner_signal = "present_codeowners_file"
        elif not codeowners_exists:
            owner_signal = "codeowners_missing"
        else:
            owner_signal = "no_obvious_owner_signal"
        if owner_signal in {"codeowners_missing", "no_obvious_owner_signal"}:
            uncovered.append(p)
        protected_presence.append(
            {
                "path": p,
                "exists": exists,
                "file_type": ftype,
                "owner_signal_if_any": owner_signal,
                "hash": file_hash(abs_p) if abs_p.is_file() else "",
                "notes": "presence evidence only",
            }
        )

    owners = {
        "codeowners_present": codeowners_exists,
        "placeholder_owner_signals": owner_placeholder_signals,
        "paths_with_no_obvious_owner_coverage": sorted(uncovered),
        "protected_artifact_owner_coverage_signals": [
            {
                "path": x["path"],
                "owner_signal_if_any": x["owner_signal_if_any"],
            }
            for x in protected_presence
        ],
    }
    resolved_outputs["owners"].write_text(
        json.dumps(owners, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    resolved_outputs["protected"].write_text(
        json.dumps(
            {"artifacts": protected_presence},
            indent=2,
            ensure_ascii=False,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )

    drift = {
        "final_status_pattern_candidates": [],
        "readiness_field_candidates": [],
        "non_authority_boundary_candidates": [],
        "approval_completion_claim_candidates": [],
        "inventory_freshness_candidates": [],
        "idle_state_candidates": [],
        "workflow_permission_candidates": [],
        "adapter_drift_candidates": [],
    }
    target_suffixes = {".md", ".txt", ".yml", ".yaml", ".json", ".py"}
    for f in files:
        if f.suffix.lower() not in target_suffixes:
            continue
        r = rel(root, f)
        text = safe_text_read(f)
        if "FINAL_STATUS:" in text:
            drift["final_status_pattern_candidates"].append(r)
        if "readiness" in text.lower() or "ready_for_" in text.lower():
            drift["readiness_field_candidates"].append(r)
        if "non-authority" in text.lower():
            drift["non_authority_boundary_candidates"].append(r)
        if "APPROVED" in text or "completion" in text.lower():
            drift["approval_completion_claim_candidates"].append(r)
        if "inventory" in text.lower() and "generated_at" in text.lower():
            drift["inventory_freshness_candidates"].append(r)
        if "No active task yet" in text or "status: none" in text:
            drift["idle_state_candidates"].append(r)
        if "permissions" in text.lower() and "workflow" in r.lower():
            drift["workflow_permission_candidates"].append(r)
        if "adapter" in r.lower() or "adapter" in text.lower():
            drift["adapter_drift_candidates"].append(r)
    for k in drift:
        drift[k] = sorted(set(drift[k]))
    resolved_outputs["drift"].write_text(
        json.dumps(drift, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    bootstrap_names = {"llms.txt", "AGENTS.md", "README.md"}
    bootstrap_files = [f for f in files if f.name in bootstrap_names or "bootstrap" in f.name.lower()]
    adapter_files = [f for f in files if "adapter" in rel(root, f).lower()]
    large_reports = [
        {"path": rel(root, f), "bytes": f.stat().st_size}
        for f in files
        if rel(root, f).startswith("reports/") and f.stat().st_size > 250_000
    ]
    prompt_metrics = {
        "bootstrap_startup_adjacent_files": len(bootstrap_files),
        "adapter_files": len(adapter_files),
        "line_counts": {
            rel(root, f): safe_text_read(f).count("\n") + 1
            for f in sorted(bootstrap_files, key=lambda x: x.as_posix())
        },
        "byte_counts": {
            rel(root, f): f.stat().st_size
            for f in sorted(bootstrap_files, key=lambda x: x.as_posix())
        },
        "large_files_startup_discovery_surface": [
            {"path": rel(root, f), "bytes": f.stat().st_size}
            for f in sorted(bootstrap_files, key=lambda x: x.as_posix())
            if f.stat().st_size > 250_000
        ],
        "large_generated_reports": sorted(large_reports, key=lambda x: x["path"]),
        "prompt_surface_risk_signals": [
            "LARGE_STARTUP_FILE" if any(x["bytes"] > 250_000 for x in large_reports) else "NONE"
        ],
    }
    resolved_outputs["prompt_metrics"].write_text(
        json.dumps(prompt_metrics, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    anomaly_patterns = [
        "@OWNER_OR_ADMIN_REPLACE_ME",
        "__pycache__",
        "copy",
        "copy 2",
        "HANDOFF 2.md",
        "run-all 3.sh",
        "run-all 4.sh",
        "No active task yet",
        "status: none",
        "READY_FOR_M69",
        "APPROVED",
        "CAN_DELETE",
        "CAN_DEPRECATE",
    ]
    anomaly_lines = []
    for f in files:
        r = rel(root, f)
        text = safe_text_read(f)
        if not text:
            continue
        for i, line in enumerate(text.splitlines(), start=1):
            low = line.lower()
            for ptn in anomaly_patterns:
                if ptn.lower() in low:
                    anomaly_lines.append(f"{r}:{i}:{line}")
                    break
    resolved_outputs["anomaly_grep"].write_text("\n".join(sorted(anomaly_lines)) + "\n", encoding="utf-8")

    top_dirs = sorted([d.name for d in root.iterdir() if d.is_dir() and d.name != ".git"])
    final_status = "FINAL_STATUS: M68_RAW_INVENTORY_COMPLETE"
    warnings = []
    if missing_expected:
        warnings.append("missing_expected_paths")
    if not ok_branch or not ok_sha:
        warnings.append("git_metadata_unavailable")
    if owners["paths_with_no_obvious_owner_coverage"]:
        warnings.append("owner_gaps")
    if dup_signals:
        warnings.append("duplicate_or_copy_signals")
    if warnings:
        final_status = "FINAL_STATUS: M68_RAW_INVENTORY_COMPLETE_WITH_WARNINGS"

    md = []
    md.append("# M68.0 — Repository Scan / Authoritative Raw Inventory")
    md.append("## Task Boundary")
    md.append("This report is scanner-backed inventory evidence only.")
    md.append("This report records repository facts and raw review signals only.")
    md.append("This report does not identify canonical documents.")
    md.append("This report does not identify deprecated documents.")
    md.append("This report does not approve cleanup, deletion, compression, consolidation, or docs-to-code conversion.")
    md.append("This report does not create registries.")
    md.append("This report does not create validators.")
    md.append("This report does not create fixtures.")
    md.append("This report does not modify protected artifacts.")
    md.append("This report does not complete M68.")
    md.append("Human review remains required before M68.1.")
    md.append("## Active Task Record")
    md.append(f"- active_task_id: {active_task_id}")
    md.append("## Scan Revision")
    md.append(f"- generated_at: {now}")
    md.append(f"- branch: {branch if ok_branch else 'GIT_METADATA_UNAVAILABLE'}")
    md.append(f"- commit_sha: {sha if ok_sha else 'GIT_METADATA_UNAVAILABLE'}")
    md.append("## Scanner Boundary")
    md.append("Read-only scanner. No cleanup, no approval, no lifecycle mutation.")
    md.append("## Generated Artifacts")
    for out in sorted(resolved_outputs.values(), key=lambda x: x.as_posix()):
        md.append(f"- {rel(root, out)}")
    md.append("## Repository Tree Summary")
    md.append(f"- total_paths: {len(all_paths)}")
    md.append("## Directory Inventory Summary")
    md.append(f"- top_level_directories: {', '.join(top_dirs)}")
    md.append("## Root-Level Inventory")
    md.append(f"- top_level_count: {len(list(root.iterdir()))}")
    md.append("## Bootstrap Surface Inventory")
    md.append(f"- bootstrap_files: {len(bootstrap_files)}")
    md.append("## scripts/ Inventory")
    md.append(f"- files: {sum(1 for f in files if rel(root, f).startswith('scripts/'))}")
    md.append("## schemas/ Inventory")
    md.append(f"- files: {sum(1 for f in files if rel(root, f).startswith('schemas/'))}")
    md.append("## tests/fixtures/ Inventory")
    md.append(f"- files: {sum(1 for f in files if rel(root, f).startswith('tests/fixtures/'))}")
    md.append("## reports/ Inventory")
    md.append(f"- files: {sum(1 for f in files if rel(root, f).startswith('reports/'))}")
    md.append("## tasks/ Inventory")
    md.append(f"- files: {sum(1 for f in files if rel(root, f).startswith('tasks/'))}")
    md.append("## .github/ Inventory")
    md.append(f"- files: {sum(1 for f in files if rel(root, f).startswith('.github/'))}")
    md.append("## .agentos/ Inventory")
    md.append(f"- present: {(root / '.agentos').exists()}")
    md.append("## Protected Artifacts Presence")
    md.append(f"- total_listed: {len(protected_presence)}")
    md.append(f"- present_count: {sum(1 for x in protected_presence if x['exists'])}")
    md.append("## Owner Gap Signals")
    md.append(f"- codeowners_present: {codeowners_exists}")
    md.append(f"- uncovered_count: {len(uncovered)}")
    md.append("## Duplicate / Backup Filename Signals")
    md.append(f"- signal_count: {len(dup_signals)}")
    md.append("## Active-Tree Ambiguity Signals")
    md.append(f"- same_stem_signals: {sum(1 for x in dup_signals if x.get('category') == 'same_stem_signal')}")
    md.append("## Idle-State Format Signals")
    md.append(f"- candidates: {len(drift['idle_state_candidates'])}")
    md.append("## Adapter Drift Signals")
    md.append(f"- candidates: {len(drift['adapter_drift_candidates'])}")
    md.append("## Validation Authority Drift Signals")
    md.append(f"- candidates: {len(drift['approval_completion_claim_candidates'])}")
    md.append("## Task Ledger vs Reports Signals")
    md.append(f"- inventory_freshness_candidates: {len(drift['inventory_freshness_candidates'])}")
    md.append("## Workflow Permission Risk Signals")
    md.append(f"- candidates: {len(drift['workflow_permission_candidates'])}")
    md.append("## Large Generated Artifact Signals")
    md.append(f"- large_generated_reports: {len(large_reports)}")
    md.append("## Prompt / Bootstrap Metrics")
    md.append(f"- bootstrap_startup_adjacent_files: {prompt_metrics['bootstrap_startup_adjacent_files']}")
    md.append(f"- adapter_files: {prompt_metrics['adapter_files']}")
    md.append("## Raw Review Signals For M68.1")
    md.append("- Review JSON/TXT artifacts only; no cleanup action in M68.0.")
    md.append("## Explicit Non-Conclusions")
    md.append("- No deletion decision.")
    md.append("- No compression decision.")
    md.append("- No docs-to-code decision.")
    md.append("- No M69 start authorization.")
    md.append("## Final Status")
    md.append(final_status)
    if warnings:
        md.append(f"- warnings: {', '.join(sorted(warnings))}")

    (root / "reports/m68-repo-raw-inventory.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print(final_status.replace("FINAL_STATUS: ", "SCAN_STATUS: ").replace("M68_RAW_INVENTORY_", ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
