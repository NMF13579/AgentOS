# M71.3 — Legacy / Duplicate / Backup Classification

## Task Boundary

This M71 legacy and duplicate map is evidence only.
This M71 legacy and duplicate map is not approval.
This M71 legacy and duplicate map does not authorize cleanup.
This M71 legacy and duplicate map does not authorize script changes.
This M71 legacy and duplicate map does not classify final lifecycle status.
This M71 legacy and duplicate map does not approve deletion, archiving, renaming, or moving files.
This M71 legacy and duplicate map does not create registry authority.
This M71 legacy and duplicate map does not authorize validator creation, fixture creation, or lifecycle mutation.
reports/m71-script-inventory.md is the source-of-truth inventory artifact.
reports/m71-script-inventory.json is a derived navigation artifact only.
reports/m71-script-inventory.json must not become source of truth.
Human review remains required.

## Active Task Record

- id: task-71.3
- milestone: M71
- name: "Legacy / Duplicate / Backup Classification"
- status: active
- mode: "AUDIT / READ-ONLY CLASSIFICATION / NO CLEANUP"
- branch: dev
- started_at: "2026-05-29"

## Inputs Reviewed

- PRIMARY_INPUT: reports/m71-script-inventory.md
- SECONDARY_INPUT: docs/SCRIPT-RESPONSIBILITY-MAP.md
- NAVIGATION_HELPER: reports/m71-script-inventory.json
- Workflow files under `.github/workflows/`
- Documentation files under `docs/`
- Tasks files under `tasks/`
- Test fixtures under `tests/fixtures/`

## Authority Rule

reports/m71-script-inventory.md is the source-of-truth inventory artifact.
reports/m71-script-inventory.json is a derived navigation artifact only.
reports/m71-script-inventory.json must not become source of truth.
In case of any discrepancy or conflict, the Markdown inventory wins.

## Source Inventory Summary

The source inventory lists a total of 231 script entries + 1 automation-adjacent script (install.sh).
All entries have been classified.

## Responsibility Map Summary

