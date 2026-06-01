# M77.1 - Cleanup Classification Review

## Human Summary
- Can next M77 task be prepared: true_with_warnings
- Does this block M78 preparation: true
- Main blockers:
  - none
- Main warnings:
  - M76_WARNINGS_CARRIED_FORWARD, UNKNOWN_BLOCKED_RECLASSIFICATION_CORRECTED, NON_BLOCKING_M76_CONTRADICTIONS_CARRIED_FORWARD
- Human checkpoint required: true
- Cleanup authorized: false
- Physical cleanup performed: false
- Next readiness field: "may_prepare_m77_2: true_with_warnings"

## Title
- Task: `77.1 - Cleanup Classification Review`
- Mode: read-only classification review / cleanup planning classification

## Purpose
This report classifies M76 scope-lock candidates into M77 planning groups and initial execution waves.
It preserves M76 findings and does not authorize cleanup.

## 77.0 Intake Check
- `reports/m77-m76-completion-intake.md` exists and is readable.
- `m77_0_final_status_detected: "M77_M76_COMPLETION_INTAKE_READY_WITH_WARNINGS"`
- `m77_0_readiness_detected: "true_with_warnings"`

## M76 Source Inputs Checked
- `reports/m76-cleanup-candidate-inventory.md` exists and is readable.
- `reports/m76-optimization-risk-map.md` exists and is readable.
- `reports/m76-human-checkpoint-plan.md` exists and is readable.
- `reports/m76-optimization-scope-lock.md` exists and is readable.
- `reports/m76-completion-review.md` exists and is readable.

## Classification Method
- Keep M76 risk classes, protected status, unknown status, checkpoint requirements, and scope boundaries intact.
- Use the stricter classification when a candidate could be interpreted more than one way.
- Derived navigation/index items are deferred to M80-only handling.
- No item is marked executable cleanup in this report.

## M76 Non-Override Review
- `m76_findings_overridden: false`
- `m76_contradictions_detected: true`
- `m76_contradictions_resolved_by_agent: false`
- `m76_contradiction_count: 2`
- `m76_contradiction_register_complete: true`

## M76 Contradiction Register
- `M77-CONTRADICTION-001` for `M76-CAND-051` at `reports/m71-script-inventory.json`
- `M77-CONTRADICTION-002` for `M76-CAND-052` at `repo-map.md`
- Both remain blocked as UNKNOWN_BLOCKED and cannot be reclassified by the agent.

## Classification Group Summary
- `eligible_for_low_risk_cleanup_planning`: 6
- `eligible_for_checkpoint_required_planning`: 43
- `protected_do_not_touch`: 6
- `unknown_blocked`: 3
- `reference_only`: 0
- `m80_derived_update_candidate`: 0

## Execution Wave Summary
- `wave_1_cache_noise`: 6
- `wave_2_stale_copy`: 1
- `wave_3_scripts_validation`: 38
- `wave_4_text_bootstrap`: 11
- `wave_5_derived_navigation`: 0

## Full Classification Review
- 58 candidates are classified below.
- M76 findings are preserved.
- Unknown-blocked, protected, and checkpoint-required items remain non-executable.

## Unknown Blocked Candidates
- `M76-CAND-035`, `M76-CAND-051`, and `M76-CAND-052` stay blocked reference only in this report.

## Protected Do-Not-Touch Candidates
- `M76-CAND-053` through `M76-CAND-058` remain protected and blocked from M78 eligibility.

## Checkpoint-Required Planning Candidates
- `M76-CAND-007` through `M76-CAND-034`, `M76-CAND-036` through `M76-CAND-050` remain planning-only with checkpoint requirements.

## Low-Risk Planning Candidates
- `M76-CAND-001` through `M76-CAND-006` remain eligible only for low-risk planning.

## Reference-Only Candidates
- None.

## M80-Only Derived Update Candidates
- None.

## Cleanup Authorization Boundary
- `cleanup_authorized_by_77_1: false`
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
- `m80_artifact_created_by_77_1: false`
- `protected_artifact_review_created: false`
- `cleanup_plan_created: false`
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
  - `M77_0_WARNINGS_CARRIED_FORWARD`
  - `M76_WARNINGS_CARRIED_FORWARD`
  - `UNKNOWN_BLOCKED_CANDIDATES_PRESENT`
  - `PROTECTED_DO_NOT_TOUCH_CANDIDATES_PRESENT`
  - `REQUIRES_HUMAN_CHECKPOINT_CANDIDATES_PRESENT`
  - `M80_DERIVED_UPDATE_CANDIDATES_PRESENT`
  - `NON_BLOCKING_M76_CONTRADICTIONS_CARRIED_FORWARD`

