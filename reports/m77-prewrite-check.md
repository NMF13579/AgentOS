## Human Summary
- Can next M77 task be prepared: true_with_warnings
- Does this block M78 preparation: true
- Main blockers:
  - none
- Main warnings:
  - M77_3_WARNINGS_CARRIED_FORWARD, M77_2_WARNINGS_CARRIED_FORWARD, M77_1_WARNINGS_CARRIED_FORWARD, M76_WARNINGS_CARRIED_FORWARD, PREWRITE_ELIGIBILITY_PROVISIONAL, BLOCKED_ITEMS_PRESENT, UNKNOWN_BLOCKED_ITEMS_PRESENT, PROTECTED_DO_NOT_TOUCH_ITEMS_PRESENT, CHECKPOINT_REQUIRED_ITEMS_PRESENT, M80_DERIVED_UPDATE_CANDIDATES_PRESENT, NON_BLOCKING_M76_CONTRADICTIONS_CARRIED_FORWARD
- Human checkpoint required: true
- Cleanup authorized: false
- Physical cleanup performed: false
- Next readiness field: "may_prepare_m77_5: true_with_warnings"

## Title
- Task: `77.4 - Prewrite Check`
- Mode: read-only prewrite verification / provisional execution eligibility check

## Purpose
This report checks every cleanup plan item from 77.3 and records whether it is structurally eligible for future M78 consideration. Eligibility is provisional and does not replace rollback confirmation in 77.5.

## 77.3 Cleanup Plan Draft Check
- `reports/m77-cleanup-plan.md` exists and is readable.
- `m77_3_final_status_detected: "M77_CLEANUP_PLAN_DRAFT_COMPLETE_WITH_WARNINGS"
- `m77_3_final_status_acceptable: true
- `m77_3_readiness_detected: "true_with_warnings"
- `m77_3_readiness_acceptable: true

## 77.2 Protected Artifact Review Check
- `reports/m77-protected-artifact-review.md` exists and is readable.
- `m77_2_final_status_detected: "M77_PROTECTED_ARTIFACT_REVIEW_COMPLETE_WITH_WARNINGS"
- `m77_2_final_status_acceptable: true
- `m77_2_readiness_detected: "true_with_warnings"
- `m77_2_readiness_acceptable: true

## 77.1 Classification Review Check
- `reports/m77-classification-review.md` exists and is readable.
- `m77_1_final_status_detected: "M77_CLASSIFICATION_REVIEW_COMPLETE_WITH_WARNINGS"
- `m77_1_final_status_acceptable: true
- `m77_1_readiness_detected: "true_with_warnings"
- `m77_1_readiness_acceptable: true

## M76 Source Inputs Checked
- `reports/m76-cleanup-candidate-inventory.md` exists and is readable.
- `reports/m76-optimization-risk-map.md` exists and is readable.
- `reports/m76-human-checkpoint-plan.md` exists and is readable.
- `reports/m76-optimization-scope-lock.md` exists and is readable.
- `reports/m76-completion-review.md` exists and is readable.

## Prewrite Check Method
- Keep M76 findings intact.
- Treat prewrite eligibility as provisional.
- Require rollback confirmation later in 77.5 before any final M78 readiness decision.
- Mark items blocked whenever validation is not read-only, protection is unclear, or the cleanup plan template is incomplete.

## Prewrite / Rollback Dependency Boundary
- 77.4 is not final M78 readiness.
- 77.5 still has to confirm rollback readiness.
- If 77.5 later blocks rollback, the item cannot advance to final M78 readiness.

## Cleanup Item Template Check
- `cleanup_item_template_checked: true`
- `cleanup_item_template_missing_required_field_count: 0`
- `cleanup_item_template_complete: true`

## Target Path Check
- `target_path_exact_count: 56`
- `target_path_missing_or_unclear_count: 2`
- The two missing-or-unclear targets are `scripts/check-human-approval.py` and `scripts/check-lifecycle-mutation.py`, which were not present in the working tree during verification.

## Planned Action Check
- The planned actions are preserved from 77.3.
- `defer_to_m80` is used only for the wave 5 derived/navigation items.
- No action is upgraded from planning metadata to execution permission.

