# M83.5 Reduction Diff Summary

## M83.4 Intake

```yaml
m83_4_status_detected: "M83_4_REFERENCE_UPDATES_BLOCKED"
m83_4_status_acceptable: false
m83_4_may_prepare_83_5_detected: false
m83_5_diff_summary_allowed: false
```

## Actual Git Diff Capture

```yaml
actual_git_diff_capture:
  git_status_checked: true
  git_diff_name_status_checked: true
  git_diff_checked: true
  git_metadata_available: true
  changed_files_count: 0
  changed_files: []
```

## Expected Change Boundary

```yaml
expected_change_boundary:
  all_changed_files_expected: true
  unexpected_changed_files_count: 0
  forbidden_changed_files_count: 0
  unexpected_changed_files: []
  forbidden_changed_files: []
```

## M83.2 / M83.3 / M83.4 Change Reflection

```yaml
m83_execution_change_reflection:
  m83_2_reports_archival_reflected: false
  m83_3_docs_bootstrap_compression_reflected: false
  m83_4_reference_updates_reflected: false
  claimed_changes_match_actual_diff: true
  reflection_items: []
```

## Permanent Deletion Check

```yaml
permanent_deletion_check:
  permanent_deletion_detected: false
  deleted_files_count: 0
  deleted_files: []
```

## Protected / Canonical / Source-of-Truth Diff Check

```yaml
protected_canonical_source_of_truth_diff_check:
  protected_files_changed: false
  canonical_files_changed: false
  source_of_truth_files_changed: false
  protected_or_canonical_changes_authorized_by_m82_m83: not_applicable
  trusted_checkpoint_evidence_present_if_required: not_required
  changed_protected_canonical_items: []
```

## Forbidden Artifact / Downstream Artifact Check

```yaml
forbidden_downstream_artifact_check:
  m83_validation_summary_created: false
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

## Diff Summary

```yaml
m83_reduction_diff_summary:
  physical_reduction_performed: false
  files_archived: false
  files_compressed: false
  files_merged: false
  files_deleted: false
  files_moved: false
  files_renamed: false
  reference_updates_performed: false
  protected_artifacts_modified: false
  scripts_modified: false
  ci_modified: false
  schemas_modified: false
  validation_authority_modified: false
  changed_files_total: 0
  expected_changed_files_total: 0
  unexpected_changed_files_total: 0
  forbidden_changed_files_total: 0
  diff_summary_result: "BLOCKED"
```

## Carry-Forward From M83.4

```yaml
warnings_from_m83_4_carried_forward: true
unknowns_from_m83_4_carried_forward: true
gaps_from_m83_4_carried_forward: true
not_claimed_metrics_from_m83_4_carried_forward: true
blocking_items_from_m83_4_carried_forward: true
carry_forward_items_hidden: false
```

## Local M83.5 Status

```yaml
M83_5_STATUS: M83_5_REDUCTION_DIFF_SUMMARY_BLOCKED
may_prepare_83_6_validation_summary: false
```
