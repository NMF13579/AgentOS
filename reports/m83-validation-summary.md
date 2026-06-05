# M83.6 Post-Reduction Validation Summary

## M83.5 Intake

```yaml
m83_5_status_detected: "M83_5_REDUCTION_DIFF_SUMMARY_BLOCKED"
m83_5_status_acceptable: false
m83_5_may_prepare_83_6_detected: false
m83_6_validation_summary_allowed: false
```

## Validation Requirement Extraction

```yaml
validation_requirement_extraction:
  m82_rollback_plan_readable: true
  m83_execution_report_readable: true
  m83_diff_summary_readable: true
  validation_requirements_found: false
  validation_requirements_count: 0
  validation_requirements: []
```

## Validation Execution Summary

```yaml
m83_validation_summary:
  validation_required: false
  validation_performed: false
  validation_items: []
  validation_summary_result: "BLOCKED"
```

## Archive Validation Reflection

```yaml
archive_validation_reflection:
  archive_validation_required: false
  archive_validation_performed: false
  archive_validation_items: []
```

## Compression Validation Reflection

```yaml
compression_validation_reflection:
  compression_validation_required: false
  compression_validation_performed: false
  compression_validation_items: []
```

## Reference Update Validation Reflection

```yaml
reference_update_validation_reflection:
  reference_update_validation_required: false
  reference_update_validation_performed: false
  reference_update_validation_items: []
```

## Diff Boundary Validation

```yaml
diff_boundary_validation:
  git_status_checked: false
  git_diff_name_status_checked: false
  m83_5_diff_summary_matches_current_diff: false
  forbidden_changes_detected: false
  unexpected_changes_detected: false
  permanent_deletion_detected: false
  validation_authority_changed: false
  scripts_ci_schemas_changed: false
```

## False PASS / Claim Boundary Check

```yaml
false_pass_claim_boundary_check:
  validation_pass_claimed: false
  validation_pass_treated_as_approval: false
  evidence_treated_as_approval: false
  ci_pass_treated_as_approval: false
  release_claim_created: false
  production_readiness_claim_created: false
  lifecycle_mutation_created: false
  feature_work_authorized: false
  m84_start_authorized: false
```

## Forbidden / Downstream Artifact Check

```yaml
forbidden_downstream_artifact_check:
  m83_completion_review_created: false
  m84_artifacts_created: false
  m85_artifacts_created: false
  m86_artifacts_created: false
  m87_artifacts_created: false
  m88_artifacts_created: false
  m91_artifacts_created: false
  validation_script_created_or_modified: false
  helper_script_created_or_modified: false
  automation_wrapper_created_or_modified: false
  approval_artifact_created: false
  release_artifact_created: false
  lifecycle_mutation_artifact_created: false
  feature_work_artifact_created: false
  human_checkpoint_artifact_created: false
```

## Carry-Forward From M83.5

```yaml
warnings_from_m83_5_carried_forward: true
unknowns_from_m83_5_carried_forward: true
gaps_from_m83_5_carried_forward: true
not_claimed_metrics_from_m83_5_carried_forward: true
blocking_items_from_m83_5_carried_forward: true
carry_forward_items_hidden: false
```

## Local M83.6 Status

```yaml
M83_6_STATUS: M83_6_VALIDATION_SUMMARY_BLOCKED
may_prepare_83_7_completion_review: false
```
