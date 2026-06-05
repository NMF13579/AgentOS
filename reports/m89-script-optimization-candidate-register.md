---
task_id: M89.2
task_name: Script Optimization Candidate Register
mode: read_only_candidate_register

preconditions:
  m89_1_scripts_inventory_exists: true
  m89_1_validation_authority_map_exists: true
  m89_1_script_spec_source_map_exists: true
  m89_1_allows_m89_2: true_with_warnings

candidate_register_scope:
  source_inventory_report: reports/m89-scripts-inventory.md
  source_authority_report: reports/m89-validation-authority-map.md
  source_spec_map_report: reports/m89-script-spec-source-map.md
  scripts_examined_count: 202
  candidates_created_count: 4
  candidates_allowed_for_execution_consideration_count: 4
  candidates_blocked_count: 7
  unknown_blocked_count: 5
  high_risk_blocked_count: 2
  no_safe_candidates_found: false

candidate_eligibility_requires:
  exact_script_path: true
  script_exists: true
  source_inventory_item_exists: true
  validation_authority_impact_not_unknown: true
  pass_semantics_impact_not_unknown: true
  unknown_semantics_impact_not_unknown: true
  not_run_semantics_impact_not_unknown: true
  lifecycle_impact_not_unknown: true
  approval_boundary_impact_not_unknown: true
  doc_contract_impact_not_unknown: true
  related_spec_contracts_available_or_non_authority_script: true
  risk_class_not_high: true
  risk_class_not_unknown_blocked: true
  optimization_risk_tier_not_high_risk: true
  optimization_risk_tier_not_unknown_blocked: true
  rollback_required: true
  human_selection_required: true

unknown_impact_rule:
  allowed_for_m89_execution_consideration: false
  optimization_risk_tier: UNKNOWN_BLOCKED
  risk_class: UNKNOWN_BLOCKED

doc_contract_unknown_rule:
  allowed_for_m89_execution_consideration: false
  block_reason: DOC_CONTRACT_IMPACT_UNKNOWN

validation_authority_contract_unknown_rule:
  allowed_for_m89_execution_consideration: false
  block_reason: SCRIPT_SPEC_CONTRACT_UNKNOWN_BLOCKED

high_risk_rule:
  allowed_for_m89_execution_consideration: false
  optimization_risk_tier: HIGH_RISK
  block_reason: HIGH_RISK_REQUIRES_DEDICATED_LINE_OR_HUMAN_CHECKPOINT

optimization_type_rules:
  trivial_safe:
    allowed_only_if_all_impacts_none: true
  deduplicate_logic:
    allowed_only_if_behavior_preserved: true
  simplify_wrapper:
    allowed_only_if_cli_json_exit_code_contracts_preserved: true
  remove_dead_helper_inline:
    allowed_only_inside_selected_script_file: true
    deleting_helper_file_allowed: false
    deleting_script_file_allowed: false
  clarify_exit_code_handling:
    allowed_only_if_exit_code_contract_preserved: true
    changing_exit_code_semantics_allowed: false
  improve_error_reporting:
    allowed_only_if_error_format_contract_preserved_or_non_contract_clarification: true
  unknown:
    allowed_for_m89_execution_consideration: false

m90_handoff_boundary:
  markdown_update_may_be_required: true
  m89_must_not_modify_markdown: true
  m89_must_not_create_m90_artifacts: true
  m89_may_record_possible_m90_handoff_item: true
  contract_behavior_change_cannot_be_deferred_to_m90: true

allowed_m90_handoff_reasons:
  - documentation_clarification_needed
  - examples_alignment_needed
  - non_contract_error_text_clarification
  - doc_contract_alignment_needed

forbidden_m90_handoff_reasons:
  - cli_contract_changed
  - json_contract_changed
  - exit_code_contract_changed
  - pass_blocked_unknown_not_run_semantics_changed
  - lifecycle_semantics_changed
  - approval_boundary_changed
  - validation_authority_changed

