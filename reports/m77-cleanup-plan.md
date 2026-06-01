## Human Summary

- Can next M77 task be prepared: true_with_warnings
- Does this block M78 preparation: true
- Main blockers:
  - none
- Main warnings:
  - M77_2_WARNINGS_CARRIED_FORWARD, M77_1_WARNINGS_CARRIED_FORWARD, M76_WARNINGS_CARRIED_FORWARD, BLOCKED_ITEMS_PRESENT, PROTECTED_DO_NOT_TOUCH_ITEMS_PRESENT, CHECKPOINT_REQUIRED_ITEMS_PRESENT, M80_DERIVED_UPDATE_CANDIDATES_PRESENT, NON_BLOCKING_M76_CONTRADICTIONS_CARRIED_FORWARD
- Human checkpoint required: true
- Cleanup authorized: false
- Physical cleanup performed: false
- Next readiness field: "may_prepare_m77_4: true_with_warnings"

## Title
- Task: `77.3 - Cleanup Plan Draft`
- Mode: read-only cleanup planning / draft execution package

## Purpose
This report defines exact cleanup plan items for later review by 77.4 and 77.5.
It preserves M76 findings and keeps the draft separate from any cleanup authorization.

## 77.2 Protected Artifact Review Check
- `reports/m77-protected-artifact-review.md` exists and is readable.
- `m77_2_final_status_detected: "M77_PROTECTED_ARTIFACT_REVIEW_COMPLETE_WITH_WARNINGS"`
- `m77_2_readiness_detected: "true_with_warnings"`

## 77.1 Classification Review Check
- `reports/m77-classification-review.md` exists and is readable.
- `m77_1_final_status_detected: "M77_CLASSIFICATION_REVIEW_COMPLETE_WITH_WARNINGS"`
- `m77_1_readiness_detected: "true_with_warnings"`
- `m77_1_final_status_acceptable: true`
- `m77_1_readiness_acceptable: true`

## M76 Source Inputs Checked
- `reports/m76-cleanup-candidate-inventory.md` exists and is readable.
- `reports/m76-optimization-risk-map.md` exists and is readable.
- `reports/m76-human-checkpoint-plan.md` exists and is readable.
- `reports/m76-optimization-scope-lock.md` exists and is readable.
- `reports/m76-completion-review.md` exists and is readable.

## Cleanup Plan Draft Method
- Keep M76 classifications intact.
- Preserve execution wave from 77.1 unless the wave5 M80-deferred rule applies.
- Use the exact cleanup item template for every item.
- Treat this draft as planning only and not cleanup authorization.

## Cleanup Item Template Enforcement
- `cleanup_item_template_enforced: true`
- `cleanup_item_template_missing_required_field_count: 0`
- `cleanup_item_template_complete: true`

## M76 Non-Override Review
- `m76_findings_overridden: false`
- `m76_contradictions_detected: true`
- `m76_contradictions_resolved_by_agent: false`
- `m76_contradiction_count: 2`
- `m76_contradiction_register_complete: true`

## M76 Contradiction Register
- `M77-CONTRADICTION-001` for `M76-CAND-051` at `reports/m71-script-inventory.json`
- `M77-CONTRADICTION-002` for `M76-CAND-052` at `repo-map.md`
- Both remain deferred to M80 and are not executable cleanup items in this draft.

## Cleanup Plan Item Summary
- `cleanup_plan_draft_created: true`
- `cleanup_plan_item_count: 58`
- `wave_1_cache_noise_item_count: 6`
- `wave_2_stale_copy_item_count: 1`
- `wave_3_scripts_validation_item_count: 38`
- `wave_4_text_bootstrap_item_count: 11`
- `wave_5_derived_navigation_item_count: 2`

## Execution Wave Summary
- `wave_1_cache_noise`: 6
- `wave_2_stale_copy`: 1
- `wave_3_scripts_validation`: 38
- `wave_4_text_bootstrap`: 11
- `wave_5_derived_navigation`: 2

## Wave 1 Cache / Noise Items
- `M76-CAND-001` through `M76-CAND-006` are planned for deletion as cache noise.

## Wave 2 Stale / Copy Items
- `M76-CAND-035` is kept blocked pending clarification.

## Wave 3 Scripts / Validation Items
- `M76-CAND-007` through `M76-CAND-034` and `M76-CAND-041` through `M76-CAND-050` are planned for cleanup review with human checkpoint coverage.

## Wave 4 Text / Bootstrap / Adapter Items
- `M76-CAND-030` through `M76-CAND-040` and `M76-CAND-053` through `M76-CAND-058` cover bootstrap, adapter, and protected text artifacts.

## Wave 5 M80-Only Derived / Index Items
- `M76-CAND-051` and `M76-CAND-052` are deferred to M80 only.

## Protected Hard Stop Review
- No M76 `PROTECTED_DO_NOT_TOUCH` item is marked M78-eligible.
- Protected canonical items remain blocked do-not-touch.
- Wave 5 derived/index items remain M80-only and not M78-executable.

## Protected Checkpoint / Block Coverage Inputs
- `protected_items_referenced_in_cleanup_plan_count: 6`
- `protected_items_with_checkpoint_requirement_count: 0`
- `protected_items_blocked_do_not_touch_count: 6`
- `protected_checkpoint_coverage_complete_for_draft: true`

## Validation Command Coverage
- `validation_command_present_count: 58`
- `validation_command_missing_count: 0`

## Rollback Plan Coverage
- `rollback_plan_present_count: 58`
- `rollback_plan_missing_count: 0`
- `rollback_validation_command_present_count: 58`
- `rollback_validation_command_missing_count: 0`

## Human Checkpoint Requirement Coverage
- `human_checkpoint_required_item_count: 50`

