# M71.1 — Script Inventory Snapshot

## Task Boundary

This M71 script inventory is evidence only.
This M71 script inventory is not approval.
This M71 script inventory does not authorize cleanup.
This M71 script inventory does not authorize script changes.
This M71 script inventory does not classify final lifecycle status.
reports/m71-script-inventory.md is the source-of-truth inventory artifact.
reports/m71-script-inventory.json is a derived navigation artifact only.
reports/m71-script-inventory.json must not become source of truth.
This M71 script inventory does not create registry authority.
This M71 script inventory does not authorize validator creation, fixture creation, or lifecycle mutation.
Human review remains required.

## Active Task Record

- id: task-71.1
- milestone: M71
- name: "Script Inventory Snapshot"
- status: active
- mode: "INVENTORY / READ-ONLY SCAN / DERIVED JSON"
- branch: dev
- started_at: "2026-05-29"

## Inputs Reviewed

- `reports/m71-m70-completion-intake.md`
- `scripts/` directory tree
- `.github/workflows/` directory tree
- `install.sh`
- `repo-map.md`
- `README.md`

## Authority Rule

reports/m71-script-inventory.md is the source-of-truth inventory artifact.
reports/m71-script-inventory.json is a derived navigation artifact only.
reports/m71-script-inventory.json must not become source of truth.
In case of any discrepancy or conflict between the JSON and Markdown files, the Markdown file will serve as the final authority.

## Scan Method

Read-only static scanning of files tracked in the Git repository under `scripts/` and top-level automation directories, coupled with search scans for references across workflows, documentation, and tasks.

## Top-Level Automation Surfaces

- `scripts/` (containing Python, Shell, and helper scripts)
- `install.sh` (root-level setup helper)
- `.github/workflows/` (containing CI/CD configuration files referencing scripts)

## scripts/ Inventory

Tracked files under `scripts/` include:
- `scripts/VALIDATORS.md`
- Various verification checkers, platform validators, execution controllers, regression suites, and duplicate files.

## Python Scripts

A total of 213 Python scripts (`.py`) exist in the `scripts/` directory, implementing:
- Validator logic, readiness checkers, and task execution rules.
- Legacy audit checks from prior milestones.

## Shell Scripts

A total of 11 shell scripts (`.sh`) are tracked under `scripts/`, including:
- `scripts/install-hooks.sh`
- `scripts/sync-context.sh`
- `scripts/canonical-cleanup.sh`
- `scripts/health-check.sh`
- `scripts/run-all.sh`

## Run-All Variants

Only one run-all script variant is tracked under the scripts directory:
- `scripts/run-all.sh`

## Copy / Backup / Legacy-Looking Filename Signals

A total of 23 files under `scripts/` were identified as having copy-numbered filename duplicate suffixes (ending with ` 3.py`), which are flagged for later review:
- `scripts/audit-m27 3.py`
- `scripts/audit-m27-level1 3.py`
- `scripts/audit-metadata-consistency 3.py`
- `scripts/audit-pre-merge-corridor 3.py`
- `scripts/audit-validation-integration 3.py`
- `scripts/build-index 3.py`
- `scripts/check-commit-push-preconditions 3.py`
- `scripts/check-github-platform-enforcement 3.py`
- `scripts/check-pre-merge-scope 3.py`
- `scripts/check-scope-compliance 3.py`
- `scripts/test-ci-advisory-config 3.py`
- `scripts/test-commit-push-preconditions-fixtures 3.py`
- `scripts/test-enforcement-fixtures 3.py`
- `scripts/test-m22-guardrails 3.py`
- `scripts/test-m27-level1-fixtures 3.py`
- `scripts/test-pre-merge-corridor-fixtures 3.py`
- `scripts/test-pre-merge-scope-fixtures 3.py`
- `scripts/test-scope-compliance-fixtures 3.py`
- `scripts/validate-boundary-claims 3.py`
- `scripts/validate-frontmatter 3.py`
- `scripts/validate-index 3.py`
- `scripts/validate-required-sections 3.py`
- `scripts/validate-status-semantics 3.py`

## Generated / Cache-Looking Signals

