---
task_id: M89.1
task_name: Validation Authority Map
mode: read_only_authority_mapping

validation_authority_summary:
  validation_authority_scripts_count: 121
  possible_validation_authority_scripts_count: 0
  unknown_validation_authority_scripts_count: 0
  non_authority_scripts_count: 81

validation_authority_items:
  - item_id: "M89-AUTH-001"
    script_path: "scripts/agentos-validate.py"
    source_inventory_item: "M89-SCRIPT-001"
    authority_type:
      - "pass_fail_result"
      - "exit_code_contract"
      - "json_contract"
      - "cli_contract"
      - "ci_validation"
    authority_confidence: "high"
    evidence_paths:
      - "scripts/VALIDATORS.md"
      - ".github/workflows/agentos-validate.yml"
      - "README.md"
    affects_result_semantics: true
    affects_exit_codes: true
    affects_json_output: true
    affects_cli_behavior: true
    affects_error_format: true
    affects_lifecycle_mutation: false
    affects_approval_boundary: false
    optimization_review_allowed: false
    block_reason: "UNKNOWN_CLASSIFICATION_BLOCKED"
  - item_id: "M89-AUTH-002"
    script_path: "scripts/run-all.sh"
    source_inventory_item: "M89-SCRIPT-002"
    authority_type:
      - "pass_fail_result"
      - "exit_code_contract"
      - "cli_contract"
      - "ci_validation"
    authority_confidence: "high"
    evidence_paths:
      - "scripts/VALIDATORS.md"
      - "docs/installation.md"
      - "docs/quickstart.md"
    affects_result_semantics: true
    affects_exit_codes: true
    affects_json_output: false
    affects_cli_behavior: true
    affects_error_format: false
    affects_lifecycle_mutation: false
    affects_approval_boundary: false
    optimization_review_allowed: true
    block_reason: ""
  - item_id: "M89-AUTH-003"
    script_path: "scripts/health-check.sh"
    source_inventory_item: "M89-SCRIPT-003"
    authority_type:
      - "pass_fail_result"
      - "exit_code_contract"
      - "cli_contract"
      - "ci_validation"
    authority_confidence: "high"
    evidence_paths:
      - "scripts/VALIDATORS.md"
      - ".github/workflows/dev-only/health.yml"
      - "docs/SCRIPT-OUTPUT-CONTRACT.md"
    affects_result_semantics: true
    affects_exit_codes: true
    affects_json_output: false
    affects_cli_behavior: true
    affects_error_format: false
    affects_lifecycle_mutation: false
    affects_approval_boundary: false
    optimization_review_allowed: true
    block_reason: ""
  - item_id: "M89-AUTH-004"
    script_path: "scripts/audit-agentos.py"
    source_inventory_item: "M89-SCRIPT-005"
    authority_type:
      - "pass_fail_result"
      - "cli_contract"
      - "ci_validation"
    authority_confidence: "high"
    evidence_paths:
      - "llms.txt"
      - "README.md"
      - "docs/SAFETY-BOUNDARIES.md"
    affects_result_semantics: true
    affects_exit_codes: true
    affects_json_output: false
    affects_cli_behavior: true
    affects_error_format: true
    affects_lifecycle_mutation: false
    affects_approval_boundary: false
    optimization_review_allowed: true
    block_reason: ""
  - item_id: "M89-AUTH-005"
    script_path: "scripts/check-execution-readiness.py"
    source_inventory_item: "M89-SCRIPT-006"
    authority_type:
      - "pass_fail_result"
      - "blocked_result"
      - "exit_code_contract"
      - "cli_contract"
      - "approval_boundary_gate"
    authority_confidence: "high"
    evidence_paths:
      - "docs/EXECUTION-VERIFICATION-SOURCE-OF-TRUTH.md"
      - "docs/TASK-EXECUTION-READINESS-CLI.md"
      - "schemas/task-execution-readiness-input.schema.json"
    affects_result_semantics: true
    affects_exit_codes: true
    affects_json_output: false
    affects_cli_behavior: true
    affects_error_format: true
    affects_lifecycle_mutation: false
    affects_approval_boundary: true
    optimization_review_allowed: true
    block_reason: ""
  - item_id: "M89-AUTH-006"
    script_path: "scripts/check-execution-authorization.py"
    source_inventory_item: "M89-SCRIPT-007"
    authority_type:
      - "pass_fail_result"
      - "blocked_result"
      - "exit_code_contract"
      - "cli_contract"
      - "approval_boundary_gate"
    authority_confidence: "high"
    evidence_paths:
      - "docs/EXECUTION-VERIFICATION-SOURCE-OF-TRUTH.md"
      - "docs/TASK-EXECUTION-AUTHORIZATION-CLI.md"
      - "schemas/task-execution-authorization-preconditions.schema.json"
    affects_result_semantics: true
    affects_exit_codes: true
    affects_json_output: false
    affects_cli_behavior: true
    affects_error_format: true
    affects_lifecycle_mutation: false
    affects_approval_boundary: true
    optimization_review_allowed: true
    block_reason: ""
  - item_id: "M89-AUTH-007"
    script_path: "scripts/check-controlled-execution-session.py"
    source_inventory_item: "M89-SCRIPT-008"
    authority_type:
      - "pass_fail_result"
      - "blocked_result"
      - "exit_code_contract"
      - "cli_contract"
      - "approval_boundary_gate"
    authority_confidence: "high"
    evidence_paths:
      - "docs/EXECUTION-VERIFICATION-SOURCE-OF-TRUTH.md"
      - "docs/CONTROLLED-EXECUTION-SESSION-FIXTURE-RUNNER.md"
      - "schemas/execution-session-boundary.schema.json"
    affects_result_semantics: true
    affects_exit_codes: true
    affects_json_output: false
    affects_cli_behavior: true
    affects_error_format: true
    affects_lifecycle_mutation: false
    affects_approval_boundary: true
    optimization_review_allowed: true
    block_reason: ""
  - item_id: "M89-AUTH-008"
    script_path: "scripts/check-execution-result-verification.py"
    source_inventory_item: "M89-SCRIPT-009"
    authority_type:
      - "pass_fail_result"
      - "blocked_result"
      - "exit_code_contract"
      - "json_contract"
      - "cli_contract"
    authority_confidence: "high"
    evidence_paths:
      - "docs/EXECUTION-VERIFICATION-SOURCE-OF-TRUTH.md"
      - "docs/EXECUTION-RESULT-VERIFICATION-ARCHITECTURE.md"
      - "schemas/execution-result-verification-result-output.schema.json"
    affects_result_semantics: true
    affects_exit_codes: true
    affects_json_output: true
    affects_cli_behavior: true
    affects_error_format: true
    affects_lifecycle_mutation: false
    affects_approval_boundary: false
    optimization_review_allowed: true
    block_reason: ""
  - item_id: "M89-AUTH-009"
    script_path: "scripts/check-false-pass-resistance.py"
    source_inventory_item: "M89-SCRIPT-010"
    authority_type:
      - "pass_fail_result"
      - "unknown_result"
      - "exit_code_contract"
      - "cli_contract"
    authority_confidence: "high"
    evidence_paths:
      - "docs/FALSE-PASS-RESISTANCE-CHECKER.md"
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
      - "reports/m67-false-pass-evidence-report.md"
    affects_result_semantics: true
    affects_exit_codes: true
    affects_json_output: false
    affects_cli_behavior: true
    affects_error_format: false
    affects_lifecycle_mutation: false
    affects_approval_boundary: false
    optimization_review_allowed: true
    block_reason: ""
  - item_id: "M89-AUTH-010"
    script_path: "scripts/validate-status-semantics.py"
    source_inventory_item: "M89-SCRIPT-012"
    authority_type:
      - "pass_fail_result"
      - "unknown_result"
      - "not_run_result"
      - "cli_contract"
    authority_confidence: "medium"
    evidence_paths:
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
      - "reports/m40-fixup-help-semantics-report.md"
      - "reports/milestone-10-final-hardening-review.md"
    affects_result_semantics: true
    affects_exit_codes: true
    affects_json_output: false
    affects_cli_behavior: true
    affects_error_format: false
    affects_lifecycle_mutation: false
    affects_approval_boundary: false
    optimization_review_allowed: true
    block_reason: ""
  - item_id: "M89-AUTH-011"
    script_path: "scripts/validate-human-approval.py"
    source_inventory_item: "M89-SCRIPT-013"
    authority_type:
      - "blocked_result"
      - "cli_contract"
      - "approval_boundary_gate"
    authority_confidence: "high"
    evidence_paths:
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
      - "reports/m57-execution-authorization-evidence-report.md"
      - "tests/fixtures/negative/activation/missing-approval-marker/approvals/approval.md"
    affects_result_semantics: true
    affects_exit_codes: true
    affects_json_output: false
    affects_cli_behavior: true
    affects_error_format: true
    affects_lifecycle_mutation: false
    affects_approval_boundary: true
    optimization_review_allowed: true
    block_reason: ""
  - item_id: "M89-AUTH-012"
    script_path: "scripts/validate-approval-marker.py"
    source_inventory_item: "M89-SCRIPT-014"
    authority_type:
      - "blocked_result"
      - "cli_contract"
      - "approval_boundary_gate"
    authority_confidence: "high"
    evidence_paths:
      - "docs/EXECUTION-READINESS.md"
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
      - "tests/fixtures/negative/activation/invalid-approval-marker/task/TASK.md"
    affects_result_semantics: true
    affects_exit_codes: true
    affects_json_output: false
    affects_cli_behavior: true
    affects_error_format: true
    affects_lifecycle_mutation: false
    affects_approval_boundary: true
    optimization_review_allowed: true
    block_reason: ""
  - item_id: "M89-AUTH-013"
    script_path: "scripts/validate-lifecycle-apply.py"
    source_inventory_item: "M89-SCRIPT-015"
    authority_type:
      - "pass_fail_result"
      - "blocked_result"
      - "cli_contract"
      - "lifecycle_gate"
      - "approval_boundary_gate"
    authority_confidence: "high"
    evidence_paths:
      - "docs/APPLY-COMMAND-INTEGRATION.md"
      - "docs/SCRIPT-LIFECYCLE-POLICY.md"
      - "reports/m16-completion-review.md"
    affects_result_semantics: true
    affects_exit_codes: true
    affects_json_output: false
    affects_cli_behavior: true
    affects_error_format: true
    affects_lifecycle_mutation: true
    affects_approval_boundary: true
    optimization_review_allowed: true
    block_reason: ""
  - item_id: "M89-AUTH-014"
    script_path: "scripts/check-apply-preconditions.py"
    source_inventory_item: "M89-SCRIPT-016"
    authority_type:
      - "pass_fail_result"
      - "blocked_result"
      - "cli_contract"
      - "lifecycle_gate"
      - "approval_boundary_gate"
    authority_confidence: "high"
    evidence_paths:
      - "docs/APPLY-PRECONDITIONS.md"
      - "docs/APPLY-COMMAND-INTEGRATION.md"
      - "scripts/apply-transition.py"
    affects_result_semantics: true
    affects_exit_codes: true
    affects_json_output: true
    affects_cli_behavior: true
    affects_error_format: true
    affects_lifecycle_mutation: true
    affects_approval_boundary: true
    optimization_review_allowed: true
    block_reason: ""
  - item_id: "M89-AUTH-015"
    script_path: "scripts/check-transition.py"
    source_inventory_item: "M89-SCRIPT-017"
    authority_type:
      - "pass_fail_result"
      - "blocked_result"
      - "cli_contract"
      - "lifecycle_gate"
    authority_confidence: "high"
    evidence_paths:
      - "docs/TASK-TRANSITION-RULES.md"
      - "docs/SCRIPT-LIFECYCLE-POLICY.md"
      - "reports/task-state-machine-smoke.md"
    affects_result_semantics: true
    affects_exit_codes: true
    affects_json_output: false
    affects_cli_behavior: true
    affects_error_format: true
    affects_lifecycle_mutation: true
    affects_approval_boundary: false
    optimization_review_allowed: true
    block_reason: ""
  - item_id: "M89-AUTH-016"
    script_path: "scripts/agentos-enforce.py"
    source_inventory_item: "M89-SCRIPT-023"
    authority_type:
      - "pass_fail_result"
      - "blocked_result"
      - "cli_contract"
      - "ci_validation"
    authority_confidence: "high"
    evidence_paths:
      - ".github/workflows/dev-only/m27-enforcement.yml"
      - "docs/M27-RUNTIME-BOUNDARY-CONTRACT.md"
      - "docs/SCRIPT-OUTPUT-CONTRACT.md"
    affects_result_semantics: true
    affects_exit_codes: true
    affects_json_output: true
    affects_cli_behavior: true
    affects_error_format: true
    affects_lifecycle_mutation: false
    affects_approval_boundary: false
    optimization_review_allowed: false
    block_reason: "UNKNOWN_CLASSIFICATION_BLOCKED"
  - item_id: "M89-AUTH-017"
    script_path: "scripts/agentos-command-guard.py"
    source_inventory_item: "M89-SCRIPT-024"
    authority_type:
      - "blocked_result"
      - "cli_contract"
      - "ci_validation"
    authority_confidence: "high"
    evidence_paths:
      - ".github/workflows/dev-only/m27-enforcement.yml"
      - "docs/M27-COMMAND-ENFORCEMENT-RUNTIME.md"
      - "docs/SCRIPT-DANGEROUS-OPERATIONS-AUDIT.md"
    affects_result_semantics: true
    affects_exit_codes: true
    affects_json_output: true
    affects_cli_behavior: true
    affects_error_format: true
    affects_lifecycle_mutation: false
    affects_approval_boundary: false
    optimization_review_allowed: false
    block_reason: "UNKNOWN_CLASSIFICATION_BLOCKED"
  - item_id: "M89-AUTH-018"
    script_path: "scripts/agentos-human-gate.py"
    source_inventory_item: "M89-SCRIPT-025"
    authority_type:
      - "blocked_result"
      - "approval_boundary_gate"
      - "ci_validation"
      - "cli_contract"
    authority_confidence: "high"
    evidence_paths:
      - ".github/workflows/dev-only/m27-enforcement.yml"
      - "docs/M27-UNIFIED-ENFORCEMENT-CLI.md"
      - "docs/M27-RUNTIME-BOUNDARY-CONTRACT.md"
    affects_result_semantics: true
    affects_exit_codes: true
    affects_json_output: true
    affects_cli_behavior: true
    affects_error_format: true
    affects_lifecycle_mutation: false
    affects_approval_boundary: true
    optimization_review_allowed: false
    block_reason: "UNKNOWN_CLASSIFICATION_BLOCKED"
  - item_id: "M89-AUTH-019"
    script_path: "scripts/agentos-violation-enforce.py"
    source_inventory_item: "M89-SCRIPT-026"
    authority_type:
      - "blocked_result"
      - "ci_validation"
      - "cli_contract"
    authority_confidence: "high"
    evidence_paths:
      - ".github/workflows/dev-only/m27-enforcement.yml"
      - "docs/M27-RUNTIME-BOUNDARY-CONTRACT.md"
      - "docs/SCRIPT-LIFECYCLE-POLICY.md"
    affects_result_semantics: true
    affects_exit_codes: true
    affects_json_output: true
    affects_cli_behavior: true
    affects_error_format: true
    affects_lifecycle_mutation: false
    affects_approval_boundary: false
    optimization_review_allowed: false
    block_reason: "UNKNOWN_CLASSIFICATION_BLOCKED"
  - item_id: "M89-AUTH-020"
    script_path: "scripts/agentos-retry-enforce.py"
    source_inventory_item: "M89-SCRIPT-027"
    authority_type:
      - "blocked_result"
      - "ci_validation"
      - "cli_contract"
    authority_confidence: "high"
    evidence_paths:
      - ".github/workflows/dev-only/m27-enforcement.yml"
      - "docs/M27-RUNTIME-BOUNDARY-CONTRACT.md"
      - "docs/SCRIPT-OUTPUT-CONTRACT.md"
    affects_result_semantics: true
    affects_exit_codes: true
    affects_json_output: true
    affects_cli_behavior: true
    affects_error_format: true
    affects_lifecycle_mutation: false
    affects_approval_boundary: false
    optimization_review_allowed: false
    block_reason: "UNKNOWN_CLASSIFICATION_BLOCKED"
  - item_id: "M89-AUTH-021"
    script_path: "scripts/check-m74-dispatcher-regression.py"
    source_inventory_item: "M89-SCRIPT-028"
    authority_type:
      - "pass_fail_result"
      - "exit_code_contract"
      - "unknown"
    authority_confidence: "low"
    evidence_paths:
      - "reports/m74-regression-evidence-report.md"
      - "reports/m86-cleanup-candidate-register.md"
    affects_result_semantics: true
    affects_exit_codes: true
    affects_json_output: unknown
    affects_cli_behavior: unknown
    affects_error_format: unknown
    affects_lifecycle_mutation: false
    affects_approval_boundary: false
    optimization_review_allowed: false
    block_reason: "SCRIPT_SPEC_CONTRACT_UNKNOWN_BLOCKED"

