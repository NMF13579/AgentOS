## Human Summary

- Can next M80 task be prepared: true_with_warnings
- Does this change validation authority: false
- Does this edit scripts/workflows: false
- Does this create new baseline: false
- Does this start M81: false
- Main blockers:
  - "none"
- Main warnings:
  - "LEGACY_VALIDATION_ENTRYPOINTS_PRESENT; ADVISORY_ENTRYPOINTS_PRESENT; REVIEW_ITEMS_CARRIED_TO_80_4; GIT_STATUS_HAS_UNRELATED_CHANGES"
- Canonical dispatcher identified: true
- Validation authority clear: true
- CI validation mapping clear: true
- Unknown validation entrypoints: 0
- Legacy validation entrypoints: 1
- Items requiring 80.4 review: 4
- Authority changes allowed by 80.3: 0
- M81 artifacts created: false
- M81 task briefs created: false
- Next readiness field: "may_prepare_m80_4: true_with_warnings"

## Title

M80.3 Validation Entrypoint Map

## Purpose

Map the validation authority and validation entrypoints that remain after M79 and the M80 source-evidence intake. This report is read-only and records what appears to be the canonical dispatcher, the direct validation checkers, the wrappers, the CI-invoked entrypoints, and the remaining review items that should be carried to 80.4.

## 80.2 Optimized File Map Check

task_id: "80.3"
task_name: "Validation Entrypoint Map"
reports_directory_exists: true
input_file: "reports/m80-optimized-file-map.md"

m80_2_optimized_file_map_exists: true
m80_2_optimized_file_map_readable: true
m80_2_final_status_detected: "FINAL_STATUS: M80_OPTIMIZED_FILE_MAP_COMPLETE_WITH_WARNINGS"
m80_2_final_status_acceptable: true
m80_2_readiness_detected: "may_prepare_m80_3: true_with_warnings"
m80_2_readiness_acceptable: true

validation_entrypoint_map_created: true

validation_entrypoint_candidate_count: 15
canonical_dispatcher_count: 1
canonical_checker_count: 5
active_wrapper_count: 2
ci_entrypoint_count: 4
advisory_entrypoint_count: 2
legacy_entrypoint_count: 1
deprecated_candidate_count: 0
unknown_entrypoint_count: 0
non_validation_script_count: 0

ci_workflow_count: 5
ci_workflow_invoking_validation_count: 5
ci_workflow_unknown_validation_count: 0

e1_direct_evidence_count: 15
e2_structural_evidence_count: 0
e3_heuristic_evidence_count: 0
e0_unknown_evidence_count: 0

high_confidence_count: 15
medium_confidence_count: 0
low_confidence_count: 0
unknown_confidence_count: 0

output_contract_visible_count: 12
json_output_visible_count: 7
exit_code_semantics_visible_count: 15
warning_visibility_visible_count: 6
false_pass_boundary_visible_count: 7
approval_boundary_visible_count: 15

review_needed_in_80_4_count: 4

validation_authority_clear: true
canonical_dispatcher_identified: true
ci_validation_mapping_clear: true
legacy_validation_paths_visible: true
unknown_validation_paths_visible: false

authority_change_allowed_by_80_3_count: 0
cleanup_action_allowed_by_80_3_count: 0
mutation_allowed_by_80_3_count: 0

validation_authority_modified_by_80_3: false
scripts_modified_by_80_3: false
workflows_modified_by_80_3: false
dispatcher_modified_by_80_3: false
ci_modified_by_80_3: false
entrypoints_consolidated_by_80_3: false
entrypoints_deprecated_by_80_3: false

unknown_treated_as_ok: false
missing_evidence_treated_as_ok: false
ci_pass_treated_as_approval: false
validation_pass_treated_as_approval: false
evidence_treated_as_approval: false
readiness_treated_as_start: false
false_pass_boundary_weakened_by_80_3: false
validation_authority_weakened_by_80_3: false

