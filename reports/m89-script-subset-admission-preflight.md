---
task_id: M89.3
task_name: Human-Selected Script Subset Admission & Preflight
mode: human_selected_subset_admission_preflight

preconditions:
  m89_2_candidate_register_exists: true
  m89_2_status: M89_2_CANDIDATE_REGISTER_COMPLETE_WITH_WARNINGS
  m89_2_allows_m89_3: true_with_warnings
  m89_2_no_safe_candidates: false

human_selection_rules:
  selected_by_human_required: true
  agent_generated_selection_forbidden: true
  selected_candidates_count_must_equal: 1
  human_reason_required: true
  candidate_id_must_exist_in_m89_2: true
  selected_path_must_match_candidate_register: true

admission_requires:
  selected_candidate_exists_in_m89_2: true
  selected_script_exists: true
  selected_candidate_count_equals_1: true
  exact_path: true
  broad_globs_used: false
  selected_candidate_allowed_for_execution_consideration: true
  risk_class_allowed:
    - LOW
    - MEDIUM
  optimization_risk_tier_allowed:
    - TRIVIAL_SAFE
    - CONTROLLED_CHANGE
  validation_authority_impact_not_unknown: true
  pass_semantics_impact_not_unknown: true
  unknown_semantics_impact_not_unknown: true
  not_run_semantics_impact_not_unknown: true
  lifecycle_impact_not_unknown: true
  approval_boundary_impact_not_unknown: true
  doc_contract_impact_not_unknown: true
  related_spec_contracts_available: true
  rollback_plan_exists: true
  validation_commands_available: true
  spec_consistency_check_available: true
  git_diff_clean_before_action: true

block_if:
  m89_2_missing: true
  m89_2_blocked: true
  m89_2_no_safe_candidates: true
  no_human_selected_subset: true
  agent_selected_candidate: true
  selected_candidate_count_not_equal_1: true
  selected_candidate_not_in_m89_2: true
  selected_candidate_previously_blocked: true
  selected_script_missing: true
  broad_glob_used: true
  exact_path_missing: true
  risk_class_HIGH: true
  risk_class_UNKNOWN_BLOCKED: true
  optimization_risk_tier_HIGH_RISK: true
  optimization_risk_tier_UNKNOWN_BLOCKED: true
  validation_authority_impact_unknown: true
  pass_semantics_impact_unknown: true
  unknown_semantics_impact_unknown: true
  not_run_semantics_impact_unknown: true
  lifecycle_impact_unknown: true
  approval_boundary_impact_unknown: true
  doc_contract_impact_unknown: true
  related_spec_contracts_missing: true
  rollback_missing: true
  validation_commands_missing: true
  spec_consistency_check_missing: true
  git_diff_not_clean_before_action: true
  m89_4_artifacts_already_exist_unexpectedly: true
  m90_artifacts_exist_prematurely: true
  m91_artifacts_exist_prematurely: true

human_selected_script_subset:
  selected_by_human: true
  agent_generated: false
  selected_candidates_count: 1
  selected_candidates:
    - candidate_id: "M89-SCRIPT-CAND-003"
      path: "scripts/validate-architecture.sh"
      selected_optimization_type: "simplify_wrapper"
      selected_risk_tier: "CONTROLLED_CHANGE"
      selected_risk_class: "MEDIUM"
      human_reason: "хочу начать с архитектурной проверки, она важна для качества, но относительно безопасна для первого контролируемого изменения"
  selection_scope:
    max_candidates: 1
    exact_paths_only: true
    broad_globs_allowed: false
    broad_globs_used: false

candidate_admission:
  selected_candidate_exists_in_m89_2: true
  selected_script_exists: true
  selected_path_matches_candidate_register: true
  selected_candidate_allowed_for_execution_consideration: true
  selected_candidate_block_reason_from_m89_2: "none"
  selected_candidate_not_previously_blocked: true

risk_admission:
  risk_class_allowed: true
  selected_risk_class: "MEDIUM"
  optimization_risk_tier_allowed: true
  selected_optimization_risk_tier: "CONTROLLED_CHANGE"
  validation_authority_impact_not_unknown: true
  pass_semantics_impact_not_unknown: true
  unknown_semantics_impact_not_unknown: true
  not_run_semantics_impact_not_unknown: true
  lifecycle_impact_not_unknown: true
  approval_boundary_impact_not_unknown: true
  doc_contract_impact_not_unknown: true
  ci_or_workflow_impact_not_unknown: true

