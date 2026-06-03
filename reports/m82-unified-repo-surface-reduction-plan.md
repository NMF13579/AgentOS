# M82 Unified Repo Surface Reduction Plan

## M81 Completion Intake

```yaml
m81_scope_lock_exists: true
m81_scope_lock_readable: true
m81_final_status_detected: "FINAL_STATUS: M81_SCOPE_LOCK_COMPLETE_WITH_WARNINGS"
m81_final_status_acceptable: true
m81_may_prepare_m82_detected: true_with_warnings
m81_may_prepare_m82_acceptable: true
m81_physical_changes_authorized: false
m81_feature_work_authorized: false
m81_m82_execution_authorized: false
m81_validation_script_created: false
m81_validation_script_modified: false
m81_scope_lock_contradictory: false
m82_0_intake_result: "PASS_WITH_WARNINGS"
may_prepare_82_1_candidate_inventory: true_with_warnings
blocker_codes: []
```

## M81 Contradiction Check

```yaml
m81_contradiction_check:
  multiple_final_statuses_detected: false
  acceptable_status_with_may_prepare_m82_false_detected: false
  physical_change_authorized_despite_scope_lock: false
  feature_work_authorized_despite_scope_lock: false
  m82_execution_authorized_despite_boundary: false
  validator_script_claim_conflict_detected: false
  downstream_artifact_conflict_detected: false
  carry_forward_conflict_detected: false
  contradiction_detected: false
```

## M81 Carry-Forward Review