new_baseline_created_by_80_3: false
baseline_updated_by_80_3: false
derived_artifacts_updated_by_80_3: false
repo_map_updated_by_80_3: false
context_index_updated_by_80_3: false
physical_cleanup_performed_by_80_3: false
rollback_executed_by_80_3: false
repair_authorized_by_80_3: false
fix_tasks_created_by_80_3: false
lifecycle_mutation_by_80_3: false
approval_claim_created_by_80_3: false

m80_artifacts_created_by_80_3_beyond_entrypoint_map: false
m80_consolidation_started_by_80_3_beyond_entrypoint_map: false
m81_artifacts_created_by_80_3: false
m81_task_briefs_created_by_80_3: false
m81_started_by_80_3: false
saas_or_ui_artifacts_created_by_80_3: false
autopilot_enabled_by_80_3: false

human_summary_consistent_with_machine_fields: true

blocker_codes:
  - "none"
warning_codes:
  - "M80_2_WARNINGS_CARRIED_FORWARD"
  - "M79_WARNINGS_CARRIED_FORWARD"
  - "M78_WARNINGS_CARRIED_FORWARD"
  - "VALIDATION_AUTHORITY_AMBIGUITY_VISIBLE"
  - "CI_VALIDATION_MAPPING_AMBIGUITY_VISIBLE"
  - "LEGACY_VALIDATION_ENTRYPOINTS_PRESENT"
  - "ADVISORY_ENTRYPOINTS_PRESENT"
  - "REVIEW_ITEMS_CARRIED_TO_80_4"
  - "GIT_STATUS_HAS_UNRELATED_CHANGES"

## Validation Entrypoint Mapping Method

I used the optimized file map, the validation authority docs, the dispatcher contract docs, the script responsibility map, the validators registry, and the read-only workflow files. I treated direct registry and workflow references as direct evidence, and I did not edit any script or workflow.

## Bounded Evidence Rules Used

- `E1_DIRECT_EVIDENCE` for the dispatcher registry, responsibility map, script headers, and workflow references.
- `E2_STRUCTURAL_EVIDENCE` was not needed for the chosen set.
- `E3_HEURISTIC_EVIDENCE` was not needed for the chosen set.
- `E0_UNKNOWN` was not used for the chosen set.

## Validation Entrypoint Inventory

