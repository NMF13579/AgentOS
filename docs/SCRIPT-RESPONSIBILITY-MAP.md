# M71.2 — Script Responsibility Map

## Task Boundary

This M71 script responsibility map is evidence only.
This M71 script responsibility map is not approval.
This M71 script responsibility map does not authorize cleanup.
This M71 script responsibility map does not authorize script changes.
This M71 script responsibility map does not classify final lifecycle status.
This M71 script responsibility map does not create registry authority.
This M71 script responsibility map does not authorize validator creation, fixture creation, or lifecycle mutation.
reports/m71-script-inventory.md is the source-of-truth inventory artifact.
reports/m71-script-inventory.json is a derived navigation artifact only.
reports/m71-script-inventory.json must not become source of truth.
Human review remains required.

## Active Task Record

- id: task-71.2
- milestone: M71
- name: "Script Responsibility Map"
- status: active
- mode: "AUDIT / READ-ONLY CLASSIFICATION / NO SCRIPT CHANGES"
- branch: dev
- started_at: "2026-05-29"

## Inputs Reviewed

- PRIMARY_INPUT: reports/m71-script-inventory.md
- NAVIGATION_HELPER: reports/m71-script-inventory.json
- `scripts/` directory tree static text analysis
- Workflow files under `.github/workflows/`

## Authority Rule

reports/m71-script-inventory.md is the source-of-truth inventory artifact.
reports/m71-script-inventory.json is a derived navigation artifact only.
reports/m71-script-inventory.json must not become source of truth.
In case of any discrepancy or conflict, the Markdown inventory wins.

## Source Inventory Summary

The source inventory lists a total of 231 script entries + 1 automation-adjacent script (install.sh).
All entries have been classified by responsibility category.

## Responsibility Categories

The mapped scripts belong to the following responsibility categories:
- `acceptance_checking`: 1 scripts
- `agent_evidence_validation`: 1 scripts
- `completion_gate_boundary`: 1 scripts
- `context_indexing`: 7 scripts
- `documentation_helper`: 3 scripts
- `false_pass_resistance`: 1 scripts
- `install_template`: 3 scripts
- `legacy_runner_candidate`: 23 scripts
- `repo_inventory`: 1 scripts
- `task_validation`: 80 scripts
- `test_fixture_helper`: 42 scripts
- `unified_runner`: 26 scripts
- `unknown`: 24 scripts
- `workflow_validation`: 19 scripts

## Script Responsibility Table