## Local Final Status
- `FINAL_STATUS: "M77_CLASSIFICATION_REVIEW_COMPLETE_WITH_WARNINGS"`

## Readiness for 77.2
- `may_prepare_m77_2: "true_with_warnings"`

## Final Boundary Statement
This report only classifies M76 candidates for M77 planning.
It does not authorize cleanup, does not create cleanup planning artifacts, and does not start M77, M78, M80, or M81.
Human review remains required.

### Machine-Readable Metadata
```yaml
task_id: "77.1"
task_name: "Cleanup Classification Review"
reports_directory_exists: true
input_file: "reports/m77-m76-completion-intake.md"

m77_0_intake_exists: true
m77_0_intake_readable: true
m77_0_final_status_detected: "M77_M76_COMPLETION_INTAKE_READY_WITH_WARNINGS"
m77_0_final_status_acceptable: true
m77_0_readiness_detected: "true_with_warnings"
m77_0_readiness_acceptable: true

m76_candidate_inventory_exists: true
m76_risk_map_exists: true
m76_human_checkpoint_plan_exists: true
m76_scope_lock_exists: true
m76_completion_review_exists: true

classification_review_created: true
candidate_count_total: 58
classification_item_count: 58

eligible_for_low_risk_cleanup_planning_count: 6
eligible_for_checkpoint_required_planning_count: 43
protected_do_not_touch_count: 6
unknown_blocked_count: 3
reference_only_count: 0
m80_derived_update_candidate_count: 0

wave_1_cache_noise_count: 6
wave_2_stale_copy_count: 1
wave_3_scripts_validation_count: 38
wave_4_text_bootstrap_count: 11
wave_5_derived_navigation_count: 0

m76_findings_overridden: false
m76_contradictions_detected: true
m76_contradictions_resolved_by_agent: false
m76_contradiction_count: 2
m76_contradiction_register_complete: true

protected_m76_item_marked_m78_eligible: false
wave_5_derived_item_marked_m78_executable: false
m80_artifact_created_by_77_1: false

cleanup_authorized_by_77_1: false
physical_cleanup_occurred: false
files_deleted: false
files_moved: false
files_renamed: false
files_archived: false
files_compressed: false
scripts_consolidated: false
docs_compressed: false

protected_artifact_review_created: false
cleanup_plan_created: false
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
  - "M77_0_WARNINGS_CARRIED_FORWARD"
  - "M76_WARNINGS_CARRIED_FORWARD"
  - "UNKNOWN_BLOCKED_CANDIDATES_PRESENT"
  - "PROTECTED_DO_NOT_TOUCH_CANDIDATES_PRESENT"
  - "REQUIRES_HUMAN_CHECKPOINT_CANDIDATES_PRESENT"
  - "UNKNOWN_BLOCKED_RECLASSIFICATION_CORRECTED"
  - "NON_BLOCKING_M76_CONTRADICTIONS_CARRIED_FORWARD"

m76_contradictions:
  - contradiction_id: "M77-CONTRADICTION-001"
    candidate_id: "M76-CAND-051"
    target_path: "reports/m71-script-inventory.json"
    m76_finding: "UNKNOWN_BLOCKED in the M76 risk map and scope lock"
    m77_finding: "m80_derived_update_candidate; execution_wave wave_5_derived_navigation; M80_ONLY_DERIVED_UPDATE_CANDIDATE"
    contradiction_type: "wave_assignment"
    resolution: "blocked"
    resolved_by_agent: false
    blocks_m78: true
    note: "UNKNOWN_BLOCKED_CANNOT_BE_RECLASSIFIED_BY_AGENT"
  - contradiction_id: "M77-CONTRADICTION-002"
    candidate_id: "M76-CAND-052"
    target_path: "repo-map.md"
    m76_finding: "UNKNOWN_BLOCKED in the M76 risk map and scope lock"
    m77_finding: "m80_derived_update_candidate; execution_wave wave_5_derived_navigation; M80_ONLY_DERIVED_UPDATE_CANDIDATE"
    contradiction_type: "wave_assignment"
    resolution: "blocked"
    resolved_by_agent: false
    blocks_m78: true
    note: "UNKNOWN_BLOCKED_CANNOT_BE_RECLASSIFIED_BY_AGENT"

classification_items:
  - candidate_id: "M76-CAND-001"
    target_path: "scripts/__pycache__/agent-complete.cpython-314.pyc"
    m76_category: "tracked_pycache"
    m76_scope_group: "low_risk_cleanup_planning_candidates"
    risk_class_from_m76: "LOW_RISK_CLEANUP"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: false
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_low_risk_cleanup_planning"
    m77_planning_class: "M78_ELIGIBLE_LOW_RISK"
    execution_wave_from_77_1: "wave_1_cache_noise"
    execution_wave_current: "wave_1_cache_noise"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Tracked pycache file."

  - candidate_id: "M76-CAND-002"
    target_path: "scripts/__pycache__/agent-fail.cpython-314.pyc"
    m76_category: "tracked_pycache"
    m76_scope_group: "low_risk_cleanup_planning_candidates"
    risk_class_from_m76: "LOW_RISK_CLEANUP"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: false
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_low_risk_cleanup_planning"
    m77_planning_class: "M78_ELIGIBLE_LOW_RISK"
    execution_wave_from_77_1: "wave_1_cache_noise"
    execution_wave_current: "wave_1_cache_noise"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Tracked pycache file."

  - candidate_id: "M76-CAND-003"
    target_path: "scripts/__pycache__/agent-next.cpython-314.pyc"
    m76_category: "tracked_pycache"
    m76_scope_group: "low_risk_cleanup_planning_candidates"
    risk_class_from_m76: "LOW_RISK_CLEANUP"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: false
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_low_risk_cleanup_planning"
    m77_planning_class: "M78_ELIGIBLE_LOW_RISK"
    execution_wave_from_77_1: "wave_1_cache_noise"
    execution_wave_current: "wave_1_cache_noise"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Tracked pycache file."

  - candidate_id: "M76-CAND-004"
    target_path: "scripts/__pycache__/generate-task-contract.cpython-314.pyc"
    m76_category: "tracked_pycache"
    m76_scope_group: "low_risk_cleanup_planning_candidates"
    risk_class_from_m76: "LOW_RISK_CLEANUP"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: false
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_low_risk_cleanup_planning"
    m77_planning_class: "M78_ELIGIBLE_LOW_RISK"
    execution_wave_from_77_1: "wave_1_cache_noise"
    execution_wave_current: "wave_1_cache_noise"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Tracked pycache file."

  - candidate_id: "M76-CAND-005"
    target_path: "scripts/__pycache__/validate-task.cpython-314.pyc"
    m76_category: "tracked_pycache"
    m76_scope_group: "low_risk_cleanup_planning_candidates"
    risk_class_from_m76: "LOW_RISK_CLEANUP"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: false
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_low_risk_cleanup_planning"
    m77_planning_class: "M78_ELIGIBLE_LOW_RISK"
    execution_wave_from_77_1: "wave_1_cache_noise"
    execution_wave_current: "wave_1_cache_noise"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Tracked pycache file."

  - candidate_id: "M76-CAND-006"
    target_path: "scripts/__pycache__/validate-verification.cpython-314.pyc"
    m76_category: "tracked_pycache"
    m76_scope_group: "low_risk_cleanup_planning_candidates"
    risk_class_from_m76: "LOW_RISK_CLEANUP"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: false
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_low_risk_cleanup_planning"
    m77_planning_class: "M78_ELIGIBLE_LOW_RISK"
    execution_wave_from_77_1: "wave_1_cache_noise"
    execution_wave_current: "wave_1_cache_noise"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Tracked pycache file."

  - candidate_id: "M76-CAND-007"
    target_path: "scripts/audit-m27 3.py"
    m76_category: "duplicate_script"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Duplicate audit script."

  - candidate_id: "M76-CAND-008"
    target_path: "scripts/audit-m27-level1 3.py"
    m76_category: "duplicate_script"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Duplicate audit script."

  - candidate_id: "M76-CAND-009"
    target_path: "scripts/audit-metadata-consistency 3.py"
    m76_category: "duplicate_script"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Duplicate audit script."

  - candidate_id: "M76-CAND-010"
    target_path: "scripts/audit-pre-merge-corridor 3.py"
    m76_category: "duplicate_script"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Duplicate audit script."

  - candidate_id: "M76-CAND-011"
    target_path: "scripts/audit-validation-integration 3.py"
    m76_category: "duplicate_script"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Duplicate audit script."

  - candidate_id: "M76-CAND-012"
    target_path: "scripts/build-index 3.py"
    m76_category: "duplicate_script"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Duplicate script."

  - candidate_id: "M76-CAND-013"
    target_path: "scripts/check-commit-push-preconditions 3.py"
    m76_category: "duplicate_script"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Duplicate script."

  - candidate_id: "M76-CAND-014"
    target_path: "scripts/check-github-platform-enforcement 3.py"
    m76_category: "duplicate_script"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Duplicate script."

  - candidate_id: "M76-CAND-015"
    target_path: "scripts/check-pre-merge-scope 3.py"
    m76_category: "duplicate_script"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Duplicate script."

  - candidate_id: "M76-CAND-016"
    target_path: "scripts/check-scope-compliance 3.py"
    m76_category: "duplicate_script"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Duplicate script."

  - candidate_id: "M76-CAND-017"
    target_path: "scripts/test-ci-advisory-config 3.py"
    m76_category: "duplicate_script"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Duplicate script."

  - candidate_id: "M76-CAND-018"
    target_path: "scripts/test-commit-push-preconditions-fixtures 3.py"
    m76_category: "duplicate_script"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Duplicate fixture script."

  - candidate_id: "M76-CAND-019"
    target_path: "scripts/test-enforcement-fixtures 3.py"
    m76_category: "duplicate_script"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Duplicate fixture script."

  - candidate_id: "M76-CAND-020"
    target_path: "scripts/test-m22-guardrails 3.py"
    m76_category: "duplicate_script"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Duplicate guardrail script."

  - candidate_id: "M76-CAND-021"
    target_path: "scripts/test-m27-level1-fixtures 3.py"
    m76_category: "duplicate_script"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Duplicate fixture script."

  - candidate_id: "M76-CAND-022"
    target_path: "scripts/test-pre-merge-corridor-fixtures 3.py"
    m76_category: "duplicate_script"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Duplicate fixture script."

  - candidate_id: "M76-CAND-023"
    target_path: "scripts/test-pre-merge-scope-fixtures 3.py"
    m76_category: "duplicate_script"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Duplicate fixture script."

  - candidate_id: "M76-CAND-024"
    target_path: "scripts/test-scope-compliance-fixtures 3.py"
    m76_category: "duplicate_script"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Duplicate fixture script."

  - candidate_id: "M76-CAND-025"
    target_path: "scripts/validate-boundary-claims 3.py"
    m76_category: "duplicate_script"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Duplicate validator script."

  - candidate_id: "M76-CAND-026"
    target_path: "scripts/validate-frontmatter 3.py"
    m76_category: "duplicate_script"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Duplicate validator script."

  - candidate_id: "M76-CAND-027"
    target_path: "scripts/validate-index 3.py"
    m76_category: "duplicate_script"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Duplicate validator script."

  - candidate_id: "M76-CAND-028"
    target_path: "scripts/validate-required-sections 3.py"
    m76_category: "duplicate_script"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Duplicate validator script."

  - candidate_id: "M76-CAND-029"
    target_path: "scripts/validate-status-semantics 3.py"
    m76_category: "duplicate_script"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Duplicate validator script."

  - candidate_id: "M76-CAND-030"
    target_path: "scripts/agent-complete.py"
    m76_category: "legacy_entrypoint"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Legacy entrypoint."

  - candidate_id: "M76-CAND-031"
    target_path: "scripts/agent-fail.py"
    m76_category: "legacy_entrypoint"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Legacy entrypoint."

  - candidate_id: "M76-CAND-032"
    target_path: "scripts/agent-next.py"
    m76_category: "legacy_entrypoint"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Legacy entrypoint."

  - candidate_id: "M76-CAND-033"
    target_path: "scripts/agentos.py"
    m76_category: "legacy_entrypoint"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Legacy entrypoint."

  - candidate_id: "M76-CAND-034"
    target_path: "scripts/run-active-task.py"
    m76_category: "legacy_entrypoint"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Legacy entrypoint."

  - candidate_id: "M76-CAND-035"
    target_path: "HANDOFF 2.md"
    m76_category: "copy_file"
    m76_scope_group: "unknown_blocked"
    risk_class_from_m76: "UNKNOWN_BLOCKED"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "medium"
    classification_group: "unknown_blocked"
    m77_planning_class: "BLOCKED_UNKNOWN"
    execution_wave_from_77_1: "wave_2_stale_copy"
    execution_wave_current: "wave_2_stale_copy"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Copy file remains blocked reference only."

  - candidate_id: "M76-CAND-036"
    target_path: "llms.txt"
    m76_category: "bootstrap_doc"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_4_text_bootstrap"
    execution_wave_current: "wave_4_text_bootstrap"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Bootstrap document."

  - candidate_id: "M76-CAND-037"
    target_path: "AGENTS.md"
    m76_category: "bootstrap_doc"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_4_text_bootstrap"
    execution_wave_current: "wave_4_text_bootstrap"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Bootstrap document."

  - candidate_id: "M76-CAND-038"
    target_path: "CLAUDE.md"
    m76_category: "bootstrap_doc"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_4_text_bootstrap"
    execution_wave_current: "wave_4_text_bootstrap"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Bootstrap document."

  - candidate_id: "M76-CAND-039"
    target_path: "GEMINI.md"
    m76_category: "bootstrap_doc"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_4_text_bootstrap"
    execution_wave_current: "wave_4_text_bootstrap"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Bootstrap document."

  - candidate_id: "M76-CAND-040"
    target_path: "README.md"
    m76_category: "bootstrap_doc"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_4_text_bootstrap"
    execution_wave_current: "wave_4_text_bootstrap"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Bootstrap document."

  - candidate_id: "M76-CAND-041"
    target_path: "scripts/agentos-validate.py"
    m76_category: "validation_wrapper"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Validation wrapper."

  - candidate_id: "M76-CAND-042"
    target_path: "scripts/check-dangerous-commands.py"
    m76_category: "validation_wrapper"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Validation wrapper."

  - candidate_id: "M76-CAND-043"
    target_path: "scripts/check-execution-authorization.py"
    m76_category: "validation_wrapper"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Validation wrapper."

  - candidate_id: "M76-CAND-044"
    target_path: "scripts/check-execution-readiness.py"
    m76_category: "validation_wrapper"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Validation wrapper."

  - candidate_id: "M76-CAND-045"
    target_path: "scripts/check-human-approval.py"
    m76_category: "validation_wrapper"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Validation wrapper."

  - candidate_id: "M76-CAND-046"
    target_path: "scripts/check-lifecycle-mutation.py"
    m76_category: "validation_wrapper"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Validation wrapper."

  - candidate_id: "M76-CAND-047"
    target_path: "scripts/check-readiness-assertions.py"
    m76_category: "validation_wrapper"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Validation wrapper."

  - candidate_id: "M76-CAND-048"
    target_path: "scripts/check-validator-authority-boundary.py"
    m76_category: "validation_wrapper"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Validation wrapper."

  - candidate_id: "M76-CAND-049"
    target_path: "scripts/validate-lifecycle-apply.py"
    m76_category: "validation_wrapper"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Validation wrapper."

  - candidate_id: "M76-CAND-050"
    target_path: "scripts/validate-task.py"
    m76_category: "validation_wrapper"
    m76_scope_group: "requires_human_checkpoint_before_cleanup"
    risk_class_from_m76: "REQUIRES_HUMAN_CHECKPOINT"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "eligible_for_checkpoint_required_planning"
    m77_planning_class: "M78_ELIGIBLE_AFTER_HUMAN_CHECKPOINT"
    execution_wave_from_77_1: "wave_3_scripts_validation"
    execution_wave_current: "wave_3_scripts_validation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Validation wrapper."

  - candidate_id: "M76-CAND-051"
    target_path: "reports/m71-script-inventory.json"
    m76_category: "derived_navigation_index_artifact"
    m76_scope_group: "unknown_blocked"
    risk_class_from_m76: "UNKNOWN_BLOCKED"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "unknown_blocked"
    m77_planning_class: "BLOCKED_UNKNOWN"
    execution_wave_from_77_1: "wave_5_derived_navigation"
    execution_wave_current: "wave_5_derived_navigation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: true
    contradiction_id: "M77-CONTRADICTION-001"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "UNKNOWN_BLOCKED_CANNOT_BE_RECLASSIFIED_BY_AGENT."

  - candidate_id: "M76-CAND-052"
    target_path: "repo-map.md"
    m76_category: "derived_navigation_index_artifact"
    m76_scope_group: "unknown_blocked"
    risk_class_from_m76: "UNKNOWN_BLOCKED"
    protected_or_canonical_from_m76: false
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "unknown_blocked"
    m77_planning_class: "BLOCKED_UNKNOWN"
    execution_wave_from_77_1: "wave_5_derived_navigation"
    execution_wave_current: "wave_5_derived_navigation"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: true
    contradiction_id: "M77-CONTRADICTION-002"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "UNKNOWN_BLOCKED_CANNOT_BE_RECLASSIFIED_BY_AGENT."

  - candidate_id: "M76-CAND-053"
    target_path: "ROUTES-REGISTRY.md"
    m76_category: "DO_NOT_TOUCH"
    m76_scope_group: "protected_do_not_touch"
    risk_class_from_m76: "PROTECTED_DO_NOT_TOUCH"
    protected_or_canonical_from_m76: true
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "protected_do_not_touch"
    m77_planning_class: "BLOCKED_PROTECTED_DO_NOT_TOUCH"
    execution_wave_from_77_1: "wave_4_text_bootstrap"
    execution_wave_current: "wave_4_text_bootstrap"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Protected canonical routing authority."

  - candidate_id: "M76-CAND-054"
    target_path: "core-rules/MAIN.md"
    m76_category: "DO_NOT_TOUCH"
    m76_scope_group: "protected_do_not_touch"
    risk_class_from_m76: "PROTECTED_DO_NOT_TOUCH"
    protected_or_canonical_from_m76: true
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "protected_do_not_touch"
    m77_planning_class: "BLOCKED_PROTECTED_DO_NOT_TOUCH"
    execution_wave_from_77_1: "wave_4_text_bootstrap"
    execution_wave_current: "wave_4_text_bootstrap"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Protected canonical governance authority."

  - candidate_id: "M76-CAND-055"
    target_path: "state/MAIN.md"
    m76_category: "DO_NOT_TOUCH"
    m76_scope_group: "protected_do_not_touch"
    risk_class_from_m76: "PROTECTED_DO_NOT_TOUCH"
    protected_or_canonical_from_m76: true
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "protected_do_not_touch"
    m77_planning_class: "BLOCKED_PROTECTED_DO_NOT_TOUCH"
    execution_wave_from_77_1: "wave_4_text_bootstrap"
    execution_wave_current: "wave_4_text_bootstrap"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Protected canonical state authority."

  - candidate_id: "M76-CAND-056"
    target_path: "workflow/MAIN.md"
    m76_category: "DO_NOT_TOUCH"
    m76_scope_group: "protected_do_not_touch"
    risk_class_from_m76: "PROTECTED_DO_NOT_TOUCH"
    protected_or_canonical_from_m76: true
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "protected_do_not_touch"
    m77_planning_class: "BLOCKED_PROTECTED_DO_NOT_TOUCH"
    execution_wave_from_77_1: "wave_4_text_bootstrap"
    execution_wave_current: "wave_4_text_bootstrap"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Protected canonical workflow authority."

  - candidate_id: "M76-CAND-057"
    target_path: "quality/MAIN.md"
    m76_category: "DO_NOT_TOUCH"
    m76_scope_group: "protected_do_not_touch"
    risk_class_from_m76: "PROTECTED_DO_NOT_TOUCH"
    protected_or_canonical_from_m76: true
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "protected_do_not_touch"
    m77_planning_class: "BLOCKED_PROTECTED_DO_NOT_TOUCH"
    execution_wave_from_77_1: "wave_4_text_bootstrap"
    execution_wave_current: "wave_4_text_bootstrap"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Protected canonical quality authority."

  - candidate_id: "M76-CAND-058"
    target_path: "security/MAIN.md"
    m76_category: "DO_NOT_TOUCH"
    m76_scope_group: "protected_do_not_touch"
    risk_class_from_m76: "PROTECTED_DO_NOT_TOUCH"
    protected_or_canonical_from_m76: true
    human_checkpoint_required_from_m76: true
    evidence_status_from_m76: "evidence_present"
    candidate_confidence_from_m76: "high"
    classification_group: "protected_do_not_touch"
    m77_planning_class: "BLOCKED_PROTECTED_DO_NOT_TOUCH"
    execution_wave_from_77_1: "wave_4_text_bootstrap"
    execution_wave_current: "wave_4_text_bootstrap"
    wave_changed: false
    wave_change_reason: "none"
    wave_consistency_status: "CONSISTENT"
    m76_findings_overridden: false
    m76_contradictions_detected: false
    contradiction_id: "none"
    m80_only_deferred_candidate: false
    derived_update_authorized_by_m77: false
    derived_update_executable_in_m78: false
    cleanup_authorized_by_77_1: false
    physical_cleanup_performed: false
    notes: "Protected canonical security authority."
```