```yaml
warnings_from_m81_carried_forward: true
unknowns_from_m81_carried_forward: true
gaps_from_m81_carried_forward: true
not_claimed_metrics_from_m81_carried_forward: true
blocking_items_from_m81_carried_forward: false
carry_forward_items_hidden: false

carry_forward_trace:
  warnings:
    - source_path: "reports/m81-scope-lock.md"
      source_section_or_field: "Carry-Forward From M81.0"
      source_item_id: "M80_7_WARNINGS_CARRIED_FORWARD"
      carried_to_path: "reports/m82-unified-repo-surface-reduction-plan.md"
      carried_to_section_or_field: "M81 Carry-Forward Review"
      disposition: "carried_forward"
      evidence_path: null
      notes: "Carried forward from M81 to M82."
    - source_path: "reports/m81-scope-lock.md"
      source_section_or_field: "Carry-Forward From M81.0"
      source_item_id: "M80_6_WARNINGS_CARRIED_FORWARD"
      carried_to_path: "reports/m82-unified-repo-surface-reduction-plan.md"
      carried_to_section_or_field: "M81 Carry-Forward Review"
      disposition: "carried_forward"
      evidence_path: null
      notes: "Carried forward from M81 to M82."
    - source_path: "reports/m81-scope-lock.md"
      source_section_or_field: "Carry-Forward From M81.0"
      source_item_id: "M80_5_WARNINGS_CARRIED_FORWARD"
      carried_to_path: "reports/m82-unified-repo-surface-reduction-plan.md"
      carried_to_section_or_field: "M81 Carry-Forward Review"
      disposition: "carried_forward"
      evidence_path: null
      notes: "Carried forward from M81 to M82."
    - source_path: "reports/m81-scope-lock.md"
      source_section_or_field: "Carry-Forward From M81.0"
      source_item_id: "M80_4_WARNINGS_CARRIED_FORWARD"
      carried_to_path: "reports/m82-unified-repo-surface-reduction-plan.md"
      carried_to_section_or_field: "M81 Carry-Forward Review"
      disposition: "carried_forward"
      evidence_path: null
      notes: "Carried forward from M81 to M82."
    - source_path: "reports/m81-scope-lock.md"
      source_section_or_field: "Carry-Forward From M81.0"
      source_item_id: "M80_3_WARNINGS_CARRIED_FORWARD"
      carried_to_path: "reports/m82-unified-repo-surface-reduction-plan.md"
      carried_to_section_or_field: "M81 Carry-Forward Review"
      disposition: "carried_forward"
      evidence_path: null
      notes: "Carried forward from M81 to M82."
    - source_path: "reports/m81-scope-lock.md"
      source_section_or_field: "Carry-Forward From M81.0"
      source_item_id: "M80_2_WARNINGS_CARRIED_FORWARD"
      carried_to_path: "reports/m82-unified-repo-surface-reduction-plan.md"
      carried_to_section_or_field: "M81 Carry-Forward Review"
      disposition: "carried_forward"
      evidence_path: null
      notes: "Carried forward from M81 to M82."
    - source_path: "reports/m81-scope-lock.md"
      source_section_or_field: "Carry-Forward From M81.0"
      source_item_id: "M80_1_WARNINGS_CARRIED_FORWARD"
      carried_to_path: "reports/m82-unified-repo-surface-reduction-plan.md"
      carried_to_section_or_field: "M81 Carry-Forward Review"
      disposition: "carried_forward"
      evidence_path: null
      notes: "Carried forward from M81 to M82."
    - source_path: "reports/m81-scope-lock.md"
      source_section_or_field: "Carry-Forward From M81.0"
      source_item_id: "M79_WARNINGS_CARRIED_FORWARD"
      carried_to_path: "reports/m82-unified-repo-surface-reduction-plan.md"
      carried_to_section_or_field: "M81 Carry-Forward Review"
      disposition: "carried_forward"
      evidence_path: null
      notes: "Carried forward from M81 to M82."
    - source_path: "reports/m81-scope-lock.md"
      source_section_or_field: "Carry-Forward From M81.0"
      source_item_id: "M80_COMPLETE_WITH_WARNINGS"
      carried_to_path: "reports/m82-unified-repo-surface-reduction-plan.md"
      carried_to_section_or_field: "M81 Carry-Forward Review"
      disposition: "carried_forward"
      evidence_path: null
      notes: "Carried forward from M81 to M82."
    - source_path: "reports/m81-scope-lock.md"
      source_section_or_field: "Carry-Forward From M81.0"
      source_item_id: "OPERATOR_RC_PLANNING_POSSIBLE_WITH_WARNINGS"
      carried_to_path: "reports/m82-unified-repo-surface-reduction-plan.md"
      carried_to_section_or_field: "M81 Carry-Forward Review"
      disposition: "carried_forward"
      evidence_path: null
      notes: "Carried forward from M81 to M82."
    - source_path: "reports/m81-scope-lock.md"
      source_section_or_field: "Carry-Forward From M81.0"
      source_item_id: "REMAINING_WARNINGS_VISIBLE"
      carried_to_path: "reports/m82-unified-repo-surface-reduction-plan.md"
      carried_to_section_or_field: "M81 Carry-Forward Review"
      disposition: "carried_forward"
      evidence_path: null
      notes: "Carried forward from M81 to M82."
    - source_path: "reports/m81-scope-lock.md"
      source_section_or_field: "Carry-Forward From M81.0"
      source_item_id: "REMAINING_UNKNOWNS_VISIBLE"
      carried_to_path: "reports/m82-unified-repo-surface-reduction-plan.md"
      carried_to_section_or_field: "M81 Carry-Forward Review"
      disposition: "carried_forward"
      evidence_path: null
      notes: "Carried forward from M81 to M82."
    - source_path: "reports/m81-scope-lock.md"
      source_section_or_field: "Carry-Forward From M81.0"
      source_item_id: "NOT_CLAIMED_METRICS_VISIBLE"
      carried_to_path: "reports/m82-unified-repo-surface-reduction-plan.md"
      carried_to_section_or_field: "M81 Carry-Forward Review"
      disposition: "carried_forward"
      evidence_path: null
      notes: "Carried forward from M81 to M82."
    - source_path: "reports/m81-scope-lock.md"
      source_section_or_field: "Carry-Forward From M81.0"
      source_item_id: "REMAINING_GAPS_VISIBLE"
      carried_to_path: "reports/m82-unified-repo-surface-reduction-plan.md"
      carried_to_section_or_field: "M81 Carry-Forward Review"
      disposition: "carried_forward"
      evidence_path: null
      notes: "Carried forward from M81 to M82."
    - source_path: "reports/m81-scope-lock.md"
      source_section_or_field: "Carry-Forward From M81.0"
      source_item_id: "HUMAN_REVIEW_REQUIREMENTS_VISIBLE"
      carried_to_path: "reports/m82-unified-repo-surface-reduction-plan.md"
      carried_to_section_or_field: "M81 Carry-Forward Review"
      disposition: "carried_forward"
      evidence_path: null
      notes: "Carried forward from M81 to M82."
    - source_path: "reports/m81-scope-lock.md"
      source_section_or_field: "Carry-Forward From M81.0"
      source_item_id: "VALIDATION_AUTHORITY_WARNINGS_VISIBLE"
      carried_to_path: "reports/m82-unified-repo-surface-reduction-plan.md"
      carried_to_section_or_field: "M81 Carry-Forward Review"
      disposition: "carried_forward"
      evidence_path: null
      notes: "Carried forward from M81 to M82."
    - source_path: "reports/m81-scope-lock.md"
      source_section_or_field: "Carry-Forward From M81.0"
      source_item_id: "SOURCE_OF_TRUTH_WARNINGS_VISIBLE"
      carried_to_path: "reports/m82-unified-repo-surface-reduction-plan.md"
      carried_to_section_or_field: "M81 Carry-Forward Review"
      disposition: "carried_forward"
      evidence_path: null
      notes: "Carried forward from M81 to M82."
    - source_path: "reports/m81-scope-lock.md"
      source_section_or_field: "Carry-Forward From M81.0"
      source_item_id: "DERIVED_CACHE_WARNINGS_VISIBLE"
      carried_to_path: "reports/m82-unified-repo-surface-reduction-plan.md"
      carried_to_section_or_field: "M81 Carry-Forward Review"
      disposition: "carried_forward"
      evidence_path: null
      notes: "Carried forward from M81 to M82."
    - source_path: "reports/m81-scope-lock.md"
      source_section_or_field: "Carry-Forward From M81.0"
      source_item_id: "GIT_STATUS_HAS_UNRELATED_CHANGES"
      carried_to_path: "reports/m82-unified-repo-surface-reduction-plan.md"
      carried_to_section_or_field: "M81 Carry-Forward Review"
      disposition: "carried_forward"
      evidence_path: null
      notes: "Carried forward from M81 to M82."

  unknowns:
    - source_path: "reports/m81-scope-lock.md"
      source_section_or_field: "Carry-Forward From M81.0"
      source_item_id: "Unknowns remain visible across the chain."
      carried_to_path: "reports/m82-unified-repo-surface-reduction-plan.md"
      carried_to_section_or_field: "M81 Carry-Forward Review"
      disposition: "carried_forward"
      evidence_path: null
      notes: "Carried forward from M81 to M82."

  gaps:
    - source_path: "reports/m81-scope-lock.md"
      source_section_or_field: "Carry-Forward From M81.0"
      source_item_id: "Remaining gaps remain visible."
      carried_to_path: "reports/m82-unified-repo-surface-reduction-plan.md"
      carried_to_section_or_field: "M81 Carry-Forward Review"
      disposition: "carried_forward"
      evidence_path: null
      notes: "Carried forward from M81 to M82."
    - source_path: "reports/m81-scope-lock.md"
      source_section_or_field: "Carry-Forward From M81.0"
      source_item_id: "Human review requirements remain visible."
      carried_to_path: "reports/m82-unified-repo-surface-reduction-plan.md"
      carried_to_section_or_field: "M81 Carry-Forward Review"
      disposition: "carried_forward"
      evidence_path: null
      notes: "Carried forward from M81 to M82."

  not_claimed_metrics:
    - source_path: "reports/m81-scope-lock.md"
      source_section_or_field: "Carry-Forward From M81.0"
      source_item_id: "Not-claimed metrics remain visible across the chain."
      carried_to_path: "reports/m82-unified-repo-surface-reduction-plan.md"
      carried_to_section_or_field: "M81 Carry-Forward Review"
      disposition: "carried_forward"
      evidence_path: null
      notes: "Carried forward from M81 to M82."

  blocking_items: []
```