A total of 6 pyc Python compiled cache files are currently tracked in Git under the `scripts/__pycache__/` path:
- `scripts/__pycache__/agent-complete.cpython-314.pyc`
- `scripts/__pycache__/agent-fail.cpython-314.pyc`
- `scripts/__pycache__/agent-next.cpython-314.pyc`
- `scripts/__pycache__/generate-task-contract.cpython-314.pyc`
- `scripts/__pycache__/validate-task.cpython-314.pyc`
- `scripts/__pycache__/validate-verification.cpython-314.pyc`

## Workflow References

CI workflow files in `.github/workflows/` contain a total of 29 references to scripts under the `scripts/` directory and `run-all.sh`. These workflows orchestrate execution verification, code/doc integrity audits, and boundary checks.

## Documentation References

A total of 743 occurrences of "scripts/" were found under the `docs/` directory, detailing the usage of validator and enforcement tools.

## Report References

A total of 8,998 occurrences of "scripts/" were found in the `reports/` directory, primarily due to static repository scans and file lists.

## Task References

A total of 57 occurrences of "scripts/" were found in the `tasks/` directory, outlining tasks related to validator updates.

## Tests / Fixtures References

Script paths are referenced by various test execution commands and fixture definition files under `tests/` and `tests/fixtures/`.

## Automation-Adjacent Root Files

The following root-level script is flagged as automation-adjacent:
- `install.sh`

## Missing Or Empty Expected Areas

We identified a reference to `scripts/new-task.py` inside `install.sh`, but this script does not exist on disk. This missing script is logged for review.

## Raw Inventory Counts

- total_scripts_entries: 231
- python_scripts_count: 213
- shell_scripts_count: 11
- run_all_variant_count: 1
- copy_backup_signal_count: 23
- generated_cache_signal_count: 6
- workflow_reference_count: 29
- documentation_reference_count: 743
- unknown_reference_count: 1

Note: Counts are based on files tracked in the repository and static keyword search matches.

## JSON Navigation Artifact

The derived JSON artifact containing entries and counts is available at:
DERIVED_NAVIGATION_ARTIFACT: reports/m71-script-inventory.json

## Raw Signals For Later M71 Review

The 23 duplicate ` 3.py` files and the missing `scripts/new-task.py` reference require classification in later M71 tasks.
- raw_signal_copy_like_filename: present (23 files)
- raw_signal_run_all_variant: present (1 file)
- raw_signal_cache_like_path: present (6 files)
- raw_signal_referenced_by_workflow: present
- raw_signal_reference_unknown: present (1 file - scripts/new-task.py)
- needs_later_classification: true

## Classification Boundary

No final lifecycle status decisions have been made in M71.1. No files were marked as DEPRECATED, REPLACED, REMOVE, DELETE, ARCHIVE_NOW, CANONICAL_FINAL, or APPROVED_FOR_CLEANUP.
classification_finalized: false

## Scope Compliance

No scripts, docs, schemas, workflows, or data files were modified. The changed files are strictly limited to `tasks/active-task.md`, `reports/m71-script-inventory.md`, and `reports/m71-script-inventory.json`.
scope_violations: false

## M71.2 Preparation Decision

may_prepare_m71_2: true_with_warnings

may_prepare_m71_2 is roadmap preparation only.
may_prepare_m71_2 does not start M71.2.
may_prepare_m71_2 is not approval.
Human review remains required.

Rationale: The initial script inventory snapshot has been successfully compiled into this source-of-truth Markdown document and its derived JSON companion. Warnings are carried forward due to raw signals requiring review and missing script references, but no blockers remain.

## Explicit Non-Approval Boundary

This M71 script inventory is evidence only.
This M71 script inventory is not approval.
This M71 script inventory does not authorize cleanup.
This M71 script inventory does not authorize script changes.
This M71 script inventory does not classify final lifecycle status.
reports/m71-script-inventory.md is the source-of-truth inventory artifact.
reports/m71-script-inventory.json is a derived navigation artifact only.
reports/m71-script-inventory.json must not become source of truth.
This M71 script inventory does not create registry authority.
This M71 script inventory does not authorize validator creation, fixture creation, or lifecycle mutation.
Human review remains required.

## Final Status

SOURCE_OF_TRUTH_ARTIFACT: reports/m71-script-inventory.md
json_is_source_of_truth: false
markdown_is_source_of_truth: true
scripts_modified: false
cleanup_performed: false
registries_created: false
validators_created: false

FINAL_STATUS: M71_SCRIPT_INVENTORY_COMPLETE_WITH_WARNINGS
