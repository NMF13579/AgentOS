```yaml
report_id: M85_1_REPORT_LIFECYCLE_POLICY_REPORT
task_id: M85.1
task_name: Report Lifecycle Policy
mode: policy creation
```

## Precondition Check

```yaml
precondition_check:
  m85_0_exists: true
  m85_0_final_status: M85_0R2_READY_FOR_GROWTH_CONTROL_WITH_WARNINGS
  may_prepare_m85_1_growth_control: true_with_warnings
  m84_continuation_allowed: false
  physical_cleanup_allowed: false
  approval_created: false
  lifecycle_mutation_created: false
```

## Policy Creation

```yaml
policy_creation:
  policy_path: docs/REPORT-LIFECYCLE-POLICY.md
  policy_created_or_updated: true
  lifecycle_statuses_defined: true
  non_approval_boundary_defined: true
  cleanup_authorization_forbidden: true
  unknown_blocked_rule_defined: true
  future_report_budget_defined: true
```

## Boundary Status

```yaml
boundary_status:
  physical_cleanup_performed: false
  existing_reports_modified: false
  existing_reports_deleted: false
  existing_reports_moved: false
  existing_reports_archived: false
  existing_reports_compressed: false
  registry_created: false
  dependency_map_created: false
  cleanup_candidate_register_created: false
  approval_created: false
  lifecycle_mutation_created: false
  m86_started: false
  m87_started: false
  m88_started: false
```

## Validation Results

```yaml
validation_results:
  carry_forward_exception_used_for_validation: true
  carry_forward_paths:
    - tasks/active-task.md
    - reports/m85-m82-closure-intake.md
  notes:
    - Owner approved runner-managed carry-forward for M85.1 validation.
    - Existing reports were not rewritten; only the new M85.1 report was created.
```

## Final Decision

```yaml
FINAL_STATUS: M85_1_REPORT_LIFECYCLE_POLICY_COMPLETE_WITH_WARNINGS
may_prepare_m85_2_new_artifact_prewrite_gate: true_with_warnings
```
