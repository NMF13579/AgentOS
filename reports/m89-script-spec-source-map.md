---
task_id: M89.1
task_name: Script Spec Source Map
mode: read_only_spec_mapping

script_spec_source_summary:
  scripts_with_documented_behavior_count: 201
  scripts_without_documented_behavior_count: 1
  scripts_with_unknown_documented_behavior_count: 0
  validation_authority_scripts_missing_contract_count: 1

script_spec_source_items:
  - item_id: "M89-SPECMAP-001"
    script_path: "scripts/agentos-validate.py"
    source_inventory_item: "M89-SCRIPT-001"
    validation_authority: true
    documented_behavior_sources:
      - "scripts/VALIDATORS.md"
      - "README.md"
      - "docs/SCRIPT-EXIT-CODE-STANDARD.md"
      - ".github/workflows/agentos-validate.yml"
    documented_behavior_known: true
    spec_contract_available: true
    cli_contract_documented: true
    json_contract_documented: true
    exit_code_contract_documented: true
    error_format_documented: true
    lifecycle_contract_documented: false
    approval_boundary_documented: true
    source_of_truth_docs:
      - "scripts/VALIDATORS.md"
    supporting_docs:
      - "README.md"
      - "docs/CI-EVIDENCE-ARTIFACTS.md"
      - ".github/workflows/agentos-validate.yml"
    reports_as_evidence_only:
      - "reports/m39-public-mvp-readiness-evidence-report.md"
    missing_contract_fields: []
    optimization_review_allowed: false
    block_reason: "UNKNOWN_CLASSIFICATION_BLOCKED"
  - item_id: "M89-SPECMAP-002"
    script_path: "scripts/run-all.sh"
    source_inventory_item: "M89-SCRIPT-002"
    validation_authority: true
    documented_behavior_sources:
      - "scripts/VALIDATORS.md"
      - "docs/installation.md"
      - "docs/quickstart.md"
    documented_behavior_known: true
    spec_contract_available: true
    cli_contract_documented: true
    json_contract_documented: false
    exit_code_contract_documented: true
    error_format_documented: false
    lifecycle_contract_documented: false
    approval_boundary_documented: true
    source_of_truth_docs:
      - "scripts/VALIDATORS.md"
    supporting_docs:
      - "docs/installation.md"
      - "docs/quickstart.md"
    reports_as_evidence_only:
      - "reports/m36-external-usability-smoke-test.md"
    missing_contract_fields: []
    optimization_review_allowed: true
    block_reason: ""
  - item_id: "M89-SPECMAP-003"
    script_path: "scripts/health-check.sh"
    source_inventory_item: "M89-SCRIPT-003"
    validation_authority: true
    documented_behavior_sources:
      - "scripts/VALIDATORS.md"
      - "docs/SCRIPT-OUTPUT-CONTRACT.md"
      - ".github/workflows/dev-only/health.yml"
    documented_behavior_known: true
    spec_contract_available: true
    cli_contract_documented: true
    json_contract_documented: false
    exit_code_contract_documented: true
    error_format_documented: false
    lifecycle_contract_documented: false
    approval_boundary_documented: true
    source_of_truth_docs:
      - "scripts/VALIDATORS.md"
    supporting_docs:
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
      - ".github/workflows/dev-only/health.yml"
    reports_as_evidence_only: []
    missing_contract_fields: []
    optimization_review_allowed: true
    block_reason: ""
  - item_id: "M89-SPECMAP-004"
    script_path: "scripts/check-execution-readiness.py"
    source_inventory_item: "M89-SCRIPT-006"
    validation_authority: true
    documented_behavior_sources:
      - "docs/EXECUTION-VERIFICATION-SOURCE-OF-TRUTH.md"
      - "docs/TASK-EXECUTION-READINESS-CLI.md"
      - "schemas/task-execution-readiness-input.schema.json"
    documented_behavior_known: true
    spec_contract_available: true
    cli_contract_documented: true
    json_contract_documented: false
    exit_code_contract_documented: true
    error_format_documented: true
    lifecycle_contract_documented: false
    approval_boundary_documented: true
    source_of_truth_docs:
      - "docs/EXECUTION-VERIFICATION-SOURCE-OF-TRUTH.md"
      - "docs/TASK-EXECUTION-READINESS-CLI.md"
    supporting_docs:
      - "schemas/task-execution-readiness-input.schema.json"
    reports_as_evidence_only:
      - "reports/m56-execution-readiness-integration.md"
    missing_contract_fields: []
    optimization_review_allowed: true
    block_reason: ""
  - item_id: "M89-SPECMAP-005"
    script_path: "scripts/check-execution-authorization.py"
    source_inventory_item: "M89-SCRIPT-007"
    validation_authority: true
    documented_behavior_sources:
      - "docs/EXECUTION-VERIFICATION-SOURCE-OF-TRUTH.md"
      - "docs/TASK-EXECUTION-AUTHORIZATION-CLI.md"
      - "schemas/task-execution-authorization-preconditions.schema.json"
    documented_behavior_known: true
    spec_contract_available: true
    cli_contract_documented: true
    json_contract_documented: false
    exit_code_contract_documented: true
    error_format_documented: true
    lifecycle_contract_documented: false
    approval_boundary_documented: true
    source_of_truth_docs:
      - "docs/EXECUTION-VERIFICATION-SOURCE-OF-TRUTH.md"
      - "docs/TASK-EXECUTION-AUTHORIZATION-CLI.md"
    supporting_docs:
      - "schemas/task-execution-authorization-preconditions.schema.json"
    reports_as_evidence_only:
      - "reports/m57-execution-authorization-evidence-report.md"
    missing_contract_fields: []
    optimization_review_allowed: true
    block_reason: ""
  - item_id: "M89-SPECMAP-006"
    script_path: "scripts/check-controlled-execution-session.py"
    source_inventory_item: "M89-SCRIPT-008"
    validation_authority: true
    documented_behavior_sources:
      - "docs/EXECUTION-VERIFICATION-SOURCE-OF-TRUTH.md"
      - "docs/CONTROLLED-EXECUTION-SESSION-FIXTURE-RUNNER.md"
      - "schemas/execution-session-boundary.schema.json"
    documented_behavior_known: true
    spec_contract_available: true
    cli_contract_documented: true
    json_contract_documented: false
    exit_code_contract_documented: true
    error_format_documented: true
    lifecycle_contract_documented: false
    approval_boundary_documented: true
    source_of_truth_docs:
      - "docs/EXECUTION-VERIFICATION-SOURCE-OF-TRUTH.md"
    supporting_docs:
      - "docs/CONTROLLED-EXECUTION-SESSION-FIXTURE-RUNNER.md"
      - "schemas/execution-session-boundary.schema.json"
    reports_as_evidence_only:
      - "reports/m58-controlled-execution-session-evidence-report.md"
    missing_contract_fields: []
    optimization_review_allowed: true
    block_reason: ""
  - item_id: "M89-SPECMAP-007"
    script_path: "scripts/check-execution-result-verification.py"
    source_inventory_item: "M89-SCRIPT-009"
    validation_authority: true
    documented_behavior_sources:
      - "docs/EXECUTION-VERIFICATION-SOURCE-OF-TRUTH.md"
      - "docs/EXECUTION-RESULT-VERIFICATION-ARCHITECTURE.md"
      - "schemas/execution-result-verification-result-output.schema.json"
    documented_behavior_known: true
    spec_contract_available: true
    cli_contract_documented: true
    json_contract_documented: true
    exit_code_contract_documented: true
    error_format_documented: true
    lifecycle_contract_documented: false
    approval_boundary_documented: false
    source_of_truth_docs:
      - "docs/EXECUTION-VERIFICATION-SOURCE-OF-TRUTH.md"
    supporting_docs:
      - "docs/EXECUTION-RESULT-VERIFICATION-ARCHITECTURE.md"
      - "schemas/execution-result-verification-result-output.schema.json"
    reports_as_evidence_only:
      - "reports/m59-execution-result-verification-evidence-report.md"
    missing_contract_fields: []
    optimization_review_allowed: true
    block_reason: ""
  - item_id: "M89-SPECMAP-008"
    script_path: "scripts/check-false-pass-resistance.py"
    source_inventory_item: "M89-SCRIPT-010"
    validation_authority: true
    documented_behavior_sources:
      - "docs/FALSE-PASS-RESISTANCE-CHECKER.md"
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
    documented_behavior_known: true
    spec_contract_available: true
    cli_contract_documented: true
    json_contract_documented: false
    exit_code_contract_documented: true
    error_format_documented: false
    lifecycle_contract_documented: false
    approval_boundary_documented: false
    source_of_truth_docs:
      - "docs/FALSE-PASS-RESISTANCE-CHECKER.md"
    supporting_docs:
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
    reports_as_evidence_only:
      - "reports/m67-false-pass-evidence-report.md"
    missing_contract_fields: []
    optimization_review_allowed: true
    block_reason: ""
  - item_id: "M89-SPECMAP-009"
    script_path: "scripts/validate-status-semantics.py"
    source_inventory_item: "M89-SCRIPT-012"
    validation_authority: true
    documented_behavior_sources:
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
      - "reports/m40-fixup-help-semantics-report.md"
    documented_behavior_known: true
    spec_contract_available: true
    cli_contract_documented: true
    json_contract_documented: false
    exit_code_contract_documented: true
    error_format_documented: false
    lifecycle_contract_documented: false
    approval_boundary_documented: false
    source_of_truth_docs:
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
    supporting_docs: []
    reports_as_evidence_only:
      - "reports/m40-fixup-help-semantics-report.md"
    missing_contract_fields: []
    optimization_review_allowed: true
    block_reason: ""
  - item_id: "M89-SPECMAP-010"
    script_path: "scripts/validate-human-approval.py"
    source_inventory_item: "M89-SCRIPT-013"
    validation_authority: true
    documented_behavior_sources:
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
      - "tests/fixtures/negative/activation/missing-approval-marker/approvals/approval.md"
    documented_behavior_known: true
    spec_contract_available: true
    cli_contract_documented: true
    json_contract_documented: false
    exit_code_contract_documented: true
    error_format_documented: true
    lifecycle_contract_documented: false
    approval_boundary_documented: true
    source_of_truth_docs:
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
    supporting_docs: []
    reports_as_evidence_only:
      - "reports/m57-execution-authorization-evidence-report.md"
    missing_contract_fields: []
    optimization_review_allowed: true
    block_reason: ""
  - item_id: "M89-SPECMAP-011"
    script_path: "scripts/validate-approval-marker.py"
    source_inventory_item: "M89-SCRIPT-014"
    validation_authority: true
    documented_behavior_sources:
      - "docs/EXECUTION-READINESS.md"
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
    documented_behavior_known: true
    spec_contract_available: true
    cli_contract_documented: true
    json_contract_documented: false
    exit_code_contract_documented: true
    error_format_documented: true
    lifecycle_contract_documented: false
    approval_boundary_documented: true
    source_of_truth_docs:
      - "docs/EXECUTION-READINESS.md"
    supporting_docs:
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
    reports_as_evidence_only: []
    missing_contract_fields: []
    optimization_review_allowed: true
    block_reason: ""
  - item_id: "M89-SPECMAP-012"
    script_path: "scripts/validate-lifecycle-apply.py"
    source_inventory_item: "M89-SCRIPT-015"
    validation_authority: true
    documented_behavior_sources:
      - "docs/APPLY-COMMAND-INTEGRATION.md"
      - "docs/SCRIPT-LIFECYCLE-POLICY.md"
    documented_behavior_known: true
    spec_contract_available: true
    cli_contract_documented: true
    json_contract_documented: false
    exit_code_contract_documented: true
    error_format_documented: true
    lifecycle_contract_documented: true
    approval_boundary_documented: true
    source_of_truth_docs:
      - "docs/APPLY-COMMAND-INTEGRATION.md"
      - "docs/SCRIPT-LIFECYCLE-POLICY.md"
    supporting_docs: []
    reports_as_evidence_only:
      - "reports/m16-completion-review.md"
    missing_contract_fields: []
    optimization_review_allowed: true
    block_reason: ""
  - item_id: "M89-SPECMAP-013"
    script_path: "scripts/check-apply-preconditions.py"
    source_inventory_item: "M89-SCRIPT-016"
    validation_authority: true
    documented_behavior_sources:
      - "docs/APPLY-PRECONDITIONS.md"
      - "docs/APPLY-COMMAND-INTEGRATION.md"
    documented_behavior_known: true
    spec_contract_available: true
    cli_contract_documented: true
    json_contract_documented: true
    exit_code_contract_documented: true
    error_format_documented: true
    lifecycle_contract_documented: true
    approval_boundary_documented: true
    source_of_truth_docs:
      - "docs/APPLY-PRECONDITIONS.md"
      - "docs/APPLY-COMMAND-INTEGRATION.md"
    supporting_docs: []
    reports_as_evidence_only:
      - "reports/m15-completion-review.md"
    missing_contract_fields: []
    optimization_review_allowed: true
    block_reason: ""
  - item_id: "M89-SPECMAP-014"
    script_path: "scripts/check-transition.py"
    source_inventory_item: "M89-SCRIPT-017"
    validation_authority: true
    documented_behavior_sources:
      - "docs/TASK-TRANSITION-RULES.md"
      - "docs/SCRIPT-LIFECYCLE-POLICY.md"
    documented_behavior_known: true
    spec_contract_available: true
    cli_contract_documented: true
    json_contract_documented: false
    exit_code_contract_documented: true
    error_format_documented: true
    lifecycle_contract_documented: true
    approval_boundary_documented: false
    source_of_truth_docs:
      - "docs/TASK-TRANSITION-RULES.md"
    supporting_docs:
      - "docs/SCRIPT-LIFECYCLE-POLICY.md"
    reports_as_evidence_only:
      - "reports/task-state-machine-smoke.md"
    missing_contract_fields: []
    optimization_review_allowed: true
    block_reason: ""
  - item_id: "M89-SPECMAP-015"
    script_path: "scripts/agentos-enforce.py"
    source_inventory_item: "M89-SCRIPT-023"
    validation_authority: true
    documented_behavior_sources:
      - "docs/M27-RUNTIME-BOUNDARY-CONTRACT.md"
      - "docs/SCRIPT-OUTPUT-CONTRACT.md"
      - ".github/workflows/dev-only/m27-enforcement.yml"
    documented_behavior_known: true
    spec_contract_available: true
    cli_contract_documented: true
    json_contract_documented: true
    exit_code_contract_documented: true
    error_format_documented: true
    lifecycle_contract_documented: false
    approval_boundary_documented: false
    source_of_truth_docs:
      - "docs/M27-RUNTIME-BOUNDARY-CONTRACT.md"
    supporting_docs:
      - "docs/SCRIPT-OUTPUT-CONTRACT.md"
      - ".github/workflows/dev-only/m27-enforcement.yml"
    reports_as_evidence_only:
      - "reports/m27-enforcement-evidence-report.md"
    missing_contract_fields: []
    optimization_review_allowed: false
    block_reason: "UNKNOWN_CLASSIFICATION_BLOCKED"
  - item_id: "M89-SPECMAP-016"
    script_path: "scripts/agentos-human-gate.py"
    source_inventory_item: "M89-SCRIPT-025"
    validation_authority: true
    documented_behavior_sources:
      - "docs/M27-UNIFIED-ENFORCEMENT-CLI.md"
      - "docs/M27-RUNTIME-BOUNDARY-CONTRACT.md"
      - ".github/workflows/dev-only/m27-enforcement.yml"
    documented_behavior_known: true
    spec_contract_available: true
    cli_contract_documented: true
    json_contract_documented: true
    exit_code_contract_documented: true
    error_format_documented: true
    lifecycle_contract_documented: false
    approval_boundary_documented: true
    source_of_truth_docs:
      - "docs/M27-RUNTIME-BOUNDARY-CONTRACT.md"
    supporting_docs:
      - "docs/M27-UNIFIED-ENFORCEMENT-CLI.md"
      - ".github/workflows/dev-only/m27-enforcement.yml"
    reports_as_evidence_only:
      - "reports/m27-human-gate-runtime-review.md"
    missing_contract_fields: []
    optimization_review_allowed: false
    block_reason: "UNKNOWN_CLASSIFICATION_BLOCKED"
  - item_id: "M89-SPECMAP-017"
    script_path: "scripts/check-m74-dispatcher-regression.py"
    source_inventory_item: "M89-SCRIPT-028"
    validation_authority: true
    documented_behavior_sources: []
    documented_behavior_known: false
    spec_contract_available: false
    cli_contract_documented: false
    json_contract_documented: false
    exit_code_contract_documented: false
    error_format_documented: false
    lifecycle_contract_documented: false
    approval_boundary_documented: false
    source_of_truth_docs: []
    supporting_docs: []
    reports_as_evidence_only:
      - "reports/m74-regression-evidence-report.md"
    missing_contract_fields:
      - "cli_contract"
      - "json_contract"
      - "exit_code_contract"
      - "error_format"
    optimization_review_allowed: false
    block_reason: "SCRIPT_SPEC_CONTRACT_UNKNOWN_BLOCKED"

