## Executive Summary
M43.5 does not delete, move, merge, rename, rewrite, or deprecate scripts.
Script entrypoint planning is repository hygiene, not runtime authority.
Script name similarity is not proof of duplicate behavior.
Standalone checker behavior must not become harder to validate during CLI simplification.
Do not invent references.

## Inventory Scope
Read-only scope: recursive `scripts/` inventory with references from README/docs/reports/templates/schemas/fixtures/scripts.

## Script Count Summary
Total script paths reviewed: 225
Discovered scripts count: 225
Listed script inventory rows count: 225
Intentionally excluded scripts: 0
Primary user entrypoints: 2
Primary validation entrypoints: 1
Unified CLI entrypoints: 1
Standalone checkers: 38
Test runners: 12
Fixture runners: 28
Internal helpers: 79
Wrapper scripts: 23
Simplification candidates: 155
Keep standalone: 69
Unknown needs review: 1

## Enumeration Method
Script enumeration must be recursive under scripts/
```bash
find scripts -type f | sort
```

## Primary Entrypoints
- Count: 3
## Unified CLI Entrypoints
- Count: 1
## Standalone Checkers
- Count: 38
## Test / Fixture Runners
- Count: 40
## Internal Helpers
- Count: 79
## Wrapper Scripts
- Count: 23
## Simplification Candidates
- Count: 155
## Keep Standalone
- Count: 69
## Unknown / Needs Review
- Count: 1

### Classification Presence Summary
- PRIMARY_USER_ENTRYPOINT: 2
- PRIMARY_VALIDATION_ENTRYPOINT: 1
- UNIFIED_CLI_ENTRYPOINT: 1
- STANDALONE_CHECKER: 38
- TEST_RUNNER: 12
- FIXTURE_RUNNER: 28
- INTERNAL_HELPER: 79
- WRAPPER_SCRIPT: 23
- LEGACY_OR_HISTORICAL: 40
- SIMPLIFICATION_CANDIDATE: 0
- KEEP_STANDALONE: 0
- UNKNOWN_NEEDS_REVIEW: 1