## Boundary Reflection

```yaml
m81_boundary_reflection:
  m82_preparation_allowed: true_with_warnings
  m82_execution_authorized: false
  m83_physical_changes_authorized: false
  feature_work_authorized: false
  approval_created: false
  release_created: false
  lifecycle_mutation_created: false
```

## M82.0 Local Status

```yaml
M82_0_STATUS: M82_0_INTAKE_PASS_WITH_WARNINGS
m82_0_intake_result: "PASS_WITH_WARNINGS"
may_prepare_82_1_candidate_inventory: true_with_warnings
```

## Repo Surface Candidate Inventory

```yaml
surface_reduction_candidates:
  - candidate_id: "M82-CAND-001"
    path: "reports/m82-*"
    action_type: "keep_active"
    candidate_class: "KEEP_ACTIVE"
    candidate_confidence: "high"
    source_evidence:
      - "reports/m81-scope-lock.md"
    protected_or_canonical: false
    protected_or_canonical_reason: "Current execution context, active."
    human_checkpoint_required: false
    human_checkpoint_exists: false
    human_checkpoint_path: null
    rollback_path_exists: false
    rollback_path: null
    validation_after_change_exists: false
    validation_after_change: []
    meaning_preservation_requirements:
      invariants_preserved: unknown
      failure_semantics_preserved: unknown
      human_checkpoint_requirements_preserved: unknown
      approval_boundary_preserved: unknown
      evidence_trace_preserved: unknown
      source_of_truth_role_preserved: unknown
      information_that_must_not_be_lost:
        - "unknown pending M82.3"
      compression_invariant_preserved: unknown
      archive_safe_without_losing_evidence: unknown
    physical_change_allowed_in_m83: false
    m83_action_precondition_summary:
      - "Requires M82.2 protected artifact review."
      - "Requires M82.3 meaning preservation requirements."
      - "Requires M82.4 human checkpoint plan if applicable."
      - "Requires M82.5 rollback and validation plan."
    notes: "Active task state."

  - candidate_id: "M82-CAND-002"
    path: "reports/m81-*"
    action_type: "keep_reference"
    candidate_class: "KEEP_REFERENCE"
    candidate_confidence: "high"
    source_evidence:
      - "reports/m81-scope-lock.md"
    protected_or_canonical: true
    protected_or_canonical_reason: "Recent evidence chain."
    human_checkpoint_required: false
    human_checkpoint_exists: false
    human_checkpoint_path: null
    rollback_path_exists: false
    rollback_path: null
    validation_after_change_exists: false
    validation_after_change: []
    meaning_preservation_requirements:
      invariants_preserved: unknown
      failure_semantics_preserved: unknown
      human_checkpoint_requirements_preserved: unknown
      approval_boundary_preserved: unknown
      evidence_trace_preserved: unknown
      source_of_truth_role_preserved: unknown
      information_that_must_not_be_lost:
        - "unknown pending M82.3"
      compression_invariant_preserved: unknown
      archive_safe_without_losing_evidence: unknown
    physical_change_allowed_in_m83: false
    m83_action_precondition_summary:
      - "Requires M82.2 protected artifact review."
      - "Requires M82.3 meaning preservation requirements."
      - "Requires M82.4 human checkpoint plan if applicable."
      - "Requires M82.5 rollback and validation plan."
    notes: "Requires preservation as recent context."

  - candidate_id: "M82-CAND-003"
    path: "reports/m80-* reports/m79-*"
    action_type: "block"
    candidate_class: "UNKNOWN_BLOCKED"
    candidate_confidence: "unknown"
    source_evidence:
      - "reports/m81-scope-lock.md"
    protected_or_canonical: unknown
    protected_or_canonical_reason: "Needs review in M82.2."
    human_checkpoint_required: true
    human_checkpoint_exists: false
    human_checkpoint_path: null
    rollback_path_exists: false
    rollback_path: null
    validation_after_change_exists: false
    validation_after_change: []
    meaning_preservation_requirements:
      invariants_preserved: unknown
      failure_semantics_preserved: unknown
      human_checkpoint_requirements_preserved: unknown
      approval_boundary_preserved: unknown
      evidence_trace_preserved: unknown
      source_of_truth_role_preserved: unknown
      information_that_must_not_be_lost:
        - "unknown pending M82.3"
      compression_invariant_preserved: unknown
      archive_safe_without_losing_evidence: unknown
    physical_change_allowed_in_m83: false
    m83_action_precondition_summary:
      - "Requires M82.2 protected artifact review."
      - "Requires M82.3 meaning preservation requirements."
      - "Requires M82.4 human checkpoint plan if applicable."
      - "Requires M82.5 rollback and validation plan."
    notes: "Older evidence. Unknown canonical status."

  - candidate_id: "M82-CAND-004"
    path: "docs/*"
    action_type: "block"
    candidate_class: "UNKNOWN_BLOCKED"
    candidate_confidence: "unknown"
    source_evidence:
      - "reports/m81-scope-lock.md"
    protected_or_canonical: unknown
    protected_or_canonical_reason: "Needs review in M82.2."
    human_checkpoint_required: true
    human_checkpoint_exists: false
    human_checkpoint_path: null
    rollback_path_exists: false
    rollback_path: null
    validation_after_change_exists: false
    validation_after_change: []
    meaning_preservation_requirements:
      invariants_preserved: unknown
      failure_semantics_preserved: unknown
      human_checkpoint_requirements_preserved: unknown
      approval_boundary_preserved: unknown
      evidence_trace_preserved: unknown
      source_of_truth_role_preserved: unknown
      information_that_must_not_be_lost:
        - "unknown pending M82.3"
      compression_invariant_preserved: unknown
      archive_safe_without_losing_evidence: unknown
    physical_change_allowed_in_m83: false
    m83_action_precondition_summary:
      - "Requires M82.2 protected artifact review."
      - "Requires M82.3 meaning preservation requirements."
      - "Requires M82.4 human checkpoint plan if applicable."
      - "Requires M82.5 rollback and validation plan."
    notes: "Unknown documentation scope."

  - candidate_id: "M82-CAND-005"
    path: "scripts/* schemas/* .github/* bootstrap files adapter files"
    action_type: "block"
    candidate_class: "PROTECTED_DO_NOT_TOUCH"
    candidate_confidence: "high"
    source_evidence:
      - "reports/m81-scope-lock.md"
    protected_or_canonical: true
    protected_or_canonical_reason: "Forbidden from physical change by M81 boundaries."
    human_checkpoint_required: true
    human_checkpoint_exists: false
    human_checkpoint_path: null
    rollback_path_exists: false
    rollback_path: null
    validation_after_change_exists: false
    validation_after_change: []
    meaning_preservation_requirements:
      invariants_preserved: unknown
      failure_semantics_preserved: unknown
      human_checkpoint_requirements_preserved: unknown
      approval_boundary_preserved: unknown
      evidence_trace_preserved: unknown
      source_of_truth_role_preserved: unknown
      information_that_must_not_be_lost:
        - "unknown pending M82.3"
      compression_invariant_preserved: unknown
      archive_safe_without_losing_evidence: unknown
    physical_change_allowed_in_m83: false
    m83_action_precondition_summary:
      - "Requires M82.2 protected artifact review."
      - "Requires M82.3 meaning preservation requirements."
      - "Requires M82.4 human checkpoint plan if applicable."
      - "Requires M82.5 rollback and validation plan."
    notes: "Strictly protected."
```

