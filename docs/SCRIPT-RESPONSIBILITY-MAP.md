# Script Responsibility Map
## Task Boundary
This script responsibility map is a planning artifact only.
This script responsibility map does not assign lifecycle status.
This script responsibility map does not authorize script cleanup, deletion, rename, move, merge, or refactor.
This script responsibility map does not decide final validation authority.
This script responsibility map does not create validators, registries, fixtures, or lifecycle mutation.
This script responsibility map does not approve M69.
Human review remains required.

## Active Task Record
- active_task_id: task-69.2
- milestone: M69
- mode: EXECUTION / READ-ONLY SCRIPT RESPONSIBILITY MAPPING

## Inputs Reviewed
- reports/m69-m68-completion-intake.md
- reports/m69-script-inventory-intake.md
- reports/m68-inventory.json
- reports/m68-duplicates.json
- reports/m68-protected-artifacts.json
- reports/m68-docs-to-code-drift.json
- reports/m68-anomaly-grep.txt
- docs/REPO-RESPONSIBILITY-MAP.md
- docs/REPO-ANOMALY-MAP.md
- docs/DUPLICATION-MAP.md
- scripts/
- .github/workflows/
- scripts/VALIDATORS.md

## M69.1 Inventory Status
- M69.1 intake status: `FINAL_STATUS: M69_SCRIPT_INVENTORY_INTAKE_COMPLETE_WITH_WARNINGS`
- M69.1 preparation value: `may_prepare_m69_2: true_with_warnings`

## Responsibility Mapping Model
M69.2 maps apparent script responsibilities only.
M69.2 does not assign lifecycle status.
M69.2 does not decide final validation authority.

## Validation-Related Scripts
- observed validation-related scripts include `scripts/agentos-validate.py`, `scripts/run-task-validation.py`, `scripts/validate-architecture.sh`, `scripts/validate-docs.py`, `scripts/validate-route.py`, `scripts/validate-runner-protocol.py`, `scripts/validate-task.py`, `scripts/validate-task-state.py`, `scripts/validate-required-sections.py`, `scripts/validate-status-semantics.py`, `scripts/check-task-validation-contract.py`, `scripts/check-acceptance-criteria.py`, `scripts/check-false-pass-resistance.py`, `scripts/check-validator-authority-boundary.py`, `scripts/check-execution-readiness.py`, `scripts/check-completion-readiness.py`
- validation-related support references also include `scripts/VALIDATORS.md`

## Runner / Dispatcher-Related Scripts
- observed runner/dispatcher-like scripts include `scripts/run-all.sh`, `scripts/run-active-task.py`, `scripts/run-execution-verification.py`, `scripts/run-task-validation.py`, `scripts/agentos.py`, `scripts/agentos-enforce.py`, `scripts/agentos-next-step.py`, `scripts/agentos-status.py`, `scripts/agent-next.py`, `scripts/complete-active-task.py`, `scripts/activate-task.py`, `scripts/detect-task-state.py`

## Audit-Related Scripts
- observed audit-like scripts include `scripts/audit-agentos.py`, `scripts/audit-enforcement.py`, `scripts/audit-execution-control.py`, `scripts/audit-gate-contract.py`, `scripts/audit-lifecycle-mutation.py`, `scripts/audit-pre-merge-corridor.py`, `scripts/audit-validation-integration.py`, `scripts/audit-metadata-consistency.py`, `scripts/audit-mvp-readiness.py`, `scripts/audit-release-readiness.py`, `scripts/audit-template-packaging.py`

## Evidence / Report-Related Scripts
- observed evidence/report-related scripts include `scripts/agentos-audit-log.py`, `scripts/check-evidence-binding.py`, `scripts/check-evidence-immutability.py`, `scripts/check-evidence-amendments.py`, `scripts/check-execution-result-verification.py`, `scripts/check-execution-verification-chain.py`, `scripts/check-execution-verification-registry.py`, `scripts/check-execution-verification-regression.py`, `scripts/build-execution-verification-registry.py`, `scripts/build-context-index.py`, `scripts/build-context-cache.py`, `scripts/build-index.py`, `scripts/generate-repo-map.py`

## Task / Lifecycle-Related Scripts
- observed task/lifecycle-related scripts include `scripts/activate-task.py`, `scripts/complete-active-task.py`, `scripts/run-active-task.py`, `scripts/validate-active-task.py`, `scripts/validate-task-state.py`, `scripts/validate-task.py`, `scripts/detect-task-state.py`, `scripts/apply-transition.py`, `scripts/validate-lifecycle-apply.py`, `scripts/audit-lifecycle-mutation.py`, `scripts/validate-queue.py`, `scripts/validate-queue-entry.py`, `scripts/validate-task-brief.py`, `scripts/validate-task-contract-candidate.py`, `scripts/build-task-dependency-map.py`, `scripts/sync-task-ids.py`

## Scope / Governance-Related Scripts
- observed scope/governance-related scripts include `scripts/agentos-command-guard.py`, `scripts/agentos-write-guard.py`, `scripts/agentos-git-guard.py`, `scripts/agentos-human-gate.py`, `scripts/agentos-permission-state.py`, `scripts/agentos-retry-enforce.py`, `scripts/agentos-violation-enforce.py`, `scripts/check-execution-scope.py`, `scripts/check-pre-merge-scope.py`, `scripts/check-scope-compliance.py`, `scripts/check-risk.py`, `scripts/check-dangerous-commands.py`, `scripts/validate-boundary-claims.py`, `scripts/validate-gate-contract.py`, `scripts/validate-policy.py`, `scripts/validate-human-approval.py`, `scripts/validate-approval-marker.py`, `scripts/check-pr-quality.py`