## Source Evidence Check
- `source_evidence_present_count: 58`
- `source_evidence_missing_count: 0`

## Validation Command Check
- `validation_command_present_count: 58`
- `validation_command_missing_count: 0`
- Ten items use `python3 -m py_compile`, which is not read-only, so those items are blocked from prewrite eligibility.

## Rollback Field Presence Check
- `rollback_plan_present_count: 58`
- `rollback_plan_missing_count: 0`
- `rollback_validation_command_present_count: 58`
- `rollback_validation_command_missing_count: 0`

## Human Checkpoint Requirement Check
- `human_checkpoint_required_item_count: 50`
- `checkpoint_requirement_missing_for_high_risk_count: 0`

## Protected Hard Stop Check
- `protected_items_referenced_in_cleanup_plan_count: 6`
- `protected_items_with_checkpoint_requirement_count: 0`
- `protected_items_blocked_do_not_touch_count: 6`
- Protected canonical items remain blocked do-not-touch.

## Protected Checkpoint / Block Coverage Check
- `protected_checkpoint_coverage_complete_for_prewrite: true`

## UNKNOWN Handling Check
- The unknown-blocked item stays blocked and is not promoted to M78 eligibility.
- Unknown does not become low risk.

## Wave Consistency Check
- Every item preserves its 77.1 wave assignment.
- No wave change is used to lower risk.

## Wave 5 / M80 Deferred Check
- The two wave 5 items remain M80-only deferred and are not executable in M78.

## M76 Non-Override Review
- `m76_findings_overridden: false`
- `m76_contradictions_detected: true`
- `m76_contradictions_resolved_by_agent: false`
- `m76_contradiction_count: 2`
- `m76_contradiction_register_complete: true`

## M76 Contradiction Register
- `M77-CONTRADICTION-001` stays attached to `M76-CAND-051`.
- `M77-CONTRADICTION-002` stays attached to `M76-CAND-052`.
- Both remain carried forward for human review, not resolved by agent judgment.

## Full Prewrite Results
- `M78_ELIGIBLE_LOW_RISK: 6`
- `M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT: 33`
- `M80_ONLY_DERIVED_UPDATE_CANDIDATE: 2`
- `BLOCKED_UNKNOWN: 1`
- `BLOCKED_PROTECTED_DO_NOT_TOUCH: 6`
- `BLOCKED_INSUFFICIENT_ROLLBACK: 0`
- `BLOCKED_INSUFFICIENT_VALIDATION: 10`
- `BLOCKED_SCOPE_OR_EVIDENCE: 0`
- `BLOCKED_WAVE_INCONSISTENCY: 0`
- `BLOCKED_M76_OVERRIDE: 0`
- `BLOCKED_HUMAN_SUMMARY_MISMATCH: 0`
- `BLOCKED_WAVE_5_NOT_M78_EXECUTABLE: 0`
- `BLOCKED_M76_CONTRADICTION_UNREGISTERED: 0`
- `BLOCKED_CLEANUP_ITEM_TEMPLATE_MISSING_FIELD: 0`
- `BLOCKED_PROTECTED_CHECKPOINT_COVERAGE_INCOMPLETE: 0`

## Provisional M78 Eligibility Summary
- `6` items are structurally eligible at low risk.
- `33` items are structurally eligible only after human checkpoint.
- `2` items are M80-only deferred derived/navigation items.
- `1` item stays blocked as unknown.
- `10` items are blocked because validation is not read-only.
- `6` items remain blocked do-not-touch.

## Cleanup Authorization Boundary
- This report does not authorize cleanup.
- It does not authorize deletion, archiving, consolidation, or bootstrap compression.
- It only records provisional structural eligibility.

## Premature Artifact Check
- `downstream_m77_artifacts_exist: false`
- `m78_artifacts_exist: false`
- `m80_artifacts_exist: false`
- `m81_artifacts_exist: false`
- `m81_task_briefs_exist: false`