## Candidate Classification Summary

```yaml
candidate_classification_summary:
  total_candidates_count: 5
  keep_active_count: 1
  keep_reference_count: 1
  archive_candidate_count: 0
  compression_candidate_count: 0
  merge_candidate_count: 0
  protected_do_not_touch_count: 1
  unknown_blocked_count: 2
  post_m87_review_count: 0
  physical_change_allowed_in_m83_count: 0
  candidate_inventory_complete: true
```

## Carry-Forward From M82.0

```yaml
warnings_from_m82_0_carried_forward: true
unknowns_from_m82_0_carried_forward: true
gaps_from_m82_0_carried_forward: true
not_claimed_metrics_from_m82_0_carried_forward: true
blocking_items_from_m82_0_carried_forward: true
carry_forward_items_hidden: false
```
The carry-forward items for M82.0 were inspected and no additional source items were found beyond the M81 carry-forwards preserved directly.

## Premature Artifact Check

```yaml
premature_artifact_check:
  m82_protected_artifact_review_created: false
  m82_human_checkpoint_plan_created: false
  m82_rollback_plan_created: false
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
```

## M82.1 Local Status

```yaml
M82_1_STATUS: M82_1_CANDIDATE_INVENTORY_COMPLETE_WITH_WARNINGS
may_prepare_82_2_protected_artifact_review: true_with_warnings
```

