# Script Lifecycle Policy
## Task Boundary
This script lifecycle policy is a planning artifact only.
This script lifecycle policy does not authorize script cleanup, deletion, rename, move, merge, or refactor.
This script lifecycle policy does not decide final validation authority.
This script lifecycle policy does not create validators, registries, fixtures, or lifecycle mutation.
This script lifecycle policy does not approve M69.
Human review remains required.

## Active Task Record
- active_task_id: task-69.3
- milestone: M69
- mode: EXECUTION / READ-ONLY SCRIPT LIFECYCLE CLASSIFICATION

## Inputs Reviewed
- reports/m69-m68-completion-intake.md
- reports/m69-script-inventory-intake.md
- docs/SCRIPT-RESPONSIBILITY-MAP.md
- reports/m68-inventory.json
- reports/m68-duplicates.json
- reports/m68-protected-artifacts.json
- reports/m68-docs-to-code-drift.json
- reports/m68-anomaly-grep.txt
- docs/REPO-ANOMALY-MAP.md
- docs/DUPLICATION-MAP.md
- scripts/
- .github/workflows/
- scripts/VALIDATORS.md

## M69.2 Responsibility Map Status
- M69.2 status: `FINAL_STATUS: M69_SCRIPT_RESPONSIBILITY_MAP_COMPLETE_WITH_WARNINGS`
- M69.2 preparation value: `may_prepare_m69_3: true_with_warnings`

## Lifecycle Status Vocabulary
ACTIVE
LEGACY
DEPRECATED
REPLACED
CANDIDATE_FOR_MERGE
CANDIDATE_FOR_REMOVAL
DANGEROUS_REQUIRES_REVIEW
NEEDS_REVIEW
BLOCKED
PROTECTED
UNKNOWN

## Classification Rules
Lifecycle classification is planning evidence only.
Lifecycle classification does not authorize cleanup.
Lifecycle classification does not authorize deletion.
Lifecycle classification does not authorize merge.
Lifecycle classification does not authorize refactor.
Lifecycle classification does not decide validation authority.
Human review remains required.

## Protected Script Classification Rules
Any protected M61–M67 script must be classified as PROTECTED or PROTECTED plus an advisory note.
Protected classification does not mean the script is correct.
Protected classification only means modification requires human checkpoint.

## ACTIVE Classifications
- `scripts/agentos-validate.py`
- `scripts/run-all.sh`
- `scripts/validate-architecture.sh`
- `scripts/validate-docs.py`
- `scripts/validate-route.py`
- `scripts/check-links.py`
- `scripts/check-llms-graph-files.sh`
- `scripts/health-check.sh`
- `scripts/run-task-validation.py`
- `scripts/check-execution-readiness.py`
- `scripts/check-completion-readiness.py`
- `scripts/check-task-validation-contract.py` is protected and therefore not a normal ACTIVE target; see PROTECTED

## LEGACY Classifications
- No script was strongly supported as LEGACY by current evidence.
- Where the evidence is weak or mixed, use NEEDS_REVIEW or UNKNOWN instead.

## DEPRECATED Classifications
- No script was strongly supported as DEPRECATED by current evidence.
- Existing evidence does not justify final deprecation wording.

## REPLACED Classifications
- No script was strongly supported as REPLACED by current evidence.
- Numbered duplicate-name files may look replace-like, but that is not yet a final replacement decision.

## CANDIDATE_FOR_MERGE Classifications
- `scripts/audit-m27.py` and `scripts/audit-m27 3.py` family
- `scripts/audit-m27-level1.py` and `scripts/audit-m27-level1 3.py` family
- `scripts/test-scope-compliance-fixtures.py` and `scripts/test-scope-compliance-fixtures 3.py` family
- `scripts/validate-frontmatter.py` and `scripts/validate-frontmatter 3.py` family
- `scripts/validate-status-semantics.py` and `scripts/validate-status-semantics 3.py` family
- `scripts/validate-required-sections.py` and `scripts/validate-required-sections 3.py` family
- candidate only
- requires human review
- not approved for cleanup

## CANDIDATE_FOR_REMOVAL Classifications
- `scripts/audit-metadata-consistency 3.py`
- `scripts/audit-pre-merge-corridor 3.py`
- `scripts/audit-validation-integration 3.py`
- `scripts/build-index 3.py`
- `scripts/check-commit-push-preconditions 3.py`
- `scripts/check-github-platform-enforcement 3.py`
- `scripts/check-pre-merge-scope 3.py`
- `scripts/check-scope-compliance 3.py`
- `scripts/test-ci-advisory-config 3.py`
- `scripts/test-enforcement-fixtures 3.py`
- `scripts/test-m22-guardrails 3.py`
- `scripts/test-m27-level1-fixtures 3.py`
- candidate only
- requires human review
- not approved for cleanup

