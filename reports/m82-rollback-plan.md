# M82 Rollback & Validation Plan

## M82.4 Intake

```yaml
m82_4_status_detected: "M82_4_HUMAN_CHECKPOINT_PLAN_COMPLETE_WITH_WARNINGS"
m82_4_status_acceptable: true
m82_4_may_prepare_82_5_detected: true_with_warnings
m82_5_rollback_validation_plan_allowed: true_with_warnings
```

## Rollback Plan

```yaml
rollback_plan:
  rollback_plan_exists: true
  rollback_items:
    - candidate_id: "M82-CAND-001"
      path: "reports/m82-*"
      proposed_action: "keep_active"
      candidate_class_from_m82_1: "KEEP_ACTIVE"
      protection_status_from_m82_2: "not_protected"
      checkpoint_requirement_from_m82_4: "not_required"
      rollback_path_exists: false
      rollback_path: null
      rollback_method: "no physical change"
      rollback_validation_command: null
      rollback_blocks_m83_if_missing: true
      rollback_ready_for_m82_6_consideration: true
      notes: "Active task execution context."

    - candidate_id: "M82-CAND-002"
      path: "reports/m81-*"
      proposed_action: "keep_reference"
      candidate_class_from_m82_1: "KEEP_REFERENCE"
      protection_status_from_m82_2: "protected"
      checkpoint_requirement_from_m82_4: "required"
      rollback_path_exists: false
      rollback_path: null
      rollback_method: "no physical change"
      rollback_validation_command: null
      rollback_blocks_m83_if_missing: true
      rollback_ready_for_m82_6_consideration: true
      notes: "Protected evidence trace."

    - candidate_id: "M82-CAND-003"
      path: "reports/m80-* reports/m79-*"
      proposed_action: "block"
      candidate_class_from_m82_1: "UNKNOWN_BLOCKED"
      protection_status_from_m82_2: "unknown"
      checkpoint_requirement_from_m82_4: "required"
      rollback_path_exists: false
      rollback_path: null
      rollback_method: "blocked"
      rollback_validation_command: null
      rollback_blocks_m83_if_missing: true
      rollback_ready_for_m82_6_consideration: true
      notes: "Blocked from physical change."

    - candidate_id: "M82-CAND-004"
      path: "docs/*"
      proposed_action: "block"
      candidate_class_from_m82_1: "UNKNOWN_BLOCKED"
      protection_status_from_m82_2: "unknown"
      checkpoint_requirement_from_m82_4: "required"
      rollback_path_exists: false
      rollback_path: null
      rollback_method: "blocked"
      rollback_validation_command: null
      rollback_blocks_m83_if_missing: true
      rollback_ready_for_m82_6_consideration: true
      notes: "Blocked from physical change."

    - candidate_id: "M82-CAND-005"
      path: "scripts/* schemas/* .github/* bootstrap files adapter files"
      proposed_action: "block"
      candidate_class_from_m82_1: "PROTECTED_DO_NOT_TOUCH"
      protection_status_from_m82_2: "protected"
      checkpoint_requirement_from_m82_4: "required"
      rollback_path_exists: false
      rollback_path: null
      rollback_method: "blocked"
      rollback_validation_command: null
      rollback_blocks_m83_if_missing: true
      rollback_ready_for_m82_6_consideration: true
      notes: "Strictly protected."

  rollback_plan_status: "COMPLETE_WITH_WARNINGS"
```

## Post-Change Validation Plan

```yaml
post_change_validation_plan:
  validation_plan_exists: true
  validation_items:
    - candidate_id: "M82-CAND-001"
      path: "reports/m82-*"
      proposed_action: "keep_active"
      validation_after_change_exists: false
      validation_type: "no_physical_change"
      validation_after_change: []
      expected_validation_result: "Files remain as is."
      not_run_handling: "NOT_RUN remains NOT_RUN and must not become PASS"
      validation_blocks_m83_if_missing: true
      validation_ready_for_m82_6_consideration: true
      notes: "Active context."

    - candidate_id: "M82-CAND-002"
      path: "reports/m81-*"
      proposed_action: "keep_reference"
      validation_after_change_exists: false
      validation_type: "no_physical_change"
      validation_after_change: []
      expected_validation_result: "Files remain as is."
      not_run_handling: "NOT_RUN remains NOT_RUN and must not become PASS"
      validation_blocks_m83_if_missing: true
      validation_ready_for_m82_6_consideration: true
      notes: "Protected artifact."

    - candidate_id: "M82-CAND-003"
      path: "reports/m80-* reports/m79-*"
      proposed_action: "block"
      validation_after_change_exists: false
      validation_type: "blocked"
      validation_after_change: []
      expected_validation_result: "Files remain as is."
      not_run_handling: "NOT_RUN remains NOT_RUN and must not become PASS"
      validation_blocks_m83_if_missing: true
      validation_ready_for_m82_6_consideration: true
      notes: "Blocked candidate."

    - candidate_id: "M82-CAND-004"
      path: "docs/*"
      proposed_action: "block"
      validation_after_change_exists: false
      validation_type: "blocked"
      validation_after_change: []
      expected_validation_result: "Files remain as is."
      not_run_handling: "NOT_RUN remains NOT_RUN and must not become PASS"
      validation_blocks_m83_if_missing: true
      validation_ready_for_m82_6_consideration: true
      notes: "Blocked candidate."

    - candidate_id: "M82-CAND-005"
      path: "scripts/* schemas/* .github/* bootstrap files adapter files"
      proposed_action: "block"
      validation_after_change_exists: false
      validation_type: "blocked"
      validation_after_change: []
      expected_validation_result: "Files remain as is."
      not_run_handling: "NOT_RUN remains NOT_RUN and must not become PASS"
      validation_blocks_m83_if_missing: true
      validation_ready_for_m82_6_consideration: true
      notes: "Strictly protected."
```