## GitHub / Workflow-Related Script References
- observed workflow references include `.github/workflows/agentos-validate.yml`, `.github/workflows/dev-only/agentos-validation.yml`, `.github/workflows/dev-only/context-pipeline.yml`, `.github/workflows/dev-only/modular-validators.yml`, `.github/workflows/dev-only/health.yml`, `.github/workflows/setup-repository.yml`, `.github/workflows/init-from-template.yml`
- workflow references point to `scripts/agentos-validate.py`, `scripts/run-all.sh`, `scripts/validate-task.py`, `scripts/check-dangerous-commands.py`, `scripts/check-risk.py`, `scripts/validate-architecture.sh`, and `scripts/health-check.sh`

## Fixture / Support-Related Scripts
- observed fixture/support-related scripts include `scripts/test-*-fixtures.py` families, `scripts/check-m54-queue-placement-fixtures.py`, `scripts/check-m55-active-task-readiness-fixtures.py`, `scripts/check-m56-execution-readiness-fixtures.py`, `scripts/check-m57-execution-authorization-fixtures.py`, `scripts/check-m58-controlled-execution-session-fixtures.py`, `scripts/check-m59-execution-result-verification-fixtures.py`, `scripts/check-bypass-fixtures.py`, `scripts/check-pre-merge-scope-fixtures.py`, `scripts/check-scope-compliance-fixtures.py`
- support scripts also include `scripts/test-*.sh` smoke/helpers such as `scripts/test-example-project.sh`, `scripts/test-install.sh`

## Template / Install-Related Scripts
- observed template/install-related scripts include `scripts/install-agentos.py`, `scripts/install-hooks.sh`, `scripts/check-template-integrity.py`, `scripts/test-template-integrity.py`, `scripts/check-template-cleanliness.py`, `scripts/validate-ux-to-task-proposal.py`, `scripts/generate-task-contract-candidate.py`, `scripts/generate-tasks-from-spec.py`, `scripts/generate-repo-map.py`

## Protected Script Artifacts
- protected artifacts observed as present: `schemas/task-validation-package.schema.json`, `schemas/task-validation-result.schema.json`, `scripts/check-task-validation-contract.py`, `schemas/agent-task-output-evidence.schema.json`, `scripts/check-agent-task-evidence.py`, `schemas/acceptance-criteria-check-package.schema.json`, `scripts/check-acceptance-criteria.py`, `schemas/unified-runner-input.schema.json`, `scripts/run-task-validation.py`, `scripts/check-false-pass-resistance.py`, `tests/fixtures/m67-false-pass-resistance/`, `docs/COMPLETION-GATE-HARDENING-CONTRACT.md`, `reports/m63-completion-review.md`, `reports/m64-completion-review.md`, `reports/m65-completion-review.md`, `reports/m66-completion-review.md`, `reports/m67-completion-review.md`
- protected artifacts are recorded for later review only; no correctness decision is made here

## Unknown Responsibility Scripts
- `scripts/build-context-cache.py` — unknown responsibility — requires M69.3 lifecycle classification
- `scripts/build-context-index.py` — unknown responsibility — requires M69.3 lifecycle classification
- `scripts/generate-repo-map.py` — unknown responsibility — requires M69.3 lifecycle classification
- `scripts/smoke-interview-layer.py` — unknown responsibility — requires M69.3 lifecycle classification
- `scripts/agentos-explain.py` — unknown responsibility — requires M69.3 lifecycle classification
- `scripts/agentos-view-model.py` — unknown responsibility — requires M69.3 lifecycle classification
- `scripts/install-agentos.py` — unknown responsibility — requires M69.3 lifecycle classification
- additional long-tail scripts that do not clearly fit the above groups require later M69 classification

## Validation Authority Drift Signals
- observed drift references include `scripts/agentos-validate.py`, `scripts/run-all.sh`, `scripts/VALIDATORS.md`, `.github/workflows/agentos-validate.yml`
- observed drift evidence also includes workflow references to human-readable and JSON validation paths
- M69.2 records the ambiguity only; it does not decide final validation authority

## Items Requiring M69.3 Lifecycle Classification
- validation-related scripts and workflow references above
- runner/dispatcher-related scripts and workflow references above
- audit-related scripts above
- task/lifecycle-related scripts above
- unknown responsibility scripts above
- protected script artifacts above

## Explicit Non-Lifecycle Boundary
- This map is a planning artifact only.
- It does not assign lifecycle status.
- It does not authorize script cleanup, deletion, rename, move, merge, or refactor.
- It does not decide final validation authority.
- It does not create validators, registries, fixtures, or lifecycle mutation.
- It does not approve M69.
- Human review remains required.

## M69.3 Preparation Decision
may_prepare_m69_3: true_with_warnings
may_prepare_m69_3 is roadmap preparation only.
may_prepare_m69_3 does not start M69.3.
may_prepare_m69_3 is not approval.

## Final Status
FINAL_STATUS: M69_SCRIPT_RESPONSIBILITY_MAP_COMPLETE_WITH_WARNINGS