## Boundary Check
- `protected_m76_item_marked_m78_eligible: false`
- `wave_5_derived_item_marked_m78_executable: false`
- `m80_artifact_created_by_77_4: false`
- `cleanup_authorized_by_77_4: false`
- `physical_cleanup_occurred: false`
- `prewrite_check_created: true`
- `rollback_plan_created: false`
- `human_checkpoint_requirements_created: false`
- `m77_completion_review_created: false`
- `m78_started: false`
- `m80_started: false`
- `m81_started: false`

## Blockers
- `blocker_codes:`
  - `none`

## Warnings
- `warning_codes:`
  - `M77_3_WARNINGS_CARRIED_FORWARD`
  - `M77_2_WARNINGS_CARRIED_FORWARD`
  - `M77_1_WARNINGS_CARRIED_FORWARD`
  - `M76_WARNINGS_CARRIED_FORWARD`
  - `PREWRITE_ELIGIBILITY_PROVISIONAL`
  - `BLOCKED_ITEMS_PRESENT`
  - `UNKNOWN_BLOCKED_ITEMS_PRESENT`
  - `PROTECTED_DO_NOT_TOUCH_ITEMS_PRESENT`
  - `CHECKPOINT_REQUIRED_ITEMS_PRESENT`
  - `M80_DERIVED_UPDATE_CANDIDATES_PRESENT`
  - `NON_BLOCKING_M76_CONTRADICTIONS_CARRIED_FORWARD`

## Local Final Status
- `FINAL_STATUS: "M77_PREWRITE_CHECK_COMPLETE_WITH_WARNINGS"`

## Readiness for 77.5
- `may_prepare_m77_5: "true_with_warnings"`

## Final Boundary Statement
This report only checks provisional prewrite eligibility.
It does not authorize cleanup, does not create rollback or checkpoint artifacts, and does not start M78, M80, or M81.
Human review remains required.

### Machine-Readable Metadata
```yaml
task_id: "77.4"
task_name: "Prewrite Check"
reports_directory_exists: true
input_file: "reports/m77-cleanup-plan.md"
m77_3_cleanup_plan_exists: true
m77_3_cleanup_plan_readable: true
m77_3_final_status_detected: "M77_CLEANUP_PLAN_DRAFT_COMPLETE_WITH_WARNINGS"
m77_3_final_status_acceptable: true
m77_3_readiness_detected: "true_with_warnings"
m77_3_readiness_acceptable: true
m77_2_protected_artifact_review_exists: true
m77_2_protected_artifact_review_readable: true
m77_1_classification_review_exists: true
m77_1_classification_review_readable: true
m76_candidate_inventory_exists: true
m76_risk_map_exists: true
m76_human_checkpoint_plan_exists: true
m76_scope_lock_exists: true
m76_completion_review_exists: true
prewrite_check_created: true
prewrite_eligibility_is_provisional: true
rollback_confirmation_required_in_77_5: true
cleanup_plan_item_count: 58
prewrite_item_count: 58
m78_eligible_low_risk_count: 6
m78_eligible_after_human_checkpoint_count: 33
m80_only_deferred_candidate_count: 2
blocked_unknown_count: 1
blocked_protected_do_not_touch_count: 6
blocked_insufficient_rollback_count: 0
blocked_insufficient_validation_count: 10
blocked_scope_or_evidence_count: 0
blocked_wave_inconsistency_count: 0
blocked_m76_override_count: 0
blocked_human_summary_mismatch_count: 0
blocked_wave_5_not_m78_executable_count: 0
blocked_m76_contradiction_unregistered_count: 0
blocked_cleanup_item_template_missing_field_count: 0
blocked_protected_checkpoint_coverage_incomplete_count: 0
cleanup_item_template_checked: true
cleanup_item_template_missing_required_field_count: 0
cleanup_item_template_complete: true
target_path_exact_count: 56
target_path_missing_or_unclear_count: 2
source_evidence_present_count: 58
source_evidence_missing_count: 0
validation_command_present_count: 58
validation_command_missing_count: 0
rollback_plan_present_count: 58
rollback_plan_missing_count: 0
rollback_validation_command_present_count: 58
rollback_validation_command_missing_count: 0
human_checkpoint_required_item_count: 50
checkpoint_requirement_missing_for_high_risk_count: 0
protected_items_referenced_in_cleanup_plan_count: 6
protected_items_with_checkpoint_requirement_count: 0
protected_items_blocked_do_not_touch_count: 6
protected_checkpoint_coverage_complete_for_prewrite: true
m76_findings_overridden: false
m76_contradictions_detected: true
m76_contradictions_resolved_by_agent: false
m76_contradiction_count: 2
m76_contradiction_register_complete: true
protected_m76_item_marked_m78_eligible: false
wave_5_derived_item_marked_m78_executable: false
m80_artifact_created_by_77_4: false
cleanup_authorized_by_77_4: false
physical_cleanup_occurred: false
files_deleted: false
files_moved: false
files_renamed: false
files_archived: false
files_compressed: false
scripts_consolidated: false
docs_compressed: false
rollback_plan_created: false
human_checkpoint_requirements_created: false
m77_completion_review_created: false
m78_artifacts_created: false
m78_started: false
m80_artifacts_created: false
m80_started: false
m81_artifacts_created: false
m81_task_briefs_created: false
m81_started: false
human_summary_consistent_with_machine_fields: true
blocker_codes:
  - "none"
warning_codes:
  - "M77_3_WARNINGS_CARRIED_FORWARD"
  - "M77_2_WARNINGS_CARRIED_FORWARD"
  - "M77_1_WARNINGS_CARRIED_FORWARD"
  - "M76_WARNINGS_CARRIED_FORWARD"
  - "PREWRITE_ELIGIBILITY_PROVISIONAL"
  - "BLOCKED_ITEMS_PRESENT"
  - "UNKNOWN_BLOCKED_ITEMS_PRESENT"
  - "PROTECTED_DO_NOT_TOUCH_ITEMS_PRESENT"
  - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
  - "M80_DERIVED_UPDATE_CANDIDATES_PRESENT"
  - "NON_BLOCKING_M76_CONTRADICTIONS_CARRIED_FORWARD"
FINAL_STATUS: "M77_PREWRITE_CHECK_COMPLETE_WITH_WARNINGS"
may_prepare_m77_5: "true_with_warnings"
```