## Cleanup Authorization Boundary
- `cleanup_authorized_by_77_3: false`
- `physical_cleanup_occurred: false`
- `files_deleted: false`
- `files_moved: false`
- `files_renamed: false`
- `files_archived: false`
- `files_compressed: false`
- `scripts_consolidated: false`
- `docs_compressed: false`

## Premature Artifact Check
- `downstream_m77_artifacts_exist: false`
- `m78_artifacts_exist: false`
- `m80_artifacts_exist: false`
- `m81_artifacts_exist: false`
- `m81_task_briefs_exist: false`

## Boundary Check
- `protected_m76_item_marked_m78_eligible: false`
- `wave_5_derived_item_marked_m78_executable: false`
- `m80_artifact_created_by_77_3: false`
- `cleanup_plan_draft_created: true`
- `cleanup_item_template_enforced: true`
- `cleanup_item_template_complete: true`
- `m76_findings_overridden: false`
- `m76_contradictions_resolved_by_agent: false`
- `prewrite_check_created: false`
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
  - `M77_2_WARNINGS_CARRIED_FORWARD`
  - `M77_1_WARNINGS_CARRIED_FORWARD`
  - `M76_WARNINGS_CARRIED_FORWARD`
  - `BLOCKED_ITEMS_PRESENT`
  - `PROTECTED_DO_NOT_TOUCH_ITEMS_PRESENT`
  - `CHECKPOINT_REQUIRED_ITEMS_PRESENT`
  - `M80_DERIVED_UPDATE_CANDIDATES_PRESENT`
  - `NON_BLOCKING_M76_CONTRADICTIONS_CARRIED_FORWARD`

## Local Final Status
- `FINAL_STATUS: "M77_CLEANUP_PLAN_DRAFT_COMPLETE_WITH_WARNINGS"`

## Readiness for 77.4
- `may_prepare_m77_4: "true_with_warnings"`

## Final Boundary Statement
This report only drafts cleanup planning items.
It does not authorize cleanup, does not create prewrite or rollback plans, and does not start M78, M80, or M81.
Human review remains required.