unknown_resolution_register:
  unknown_items_present: true
  unknown_items:
    - path: "scripts/agentos-validate.py"
      unknown_field: "writes_files"
      attempted_resolution: "read_docs"
      resolved: false
      final_classification: "UNKNOWN_BLOCKED"
      block_reason: "WRITE_SURFACE_NOT_PROVEN_SAFE_BY_READ_ONLY_SCAN"
    - path: "scripts/agentos-enforce.py"
      unknown_field: "writes_files"
      attempted_resolution: "read_docs"
      resolved: false
      final_classification: "UNKNOWN_BLOCKED"
      block_reason: "WRITE_SURFACE_NOT_PROVEN_SAFE_BY_READ_ONLY_SCAN"
    - path: "scripts/agentos-command-guard.py"
      unknown_field: "writes_files"
      attempted_resolution: "read_docs"
      resolved: false
      final_classification: "UNKNOWN_BLOCKED"
      block_reason: "WRITE_SURFACE_NOT_PROVEN_SAFE_BY_READ_ONLY_SCAN"
    - path: "scripts/agentos-human-gate.py"
      unknown_field: "writes_files"
      attempted_resolution: "read_docs"
      resolved: false
      final_classification: "UNKNOWN_BLOCKED"
      block_reason: "WRITE_SURFACE_NOT_PROVEN_SAFE_BY_READ_ONLY_SCAN"
    - path: "scripts/check-m74-dispatcher-regression.py"
      unknown_field: "documented_behavior_sources"
      attempted_resolution: "read_docs"
      resolved: false
      final_classification: "UNKNOWN_BLOCKED"
      block_reason: "SCRIPT_SPEC_CONTRACT_UNKNOWN_BLOCKED"