forbidden_weakening_confirmed:
  pass_is_not_approval_preserved: true
  evidence_is_not_approval_preserved: true
  ci_pass_is_not_approval_preserved: true
  unknown_is_not_ok_preserved: true
  not_run_is_not_pass_preserved: true
  fail_closed_semantics_preserved: true

mapping_rules:
  inventory_is_not_authorization: true
  authority_map_is_not_approval: true
  unknown_authority_blocks_optimization_review: true
  validation_authority_scripts_require_documented_behavior_sources: true
  no_script_change_allowed_in_m89_1: true

FINAL_STATUS: M89_1_VALIDATION_AUTHORITY_MAP_COMPLETE_WITH_WARNINGS

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

# M89.1 Validation Authority Map

Проверка показала 121 скрипт, которые прямо влияют на результат проверок или на договор о выходном статусе, и 81 скрипт, которые в эту категорию не попадают. Неопределенных по самому факту “влияет или не влияет на authority” сейчас нет: риск сосредоточен не в классификации authority, а в том, что часть диспетчеров и enforcement-скриптов имеет не до конца доказанную поверхность записи и побочных действий.

Главные authority-скрипты с хорошо читаемыми письменными опорами: `agentos-validate.py`, `run-all.sh`, `health-check.sh`, `audit-agentos.py`, а также проверяющие скрипты для readiness, authorization, controlled session и result verification. Заблокированы для будущего optimization review в первую очередь `agentos-enforce.py`, `agentos-command-guard.py`, `agentos-human-gate.py`, `agentos-violation-enforce.py`, `agentos-retry-enforce.py` и `check-m74-dispatcher-regression.py`.

Эта карта не разрешает менять скрипты. Она только показывает, какие из них влияют на итог проверки, на отказ/блокировку, на человеческое подтверждение и на CI, то есть на автоматические проверки в GitHub Actions.