### Prewrite Results
```yaml
prewrite_results:
  - cleanup_plan_item_id: "M77-CLEANUP-001"
    candidate_id: "M76-CAND-001"
    target_path: "scripts/__pycache__/agent-complete.cpython-314.pyc"
    planned_action: "delete"
    risk_class_from_m76: "LOW_RISK_CLEANUP"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_LOW_RISK"
    prewrite_result: "M78_ELIGIBLE_LOW_RISK"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "not_required"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "none"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-002"
    candidate_id: "M76-CAND-002"
    target_path: "scripts/__pycache__/agent-fail.cpython-314.pyc"
    planned_action: "delete"
    risk_class_from_m76: "LOW_RISK_CLEANUP"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_LOW_RISK"
    prewrite_result: "M78_ELIGIBLE_LOW_RISK"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "not_required"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "none"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-003"
    candidate_id: "M76-CAND-003"
    target_path: "scripts/__pycache__/agent-next.cpython-314.pyc"
    planned_action: "delete"
    risk_class_from_m76: "LOW_RISK_CLEANUP"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_LOW_RISK"
    prewrite_result: "M78_ELIGIBLE_LOW_RISK"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "not_required"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "none"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-004"
    candidate_id: "M76-CAND-004"
    target_path: "scripts/__pycache__/generate-task-contract.cpython-314.pyc"
    planned_action: "delete"
    risk_class_from_m76: "LOW_RISK_CLEANUP"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_LOW_RISK"
    prewrite_result: "M78_ELIGIBLE_LOW_RISK"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "not_required"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "none"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-005"
    candidate_id: "M76-CAND-005"
    target_path: "scripts/__pycache__/validate-task.cpython-314.pyc"
    planned_action: "delete"
    risk_class_from_m76: "LOW_RISK_CLEANUP"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_LOW_RISK"
    prewrite_result: "M78_ELIGIBLE_LOW_RISK"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "not_required"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "none"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-006"
    candidate_id: "M76-CAND-006"
    target_path: "scripts/__pycache__/validate-verification.cpython-314.pyc"
    planned_action: "delete"
    risk_class_from_m76: "LOW_RISK_CLEANUP"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_LOW_RISK"
    prewrite_result: "M78_ELIGIBLE_LOW_RISK"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "not_required"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "none"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-007"
    candidate_id: "M76-CAND-007"
    target_path: "scripts/audit-m27 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-008"
    candidate_id: "M76-CAND-008"
    target_path: "scripts/audit-m27-level1 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-009"
    candidate_id: "M76-CAND-009"
    target_path: "scripts/audit-metadata-consistency 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-010"
    candidate_id: "M76-CAND-010"
    target_path: "scripts/audit-pre-merge-corridor 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-011"
    candidate_id: "M76-CAND-011"
    target_path: "scripts/audit-validation-integration 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-012"
    candidate_id: "M76-CAND-012"
    target_path: "scripts/build-index 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-013"
    candidate_id: "M76-CAND-013"
    target_path: "scripts/check-commit-push-preconditions 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-014"
    candidate_id: "M76-CAND-014"
    target_path: "scripts/check-github-platform-enforcement 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-015"
    candidate_id: "M76-CAND-015"
    target_path: "scripts/check-pre-merge-scope 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-016"
    candidate_id: "M76-CAND-016"
    target_path: "scripts/check-scope-compliance 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-017"
    candidate_id: "M76-CAND-017"
    target_path: "scripts/test-ci-advisory-config 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-018"
    candidate_id: "M76-CAND-018"
    target_path: "scripts/test-commit-push-preconditions-fixtures 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-019"
    candidate_id: "M76-CAND-019"
    target_path: "scripts/test-enforcement-fixtures 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-020"
    candidate_id: "M76-CAND-020"
    target_path: "scripts/test-m22-guardrails 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-021"
    candidate_id: "M76-CAND-021"
    target_path: "scripts/test-m27-level1-fixtures 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-022"
    candidate_id: "M76-CAND-022"
    target_path: "scripts/test-pre-merge-corridor-fixtures 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-023"
    candidate_id: "M76-CAND-023"
    target_path: "scripts/test-pre-merge-scope-fixtures 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-024"
    candidate_id: "M76-CAND-024"
    target_path: "scripts/test-scope-compliance-fixtures 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-025"
    candidate_id: "M76-CAND-025"
    target_path: "scripts/validate-boundary-claims 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-026"
    candidate_id: "M76-CAND-026"
    target_path: "scripts/validate-frontmatter 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-027"
    candidate_id: "M76-CAND-027"
    target_path: "scripts/validate-index 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-028"
    candidate_id: "M76-CAND-028"
    target_path: "scripts/validate-required-sections 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-029"
    candidate_id: "M76-CAND-029"
    target_path: "scripts/validate-status-semantics 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-030"
    candidate_id: "M76-CAND-030"
    target_path: "scripts/agent-complete.py"
    planned_action: "mark_legacy"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-031"
    candidate_id: "M76-CAND-031"
    target_path: "scripts/agent-fail.py"
    planned_action: "mark_legacy"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-032"
    candidate_id: "M76-CAND-032"
    target_path: "scripts/agent-next.py"
    planned_action: "mark_legacy"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-033"
    candidate_id: "M76-CAND-033"
    target_path: "scripts/agentos.py"
    planned_action: "mark_legacy"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-034"
    candidate_id: "M76-CAND-034"
    target_path: "scripts/run-active-task.py"
    planned_action: "mark_legacy"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-035"
    candidate_id: "M76-CAND-035"
    target_path: "HANDOFF 2.md"
    planned_action: "archive"
    risk_class_from_m76: "UNKNOWN_BLOCKED"
    m77_planning_class_from_77_3: "BLOCKED_UNKNOWN"
    prewrite_result: "BLOCKED_UNKNOWN"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "UNKNOWN_BLOCKED_ITEMS_PRESENT"
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-036"
    candidate_id: "M76-CAND-036"
    target_path: "llms.txt"
    planned_action: "compress"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-037"
    candidate_id: "M76-CAND-037"
    target_path: "AGENTS.md"
    planned_action: "compress"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-038"
    candidate_id: "M76-CAND-038"
    target_path: "CLAUDE.md"
    planned_action: "compress"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-039"
    candidate_id: "M76-CAND-039"
    target_path: "GEMINI.md"
    planned_action: "compress"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-040"
    candidate_id: "M76-CAND-040"
    target_path: "README.md"
    planned_action: "compress"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-041"
    candidate_id: "M76-CAND-041"
    target_path: "scripts/agentos-validate.py"
    planned_action: "consolidate"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "BLOCKED_INSUFFICIENT_VALIDATION"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "unclear_or_not_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "VALIDATION_COMMAND_NOT_READONLY"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-042"
    candidate_id: "M76-CAND-042"
    target_path: "scripts/check-dangerous-commands.py"
    planned_action: "consolidate"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "BLOCKED_INSUFFICIENT_VALIDATION"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "unclear_or_not_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "VALIDATION_COMMAND_NOT_READONLY"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-043"
    candidate_id: "M76-CAND-043"
    target_path: "scripts/check-execution-authorization.py"
    planned_action: "consolidate"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "BLOCKED_INSUFFICIENT_VALIDATION"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "unclear_or_not_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "VALIDATION_COMMAND_NOT_READONLY"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-044"
    candidate_id: "M76-CAND-044"
    target_path: "scripts/check-execution-readiness.py"
    planned_action: "consolidate"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "BLOCKED_INSUFFICIENT_VALIDATION"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "unclear_or_not_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "VALIDATION_COMMAND_NOT_READONLY"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-045"
    candidate_id: "M76-CAND-045"
    target_path: "scripts/check-human-approval.py"
    planned_action: "consolidate"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "BLOCKED_INSUFFICIENT_VALIDATION"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "missing_or_unclear"
    source_evidence_status: "present"
    validation_command_status: "unclear_or_not_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "VALIDATION_COMMAND_NOT_READONLY"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-046"
    candidate_id: "M76-CAND-046"
    target_path: "scripts/check-lifecycle-mutation.py"
    planned_action: "consolidate"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "BLOCKED_INSUFFICIENT_VALIDATION"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "missing_or_unclear"
    source_evidence_status: "present"
    validation_command_status: "unclear_or_not_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "VALIDATION_COMMAND_NOT_READONLY"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-047"
    candidate_id: "M76-CAND-047"
    target_path: "scripts/check-readiness-assertions.py"
    planned_action: "consolidate"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "BLOCKED_INSUFFICIENT_VALIDATION"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "unclear_or_not_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "VALIDATION_COMMAND_NOT_READONLY"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-048"
    candidate_id: "M76-CAND-048"
    target_path: "scripts/check-validator-authority-boundary.py"
    planned_action: "consolidate"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "BLOCKED_INSUFFICIENT_VALIDATION"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "unclear_or_not_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "VALIDATION_COMMAND_NOT_READONLY"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-049"
    candidate_id: "M76-CAND-049"
    target_path: "scripts/validate-lifecycle-apply.py"
    planned_action: "consolidate"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "BLOCKED_INSUFFICIENT_VALIDATION"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "unclear_or_not_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "VALIDATION_COMMAND_NOT_READONLY"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-050"
    candidate_id: "M76-CAND-050"
    target_path: "scripts/validate-task.py"
    planned_action: "consolidate"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class_from_77_3: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    prewrite_result: "BLOCKED_INSUFFICIENT_VALIDATION"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "unclear_or_not_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "VALIDATION_COMMAND_NOT_READONLY"
    warning_codes:
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-051"
    candidate_id: "M76-CAND-051"
    target_path: "reports/m71-script-inventory.json"
    planned_action: "defer_to_m80"
    risk_class_from_m76: "UNKNOWN_BLOCKED"
    m77_planning_class_from_77_3: "M80_ONLY_DERIVED_UPDATE_CANDIDATE"
    prewrite_result: "M80_ONLY_DERIVED_UPDATE_CANDIDATE"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "not_required"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "M77-CONTRADICTION-001"
    m80_only_deferred_candidate: true
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "M80_DERIVED_UPDATE_CANDIDATES_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-052"
    candidate_id: "M76-CAND-052"
    target_path: "repo-map.md"
    planned_action: "defer_to_m80"
    risk_class_from_m76: "UNKNOWN_BLOCKED"
    m77_planning_class_from_77_3: "M80_ONLY_DERIVED_UPDATE_CANDIDATE"
    prewrite_result: "M80_ONLY_DERIVED_UPDATE_CANDIDATE"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "not_required"
    protected_hard_stop_status: "not_applicable"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "M77-CONTRADICTION-002"
    m80_only_deferred_candidate: true
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "M80_DERIVED_UPDATE_CANDIDATES_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-053"
    candidate_id: "M76-CAND-053"
    target_path: "ROUTES-REGISTRY.md"
    planned_action: "mark_legacy"
    risk_class_from_m76: "PROTECTED_DO_NOT_TOUCH"
    m77_planning_class_from_77_3: "BLOCKED_PROTECTED_DO_NOT_TOUCH"
    prewrite_result: "BLOCKED_PROTECTED_DO_NOT_TOUCH"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "enforced"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "PROTECTED_DO_NOT_TOUCH_ITEMS_PRESENT"
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-054"
    candidate_id: "M76-CAND-054"
    target_path: "core-rules/MAIN.md"
    planned_action: "mark_legacy"
    risk_class_from_m76: "PROTECTED_DO_NOT_TOUCH"
    m77_planning_class_from_77_3: "BLOCKED_PROTECTED_DO_NOT_TOUCH"
    prewrite_result: "BLOCKED_PROTECTED_DO_NOT_TOUCH"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "enforced"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "PROTECTED_DO_NOT_TOUCH_ITEMS_PRESENT"
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-055"
    candidate_id: "M76-CAND-055"
    target_path: "state/MAIN.md"
    planned_action: "mark_legacy"
    risk_class_from_m76: "PROTECTED_DO_NOT_TOUCH"
    m77_planning_class_from_77_3: "BLOCKED_PROTECTED_DO_NOT_TOUCH"
    prewrite_result: "BLOCKED_PROTECTED_DO_NOT_TOUCH"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "enforced"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "PROTECTED_DO_NOT_TOUCH_ITEMS_PRESENT"
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-056"
    candidate_id: "M76-CAND-056"
    target_path: "workflow/MAIN.md"
    planned_action: "mark_legacy"
    risk_class_from_m76: "PROTECTED_DO_NOT_TOUCH"
    m77_planning_class_from_77_3: "BLOCKED_PROTECTED_DO_NOT_TOUCH"
    prewrite_result: "BLOCKED_PROTECTED_DO_NOT_TOUCH"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "enforced"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "PROTECTED_DO_NOT_TOUCH_ITEMS_PRESENT"
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-057"
    candidate_id: "M76-CAND-057"
    target_path: "quality/MAIN.md"
    planned_action: "mark_legacy"
    risk_class_from_m76: "PROTECTED_DO_NOT_TOUCH"
    m77_planning_class_from_77_3: "BLOCKED_PROTECTED_DO_NOT_TOUCH"
    prewrite_result: "BLOCKED_PROTECTED_DO_NOT_TOUCH"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "enforced"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "PROTECTED_DO_NOT_TOUCH_ITEMS_PRESENT"
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-058"
    candidate_id: "M76-CAND-058"
    target_path: "security/MAIN.md"
    planned_action: "mark_legacy"
    risk_class_from_m76: "PROTECTED_DO_NOT_TOUCH"
    m77_planning_class_from_77_3: "BLOCKED_PROTECTED_DO_NOT_TOUCH"
    prewrite_result: "BLOCKED_PROTECTED_DO_NOT_TOUCH"
    prewrite_eligibility_is_provisional: true
    rollback_confirmation_required_in_77_5: true
    target_path_status: "exact_exists"
    source_evidence_status: "present"
    validation_command_status: "present_readonly"
    rollback_plan_field_status: "present"
    rollback_validation_command_field_status: "present"
    human_checkpoint_requirement_status: "required_present"
    protected_hard_stop_status: "enforced"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_4: false
    physical_cleanup_performed: false
    blocker_codes:
      - "none"
    warning_codes:
      - "PROTECTED_DO_NOT_TOUCH_ITEMS_PRESENT"
      - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
    human_summary_consistent_with_machine_fields: true
```