validation_entrypoints:
  - path: "scripts/agentos-validate.py"
    entrypoint_class: "CANONICAL_DISPATCHER"
    area: "scripts"
    invoked_by:
      - "ci"
      - "manual"
    invokes:
      - "scripts/agentos-validate.py all"
    authority_level: "canonical"
    evidence_level: "E1_DIRECT_EVIDENCE"
    evidence_source:
      - "scripts/VALIDATORS.md"
      - ".github/workflows/agentos-validate.yml"
      - "docs/VALIDATION-AUTHORITY-MODEL.md"
    classification_confidence: "high"
    output_contract_visible: true
    json_output_visible: true
    exit_code_semantics_visible: true
    warning_visibility_visible: true
    false_pass_boundary_visible: true
    approval_boundary_visible: true
    review_needed_in_80_4: false
    authority_change_allowed_by_80_3: false
    cleanup_action_allowed_by_80_3: false
    mutation_allowed_by_80_3: false
    notes: "Official validation orchestrator and routing entrypoint."
  - path: "scripts/validate-task.py"
    entrypoint_class: "CANONICAL_CHECKER"
    area: "scripts"
    invoked_by:
      - "ci"
    invokes:
      - "tasks/active-task.md"
    authority_level: "canonical"
    evidence_level: "E1_DIRECT_EVIDENCE"
    evidence_source:
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
      - ".github/workflows/dev-only/agentos-validation.yml"
      - "scripts/validate-task.py"
    classification_confidence: "high"
    output_contract_visible: true
    json_output_visible: false
    exit_code_semantics_visible: true
    warning_visibility_visible: false
    false_pass_boundary_visible: false
    approval_boundary_visible: true
    review_needed_in_80_4: false
    authority_change_allowed_by_80_3: false
    cleanup_action_allowed_by_80_3: false
    mutation_allowed_by_80_3: false
    notes: "Direct task validation checker."
  - path: "scripts/validate-verification.py"
    entrypoint_class: "CANONICAL_CHECKER"
    area: "scripts"
    invoked_by:
      - "ci"
    invokes:
      - "reports/verification.md"
    authority_level: "canonical"
    evidence_level: "E1_DIRECT_EVIDENCE"
    evidence_source:
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
      - ".github/workflows/dev-only/agentos-validation.yml"
      - "scripts/validate-verification.py"
    classification_confidence: "high"
    output_contract_visible: true
    json_output_visible: false
    exit_code_semantics_visible: true
    warning_visibility_visible: false
    false_pass_boundary_visible: false
    approval_boundary_visible: true
    review_needed_in_80_4: false
    authority_change_allowed_by_80_3: false
    cleanup_action_allowed_by_80_3: false
    mutation_allowed_by_80_3: false
    notes: "Direct verification schema checker."
  - path: "scripts/check-false-pass-resistance.py"
    entrypoint_class: "CANONICAL_CHECKER"
    area: "scripts"
    invoked_by:
      - "ci"
      - "manual"
    invokes:
      - "false-pass resistance checks"
    authority_level: "canonical"
    evidence_level: "E1_DIRECT_EVIDENCE"
    evidence_source:
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
      - "scripts/check-false-pass-resistance.py"
      - "docs/DISPATCHER-IO-CONTRACT.md"
    classification_confidence: "high"
    output_contract_visible: true
    json_output_visible: true
    exit_code_semantics_visible: true
    warning_visibility_visible: true
    false_pass_boundary_visible: true
    approval_boundary_visible: true
    review_needed_in_80_4: false
    authority_change_allowed_by_80_3: false
    cleanup_action_allowed_by_80_3: false
    mutation_allowed_by_80_3: false
    notes: "Explicit false PASS resistance boundary checker."
  - path: "scripts/check-task-validation-contract.py"
    entrypoint_class: "CANONICAL_CHECKER"
    area: "scripts"
    invoked_by:
      - "ci"
      - "manual"
    invokes:
      - "task validation contract checks"
    authority_level: "canonical"
    evidence_level: "E1_DIRECT_EVIDENCE"
    evidence_source:
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
      - "docs/TASK-VALIDATION-CONTRACT-ARCHITECTURE.md"
      - "scripts/check-task-validation-contract.py"
    classification_confidence: "high"
    output_contract_visible: true
    json_output_visible: true
    exit_code_semantics_visible: true
    warning_visibility_visible: true
    false_pass_boundary_visible: true
    approval_boundary_visible: true
    review_needed_in_80_4: false
    authority_change_allowed_by_80_3: false
    cleanup_action_allowed_by_80_3: false
    mutation_allowed_by_80_3: false
    notes: "Contract checker keeps human-review and completion boundaries visible."
  - path: "scripts/check-validator-authority-boundary.py"
    entrypoint_class: "CANONICAL_CHECKER"
    area: "scripts"
    invoked_by:
      - "ci"
      - "manual"
    invokes:
      - "validator authority boundary checks"
    authority_level: "canonical"
    evidence_level: "E1_DIRECT_EVIDENCE"
    evidence_source:
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
      - "scripts/check-validator-authority-boundary.py"
      - "docs/VALIDATION-AUTHORITY-MODEL.md"
    classification_confidence: "high"
    output_contract_visible: true
    json_output_visible: true
    exit_code_semantics_visible: true
    warning_visibility_visible: false
    false_pass_boundary_visible: true
    approval_boundary_visible: true
    review_needed_in_80_4: false
    authority_change_allowed_by_80_3: false
    cleanup_action_allowed_by_80_3: false
    mutation_allowed_by_80_3: false
    notes: "Authority-boundary checker does not modify authority."
  - path: "scripts/run-all.sh"
    entrypoint_class: "ACTIVE_WRAPPER"
    area: "scripts"
    invoked_by:
      - "ci"
      - "manual"
    invokes:
      - "scripts/agentos-validate.py all"
    authority_level: "wrapper"
    evidence_level: "E1_DIRECT_EVIDENCE"
    evidence_source:
      - "scripts/VALIDATORS.md"
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
      - "scripts/run-all.sh"
    classification_confidence: "high"
    output_contract_visible: true
    json_output_visible: false
    exit_code_semantics_visible: true
    warning_visibility_visible: false
    false_pass_boundary_visible: true
    approval_boundary_visible: true
    review_needed_in_80_4: false
    authority_change_allowed_by_80_3: false
    cleanup_action_allowed_by_80_3: false
    mutation_allowed_by_80_3: false
    notes: "Compatibility wrapper that delegates to the dispatcher."
  - path: "scripts/health-check.sh"
    entrypoint_class: "ACTIVE_WRAPPER"
    area: "scripts"
    invoked_by:
      - "ci"
      - "manual"
    invokes:
      - "scripts/agentos-validate.py all"
    authority_level: "wrapper"
    evidence_level: "E1_DIRECT_EVIDENCE"
    evidence_source:
      - "scripts/VALIDATORS.md"
      - ".github/workflows/dev-only/health.yml"
      - "scripts/health-check.sh"
    classification_confidence: "high"
    output_contract_visible: true
    json_output_visible: false
    exit_code_semantics_visible: true
    warning_visibility_visible: false
    false_pass_boundary_visible: false
    approval_boundary_visible: true
    review_needed_in_80_4: false
    authority_change_allowed_by_80_3: false
    cleanup_action_allowed_by_80_3: false
    mutation_allowed_by_80_3: false
    notes: "Compatibility wrapper with module-layout checks."
  - path: "scripts/validate-architecture.sh"
    entrypoint_class: "LEGACY_ENTRYPOINT"
    area: "scripts"
    invoked_by:
      - "ci"
      - "manual"
    invokes:
      - "scripts/agentos-validate.py all"
    authority_level: "legacy"
    evidence_level: "E1_DIRECT_EVIDENCE"
    evidence_source:
      - "scripts/VALIDATORS.md"
      - ".github/workflows/dev-only/modular-validators.yml"
      - "scripts/validate-architecture.sh"
    classification_confidence: "high"
    output_contract_visible: true
    json_output_visible: false
    exit_code_semantics_visible: true
    warning_visibility_visible: false
    false_pass_boundary_visible: true
    approval_boundary_visible: true
    review_needed_in_80_4: true
    authority_change_allowed_by_80_3: false
    cleanup_action_allowed_by_80_3: false
    mutation_allowed_by_80_3: false
    notes: "Legacy wrapper remains visible and should be reviewed later."
  - path: "scripts/check-pr-quality.py"
    entrypoint_class: "CI_ENTRYPOINT"
    area: "scripts"
    invoked_by:
      - "ci"
    invokes:
      - "task and verification frontmatter checks"
    authority_level: "ci"
    evidence_level: "E1_DIRECT_EVIDENCE"
    evidence_source:
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
      - ".github/workflows/dev-only/agentos-validation.yml"
      - "scripts/check-pr-quality.py"
    classification_confidence: "high"
    output_contract_visible: false
    json_output_visible: false
    exit_code_semantics_visible: true
    warning_visibility_visible: false
    false_pass_boundary_visible: false
    approval_boundary_visible: true
    review_needed_in_80_4: false
    authority_change_allowed_by_80_3: false
    cleanup_action_allowed_by_80_3: false
    mutation_allowed_by_80_3: false
    notes: "CI-invoked quality gate with exit-status contract."
  - path: "scripts/check-dangerous-commands.py"
    entrypoint_class: "CI_ENTRYPOINT"
    area: "scripts"
    invoked_by:
      - "ci"
    invokes:
      - "dangerous-command scan"
    authority_level: "ci"
    evidence_level: "E1_DIRECT_EVIDENCE"
    evidence_source:
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
      - ".github/workflows/dev-only/agentos-validation.yml"
      - "scripts/check-dangerous-commands.py"
    classification_confidence: "high"
    output_contract_visible: false
    json_output_visible: false
    exit_code_semantics_visible: true
    warning_visibility_visible: false
    false_pass_boundary_visible: false
    approval_boundary_visible: true
    review_needed_in_80_4: false
    authority_change_allowed_by_80_3: false
    cleanup_action_allowed_by_80_3: false
    mutation_allowed_by_80_3: false
    notes: "CI-invoked safety scan with exit-status contract."
  - path: "scripts/check-risk.py"
    entrypoint_class: "CI_ENTRYPOINT"
    area: "scripts"
    invoked_by:
      - "ci"
    invokes:
      - "risk-policy checks"
    authority_level: "ci"
    evidence_level: "E1_DIRECT_EVIDENCE"
    evidence_source:
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
      - ".github/workflows/dev-only/agentos-validation.yml"
      - "scripts/check-risk.py"
    classification_confidence: "high"
    output_contract_visible: false
    json_output_visible: false
    exit_code_semantics_visible: true
    warning_visibility_visible: false
    false_pass_boundary_visible: false
    approval_boundary_visible: true
    review_needed_in_80_4: false
    authority_change_allowed_by_80_3: false
    cleanup_action_allowed_by_80_3: false
    mutation_allowed_by_80_3: false
    notes: "CI-invoked risk gate with exit-status contract."
  - path: "scripts/check-context-pipeline.py"
    entrypoint_class: "CI_ENTRYPOINT"
    area: "scripts"
    invoked_by:
      - "ci"
      - "manual"
    invokes:
      - "scripts/check-context-pipeline.py --strict --json"
      - "scripts/check-context-pipeline.py --advisory --json"
    authority_level: "ci"
    evidence_level: "E1_DIRECT_EVIDENCE"
    evidence_source:
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
      - ".github/workflows/dev-only/context-pipeline.yml"
      - "scripts/check-context-pipeline.py"
    classification_confidence: "high"
    output_contract_visible: true
    json_output_visible: true
    exit_code_semantics_visible: true
    warning_visibility_visible: true
    false_pass_boundary_visible: true
    approval_boundary_visible: true
    review_needed_in_80_4: true
    authority_change_allowed_by_80_3: false
    cleanup_action_allowed_by_80_3: false
    mutation_allowed_by_80_3: false
    notes: "CI workflow runs strict and advisory modes; advisory mode is carried forward."
  - path: "scripts/check-context-index-freshness.py"
    entrypoint_class: "ADVISORY_ENTRYPOINT"
    area: "scripts"
    invoked_by:
      - "manual"
    invokes:
      - "data/context-index.json freshness checks"
    authority_level: "advisory"
    evidence_level: "E1_DIRECT_EVIDENCE"
    evidence_source:
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
      - "docs/M30-CONTEXT-INDEX-FRESHNESS-GATE.md"
      - "scripts/check-context-index-freshness.py"
    classification_confidence: "high"
    output_contract_visible: true
    json_output_visible: true
    exit_code_semantics_visible: true
    warning_visibility_visible: true
    false_pass_boundary_visible: false
    approval_boundary_visible: true
    review_needed_in_80_4: true
    authority_change_allowed_by_80_3: false
    cleanup_action_allowed_by_80_3: false
    mutation_allowed_by_80_3: false
    notes: "Freshness audit remains advisory and should be reviewed later."
  - path: "scripts/audit-validation-integration.py"
    entrypoint_class: "ADVISORY_ENTRYPOINT"
    area: "scripts"
    invoked_by:
      - "manual"
    invokes:
      - "validation integration audit"
    authority_level: "advisory"
    evidence_level: "E1_DIRECT_EVIDENCE"
    evidence_source:
      - "docs/SCRIPT-RESPONSIBILITY-MAP.md"
      - "scripts/audit-validation-integration.py"
    classification_confidence: "high"
    output_contract_visible: true
    json_output_visible: true
    exit_code_semantics_visible: true
    warning_visibility_visible: true
    false_pass_boundary_visible: false
    approval_boundary_visible: true
    review_needed_in_80_4: true
    authority_change_allowed_by_80_3: false
    cleanup_action_allowed_by_80_3: false
    mutation_allowed_by_80_3: false
    notes: "Integration audit is advisory, not authority-changing."

