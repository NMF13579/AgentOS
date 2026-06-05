```yaml
report_id: M85_3_COMPACT_TASK_BRIEF_STANDARD_REPORT
task_id: M85.3
task_name: Compact Task Brief Standard
mode: policy creation
```

## Precondition Check

```yaml
precondition_check:
  m85_2_report_exists: true
  m85_2_final_status: M85_2_NEW_ARTIFACT_PREWRITE_GATE_COMPLETE_WITH_WARNINGS
  may_prepare_m85_3_compact_task_brief_standard: true_with_warnings
  physical_cleanup_performed: false
  approval_created: false
  lifecycle_mutation_created: false
  m86_started: false
  m87_started: false
  m88_started: false
```

## Standard Creation

```yaml
standard_creation:
  standard_path: docs/COMPACT-TASK-BRIEF-STANDARD.md
  standard_created_or_updated: true
  required_minimal_structure_defined: true
  non_weakening_boundary_defined: true
  required_safety_blocks_defined: true
  compression_rules_defined: true
  prohibited_compression_defined: true
  risk_based_expansion_defined: true
  validation_requirements_preserved: true
  final_boundary_rule_required: true
  canonical_precedence_rule_defined: true
  task_brief_non_override_rule_defined: true
  hidden_source_of_truth_prevention_defined: true
  high_risk_exact_paths_required: true
  high_risk_fail_closed_preconditions_required: true
```

## Boundary Status

```yaml
boundary_status:
  physical_cleanup_performed: false
  existing_files_deleted: false
  existing_files_moved: false
  existing_files_archived: false
  existing_files_compressed: false
  existing_files_consolidated: false
  scripts_created: false
  schemas_created: false
  workflows_created: false
  registry_created: false
  dependency_map_created: false
  cleanup_candidate_register_created: false
  approval_created: false
  lifecycle_mutation_created: false
  canonical_docs_overridden: false
  hidden_source_of_truth_created: false
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
    - docs/REPORT-LIFECYCLE-POLICY.md
    - docs/NEW-ARTIFACT-PREWRITE-GATE.md
    - reports/m85-m82-closure-intake.md
    - reports/m85-report-lifecycle-policy-report.md
    - reports/m85-new-artifact-prewrite-gate-report.md
  notes:
    - Owner approved M85.2 carry-forward for M85.3 validation.
    - Canonical docs were not overridden by the new standard.
```

## Final Decision

```yaml
FINAL_STATUS: M85_3_COMPACT_TASK_BRIEF_STANDARD_COMPLETE_WITH_WARNINGS
may_prepare_m85_4_growth_control_evidence_scope_lock: true_with_warnings
```