spec_source_rules:
  markdown_is_source_of_truth: true
  reports_are_evidence_not_approval: true
  generated_indexes_are_not_source_of_truth: true
  validation_authority_script_without_documented_behavior_blocks_optimization_review: true
  script_spec_map_does_not_authorize_changes: true
  m89_must_not_fix_docs: true
  missing_docs_may_be_handed_to_m90_later: true

if_validation_authority_true_and_documented_behavior_unknown:
  optimization_review_allowed: false
  block_reason: SCRIPT_SPEC_CONTRACT_UNKNOWN_BLOCKED

if_markdown_clarification_needed:
  m89_must_not_modify_markdown: true
  possible_m90_handoff_item: true
  candidate_creation_deferred_to_m89_2: true

FINAL_STATUS: M89_1_SCRIPT_SPEC_SOURCE_MAP_COMPLETE_WITH_WARNINGS

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

# M89.1 Script Spec Source Map

По итогам read-only сопоставления у 201 script-like файлов нашлись письменные источники поведения, а у 1 файла нет. Этот файл — `scripts/check-m74-dispatcher-regression.py`; он влияет на проверку, но по нему не найден отдельный письменный контракт поведения, поэтому он должен оставаться заблокированным для optimization review.

Важно: письменное описание поведения не равно разрешению на изменение. Документы и workflow здесь используются как источник смысла, а отчеты — только как доказательство того, что такой смысл раньше уже применялся. Если для authority-скрипта письменное описание неполное, M89.1 не исправляет это и не дописывает документацию, а только фиксирует пробел для следующего этапа с предупреждениями.