- `scripts/agentos-validate.py` - `CANONICAL_DISPATCHER` - official validation orchestrator and routing entrypoint.
- `scripts/validate-task.py` - `CANONICAL_CHECKER` - direct task validation checker.
- `scripts/validate-verification.py` - `CANONICAL_CHECKER` - direct verification schema checker.
- `scripts/check-false-pass-resistance.py` - `CANONICAL_CHECKER` - false PASS boundary checker.
- `scripts/check-task-validation-contract.py` - `CANONICAL_CHECKER` - task validation contract checker.
- `scripts/check-validator-authority-boundary.py` - `CANONICAL_CHECKER` - validator authority boundary checker.
- `scripts/run-all.sh` - `ACTIVE_WRAPPER` - compatibility wrapper that delegates to the dispatcher.
- `scripts/health-check.sh` - `ACTIVE_WRAPPER` - compatibility wrapper that delegates to the dispatcher after module checks.
- `scripts/validate-architecture.sh` - `LEGACY_ENTRYPOINT` - legacy wrapper that delegates to the dispatcher.
- `scripts/check-pr-quality.py` - `CI_ENTRYPOINT` - directly invoked by CI validation workflow.
- `scripts/check-dangerous-commands.py` - `CI_ENTRYPOINT` - directly invoked by CI validation workflow.
- `scripts/check-risk.py` - `CI_ENTRYPOINT` - directly invoked by CI validation workflow.
- `scripts/check-context-pipeline.py` - `CI_ENTRYPOINT` - directly invoked by CI workflow in strict and advisory modes.
- `scripts/check-context-index-freshness.py` - `ADVISORY_ENTRYPOINT` - freshness audit that stays advisory and needs later review.
- `scripts/audit-validation-integration.py` - `ADVISORY_ENTRYPOINT` - audit entrypoint that stays advisory and needs later review.