The responsibility map [docs/SCRIPT-RESPONSIBILITY-MAP.md](file:///Users/muhammednazyrov/Documents/GitHub/AgentOS/docs/SCRIPT-RESPONSIBILITY-MAP.md) was used to cross-reference responsibility categories and known caller details for each mapped script.

## Classification Categories

The classification categorizes scripts into the following candidate statuses:
- `ACTIVE_CANDIDATE`: Mapped active scripts needed for repository support.
- `LEGACY_CANDIDATE`: Older versions of scripts requiring review.
- `BACKUP_CANDIDATE`: Backup scripts.
- `ORPHAN_CANDIDATE`: Scripts without any active callers.
- `GENERATED_CACHE_CANDIDATE`: Compiled python cache files.
- `RUN_ALL_VARIANT_CANDIDATE`: run-all variants.
- `NEEDS_REVIEW`: Candidates that require human reviews before deletion/archive.
- `BLOCKED_UNKNOWN`: Missing or contradictory scripts.
- `BLOCKED_PROTECTED`: Safety-critical, validation, or governance files blocked from cleanup.

## Copy-Like Filename Signals

- copy_like_signal_count: 23

## Backup-Like Filename Signals

- backup_like_signal_count: 7
Files with backup-like names (containing `backup`, `bak`, `temp`, `tmp`, `copy`).

## Legacy-Like Filename Signals

- legacy_like_signal_count: 23
Files with legacy-like names (containing `legacy`, `old`).

## Run-All Variant Signals

- run_all_variant_signal_count: 1
Files serving as unified runners (`scripts/run-all.sh`).

## Generated / Cache-Like Signals

- generated_cache_signal_count: 6
Python compiled bytecode files under `__pycache__/`.

## Orphan-Like Reference Signals

- orphan_like_signal_count: 0
Files with no active callers found in workflows, docs, reports, tasks, or tests.

## Protected / Governance-Critical Signals

- protected_signal_count: 130
Validation and enforcement authority scripts.

## Candidate Classification Table

| path | raw_signal | candidate_status | responsibility_category | known_caller | reference_signal | protected_signal | proposed_later_review | cleanup_authorized | notes |
|---|---|---|---|---|---|---|---|---|---|
| `install.sh` | needs_later_classification | BLOCKED_PROTECTED | unknown | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/VALIDATORS.md` | needs_later_classification | ACTIVE_CANDIDATE | unknown | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/__pycache__/agent-complete.cpython-314.pyc` | raw_signal_cache_like_path | GENERATED_CACHE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/__pycache__/agent-fail.cpython-314.pyc` | raw_signal_cache_like_path | GENERATED_CACHE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/__pycache__/agent-next.cpython-314.pyc` | raw_signal_cache_like_path | GENERATED_CACHE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/__pycache__/generate-task-contract.cpython-314.pyc` | raw_signal_cache_like_path | GENERATED_CACHE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/__pycache__/validate-task.cpython-314.pyc` | raw_signal_cache_like_path | GENERATED_CACHE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/__pycache__/validate-verification.cpython-314.pyc` | raw_signal_cache_like_path | GENERATED_CACHE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/activate-task.py` | needs_later_classification | ACTIVE_CANDIDATE | unknown | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/agent-complete.py` | needs_later_classification | BLOCKED_PROTECTED | unified_runner | docs, reports, tasks | docs, reports, tasks | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/agent-fail.py` | needs_later_classification | BLOCKED_PROTECTED | unified_runner | docs, reports, tasks | docs, reports, tasks | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/agent-next.py` | needs_later_classification | BLOCKED_PROTECTED | unified_runner | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/agentos-audit-log.py` | needs_later_classification | BLOCKED_PROTECTED | unified_runner | workflow, docs, reports | workflow, docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/agentos-command-guard.py` | needs_later_classification | BLOCKED_PROTECTED | unified_runner | workflow, docs, reports | workflow, docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/agentos-enforce.py` | needs_later_classification | BLOCKED_PROTECTED | unified_runner | workflow, docs, reports | workflow, docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/agentos-explain.py` | needs_later_classification | BLOCKED_PROTECTED | unified_runner | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/agentos-git-guard.py` | needs_later_classification | BLOCKED_PROTECTED | unified_runner | workflow, docs, reports | workflow, docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/agentos-human-gate.py` | needs_later_classification | BLOCKED_PROTECTED | unified_runner | workflow, docs, reports | workflow, docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/agentos-next-step.py` | needs_later_classification | BLOCKED_PROTECTED | unified_runner | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/agentos-permission-state.py` | needs_later_classification | BLOCKED_PROTECTED | unified_runner | workflow, docs, reports | workflow, docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/agentos-retry-enforce.py` | needs_later_classification | BLOCKED_PROTECTED | unified_runner | workflow, docs, reports | workflow, docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/agentos-status.py` | needs_later_classification | BLOCKED_PROTECTED | unified_runner | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/agentos-tui.py` | needs_later_classification | BLOCKED_PROTECTED | unified_runner | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/agentos-validate.py` | needs_later_classification | BLOCKED_PROTECTED | unified_runner | workflow, docs, reports, tasks, fixtures | workflow, docs, reports, tasks, fixtures | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/agentos-view-model.py` | needs_later_classification | BLOCKED_PROTECTED | unified_runner | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/agentos-violation-enforce.py` | needs_later_classification | BLOCKED_PROTECTED | unified_runner | workflow, docs, reports | workflow, docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/agentos-write-guard.py` | needs_later_classification | BLOCKED_PROTECTED | unified_runner | workflow, docs, reports | workflow, docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/agentos.py` | needs_later_classification | BLOCKED_PROTECTED | unified_runner | docs, reports, tasks | docs, reports, tasks | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/apply-transition.py` | needs_later_classification | ACTIVE_CANDIDATE | unknown | docs, reports, fixtures | docs, reports, fixtures | none | NEEDS_REVIEW | false | |
| `scripts/audit-agentos.py` | needs_later_classification | BLOCKED_PROTECTED | workflow_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/audit-approval-boundary.py` | needs_later_classification | BLOCKED_PROTECTED | workflow_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/audit-context-layer.py` | needs_later_classification | BLOCKED_PROTECTED | workflow_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/audit-enforcement.py` | needs_later_classification | BLOCKED_PROTECTED | workflow_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/audit-execution-control.py` | needs_later_classification | BLOCKED_PROTECTED | completion_gate_boundary | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/audit-gate-contract.py` | needs_later_classification | BLOCKED_PROTECTED | workflow_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/audit-lifecycle-mutation.py` | needs_later_classification | BLOCKED_PROTECTED | workflow_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/audit-m27-level1.py` | needs_later_classification | BLOCKED_PROTECTED | workflow_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/audit-m27.py` | needs_later_classification | BLOCKED_PROTECTED | workflow_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/audit-m30-context-pipeline.py` | needs_later_classification | BLOCKED_PROTECTED | workflow_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/audit-m31-tui-tutor.py` | needs_later_classification | BLOCKED_PROTECTED | workflow_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/audit-metadata-consistency.py` | needs_later_classification | BLOCKED_PROTECTED | workflow_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/audit-mvp-readiness.py` | needs_later_classification | BLOCKED_PROTECTED | workflow_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/audit-policy-boundary.py` | needs_later_classification | BLOCKED_PROTECTED | workflow_validation | docs, reports, fixtures | docs, reports, fixtures | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/audit-pre-merge-corridor.py` | needs_later_classification | BLOCKED_PROTECTED | workflow_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/audit-release-readiness.py` | needs_later_classification | BLOCKED_PROTECTED | workflow_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/audit-template-packaging.py` | raw_signal_backup_like_filename | BLOCKED_PROTECTED | workflow_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/audit-validation-integration.py` | needs_later_classification | BLOCKED_PROTECTED | workflow_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/build-context-cache.py` | needs_later_classification | ACTIVE_CANDIDATE | unknown | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/build-context-index.py` | needs_later_classification | ACTIVE_CANDIDATE | unknown | docs, reports, fixtures | docs, reports, fixtures | none | NEEDS_REVIEW | false | |
| `scripts/build-execution-verification-registry.py` | needs_later_classification | ACTIVE_CANDIDATE | unknown | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/build-index.py` | needs_later_classification | ACTIVE_CANDIDATE | context_indexing | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/build-task-dependency-map.py` | needs_later_classification | ACTIVE_CANDIDATE | unknown | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/canonical-cleanup.sh` | needs_later_classification | ACTIVE_CANDIDATE | unknown | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/check-acceptance-criteria.py` | needs_later_classification | BLOCKED_PROTECTED | acceptance_checking | docs, reports, fixtures | docs, reports, fixtures | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-active-task-readiness.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs | docs | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-agent-task-evidence.py` | needs_later_classification | BLOCKED_PROTECTED | agent_evidence_validation | docs, reports, fixtures | docs, reports, fixtures | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-apply-preconditions.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports, fixtures | docs, reports, fixtures | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-bypass-fixtures.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-bypass-resistance.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-canary-integrity.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-commit-push-preconditions.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports, fixtures | docs, reports, fixtures | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-completion-readiness.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-context-compliance.py` | needs_later_classification | ACTIVE_CANDIDATE | context_indexing | docs, reports, fixtures | docs, reports, fixtures | none | NEEDS_REVIEW | false | |
| `scripts/check-context-index-freshness.py` | needs_later_classification | ACTIVE_CANDIDATE | context_indexing | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/check-context-pipeline.py` | needs_later_classification | ACTIVE_CANDIDATE | context_indexing | workflow, docs, reports | workflow, docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/check-context-required.py` | needs_later_classification | ACTIVE_CANDIDATE | context_indexing | docs, reports, fixtures | docs, reports, fixtures | none | NEEDS_REVIEW | false | |
| `scripts/check-controlled-execution-session.py` | needs_later_classification | BLOCKED_PROTECTED | unified_runner | docs, reports, fixtures | docs, reports, fixtures | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-dangerous-commands.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | workflow, docs, reports | workflow, docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-evidence-amendments.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-evidence-binding.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-evidence-immutability.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-execution-authorization.py` | needs_later_classification | BLOCKED_PROTECTED | unified_runner | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-execution-readiness.py` | needs_later_classification | BLOCKED_PROTECTED | unified_runner | docs, reports, fixtures | docs, reports, fixtures | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-execution-result-verification.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-execution-scope.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports, fixtures | docs, reports, fixtures | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-execution-verification-chain.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-execution-verification-registry.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-execution-verification-regression.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-false-pass-resistance.py` | needs_later_classification | BLOCKED_PROTECTED | false_pass_resistance | docs, reports, fixtures | docs, reports, fixtures | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-github-platform-enforcement.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-identity-drift.sh` | needs_later_classification | BLOCKED_PROTECTED | task_validation | workflow, docs, reports | workflow, docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-interview-completeness.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-links.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-llms-graph-files.sh` | needs_later_classification | BLOCKED_PROTECTED | task_validation | workflow, docs, reports | workflow, docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-m54-queue-placement-fixtures.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs | docs | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-m55-active-task-readiness-fixtures.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-m56-execution-readiness-fixtures.py` | needs_later_classification | BLOCKED_PROTECTED | unified_runner | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-m57-execution-authorization-fixtures.py` | needs_later_classification | BLOCKED_PROTECTED | unified_runner | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-m58-controlled-execution-session-fixtures.py` | needs_later_classification | BLOCKED_PROTECTED | unified_runner | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-m59-execution-result-verification-fixtures.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-m61-hardening-regression.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-pr-quality.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | workflow, docs, reports, tasks | workflow, docs, reports, tasks | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-pre-merge-scope.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports, fixtures | docs, reports, fixtures | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-premature-artifacts.sh` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-private-evaluator-consistency.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-process-trace.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-product-spec-readiness.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-readiness-assertions.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-required-context-compliance.py` | needs_later_classification | ACTIVE_CANDIDATE | context_indexing | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/check-required-context-pack.py` | needs_later_classification | ACTIVE_CANDIDATE | context_indexing | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/check-risk.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | workflow, docs, reports | workflow, docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-role-separation.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-scope-compliance.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-single-role-execution.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-task-acceptance-mvp.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports, fixtures | docs, reports, fixtures | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-task-validation-contract.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports, fixtures | docs, reports, fixtures | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-template-cleanliness.py` | raw_signal_backup_like_filename | BLOCKED_PROTECTED | task_validation | docs, reports, tasks | docs, reports, tasks | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-template-integrity.py` | raw_signal_backup_like_filename | BLOCKED_PROTECTED | task_validation | docs, reports, fixtures | docs, reports, fixtures | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-transition.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-use-template-readiness.py` | raw_signal_backup_like_filename | BLOCKED_PROTECTED | task_validation | docs, reports, tasks | docs, reports, tasks | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/check-validator-authority-boundary.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/complete-active-task.py` | needs_later_classification | ACTIVE_CANDIDATE | unknown | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/detect-task-state.py` | needs_later_classification | ACTIVE_CANDIDATE | unknown | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/generate-repo-map.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/generate-task-contract-candidate.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/generate-task-contract.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports, fixtures | docs, reports, fixtures | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/generate-tasks-from-spec.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/generate-tasks-from-ux.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/health-check.sh` | needs_later_classification | ACTIVE_CANDIDATE | unknown | workflow, docs, reports | workflow, docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/install-agentos.py` | needs_later_classification | ACTIVE_CANDIDATE | install_template | docs, reports, tasks | docs, reports, tasks | none | NEEDS_REVIEW | false | |
| `scripts/install-hooks.sh` | needs_later_classification | ACTIVE_CANDIDATE | install_template | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/lib/__init__.py` | needs_later_classification | ACTIVE_CANDIDATE | unknown | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/lib/path_utils.py` | needs_later_classification | ACTIVE_CANDIDATE | unknown | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/lint-task-contract.py` | needs_later_classification | ACTIVE_CANDIDATE | unknown | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/materialize-task-candidate-placement.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs | docs | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/prepare-clean-template.py` | raw_signal_backup_like_filename | NEEDS_REVIEW | unknown | docs, reports, tasks | docs, reports, tasks | none | NEEDS_REVIEW | false | |
| `scripts/renderers/__init__.py` | needs_later_classification | ACTIVE_CANDIDATE | unknown | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/renderers/plain_status_renderer.py` | needs_later_classification | ACTIVE_CANDIDATE | unknown | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/renderers/rich_status_renderer.py` | needs_later_classification | ACTIVE_CANDIDATE | unknown | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/repo-scan.py` | needs_later_classification | ACTIVE_CANDIDATE | repo_inventory | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/review-task-candidate-placement.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/run-active-task.py` | needs_later_classification | ACTIVE_CANDIDATE | unknown | docs, reports, fixtures | docs, reports, fixtures | none | NEEDS_REVIEW | false | |
| `scripts/run-all.sh` | raw_signal_run_all_variant | BLOCKED_PROTECTED | unified_runner | workflow, docs, reports, tasks, fixtures | workflow, docs, reports, tasks, fixtures | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/run-execution-verification.py` | needs_later_classification | ACTIVE_CANDIDATE | unknown | docs, reports, fixtures | docs, reports, fixtures | none | NEEDS_REVIEW | false | |
| `scripts/run-task-validation.py` | needs_later_classification | ACTIVE_CANDIDATE | unknown | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/select-context.py` | needs_later_classification | ACTIVE_CANDIDATE | unknown | docs, reports, fixtures | docs, reports, fixtures | none | NEEDS_REVIEW | false | |
| `scripts/smoke-interview-layer.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/smoke-m44-decomposition.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/sync-context.sh` | needs_later_classification | ACTIVE_CANDIDATE | unknown | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/sync-task-ids.py` | needs_later_classification | BLOCKED_PROTECTED | workflow_validation | workflow, docs, reports, tasks | workflow, docs, reports, tasks | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/task-health.py` | needs_later_classification | ACTIVE_CANDIDATE | unknown | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/test-activation-fixtures.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/test-active-task-fixtures.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/test-apply-transition-fixtures.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports, fixtures | docs, reports, fixtures | none | NEEDS_REVIEW | false | |
| `scripts/test-approval-fixtures.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/test-approval-flow-smoke.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/test-approval-marker-fixtures.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/test-ci-advisory-config.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/test-commit-push-preconditions-fixtures.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/test-completion-flow-smoke.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports, fixtures | docs, reports, fixtures | none | NEEDS_REVIEW | false | |
| `scripts/test-enforcement-fixtures.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/test-example-project.sh` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/test-execution-runner-fixtures.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/test-gate-regression-fixtures.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/test-guard-failures.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/test-honest-pass-fixtures.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/test-human-approval-fixtures.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/test-install.sh` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/test-integrity-regression.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/test-m22-guardrails.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/test-m27-level1-fixtures.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/test-m40-runtime-bypass-smoke.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/test-negative-fixtures.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports, fixtures | docs, reports, fixtures | none | NEEDS_REVIEW | false | |
| `scripts/test-policy-enforcement-fixtures.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports, fixtures | docs, reports, fixtures | none | NEEDS_REVIEW | false | |
| `scripts/test-policy-fixtures.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/test-policy-flow-smoke.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports, fixtures | docs, reports, fixtures | none | NEEDS_REVIEW | false | |
| `scripts/test-pre-merge-corridor-fixtures.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/test-pre-merge-scope-fixtures.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/test-readiness-fixtures.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/test-scope-compliance-fixtures.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/test-single-role-execution-fixtures.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/test-state-fixtures.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/test-template-integrity-fixtures.py` | raw_signal_backup_like_filename | NEEDS_REVIEW | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/test-template-integrity.py` | raw_signal_backup_like_filename | NEEDS_REVIEW | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/test-unified-gate-smoke.py` | needs_later_classification | ACTIVE_CANDIDATE | test_fixture_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/validate-active-task.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports, fixtures | docs, reports, fixtures | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/validate-approval-marker.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports, fixtures | docs, reports, fixtures | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/validate-architecture.sh` | needs_later_classification | BLOCKED_PROTECTED | task_validation | workflow, docs, reports | workflow, docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/validate-boundary-claims.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/validate-commit-msg.py` | needs_later_classification | BLOCKED_PROTECTED | workflow_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/validate-contract-draft.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/validate-docs.py` | needs_later_classification | ACTIVE_CANDIDATE | documentation_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/validate-frontmatter.py` | needs_later_classification | ACTIVE_CANDIDATE | documentation_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/validate-gate-contract.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/validate-handoff.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/validate-human-approval.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports, fixtures | docs, reports, fixtures | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/validate-incident.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/validate-index.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/validate-lessons.py` | needs_later_classification | ACTIVE_CANDIDATE | documentation_helper | docs, reports | docs, reports | none | NEEDS_REVIEW | false | |
| `scripts/validate-lifecycle-apply.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/validate-policy.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports, fixtures | docs, reports, fixtures | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/validate-product-spec.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/validate-proposal-to-task-conversion.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports, fixtures | docs, reports, fixtures | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/validate-queue-entry.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/validate-queue.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/validate-required-sections.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/validate-review.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/validate-route.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/validate-runner-protocol.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/validate-status-semantics.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/validate-task-brief.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports, tasks, fixtures | docs, reports, tasks, fixtures | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/validate-task-contract-candidate.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/validate-task-state.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/validate-task.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | workflow, docs, reports, tasks | workflow, docs, reports, tasks | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/validate-trace.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/validate-ux-contract.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/validate-ux-planning-readiness.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/validate-ux-to-task-proposal.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | docs, reports | docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |
| `scripts/validate-verification.py` | needs_later_classification | BLOCKED_PROTECTED | task_validation | workflow, docs, reports | workflow, docs, reports | governance_critical_validator_or_runner | M71.4, M71.5 | false | |

## NEEDS_REVIEW Items

Total needs review items: 3
- `scripts/prepare-clean-template.py`
- `scripts/test-template-integrity-fixtures.py`
- `scripts/test-template-integrity.py`

## BLOCKED_UNKNOWN Items

Total blocked unknown items: 0


## BLOCKED_PROTECTED Items

Total blocked protected items: 130
- `install.sh`
- `scripts/agent-complete.py`
- `scripts/agent-fail.py`
- `scripts/agent-next.py`
- `scripts/agentos-audit-log.py`
- `scripts/agentos-command-guard.py`
- `scripts/agentos-enforce.py`
- `scripts/agentos-explain.py`
- `scripts/agentos-git-guard.py`
- `scripts/agentos-human-gate.py`
- `scripts/agentos-next-step.py`
- `scripts/agentos-permission-state.py`
- `scripts/agentos-retry-enforce.py`
- `scripts/agentos-status.py`
- `scripts/agentos-tui.py`
- `scripts/agentos-validate.py`
- `scripts/agentos-view-model.py`
- `scripts/agentos-violation-enforce.py`
- `scripts/agentos-write-guard.py`
- `scripts/agentos.py`
- `scripts/audit-agentos.py`
- `scripts/audit-approval-boundary.py`
- `scripts/audit-context-layer.py`
- `scripts/audit-enforcement.py`
- `scripts/audit-execution-control.py`
- `scripts/audit-gate-contract.py`
- `scripts/audit-lifecycle-mutation.py`
- `scripts/audit-m27-level1.py`
- `scripts/audit-m27.py`
- `scripts/audit-m30-context-pipeline.py`
- `scripts/audit-m31-tui-tutor.py`
- `scripts/audit-metadata-consistency.py`
- `scripts/audit-mvp-readiness.py`
- `scripts/audit-policy-boundary.py`
- `scripts/audit-pre-merge-corridor.py`
- `scripts/audit-release-readiness.py`
- `scripts/audit-template-packaging.py`
- `scripts/audit-validation-integration.py`
- `scripts/check-acceptance-criteria.py`
- `scripts/check-active-task-readiness.py`
- `scripts/check-agent-task-evidence.py`
- `scripts/check-apply-preconditions.py`
- `scripts/check-bypass-fixtures.py`
- `scripts/check-bypass-resistance.py`
- `scripts/check-canary-integrity.py`
- `scripts/check-commit-push-preconditions.py`
- `scripts/check-completion-readiness.py`
- `scripts/check-controlled-execution-session.py`
- `scripts/check-dangerous-commands.py`
- `scripts/check-evidence-amendments.py`
- `scripts/check-evidence-binding.py`
- `scripts/check-evidence-immutability.py`
- `scripts/check-execution-authorization.py`
- `scripts/check-execution-readiness.py`
- `scripts/check-execution-result-verification.py`
- `scripts/check-execution-scope.py`
- `scripts/check-execution-verification-chain.py`
- `scripts/check-execution-verification-registry.py`
- `scripts/check-execution-verification-regression.py`
- `scripts/check-false-pass-resistance.py`
- `scripts/check-github-platform-enforcement.py`
- `scripts/check-identity-drift.sh`
- `scripts/check-interview-completeness.py`
- `scripts/check-links.py`
- `scripts/check-llms-graph-files.sh`
- `scripts/check-m54-queue-placement-fixtures.py`
- `scripts/check-m55-active-task-readiness-fixtures.py`
- `scripts/check-m56-execution-readiness-fixtures.py`
- `scripts/check-m57-execution-authorization-fixtures.py`
- `scripts/check-m58-controlled-execution-session-fixtures.py`
- `scripts/check-m59-execution-result-verification-fixtures.py`
- `scripts/check-m61-hardening-regression.py`
- `scripts/check-pr-quality.py`
- `scripts/check-pre-merge-scope.py`
- `scripts/check-premature-artifacts.sh`
- `scripts/check-private-evaluator-consistency.py`
- `scripts/check-process-trace.py`
- `scripts/check-product-spec-readiness.py`
- `scripts/check-readiness-assertions.py`
- `scripts/check-risk.py`
- `scripts/check-role-separation.py`
- `scripts/check-scope-compliance.py`
- `scripts/check-single-role-execution.py`
- `scripts/check-task-acceptance-mvp.py`
- `scripts/check-task-validation-contract.py`
- `scripts/check-template-cleanliness.py`
- `scripts/check-template-integrity.py`
- `scripts/check-transition.py`
- `scripts/check-use-template-readiness.py`
- `scripts/check-validator-authority-boundary.py`
- `scripts/generate-repo-map.py`
- `scripts/generate-task-contract-candidate.py`
- `scripts/generate-task-contract.py`
- `scripts/generate-tasks-from-spec.py`
- `scripts/generate-tasks-from-ux.py`
- `scripts/materialize-task-candidate-placement.py`
- `scripts/review-task-candidate-placement.py`
- `scripts/run-all.sh`
- `scripts/sync-task-ids.py`
- `scripts/validate-active-task.py`
- `scripts/validate-approval-marker.py`
- `scripts/validate-architecture.sh`
- `scripts/validate-boundary-claims.py`
- `scripts/validate-commit-msg.py`
- `scripts/validate-contract-draft.py`
- `scripts/validate-gate-contract.py`
- `scripts/validate-handoff.py`
- `scripts/validate-human-approval.py`
- `scripts/validate-incident.py`
- `scripts/validate-index.py`
- `scripts/validate-lifecycle-apply.py`
- `scripts/validate-policy.py`
- `scripts/validate-product-spec.py`
- `scripts/validate-proposal-to-task-conversion.py`
- `scripts/validate-queue-entry.py`
- `scripts/validate-queue.py`
- `scripts/validate-required-sections.py`
- `scripts/validate-review.py`
- `scripts/validate-route.py`
- `scripts/validate-runner-protocol.py`
- `scripts/validate-status-semantics.py`
- `scripts/validate-task-brief.py`
- `scripts/validate-task-contract-candidate.py`
- `scripts/validate-task-state.py`
- `scripts/validate-task.py`
- `scripts/validate-trace.py`
- `scripts/validate-ux-contract.py`
- `scripts/validate-ux-planning-readiness.py`
- `scripts/validate-ux-to-task-proposal.py`
- `scripts/validate-verification.py`

## M71.4 Candidates

Total write/subprocess reviews proposed for M71.4: 147
(See [docs/SCRIPT-RESPONSIBILITY-MAP.md](file:///Users/muhammednazyrov/Documents/GitHub/AgentOS/docs/SCRIPT-RESPONSIBILITY-MAP.md))

## M71.5 Candidates

Total Git integration reviews proposed for M71.5: 46
(See [docs/SCRIPT-RESPONSIBILITY-MAP.md](file:///Users/muhammednazyrov/Documents/GitHub/AgentOS/docs/SCRIPT-RESPONSIBILITY-MAP.md))

## M71.6 Candidates

Total template setup reviews proposed for M71.6: 2
(See [docs/SCRIPT-RESPONSIBILITY-MAP.md](file:///Users/muhammednazyrov/Documents/GitHub/AgentOS/docs/SCRIPT-RESPONSIBILITY-MAP.md))

## Markdown / JSON Authority Check

- PRIMARY_INPUT: reports/m71-script-inventory.md
- SECONDARY_INPUT: docs/SCRIPT-RESPONSIBILITY-MAP.md
- NAVIGATION_HELPER: reports/m71-script-inventory.json
- markdown_inputs_used_as_primary: true
- json_used_as_navigation_only: true
- json_overrode_markdown: false

No JSON/Markdown authority conflict was observed. Markdown was used as the primary source of truth, with JSON serving as a navigation helper only. No new JSON artifacts were created by M71.3.

## Lifecycle Classification Boundary

No final lifecycle status decisions were made. No files were marked as DEPRECATED, REPLACED, REMOVE, DELETE, ARCHIVE_NOW, CANONICAL_FINAL, or APPROVED_FOR_CLEANUP.
final_lifecycle_classification_made: false

## Cleanup Non-Authorization Boundary

This classification map does not authorize cleanup.
cleanup_authorized: false

## Scope Compliance

No scripts, reports, schemas, workflows, or data files were modified. Changed files are strictly limited to tasks/active-task.md and docs/SCRIPT-LEGACY-AND-DUPLICATE-MAP.md.
scripts_modified: false
cleanup_performed: false
registries_created: false
validators_created: false
json_artifacts_created: false
scope_violations: false

## M71.4 Preparation Decision

may_prepare_m71_4: true_with_warnings

may_prepare_m71_4 is roadmap preparation only.
may_prepare_m71_4 does not start M71.4.
may_prepare_m71_4 is not approval.
Human review remains required.

Rationale: The script legacy and duplicate map has been compiled successfully. Warnings are carried forward because legacy duplicate items, unreferenced scripts, and safety-critical files are flagged for later task reviews.

## Explicit Non-Approval Boundary

This M71 legacy and duplicate map is evidence only.
This M71 legacy and duplicate map is not approval.
This M71 legacy and duplicate map does not authorize cleanup.
This M71 legacy and duplicate map does not authorize script changes.
This M71 legacy and duplicate map does not classify final lifecycle status.
This M71 legacy and duplicate map does not approve deletion, archiving, renaming, or moving files.
This M71 legacy and duplicate map does not create registry authority.
This M71 legacy and duplicate map does not authorize validator creation, fixture creation, or lifecycle mutation.
reports/m71-script-inventory.md is the source-of-truth inventory artifact.
reports/m71-script-inventory.json is a derived navigation artifact only.
reports/m71-script-inventory.json must not become source of truth.
Human review remains required.

## Final Status

FINAL_STATUS: M71_LEGACY_DUPLICATE_MAP_COMPLETE_WITH_WARNINGS
