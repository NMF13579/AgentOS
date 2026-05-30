# Active-Tree Cleanup Plan

## Task Boundary

This active-tree cleanup plan is a planning artifact only.
This active-tree cleanup plan does not execute cleanup.
This active-tree cleanup plan does not authorize deletion, rename, move, merge, archive, or refactor.
This active-tree cleanup plan does not modify scripts.
This active-tree cleanup plan does not decide final validation authority.
This active-tree cleanup plan does not create validators, registries, fixtures, or lifecycle mutation.
This active-tree cleanup plan does not approve M69.
Human review remains required.

## Active Task Record

- `id: task-69.5`
- `milestone: M69`
- `name: "Active-Tree Cleanup Plan"`
- `status: active`
- `mode: "EXECUTION / PLANNING / NO CLEANUP"`
- `branch: dev`
- `started_at: "2026-05-28"`

## Inputs Reviewed

- `reports/m69-m68-completion-intake.md`
- `reports/m69-script-inventory-intake.md`
- `docs/SCRIPT-RESPONSIBILITY-MAP.md`
- `docs/SCRIPT-LIFECYCLE-POLICY.md`
- `docs/SCRIPT-OUTPUT-CONTRACT.md`
- `docs/SCRIPT-EXIT-CODE-STANDARD.md`
- `reports/m68-duplicates.json`
- `reports/m68-protected-artifacts.json`
- `reports/m68-owner-gaps.json`
- `reports/m68-docs-to-code-drift.json`
- `reports/m68-anomaly-grep.txt`
- `docs/REPO-ANOMALY-MAP.md`
- `docs/DUPLICATION-MAP.md`
- `scripts/`
- root files
- `.github/workflows/`
- `.gitignore`

## M69.4 Contract Audit Status

M69.4 is complete with warnings.

The output and exit-code contract is documented, but cleanup is still planning only.

## Cleanup Planning Principles

M69.5 plans cleanup only.
M69.5 does not execute cleanup.
Cleanup candidates are not cleanup approvals.
Removal candidates are not deletion approvals.
Merge candidates are not merge approvals.
Human review remains required before any cleanup action.

## Protected Artifacts Exclusion Rule

Protected artifacts are excluded from cleanup execution in M69.5.
Protected artifacts must not be deleted, renamed, moved, merged, or refactored without separate human checkpoint.
PROTECTED means not a cleanup candidate without separate human checkpoint and rollback plan.

## Copy / Backup Script Candidates

- `scripts/audit-m27 3.py`
- `scripts/audit-m27-level1 3.py`
- `scripts/audit-metadata-consistency 3.py`
- `scripts/audit-pre-merge-corridor 3.py`
- `scripts/audit-validation-integration 3.py`
- `scripts/check-commit-push-preconditions 3.py`
- `scripts/check-github-platform-enforcement 3.py`
- `scripts/check-pre-merge-scope 3.py`
- `scripts/check-scope-compliance 3.py`
- other numbered copy signals in `scripts/* 3.py`

## Numbered Script Variant Candidates

- `scripts/build-index 3.py`
- `scripts/validate-frontmatter 3.py`
- `scripts/validate-index 3.py`
- `scripts/validate-required-sections 3.py`
- `scripts/validate-status-semantics 3.py`
- `scripts/test-m27-level1-fixtures 3.py`
- `scripts/test-pre-merge-scope-fixtures 3.py`
- `scripts/test-scope-compliance-fixtures 3.py`
- `scripts/test-enforcement-fixtures 3.py`
- `scripts/test-commit-push-preconditions-fixtures 3.py`

## Run-All Variant Candidates

- `scripts/run-all.sh`
- `templates/agentos-full/scripts/run-all.sh`
- `templates/agentos-minimal/scripts/run-all.sh`
- `templates/dist/full/scripts/run-all.sh`
- `templates/dist/minimal/scripts/run-all.sh`

## Tracked Cache / Generated Artifact Candidates

- `reports/ci/agentos-validate.json`
- `scripts/__pycache__`
- `scripts/lib/__pycache__`
- `scripts/renderers/__pycache__`
- `tests/fixtures/m66-unified-runner/mock-execution/mock-checkers/__pycache__`