## Canonical Dispatcher Candidates

- `scripts/agentos-validate.py`

## Canonical Checkers

- `scripts/validate-task.py`
- `scripts/validate-verification.py`
- `scripts/check-false-pass-resistance.py`
- `scripts/check-task-validation-contract.py`
- `scripts/check-validator-authority-boundary.py`

## Active Wrappers

- `scripts/run-all.sh`
- `scripts/health-check.sh`

## CI Entrypoints

- `scripts/check-pr-quality.py`
- `scripts/check-dangerous-commands.py`
- `scripts/check-risk.py`
- `scripts/check-context-pipeline.py`

## Advisory Entrypoints

- `scripts/check-context-index-freshness.py`
- `scripts/audit-validation-integration.py`

## Legacy Entrypoints

- `scripts/validate-architecture.sh`

## Deprecated Candidates

- none identified in the chosen validation set

## Unknown Entrypoints

- none identified in the chosen validation set

## Non-Validation Scripts

- none identified in the chosen validation set

## CI Workflow Validation Map

ci_workflow_validation_map:
  - workflow_path: ".github/workflows/agentos-validate.yml"
    workflow_name: "AgentOS Validate"
    invokes_validation: true
    invoked_entrypoints:
      - "scripts/agentos-validate.py"
      - "scripts/sync-task-ids.py"
    result_interpretation_visible: true
    exit_code_semantics_visible: true
    warnings_visibility_visible: true
    approval_boundary_visible: true
    evidence_source:
      - ".github/workflows/agentos-validate.yml"
    review_needed_in_80_4: false
  - workflow_path: ".github/workflows/dev-only/agentos-validation.yml"
    workflow_name: "AgentOS Validation"
    invokes_validation: true
    invoked_entrypoints:
      - "scripts/validate-task.py"
      - "scripts/validate-verification.py"
      - "scripts/check-pr-quality.py"
      - "scripts/check-dangerous-commands.py"
      - "scripts/check-risk.py"
      - "scripts/run-all.sh"
    result_interpretation_visible: true
    exit_code_semantics_visible: true
    warnings_visibility_visible: true
    approval_boundary_visible: true
    evidence_source:
      - ".github/workflows/dev-only/agentos-validation.yml"
    review_needed_in_80_4: false
  - workflow_path: ".github/workflows/dev-only/context-pipeline.yml"
    workflow_name: "Context Pipeline"
    invokes_validation: true
    invoked_entrypoints:
      - "scripts/check-context-pipeline.py --strict --json"
      - "scripts/check-context-pipeline.py --advisory --json"
    result_interpretation_visible: true
    exit_code_semantics_visible: true
    warnings_visibility_visible: true
    approval_boundary_visible: true
    evidence_source:
      - ".github/workflows/dev-only/context-pipeline.yml"
    review_needed_in_80_4: true
  - workflow_path: ".github/workflows/dev-only/health.yml"
    workflow_name: "Health Check"
    invokes_validation: true
    invoked_entrypoints:
      - "scripts/health-check.sh"
    result_interpretation_visible: true
    exit_code_semantics_visible: true
    warnings_visibility_visible: true
    approval_boundary_visible: true
    evidence_source:
      - ".github/workflows/dev-only/health.yml"
    review_needed_in_80_4: false
  - workflow_path: ".github/workflows/dev-only/modular-validators.yml"
    workflow_name: "Canonical Architecture Validation (primary)"
    invokes_validation: true
    invoked_entrypoints:
      - "scripts/validate-architecture.sh"
    result_interpretation_visible: true
    exit_code_semantics_visible: true
    warnings_visibility_visible: true
    approval_boundary_visible: true
    evidence_source:
      - ".github/workflows/dev-only/modular-validators.yml"
    review_needed_in_80_4: true