## M82.2 Intake

```yaml
m82_2_status_detected: "M82_2_PROTECTED_ARTIFACT_REVIEW_COMPLETE_WITH_WARNINGS"
m82_2_status_acceptable: true
m82_2_may_prepare_82_3_detected: true_with_warnings
m82_3_meaning_preservation_allowed: true_with_warnings
```

## Meaning Preservation Coverage

```yaml
meaning_preservation_coverage:
  candidate_inventory_found: true
  total_candidates_from_m82_1: 5
  candidates_with_meaning_preservation_requirements: 5
  candidates_missing_meaning_preservation_requirements: 0
  all_candidates_covered: true
```

## Candidate Meaning Preservation Matrix

```yaml
candidate_meaning_preservation_matrix:
  - candidate_id: "M82-CAND-001"
    path: "reports/m82-*"
    candidate_class_from_m82_1: "KEEP_ACTIVE"
    protection_status_from_m82_2: "not_protected"
    proposed_action_type: "keep_active"
    meaning_preservation_requirements:
      invariants_preserved: unknown
      failure_semantics_preserved: unknown
      human_checkpoint_requirements_preserved: unknown
      approval_boundary_preserved: unknown
      evidence_trace_preserved: unknown
      source_of_truth_role_preserved: unknown
      bootstrap_context_preserved: unknown
      validation_authority_preserved: unknown
      lifecycle_boundary_preserved: unknown
      security_boundary_preserved: unknown
      information_that_must_not_be_lost:
        - "Active M82 execution context."
      compression_invariant_preserved: unknown
      archive_safe_without_losing_evidence: unknown
      merge_safe_without_creating_new_source_of_truth: unknown
    non_physical_preservation_requirements:
      reason_for_no_physical_change: "Remains active context for the current milestone."
      preservation_risk: "low"
      future_review_needed: false
    physical_change_allowed_in_m83_after_meaning_review: false
    preservation_blocker_codes:
      - "INVARIANTS_NOT_PRESERVED"
    notes: "Remains active. No physical change proposed."

  - candidate_id: "M82-CAND-002"
    path: "reports/m81-*"
    candidate_class_from_m82_1: "KEEP_REFERENCE"
    protection_status_from_m82_2: "protected"
    proposed_action_type: "keep_reference"
    meaning_preservation_requirements:
      invariants_preserved: unknown
      failure_semantics_preserved: unknown
      human_checkpoint_requirements_preserved: unknown
      approval_boundary_preserved: unknown
      evidence_trace_preserved: unknown
      source_of_truth_role_preserved: unknown
      bootstrap_context_preserved: unknown
      validation_authority_preserved: unknown
      lifecycle_boundary_preserved: unknown
      security_boundary_preserved: unknown
      information_that_must_not_be_lost:
        - "M81 evidence trace must be fully preserved."
      compression_invariant_preserved: unknown
      archive_safe_without_losing_evidence: unknown
      merge_safe_without_creating_new_source_of_truth: unknown
    non_physical_preservation_requirements:
      reason_for_no_physical_change: "Requires preservation as recent M81 context and evidence."
      preservation_risk: "low"
      future_review_needed: false
    physical_change_allowed_in_m83_after_meaning_review: false
    preservation_blocker_codes:
      - "EVIDENCE_TRACE_NOT_PRESERVED"
    notes: "Protected artifact. No physical change proposed."

  - candidate_id: "M82-CAND-003"
    path: "reports/m80-* reports/m79-*"
    candidate_class_from_m82_1: "UNKNOWN_BLOCKED"
    protection_status_from_m82_2: "unknown"
    proposed_action_type: "block"
    meaning_preservation_requirements:
      invariants_preserved: unknown
      failure_semantics_preserved: unknown
      human_checkpoint_requirements_preserved: unknown
      approval_boundary_preserved: unknown
      evidence_trace_preserved: unknown
      source_of_truth_role_preserved: unknown
      bootstrap_context_preserved: unknown
      validation_authority_preserved: unknown
      lifecycle_boundary_preserved: unknown
      security_boundary_preserved: unknown
      information_that_must_not_be_lost:
        - "Older evidence trace must not be lost."
      compression_invariant_preserved: unknown
      archive_safe_without_losing_evidence: unknown
      merge_safe_without_creating_new_source_of_truth: unknown
    non_physical_preservation_requirements:
      reason_for_no_physical_change: "Blocked due to unknown protection status."
      preservation_risk: "unknown"
      future_review_needed: true
    physical_change_allowed_in_m83_after_meaning_review: false
    preservation_blocker_codes:
      - "ARCHIVE_EVIDENCE_SAFETY_UNKNOWN_OR_FALSE"
    notes: "Blocked due to unknown protection status."

  - candidate_id: "M82-CAND-004"
    path: "docs/*"
    candidate_class_from_m82_1: "UNKNOWN_BLOCKED"
    protection_status_from_m82_2: "unknown"
    proposed_action_type: "block"
    meaning_preservation_requirements:
      invariants_preserved: unknown
      failure_semantics_preserved: unknown
      human_checkpoint_requirements_preserved: unknown
      approval_boundary_preserved: unknown
      evidence_trace_preserved: unknown
      source_of_truth_role_preserved: unknown
      bootstrap_context_preserved: unknown
      validation_authority_preserved: unknown
      lifecycle_boundary_preserved: unknown
      security_boundary_preserved: unknown
      information_that_must_not_be_lost:
        - "Canonical and governance documentation must be preserved."
      compression_invariant_preserved: unknown
      archive_safe_without_losing_evidence: unknown
      merge_safe_without_creating_new_source_of_truth: unknown
    non_physical_preservation_requirements:
      reason_for_no_physical_change: "Blocked due to unknown individual canonical status."
      preservation_risk: "unknown"
      future_review_needed: true
    physical_change_allowed_in_m83_after_meaning_review: false
    preservation_blocker_codes:
      - "SOURCE_OF_TRUTH_ROLE_NOT_PRESERVED"
    notes: "Blocked due to unknown individual canonical status."

  - candidate_id: "M82-CAND-005"
    path: "scripts/* schemas/* .github/* bootstrap files adapter files"
    candidate_class_from_m82_1: "PROTECTED_DO_NOT_TOUCH"
    protection_status_from_m82_2: "protected"
    proposed_action_type: "block"
    meaning_preservation_requirements:
      invariants_preserved: unknown
      failure_semantics_preserved: unknown
      human_checkpoint_requirements_preserved: unknown
      approval_boundary_preserved: unknown
      evidence_trace_preserved: unknown
      source_of_truth_role_preserved: unknown
      bootstrap_context_preserved: unknown
      validation_authority_preserved: unknown
      lifecycle_boundary_preserved: unknown
      security_boundary_preserved: unknown
      information_that_must_not_be_lost:
        - "Strict canonical behavior, scripts, schemas, and CI boundaries."
      compression_invariant_preserved: unknown
      archive_safe_without_losing_evidence: unknown
      merge_safe_without_creating_new_source_of_truth: unknown
    non_physical_preservation_requirements:
      reason_for_no_physical_change: "Strictly protected authority files."
      preservation_risk: "low"
      future_review_needed: false
    physical_change_allowed_in_m83_after_meaning_review: false
    preservation_blocker_codes:
      - "VALIDATION_AUTHORITY_NOT_PRESERVED"
    notes: "Strictly protected. Cannot be changed."
```