script_optimization_candidates:
  - candidate_id: "M89-SCRIPT-CAND-001"
    path: "scripts/run-all.sh"
    source_inventory_item: "M89-SCRIPT-002"
    source_authority_item: "M89-AUTH-002"
    source_spec_map_item: "M89-SPECMAP-002"
    related_spec_contracts:
      - "scripts/VALIDATORS.md"
      - "docs/installation.md"
      - "docs/quickstart.md"
    optimization_type: "simplify_wrapper"
    optimization_risk_tier: "CONTROLLED_CHANGE"
    risk_class: "MEDIUM"
    validation_authority_impact: "direct"
    pass_semantics_impact: "direct"
    unknown_semantics_impact: "none"
    not_run_semantics_impact: "possible"
    lifecycle_impact: "none"
    approval_boundary_impact: "none"
    ci_or_workflow_impact: "direct"
    doc_contract_impact: "direct"
    markdown_update_may_be_required: false
    allowed_for_m89_execution_consideration: true
    human_selection_required: true
    rollback_required: true
    exact_path_required: true
    broad_globs_allowed: false
    block_reason: ""
  - candidate_id: "M89-SCRIPT-CAND-002"
    path: "scripts/health-check.sh"
    source_inventory_item: "M89-SCRIPT-003"
    source_authority_item: "M89-AUTH-003"
    source_spec_map_item: "M89-SPECMAP-003"
    related_spec_contracts:
      - "scripts/VALIDATORS.md"
      - "docs/SCRIPT-OUTPUT-CONTRACT.md"
      - ".github/workflows/dev-only/health.yml"
    optimization_type: "simplify_wrapper"
    optimization_risk_tier: "CONTROLLED_CHANGE"
    risk_class: "MEDIUM"
    validation_authority_impact: "direct"
    pass_semantics_impact: "direct"
    unknown_semantics_impact: "none"
    not_run_semantics_impact: "possible"
    lifecycle_impact: "none"
    approval_boundary_impact: "none"
    ci_or_workflow_impact: "direct"
    doc_contract_impact: "direct"
    markdown_update_may_be_required: false
    allowed_for_m89_execution_consideration: true
    human_selection_required: true
    rollback_required: true
    exact_path_required: true
    broad_globs_allowed: false
    block_reason: ""
  - candidate_id: "M89-SCRIPT-CAND-003"
    path: "scripts/validate-architecture.sh"
    source_inventory_item: "M89-SCRIPT-004"
    source_authority_item: "unknown"
    source_spec_map_item: "unknown"
    related_spec_contracts:
      - "scripts/VALIDATORS.md"
      - "docs/SCRIPT-OUTPUT-CONTRACT.md"
      - ".github/workflows/dev-only/modular-validators.yml"
    optimization_type: "simplify_wrapper"
    optimization_risk_tier: "CONTROLLED_CHANGE"
    risk_class: "MEDIUM"
    validation_authority_impact: "direct"
    pass_semantics_impact: "direct"
    unknown_semantics_impact: "none"
    not_run_semantics_impact: "possible"
    lifecycle_impact: "none"
    approval_boundary_impact: "none"
    ci_or_workflow_impact: "direct"
    doc_contract_impact: "direct"
    markdown_update_may_be_required: false
    allowed_for_m89_execution_consideration: true
    human_selection_required: true
    rollback_required: true
    exact_path_required: true
    broad_globs_allowed: false
    block_reason: ""
  - candidate_id: "M89-SCRIPT-CAND-004"
    path: "scripts/audit-agentos.py"
    source_inventory_item: "M89-SCRIPT-005"
    source_authority_item: "M89-AUTH-004"
    source_spec_map_item: "unknown"
    related_spec_contracts:
      - "llms.txt"
      - "README.md"
      - "docs/SAFETY-BOUNDARIES.md"
    optimization_type: "improve_error_reporting"
    optimization_risk_tier: "CONTROLLED_CHANGE"
    risk_class: "MEDIUM"
    validation_authority_impact: "possible"
    pass_semantics_impact: "none"
    unknown_semantics_impact: "none"
    not_run_semantics_impact: "none"
    lifecycle_impact: "none"
    approval_boundary_impact: "none"
    ci_or_workflow_impact: "none"
    doc_contract_impact: "possible"
    markdown_update_may_be_required: true
    allowed_for_m89_execution_consideration: true
    human_selection_required: true
    rollback_required: true
    exact_path_required: true
    broad_globs_allowed: false
    block_reason: ""

blocked_items:
  - path: "scripts/agentos-validate.py"
    source_inventory_item: "M89-SCRIPT-001"
    reason: "UNKNOWN_IMPACT"
    may_be_reconsidered_after: "dedicated_future_line"
  - path: "scripts/agentos.py"
    source_inventory_item: "M89-SCRIPT-020"
    reason: "HIGH_RISK"
    may_be_reconsidered_after: "dedicated_future_line"
  - path: "scripts/canonical-cleanup.sh"
    source_inventory_item: "M89-SCRIPT-045"
    reason: "HIGH_RISK"
    may_be_reconsidered_after: "never_without_human_checkpoint"
  - path: "scripts/check-m74-dispatcher-regression.py"
    source_inventory_item: "M89-SCRIPT-028"
    reason: "SCRIPT_SPEC_CONTRACT_UNKNOWN"
    may_be_reconsidered_after: "M90_docs_clarification"
  - path: "scripts/lib/path_utils.py"
    source_inventory_item: "M89-SCRIPT-116"
    reason: "DOC_CONTRACT_IMPACT_UNKNOWN"
    may_be_reconsidered_after: "M90_docs_clarification"
  - path: "scripts/renderers/plain_status_renderer.py"
    source_inventory_item: "M89-SCRIPT-121"
    reason: "DOC_CONTRACT_IMPACT_UNKNOWN"
    may_be_reconsidered_after: "M90_docs_clarification"
  - path: "scripts/renderers/rich_status_renderer.py"
    source_inventory_item: "M89-SCRIPT-122"
    reason: "DOC_CONTRACT_IMPACT_UNKNOWN"
    may_be_reconsidered_after: "M90_docs_clarification"