| workflow_path | workflow_name | invokes_validation | invoked_entrypoints | result_interpretation_visible | exit_code_semantics_visible | warnings_visibility_visible | approval_boundary_visible | evidence_source | review_needed_in_80_4 |
|---|---|---|---|---|---|---|---|---|---|
| `.github/workflows/agentos-validate.yml` | AgentOS Validate | true | `scripts/agentos-validate.py`, `scripts/sync-task-ids.py` | true | true | true | true | `.github/workflows/agentos-validate.yml` | false |
| `.github/workflows/dev-only/agentos-validation.yml` | AgentOS Validation | true | `scripts/validate-task.py`, `scripts/validate-verification.py`, `scripts/check-pr-quality.py`, `scripts/check-dangerous-commands.py`, `scripts/check-risk.py`, `scripts/run-all.sh` | true | true | true | true | `.github/workflows/dev-only/agentos-validation.yml` | false |
| `.github/workflows/dev-only/context-pipeline.yml` | Context Pipeline | true | `scripts/check-context-pipeline.py --strict --json`, `scripts/check-context-pipeline.py --advisory --json` | true | true | true | true | `.github/workflows/dev-only/context-pipeline.yml` | true |
| `.github/workflows/dev-only/health.yml` | Health Check | true | `scripts/health-check.sh` | true | true | true | true | `.github/workflows/dev-only/health.yml` | false |
| `.github/workflows/dev-only/modular-validators.yml` | Canonical Architecture Validation (primary) | true | `scripts/validate-architecture.sh` | true | true | true | true | `.github/workflows/dev-only/modular-validators.yml` | true |