## Protected / Unknown Candidate Handling

```yaml
protected_meaning_handling:
  protected_candidates_count: 2
  unknown_protection_candidates_count: 2
  protected_candidates_kept_blocked: true
  unknown_protection_candidates_kept_blocked: true
```

## Meaning Preservation Summary

```yaml
meaning_preservation_summary:
  total_candidates_reviewed: 5
  candidates_with_all_preservation_dimensions_true: 0
  candidates_with_unknown_preservation_dimensions: 5
  candidates_with_false_preservation_dimensions: 0
  protected_candidates_kept_blocked: true
  unknown_candidates_kept_blocked: true
  physical_change_allowed_in_m83_after_meaning_review_count: 0
  meaning_preservation_requirements_complete: true
```

## Carry-Forward From M82.2

```yaml
warnings_from_m82_2_carried_forward: true
unknowns_from_m82_2_carried_forward: true
gaps_from_m82_2_carried_forward: true
not_claimed_metrics_from_m82_2_carried_forward: true
blocking_items_from_m82_2_carried_forward: true
carry_forward_items_hidden: false
```

## Premature Artifact Check

```yaml
premature_artifact_check:
  m82_human_checkpoint_plan_created: false
  m82_rollback_plan_created: false
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
```

## M82.3 Local Status