## Ambiguous Root File Candidates

- `install.sh`
- `handoff/HANDOFF.md`

## Large Generated Report Candidates

- `reports/ci/agentos-validate.json`
- large M68 report outputs already used as evidence
- future generated reports under `reports/ci/` if they are only execution artifacts

## Workflow-Referenced File Constraints

- `scripts/agentos-validate.py` requires workflow reference review before cleanup.
- `scripts/run-all.sh` requires workflow reference review before cleanup.
- `scripts/VALIDATORS.md` requires workflow reference review before cleanup.
- `scripts/validate-architecture.sh` requires workflow reference review before cleanup.
- `scripts/validate-docs.py` requires workflow reference review before cleanup.
- `scripts/check-links.py` requires workflow reference review before cleanup.
- `scripts/check-llms-graph-files.sh` requires workflow reference review before cleanup.
- `.github/workflows/agentos-validate.yml` requires workflow reference review before cleanup.
- `.github/workflows/dev-only/agentos-validation.yml` requires workflow reference review before cleanup.
- `.github/workflows/dev-only/modular-validators.yml` requires workflow reference review before cleanup.

## Validation-Referenced File Constraints

- `scripts/agentos-validate.py` requires validation reference review before cleanup.
- `scripts/run-all.sh` requires validation reference review before cleanup.
- `scripts/VALIDATORS.md` requires validation reference review before cleanup.
- `scripts/check-execution-result-verification.py` requires validation reference review before cleanup.
- `scripts/check-task-acceptance-mvp.py` requires validation reference review before cleanup.
- `scripts/check-scope-compliance.py` requires validation reference review before cleanup.
- `scripts/check-single-role-execution.py` requires validation reference review before cleanup.
- `scripts/check-template-cleanliness.py` requires validation reference review before cleanup.
- `scripts/check-template-integrity.py` requires validation reference review before cleanup.

## Human Review Checkpoints

1. Confirm protected artifacts are excluded.
2. Confirm workflow references are still needed.
3. Confirm validation references are still needed.
4. Confirm rollback path for every cleanup candidate.
5. Confirm the human owner for the cleanup decision.

## Required Validation Before Cleanup Execution

- verify no workflow references
- verify no validation references
- verify no protected artifact path
- verify no source-of-truth dependency
- verify rollback path
- verify human approval
- verify scope of cleanup task
- verify `git diff --name-only`
- verify no lifecycle mutation unless explicitly tasked

## Proposed Future Cleanup Sequence

1. Confirm protected artifacts exclusion.
2. Confirm workflow references.
3. Confirm validation references.
4. Confirm owner/human review.
5. Move or delete only in a separate cleanup task.
6. Run regression validation.
7. Record evidence.

This sequence is not authorization to execute cleanup.

## Items Not Safe To Plan For Cleanup

- protected M61–M67 artifacts
- `scripts/agentos-validate.py`
- `scripts/run-all.sh`
- `scripts/VALIDATORS.md`
- `.github/workflows/agentos-validate.yml`
- `llms.txt`
- `ROUTES-REGISTRY.md`
- any file that is still used as source-of-truth or workflow input

## Explicit Non-Cleanup Boundary

This active-tree cleanup plan does not execute cleanup.
This active-tree cleanup plan does not authorize deletion, rename, move, merge, archive, or refactor.
This active-tree cleanup plan does not modify scripts.
This active-tree cleanup plan does not decide final validation authority.
This active-tree cleanup plan does not create validators, registries, fixtures, or lifecycle mutation.
This active-tree cleanup plan does not approve M69.
Human review remains required.

## M69.6 Preparation Decision

may_prepare_m69_6: true_with_warnings

may_prepare_m69_6 is roadmap preparation only.
may_prepare_m69_6 does not start M69.6.
may_prepare_m69_6 is not approval.

## Final Status

FINAL_STATUS: M69_ACTIVE_TREE_CLEANUP_PLAN_COMPLETE_WITH_WARNINGS