## Output Contract Visibility

The dispatcher and the direct checker scripts have visible output contracts. The shell wrappers inherit that visibility by delegation. The exit-only checkers are still visible through their documented exit behavior, but they do not expose a richer machine-readable output contract.

## JSON Output Visibility

JSON output is visible for the dispatcher, the false-pass checker, the task-validation contract checker, the validator-authority boundary checker, and the context-pipeline / advisory audits. The exit-only checkers do not expose JSON output in the chosen mapping.

## Exit-Code Semantics Visibility

Exit-code semantics are visible for every selected validation entrypoint. The dispatcher contract, the script docs, or the workflow usage make the exit behavior visible.

## Warning Visibility

Warnings are visible for the dispatcher, the false-pass checker, the task-validation contract checker, the context-pipeline workflow path, and the advisory audits. The exit-only checkers do not hide warnings because they do not claim warning-bearing clean PASS semantics.

## False PASS Boundary Visibility

The false PASS boundary is visible in the dispatcher contract, the false-pass checker, the task-validation contract checker, the validator-authority boundary checker, and the wrapper/doc boundary references. The wrappers do not weaken that boundary.

## Approval Boundary Visibility

The approval boundary is visible in the dispatcher docs, the validation authority model, the CI workflow headers, and the validation scripts. CI PASS is not approval, and the selected entrypoints do not override that rule.