| path | responsibility_category | observed_purpose | known_caller | input_contract_signal | output_contract_signal | writes_files_signal | uses_git_signal | uses_shell_or_subprocess_signal | risk_signal | needs_later_review | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `scripts/VALIDATORS.md` | unknown | UNKNOWN_PURPOSE | docs, reports | UNKNOWN_INPUT_CONTRACT | UNKNOWN_OUTPUT_CONTRACT | false | false | false | none | NEEDS_REVIEW | |
| `scripts/__pycache__/agent-complete.cpython-314.pyc` | test_fixture_helper | Python compiled bytecode cache | docs, reports, fixtures | UNKNOWN_INPUT_CONTRACT | UNKNOWN_OUTPUT_CONTRACT | false | false | false | none | NEEDS_REVIEW | |
| `scripts/__pycache__/agent-fail.cpython-314.pyc` | test_fixture_helper | Python compiled bytecode cache | docs, reports, fixtures | UNKNOWN_INPUT_CONTRACT | UNKNOWN_OUTPUT_CONTRACT | false | false | false | none | NEEDS_REVIEW | |
| `scripts/__pycache__/agent-next.cpython-314.pyc` | test_fixture_helper | Python compiled bytecode cache | docs, reports, fixtures | UNKNOWN_INPUT_CONTRACT | UNKNOWN_OUTPUT_CONTRACT | false | false | false | none | NEEDS_REVIEW | |
| `scripts/__pycache__/generate-task-contract.cpython-314.pyc` | test_fixture_helper | Python compiled bytecode cache | docs, reports, fixtures | UNKNOWN_INPUT_CONTRACT | UNKNOWN_OUTPUT_CONTRACT | false | false | false | none | NEEDS_REVIEW | |
| `scripts/__pycache__/validate-task.cpython-314.pyc` | test_fixture_helper | Python compiled bytecode cache | docs, reports, fixtures | UNKNOWN_INPUT_CONTRACT | UNKNOWN_OUTPUT_CONTRACT | false | false | false | none | NEEDS_REVIEW | |
| `scripts/__pycache__/validate-verification.cpython-314.pyc` | test_fixture_helper | Python compiled bytecode cache | docs, reports, fixtures | UNKNOWN_INPUT_CONTRACT | UNKNOWN_OUTPUT_CONTRACT | false | false | false | none | NEEDS_REVIEW | |
| `scripts/activate-task.py` | unknown | UNKNOWN_PURPOSE | docs, reports | argparse / sys.argv CLI options | UNKNOWN_OUTPUT_CONTRACT | true | false | true | none | M71.4 | |
| `scripts/agent-complete.py` | unified_runner | State transition hooks for agent run stages | docs, reports, tasks | argparse / sys.argv CLI options | exit status code | false | false | false | none | NEEDS_REVIEW | |
| `scripts/agent-fail.py` | unified_runner | State transition hooks for agent run stages | docs, reports, tasks | argparse / sys.argv CLI options | exit status code | false | false | false | none | NEEDS_REVIEW | |
| `scripts/agent-next.py` | unified_runner | State transition hooks for agent run stages | docs, reports | argparse / sys.argv CLI options | exit status code | false | false | false | none | NEEDS_REVIEW | |
| `scripts/agentos-audit-log.py` | unified_runner | AgentOS command guard, write guard, and TUI runtime entrypoints | workflow, docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | false | potential credential token variables | M71.4 | |
| `scripts/agentos-command-guard.py` | unified_runner | AgentOS command guard, write guard, and TUI runtime entrypoints | workflow, docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | true | true | none | M71.4, M71.5 | |
| `scripts/agentos-enforce.py` | unified_runner | AgentOS command guard, write guard, and TUI runtime entrypoints | workflow, docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | true | true | none | M71.4, M71.5 | |
| `scripts/agentos-explain.py` | unified_runner | AgentOS command guard, write guard, and TUI runtime entrypoints | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | true | none | M71.4 | |
| `scripts/agentos-git-guard.py` | unified_runner | AgentOS command guard, write guard, and TUI runtime entrypoints | workflow, docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | true | true | none | M71.4, M71.5 | |
| `scripts/agentos-human-gate.py` | unified_runner | AgentOS command guard, write guard, and TUI runtime entrypoints | workflow, docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | false | potential credential token variables | M71.4 | |
| `scripts/agentos-next-step.py` | unified_runner | AgentOS command guard, write guard, and TUI runtime entrypoints | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | true | none | M71.4 | |
| `scripts/agentos-permission-state.py` | unified_runner | AgentOS command guard, write guard, and TUI runtime entrypoints | workflow, docs, reports | argparse / sys.argv CLI options | UNKNOWN_OUTPUT_CONTRACT | false | false | false | none | NEEDS_REVIEW | |
| `scripts/agentos-retry-enforce.py` | unified_runner | AgentOS command guard, write guard, and TUI runtime entrypoints | workflow, docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | true | none | M71.4 | |
| `scripts/agentos-status.py` | unified_runner | AgentOS command guard, write guard, and TUI runtime entrypoints | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | false | none | M71.4 | |
| `scripts/agentos-tui.py` | unified_runner | AgentOS command guard, write guard, and TUI runtime entrypoints | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | true | none | M71.4 | |
| `scripts/agentos-validate.py` | unified_runner | AgentOS command guard, write guard, and TUI runtime entrypoints | workflow, docs, reports, tasks, fixtures | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | true | potential credential token variables | M71.4 | |
| `scripts/agentos-view-model.py` | unified_runner | AgentOS command guard, write guard, and TUI runtime entrypoints | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | true | none | M71.4 | |
| `scripts/agentos-violation-enforce.py` | unified_runner | AgentOS command guard, write guard, and TUI runtime entrypoints | workflow, docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | true | potential credential token variables | M71.4 | |
| `scripts/agentos-write-guard.py` | unified_runner | AgentOS command guard, write guard, and TUI runtime entrypoints | workflow, docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | true | destructive commands found | M71.4 | |
| `scripts/agentos.py` | unified_runner | AgentOS command guard, write guard, and TUI runtime entrypoints | docs, reports, tasks | argparse / sys.argv CLI options | exit status code | false | false | true | none | M71.4 | |
| `scripts/apply-transition.py` | unknown | UNKNOWN_PURPOSE | docs, reports, fixtures | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | true | none | M71.4 | |
| `scripts/audit-agentos.py` | workflow_validation | Audits workspace and validation authority boundaries | docs, reports | UNKNOWN_INPUT_CONTRACT | exit status code | true | false | true | none | M71.4 | |
| `scripts/audit-approval-boundary.py` | workflow_validation | Audits workspace and validation authority boundaries | docs, reports | reads input file | UNKNOWN_OUTPUT_CONTRACT | true | false | false | none | M71.4 | |
| `scripts/audit-context-layer.py` | workflow_validation | Audits workspace and validation authority boundaries | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | true | false | potential credential token variables | M71.4, M71.5 | |
| `scripts/audit-enforcement.py` | workflow_validation | Audits workspace and validation authority boundaries | docs, reports | argparse / sys.argv CLI options | exit status code | false | false | false | destructive commands found | NEEDS_REVIEW | |
| `scripts/audit-execution-control.py` | completion_gate_boundary | Audits execution control artifacts | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | true | none | M71.4 | |
| `scripts/audit-gate-contract.py` | workflow_validation | Audits workspace and validation authority boundaries | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | true | none | M71.4 | |
| `scripts/audit-lifecycle-mutation.py` | workflow_validation | Audits workspace and validation authority boundaries | docs, reports | reads input file | UNKNOWN_OUTPUT_CONTRACT | false | false | false | none | NEEDS_REVIEW | |
| `scripts/audit-m27-level1.py` | workflow_validation | Audits workspace and validation authority boundaries | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | true | true | potential credential token variables | M71.4, M71.5 | |
| `scripts/audit-m27.py` | workflow_validation | Audits workspace and validation authority boundaries | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | true | true | destructive commands found | M71.4, M71.5 | |
| `scripts/audit-m30-context-pipeline.py` | workflow_validation | Audits workspace and validation authority boundaries | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | false | none | NEEDS_REVIEW | |
| `scripts/audit-m31-tui-tutor.py` | workflow_validation | Audits workspace and validation authority boundaries | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | true | none | M71.4 | |
| `scripts/audit-metadata-consistency.py` | workflow_validation | Audits workspace and validation authority boundaries | docs, reports | argparse / sys.argv CLI options | exit status code | true | false | false | none | M71.4 | |
| `scripts/audit-mvp-readiness.py` | workflow_validation | Audits workspace and validation authority boundaries | docs, reports | argparse / sys.argv CLI options | exit status code | false | false | true | none | M71.4 | |
| `scripts/audit-policy-boundary.py` | workflow_validation | Audits workspace and validation authority boundaries | docs, reports, fixtures | reads input file | UNKNOWN_OUTPUT_CONTRACT | false | false | false | none | NEEDS_REVIEW | |
| `scripts/audit-pre-merge-corridor.py` | workflow_validation | Audits workspace and validation authority boundaries | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | true | true | none | M71.4, M71.5 | |
| `scripts/audit-release-readiness.py` | workflow_validation | Audits workspace and validation authority boundaries | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | true | none | M71.4 | |
| `scripts/audit-template-packaging.py` | workflow_validation | Audits workspace and validation authority boundaries | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | true | none | M71.4 | |
| `scripts/audit-validation-integration.py` | workflow_validation | Audits workspace and validation authority boundaries | docs, reports | argparse / sys.argv CLI options | exit status code | false | true | true | potential credential token variables | M71.4, M71.5 | |
| `scripts/build-context-cache.py` | unknown | UNKNOWN_PURPOSE | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | false | none | M71.4 | |
| `scripts/build-context-index.py` | unknown | UNKNOWN_PURPOSE | docs, reports, fixtures | argparse / sys.argv CLI options | JSON stdout / JSON file | true | true | true | none | M71.4, M71.5 | |
| `scripts/build-execution-verification-registry.py` | unknown | UNKNOWN_PURPOSE | docs, reports | reads input file | JSON stdout / JSON file | true | false | false | none | M71.4 | |
| `scripts/build-index.py` | context_indexing | Indexes directory context files | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | false | none | M71.4 | |
| `scripts/build-task-dependency-map.py` | unknown | UNKNOWN_PURPOSE | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | false | potential credential token variables | M71.4 | |
| `scripts/canonical-cleanup.sh` | unknown | UNKNOWN_PURPOSE | docs, reports | UNKNOWN_INPUT_CONTRACT | UNKNOWN_OUTPUT_CONTRACT | false | true | false | destructive commands found | M71.5 | |
| `scripts/check-acceptance-criteria.py` | acceptance_checking | Validates structured acceptance criteria packages | docs, reports, fixtures | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | false | none | NEEDS_REVIEW | |
| `scripts/check-active-task-readiness.py` | task_validation | Performs task-level static validation checks | docs | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | false | potential credential token variables | M71.4 | |
| `scripts/check-agent-task-evidence.py` | agent_evidence_validation | Validates output evidence packages against schema | docs, reports, fixtures | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | false | destructive commands found | M71.4 | |
| `scripts/check-apply-preconditions.py` | task_validation | Performs task-level static validation checks | docs, reports, fixtures | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | true | none | M71.4 | |
| `scripts/check-bypass-fixtures.py` | task_validation | Performs task-level static validation checks | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | false | potential credential token variables | M71.4 | |
| `scripts/check-bypass-resistance.py` | task_validation | Performs task-level static validation checks | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | true | destructive commands found | M71.4 | |
| `scripts/check-canary-integrity.py` | task_validation | Performs task-level static validation checks | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | false | none | NEEDS_REVIEW | |
| `scripts/check-commit-push-preconditions.py` | task_validation | Performs task-level static validation checks | docs, reports, fixtures | argparse / sys.argv CLI options | JSON stdout / JSON file | false | true | false | none | M71.5 | |
| `scripts/check-completion-readiness.py` | task_validation | Performs task-level static validation checks | docs, reports | argparse / sys.argv CLI options | UNKNOWN_OUTPUT_CONTRACT | false | false | false | destructive commands found | NEEDS_REVIEW | |
| `scripts/check-context-compliance.py` | context_indexing | Ensures integrity and freshness of context index files | docs, reports, fixtures | argparse / sys.argv CLI options | JSON stdout / JSON file | true | true | true | destructive commands found | M71.4, M71.5 | |
| `scripts/check-context-index-freshness.py` | context_indexing | Ensures integrity and freshness of context index files | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | true | true | potential credential token variables | M71.4, M71.5 | |
| `scripts/check-context-pipeline.py` | context_indexing | Ensures integrity and freshness of context index files | workflow, docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | true | true | none | M71.4, M71.5 | |
| `scripts/check-context-required.py` | context_indexing | Ensures integrity and freshness of context index files | docs, reports, fixtures | argparse / sys.argv CLI options | JSON stdout / JSON file | true | true | true | none | M71.4, M71.5 | |
| `scripts/check-controlled-execution-session.py` | unified_runner | Controlled execution validation checkers | docs, reports, fixtures | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | false | none | NEEDS_REVIEW | |
| `scripts/check-dangerous-commands.py` | task_validation | Performs task-level static validation checks | workflow, docs, reports | argparse / sys.argv CLI options | exit status code | false | false | false | none | NEEDS_REVIEW | |
| `scripts/check-evidence-amendments.py` | task_validation | Performs task-level static validation checks | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | false | none | NEEDS_REVIEW | |
| `scripts/check-evidence-binding.py` | task_validation | Performs task-level static validation checks | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | false | none | NEEDS_REVIEW | |
| `scripts/check-evidence-immutability.py` | task_validation | Performs task-level static validation checks | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | false | none | NEEDS_REVIEW | |
| `scripts/check-execution-authorization.py` | unified_runner | Controlled execution validation checkers | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | false | none | NEEDS_REVIEW | |
| `scripts/check-execution-readiness.py` | unified_runner | Controlled execution validation checkers | docs, reports, fixtures | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | false | none | NEEDS_REVIEW | |
| `scripts/check-execution-result-verification.py` | task_validation | Performs task-level static validation checks | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | true | false | destructive commands found | M71.4, M71.5 | |
| `scripts/check-execution-scope.py` | task_validation | Performs task-level static validation checks | docs, reports, fixtures | argparse / sys.argv CLI options | UNKNOWN_OUTPUT_CONTRACT | false | true | true | destructive commands found | M71.4, M71.5 | |
| `scripts/check-execution-verification-chain.py` | task_validation | Performs task-level static validation checks | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | false | none | M71.4 | |
| `scripts/check-execution-verification-registry.py` | task_validation | Performs task-level static validation checks | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | false | none | M71.4 | |
| `scripts/check-execution-verification-regression.py` | task_validation | Performs task-level static validation checks | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | true | true | none | M71.4, M71.5 | |
| `scripts/check-false-pass-resistance.py` | false_pass_resistance | Checks for false-pass scenarios in validation runs | docs, reports, fixtures | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | false | destructive commands found | M71.4 | |
| `scripts/check-github-platform-enforcement.py` | task_validation | Performs task-level static validation checks | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | false | destructive commands found | NEEDS_REVIEW | |
| `scripts/check-identity-drift.sh` | task_validation | Performs task-level static validation checks | workflow, docs, reports | UNKNOWN_INPUT_CONTRACT | UNKNOWN_OUTPUT_CONTRACT | false | false | false | none | NEEDS_REVIEW | |
| `scripts/check-interview-completeness.py` | task_validation | Performs task-level static validation checks | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | false | none | NEEDS_REVIEW | |
| `scripts/check-links.py` | task_validation | Performs task-level static validation checks | docs, reports | reads input file | exit status code | false | false | false | none | NEEDS_REVIEW | |
| `scripts/check-llms-graph-files.sh` | task_validation | Performs task-level static validation checks | workflow, docs, reports | UNKNOWN_INPUT_CONTRACT | UNKNOWN_OUTPUT_CONTRACT | false | false | false | none | NEEDS_REVIEW | |
| `scripts/check-m54-queue-placement-fixtures.py` | task_validation | Performs task-level static validation checks | docs | argparse / sys.argv CLI options | JSON stdout / JSON file | true | true | true | none | M71.4, M71.5 | |
| `scripts/check-m55-active-task-readiness-fixtures.py` | task_validation | Performs task-level static validation checks | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | true | true | none | M71.4, M71.5 | |
| `scripts/check-m56-execution-readiness-fixtures.py` | unified_runner | Controlled execution validation checkers | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | true | none | M71.4 | |
| `scripts/check-m57-execution-authorization-fixtures.py` | unified_runner | Controlled execution validation checkers | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | true | none | M71.4 | |
| `scripts/check-m58-controlled-execution-session-fixtures.py` | unified_runner | Controlled execution validation checkers | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | true | destructive commands found | M71.4 | |
| `scripts/check-m59-execution-result-verification-fixtures.py` | task_validation | Performs task-level static validation checks | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | true | none | M71.4 | |
| `scripts/check-m61-hardening-regression.py` | task_validation | Performs task-level static validation checks | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | true | none | M71.4 | |
| `scripts/check-pr-quality.py` | task_validation | Performs task-level static validation checks | workflow, docs, reports, tasks | reads input file | exit status code | false | false | false | none | NEEDS_REVIEW | |
| `scripts/check-pre-merge-scope.py` | task_validation | Performs task-level static validation checks | docs, reports, fixtures | argparse / sys.argv CLI options | JSON stdout / JSON file | true | true | true | none | M71.4, M71.5 | |
| `scripts/check-premature-artifacts.sh` | task_validation | Performs task-level static validation checks | docs, reports | UNKNOWN_INPUT_CONTRACT | UNKNOWN_OUTPUT_CONTRACT | false | false | false | none | NEEDS_REVIEW | |
| `scripts/check-private-evaluator-consistency.py` | task_validation | Performs task-level static validation checks | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | false | none | NEEDS_REVIEW | |
| `scripts/check-process-trace.py` | task_validation | Performs task-level static validation checks | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | false | none | NEEDS_REVIEW | |
| `scripts/check-product-spec-readiness.py` | task_validation | Performs task-level static validation checks | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | true | potential credential token variables | M71.4 | |
| `scripts/check-readiness-assertions.py` | task_validation | Performs task-level static validation checks | docs, reports | reads input file | exit status code | false | false | false | potential credential token variables | NEEDS_REVIEW | |
| `scripts/check-required-context-compliance.py` | context_indexing | Ensures integrity and freshness of context index files | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | true | true | none | M71.4, M71.5 | |
| `scripts/check-required-context-pack.py` | context_indexing | Ensures integrity and freshness of context index files | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | true | true | none | M71.4, M71.5 | |
| `scripts/check-risk.py` | task_validation | Performs task-level static validation checks | workflow, docs, reports | argparse / sys.argv CLI options | exit status code | false | false | false | none | NEEDS_REVIEW | |
| `scripts/check-role-separation.py` | task_validation | Performs task-level static validation checks | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | false | none | NEEDS_REVIEW | |
| `scripts/check-scope-compliance.py` | task_validation | Performs task-level static validation checks | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | true | true | none | M71.4, M71.5 | |
| `scripts/check-single-role-execution.py` | task_validation | Performs task-level static validation checks | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | false | potential credential token variables | M71.4 | |
| `scripts/check-task-acceptance-mvp.py` | task_validation | Performs task-level static validation checks | docs, reports, fixtures | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | false | destructive commands found | M71.4 | |
| `scripts/check-task-validation-contract.py` | task_validation | Performs task-level static validation checks | docs, reports, fixtures | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | false | none | M71.4 | |
| `scripts/check-template-cleanliness.py` | task_validation | Performs task-level static validation checks | docs, reports, tasks | argparse / sys.argv CLI options | exit status code | false | false | false | none | NEEDS_REVIEW | |
| `scripts/check-template-integrity.py` | task_validation | Performs task-level static validation checks | docs, reports, fixtures | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | false | destructive commands found | NEEDS_REVIEW | |
| `scripts/check-transition.py` | task_validation | Performs task-level static validation checks | docs, reports | argparse / sys.argv CLI options | UNKNOWN_OUTPUT_CONTRACT | true | false | true | none | M71.4 | |
| `scripts/check-use-template-readiness.py` | task_validation | Performs task-level static validation checks | docs, reports, tasks | reads input file | exit status code | false | true | true | none | M71.4, M71.5 | |
| `scripts/check-validator-authority-boundary.py` | task_validation | Performs task-level static validation checks | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | false | none | NEEDS_REVIEW | |
| `scripts/complete-active-task.py` | unknown | UNKNOWN_PURPOSE | docs, reports | argparse / sys.argv CLI options | UNKNOWN_OUTPUT_CONTRACT | true | false | true | none | M71.4 | |
| `scripts/detect-task-state.py` | unknown | UNKNOWN_PURPOSE | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | false | none | M71.4 | |
| `scripts/generate-repo-map.py` | task_validation | Generates and reviews task candidate placements | docs, reports | reads input file | exit status code | true | false | false | none | M71.4 | |
| `scripts/generate-task-contract-candidate.py` | task_validation | Generates and reviews task candidate placements | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | false | potential credential token variables | M71.4 | |
| `scripts/generate-task-contract.py` | task_validation | Generates and reviews task candidate placements | docs, reports, fixtures | argparse / sys.argv CLI options | exit status code | true | false | false | none | M71.4 | |
| `scripts/generate-tasks-from-spec.py` | task_validation | Generates and reviews task candidate placements | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | false | potential credential token variables | M71.4 | |
| `scripts/generate-tasks-from-ux.py` | task_validation | Generates and reviews task candidate placements | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | false | none | M71.4 | |
| `scripts/health-check.sh` | unknown | UNKNOWN_PURPOSE | workflow, docs, reports | UNKNOWN_INPUT_CONTRACT | UNKNOWN_OUTPUT_CONTRACT | false | false | false | none | NEEDS_REVIEW | |
| `scripts/install-agentos.py` | install_template | Installs Git hooks or packages agentos helpers | docs, reports, tasks | argparse / sys.argv CLI options | JSON stdout / JSON file | true | true | false | potential credential token variables | M71.4, M71.5 | |
| `scripts/install-hooks.sh` | install_template | Installs Git hooks or packages agentos helpers | docs, reports | UNKNOWN_INPUT_CONTRACT | UNKNOWN_OUTPUT_CONTRACT | false | false | false | none | NEEDS_REVIEW | |
| `scripts/lib/__init__.py` | unknown | UNKNOWN_PURPOSE | docs, reports | UNKNOWN_INPUT_CONTRACT | UNKNOWN_OUTPUT_CONTRACT | false | false | false | none | NEEDS_REVIEW | |
| `scripts/lib/path_utils.py` | unknown | UNKNOWN_PURPOSE | docs, reports | UNKNOWN_INPUT_CONTRACT | UNKNOWN_OUTPUT_CONTRACT | false | false | false | none | NEEDS_REVIEW | |
| `scripts/lint-task-contract.py` | unknown | UNKNOWN_PURPOSE | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | false | potential credential token variables | NEEDS_REVIEW | |
| `scripts/materialize-task-candidate-placement.py` | task_validation | Generates and reviews task candidate placements | docs | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | false | potential credential token variables | M71.4 | |
| `scripts/prepare-clean-template.py` | unknown | UNKNOWN_PURPOSE | docs, reports, tasks | argparse / sys.argv CLI options | exit status code | true | false | false | none | M71.4 | |
| `scripts/renderers/__init__.py` | unknown | UNKNOWN_PURPOSE | docs, reports | UNKNOWN_INPUT_CONTRACT | UNKNOWN_OUTPUT_CONTRACT | false | false | false | none | NEEDS_REVIEW | |
| `scripts/renderers/plain_status_renderer.py` | unknown | UNKNOWN_PURPOSE | docs, reports | argparse / sys.argv CLI options | UNKNOWN_OUTPUT_CONTRACT | false | false | false | none | NEEDS_REVIEW | |
| `scripts/renderers/rich_status_renderer.py` | unknown | UNKNOWN_PURPOSE | docs, reports | argparse / sys.argv CLI options | UNKNOWN_OUTPUT_CONTRACT | false | false | false | none | NEEDS_REVIEW | |
| `scripts/repo-scan.py` | repo_inventory | Scans repository and compiles inventory lists | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | true | true | none | M71.4, M71.5 | |
| `scripts/review-task-candidate-placement.py` | task_validation | Generates and reviews task candidate placements | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | false | potential credential token variables | M71.4 | |
| `scripts/run-active-task.py` | unknown | UNKNOWN_PURPOSE | docs, reports, fixtures | argparse / sys.argv CLI options | UNKNOWN_OUTPUT_CONTRACT | true | false | true | none | M71.4 | |
| `scripts/run-all.sh` | unified_runner | Runner script to execute validation suite | workflow, docs, reports, tasks, fixtures | UNKNOWN_INPUT_CONTRACT | UNKNOWN_OUTPUT_CONTRACT | false | false | false | none | M71.6 | |
| `scripts/run-execution-verification.py` | unknown | UNKNOWN_PURPOSE | docs, reports, fixtures | argparse / sys.argv CLI options | UNKNOWN_OUTPUT_CONTRACT | true | true | true | potential credential token variables | M71.4, M71.5 | |
| `scripts/run-task-validation.py` | unknown | UNKNOWN_PURPOSE | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | true | none | M71.4 | |
| `scripts/select-context.py` | unknown | UNKNOWN_PURPOSE | docs, reports, fixtures | argparse / sys.argv CLI options | JSON stdout / JSON file | true | true | true | none | M71.4, M71.5 | |
| `scripts/smoke-interview-layer.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | true | none | M71.4 | |
| `scripts/smoke-m44-decomposition.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | true | potential credential token variables | M71.4 | |
| `scripts/sync-context.sh` | unknown | UNKNOWN_PURPOSE | docs, reports | argparse / sys.argv CLI options | UNKNOWN_OUTPUT_CONTRACT | false | true | false | none | M71.5 | |
| `scripts/sync-task-ids.py` | workflow_validation | Syncs task IDs across artifacts | workflow, docs, reports, tasks | reads input file | exit status code | true | false | false | none | M71.4 | |
| `scripts/task-health.py` | unknown | UNKNOWN_PURPOSE | docs, reports | argparse / sys.argv CLI options | exit status code | true | false | false | none | M71.4 | |
| `scripts/test-activation-fixtures.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | reads input file | UNKNOWN_OUTPUT_CONTRACT | true | false | true | none | M71.4 | |
| `scripts/test-active-task-fixtures.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | reads input file | UNKNOWN_OUTPUT_CONTRACT | false | false | true | none | M71.4 | |
| `scripts/test-apply-transition-fixtures.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | argparse / sys.argv CLI options | UNKNOWN_OUTPUT_CONTRACT | true | false | true | none | M71.4 | |
| `scripts/test-approval-fixtures.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | reads input file | UNKNOWN_OUTPUT_CONTRACT | true | false | true | potential credential token variables | M71.4 | |
| `scripts/test-approval-flow-smoke.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | reads input file | UNKNOWN_OUTPUT_CONTRACT | true | false | true | potential credential token variables | M71.4 | |
| `scripts/test-approval-marker-fixtures.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | argparse / sys.argv CLI options | exit status code | true | false | true | none | M71.4 | |
| `scripts/test-ci-advisory-config.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | argparse / sys.argv CLI options | exit status code | false | false | false | potential credential token variables | NEEDS_REVIEW | |
| `scripts/test-commit-push-preconditions-fixtures.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | argparse / sys.argv CLI options | exit status code | false | false | true | none | M71.4 | |
| `scripts/test-completion-flow-smoke.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | argparse / sys.argv CLI options | UNKNOWN_OUTPUT_CONTRACT | true | false | true | potential credential token variables | M71.4 | |
| `scripts/test-enforcement-fixtures.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | UNKNOWN_INPUT_CONTRACT | UNKNOWN_OUTPUT_CONTRACT | false | false | true | none | M71.4 | |
| `scripts/test-example-project.sh` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | UNKNOWN_INPUT_CONTRACT | UNKNOWN_OUTPUT_CONTRACT | false | true | false | destructive commands found | M71.5 | |
| `scripts/test-execution-runner-fixtures.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | argparse / sys.argv CLI options | UNKNOWN_OUTPUT_CONTRACT | true | false | true | none | M71.4 | |
| `scripts/test-gate-regression-fixtures.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | UNKNOWN_INPUT_CONTRACT | exit status code | false | false | true | none | M71.4 | |
| `scripts/test-guard-failures.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | reads input file | exit status code | false | false | true | none | M71.4 | |
| `scripts/test-honest-pass-fixtures.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | true | potential credential token variables | M71.4 | |
| `scripts/test-human-approval-fixtures.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | UNKNOWN_INPUT_CONTRACT | UNKNOWN_OUTPUT_CONTRACT | false | false | true | none | M71.4 | |
| `scripts/test-install.sh` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | UNKNOWN_INPUT_CONTRACT | UNKNOWN_OUTPUT_CONTRACT | true | true | false | destructive commands found | M71.4, M71.5 | |
| `scripts/test-integrity-regression.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | true | potential credential token variables | M71.4 | |
| `scripts/test-m22-guardrails.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | UNKNOWN_INPUT_CONTRACT | exit status code | false | false | true | none | M71.4 | |
| `scripts/test-m27-level1-fixtures.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | argparse / sys.argv CLI options | JSON stdout / JSON file | false | true | true | destructive commands found | M71.4, M71.5 | |
| `scripts/test-m40-runtime-bypass-smoke.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | argparse / sys.argv CLI options | JSON stdout / JSON file | true | true | true | potential credential token variables | M71.4, M71.5 | |
| `scripts/test-negative-fixtures.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | reads input file | exit status code | true | true | true | none | M71.4, M71.5 | |
| `scripts/test-policy-enforcement-fixtures.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | UNKNOWN_INPUT_CONTRACT | UNKNOWN_OUTPUT_CONTRACT | false | false | true | none | M71.4 | |
| `scripts/test-policy-fixtures.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | UNKNOWN_INPUT_CONTRACT | UNKNOWN_OUTPUT_CONTRACT | false | false | true | none | M71.4 | |
| `scripts/test-policy-flow-smoke.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | UNKNOWN_INPUT_CONTRACT | UNKNOWN_OUTPUT_CONTRACT | false | false | true | none | M71.4 | |
| `scripts/test-pre-merge-corridor-fixtures.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | argparse / sys.argv CLI options | exit status code | false | false | true | none | M71.4 | |
| `scripts/test-pre-merge-scope-fixtures.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | argparse / sys.argv CLI options | exit status code | false | false | true | none | M71.4 | |
| `scripts/test-readiness-fixtures.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | reads input file | UNKNOWN_OUTPUT_CONTRACT | false | false | true | none | M71.4 | |
| `scripts/test-scope-compliance-fixtures.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | argparse / sys.argv CLI options | exit status code | true | true | true | none | M71.4, M71.5 | |
| `scripts/test-single-role-execution-fixtures.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | UNKNOWN_INPUT_CONTRACT | exit status code | false | false | true | potential credential token variables | M71.4 | |
| `scripts/test-state-fixtures.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | argparse / sys.argv CLI options | UNKNOWN_OUTPUT_CONTRACT | true | false | true | none | M71.4 | |
| `scripts/test-template-integrity-fixtures.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | UNKNOWN_INPUT_CONTRACT | exit status code | false | false | true | none | M71.4 | |
| `scripts/test-template-integrity.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | UNKNOWN_INPUT_CONTRACT | exit status code | false | false | true | none | M71.4 | |
| `scripts/test-unified-gate-smoke.py` | test_fixture_helper | Validation test fixture / smoke test execution helper | docs, reports, fixtures | UNKNOWN_INPUT_CONTRACT | exit status code | false | false | true | none | M71.4 | |
| `scripts/validate-active-task.py` | task_validation | Validates task structure and state schemas | docs, reports, fixtures | argparse / sys.argv CLI options | UNKNOWN_OUTPUT_CONTRACT | false | false | false | none | NEEDS_REVIEW | |
| `scripts/validate-approval-marker.py` | task_validation | Validates task structure and state schemas | docs, reports, fixtures | argparse / sys.argv CLI options | exit status code | false | false | false | none | NEEDS_REVIEW | |
| `scripts/validate-architecture.sh` | task_validation | Validates task structure and state schemas | workflow, docs, reports | UNKNOWN_INPUT_CONTRACT | UNKNOWN_OUTPUT_CONTRACT | false | false | false | none | NEEDS_REVIEW | |
| `scripts/validate-boundary-claims.py` | task_validation | Validates task structure and state schemas | docs, reports | argparse / sys.argv CLI options | exit status code | true | false | false | none | M71.4 | |
| `scripts/validate-commit-msg.py` | workflow_validation | Commit message format compliance validator | docs, reports | argparse / sys.argv CLI options | exit status code | true | false | false | none | M71.4 | |
| `scripts/validate-contract-draft.py` | task_validation | Validates task structure and state schemas | docs, reports | argparse / sys.argv CLI options | exit status code | true | false | false | none | M71.4 | |
| `scripts/validate-docs.py` | documentation_helper | Validates markdown structure and documentation frontmatter | docs, reports | reads input file | exit status code | false | false | false | none | NEEDS_REVIEW | |
| `scripts/validate-frontmatter.py` | documentation_helper | Validates markdown structure and documentation frontmatter | docs, reports | argparse / sys.argv CLI options | exit status code | false | false | false | none | NEEDS_REVIEW | |
| `scripts/validate-gate-contract.py` | task_validation | Validates task structure and state schemas | docs, reports | UNKNOWN_INPUT_CONTRACT | exit status code | false | false | false | none | NEEDS_REVIEW | |
| `scripts/validate-handoff.py` | task_validation | Validates task structure and state schemas | docs, reports | argparse / sys.argv CLI options | exit status code | false | false | false | none | NEEDS_REVIEW | |
| `scripts/validate-human-approval.py` | task_validation | Validates task structure and state schemas | docs, reports, fixtures | argparse / sys.argv CLI options | UNKNOWN_OUTPUT_CONTRACT | false | false | false | destructive commands found | NEEDS_REVIEW | |
| `scripts/validate-incident.py` | task_validation | Validates task structure and state schemas | docs, reports | argparse / sys.argv CLI options | exit status code | false | false | false | none | NEEDS_REVIEW | |
| `scripts/validate-index.py` | task_validation | Validates task structure and state schemas | docs, reports | argparse / sys.argv CLI options | exit status code | false | false | false | none | NEEDS_REVIEW | |
| `scripts/validate-lessons.py` | documentation_helper | Validates markdown structure and documentation frontmatter | docs, reports | argparse / sys.argv CLI options | exit status code | false | false | false | none | NEEDS_REVIEW | |
| `scripts/validate-lifecycle-apply.py` | task_validation | Validates task structure and state schemas | docs, reports | reads input file | UNKNOWN_OUTPUT_CONTRACT | false | false | false | none | NEEDS_REVIEW | |
| `scripts/validate-policy.py` | task_validation | Validates task structure and state schemas | docs, reports, fixtures | argparse / sys.argv CLI options | UNKNOWN_OUTPUT_CONTRACT | false | false | false | none | NEEDS_REVIEW | |
| `scripts/validate-product-spec.py` | task_validation | Validates task structure and state schemas | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | false | potential credential token variables | M71.4 | |
| `scripts/validate-proposal-to-task-conversion.py` | task_validation | Validates task structure and state schemas | docs, reports, fixtures | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | false | none | M71.4 | |
| `scripts/validate-queue-entry.py` | task_validation | Validates task structure and state schemas | docs, reports | argparse / sys.argv CLI options | exit status code | false | false | false | none | NEEDS_REVIEW | |
| `scripts/validate-queue.py` | task_validation | Validates task structure and state schemas | docs, reports | argparse / sys.argv CLI options | exit status code | false | true | true | none | M71.4, M71.5 | |
| `scripts/validate-required-sections.py` | task_validation | Validates task structure and state schemas | docs, reports | argparse / sys.argv CLI options | exit status code | false | false | false | none | NEEDS_REVIEW | |
| `scripts/validate-review.py` | task_validation | Validates task structure and state schemas | docs, reports | argparse / sys.argv CLI options | exit status code | false | false | false | none | NEEDS_REVIEW | |
| `scripts/validate-route.py` | task_validation | Validates task structure and state schemas | docs, reports | reads input file | exit status code | false | false | false | destructive commands found | NEEDS_REVIEW | |
| `scripts/validate-runner-protocol.py` | task_validation | Validates task structure and state schemas | docs, reports | argparse / sys.argv CLI options | exit status code | true | false | false | none | M71.4 | |
| `scripts/validate-status-semantics.py` | task_validation | Validates task structure and state schemas | docs, reports | argparse / sys.argv CLI options | exit status code | false | false | false | none | NEEDS_REVIEW | |
| `scripts/validate-task-brief.py` | task_validation | Validates task structure and state schemas | docs, reports, tasks, fixtures | argparse / sys.argv CLI options | exit status code | false | false | false | none | NEEDS_REVIEW | |
| `scripts/validate-task-contract-candidate.py` | task_validation | Validates task structure and state schemas | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | true | false | false | potential credential token variables | M71.4 | |
| `scripts/validate-task-state.py` | task_validation | Validates task structure and state schemas | docs, reports | argparse / sys.argv CLI options | UNKNOWN_OUTPUT_CONTRACT | false | false | true | none | M71.4 | |
| `scripts/validate-task.py` | task_validation | Validates task structure and state schemas | workflow, docs, reports, tasks | argparse / sys.argv CLI options | exit status code | false | false | false | none | NEEDS_REVIEW | |
| `scripts/validate-trace.py` | task_validation | Validates task structure and state schemas | docs, reports | argparse / sys.argv CLI options | exit status code | true | false | false | none | M71.4 | |
| `scripts/validate-ux-contract.py` | task_validation | Validates task structure and state schemas | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | false | destructive commands found | NEEDS_REVIEW | |
| `scripts/validate-ux-planning-readiness.py` | task_validation | Validates task structure and state schemas | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | false | destructive commands found | NEEDS_REVIEW | |
| `scripts/validate-ux-to-task-proposal.py` | task_validation | Validates task structure and state schemas | docs, reports | argparse / sys.argv CLI options | JSON stdout / JSON file | false | false | false | potential credential token variables | NEEDS_REVIEW | |
| `scripts/validate-verification.py` | task_validation | Validates task structure and state schemas | workflow, docs, reports | argparse / sys.argv CLI options | exit status code | false | false | false | none | NEEDS_REVIEW | |
| `install.sh` | install_template | Root setup script for repository template | docs, reports | UNKNOWN_INPUT_CONTRACT | UNKNOWN_OUTPUT_CONTRACT | true | false | false | none | M71.6, M71.4 | |

## Known Callers

Caller clues derived from workflows, docs, reports, and tasks search:
- Workflows: 29 script invocation lines detected.
- Docs: 743 script path references.
- Reports: 8,998 script path references.
- Tasks: 57 script path references.

## Workflow-Referenced Scripts

Total scripts referenced by workflows: 22
- `scripts/agentos-audit-log.py`
- `scripts/agentos-command-guard.py`
- `scripts/agentos-enforce.py`
- `scripts/agentos-git-guard.py`
- `scripts/agentos-human-gate.py`
- `scripts/agentos-permission-state.py`
- `scripts/agentos-retry-enforce.py`
- `scripts/agentos-validate.py`
- `scripts/agentos-violation-enforce.py`
- `scripts/agentos-write-guard.py`
- `scripts/check-context-pipeline.py`
- `scripts/check-dangerous-commands.py`
- `scripts/check-identity-drift.sh`
- `scripts/check-llms-graph-files.sh`
- `scripts/check-pr-quality.py`
- `scripts/check-risk.py`
- `scripts/health-check.sh`
- `scripts/run-all.sh`
- `scripts/sync-task-ids.py`
- `scripts/validate-architecture.sh`
- `scripts/validate-task.py`
- `scripts/validate-verification.py`

## Docs-Referenced Scripts

Total scripts referenced by documentation: 232
- `install.sh`
- `scripts/VALIDATORS.md`
- `scripts/__pycache__/agent-complete.cpython-314.pyc`
- `scripts/__pycache__/agent-fail.cpython-314.pyc`
- `scripts/__pycache__/agent-next.cpython-314.pyc`
- `scripts/__pycache__/generate-task-contract.cpython-314.pyc`
- `scripts/__pycache__/validate-task.cpython-314.pyc`
- `scripts/__pycache__/validate-verification.cpython-314.pyc`
- `scripts/activate-task.py`
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
- `scripts/apply-transition.py`
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
- `scripts/build-context-cache.py`
- `scripts/build-context-index.py`
- `scripts/build-execution-verification-registry.py`
- `scripts/build-index.py`
- `scripts/build-task-dependency-map.py`
- `scripts/canonical-cleanup.sh`
- `scripts/check-acceptance-criteria.py`
- `scripts/check-active-task-readiness.py`
- `scripts/check-agent-task-evidence.py`
- `scripts/check-apply-preconditions.py`
- `scripts/check-bypass-fixtures.py`
- `scripts/check-bypass-resistance.py`
- `scripts/check-canary-integrity.py`
- `scripts/check-commit-push-preconditions.py`
- `scripts/check-completion-readiness.py`
- `scripts/check-context-compliance.py`
- `scripts/check-context-index-freshness.py`
- `scripts/check-context-pipeline.py`
- `scripts/check-context-required.py`
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
- `scripts/check-required-context-compliance.py`
- `scripts/check-required-context-pack.py`
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
- `scripts/complete-active-task.py`
- `scripts/detect-task-state.py`
- `scripts/generate-repo-map.py`
- `scripts/generate-task-contract-candidate.py`
- `scripts/generate-task-contract.py`
- `scripts/generate-tasks-from-spec.py`
- `scripts/generate-tasks-from-ux.py`
- `scripts/health-check.sh`
- `scripts/install-agentos.py`
- `scripts/install-hooks.sh`
- `scripts/lib/__init__.py`
- `scripts/lib/path_utils.py`
- `scripts/lint-task-contract.py`
- `scripts/materialize-task-candidate-placement.py`
- `scripts/prepare-clean-template.py`
- `scripts/renderers/__init__.py`
- `scripts/renderers/plain_status_renderer.py`
- `scripts/renderers/rich_status_renderer.py`
- `scripts/repo-scan.py`
- `scripts/review-task-candidate-placement.py`
- `scripts/run-active-task.py`
- `scripts/run-all.sh`
- `scripts/run-execution-verification.py`
- `scripts/run-task-validation.py`
- `scripts/select-context.py`
- `scripts/smoke-interview-layer.py`
- `scripts/smoke-m44-decomposition.py`
- `scripts/sync-context.sh`
- `scripts/sync-task-ids.py`
- `scripts/task-health.py`
- `scripts/test-activation-fixtures.py`
- `scripts/test-active-task-fixtures.py`
- `scripts/test-apply-transition-fixtures.py`
- `scripts/test-approval-fixtures.py`
- `scripts/test-approval-flow-smoke.py`
- `scripts/test-approval-marker-fixtures.py`
- `scripts/test-ci-advisory-config.py`
- `scripts/test-commit-push-preconditions-fixtures.py`
- `scripts/test-completion-flow-smoke.py`
- `scripts/test-enforcement-fixtures.py`
- `scripts/test-example-project.sh`
- `scripts/test-execution-runner-fixtures.py`
- `scripts/test-gate-regression-fixtures.py`
- `scripts/test-guard-failures.py`
- `scripts/test-honest-pass-fixtures.py`
- `scripts/test-human-approval-fixtures.py`
- `scripts/test-install.sh`
- `scripts/test-integrity-regression.py`
- `scripts/test-m22-guardrails.py`
- `scripts/test-m27-level1-fixtures.py`
- `scripts/test-m40-runtime-bypass-smoke.py`
- `scripts/test-negative-fixtures.py`
- `scripts/test-policy-enforcement-fixtures.py`
- `scripts/test-policy-fixtures.py`
- `scripts/test-policy-flow-smoke.py`
- `scripts/test-pre-merge-corridor-fixtures.py`
- `scripts/test-pre-merge-scope-fixtures.py`
- `scripts/test-readiness-fixtures.py`
- `scripts/test-scope-compliance-fixtures.py`
- `scripts/test-single-role-execution-fixtures.py`
- `scripts/test-state-fixtures.py`
- `scripts/test-template-integrity-fixtures.py`
- `scripts/test-template-integrity.py`
- `scripts/test-unified-gate-smoke.py`
- `scripts/validate-active-task.py`
- `scripts/validate-approval-marker.py`
- `scripts/validate-architecture.sh`
- `scripts/validate-boundary-claims.py`
- `scripts/validate-commit-msg.py`
- `scripts/validate-contract-draft.py`
- `scripts/validate-docs.py`
- `scripts/validate-frontmatter.py`
- `scripts/validate-gate-contract.py`
- `scripts/validate-handoff.py`
- `scripts/validate-human-approval.py`
- `scripts/validate-incident.py`
- `scripts/validate-index.py`
- `scripts/validate-lessons.py`
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

## Reports-Referenced Scripts

Total scripts referenced by reports: 229
- `install.sh`
- `scripts/VALIDATORS.md`
- `scripts/__pycache__/agent-complete.cpython-314.pyc`
- `scripts/__pycache__/agent-fail.cpython-314.pyc`
- `scripts/__pycache__/agent-next.cpython-314.pyc`
- `scripts/__pycache__/generate-task-contract.cpython-314.pyc`
- `scripts/__pycache__/validate-task.cpython-314.pyc`
- `scripts/__pycache__/validate-verification.cpython-314.pyc`
- `scripts/activate-task.py`
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
- `scripts/apply-transition.py`
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
- `scripts/build-context-cache.py`
- `scripts/build-context-index.py`
- `scripts/build-execution-verification-registry.py`
- `scripts/build-index.py`
- `scripts/build-task-dependency-map.py`
- `scripts/canonical-cleanup.sh`
- `scripts/check-acceptance-criteria.py`
- `scripts/check-agent-task-evidence.py`
- `scripts/check-apply-preconditions.py`
- `scripts/check-bypass-fixtures.py`
- `scripts/check-bypass-resistance.py`
- `scripts/check-canary-integrity.py`
- `scripts/check-commit-push-preconditions.py`
- `scripts/check-completion-readiness.py`
- `scripts/check-context-compliance.py`
- `scripts/check-context-index-freshness.py`
- `scripts/check-context-pipeline.py`
- `scripts/check-context-required.py`
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
- `scripts/check-required-context-compliance.py`
- `scripts/check-required-context-pack.py`
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
- `scripts/complete-active-task.py`
- `scripts/detect-task-state.py`
- `scripts/generate-repo-map.py`
- `scripts/generate-task-contract-candidate.py`
- `scripts/generate-task-contract.py`
- `scripts/generate-tasks-from-spec.py`
- `scripts/generate-tasks-from-ux.py`
- `scripts/health-check.sh`
- `scripts/install-agentos.py`
- `scripts/install-hooks.sh`
- `scripts/lib/__init__.py`
- `scripts/lib/path_utils.py`
- `scripts/lint-task-contract.py`
- `scripts/prepare-clean-template.py`
- `scripts/renderers/__init__.py`
- `scripts/renderers/plain_status_renderer.py`
- `scripts/renderers/rich_status_renderer.py`
- `scripts/repo-scan.py`
- `scripts/review-task-candidate-placement.py`
- `scripts/run-active-task.py`
- `scripts/run-all.sh`
- `scripts/run-execution-verification.py`
- `scripts/run-task-validation.py`
- `scripts/select-context.py`
- `scripts/smoke-interview-layer.py`
- `scripts/smoke-m44-decomposition.py`
- `scripts/sync-context.sh`
- `scripts/sync-task-ids.py`
- `scripts/task-health.py`
- `scripts/test-activation-fixtures.py`
- `scripts/test-active-task-fixtures.py`
- `scripts/test-apply-transition-fixtures.py`
- `scripts/test-approval-fixtures.py`
- `scripts/test-approval-flow-smoke.py`
- `scripts/test-approval-marker-fixtures.py`
- `scripts/test-ci-advisory-config.py`
- `scripts/test-commit-push-preconditions-fixtures.py`
- `scripts/test-completion-flow-smoke.py`
- `scripts/test-enforcement-fixtures.py`
- `scripts/test-example-project.sh`
- `scripts/test-execution-runner-fixtures.py`
- `scripts/test-gate-regression-fixtures.py`
- `scripts/test-guard-failures.py`
- `scripts/test-honest-pass-fixtures.py`
- `scripts/test-human-approval-fixtures.py`
- `scripts/test-install.sh`
- `scripts/test-integrity-regression.py`
- `scripts/test-m22-guardrails.py`
- `scripts/test-m27-level1-fixtures.py`
- `scripts/test-m40-runtime-bypass-smoke.py`
- `scripts/test-negative-fixtures.py`
- `scripts/test-policy-enforcement-fixtures.py`
- `scripts/test-policy-fixtures.py`
- `scripts/test-policy-flow-smoke.py`
- `scripts/test-pre-merge-corridor-fixtures.py`
- `scripts/test-pre-merge-scope-fixtures.py`
- `scripts/test-readiness-fixtures.py`
- `scripts/test-scope-compliance-fixtures.py`
- `scripts/test-single-role-execution-fixtures.py`
- `scripts/test-state-fixtures.py`
- `scripts/test-template-integrity-fixtures.py`
- `scripts/test-template-integrity.py`
- `scripts/test-unified-gate-smoke.py`
- `scripts/validate-active-task.py`
- `scripts/validate-approval-marker.py`
- `scripts/validate-architecture.sh`
- `scripts/validate-boundary-claims.py`
- `scripts/validate-commit-msg.py`
- `scripts/validate-contract-draft.py`
- `scripts/validate-docs.py`
- `scripts/validate-frontmatter.py`
- `scripts/validate-gate-contract.py`
- `scripts/validate-handoff.py`
- `scripts/validate-human-approval.py`
- `scripts/validate-incident.py`
- `scripts/validate-index.py`
- `scripts/validate-lessons.py`
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

## Tasks-Referenced Scripts

Total scripts referenced by tasks: 13
- `scripts/agent-complete.py`
- `scripts/agent-fail.py`
- `scripts/agentos-validate.py`
- `scripts/agentos.py`
- `scripts/check-pr-quality.py`
- `scripts/check-template-cleanliness.py`
- `scripts/check-use-template-readiness.py`
- `scripts/install-agentos.py`
- `scripts/prepare-clean-template.py`
- `scripts/run-all.sh`
- `scripts/sync-task-ids.py`
- `scripts/validate-task-brief.py`
- `scripts/validate-task.py`

## Fixture-Related Scripts

Total scripts related to fixtures: 71
- `scripts/__pycache__/agent-complete.cpython-314.pyc`
- `scripts/__pycache__/agent-fail.cpython-314.pyc`
- `scripts/__pycache__/agent-next.cpython-314.pyc`
- `scripts/__pycache__/generate-task-contract.cpython-314.pyc`
- `scripts/__pycache__/validate-task.cpython-314.pyc`
- `scripts/__pycache__/validate-verification.cpython-314.pyc`
- `scripts/agentos-validate.py`
- `scripts/apply-transition.py`
- `scripts/audit-policy-boundary.py`
- `scripts/build-context-index.py`
- `scripts/check-acceptance-criteria.py`
- `scripts/check-agent-task-evidence.py`
- `scripts/check-apply-preconditions.py`
- `scripts/check-commit-push-preconditions.py`
- `scripts/check-context-compliance.py`
- `scripts/check-context-required.py`
- `scripts/check-controlled-execution-session.py`
- `scripts/check-execution-readiness.py`
- `scripts/check-execution-scope.py`
- `scripts/check-false-pass-resistance.py`
- `scripts/check-pre-merge-scope.py`
- `scripts/check-task-acceptance-mvp.py`
- `scripts/check-task-validation-contract.py`
- `scripts/check-template-integrity.py`
- `scripts/generate-task-contract.py`
- `scripts/run-active-task.py`
- `scripts/run-all.sh`
- `scripts/run-execution-verification.py`
- `scripts/select-context.py`
- `scripts/smoke-interview-layer.py`
- `scripts/smoke-m44-decomposition.py`
- `scripts/test-activation-fixtures.py`
- `scripts/test-active-task-fixtures.py`
- `scripts/test-apply-transition-fixtures.py`
- `scripts/test-approval-fixtures.py`
- `scripts/test-approval-flow-smoke.py`
- `scripts/test-approval-marker-fixtures.py`
- `scripts/test-ci-advisory-config.py`
- `scripts/test-commit-push-preconditions-fixtures.py`
- `scripts/test-completion-flow-smoke.py`
- `scripts/test-enforcement-fixtures.py`
- `scripts/test-example-project.sh`
- `scripts/test-execution-runner-fixtures.py`
- `scripts/test-gate-regression-fixtures.py`
- `scripts/test-guard-failures.py`
- `scripts/test-honest-pass-fixtures.py`
- `scripts/test-human-approval-fixtures.py`
- `scripts/test-install.sh`
- `scripts/test-integrity-regression.py`
- `scripts/test-m22-guardrails.py`
- `scripts/test-m27-level1-fixtures.py`
- `scripts/test-m40-runtime-bypass-smoke.py`
- `scripts/test-negative-fixtures.py`
- `scripts/test-policy-enforcement-fixtures.py`
- `scripts/test-policy-fixtures.py`
- `scripts/test-policy-flow-smoke.py`
- `scripts/test-pre-merge-corridor-fixtures.py`
- `scripts/test-pre-merge-scope-fixtures.py`
- `scripts/test-readiness-fixtures.py`
- `scripts/test-scope-compliance-fixtures.py`
- `scripts/test-single-role-execution-fixtures.py`
- `scripts/test-state-fixtures.py`
- `scripts/test-template-integrity-fixtures.py`
- `scripts/test-template-integrity.py`
- `scripts/test-unified-gate-smoke.py`
- `scripts/validate-active-task.py`
- `scripts/validate-approval-marker.py`
- `scripts/validate-human-approval.py`
- `scripts/validate-policy.py`
- `scripts/validate-proposal-to-task-conversion.py`
- `scripts/validate-task-brief.py`

## Input Contract Signals

Static analysis detects standard argparse, sys.argv, or file-reading contracts across checkers and validators to map command line options.

## Output Contract Signals

Static analysis detects json.dump/dumps output and sys.exit/exit status codes to map output contracts.

## Write Behavior Signals

Static analysis checks for write_text, open with "w", mkdir, rename, replace, and unlink commands.

## Git Usage Signals

Static analysis flags scripts calling git commands directly or via subprocess.

## Shell / Subprocess Signals

Static analysis flags Python scripts using subprocess or os.system calls.

## Unknown Responsibility Items

Total unknown responsibility items: 24

## Needs Later Review

All items are mapped with uncertainty labels (NEEDS_REVIEW) or specific stage candidates (M71.3/M71.4/M71.5/M71.6).

## M71.3 Candidates

Total duplicate candidate scripts flagged for legacy/duplicate review: 0

## M71.4 Candidates

Total scripts flagged for write/subprocess execution review: 147
- `install.sh`
- `scripts/activate-task.py`
- `scripts/agentos-audit-log.py`
- `scripts/agentos-command-guard.py`
- `scripts/agentos-enforce.py`
- `scripts/agentos-explain.py`
- `scripts/agentos-git-guard.py`
- `scripts/agentos-human-gate.py`
- `scripts/agentos-next-step.py`
- `scripts/agentos-retry-enforce.py`
- `scripts/agentos-status.py`
- `scripts/agentos-tui.py`
- `scripts/agentos-validate.py`
- `scripts/agentos-view-model.py`
- `scripts/agentos-violation-enforce.py`
- `scripts/agentos-write-guard.py`
- `scripts/agentos.py`
- `scripts/apply-transition.py`
- `scripts/audit-agentos.py`
- `scripts/audit-approval-boundary.py`
- `scripts/audit-context-layer.py`
- `scripts/audit-execution-control.py`
- `scripts/audit-gate-contract.py`
- `scripts/audit-m27-level1.py`
- `scripts/audit-m27.py`
- `scripts/audit-m31-tui-tutor.py`
- `scripts/audit-metadata-consistency.py`
- `scripts/audit-mvp-readiness.py`
- `scripts/audit-pre-merge-corridor.py`
- `scripts/audit-release-readiness.py`
- `scripts/audit-template-packaging.py`
- `scripts/audit-validation-integration.py`
- `scripts/build-context-cache.py`
- `scripts/build-context-index.py`
- `scripts/build-execution-verification-registry.py`
- `scripts/build-index.py`
- `scripts/build-task-dependency-map.py`
- `scripts/check-active-task-readiness.py`
- `scripts/check-agent-task-evidence.py`
- `scripts/check-apply-preconditions.py`
- `scripts/check-bypass-fixtures.py`
- `scripts/check-bypass-resistance.py`
- `scripts/check-context-compliance.py`
- `scripts/check-context-index-freshness.py`
- `scripts/check-context-pipeline.py`
- `scripts/check-context-required.py`
- `scripts/check-execution-result-verification.py`
- `scripts/check-execution-scope.py`
- `scripts/check-execution-verification-chain.py`
- `scripts/check-execution-verification-registry.py`
- `scripts/check-execution-verification-regression.py`
- `scripts/check-false-pass-resistance.py`
- `scripts/check-m54-queue-placement-fixtures.py`
- `scripts/check-m55-active-task-readiness-fixtures.py`
- `scripts/check-m56-execution-readiness-fixtures.py`
- `scripts/check-m57-execution-authorization-fixtures.py`
- `scripts/check-m58-controlled-execution-session-fixtures.py`
- `scripts/check-m59-execution-result-verification-fixtures.py`
- `scripts/check-m61-hardening-regression.py`
- `scripts/check-pre-merge-scope.py`
- `scripts/check-product-spec-readiness.py`
- `scripts/check-required-context-compliance.py`
- `scripts/check-required-context-pack.py`
- `scripts/check-scope-compliance.py`
- `scripts/check-single-role-execution.py`
- `scripts/check-task-acceptance-mvp.py`
- `scripts/check-task-validation-contract.py`
- `scripts/check-transition.py`
- `scripts/check-use-template-readiness.py`
- `scripts/complete-active-task.py`
- `scripts/detect-task-state.py`
- `scripts/generate-repo-map.py`
- `scripts/generate-task-contract-candidate.py`
- `scripts/generate-task-contract.py`
- `scripts/generate-tasks-from-spec.py`
- `scripts/generate-tasks-from-ux.py`
- `scripts/install-agentos.py`
- `scripts/materialize-task-candidate-placement.py`
- `scripts/prepare-clean-template.py`
- `scripts/repo-scan.py`
- `scripts/review-task-candidate-placement.py`
- `scripts/run-active-task.py`
- `scripts/run-execution-verification.py`
- `scripts/run-task-validation.py`
- `scripts/select-context.py`
- `scripts/smoke-interview-layer.py`
- `scripts/smoke-m44-decomposition.py`
- `scripts/sync-task-ids.py`
- `scripts/task-health.py`
- `scripts/test-activation-fixtures.py`
- `scripts/test-active-task-fixtures.py`
- `scripts/test-apply-transition-fixtures.py`
- `scripts/test-approval-fixtures.py`
- `scripts/test-approval-flow-smoke.py`
- `scripts/test-approval-marker-fixtures.py`
- `scripts/test-commit-push-preconditions-fixtures.py`
- `scripts/test-completion-flow-smoke.py`
- `scripts/test-enforcement-fixtures.py`
- `scripts/test-execution-runner-fixtures.py`
- `scripts/test-gate-regression-fixtures.py`
- `scripts/test-guard-failures.py`
- `scripts/test-honest-pass-fixtures.py`
- `scripts/test-human-approval-fixtures.py`
- `scripts/test-install.sh`
- `scripts/test-integrity-regression.py`
- `scripts/test-m22-guardrails.py`
- `scripts/test-m27-level1-fixtures.py`
- `scripts/test-m40-runtime-bypass-smoke.py`
- `scripts/test-negative-fixtures.py`
- `scripts/test-policy-enforcement-fixtures.py`
- `scripts/test-policy-fixtures.py`
- `scripts/test-policy-flow-smoke.py`
- `scripts/test-pre-merge-corridor-fixtures.py`
- `scripts/test-pre-merge-scope-fixtures.py`
- `scripts/test-readiness-fixtures.py`
- `scripts/test-scope-compliance-fixtures.py`
- `scripts/test-single-role-execution-fixtures.py`
- `scripts/test-state-fixtures.py`
- `scripts/test-template-integrity-fixtures.py`
- `scripts/test-template-integrity.py`
- `scripts/test-unified-gate-smoke.py`
- `scripts/validate-boundary-claims.py`
- `scripts/validate-commit-msg.py`
- `scripts/validate-contract-draft.py`
- `scripts/validate-product-spec.py`
- `scripts/validate-proposal-to-task-conversion.py`
- `scripts/validate-queue.py`
- `scripts/validate-runner-protocol.py`
- `scripts/validate-task-contract-candidate.py`
- `scripts/validate-task-state.py`
- `scripts/validate-trace.py`

## M71.5 Candidates

Total scripts flagged for Git integration review: 46
- `scripts/agentos-command-guard.py`
- `scripts/agentos-enforce.py`
- `scripts/agentos-git-guard.py`
- `scripts/audit-context-layer.py`
- `scripts/audit-m27-level1.py`
- `scripts/audit-m27.py`
- `scripts/audit-pre-merge-corridor.py`
- `scripts/audit-validation-integration.py`
- `scripts/build-context-index.py`
- `scripts/canonical-cleanup.sh`
- `scripts/check-commit-push-preconditions.py`
- `scripts/check-context-compliance.py`
- `scripts/check-context-index-freshness.py`
- `scripts/check-context-pipeline.py`
- `scripts/check-context-required.py`
- `scripts/check-execution-result-verification.py`
- `scripts/check-execution-scope.py`
- `scripts/check-execution-verification-regression.py`
- `scripts/check-m54-queue-placement-fixtures.py`
- `scripts/check-m55-active-task-readiness-fixtures.py`
- `scripts/check-pre-merge-scope.py`
- `scripts/check-required-context-compliance.py`
- `scripts/check-required-context-pack.py`
- `scripts/check-scope-compliance.py`
- `scripts/check-use-template-readiness.py`
- `scripts/install-agentos.py`
- `scripts/repo-scan.py`
- `scripts/run-execution-verification.py`
- `scripts/select-context.py`
- `scripts/sync-context.sh`
- `scripts/test-example-project.sh`
- `scripts/test-install.sh`
- `scripts/test-m27-level1-fixtures.py`
- `scripts/test-m40-runtime-bypass-smoke.py`
- `scripts/test-negative-fixtures.py`
- `scripts/test-scope-compliance-fixtures.py`
- `scripts/validate-queue.py`

## M71.6 Candidates

Total scripts flagged for template setup/run-all runner review: 2
- `install.sh`
- `scripts/run-all.sh`

## JSON Boundary Check

- PRIMARY_INPUT: reports/m71-script-inventory.md
- NAVIGATION_HELPER: reports/m71-script-inventory.json
- markdown_inventory_used_as_primary: true
- json_used_as_navigation_only: true
- json_overrode_markdown: false
- json_artifacts_created: false

No JSON/Markdown authority conflict was observed. Markdown was used as the primary source of truth, with JSON serving as a navigation helper only. No new JSON artifacts were created by M71.2.

## Lifecycle Classification Boundary

No final lifecycle status decisions were made. No files were marked as DEPRECATED, REPLACED, REMOVE, DELETE, ARCHIVE_NOW, CANONICAL_FINAL, or APPROVED_FOR_CLEANUP.
final_lifecycle_classification_made: false

## Scope Compliance

No scripts, reports, schemas, workflows, or data files were modified. Changed files are strictly limited to tasks/active-task.md and docs/SCRIPT-RESPONSIBILITY-MAP.md.
scripts_modified: false
cleanup_performed: false
registries_created: false
validators_created: false
scope_violations: false

## M71.3 Preparation Decision

may_prepare_m71_3: true_with_warnings

may_prepare_m71_3 is roadmap preparation only.
may_prepare_m71_3 does not start M71.3.
may_prepare_m71_3 is not approval.
Human review remains required.

Rationale: The script responsibility map is complete. Warnings are carried forward because legacy duplicate items, write/subprocess usage, and unknown callers/contracts are flagged for later task reviews.

## Explicit Non-Approval Boundary

This M71 script responsibility map is evidence only.
This M71 script responsibility map is not approval.
This M71 script responsibility map does not authorize cleanup.
This M71 script responsibility map does not authorize script changes.
This M71 script responsibility map does not classify final lifecycle status.
This M71 script responsibility map does not create registry authority.
This M71 script responsibility map does not authorize validator creation, fixture creation, or lifecycle mutation.
reports/m71-script-inventory.md is the source-of-truth inventory artifact.
reports/m71-script-inventory.json is a derived navigation artifact only.
reports/m71-script-inventory.json must not become source of truth.
Human review remains required.

## Final Status

FINAL_STATUS: M71_SCRIPT_RESPONSIBILITY_MAP_COMPLETE_WITH_WARNINGS