```yaml
M82_3_STATUS: M82_3_MEANING_PRESERVATION_REQUIREMENTS_COMPLETE_WITH_WARNINGS
may_prepare_82_4_human_checkpoint_plan: true_with_warnings
```

## M82.5 Intake

```yaml
m82_5_status_detected: "M82_5_ROLLBACK_VALIDATION_PLAN_COMPLETE_WITH_WARNINGS"
m82_5_status_acceptable: true
m82_5_may_prepare_82_6_detected: true_with_warnings
m82_6_unified_plan_assembly_allowed: true_with_warnings
```

## Unified Reduction Plan Assembly

```yaml
m82_assembly_source_reports:
  unified_plan_exists: true
  unified_plan_readable: true
  protected_artifact_review_exists: true
  protected_artifact_review_readable: true
  human_checkpoint_plan_exists: true
  human_checkpoint_plan_readable: true
  rollback_plan_exists: true
  rollback_plan_readable: true
```

## Final Candidate Eligibility Matrix

```yaml
final_candidate_eligibility_matrix:
  - candidate_id: "M82-CAND-001"
    path: "reports/m82-*"
    action_type: "keep_active"
    candidate_class_from_m82_1: "KEEP_ACTIVE"
    protection_status_from_m82_2: "not_protected"
    meaning_preservation_status_from_m82_3: "complete_with_warnings"
    checkpoint_status_from_m82_4: "not_required"
    rollback_status_from_m82_5: "not_required"
    validation_status_from_m82_5: "not_required"
    final_candidate_class: "KEEP_ACTIVE"
    m83_consideration_allowed: true
    physical_change_allowed_in_m83: false
    m83_consideration_preconditions:
      - "No physical change authorized."
    final_blocker_codes: []
    notes: "Active context."

  - candidate_id: "M82-CAND-002"
    path: "reports/m81-*"
    action_type: "keep_reference"
    candidate_class_from_m82_1: "KEEP_REFERENCE"
    protection_status_from_m82_2: "protected"
    meaning_preservation_status_from_m82_3: "complete_with_warnings"
    checkpoint_status_from_m82_4: "required_missing"
    rollback_status_from_m82_5: "not_required"
    validation_status_from_m82_5: "not_required"
    final_candidate_class: "KEEP_REFERENCE"
    m83_consideration_allowed: false
    physical_change_allowed_in_m83: false
    m83_consideration_preconditions:
      - "Checkpoint missing."
    final_blocker_codes:
      - "MISSING_CHECKPOINT_MARKED_ACTIONABLE"
    notes: "Protected artifact, checkpoint missing."

  - candidate_id: "M82-CAND-003"
    path: "reports/m80-* reports/m79-*"
    action_type: "block"
    candidate_class_from_m82_1: "UNKNOWN_BLOCKED"
    protection_status_from_m82_2: "unknown"
    meaning_preservation_status_from_m82_3: "complete_with_warnings"
    checkpoint_status_from_m82_4: "required_missing"
    rollback_status_from_m82_5: "blocked"
    validation_status_from_m82_5: "blocked"
    final_candidate_class: "UNKNOWN_BLOCKED"
    m83_consideration_allowed: false
    physical_change_allowed_in_m83: false
    m83_consideration_preconditions:
      - "Unknown protection status."
    final_blocker_codes:
      - "UNKNOWN_PROTECTION_CANDIDATE_MARKED_ACTIONABLE"
    notes: "Blocked."

  - candidate_id: "M82-CAND-004"
    path: "docs/*"
    action_type: "block"
    candidate_class_from_m82_1: "UNKNOWN_BLOCKED"
    protection_status_from_m82_2: "unknown"
    meaning_preservation_status_from_m82_3: "complete_with_warnings"
    checkpoint_status_from_m82_4: "required_missing"
    rollback_status_from_m82_5: "blocked"
    validation_status_from_m82_5: "blocked"
    final_candidate_class: "UNKNOWN_BLOCKED"
    m83_consideration_allowed: false
    physical_change_allowed_in_m83: false
    m83_consideration_preconditions:
      - "Unknown canonical status."
    final_blocker_codes:
      - "UNKNOWN_PROTECTION_CANDIDATE_MARKED_ACTIONABLE"
    notes: "Blocked."

  - candidate_id: "M82-CAND-005"
    path: "scripts/* schemas/* .github/* bootstrap files adapter files"
    action_type: "block"
    candidate_class_from_m82_1: "PROTECTED_DO_NOT_TOUCH"
    protection_status_from_m82_2: "protected"
    meaning_preservation_status_from_m82_3: "complete_with_warnings"
    checkpoint_status_from_m82_4: "required_missing"
    rollback_status_from_m82_5: "blocked"
    validation_status_from_m82_5: "blocked"
    final_candidate_class: "PROTECTED_DO_NOT_TOUCH"
    m83_consideration_allowed: false
    physical_change_allowed_in_m83: false
    m83_consideration_preconditions:
      - "Strict canonical protection."
    final_blocker_codes:
      - "PROTECTED_CANDIDATE_MARKED_ACTIONABLE_WITHOUT_TRUSTED_CHECKPOINT"
    notes: "Strictly protected."
```

