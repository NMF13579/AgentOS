```yaml
report_id: M85_4_GROWTH_CONTROL_EVIDENCE
task_id: M85.4
task_name: Growth Control Evidence & Scope Lock
mode: evidence consolidation
```

## Precondition Check

```yaml
precondition_check:
  m85_3_report_exists: true
  m85_3_final_status: M85_3_COMPACT_TASK_BRIEF_STANDARD_COMPLETE_WITH_WARNINGS
  may_prepare_m85_4_growth_control_evidence_scope_lock: true_with_warnings
  physical_cleanup_performed: false
  approval_created: false
  lifecycle_mutation_created: false
  canonical_docs_overridden: false
  hidden_source_of_truth_created: false
  m86_started: false
  m87_started: false
  m88_started: false
```

## Artifact Inventory

```yaml
artifact_inventory:
  m85_0_intake:
    path: reports/m85-m82-closure-intake.md
    exists: true
  report_lifecycle_policy:
    path: docs/REPORT-LIFECYCLE-POLICY.md
    exists: true
  report_lifecycle_policy_report:
    path: reports/m85-report-lifecycle-policy-report.md
    exists: true
  new_artifact_prewrite_gate:
    path: docs/NEW-ARTIFACT-PREWRITE-GATE.md
    exists: true
  new_artifact_prewrite_gate_report:
    path: reports/m85-new-artifact-prewrite-gate-report.md
    exists: true
  compact_task_brief_standard:
    path: docs/COMPACT-TASK-BRIEF-STANDARD.md
    exists: true
  compact_task_brief_standard_report:
    path: reports/m85-compact-task-brief-standard-report.md
    exists: true
```

## M85.0 Intake Evidence

```yaml
m85_0_evidence:
  final_status: M85_0R2_READY_FOR_GROWTH_CONTROL_WITH_WARNINGS
  may_prepare_m85_1_growth_control: true_with_warnings
  m85_line_is_independent: true
  m84_continuation_allowed: false
  physical_cleanup_allowed: false
  approval_created: false
  lifecycle_mutation_created: false

m85_0_required:
  m85_line_is_independent: true
  m84_continuation_allowed: false
  physical_cleanup_allowed: false
  approval_created: false
  lifecycle_mutation_created: false
```

## M85.1 Report Lifecycle Policy Evidence

```yaml
m85_1_evidence:
  final_status: M85_1_REPORT_LIFECYCLE_POLICY_COMPLETE_WITH_WARNINGS
  policy_exists: true
  non_approval_boundary_present: true
  task_completion_boundary_present: true
  cleanup_authorization_forbidden: true
  unknown_blocked_rule_present: true
  may_prepare_m85_2_new_artifact_prewrite_gate: true_with_warnings
```

## M85.2 New Artifact Pre-Write Gate Evidence

```yaml
m85_2_evidence:
  final_status: M85_2_NEW_ARTIFACT_PREWRITE_GATE_COMPLETE_WITH_WARNINGS
  policy_exists: true
  prewrite_packet_required: true
  unknown_artifact_type_blocked: true
  unknown_authority_blocked: true
  unknown_source_of_truth_blocked: true
  non_approval_boundary_present: true
  cleanup_authorization_forbidden: true
  lifecycle_mutation_forbidden: true
  human_checkpoint_rules_present: true
  may_prepare_m85_3_compact_task_brief_standard: true_with_warnings
```

## M85.3 Compact Task Brief Standard Evidence

```yaml
m85_3_evidence:
  final_status: M85_3_COMPACT_TASK_BRIEF_STANDARD_COMPLETE_WITH_WARNINGS
  standard_exists: true
  explicit_scope_preserved: true
  forbidden_changes_preserved: true
  validation_preserved: true
  final_boundary_rule_required: true
  non_weakening_boundary_present: true
  canonical_precedence_rule_present: true
  task_brief_non_override_rule_present: true
  hidden_source_of_truth_prevention_present: true
  high_risk_exact_paths_required: true
  high_risk_fail_closed_preconditions_required: true
  may_prepare_m85_4_growth_control_evidence_scope_lock: true_with_warnings
```