preflight_checks:
  exact_path: true
  broad_globs_used: false
  related_spec_contracts_available: true
  rollback_plan_exists: true
  validation_commands_available: true
  spec_consistency_check_available: true
  git_diff_clean_before_action: true
  no_unexpected_m89_4_artifacts_exist: true
  no_m90_artifacts_created: true
  no_m91_artifacts_created: true

rollback_plan:
  selected_script_path: "scripts/validate-architecture.sh"
  rollback_method: "git checkout -- scripts/validate-architecture.sh"
  rollback_command_documented: true
  rollback_scope_exact_path_only: true
  rollback_touches_docs: false
  rollback_touches_schemas: false
  rollback_touches_workflows: false
  rollback_plan_safe: true

forbidden_rollback_methods:
  - git reset --hard
  - git clean -fd
  - rm -rf
  - broad directory replacement

validation_plan:
  commands_available: true
  commands:
    - command: "bash scripts/validate-architecture.sh"
      purpose: "targeted_check"
      safe_to_run: true
      read_only: true
    - command: "python3 scripts/agentos-validate.py all"
      purpose: "repo_validation"
      safe_to_run: true
      read_only: true
    - command: "python3 scripts/audit-agentos.py"
      purpose: "regression"
      safe_to_run: true
      read_only: true
    - command: "bash scripts/health-check.sh"
      purpose: "script_spec_consistency"
      safe_to_run: true
      read_only: true
  validation_plan_blocks_if_missing: true

script_spec_consistency_preflight:
  related_spec_contracts_available: true
  cli_contract_documented_or_not_applicable: true
  json_contract_documented_or_not_applicable: true
  exit_code_contract_documented_or_not_applicable: true
  error_format_documented_or_not_applicable: true
  contract_behavior_change_expected: false
  contract_behavior_change_allowed_in_m89_4: false
  m90_handoff_possible_for_documentation_clarification_only: true

boundary:
  script_modified: false
  docs_modified: false
  schemas_modified: false
  workflows_modified: false
  approval_created: false
  lifecycle_mutation_created: false
  m89_4_started: false
  m90_started: false
  m91_started: false

blockers:
  - ""
warnings:
  - "M89.2 carried warnings into M89.3."
  - "The selected script is a legacy shell wrapper referenced by workflow and docs, so any later change must preserve wrapper semantics exactly."
  - "Selected candidate carries M89.2 warning context because authority/spec source items stayed summarized as unknown there, even though related contracts were found for preflight."

validation:
  git_status_short_run: true
  read_only_search_run: true
  read_only_search_examples:
    - "grep -n \"M89-SCRIPT-CAND-003\" reports/m89-script-optimization-candidate-register.md"
    - "rg -n \"scripts/validate-architecture.sh\" docs reports schemas .github scripts"
  canonical_validation_run: true
  validation_not_run: false
  validation_result_claimed_pass: false
  canonical_validation_command: "python3 scripts/audit-agentos.py"
  canonical_validation_result: "PASS_WITH_WARNINGS"

may_prepare_m89_4_controlled_script_execution: true_with_warnings

FINAL_STATUS: M89_3_PREFLIGHT_READY_WITH_WARNINGS
---

# M89.3 Human-Selected Script Subset Admission & Preflight

Выбранный кандидат подтвержден как человеческий выбор. Он существует в M89.2, использует точный путь `scripts/validate-architecture.sh`, не был ранее заблокирован и имеет допустимый риск: `CONTROLLED_CHANGE` / `MEDIUM`.

По содержанию сам кандидат сейчас проходит admission-проверку: путь точный, broad glob не использовался, rollback можно задокументировать как `git checkout -- scripts/validate-architecture.sh`, а набор проверок для M89.4 можно заранее перечислить.

На повторной проверке блокировка по рабочему дереву снялась: `git diff clean before action` теперь выполняется. Поэтому M89.4 можно готовить, но только с предупреждениями. Эти предупреждения связаны не с текущим состоянием git, а с тем, что выбранный файл остается legacy wrapper, и любое следующее изменение должно строго сохранить обертку, договор по выходному коду и связь с workflow.

M89.3 does not authorize script optimization by itself.
M89.3 does not approve the selected candidate.
M89.3 does not simulate human selection.
M89.3 does not start M89.4.
M89.3 does not modify scripts.
M89.3 does not modify Markdown.
Human-selected subset admission is a preflight gate, not approval.
Physical script optimization remains limited to M89.4.
PASS remains separate from approval.
Evidence remains separate from approval.