## DANGEROUS_REQUIRES_REVIEW Classifications
- `scripts/agentos-command-guard.py`
- `scripts/agentos-write-guard.py`
- `scripts/agentos-git-guard.py`
- `scripts/agentos-enforce.py`
- `scripts/agentos-violation-enforce.py`
- `scripts/install-agentos.py`
- `scripts/check-commit-push-preconditions.py`
- `scripts/check-dangerous-commands.py`
- `scripts/apply-transition.py`
- `scripts/validate-lifecycle-apply.py`
- `scripts/check-transition.py`
- raw clues include `rm -rf`, `git push`, `git reset`, file writes, and subprocess-driven enforcement
- requires human review
- not approved for cleanup

## NEEDS_REVIEW Classifications
- `scripts/build-context-cache.py`
- `scripts/build-context-index.py`
- `scripts/build-task-dependency-map.py`
- `scripts/generate-repo-map.py`
- `scripts/smoke-interview-layer.py`
- `scripts/agentos-explain.py`
- `scripts/agentos-view-model.py`
- `scripts/install-hooks.sh`
- `scripts/sync-context.sh`
- `scripts/check-pr-quality.py`
- `scripts/validate-ux-contract.py`
- `scripts/validate-policy.py`
- `scripts/validate-task-brief.py`
- `scripts/validate-runner-protocol.py`

## BLOCKED Classifications
- No script was assigned BLOCKED in this intake.

## PROTECTED Classifications
- `schemas/task-validation-package.schema.json`
- `schemas/task-validation-result.schema.json`
- `scripts/check-task-validation-contract.py`
- `schemas/agent-task-output-evidence.schema.json`
- `scripts/check-agent-task-evidence.py`
- `schemas/acceptance-criteria-check-package.schema.json`
- `scripts/check-acceptance-criteria.py`
- `schemas/unified-runner-input.schema.json`
- `scripts/run-task-validation.py`
- `scripts/check-false-pass-resistance.py`
- `tests/fixtures/m67-false-pass-resistance/`
- `docs/COMPLETION-GATE-HARDENING-CONTRACT.md`
- `reports/m63-completion-review.md`
- `reports/m64-completion-review.md`
- `reports/m65-completion-review.md`
- `reports/m66-completion-review.md`
- `reports/m67-completion-review.md`
- all are PROTECTED because they are protected artifacts, not because they are proven correct

## UNKNOWN Classifications
- `scripts/agentos.py`
- `scripts/agentos-next-step.py`
- `scripts/agentos-status.py`
- `scripts/agentos-tui.py`
- `scripts/audit-agentos.py`
- `scripts/check-risk.py`
- `scripts/check-template-cleanliness.py`
- `scripts/check-template-integrity.py`
- `scripts/check-product-spec-readiness.py`
- `scripts/check-task-acceptance-mvp.py`
- `scripts/generate-task-contract-candidate.py`
- `scripts/generate-tasks-from-spec.py`
- `scripts/materialize-task-candidate-placement.py`
- `scripts/review-task-candidate-placement.py`
- `scripts/validate-queue-entry.py`
- `scripts/validate-queue.py`
- unknown responsibility or insufficient evidence

## Validation Authority Classification Notes
- Current ambiguity remains among `scripts/agentos-validate.py`, `scripts/run-all.sh`, `scripts/VALIDATORS.md`, and `.github/workflows/agentos-validate.yml`
- The policy records drift signals only and does not decide a final winner

## Active-Tree Ambiguity Classification Notes
- Numbered variants such as `scripts/* 3.py` remain ambiguous and require later review
- `scripts/run-all.sh` and template run-all copies remain a key later review surface
- `__pycache__` and HANDOFF 2.md signals remain part of the later active-tree review surface

## Human Review Requirements
- Human review is required before deleting any script
- Human review is required before renaming any script
- Human review is required before moving any script
- Human review is required before merging script variants
- Human review is required before changing validation authority
- Human review is required before changing protected scripts
- Human review is required before changing output/exit-code semantics
- Human review is required before changing workflow script references

## Explicit Non-Cleanup Boundary
- This script lifecycle policy does not authorize script cleanup, deletion, rename, move, merge, or refactor.
- This script lifecycle policy does not decide final validation authority.
- This script lifecycle policy does not create validators, registries, fixtures, or lifecycle mutation.
- This script lifecycle policy does not approve M69.
- Human review remains required.

## M69.4 Preparation Decision
may_prepare_m69_4: true_with_warnings
may_prepare_m69_4 is roadmap preparation only.
may_prepare_m69_4 does not start M69.4.
may_prepare_m69_4 is not approval.

## Final Status
FINAL_STATUS: M69_SCRIPT_LIFECYCLE_CLASSIFICATION_COMPLETE_WITH_WARNINGS
