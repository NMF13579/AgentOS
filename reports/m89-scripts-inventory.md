---
task_id: M89.1
task_name: Scripts Inventory
mode: read_only_inventory

preconditions:
  m89_0_intake_exists: true
  m89_0_scope_lock_exists: true
  m89_0_allows_m89_1: true_with_warnings

inventory_scope:
  scanned_paths:
    - scripts/**
  scripts_found_count: 202
  script_like_files_found_count: 202
  non_script_files_in_scripts_dir_count: 69

classification_rules:
  validation_authority_true_if:
    - script produces PASS/BLOCKED/UNKNOWN/NOT_RUN decision
    - script is a validator
    - script is a validation dispatcher
    - script is called by canonical validation command
    - script is called by CI/workflow validation path
    - script gates lifecycle mutation
    - script gates approval evidence
  safe_for_optimization_review_false_if:
    - validation_authority is unknown
    - affects_pass_fail_blocked is unknown
    - affects_unknown_semantics is unknown
    - affects_not_run_semantics is unknown
    - affects_lifecycle is unknown
    - affects_approval_boundary is unknown
    - documented behavior source is unknown for validation-authority script

script_inventory:
  - item_id: "M89-SCRIPT-001"
    path: "scripts/agentos-validate.py"
    file_exists: true
    file_type: "python"
    executable_role: "dispatcher"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - ".github/workflows/agentos-validate.yml"
      - "README.md"
      - "scripts/VALIDATORS.md"
    validation_authority: true
    affects_pass_fail_blocked: true
    affects_unknown_semantics: false
    affects_not_run_semantics: true
    affects_lifecycle: false
    affects_approval_boundary: false
    affects_ci_or_workflow: true
    writes_files: unknown
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: unknown
    block_reason: "UNKNOWN_CLASSIFICATION_BLOCKED"
  - item_id: "M89-SCRIPT-002"
    path: "scripts/run-all.sh"
    file_exists: true
    file_type: "shell"
    executable_role: "runner"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - "docs/installation.md"
      - "docs/quickstart.md"
      - "scripts/VALIDATORS.md"
    validation_authority: true
    affects_pass_fail_blocked: true
    affects_unknown_semantics: false
    affects_not_run_semantics: true
    affects_lifecycle: false
    affects_approval_boundary: false
    affects_ci_or_workflow: true
    writes_files: false
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: true
    block_reason: ""
  - item_id: "M89-SCRIPT-003"
    path: "scripts/health-check.sh"
    file_exists: true
    file_type: "shell"
    executable_role: "helper"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - ".github/workflows/dev-only/health.yml"
      - "scripts/VALIDATORS.md"
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
    validation_authority: true
    affects_pass_fail_blocked: true
    affects_unknown_semantics: false
    affects_not_run_semantics: true
    affects_lifecycle: false
    affects_approval_boundary: false
    affects_ci_or_workflow: true
    writes_files: false
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: true
    block_reason: ""
  - item_id: "M89-SCRIPT-004"
    path: "scripts/validate-architecture.sh"
    file_exists: true
    file_type: "shell"
    executable_role: "validator"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - ".github/workflows/dev-only/modular-validators.yml"
      - "scripts/VALIDATORS.md"
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
    validation_authority: true
    affects_pass_fail_blocked: true
    affects_unknown_semantics: false
    affects_not_run_semantics: true
    affects_lifecycle: false
    affects_approval_boundary: false
    affects_ci_or_workflow: true
    writes_files: false
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: true
    block_reason: ""
  - item_id: "M89-SCRIPT-005"
    path: "scripts/audit-agentos.py"
    file_exists: true
    file_type: "python"
    executable_role: "validator"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - "llms.txt"
      - "README.md"
      - "docs/SAFETY-BOUNDARIES.md"
    validation_authority: true
    affects_pass_fail_blocked: true
    affects_unknown_semantics: false
    affects_not_run_semantics: true
    affects_lifecycle: false
    affects_approval_boundary: false
    affects_ci_or_workflow: false
    writes_files: false
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: true
    block_reason: ""
  - item_id: "M89-SCRIPT-006"
    path: "scripts/check-execution-readiness.py"
    file_exists: true
    file_type: "python"
    executable_role: "validator"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - "docs/EXECUTION-VERIFICATION-SOURCE-OF-TRUTH.md"
      - "docs/TASK-EXECUTION-READINESS-CLI.md"
      - "tests/fixtures/execution-readiness/positive/valid-execution-preconditions-pass.json"
    validation_authority: true
    affects_pass_fail_blocked: true
    affects_unknown_semantics: false
    affects_not_run_semantics: true
    affects_lifecycle: false
    affects_approval_boundary: true
    affects_ci_or_workflow: false
    writes_files: false
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: true
    block_reason: ""
  - item_id: "M89-SCRIPT-007"
    path: "scripts/check-execution-authorization.py"
    file_exists: true
    file_type: "python"
    executable_role: "validator"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - "docs/EXECUTION-VERIFICATION-SOURCE-OF-TRUTH.md"
      - "docs/TASK-EXECUTION-AUTHORIZATION-CLI.md"
      - "docs/TASK-EXECUTION-AUTHORIZATION-ARCHITECTURE.md"
    validation_authority: true
    affects_pass_fail_blocked: true
    affects_unknown_semantics: false
    affects_not_run_semantics: true
    affects_lifecycle: false
    affects_approval_boundary: true
    affects_ci_or_workflow: false
    writes_files: false
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: true
    block_reason: ""
  - item_id: "M89-SCRIPT-008"
    path: "scripts/check-controlled-execution-session.py"
    file_exists: true
    file_type: "python"
    executable_role: "validator"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - "docs/EXECUTION-VERIFICATION-SOURCE-OF-TRUTH.md"
      - "docs/CONTROLLED-EXECUTION-SESSION-FIXTURE-RUNNER.md"
      - "tests/fixtures/controlled-execution-session/negative/negative-boundary-blocked/expected.json"
    validation_authority: true
    affects_pass_fail_blocked: true
    affects_unknown_semantics: false
    affects_not_run_semantics: true
    affects_lifecycle: false
    affects_approval_boundary: true
    affects_ci_or_workflow: false
    writes_files: false
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: true
    block_reason: ""
  - item_id: "M89-SCRIPT-009"
    path: "scripts/check-execution-result-verification.py"
    file_exists: true
    file_type: "python"
    executable_role: "validator"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - "docs/EXECUTION-VERIFICATION-SOURCE-OF-TRUTH.md"
      - "docs/EXECUTION-RESULT-VERIFICATION-ARCHITECTURE.md"
      - "docs/EXECUTION-RESULT-VERIFICATION-FIXTURE-RUNNER.md"
    validation_authority: true
    affects_pass_fail_blocked: true
    affects_unknown_semantics: false
    affects_not_run_semantics: true
    affects_lifecycle: false
    affects_approval_boundary: false
    affects_ci_or_workflow: false
    writes_files: false
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: true
    block_reason: ""
  - item_id: "M89-SCRIPT-010"
    path: "scripts/check-false-pass-resistance.py"
    file_exists: true
    file_type: "python"
    executable_role: "validator"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - "docs/FALSE-PASS-RESISTANCE-CHECKER.md"
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
      - "reports/m67-false-pass-evidence-report.md"
    validation_authority: true
    affects_pass_fail_blocked: true
    affects_unknown_semantics: true
    affects_not_run_semantics: false
    affects_lifecycle: false
    affects_approval_boundary: false
    affects_ci_or_workflow: false
    writes_files: false
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: true
    block_reason: ""
  - item_id: "M89-SCRIPT-011"
    path: "scripts/check-validator-authority-boundary.py"
    file_exists: true
    file_type: "python"
    executable_role: "validator"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
      - "reports/m40-11-validator-authority-boundary.md"
      - "reports/m89-scripts-inventory.md"
    validation_authority: true
    affects_pass_fail_blocked: true
    affects_unknown_semantics: false
    affects_not_run_semantics: false
    affects_lifecycle: false
    affects_approval_boundary: true
    affects_ci_or_workflow: false
    writes_files: false
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: true
    block_reason: ""
  - item_id: "M89-SCRIPT-012"
    path: "scripts/validate-status-semantics.py"
    file_exists: true
    file_type: "python"
    executable_role: "validator"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
      - "reports/milestone-10-final-hardening-review.md"
      - "reports/m40-fixup-help-semantics-report.md"
    validation_authority: true
    affects_pass_fail_blocked: true
    affects_unknown_semantics: true
    affects_not_run_semantics: true
    affects_lifecycle: false
    affects_approval_boundary: false
    affects_ci_or_workflow: false
    writes_files: false
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: true
    block_reason: ""
  - item_id: "M89-SCRIPT-013"
    path: "scripts/validate-human-approval.py"
    file_exists: true
    file_type: "python"
    executable_role: "validator"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
      - "reports/m57-execution-authorization-evidence-report.md"
      - "tests/fixtures/negative/activation/missing-approval-marker/approvals/approval.md"
    validation_authority: true
    affects_pass_fail_blocked: true
    affects_unknown_semantics: false
    affects_not_run_semantics: false
    affects_lifecycle: false
    affects_approval_boundary: true
    affects_ci_or_workflow: false
    writes_files: false
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: true
    block_reason: ""
  - item_id: "M89-SCRIPT-014"
    path: "scripts/validate-approval-marker.py"
    file_exists: true
    file_type: "python"
    executable_role: "validator"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - "docs/EXECUTION-READINESS.md"
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
      - "tests/fixtures/negative/activation/invalid-approval-marker/task/TASK.md"
    validation_authority: true
    affects_pass_fail_blocked: true
    affects_unknown_semantics: false
    affects_not_run_semantics: false
    affects_lifecycle: false
    affects_approval_boundary: true
    affects_ci_or_workflow: false
    writes_files: false
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: true
    block_reason: ""
  - item_id: "M89-SCRIPT-015"
    path: "scripts/validate-lifecycle-apply.py"
    file_exists: true
    file_type: "python"
    executable_role: "validator"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - "docs/SCRIPT-LIFECYCLE-POLICY.md"
      - "docs/APPLY-COMMAND-INTEGRATION.md"
      - "reports/m16-completion-review.md"
    validation_authority: true
    affects_pass_fail_blocked: true
    affects_unknown_semantics: false
    affects_not_run_semantics: false
    affects_lifecycle: true
    affects_approval_boundary: true
    affects_ci_or_workflow: false
    writes_files: false
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: true
    block_reason: ""
  - item_id: "M89-SCRIPT-016"
    path: "scripts/check-apply-preconditions.py"
    file_exists: true
    file_type: "python"
    executable_role: "validator"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - "docs/APPLY-PRECONDITIONS.md"
      - "docs/APPLY-COMMAND-INTEGRATION.md"
      - "scripts/apply-transition.py"
    validation_authority: true
    affects_pass_fail_blocked: true
    affects_unknown_semantics: false
    affects_not_run_semantics: false
    affects_lifecycle: true
    affects_approval_boundary: true
    affects_ci_or_workflow: false
    writes_files: false
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: true
    block_reason: ""
  - item_id: "M89-SCRIPT-017"
    path: "scripts/check-transition.py"
    file_exists: true
    file_type: "python"
    executable_role: "validator"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - "docs/TASK-TRANSITION-RULES.md"
      - "docs/SCRIPT-LIFECYCLE-POLICY.md"
      - "reports/task-state-machine-smoke.md"
    validation_authority: true
    affects_pass_fail_blocked: true
    affects_unknown_semantics: false
    affects_not_run_semantics: false
    affects_lifecycle: true
    affects_approval_boundary: false
    affects_ci_or_workflow: false
    writes_files: false
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: true
    block_reason: ""
  - item_id: "M89-SCRIPT-018"
    path: "scripts/apply-transition.py"
    file_exists: true
    file_type: "python"
    executable_role: "dispatcher"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - "docs/APPLY-COMMAND-INTEGRATION.md"
      - "docs/SCRIPT-LIFECYCLE-POLICY.md"
      - "scripts/test-policy-flow-smoke.py"
    validation_authority: false
    affects_pass_fail_blocked: false
    affects_unknown_semantics: false
    affects_not_run_semantics: false
    affects_lifecycle: true
    affects_approval_boundary: true
    affects_ci_or_workflow: false
    writes_files: true
    reads_reports: true
    produces_reports: true
    safe_for_optimization_review: true
    block_reason: ""
  - item_id: "M89-SCRIPT-019"
    path: "scripts/complete-active-task.py"
    file_exists: true
    file_type: "python"
    executable_role: "dispatcher"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - "docs/AGENTOS-WORKFLOW-REVIEW.md"
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
      - "reports/m15-completion-review.md"
    validation_authority: false
    affects_pass_fail_blocked: false
    affects_unknown_semantics: false
    affects_not_run_semantics: false
    affects_lifecycle: true
    affects_approval_boundary: true
    affects_ci_or_workflow: false
    writes_files: true
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: true
    block_reason: ""
  - item_id: "M89-SCRIPT-020"
    path: "scripts/activate-task.py"
    file_exists: true
    file_type: "python"
    executable_role: "dispatcher"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - "docs/APPROVED-MODE-CONTRACT.md"
      - "docs/ACTIVATION-RECOVERY.md"
      - "tools/state/ACTIVATE-TASK.md"
    validation_authority: false
    affects_pass_fail_blocked: false
    affects_unknown_semantics: false
    affects_not_run_semantics: false
    affects_lifecycle: true
    affects_approval_boundary: true
    affects_ci_or_workflow: false
    writes_files: true
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: true
    block_reason: ""
  - item_id: "M89-SCRIPT-021"
    path: "scripts/run-task-validation.py"
    file_exists: true
    file_type: "python"
    executable_role: "runner"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - "docs/UNIFIED-RUNNER.md"
      - "docs/SCRIPT-EXIT-CODE-STANDARD.md"
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
    validation_authority: true
    affects_pass_fail_blocked: true
    affects_unknown_semantics: false
    affects_not_run_semantics: true
    affects_lifecycle: false
    affects_approval_boundary: false
    affects_ci_or_workflow: false
    writes_files: false
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: true
    block_reason: ""
  - item_id: "M89-SCRIPT-022"
    path: "scripts/run-execution-verification.py"
    file_exists: true
    file_type: "python"
    executable_role: "runner"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - "docs/CONTROLLED-EXECUTION-RUNNER.md"
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
      - "reports/m66-unified-runner-integration-summary.md"
    validation_authority: true
    affects_pass_fail_blocked: true
    affects_unknown_semantics: false
    affects_not_run_semantics: true
    affects_lifecycle: false
    affects_approval_boundary: false
    affects_ci_or_workflow: false
    writes_files: false
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: true
    block_reason: ""
  - item_id: "M89-SCRIPT-023"
    path: "scripts/agentos-enforce.py"
    file_exists: true
    file_type: "python"
    executable_role: "dispatcher"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - ".github/workflows/dev-only/m27-enforcement.yml"
      - "docs/M27-RUNTIME-BOUNDARY-CONTRACT.md"
      - "docs/SCRIPT-OUTPUT-CONTRACT.md"
    validation_authority: true
    affects_pass_fail_blocked: true
    affects_unknown_semantics: false
    affects_not_run_semantics: true
    affects_lifecycle: false
    affects_approval_boundary: false
    affects_ci_or_workflow: true
    writes_files: unknown
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: unknown
    block_reason: "UNKNOWN_CLASSIFICATION_BLOCKED"
  - item_id: "M89-SCRIPT-024"
    path: "scripts/agentos-command-guard.py"
    file_exists: true
    file_type: "python"
    executable_role: "dispatcher"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - ".github/workflows/dev-only/m27-enforcement.yml"
      - "docs/M27-COMMAND-ENFORCEMENT-RUNTIME.md"
      - "docs/SCRIPT-DANGEROUS-OPERATIONS-AUDIT.md"
    validation_authority: true
    affects_pass_fail_blocked: true
    affects_unknown_semantics: false
    affects_not_run_semantics: true
    affects_lifecycle: false
    affects_approval_boundary: false
    affects_ci_or_workflow: true
    writes_files: unknown
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: unknown
    block_reason: "UNKNOWN_CLASSIFICATION_BLOCKED"
  - item_id: "M89-SCRIPT-025"
    path: "scripts/agentos-human-gate.py"
    file_exists: true
    file_type: "python"
    executable_role: "dispatcher"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - ".github/workflows/dev-only/m27-enforcement.yml"
      - "docs/M27-UNIFIED-ENFORCEMENT-CLI.md"
      - "docs/M27-RUNTIME-BOUNDARY-CONTRACT.md"
    validation_authority: true
    affects_pass_fail_blocked: true
    affects_unknown_semantics: false
    affects_not_run_semantics: true
    affects_lifecycle: false
    affects_approval_boundary: true
    affects_ci_or_workflow: true
    writes_files: unknown
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: unknown
    block_reason: "UNKNOWN_CLASSIFICATION_BLOCKED"
  - item_id: "M89-SCRIPT-026"
    path: "scripts/agentos-violation-enforce.py"
    file_exists: true
    file_type: "python"
    executable_role: "dispatcher"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - ".github/workflows/dev-only/m27-enforcement.yml"
      - "docs/M27-RUNTIME-BOUNDARY-CONTRACT.md"
      - "docs/SCRIPT-LIFECYCLE-POLICY.md"
    validation_authority: true
    affects_pass_fail_blocked: true
    affects_unknown_semantics: false
    affects_not_run_semantics: true
    affects_lifecycle: false
    affects_approval_boundary: false
    affects_ci_or_workflow: true
    writes_files: unknown
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: unknown
    block_reason: "UNKNOWN_CLASSIFICATION_BLOCKED"
  - item_id: "M89-SCRIPT-027"
    path: "scripts/agentos-retry-enforce.py"
    file_exists: true
    file_type: "python"
    executable_role: "dispatcher"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - ".github/workflows/dev-only/m27-enforcement.yml"
      - "docs/M27-RUNTIME-BOUNDARY-CONTRACT.md"
      - "docs/SCRIPT-OUTPUT-CONTRACT.md"
    validation_authority: true
    affects_pass_fail_blocked: true
    affects_unknown_semantics: false
    affects_not_run_semantics: true
    affects_lifecycle: false
    affects_approval_boundary: false
    affects_ci_or_workflow: true
    writes_files: unknown
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: unknown
    block_reason: "UNKNOWN_CLASSIFICATION_BLOCKED"
  - item_id: "M89-SCRIPT-028"
    path: "scripts/check-m74-dispatcher-regression.py"
    file_exists: true
    file_type: "python"
    executable_role: "validator"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - "reports/m74-regression-evidence-report.md"
      - "reports/m86-cleanup-candidate-register.md"
      - "reports/m86-artifact-registry.md"
    validation_authority: true
    affects_pass_fail_blocked: true
    affects_unknown_semantics: false
    affects_not_run_semantics: true
    affects_lifecycle: false
    affects_approval_boundary: false
    affects_ci_or_workflow: false
    writes_files: false
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: false
    block_reason: "SCRIPT_SPEC_CONTRACT_UNKNOWN_BLOCKED"
  - item_id: "M89-SCRIPT-029"
    path: "scripts/agent-complete.py"
    file_exists: true
    file_type: "python"
    executable_role: "dispatcher"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - "prompt-packs/claude-code.md"
      - "tools/runner-validator/VALIDATE-RUNNER-PROTOCOL.md"
      - "tasks/queue/20260428-runner-human-checkpoints.md"
    validation_authority: false
    affects_pass_fail_blocked: false
    affects_unknown_semantics: false
    affects_not_run_semantics: false
    affects_lifecycle: true
    affects_approval_boundary: false
    affects_ci_or_workflow: false
    writes_files: unknown
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: unknown
    block_reason: "UNKNOWN_CLASSIFICATION_BLOCKED"
  - item_id: "M89-SCRIPT-030"
    path: "scripts/agent-fail.py"
    file_exists: true
    file_type: "python"
    executable_role: "dispatcher"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - "prompt-packs/claude-code.md"
      - "tools/runner-validator/VALIDATE-RUNNER-PROTOCOL.md"
      - "tasks/queue/20260428-runner-human-checkpoints.md"
    validation_authority: false
    affects_pass_fail_blocked: false
    affects_unknown_semantics: false
    affects_not_run_semantics: false
    affects_lifecycle: true
    affects_approval_boundary: false
    affects_ci_or_workflow: false
    writes_files: unknown
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: unknown
    block_reason: "UNKNOWN_CLASSIFICATION_BLOCKED"
  - item_id: "M89-SCRIPT-031"
    path: "scripts/agent-next.py"
    file_exists: true
    file_type: "python"
    executable_role: "dispatcher"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - "prompt-packs/claude-code.md"
      - "tools/runner-validator/VALIDATE-RUNNER-PROTOCOL.md"
      - "tasks/queue/20260428-runner-human-checkpoints.md"
    validation_authority: false
    affects_pass_fail_blocked: false
    affects_unknown_semantics: false
    affects_not_run_semantics: false
    affects_lifecycle: true
    affects_approval_boundary: false
    affects_ci_or_workflow: false
    writes_files: unknown
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: unknown
    block_reason: "UNKNOWN_CLASSIFICATION_BLOCKED"
  - item_id: "M89-SCRIPT-032"
    path: "scripts/detect-task-state.py"
    file_exists: true
    file_type: "python"
    executable_role: "dispatcher"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - "tools/state/DETECT-TASK-STATE.md"
      - "docs/TASK-TRANSITION-RULES.md"
      - "docs/EXECUTION-READINESS.md"
    validation_authority: false
    affects_pass_fail_blocked: false
    affects_unknown_semantics: false
    affects_not_run_semantics: false
    affects_lifecycle: true
    affects_approval_boundary: false
    affects_ci_or_workflow: false
    writes_files: unknown
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: unknown
    block_reason: "UNKNOWN_CLASSIFICATION_BLOCKED"
  - item_id: "M89-SCRIPT-033"
    path: "scripts/review-task-candidate-placement.py"
    file_exists: true
    file_type: "python"
    executable_role: "dispatcher"
    likely_entrypoint: true
    likely_imported_helper: false
    referenced_by:
      - "docs/TASK-CANDIDATE-PLACEMENT-REVIEW.md"
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
      - "examples/task-candidate-placement-review-dry-run-agent-action-review.md"
    validation_authority: false
    affects_pass_fail_blocked: false
    affects_unknown_semantics: false
    affects_not_run_semantics: false
    affects_lifecycle: false
    affects_approval_boundary: false
    affects_ci_or_workflow: false
    writes_files: unknown
    reads_reports: true
    produces_reports: false
    safe_for_optimization_review: unknown
    block_reason: "UNKNOWN_CLASSIFICATION_BLOCKED"

all_script_paths:
  - "scripts/activate-task.py"
  - "scripts/agent-complete.py"
  - "scripts/agent-fail.py"
  - "scripts/agent-next.py"
  - "scripts/agentos-audit-log.py"
  - "scripts/agentos-command-guard.py"
  - "scripts/agentos-enforce.py"
  - "scripts/agentos-explain.py"
  - "scripts/agentos-git-guard.py"
  - "scripts/agentos-human-gate.py"
  - "scripts/agentos-next-step.py"
  - "scripts/agentos-permission-state.py"
  - "scripts/agentos-retry-enforce.py"
  - "scripts/agentos-status.py"
  - "scripts/agentos-tui.py"
  - "scripts/agentos-validate.py"
  - "scripts/agentos-view-model.py"
  - "scripts/agentos-violation-enforce.py"
  - "scripts/agentos-write-guard.py"
  - "scripts/agentos.py"
  - "scripts/apply-transition.py"
  - "scripts/audit-agentos.py"
  - "scripts/audit-approval-boundary.py"
  - "scripts/audit-context-layer.py"
  - "scripts/audit-enforcement.py"
  - "scripts/audit-execution-control.py"
  - "scripts/audit-gate-contract.py"
  - "scripts/audit-lifecycle-mutation.py"
  - "scripts/audit-m27-level1.py"
  - "scripts/audit-m27.py"
  - "scripts/audit-m30-context-pipeline.py"
  - "scripts/audit-m31-tui-tutor.py"
  - "scripts/audit-metadata-consistency.py"
  - "scripts/audit-mvp-readiness.py"
  - "scripts/audit-policy-boundary.py"
  - "scripts/audit-pre-merge-corridor.py"
  - "scripts/audit-release-readiness.py"
  - "scripts/audit-template-packaging.py"
  - "scripts/audit-validation-integration.py"
  - "scripts/build-context-cache.py"
  - "scripts/build-context-index.py"
  - "scripts/build-execution-verification-registry.py"
  - "scripts/build-index.py"
  - "scripts/build-task-dependency-map.py"
  - "scripts/canonical-cleanup.sh"
  - "scripts/check-acceptance-criteria.py"
  - "scripts/check-active-task-readiness.py"
  - "scripts/check-agent-task-evidence.py"
  - "scripts/check-apply-preconditions.py"
  - "scripts/check-bypass-fixtures.py"
  - "scripts/check-bypass-resistance.py"
  - "scripts/check-canary-integrity.py"
  - "scripts/check-commit-push-preconditions.py"
  - "scripts/check-completion-readiness.py"
  - "scripts/check-context-compliance.py"
  - "scripts/check-context-index-freshness.py"
  - "scripts/check-context-pipeline.py"
  - "scripts/check-context-required.py"
  - "scripts/check-controlled-execution-session.py"
  - "scripts/check-dangerous-commands.py"
  - "scripts/check-evidence-amendments.py"
  - "scripts/check-evidence-binding.py"
  - "scripts/check-evidence-immutability.py"
  - "scripts/check-execution-authorization.py"
  - "scripts/check-execution-readiness.py"
  - "scripts/check-execution-result-verification.py"
  - "scripts/check-execution-scope.py"
  - "scripts/check-execution-verification-chain.py"
  - "scripts/check-execution-verification-registry.py"
  - "scripts/check-execution-verification-regression.py"
  - "scripts/check-false-pass-resistance.py"
  - "scripts/check-github-platform-enforcement.py"
  - "scripts/check-identity-drift.sh"
  - "scripts/check-interview-completeness.py"
  - "scripts/check-links.py"
  - "scripts/check-llms-graph-files.sh"
  - "scripts/check-m54-queue-placement-fixtures.py"
  - "scripts/check-m55-active-task-readiness-fixtures.py"
  - "scripts/check-m56-execution-readiness-fixtures.py"
  - "scripts/check-m57-execution-authorization-fixtures.py"
  - "scripts/check-m58-controlled-execution-session-fixtures.py"
  - "scripts/check-m59-execution-result-verification-fixtures.py"
  - "scripts/check-m61-hardening-regression.py"
  - "scripts/check-m74-dispatcher-regression.py"
  - "scripts/check-pr-quality.py"
  - "scripts/check-pre-merge-scope.py"
  - "scripts/check-premature-artifacts.sh"
  - "scripts/check-private-evaluator-consistency.py"
  - "scripts/check-process-trace.py"
  - "scripts/check-product-spec-readiness.py"
  - "scripts/check-readiness-assertions.py"
  - "scripts/check-required-context-compliance.py"
  - "scripts/check-required-context-pack.py"
  - "scripts/check-risk.py"
  - "scripts/check-role-separation.py"
  - "scripts/check-scope-compliance.py"
  - "scripts/check-single-role-execution.py"
  - "scripts/check-task-acceptance-mvp.py"
  - "scripts/check-task-validation-contract.py"
  - "scripts/check-template-cleanliness.py"
  - "scripts/check-template-integrity.py"
  - "scripts/check-transition.py"
  - "scripts/check-use-template-readiness.py"
  - "scripts/check-validator-authority-boundary.py"
  - "scripts/complete-active-task.py"
  - "scripts/detect-task-state.py"
  - "scripts/generate-repo-map.py"
  - "scripts/generate-task-contract-candidate.py"
  - "scripts/generate-task-contract.py"
  - "scripts/generate-tasks-from-spec.py"
  - "scripts/generate-tasks-from-ux.py"
  - "scripts/health-check.sh"
  - "scripts/install-agentos.py"
  - "scripts/install-hooks.sh"
  - "scripts/lib/__init__.py"
  - "scripts/lib/path_utils.py"
  - "scripts/lint-task-contract.py"
  - "scripts/materialize-task-candidate-placement.py"
  - "scripts/prepare-clean-template.py"
  - "scripts/renderers/__init__.py"
  - "scripts/renderers/plain_status_renderer.py"
  - "scripts/renderers/rich_status_renderer.py"
  - "scripts/repo-scan.py"
  - "scripts/review-task-candidate-placement.py"
  - "scripts/run-active-task.py"
  - "scripts/run-all.sh"
  - "scripts/run-execution-verification.py"
  - "scripts/run-task-validation.py"
  - "scripts/select-context.py"
  - "scripts/smoke-interview-layer.py"
  - "scripts/smoke-m44-decomposition.py"
  - "scripts/sync-context.sh"
  - "scripts/sync-task-ids.py"
  - "scripts/task-health.py"
  - "scripts/test-activation-fixtures.py"
  - "scripts/test-active-task-fixtures.py"
  - "scripts/test-apply-transition-fixtures.py"
  - "scripts/test-approval-fixtures.py"
  - "scripts/test-approval-flow-smoke.py"
  - "scripts/test-approval-marker-fixtures.py"
  - "scripts/test-ci-advisory-config.py"
  - "scripts/test-commit-push-preconditions-fixtures.py"
  - "scripts/test-completion-flow-smoke.py"
  - "scripts/test-enforcement-fixtures.py"
  - "scripts/test-example-project.sh"
  - "scripts/test-execution-runner-fixtures.py"
  - "scripts/test-gate-regression-fixtures.py"
  - "scripts/test-guard-failures.py"
  - "scripts/test-honest-pass-fixtures.py"
  - "scripts/test-human-approval-fixtures.py"
  - "scripts/test-install.sh"
  - "scripts/test-integrity-regression.py"
  - "scripts/test-m22-guardrails.py"
  - "scripts/test-m27-level1-fixtures.py"
  - "scripts/test-m40-runtime-bypass-smoke.py"
  - "scripts/test-negative-fixtures.py"
  - "scripts/test-policy-enforcement-fixtures.py"
  - "scripts/test-policy-fixtures.py"
  - "scripts/test-policy-flow-smoke.py"
  - "scripts/test-pre-merge-corridor-fixtures.py"
  - "scripts/test-pre-merge-scope-fixtures.py"
  - "scripts/test-readiness-fixtures.py"
  - "scripts/test-scope-compliance-fixtures.py"
  - "scripts/test-single-role-execution-fixtures.py"
  - "scripts/test-state-fixtures.py"
  - "scripts/test-template-integrity-fixtures.py"
  - "scripts/test-template-integrity.py"
  - "scripts/test-unified-gate-smoke.py"
  - "scripts/validate-active-task.py"
  - "scripts/validate-approval-marker.py"
  - "scripts/validate-architecture.sh"
  - "scripts/validate-boundary-claims.py"
  - "scripts/validate-commit-msg.py"
  - "scripts/validate-contract-draft.py"
  - "scripts/validate-docs.py"
  - "scripts/validate-frontmatter.py"
  - "scripts/validate-gate-contract.py"
  - "scripts/validate-handoff.py"
  - "scripts/validate-human-approval.py"
  - "scripts/validate-incident.py"
  - "scripts/validate-index.py"
  - "scripts/validate-lessons.py"
  - "scripts/validate-lifecycle-apply.py"
  - "scripts/validate-policy.py"
  - "scripts/validate-product-spec.py"
  - "scripts/validate-proposal-to-task-conversion.py"
  - "scripts/validate-queue-entry.py"
  - "scripts/validate-queue.py"
  - "scripts/validate-required-sections.py"
  - "scripts/validate-review.py"
  - "scripts/validate-route.py"
  - "scripts/validate-runner-protocol.py"
  - "scripts/validate-status-semantics.py"
  - "scripts/validate-task-brief.py"
  - "scripts/validate-task-contract-candidate.py"
  - "scripts/validate-task-state.py"
  - "scripts/validate-task.py"
  - "scripts/validate-trace.py"
  - "scripts/validate-ux-contract.py"
  - "scripts/validate-ux-planning-readiness.py"
  - "scripts/validate-ux-to-task-proposal.py"
  - "scripts/validate-verification.py"

blocked_from_optimization_review:
  - "scripts/agent-complete.py"
  - "scripts/agent-fail.py"
  - "scripts/agent-next.py"
  - "scripts/agentos-command-guard.py"
  - "scripts/agentos-enforce.py"
  - "scripts/agentos-explain.py"
  - "scripts/agentos-git-guard.py"
  - "scripts/agentos-human-gate.py"
  - "scripts/agentos-next-step.py"
  - "scripts/agentos-permission-state.py"
  - "scripts/agentos-retry-enforce.py"
  - "scripts/agentos-status.py"
  - "scripts/agentos-tui.py"
  - "scripts/agentos-validate.py"
  - "scripts/agentos-view-model.py"
  - "scripts/agentos-violation-enforce.py"
  - "scripts/agentos-write-guard.py"
  - "scripts/canonical-cleanup.sh"
  - "scripts/check-m74-dispatcher-regression.py"
  - "scripts/detect-task-state.py"
  - "scripts/review-task-candidate-placement.py"

unknowns_present: true
unknown_items_count: 20
blocked_from_optimization_review_count: 21

validation:
  git_status_short_run: true
  discovery_command_run: true
  discovery_command: "find scripts -type f | sort"
  canonical_validation_run: true
  validation_not_run: false
  validation_result_claimed_pass: false
  canonical_validation_command: "python3 scripts/audit-agentos.py"
  canonical_validation_result: "PASS_WITH_WARNINGS"

FINAL_STATUS: M89_1_SCRIPTS_INVENTORY_COMPLETE_WITH_WARNINGS

M89_1_OVERALL_STATUS:
  scripts_inventory_status: M89_1_SCRIPTS_INVENTORY_COMPLETE_WITH_WARNINGS
  validation_authority_map_status: M89_1_VALIDATION_AUTHORITY_MAP_COMPLETE_WITH_WARNINGS
  script_spec_source_map_status: M89_1_SCRIPT_SPEC_SOURCE_MAP_COMPLETE_WITH_WARNINGS
  scripts_modified: false
  docs_modified: false
  schemas_modified: false
  workflows_modified: false
  approval_created: false
  lifecycle_mutation_created: false
  candidates_created: false
  human_subset_selected: false
  m89_2_started: false
  m90_started: false
  m91_started: false
  may_prepare_m89_2_script_candidate_register: true_with_warnings
  FINAL_STATUS: M89_1_SCRIPT_MAPPING_COMPLETE_WITH_WARNINGS
---

# M89.1 Scripts Inventory

Инвентарь собран. Найдено 202 script-like файла в `scripts/`, из них 111 выглядят как проверяющие скрипты, 40 как запускатели или smoke/test-скрипты, 25 как диспетчеры, 13 как генераторы, 12 как вспомогательные и 1 как cleanup-скрипт. Неясных по роли файлов в текущей классификации нет.

Отдельно выявлено 21 скрипт, который пока нельзя безопасно отдавать в следующий этап отбора. Причина простая: по статическому чтению не удалось надежно закрыть вопрос о записи файлов, побочных действиях или полном документированном контракте поведения. Для одного файла, `scripts/check-m74-dispatcher-regression.py`, не найдено явного письменного контракта поведения; для остальных 20 блокированных файлов проблема в том, что read-only разбор не доказывает безопасную поверхность записи.

Инвентарь достаточно полный, чтобы готовить M89.2, но только с предупреждениями. Это не разрешение на изменение скриптов, а только основание для следующего этапа отбора кандидатов среди уже известных и не заблокированных файлов.