## M83 Consideration Boundary

M82.6 may identify candidates that M83 may consider under strict preconditions.

M82.6 does not authorize M83 execution.

M82.6 does not perform physical repo changes.

M82.6 does not approve archival, compression, merge, deletion, move, rename, or edit operations.

M83 must perform its own execution intake, pre-write checks, diff summary, validation, and completion review before any physical reduction can be accepted.

```yaml
m83_consideration_boundary:
  m83_consideration_allowed_for_some_candidates: true
  m83_execution_authorized: false
  physical_repo_changes_performed: false
  physical_repo_changes_approved: false
  deletion_authorized: false
  move_authorized: false
  rename_authorized: false
  archive_authorized_for_execution: false
  compression_authorized_for_execution: false
  merge_authorized_for_execution: false
```

## Unified Plan Summary

```yaml
m82_unified_plan:
  candidate_inventory_complete: true
  protected_artifact_review_complete: true
  meaning_preservation_requirements_defined: true
  human_checkpoint_plan_exists: true
  rollback_plan_exists: true
  validation_after_change_requirements_defined: true
  total_candidates_count: 5
  actionable_candidates_for_m83_consideration_count: 0
  blocked_candidates_count: 3
  protected_do_not_touch_count: 1
  unknown_blocked_count: 2
  post_m87_review_count: 0
  keep_active_count: 1
  keep_reference_count: 1
  archive_candidate_count: 0
  compression_candidate_count: 0
  merge_candidate_count: 0
  physical_change_plan_exists: true
  m83_execution_authorized: false
```

## Carry-Forward From M82.5

```yaml
warnings_from_m82_5_carried_forward: true
unknowns_from_m82_5_carried_forward: true
gaps_from_m82_5_carried_forward: true
not_claimed_metrics_from_m82_5_carried_forward: true
blocking_items_from_m82_5_carried_forward: true
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

## M82.6 Local Status

```yaml
M82_6_STATUS: M82_6_UNIFIED_REDUCTION_PLAN_ASSEMBLED_WITH_WARNINGS
may_prepare_82_7_completion_review: true_with_warnings
```