### Machine-Readable Metadata
```yaml
task_id: "77.3"
task_name: "Cleanup Plan Draft"
reports_directory_exists: true
input_file: "reports/m77-protected-artifact-review.md"

m77_2_protected_artifact_review_exists: true
m77_2_protected_artifact_review_readable: true
m77_2_final_status_detected: "M77_PROTECTED_ARTIFACT_REVIEW_COMPLETE_WITH_WARNINGS"
m77_2_final_status_acceptable: true
m77_2_readiness_detected: "true_with_warnings"
m77_2_readiness_acceptable: true

m77_1_classification_review_exists: true
m77_1_classification_review_readable: true

m76_candidate_inventory_exists: true
m76_risk_map_exists: true
m76_human_checkpoint_plan_exists: true
m76_scope_lock_exists: true
m76_completion_review_exists: true

cleanup_plan_draft_created: true
cleanup_plan_item_count: 58
cleanup_item_template_enforced: true
cleanup_item_template_missing_required_field_count: 0
cleanup_item_template_complete: true

wave_1_cache_noise_item_count: 6
wave_2_stale_copy_item_count: 1
wave_3_scripts_validation_item_count: 38
wave_4_text_bootstrap_item_count: 11
wave_5_derived_navigation_item_count: 2

m78_eligible_low_risk_count: 6
m78_eligible_after_human_checkpoint_count: 43
m80_only_deferred_candidate_count: 2
blocked_unknown_count: 1
blocked_protected_do_not_touch_count: 6
blocked_insufficient_rollback_count: 0
blocked_insufficient_validation_count: 0
blocked_scope_or_evidence_count: 0
blocked_wave_inconsistency_count: 0
blocked_m76_override_count: 0

validation_command_present_count: 58
validation_command_missing_count: 0
rollback_plan_present_count: 58
rollback_plan_missing_count: 0
rollback_validation_command_present_count: 58
rollback_validation_command_missing_count: 0

human_checkpoint_required_item_count: 50
protected_items_referenced_in_cleanup_plan_count: 6
protected_items_with_checkpoint_requirement_count: 0
protected_items_blocked_do_not_touch_count: 6
protected_checkpoint_coverage_complete_for_draft: true

m76_findings_overridden: false
m76_contradictions_detected: true
m76_contradictions_resolved_by_agent: false
m76_contradiction_count: 2
m76_contradiction_register_complete: true

protected_m76_item_marked_m78_eligible: false
wave_5_derived_item_marked_m78_executable: false
m80_artifact_created_by_77_3: false

cleanup_authorized_by_77_3: false
physical_cleanup_occurred: false
files_deleted: false
files_moved: false
files_renamed: false
files_archived: false
files_compressed: false
scripts_consolidated: false
docs_compressed: false

prewrite_check_created: false
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
  - "M77_2_WARNINGS_CARRIED_FORWARD"
  - "M77_1_WARNINGS_CARRIED_FORWARD"
  - "M76_WARNINGS_CARRIED_FORWARD"
  - "BLOCKED_ITEMS_PRESENT"
  - "PROTECTED_DO_NOT_TOUCH_ITEMS_PRESENT"
  - "CHECKPOINT_REQUIRED_ITEMS_PRESENT"
  - "M80_DERIVED_UPDATE_CANDIDATES_PRESENT"
  - "NON_BLOCKING_M76_CONTRADICTIONS_CARRIED_FORWARD"

m76_contradictions:
  - contradiction_id: "M77-CONTRADICTION-001"
    candidate_id: "M76-CAND-051"
    target_path: "reports/m71-script-inventory.json"
    m76_finding: "UNKNOWN_BLOCKED in the M76 risk map and scope lock"
    m77_finding: "M80_ONLY_DERIVED_UPDATE_CANDIDATE; planned_action defer_to_m80; execution_wave wave_5_derived_navigation"
    contradiction_type: "wave_assignment"
    resolution: "blocked"
    resolved_by_agent: false
    blocks_m78: true
  - contradiction_id: "M77-CONTRADICTION-002"
    candidate_id: "M76-CAND-052"
    target_path: "repo-map.md"
    m76_finding: "UNKNOWN_BLOCKED in the M76 risk map and scope lock"
    m77_finding: "M80_ONLY_DERIVED_UPDATE_CANDIDATE; planned_action defer_to_m80; execution_wave wave_5_derived_navigation"
    contradiction_type: "wave_assignment"
    resolution: "blocked"
    resolved_by_agent: false
    blocks_m78: true

cleanup_plan_items:
  - cleanup_plan_item_id: "M77-CLEANUP-001"
    candidate_id: "M76-CAND-001"
    target_path: "scripts/__pycache__/agent-complete.cpython-314.pyc"
    planned_action: "delete"
    risk_class_from_m76: "LOW_RISK_CLEANUP"
    m77_planning_class: "M78_ELIGIBLE_LOW_RISK"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Remove tracked bytecode cache noise from scripts/__pycache__."
    validation_command: "test ! -e "scripts/__pycache__/agent-complete.cpython-314.pyc""
    rollback_plan: "Restore the tracked file with git checkout -- "scripts/__pycache__/agent-complete.cpython-314.pyc"."
    rollback_validation_command: "test -f "scripts/__pycache__/agent-complete.cpython-314.pyc""
    human_checkpoint_required: false
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_1_cache_noise"
    execution_wave_current: "wave_1_cache_noise"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-002"
    candidate_id: "M76-CAND-002"
    target_path: "scripts/__pycache__/agent-fail.cpython-314.pyc"
    planned_action: "delete"
    risk_class_from_m76: "LOW_RISK_CLEANUP"
    m77_planning_class: "M78_ELIGIBLE_LOW_RISK"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Remove tracked bytecode cache noise from scripts/__pycache__."
    validation_command: "test ! -e "scripts/__pycache__/agent-fail.cpython-314.pyc""
    rollback_plan: "Restore the tracked file with git checkout -- "scripts/__pycache__/agent-fail.cpython-314.pyc"."
    rollback_validation_command: "test -f "scripts/__pycache__/agent-fail.cpython-314.pyc""
    human_checkpoint_required: false
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_1_cache_noise"
    execution_wave_current: "wave_1_cache_noise"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-003"
    candidate_id: "M76-CAND-003"
    target_path: "scripts/__pycache__/agent-next.cpython-314.pyc"
    planned_action: "delete"
    risk_class_from_m76: "LOW_RISK_CLEANUP"
    m77_planning_class: "M78_ELIGIBLE_LOW_RISK"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Remove tracked bytecode cache noise from scripts/__pycache__."
    validation_command: "test ! -e "scripts/__pycache__/agent-next.cpython-314.pyc""
    rollback_plan: "Restore the tracked file with git checkout -- "scripts/__pycache__/agent-next.cpython-314.pyc"."
    rollback_validation_command: "test -f "scripts/__pycache__/agent-next.cpython-314.pyc""
    human_checkpoint_required: false
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_1_cache_noise"
    execution_wave_current: "wave_1_cache_noise"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-004"
    candidate_id: "M76-CAND-004"
    target_path: "scripts/__pycache__/generate-task-contract.cpython-314.pyc"
    planned_action: "delete"
    risk_class_from_m76: "LOW_RISK_CLEANUP"
    m77_planning_class: "M78_ELIGIBLE_LOW_RISK"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Remove tracked bytecode cache noise from scripts/__pycache__."
    validation_command: "test ! -e "scripts/__pycache__/generate-task-contract.cpython-314.pyc""
    rollback_plan: "Restore the tracked file with git checkout -- "scripts/__pycache__/generate-task-contract.cpython-314.pyc"."
    rollback_validation_command: "test -f "scripts/__pycache__/generate-task-contract.cpython-314.pyc""
    human_checkpoint_required: false
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_1_cache_noise"
    execution_wave_current: "wave_1_cache_noise"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-005"
    candidate_id: "M76-CAND-005"
    target_path: "scripts/__pycache__/validate-task.cpython-314.pyc"
    planned_action: "delete"
    risk_class_from_m76: "LOW_RISK_CLEANUP"
    m77_planning_class: "M78_ELIGIBLE_LOW_RISK"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Remove tracked bytecode cache noise from scripts/__pycache__."
    validation_command: "test ! -e "scripts/__pycache__/validate-task.cpython-314.pyc""
    rollback_plan: "Restore the tracked file with git checkout -- "scripts/__pycache__/validate-task.cpython-314.pyc"."
    rollback_validation_command: "test -f "scripts/__pycache__/validate-task.cpython-314.pyc""
    human_checkpoint_required: false
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_1_cache_noise"
    execution_wave_current: "wave_1_cache_noise"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-006"
    candidate_id: "M76-CAND-006"
    target_path: "scripts/__pycache__/validate-verification.cpython-314.pyc"
    planned_action: "delete"
    risk_class_from_m76: "LOW_RISK_CLEANUP"
    m77_planning_class: "M78_ELIGIBLE_LOW_RISK"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Remove tracked bytecode cache noise from scripts/__pycache__."
    validation_command: "test ! -e "scripts/__pycache__/validate-verification.cpython-314.pyc""
    rollback_plan: "Restore the tracked file with git checkout -- "scripts/__pycache__/validate-verification.cpython-314.pyc"."
    rollback_validation_command: "test -f "scripts/__pycache__/validate-verification.cpython-314.pyc""
    human_checkpoint_required: false
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_1_cache_noise"
    execution_wave_current: "wave_1_cache_noise"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-007"
    candidate_id: "M76-CAND-007"
    target_path: "scripts/audit-m27 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Remove duplicate Finder-copied script or fixture file with no source-of-truth value."
    validation_command: "test ! -e "scripts/audit-m27 3.py""
    rollback_plan: "Restore the file from git history with git checkout -- "scripts/audit-m27 3.py"."
    rollback_validation_command: "test -f "scripts/audit-m27 3.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-008"
    candidate_id: "M76-CAND-008"
    target_path: "scripts/audit-m27-level1 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Remove duplicate Finder-copied script or fixture file with no source-of-truth value."
    validation_command: "test ! -e "scripts/audit-m27-level1 3.py""
    rollback_plan: "Restore the file from git history with git checkout -- "scripts/audit-m27-level1 3.py"."
    rollback_validation_command: "test -f "scripts/audit-m27-level1 3.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-009"
    candidate_id: "M76-CAND-009"
    target_path: "scripts/audit-metadata-consistency 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Remove duplicate Finder-copied script or fixture file with no source-of-truth value."
    validation_command: "test ! -e "scripts/audit-metadata-consistency 3.py""
    rollback_plan: "Restore the file from git history with git checkout -- "scripts/audit-metadata-consistency 3.py"."
    rollback_validation_command: "test -f "scripts/audit-metadata-consistency 3.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-010"
    candidate_id: "M76-CAND-010"
    target_path: "scripts/audit-pre-merge-corridor 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Remove duplicate Finder-copied script or fixture file with no source-of-truth value."
    validation_command: "test ! -e "scripts/audit-pre-merge-corridor 3.py""
    rollback_plan: "Restore the file from git history with git checkout -- "scripts/audit-pre-merge-corridor 3.py"."
    rollback_validation_command: "test -f "scripts/audit-pre-merge-corridor 3.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-011"
    candidate_id: "M76-CAND-011"
    target_path: "scripts/audit-validation-integration 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Remove duplicate Finder-copied script or fixture file with no source-of-truth value."
    validation_command: "test ! -e "scripts/audit-validation-integration 3.py""
    rollback_plan: "Restore the file from git history with git checkout -- "scripts/audit-validation-integration 3.py"."
    rollback_validation_command: "test -f "scripts/audit-validation-integration 3.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-012"
    candidate_id: "M76-CAND-012"
    target_path: "scripts/build-index 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Remove duplicate Finder-copied script or fixture file with no source-of-truth value."
    validation_command: "test ! -e "scripts/build-index 3.py""
    rollback_plan: "Restore the file from git history with git checkout -- "scripts/build-index 3.py"."
    rollback_validation_command: "test -f "scripts/build-index 3.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-013"
    candidate_id: "M76-CAND-013"
    target_path: "scripts/check-commit-push-preconditions 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Remove duplicate Finder-copied script or fixture file with no source-of-truth value."
    validation_command: "test ! -e "scripts/check-commit-push-preconditions 3.py""
    rollback_plan: "Restore the file from git history with git checkout -- "scripts/check-commit-push-preconditions 3.py"."
    rollback_validation_command: "test -f "scripts/check-commit-push-preconditions 3.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-014"
    candidate_id: "M76-CAND-014"
    target_path: "scripts/check-github-platform-enforcement 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Remove duplicate Finder-copied script or fixture file with no source-of-truth value."
    validation_command: "test ! -e "scripts/check-github-platform-enforcement 3.py""
    rollback_plan: "Restore the file from git history with git checkout -- "scripts/check-github-platform-enforcement 3.py"."
    rollback_validation_command: "test -f "scripts/check-github-platform-enforcement 3.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-015"
    candidate_id: "M76-CAND-015"
    target_path: "scripts/check-pre-merge-scope 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Remove duplicate Finder-copied script or fixture file with no source-of-truth value."
    validation_command: "test ! -e "scripts/check-pre-merge-scope 3.py""
    rollback_plan: "Restore the file from git history with git checkout -- "scripts/check-pre-merge-scope 3.py"."
    rollback_validation_command: "test -f "scripts/check-pre-merge-scope 3.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-016"
    candidate_id: "M76-CAND-016"
    target_path: "scripts/check-scope-compliance 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Remove duplicate Finder-copied script or fixture file with no source-of-truth value."
    validation_command: "test ! -e "scripts/check-scope-compliance 3.py""
    rollback_plan: "Restore the file from git history with git checkout -- "scripts/check-scope-compliance 3.py"."
    rollback_validation_command: "test -f "scripts/check-scope-compliance 3.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-017"
    candidate_id: "M76-CAND-017"
    target_path: "scripts/test-ci-advisory-config 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Remove duplicate Finder-copied script or fixture file with no source-of-truth value."
    validation_command: "test ! -e "scripts/test-ci-advisory-config 3.py""
    rollback_plan: "Restore the file from git history with git checkout -- "scripts/test-ci-advisory-config 3.py"."
    rollback_validation_command: "test -f "scripts/test-ci-advisory-config 3.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-018"
    candidate_id: "M76-CAND-018"
    target_path: "scripts/test-commit-push-preconditions-fixtures 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Remove duplicate Finder-copied script or fixture file with no source-of-truth value."
    validation_command: "test ! -e "scripts/test-commit-push-preconditions-fixtures 3.py""
    rollback_plan: "Restore the file from git history with git checkout -- "scripts/test-commit-push-preconditions-fixtures 3.py"."
    rollback_validation_command: "test -f "scripts/test-commit-push-preconditions-fixtures 3.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-019"
    candidate_id: "M76-CAND-019"
    target_path: "scripts/test-enforcement-fixtures 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Remove duplicate Finder-copied script or fixture file with no source-of-truth value."
    validation_command: "test ! -e "scripts/test-enforcement-fixtures 3.py""
    rollback_plan: "Restore the file from git history with git checkout -- "scripts/test-enforcement-fixtures 3.py"."
    rollback_validation_command: "test -f "scripts/test-enforcement-fixtures 3.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-020"
    candidate_id: "M76-CAND-020"
    target_path: "scripts/test-m22-guardrails 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Remove duplicate Finder-copied script or fixture file with no source-of-truth value."
    validation_command: "test ! -e "scripts/test-m22-guardrails 3.py""
    rollback_plan: "Restore the file from git history with git checkout -- "scripts/test-m22-guardrails 3.py"."
    rollback_validation_command: "test -f "scripts/test-m22-guardrails 3.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-021"
    candidate_id: "M76-CAND-021"
    target_path: "scripts/test-m27-level1-fixtures 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Remove duplicate Finder-copied script or fixture file with no source-of-truth value."
    validation_command: "test ! -e "scripts/test-m27-level1-fixtures 3.py""
    rollback_plan: "Restore the file from git history with git checkout -- "scripts/test-m27-level1-fixtures 3.py"."
    rollback_validation_command: "test -f "scripts/test-m27-level1-fixtures 3.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-022"
    candidate_id: "M76-CAND-022"
    target_path: "scripts/test-pre-merge-corridor-fixtures 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Remove duplicate Finder-copied script or fixture file with no source-of-truth value."
    validation_command: "test ! -e "scripts/test-pre-merge-corridor-fixtures 3.py""
    rollback_plan: "Restore the file from git history with git checkout -- "scripts/test-pre-merge-corridor-fixtures 3.py"."
    rollback_validation_command: "test -f "scripts/test-pre-merge-corridor-fixtures 3.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-023"
    candidate_id: "M76-CAND-023"
    target_path: "scripts/test-pre-merge-scope-fixtures 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Remove duplicate Finder-copied script or fixture file with no source-of-truth value."
    validation_command: "test ! -e "scripts/test-pre-merge-scope-fixtures 3.py""
    rollback_plan: "Restore the file from git history with git checkout -- "scripts/test-pre-merge-scope-fixtures 3.py"."
    rollback_validation_command: "test -f "scripts/test-pre-merge-scope-fixtures 3.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-024"
    candidate_id: "M76-CAND-024"
    target_path: "scripts/test-scope-compliance-fixtures 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Remove duplicate Finder-copied script or fixture file with no source-of-truth value."
    validation_command: "test ! -e "scripts/test-scope-compliance-fixtures 3.py""
    rollback_plan: "Restore the file from git history with git checkout -- "scripts/test-scope-compliance-fixtures 3.py"."
    rollback_validation_command: "test -f "scripts/test-scope-compliance-fixtures 3.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-025"
    candidate_id: "M76-CAND-025"
    target_path: "scripts/validate-boundary-claims 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Remove duplicate Finder-copied script or fixture file with no source-of-truth value."
    validation_command: "test ! -e "scripts/validate-boundary-claims 3.py""
    rollback_plan: "Restore the file from git history with git checkout -- "scripts/validate-boundary-claims 3.py"."
    rollback_validation_command: "test -f "scripts/validate-boundary-claims 3.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-026"
    candidate_id: "M76-CAND-026"
    target_path: "scripts/validate-frontmatter 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Remove duplicate Finder-copied script or fixture file with no source-of-truth value."
    validation_command: "test ! -e "scripts/validate-frontmatter 3.py""
    rollback_plan: "Restore the file from git history with git checkout -- "scripts/validate-frontmatter 3.py"."
    rollback_validation_command: "test -f "scripts/validate-frontmatter 3.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-027"
    candidate_id: "M76-CAND-027"
    target_path: "scripts/validate-index 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Remove duplicate Finder-copied script or fixture file with no source-of-truth value."
    validation_command: "test ! -e "scripts/validate-index 3.py""
    rollback_plan: "Restore the file from git history with git checkout -- "scripts/validate-index 3.py"."
    rollback_validation_command: "test -f "scripts/validate-index 3.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-028"
    candidate_id: "M76-CAND-028"
    target_path: "scripts/validate-required-sections 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Remove duplicate Finder-copied script or fixture file with no source-of-truth value."
    validation_command: "test ! -e "scripts/validate-required-sections 3.py""
    rollback_plan: "Restore the file from git history with git checkout -- "scripts/validate-required-sections 3.py"."
    rollback_validation_command: "test -f "scripts/validate-required-sections 3.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-029"
    candidate_id: "M76-CAND-029"
    target_path: "scripts/validate-status-semantics 3.py"
    planned_action: "delete"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Remove duplicate Finder-copied script or fixture file with no source-of-truth value."
    validation_command: "test ! -e "scripts/validate-status-semantics 3.py""
    rollback_plan: "Restore the file from git history with git checkout -- "scripts/validate-status-semantics 3.py"."
    rollback_validation_command: "test -f "scripts/validate-status-semantics 3.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-030"
    candidate_id: "M76-CAND-030"
    target_path: "scripts/agent-complete.py"
    planned_action: "mark_legacy"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Mark the legacy entrypoint as deprecated for future cleanup review."
    validation_command: "test -f "scripts/agent-complete.py""
    rollback_plan: "Restore the file from git history with git checkout -- "scripts/agent-complete.py"."
    rollback_validation_command: "test -f "scripts/agent-complete.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-031"
    candidate_id: "M76-CAND-031"
    target_path: "scripts/agent-fail.py"
    planned_action: "mark_legacy"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Mark the legacy entrypoint as deprecated for future cleanup review."
    validation_command: "test -f "scripts/agent-fail.py""
    rollback_plan: "Restore the file from git history with git checkout -- "scripts/agent-fail.py"."
    rollback_validation_command: "test -f "scripts/agent-fail.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-032"
    candidate_id: "M76-CAND-032"
    target_path: "scripts/agent-next.py"
    planned_action: "mark_legacy"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Mark the legacy entrypoint as deprecated for future cleanup review."
    validation_command: "test -f "scripts/agent-next.py""
    rollback_plan: "Restore the file from git history with git checkout -- "scripts/agent-next.py"."
    rollback_validation_command: "test -f "scripts/agent-next.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-033"
    candidate_id: "M76-CAND-033"
    target_path: "scripts/agentos.py"
    planned_action: "mark_legacy"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Mark the legacy entrypoint as deprecated for future cleanup review."
    validation_command: "test -f "scripts/agentos.py""
    rollback_plan: "Restore the file from git history with git checkout -- "scripts/agentos.py"."
    rollback_validation_command: "test -f "scripts/agentos.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-034"
    candidate_id: "M76-CAND-034"
    target_path: "scripts/run-active-task.py"
    planned_action: "mark_legacy"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Mark the legacy entrypoint as deprecated for future cleanup review."
    validation_command: "test -f "scripts/run-active-task.py""
    rollback_plan: "Restore the file from git history with git checkout -- "scripts/run-active-task.py"."
    rollback_validation_command: "test -f "scripts/run-active-task.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-035"
    candidate_id: "M76-CAND-035"
    target_path: "HANDOFF 2.md"
    planned_action: "archive"
    risk_class_from_m76: "UNKNOWN_BLOCKED"
    m77_planning_class: "BLOCKED_UNKNOWN"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Keep the unknown copy file out of executable cleanup planning until the owner and purpose are confirmed."
    validation_command: "test -f "HANDOFF 2.md""
    rollback_plan: "Restore the file from git history with git checkout -- "HANDOFF 2.md"."
    rollback_validation_command: "test -f "HANDOFF 2.md""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_2_stale_copy"
    execution_wave_current: "wave_2_stale_copy"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-036"
    candidate_id: "M76-CAND-036"
    target_path: "llms.txt"
    planned_action: "compress"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Reduce bootstrap document footprint while preserving startup guidance and adapter context."
    validation_command: "test -f "llms.txt""
    rollback_plan: "Restore the original file with git checkout -- "llms.txt"."
    rollback_validation_command: "test -f "llms.txt""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_4_text_bootstrap"
    execution_wave_current: "wave_4_text_bootstrap"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-037"
    candidate_id: "M76-CAND-037"
    target_path: "AGENTS.md"
    planned_action: "compress"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Reduce bootstrap document footprint while preserving startup guidance and adapter context."
    validation_command: "test -f "AGENTS.md""
    rollback_plan: "Restore the original file with git checkout -- "AGENTS.md"."
    rollback_validation_command: "test -f "AGENTS.md""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_4_text_bootstrap"
    execution_wave_current: "wave_4_text_bootstrap"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-038"
    candidate_id: "M76-CAND-038"
    target_path: "CLAUDE.md"
    planned_action: "compress"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Reduce bootstrap document footprint while preserving startup guidance and adapter context."
    validation_command: "test -f "CLAUDE.md""
    rollback_plan: "Restore the original file with git checkout -- "CLAUDE.md"."
    rollback_validation_command: "test -f "CLAUDE.md""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_4_text_bootstrap"
    execution_wave_current: "wave_4_text_bootstrap"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-039"
    candidate_id: "M76-CAND-039"
    target_path: "GEMINI.md"
    planned_action: "compress"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Reduce bootstrap document footprint while preserving startup guidance and adapter context."
    validation_command: "test -f "GEMINI.md""
    rollback_plan: "Restore the original file with git checkout -- "GEMINI.md"."
    rollback_validation_command: "test -f "GEMINI.md""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_4_text_bootstrap"
    execution_wave_current: "wave_4_text_bootstrap"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-040"
    candidate_id: "M76-CAND-040"
    target_path: "README.md"
    planned_action: "compress"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Reduce bootstrap document footprint while preserving startup guidance and adapter context."
    validation_command: "test -f "README.md""
    rollback_plan: "Restore the original file with git checkout -- "README.md"."
    rollback_validation_command: "test -f "README.md""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_4_text_bootstrap"
    execution_wave_current: "wave_4_text_bootstrap"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-041"
    candidate_id: "M76-CAND-041"
    target_path: "scripts/agentos-validate.py"
    planned_action: "consolidate"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Consolidate validation behavior into fewer authority scripts without changing accepted semantics."
    validation_command: "python3 -m py_compile "scripts/agentos-validate.py""
    rollback_plan: "Restore the original file with git checkout -- "scripts/agentos-validate.py"."
    rollback_validation_command: "test -f "scripts/agentos-validate.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-042"
    candidate_id: "M76-CAND-042"
    target_path: "scripts/check-dangerous-commands.py"
    planned_action: "consolidate"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Consolidate validation behavior into fewer authority scripts without changing accepted semantics."
    validation_command: "python3 -m py_compile "scripts/check-dangerous-commands.py""
    rollback_plan: "Restore the original file with git checkout -- "scripts/check-dangerous-commands.py"."
    rollback_validation_command: "test -f "scripts/check-dangerous-commands.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-043"
    candidate_id: "M76-CAND-043"
    target_path: "scripts/check-execution-authorization.py"
    planned_action: "consolidate"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Consolidate validation behavior into fewer authority scripts without changing accepted semantics."
    validation_command: "python3 -m py_compile "scripts/check-execution-authorization.py""
    rollback_plan: "Restore the original file with git checkout -- "scripts/check-execution-authorization.py"."
    rollback_validation_command: "test -f "scripts/check-execution-authorization.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-044"
    candidate_id: "M76-CAND-044"
    target_path: "scripts/check-execution-readiness.py"
    planned_action: "consolidate"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Consolidate validation behavior into fewer authority scripts without changing accepted semantics."
    validation_command: "python3 -m py_compile "scripts/check-execution-readiness.py""
    rollback_plan: "Restore the original file with git checkout -- "scripts/check-execution-readiness.py"."
    rollback_validation_command: "test -f "scripts/check-execution-readiness.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-045"
    candidate_id: "M76-CAND-045"
    target_path: "scripts/check-human-approval.py"
    planned_action: "consolidate"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Consolidate validation behavior into fewer authority scripts without changing accepted semantics."
    validation_command: "python3 -m py_compile "scripts/check-human-approval.py""
    rollback_plan: "Restore the original file with git checkout -- "scripts/check-human-approval.py"."
    rollback_validation_command: "test -f "scripts/check-human-approval.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-046"
    candidate_id: "M76-CAND-046"
    target_path: "scripts/check-lifecycle-mutation.py"
    planned_action: "consolidate"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Consolidate validation behavior into fewer authority scripts without changing accepted semantics."
    validation_command: "python3 -m py_compile "scripts/check-lifecycle-mutation.py""
    rollback_plan: "Restore the original file with git checkout -- "scripts/check-lifecycle-mutation.py"."
    rollback_validation_command: "test -f "scripts/check-lifecycle-mutation.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-047"
    candidate_id: "M76-CAND-047"
    target_path: "scripts/check-readiness-assertions.py"
    planned_action: "consolidate"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Consolidate validation behavior into fewer authority scripts without changing accepted semantics."
    validation_command: "python3 -m py_compile "scripts/check-readiness-assertions.py""
    rollback_plan: "Restore the original file with git checkout -- "scripts/check-readiness-assertions.py"."
    rollback_validation_command: "test -f "scripts/check-readiness-assertions.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-048"
    candidate_id: "M76-CAND-048"
    target_path: "scripts/check-validator-authority-boundary.py"
    planned_action: "consolidate"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Consolidate validation behavior into fewer authority scripts without changing accepted semantics."
    validation_command: "python3 -m py_compile "scripts/check-validator-authority-boundary.py""
    rollback_plan: "Restore the original file with git checkout -- "scripts/check-validator-authority-boundary.py"."
    rollback_validation_command: "test -f "scripts/check-validator-authority-boundary.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-049"
    candidate_id: "M76-CAND-049"
    target_path: "scripts/validate-lifecycle-apply.py"
    planned_action: "consolidate"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Consolidate validation behavior into fewer authority scripts without changing accepted semantics."
    validation_command: "python3 -m py_compile "scripts/validate-lifecycle-apply.py""
    rollback_plan: "Restore the original file with git checkout -- "scripts/validate-lifecycle-apply.py"."
    rollback_validation_command: "test -f "scripts/validate-lifecycle-apply.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-050"
    candidate_id: "M76-CAND-050"
    target_path: "scripts/validate-task.py"
    planned_action: "consolidate"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    source_evidence: "reports/m76-cleanup-candidate-inventory.md"
    expected_effect: "Consolidate validation behavior into fewer authority scripts without changing accepted semantics."
    validation_command: "python3 -m py_compile "scripts/validate-task.py""
    rollback_plan: "Restore the original file with git checkout -- "scripts/validate-task.py"."
    rollback_validation_command: "test -f "scripts/validate-task.py""
    human_checkpoint_required: true
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-051"
    candidate_id: "M76-CAND-051"
    target_path: "reports/m71-script-inventory.json"
    planned_action: "defer_to_m80"
    risk_class_from_m76: "UNKNOWN_BLOCKED"
    m77_planning_class: "M80_ONLY_DERIVED_UPDATE_CANDIDATE"
    source_evidence: "reports/m76-optimization-risk-map.md"
    expected_effect: "Keep the derived navigation/index artifact out of M77 cleanup and defer any regeneration-linked update to M80."
    validation_command: "grep -n "reports/m71-script-inventory.json" "reports/m76-optimization-risk-map.md""
    rollback_plan: "Restore the file from git history with git checkout -- "reports/m71-script-inventory.json" or regenerate from the source-of-truth build step."
    rollback_validation_command: "test -f "reports/m71-script-inventory.json""
    human_checkpoint_required: false
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_5_derived_navigation"
    execution_wave_current: "wave_5_derived_navigation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: true
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "M77-CONTRADICTION-001"
    m80_only_deferred_candidate: true
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-052"
    candidate_id: "M76-CAND-052"
    target_path: "repo-map.md"
    planned_action: "defer_to_m80"
    risk_class_from_m76: "UNKNOWN_BLOCKED"
    m77_planning_class: "M80_ONLY_DERIVED_UPDATE_CANDIDATE"
    source_evidence: "reports/m76-optimization-risk-map.md"
    expected_effect: "Keep the derived navigation/index artifact out of M77 cleanup and defer any regeneration-linked update to M80."
    validation_command: "grep -n "repo-map.md" "reports/m76-optimization-risk-map.md""
    rollback_plan: "Restore the file from git history with git checkout -- "repo-map.md" or regenerate from the source-of-truth build step."
    rollback_validation_command: "test -f "repo-map.md""
    human_checkpoint_required: false
    protected_or_canonical: false
    execution_wave_from_77_1: "wave_5_derived_navigation"
    execution_wave_current: "wave_5_derived_navigation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: true
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "M77-CONTRADICTION-002"
    m80_only_deferred_candidate: true
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-053"
    candidate_id: "M76-CAND-053"
    target_path: "ROUTES-REGISTRY.md"
    planned_action: "mark_legacy"
    risk_class_from_m76: "PROTECTED_DO_NOT_TOUCH"
    m77_planning_class: "BLOCKED_PROTECTED_DO_NOT_TOUCH"
    source_evidence: "reports/m77-protected-artifact-review.md"
    expected_effect: "Keep the protected canonical artifact blocked from any executable cleanup path."
    validation_command: "test -f "ROUTES-REGISTRY.md""
    rollback_plan: "No change is planned; if altered, restore the file from git history with git checkout -- "ROUTES-REGISTRY.md"."
    rollback_validation_command: "test -f "ROUTES-REGISTRY.md""
    human_checkpoint_required: true
    protected_or_canonical: true
    execution_wave_from_77_1: "wave_4_text_bootstrap"
    execution_wave_current: "wave_4_text_bootstrap"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-054"
    candidate_id: "M76-CAND-054"
    target_path: "core-rules/MAIN.md"
    planned_action: "mark_legacy"
    risk_class_from_m76: "PROTECTED_DO_NOT_TOUCH"
    m77_planning_class: "BLOCKED_PROTECTED_DO_NOT_TOUCH"
    source_evidence: "reports/m77-protected-artifact-review.md"
    expected_effect: "Keep the protected canonical artifact blocked from any executable cleanup path."
    validation_command: "test -f "core-rules/MAIN.md""
    rollback_plan: "No change is planned; if altered, restore the file from git history with git checkout -- "core-rules/MAIN.md"."
    rollback_validation_command: "test -f "core-rules/MAIN.md""
    human_checkpoint_required: true
    protected_or_canonical: true
    execution_wave_from_77_1: "wave_4_text_bootstrap"
    execution_wave_current: "wave_4_text_bootstrap"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-055"
    candidate_id: "M76-CAND-055"
    target_path: "state/MAIN.md"
    planned_action: "mark_legacy"
    risk_class_from_m76: "PROTECTED_DO_NOT_TOUCH"
    m77_planning_class: "BLOCKED_PROTECTED_DO_NOT_TOUCH"
    source_evidence: "reports/m77-protected-artifact-review.md"
    expected_effect: "Keep the protected canonical artifact blocked from any executable cleanup path."
    validation_command: "test -f "state/MAIN.md""
    rollback_plan: "No change is planned; if altered, restore the file from git history with git checkout -- "state/MAIN.md"."
    rollback_validation_command: "test -f "state/MAIN.md""
    human_checkpoint_required: true
    protected_or_canonical: true
    execution_wave_from_77_1: "wave_4_text_bootstrap"
    execution_wave_current: "wave_4_text_bootstrap"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-056"
    candidate_id: "M76-CAND-056"
    target_path: "workflow/MAIN.md"
    planned_action: "mark_legacy"
    risk_class_from_m76: "PROTECTED_DO_NOT_TOUCH"
    m77_planning_class: "BLOCKED_PROTECTED_DO_NOT_TOUCH"
    source_evidence: "reports/m77-protected-artifact-review.md"
    expected_effect: "Keep the protected canonical artifact blocked from any executable cleanup path."
    validation_command: "test -f "workflow/MAIN.md""
    rollback_plan: "No change is planned; if altered, restore the file from git history with git checkout -- "workflow/MAIN.md"."
    rollback_validation_command: "test -f "workflow/MAIN.md""
    human_checkpoint_required: true
    protected_or_canonical: true
    execution_wave_from_77_1: "wave_4_text_bootstrap"
    execution_wave_current: "wave_4_text_bootstrap"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-057"
    candidate_id: "M76-CAND-057"
    target_path: "quality/MAIN.md"
    planned_action: "mark_legacy"
    risk_class_from_m76: "PROTECTED_DO_NOT_TOUCH"
    m77_planning_class: "BLOCKED_PROTECTED_DO_NOT_TOUCH"
    source_evidence: "reports/m77-protected-artifact-review.md"
    expected_effect: "Keep the protected canonical artifact blocked from any executable cleanup path."
    validation_command: "test -f "quality/MAIN.md""
    rollback_plan: "No change is planned; if altered, restore the file from git history with git checkout -- "quality/MAIN.md"."
    rollback_validation_command: "test -f "quality/MAIN.md""
    human_checkpoint_required: true
    protected_or_canonical: true
    execution_wave_from_77_1: "wave_4_text_bootstrap"
    execution_wave_current: "wave_4_text_bootstrap"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
  - cleanup_plan_item_id: "M77-CLEANUP-058"
    candidate_id: "M76-CAND-058"
    target_path: "security/MAIN.md"
    planned_action: "mark_legacy"
    risk_class_from_m76: "PROTECTED_DO_NOT_TOUCH"
    m77_planning_class: "BLOCKED_PROTECTED_DO_NOT_TOUCH"
    source_evidence: "reports/m77-protected-artifact-review.md"
    expected_effect: "Keep the protected canonical artifact blocked from any executable cleanup path."
    validation_command: "test -f "security/MAIN.md""
    rollback_plan: "No change is planned; if altered, restore the file from git history with git checkout -- "security/MAIN.md"."
    rollback_validation_command: "test -f "security/MAIN.md""
    human_checkpoint_required: true
    protected_or_canonical: true
    execution_wave_from_77_1: "wave_4_text_bootstrap"
    execution_wave_current: "wave_4_text_bootstrap"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    m76_contradictions_resolved_by_agent: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_m77: false
    physical_cleanup_performed: false
    human_summary_consistent_with_machine_fields: true
```