## Cross-Task Boundary Evidence

```yaml
cross_task_boundary_evidence:
  m84_continued: false
  m83_recovery_reopened: false
  physical_cleanup_performed: false
  cleanup_authorized: false
  approval_created: false
  lifecycle_mutation_created: false
  registry_created: false
  dependency_map_created: false
  cleanup_candidate_register_created: false
  m86_started: false
  m87_started: false
  m88_started: false

cross_task_required:
  m84_continued: false
  m83_recovery_reopened: false
  physical_cleanup_performed: false
  cleanup_authorized: false
  approval_created: false
  lifecycle_mutation_created: false
  registry_created: false
  dependency_map_created: false
  cleanup_candidate_register_created: false
  m86_started: false
  m87_started: false
  m88_started: false
```

## Growth Control Scope Lock

```yaml
m85_growth_control_scope_lock:
  report_lifecycle_policy_active: true
  new_artifact_prewrite_gate_active: true
  compact_task_brief_standard_active: true
  future_report_growth_controlled: true
  future_artifact_creation_controlled: true
  future_task_brief_bloat_controlled: true
  hidden_source_of_truth_blocked: true
  unknown_values_block_completion: true
```

## Warnings and Carry-Forward

```yaml
warnings_and_carry_forward:
  warnings_present: true
  warning_sources:
    - M85.0R2 / reports/m85-m82-closure-intake.md / M85_0R2_READY_FOR_GROWTH_CONTROL_WITH_WARNINGS
    - M85.1 / reports/m85-report-lifecycle-policy-report.md / M85_1_REPORT_LIFECYCLE_POLICY_COMPLETE_WITH_WARNINGS
    - M85.2 / reports/m85-new-artifact-prewrite-gate-report.md / M85_2_NEW_ARTIFACT_PREWRITE_GATE_COMPLETE_WITH_WARNINGS
    - M85.3 / reports/m85-compact-task-brief-standard-report.md / M85_3_COMPACT_TASK_BRIEF_STANDARD_COMPLETE_WITH_WARNINGS
  carry_forward_required: true
  carry_forward_items:
    - item: "runner-managed active task switching inside M85 line"
      blocks_m85_5_clean_completion: false
    - item: "dirty workspace carry-forward from prior M85 steps treated as existing context"
      blocks_m85_5_clean_completion: false
```

## Clean Readiness Requires

```yaml
clean_readiness_requires:
  all_required_artifacts_exist: true
  m85_0_intake_valid: true
  m85_1_policy_valid: true
  m85_2_policy_valid: true
  m85_3_standard_valid: true
  no_physical_cleanup_performed: true
  no_cleanup_authorized: true
  no_approval_created: true
  no_lifecycle_mutation_created: true
  no_registry_created: true
  no_dependency_map_created: true
  no_cleanup_candidate_register_created: true
  m86_not_started: true
  m87_not_started: true
  m88_not_started: true
```

## Validation Results

```yaml
validation_results:
  required_source_docs_verified: true
  changed_files_rule_interpreted_with_runner_managed_exception: true
  changed_files_existing_context:
    - tasks/active-task.md
    - docs/REPORT-LIFECYCLE-POLICY.md
    - docs/NEW-ARTIFACT-PREWRITE-GATE.md
    - docs/COMPACT-TASK-BRIEF-STANDARD.md
    - reports/m85-m82-closure-intake.md
    - reports/m85-report-lifecycle-policy-report.md
    - reports/m85-new-artifact-prewrite-gate-report.md
    - reports/m85-compact-task-brief-standard-report.md
  boundary_violation_detected: false
```

## Final Decision

```yaml
FINAL_STATUS: M85_4_GROWTH_CONTROL_EVIDENCE_COMPLETE_WITH_WARNINGS
may_prepare_m85_5_completion_review: true_with_warnings
```