## Rollback / Validation Readiness Matrix

```yaml
rollback_validation_readiness_matrix:
  - candidate_id: "M82-CAND-001"
    path: "reports/m82-*"
    rollback_ready: true
    validation_ready: true
    checkpoint_requirement_known: true
    protected_or_unknown_blocked: false
    may_be_considered_by_m82_6: true
    physical_change_allowed_in_m83_after_rollback_validation_review: false
    blocker_codes: []

  - candidate_id: "M82-CAND-002"
    path: "reports/m81-*"
    rollback_ready: true
    validation_ready: true
    checkpoint_requirement_known: true
    protected_or_unknown_blocked: true
    may_be_considered_by_m82_6: true
    physical_change_allowed_in_m83_after_rollback_validation_review: false
    blocker_codes: []

  - candidate_id: "M82-CAND-003"
    path: "reports/m80-* reports/m79-*"
    rollback_ready: true
    validation_ready: true
    checkpoint_requirement_known: true
    protected_or_unknown_blocked: true
    may_be_considered_by_m82_6: true
    physical_change_allowed_in_m83_after_rollback_validation_review: false
    blocker_codes: []

  - candidate_id: "M82-CAND-004"
    path: "docs/*"
    rollback_ready: true
    validation_ready: true
    checkpoint_requirement_known: true
    protected_or_unknown_blocked: true
    may_be_considered_by_m82_6: true
    physical_change_allowed_in_m83_after_rollback_validation_review: false
    blocker_codes: []

  - candidate_id: "M82-CAND-005"
    path: "scripts/* schemas/* .github/* bootstrap files adapter files"
    rollback_ready: true
    validation_ready: true
    checkpoint_requirement_known: true
    protected_or_unknown_blocked: true
    may_be_considered_by_m82_6: true
    physical_change_allowed_in_m83_after_rollback_validation_review: false
    blocker_codes: []
```

## Rollback / Validation Coverage

```yaml
rollback_validation_coverage:
  candidate_inventory_found: true
  total_candidates_from_prior_reports: 5
  candidates_with_rollback_item: 5
  candidates_with_validation_item: 5
  candidates_missing_rollback_item: 0
  candidates_missing_validation_item: 0
  all_candidates_covered: true
```

## Rollback / Validation Summary

```yaml
rollback_validation_summary:
  total_candidates_reviewed: 5
  rollback_ready_count: 5
  rollback_missing_count: 0
  validation_ready_count: 5
  validation_missing_count: 0
  no_physical_change_candidates_count: 2
  blocked_candidates_count: 3
  may_be_considered_by_m82_6_count: 5
  physical_change_allowed_in_m83_after_rollback_validation_review_count: 0
  rollback_plan_complete: true
  validation_plan_complete: true
```

## Carry-Forward From M82.4

```yaml
warnings_from_m82_4_carried_forward: true
unknowns_from_m82_4_carried_forward: true
gaps_from_m82_4_carried_forward: true
not_claimed_metrics_from_m82_4_carried_forward: true
blocking_items_from_m82_4_carried_forward: true
carry_forward_items_hidden: false
```

## Premature Artifact Check

```yaml
premature_artifact_check:
  m82_completion_review_created: false
  m83_artifacts_created: false
  m84_artifacts_created: false
  m85_artifacts_created: false
  m86_artifacts_created: false
  m87_artifacts_created: false
  m88_artifacts_created: false
  m91_artifacts_created: false
  validation_script_created_or_modified: false
  approval_artifact_created: false
  release_artifact_created: false
  lifecycle_mutation_artifact_created: false
  feature_work_artifact_created: false
  human_checkpoint_artifact_created: false
  physical_repo_change_performed: false
```

## Local M82.5 Status

```yaml
M82_5_STATUS: M82_5_ROLLBACK_VALIDATION_PLAN_COMPLETE_WITH_WARNINGS
may_prepare_82_6_unified_reduction_plan_assembly: true_with_warnings
```