## Validation Authority Clarity

The canonical dispatcher is identified. The CI-invoked validation path is visible. Legacy and advisory validation paths are also visible, so the map is clear with warnings rather than hidden uncertainty.

## Items Requiring 80.4 Review

- `scripts/validate-architecture.sh` - legacy wrapper path.
- `scripts/check-context-pipeline.py` - advisory mode is visible in CI.
- `scripts/check-context-index-freshness.py` - advisory freshness audit.
- `scripts/audit-validation-integration.py` - advisory validation-integration audit.

## No Authority Mutation Boundary

No validation authority was changed. No new authority was created. No script, workflow, or dispatcher behavior was modified.

## No Script / Workflow Edit Boundary

No scripts were edited. No workflows were edited. No CI configuration was changed.

## No-New-Baseline Boundary

No new baseline was created. No baseline was updated. No derived artifact was updated.

## M81 Boundary Check

No M81 artifacts were created. No M81 task briefs were created. M81 was not started.

## Blockers

- none

## Warnings

- `M80_2_WARNINGS_CARRIED_FORWARD`
- `M79_WARNINGS_CARRIED_FORWARD`
- `M78_WARNINGS_CARRIED_FORWARD`
- `VALIDATION_AUTHORITY_AMBIGUITY_VISIBLE`
- `CI_VALIDATION_MAPPING_AMBIGUITY_VISIBLE`
- `LEGACY_VALIDATION_ENTRYPOINTS_PRESENT`
- `ADVISORY_ENTRYPOINTS_PRESENT`
- `REVIEW_ITEMS_CARRIED_TO_80_4`
- `GIT_STATUS_HAS_UNRELATED_CHANGES`

## Local Final Status

FINAL_STATUS: M80_VALIDATION_ENTRYPOINT_MAP_COMPLETE_WITH_WARNINGS

## Readiness for 80.4

may_prepare_m80_4: true_with_warnings

## Final Boundary Statement

This report maps validation authority only. It does not change validation authority, it does not edit scripts or workflows, it does not consolidate entrypoints, it does not create a new baseline, and it does not start M81.