Script Path | Classification | Current Role | Referenced By | Invocation Pattern | Wrap/Unify Candidate | Recommended Action | Notes
--- | --- | --- | --- | --- | --- | --- | ---
| scripts/VALIDATORS.md | UNKNOWN_NEEDS_REVIEW | script role not fully verified | unknown_needs_review | unknown_needs_review | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | needs deeper behavior audit |
| scripts/__pycache__/agent-complete.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/agent-fail.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/agent-next.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/agentos-explain.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/agentos-next-step.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/agentos-status.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/agentos-tui.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/agentos-validate.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/agentos-view-model.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/agentos.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/apply-transition.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/audit-enforcement.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/audit-execution-control.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/audit-m31-tui-tutor.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/audit-policy-boundary.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/audit-release-readiness.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/audit-validation-integration.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/check-apply-preconditions.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/check-completion-readiness.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/check-scope-compliance.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/check-template-integrity.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/complete-active-task.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/generate-task-contract.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/install-agentos.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/test-ci-advisory-config.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/test-enforcement-fixtures.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/test-integrity-regression.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/test-policy-enforcement-fixtures.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/test-policy-fixtures.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/test-policy-flow-smoke.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/test-scope-compliance-fixtures.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/test-template-integrity-fixtures.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/validate-commit-msg.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/validate-policy.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/validate-task.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/__pycache__/validate-verification.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/activate-task.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/activate-task.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/agent-complete.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/agent-complete.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/agent-fail.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/agent-fail.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/agent-next.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/agent-next.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/agentos-audit-log.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/agentos-audit-log.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/agentos-command-guard.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/agentos-command-guard.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/agentos-enforce.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/agentos-enforce.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/agentos-explain.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/agentos-explain.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/agentos-git-guard.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/agentos-git-guard.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/agentos-human-gate.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/agentos-human-gate.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/agentos-next-step.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/agentos-next-step.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/agentos-permission-state.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/agentos-permission-state.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/agentos-retry-enforce.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/agentos-retry-enforce.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/agentos-status.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/agentos-status.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/agentos-tui.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/agentos-tui.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/agentos-validate.py | UNIFIED_CLI_ENTRYPOINT | unified validation CLI | README.md;docs/VALIDATION.md;reports/m41-6-unified-integrity-closure-report.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/agentos-validate.py <subcommand> | KEEP_STANDALONE | DO_NOT_TOUCH | primary integrated entrypoint |
| scripts/agentos-view-model.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/agentos-view-model.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/agentos-violation-enforce.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/agentos-violation-enforce.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/agentos-write-guard.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/agentos-write-guard.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/agentos.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/agentos.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/apply-transition.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/apply-transition.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/audit-agentos.py | WRAPPER_SCRIPT | audit wrapper/aggregator | reports/milestone-20-evidence-report.md | python3 scripts/audit-agentos.py | SIMPLIFICATION_CANDIDATE | WRAP_LATER | aggregates checks |
| scripts/audit-approval-boundary.py | WRAPPER_SCRIPT | audit wrapper/aggregator | reports/milestone-20-evidence-report.md | python3 scripts/audit-approval-boundary.py | SIMPLIFICATION_CANDIDATE | WRAP_LATER | aggregates checks |
| scripts/audit-context-layer.py | WRAPPER_SCRIPT | audit wrapper/aggregator | reports/milestone-20-evidence-report.md | python3 scripts/audit-context-layer.py | SIMPLIFICATION_CANDIDATE | WRAP_LATER | aggregates checks |
| scripts/audit-enforcement.py | WRAPPER_SCRIPT | audit wrapper/aggregator | reports/milestone-20-evidence-report.md | python3 scripts/audit-enforcement.py | SIMPLIFICATION_CANDIDATE | WRAP_LATER | aggregates checks |
| scripts/audit-execution-control.py | WRAPPER_SCRIPT | audit wrapper/aggregator | reports/milestone-20-evidence-report.md | python3 scripts/audit-execution-control.py | SIMPLIFICATION_CANDIDATE | WRAP_LATER | aggregates checks |
| scripts/audit-gate-contract.py | WRAPPER_SCRIPT | audit wrapper/aggregator | reports/milestone-20-evidence-report.md | python3 scripts/audit-gate-contract.py | SIMPLIFICATION_CANDIDATE | WRAP_LATER | aggregates checks |
| scripts/audit-lifecycle-mutation.py | WRAPPER_SCRIPT | audit wrapper/aggregator | reports/milestone-20-evidence-report.md | python3 scripts/audit-lifecycle-mutation.py | SIMPLIFICATION_CANDIDATE | WRAP_LATER | aggregates checks |
| scripts/audit-m27 3.py | WRAPPER_SCRIPT | audit wrapper/aggregator | reports/milestone-20-evidence-report.md | python3 scripts/audit-m27 3.py | SIMPLIFICATION_CANDIDATE | WRAP_LATER | aggregates checks |
| scripts/audit-m27-level1 3.py | WRAPPER_SCRIPT | audit wrapper/aggregator | reports/milestone-20-evidence-report.md | python3 scripts/audit-m27-level1 3.py | SIMPLIFICATION_CANDIDATE | WRAP_LATER | aggregates checks |
| scripts/audit-m27-level1.py | WRAPPER_SCRIPT | audit wrapper/aggregator | reports/milestone-20-evidence-report.md | python3 scripts/audit-m27-level1.py | SIMPLIFICATION_CANDIDATE | WRAP_LATER | aggregates checks |
| scripts/audit-m27.py | WRAPPER_SCRIPT | audit wrapper/aggregator | reports/milestone-20-evidence-report.md | python3 scripts/audit-m27.py | SIMPLIFICATION_CANDIDATE | WRAP_LATER | aggregates checks |
| scripts/audit-m30-context-pipeline.py | WRAPPER_SCRIPT | audit wrapper/aggregator | reports/milestone-20-evidence-report.md | python3 scripts/audit-m30-context-pipeline.py | SIMPLIFICATION_CANDIDATE | WRAP_LATER | aggregates checks |
| scripts/audit-m31-tui-tutor.py | WRAPPER_SCRIPT | audit wrapper/aggregator | reports/milestone-20-evidence-report.md | python3 scripts/audit-m31-tui-tutor.py | SIMPLIFICATION_CANDIDATE | WRAP_LATER | aggregates checks |
| scripts/audit-metadata-consistency 3.py | WRAPPER_SCRIPT | audit wrapper/aggregator | reports/milestone-20-evidence-report.md | python3 scripts/audit-metadata-consistency 3.py | SIMPLIFICATION_CANDIDATE | WRAP_LATER | aggregates checks |
| scripts/audit-metadata-consistency.py | WRAPPER_SCRIPT | audit wrapper/aggregator | reports/milestone-20-evidence-report.md | python3 scripts/audit-metadata-consistency.py | SIMPLIFICATION_CANDIDATE | WRAP_LATER | aggregates checks |
| scripts/audit-mvp-readiness.py | WRAPPER_SCRIPT | audit wrapper/aggregator | reports/milestone-20-evidence-report.md | python3 scripts/audit-mvp-readiness.py | SIMPLIFICATION_CANDIDATE | WRAP_LATER | aggregates checks |
| scripts/audit-policy-boundary.py | WRAPPER_SCRIPT | audit wrapper/aggregator | reports/milestone-20-evidence-report.md | python3 scripts/audit-policy-boundary.py | SIMPLIFICATION_CANDIDATE | WRAP_LATER | aggregates checks |
| scripts/audit-pre-merge-corridor 3.py | WRAPPER_SCRIPT | audit wrapper/aggregator | reports/milestone-20-evidence-report.md | python3 scripts/audit-pre-merge-corridor 3.py | SIMPLIFICATION_CANDIDATE | WRAP_LATER | aggregates checks |
| scripts/audit-pre-merge-corridor.py | WRAPPER_SCRIPT | audit wrapper/aggregator | reports/milestone-20-evidence-report.md | python3 scripts/audit-pre-merge-corridor.py | SIMPLIFICATION_CANDIDATE | WRAP_LATER | aggregates checks |
| scripts/audit-release-readiness.py | WRAPPER_SCRIPT | audit wrapper/aggregator | reports/milestone-20-evidence-report.md | python3 scripts/audit-release-readiness.py | SIMPLIFICATION_CANDIDATE | WRAP_LATER | aggregates checks |
| scripts/audit-template-packaging.py | WRAPPER_SCRIPT | audit wrapper/aggregator | reports/milestone-20-evidence-report.md | python3 scripts/audit-template-packaging.py | SIMPLIFICATION_CANDIDATE | WRAP_LATER | aggregates checks |
| scripts/audit-validation-integration 3.py | WRAPPER_SCRIPT | audit wrapper/aggregator | reports/milestone-20-evidence-report.md | python3 scripts/audit-validation-integration 3.py | SIMPLIFICATION_CANDIDATE | WRAP_LATER | aggregates checks |
| scripts/audit-validation-integration.py | WRAPPER_SCRIPT | audit wrapper/aggregator | reports/milestone-20-evidence-report.md | python3 scripts/audit-validation-integration.py | SIMPLIFICATION_CANDIDATE | WRAP_LATER | aggregates checks |
| scripts/build-context-cache.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/build-context-cache.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/build-context-index.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/build-context-index.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/build-index 3.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/build-index 3.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/build-index.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/build-index.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/canonical-cleanup.sh | INTERNAL_HELPER | internal helper script | unknown_needs_review | bash scripts/canonical-cleanup.sh | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/check-apply-preconditions.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-apply-preconditions.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-bypass-fixtures.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-bypass-fixtures.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-bypass-resistance.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-bypass-resistance.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-canary-integrity.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-canary-integrity.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-commit-push-preconditions 3.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-commit-push-preconditions 3.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-commit-push-preconditions.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-commit-push-preconditions.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-completion-readiness.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-completion-readiness.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-context-compliance.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-context-compliance.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-context-index-freshness.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-context-index-freshness.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-context-pipeline.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-context-pipeline.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-context-required.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-context-required.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-dangerous-commands.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-dangerous-commands.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-evidence-amendments.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-evidence-amendments.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-evidence-binding.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-evidence-binding.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-evidence-immutability.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-evidence-immutability.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-execution-readiness.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-execution-readiness.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-execution-scope.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-execution-scope.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-github-platform-enforcement 3.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-github-platform-enforcement 3.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-github-platform-enforcement.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-github-platform-enforcement.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-identity-drift.sh | INTERNAL_HELPER | internal helper script | unknown_needs_review | bash scripts/check-identity-drift.sh | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/check-links.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-links.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-llms-graph-files.sh | INTERNAL_HELPER | internal helper script | unknown_needs_review | bash scripts/check-llms-graph-files.sh | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/check-pr-quality.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-pr-quality.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-pre-merge-scope 3.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-pre-merge-scope 3.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-pre-merge-scope.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-pre-merge-scope.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-private-evaluator-consistency.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-private-evaluator-consistency.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-process-trace.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-process-trace.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-readiness-assertions.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-readiness-assertions.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-required-context-compliance.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-required-context-compliance.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-required-context-pack.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-required-context-pack.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-risk.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-risk.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-role-separation.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-role-separation.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-scope-compliance 3.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-scope-compliance 3.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-scope-compliance.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-scope-compliance.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-single-role-execution.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-single-role-execution.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-template-cleanliness.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-template-cleanliness.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-template-integrity.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-template-integrity.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-transition.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-transition.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-use-template-readiness.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-use-template-readiness.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/check-validator-authority-boundary.py | STANDALONE_CHECKER | standalone checker | scripts/agentos-validate.py;reports/m40-13-full-honest-pass-closure-report.md | python3 scripts/check-validator-authority-boundary.py | KEEP_STANDALONE | KEEP | direct diagnostics source |
| scripts/complete-active-task.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/complete-active-task.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/detect-task-state.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/detect-task-state.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/generate-repo-map.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/generate-repo-map.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/generate-task-contract.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/generate-task-contract.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/health-check.sh | INTERNAL_HELPER | internal helper script | unknown_needs_review | bash scripts/health-check.sh | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/install-agentos.py | PRIMARY_USER_ENTRYPOINT | installation/bootstrap entrypoint | README.md;docs/installation.md | python3 scripts/install-agentos.py | KEEP_STANDALONE | DO_NOT_TOUCH | user onboarding path |
| scripts/install-hooks.sh | PRIMARY_USER_ENTRYPOINT | installation/bootstrap entrypoint | README.md;docs/installation.md | bash scripts/install-hooks.sh | KEEP_STANDALONE | DO_NOT_TOUCH | user onboarding path |
| scripts/lib/__init__.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/lib/__init__.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/lib/__pycache__/__init__.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/lib/__pycache__/path_utils.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/lib/path_utils.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/lib/path_utils.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/prepare-clean-template.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/prepare-clean-template.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/renderers/__init__.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/renderers/__init__.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/renderers/__pycache__/plain_status_renderer.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/renderers/__pycache__/rich_status_renderer.cpython-314.pyc | LEGACY_OR_HISTORICAL | compiled cache artifact | none_found | not_directly_invoked | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | not primary command surface |
| scripts/renderers/plain_status_renderer.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/renderers/plain_status_renderer.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/renderers/rich_status_renderer.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/renderers/rich_status_renderer.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/run-active-task.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/run-active-task.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/run-all.sh | PRIMARY_VALIDATION_ENTRYPOINT | high-level validation entry | README.md;docs/VALIDATION.md | bash scripts/run-all.sh | WRAPPER_SCRIPT | KEEP_AND_DOCUMENT | entry wrapper around validation commands |
| scripts/run-execution-verification.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/run-execution-verification.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/select-context.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/select-context.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/sync-context.sh | INTERNAL_HELPER | internal helper script | unknown_needs_review | bash scripts/sync-context.sh | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/sync-task-ids.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/sync-task-ids.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/task-health.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/task-health.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/test-activation-fixtures.py | FIXTURE_RUNNER | fixture runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-activation-fixtures.py | KEEP_STANDALONE | KEEP | fixture semantics sensitive |
| scripts/test-active-task-fixtures.py | FIXTURE_RUNNER | fixture runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-active-task-fixtures.py | KEEP_STANDALONE | KEEP | fixture semantics sensitive |
| scripts/test-apply-transition-fixtures.py | FIXTURE_RUNNER | fixture runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-apply-transition-fixtures.py | KEEP_STANDALONE | KEEP | fixture semantics sensitive |
| scripts/test-approval-fixtures.py | FIXTURE_RUNNER | fixture runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-approval-fixtures.py | KEEP_STANDALONE | KEEP | fixture semantics sensitive |
| scripts/test-approval-flow-smoke.py | TEST_RUNNER | test runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-approval-flow-smoke.py | SIMPLIFICATION_CANDIDATE | UNIFY_LATER | candidate for command surface simplification |
| scripts/test-approval-marker-fixtures.py | FIXTURE_RUNNER | fixture runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-approval-marker-fixtures.py | KEEP_STANDALONE | KEEP | fixture semantics sensitive |
| scripts/test-ci-advisory-config 3.py | TEST_RUNNER | test runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-ci-advisory-config 3.py | SIMPLIFICATION_CANDIDATE | UNIFY_LATER | candidate for command surface simplification |
| scripts/test-ci-advisory-config.py | TEST_RUNNER | test runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-ci-advisory-config.py | SIMPLIFICATION_CANDIDATE | UNIFY_LATER | candidate for command surface simplification |
| scripts/test-commit-push-preconditions-fixtures 3.py | FIXTURE_RUNNER | fixture runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-commit-push-preconditions-fixtures 3.py | KEEP_STANDALONE | KEEP | fixture semantics sensitive |
| scripts/test-commit-push-preconditions-fixtures.py | FIXTURE_RUNNER | fixture runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-commit-push-preconditions-fixtures.py | KEEP_STANDALONE | KEEP | fixture semantics sensitive |
| scripts/test-completion-flow-smoke.py | TEST_RUNNER | test runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-completion-flow-smoke.py | SIMPLIFICATION_CANDIDATE | UNIFY_LATER | candidate for command surface simplification |
| scripts/test-enforcement-fixtures 3.py | FIXTURE_RUNNER | fixture runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-enforcement-fixtures 3.py | KEEP_STANDALONE | KEEP | fixture semantics sensitive |
| scripts/test-enforcement-fixtures.py | FIXTURE_RUNNER | fixture runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-enforcement-fixtures.py | KEEP_STANDALONE | KEEP | fixture semantics sensitive |
| scripts/test-example-project.sh | INTERNAL_HELPER | internal helper script | unknown_needs_review | bash scripts/test-example-project.sh | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/test-execution-runner-fixtures.py | FIXTURE_RUNNER | fixture runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-execution-runner-fixtures.py | KEEP_STANDALONE | KEEP | fixture semantics sensitive |
| scripts/test-gate-regression-fixtures.py | FIXTURE_RUNNER | fixture runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-gate-regression-fixtures.py | KEEP_STANDALONE | KEEP | fixture semantics sensitive |
| scripts/test-guard-failures.py | TEST_RUNNER | test runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-guard-failures.py | SIMPLIFICATION_CANDIDATE | UNIFY_LATER | candidate for command surface simplification |
| scripts/test-honest-pass-fixtures.py | FIXTURE_RUNNER | fixture runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-honest-pass-fixtures.py | KEEP_STANDALONE | KEEP | fixture semantics sensitive |
| scripts/test-human-approval-fixtures.py | FIXTURE_RUNNER | fixture runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-human-approval-fixtures.py | KEEP_STANDALONE | KEEP | fixture semantics sensitive |
| scripts/test-install.sh | INTERNAL_HELPER | internal helper script | unknown_needs_review | bash scripts/test-install.sh | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/test-integrity-regression.py | TEST_RUNNER | test runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-integrity-regression.py | SIMPLIFICATION_CANDIDATE | UNIFY_LATER | candidate for command surface simplification |
| scripts/test-m22-guardrails 3.py | TEST_RUNNER | test runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-m22-guardrails 3.py | SIMPLIFICATION_CANDIDATE | UNIFY_LATER | candidate for command surface simplification |
| scripts/test-m22-guardrails.py | TEST_RUNNER | test runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-m22-guardrails.py | SIMPLIFICATION_CANDIDATE | UNIFY_LATER | candidate for command surface simplification |
| scripts/test-m27-level1-fixtures 3.py | FIXTURE_RUNNER | fixture runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-m27-level1-fixtures 3.py | KEEP_STANDALONE | KEEP | fixture semantics sensitive |
| scripts/test-m27-level1-fixtures.py | FIXTURE_RUNNER | fixture runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-m27-level1-fixtures.py | KEEP_STANDALONE | KEEP | fixture semantics sensitive |
| scripts/test-m40-runtime-bypass-smoke.py | TEST_RUNNER | test runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-m40-runtime-bypass-smoke.py | SIMPLIFICATION_CANDIDATE | UNIFY_LATER | candidate for command surface simplification |
| scripts/test-negative-fixtures.py | FIXTURE_RUNNER | fixture runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-negative-fixtures.py | KEEP_STANDALONE | KEEP | fixture semantics sensitive |
| scripts/test-policy-enforcement-fixtures.py | FIXTURE_RUNNER | fixture runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-policy-enforcement-fixtures.py | KEEP_STANDALONE | KEEP | fixture semantics sensitive |
| scripts/test-policy-fixtures.py | FIXTURE_RUNNER | fixture runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-policy-fixtures.py | KEEP_STANDALONE | KEEP | fixture semantics sensitive |
| scripts/test-policy-flow-smoke.py | TEST_RUNNER | test runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-policy-flow-smoke.py | SIMPLIFICATION_CANDIDATE | UNIFY_LATER | candidate for command surface simplification |
| scripts/test-pre-merge-corridor-fixtures 3.py | FIXTURE_RUNNER | fixture runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-pre-merge-corridor-fixtures 3.py | KEEP_STANDALONE | KEEP | fixture semantics sensitive |
| scripts/test-pre-merge-corridor-fixtures.py | FIXTURE_RUNNER | fixture runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-pre-merge-corridor-fixtures.py | KEEP_STANDALONE | KEEP | fixture semantics sensitive |
| scripts/test-pre-merge-scope-fixtures 3.py | FIXTURE_RUNNER | fixture runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-pre-merge-scope-fixtures 3.py | KEEP_STANDALONE | KEEP | fixture semantics sensitive |
| scripts/test-pre-merge-scope-fixtures.py | FIXTURE_RUNNER | fixture runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-pre-merge-scope-fixtures.py | KEEP_STANDALONE | KEEP | fixture semantics sensitive |
| scripts/test-readiness-fixtures.py | FIXTURE_RUNNER | fixture runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-readiness-fixtures.py | KEEP_STANDALONE | KEEP | fixture semantics sensitive |
| scripts/test-scope-compliance-fixtures 3.py | FIXTURE_RUNNER | fixture runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-scope-compliance-fixtures 3.py | KEEP_STANDALONE | KEEP | fixture semantics sensitive |
| scripts/test-scope-compliance-fixtures.py | FIXTURE_RUNNER | fixture runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-scope-compliance-fixtures.py | KEEP_STANDALONE | KEEP | fixture semantics sensitive |
| scripts/test-single-role-execution-fixtures.py | FIXTURE_RUNNER | fixture runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-single-role-execution-fixtures.py | KEEP_STANDALONE | KEEP | fixture semantics sensitive |
| scripts/test-state-fixtures.py | FIXTURE_RUNNER | fixture runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-state-fixtures.py | KEEP_STANDALONE | KEEP | fixture semantics sensitive |
| scripts/test-template-integrity-fixtures.py | FIXTURE_RUNNER | fixture runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-template-integrity-fixtures.py | KEEP_STANDALONE | KEEP | fixture semantics sensitive |
| scripts/test-template-integrity.py | TEST_RUNNER | test runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-template-integrity.py | SIMPLIFICATION_CANDIDATE | UNIFY_LATER | candidate for command surface simplification |
| scripts/test-unified-gate-smoke.py | TEST_RUNNER | test runner | reports/m42-5-integrity-regression-evidence-consolidation.md;reports/m42-6-honest-pass-integrity-final-closure-report.md | python3 scripts/test-unified-gate-smoke.py | SIMPLIFICATION_CANDIDATE | UNIFY_LATER | candidate for command surface simplification |
| scripts/validate-active-task.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-active-task.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-approval-marker.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-approval-marker.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-architecture.sh | INTERNAL_HELPER | internal helper script | unknown_needs_review | bash scripts/validate-architecture.sh | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-boundary-claims 3.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-boundary-claims 3.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-boundary-claims.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-boundary-claims.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-commit-msg.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-commit-msg.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-contract-draft.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-contract-draft.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-docs.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-docs.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-frontmatter 3.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-frontmatter 3.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-frontmatter.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-frontmatter.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-gate-contract.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-gate-contract.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-handoff.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-handoff.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-human-approval.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-human-approval.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-incident.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-incident.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-index 3.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-index 3.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-index.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-index.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-lessons.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-lessons.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-lifecycle-apply.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-lifecycle-apply.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-policy.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-policy.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-queue-entry.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-queue-entry.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-queue.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-queue.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-required-sections 3.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-required-sections 3.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-required-sections.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-required-sections.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-review.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-review.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-route.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-route.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-runner-protocol.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-runner-protocol.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-status-semantics 3.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-status-semantics 3.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-status-semantics.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-status-semantics.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-task-brief.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-task-brief.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-task-state.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-task-state.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-task.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-task.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-trace.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-trace.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |
| scripts/validate-verification.py | INTERNAL_HELPER | internal helper script | unknown_needs_review | python3 scripts/validate-verification.py | SIMPLIFICATION_CANDIDATE | REVIEW_LATER | helper role assumed |

## Intentionally Excluded Scripts
Script Path | Reason | Reviewed By | Follow-Up Action
--- | --- | --- | ---
| none | none | M43.5 audit | none |