possible_m90_handoff_items:
  - source_script: "scripts/audit-agentos.py"
    related_doc: "docs/SAFETY-BOUNDARIES.md"
    reason: "non_contract_error_text_clarification"
    contract_behavior_changed: false
    m89_must_not_modify_markdown: true
    must_be_handled_in_m90_if_selected_later: true
  - source_script: "scripts/lib/path_utils.py"
    related_doc: "docs/SCRIPT-RESPONSIBILITY-MAP.md"
    reason: "documentation_clarification_needed"
    contract_behavior_changed: false
    m89_must_not_modify_markdown: true
    must_be_handled_in_m90_if_selected_later: true
  - source_script: "scripts/renderers/plain_status_renderer.py"
    related_doc: "docs/M31-RENDERER-ARCHITECTURE.md"
    reason: "doc_contract_alignment_needed"
    contract_behavior_changed: false
    m89_must_not_modify_markdown: true
    must_be_handled_in_m90_if_selected_later: true
  - source_script: "scripts/renderers/rich_status_renderer.py"
    related_doc: "docs/M31-RENDERER-ARCHITECTURE.md"
    reason: "doc_contract_alignment_needed"
    contract_behavior_changed: false
    m89_must_not_modify_markdown: true
    must_be_handled_in_m90_if_selected_later: true

no_action_rules:
  no_safe_candidates_is_not_failure_if_supported: true
  fake_candidate_creation_for_progress_forbidden: true
  no_action_requires_block_reasons: true
  no_action_requires_no_physical_change_confirmation: true
  no_action_allows_skipping_m89_3_m89_4_m89_5_physical_regression: true

no_action_path:
  no_safe_script_optimization_action: false
  reason: ""
  may_skip_m89_3: false
  may_skip_m89_4: false
  may_prepare_m89_6_completion_review: false
  recommended_final_status_if_no_action: none

boundary:
  script_change_authorized_in_m89_2: false
  candidate_register_is_not_approval: true
  human_selected_subset_required_before_execution: true
  m89_3_started: false
  m89_4_started: false
  m90_started: false
  m91_started: false

validation:
  git_status_short_run: true
  read_only_search_run: true
  read_only_search_examples:
    - "find scripts -type f | sort"
    - "rg -n \"scripts/lib/path_utils.py|scripts/renderers/plain_status_renderer.py|scripts/renderers/rich_status_renderer.py|scripts/agentos.py|scripts/canonical-cleanup.sh\" docs reports .github tests scripts"
  canonical_validation_run: true
  validation_not_run: false
  validation_result_claimed_pass: false
  canonical_validation_command: "python3 scripts/audit-agentos.py"
  canonical_validation_result: "PASS_WITH_WARNINGS"

may_prepare_m89_3_script_subset_admission_preflight: true_with_warnings
may_prepare_m89_6_completion_review_via_no_action_path: false

FINAL_STATUS: M89_2_CANDIDATE_REGISTER_COMPLETE_WITH_WARNINGS
---

# M89.2 Script Optimization Candidate Register

Реестр кандидатов создан по read-only данным из M89.1. Безопасные для дальнейшего рассмотрения кандидаты есть, поэтому честный путь “ничего не делать” здесь не включается. При этом это не разрешение менять файлы: список только показывает, какие точные пути можно обсуждать дальше в контролируемом порядке.

Разрешенные для следующего рассмотрения кандидаты сейчас сводятся к четырем точным путям:
- `scripts/run-all.sh`
- `scripts/health-check.sh`
- `scripts/validate-architecture.sh`
- `scripts/audit-agentos.py`

Почему именно они:
- это либо тонкие обертки, либо агрегатор с читаемым письменным описанием;
- по ним не найден скрытый переход границ жизненного цикла или границ человеческого подтверждения;
- для них можно сформулировать изменение как сохранение текущего поведения, а не как переписывание правил.

Почему часть путей заблокирована:
- `scripts/agentos.py` и `scripts/canonical-cleanup.sh` слишком рискованные;
- `scripts/check-m74-dispatcher-regression.py` не имеет достаточно ясного письменного контракта поведения;
- `scripts/lib/path_utils.py`, `scripts/renderers/plain_status_renderer.py`, `scripts/renderers/rich_status_renderer.py` требуют прояснения письменных правил и, возможно, позже затронут документацию в M90.

M89.2 does not authorize script optimization.
M89.2 does not approve any candidate.
M89.2 does not select a human subset.
M89.2 does not start M89.3.
M89.2 does not start M89.4.
M89.2 does not modify scripts.
M89.2 does not modify Markdown.
Candidate registration is evidence, not approval.
Human-selected subset remains required before any physical script change.
