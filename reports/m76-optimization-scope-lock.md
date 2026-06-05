# M76.6 - Optimization Scope Lock

## Title
- Task: `76.6 - Optimization Scope Lock`
- Mode: read-only scope lock / cleanup planning boundary

## Purpose
This report locks the M76 optimization scope for future M77 planning.
It preserves blocked unknowns, protected boundaries, human checkpoint requirements, low-risk planning candidates, and the no-cleanup boundary.
It does not authorize cleanup, approval, or M77 start.

## 76.5 Human Checkpoint Plan Check
- `reports/m76-human-checkpoint-plan.md` exists and is readable.
- `m76_5_final_status_detected: "M76_HUMAN_CHECKPOINT_PLAN_COMPLETE_WITH_WARNINGS"`
- `m76_5_readiness_detected: "true_with_warnings"`
- 76.5 preconditions passed.

## 76.4 Risk Map Check
- `reports/m76-optimization-risk-map.md` exists and is readable.
- `m76_4_final_status_detected: "M76_OPTIMIZATION_RISK_MAP_COMPLETE_WITH_WARNINGS"`
- `m76_4_readiness_detected: "true_with_warnings"`
- 76.4 preconditions passed.

## Scope Lock Method
- Keep the risk map, checkpoint plan, and baseline as read-only inputs.
- Use the stricter group when a candidate could fit more than one category.
- Keep unknown-blocked items blocked as reference context only.
- Keep protected/canonical items out of executable cleanup planning.
- Keep human checkpoint items non-executable until a future human decision.
- Keep low-risk candidates as planning eligibility only, not cleanup authorization.

## In Scope for M77 Planning
- 0 candidates are placed here as executable planning scope.
- Future M77 planning may still reference the low-risk candidates below, but this scope lock does not authorize cleanup.

## Blocked from M77 Planning
- 3 unknown-blocked candidates remain blocked reference only.

## Requires Human Checkpoint Before Cleanup
- 43 candidates require future human review before any cleanup.

## Protected Do Not Touch
- 6 protected/canonical candidates remain do-not-touch.

## Unknown Blocked
- Unknown-blocked candidates remain blocked and cannot become executable cleanup items.

## Safe Read-Only Reference
- No separate safe-readonly candidates were identified in 76.4.

## Low-Risk Cleanup Planning Candidates
- 6 tracked bytecode cache candidates remain eligible only for future cleanup planning.
- Future M77 planning must still define exact target path, planned action, validation command, rollback plan, and rollback validation command.

## Scope Expansion Boundary
- Scope expansion is not allowed without human review.
- M77 may not add new executable cleanup targets that were not visible in this scope lock.
- M77 may carry unknowns only as blocked/reference context.
- M76 scope lock is not permission to perform physical cleanup.

## Cleanup Authorization Boundary
- 76.6 does not authorize cleanup.
- 76.6 does not approve deletion.
- 76.6 does not approve archiving.
- 76.6 does not approve script consolidation.
- 76.6 does not approve bootstrap compression.
- 76.6 does not create approval.

## M77 Boundary
- 76.6 does not create M77 cleanup plan.
- 76.6 does not create M77 task briefs.
- 76.6 does not start M77.
- M77 still requires separate human review before planning or execution.

## M81 Boundary
- 76.6 does not start M81.
- 76.6 does not create M81 artifacts.
- 76.6 does not create M81 task briefs.
- 76.6 does not approve operator release candidate planning.

## Premature Artifact Check
- `downstream_m76_artifacts_exist: false`
- `m77_artifacts_exist: false`
- `m81_artifacts_exist: false`
- `m81_task_briefs_exist: false`

## Boundary Check
- `approval_claim_created: false`
- `lifecycle_mutation_occurred: false`
- `repair_authorized: false`
- `fix_tasks_created: false`
- `physical_cleanup_occurred: false`
- `files_deleted: false`
- `files_moved: false`
- `files_renamed: false`
- `files_archived: false`
- `files_compressed: false`
- `scripts_consolidated: false`
- `docs_compressed: false`
- `m77_started: false`
- `m81_started: false`

## Blockers
- `blocker_codes:`
  - `none`

## Warnings
- `warning_codes:`
  - `LOW_RISK_PLANNING_CANDIDATES_PRESENT`
  - `UNKNOWN_BLOCKED_REFERENCES_PRESENT`
  - `PROTECTED_DO_NOT_TOUCH_REFERENCES_PRESENT`
  - `REQUIRES_HUMAN_CHECKPOINT_REFERENCES_PRESENT`
  - `M76_5_WARNINGS_CARRIED_FORWARD`

## Local Final Status
- `FINAL_STATUS: "M76_OPTIMIZATION_SCOPE_LOCK_REPORT_COMPLETE_WITH_WARNINGS"`

## Readiness for 76.7
- `may_prepare_m76_7: "true_with_warnings"`

## Final Boundary Statement
Task 76.6 only creates the optimization scope lock report.
It does not authorize cleanup, does not create approval, does not lower risk, does not start 76.7, M77, or M81, and does not create M77 task briefs.
Human review remains required.

### Machine-Readable Metadata
```yaml
task_id: "76.6"
task_name: "Optimization Scope Lock"
reports_directory_exists: true
input_file_checkpoint_plan: "reports/m76-human-checkpoint-plan.md"
input_file_risk_map: "reports/m76-optimization-risk-map.md"
m76_5_checkpoint_plan_exists: true
m76_5_checkpoint_plan_readable: true
m76_5_final_status_detected: "M76_HUMAN_CHECKPOINT_PLAN_COMPLETE_WITH_WARNINGS"
m76_5_final_status_acceptable: true
m76_5_readiness_detected: "true_with_warnings"
m76_5_readiness_acceptable: true
m76_4_risk_map_exists: true
m76_4_risk_map_readable: true
scope_lock_created: true
scope_lock_is_cleanup_authorization: false
scope_lock_is_approval: false
scope_lock_starts_m77: false
scope_lock_creates_m77_task_briefs: false
protected_canonical_cleanup_authorized: false
future_m77_planning_scope_only: true
unknown_targets_blocked: true
scope_expansion_allowed_without_human_review: false
candidate_count_total: 58
scope_lock_item_count: 58
in_scope_for_m77_planning_count: 0
blocked_from_m77_planning_count: 3
requires_human_checkpoint_before_cleanup_count: 43
protected_do_not_touch_count: 6
unknown_blocked_count: 3
safe_readonly_reference_count: 0
low_risk_cleanup_planning_candidate_count: 6
unknown_blocked_executable_cleanup_count: 0
protected_do_not_touch_executable_cleanup_count: 0
cleanup_authorized_by_76_6: false
downstream_m76_artifacts_exist: false
m77_artifacts_exist: false
m77_task_briefs_created: false
m81_artifacts_exist: false
m81_task_briefs_exist: false
approval_claim_created: false
lifecycle_mutation_occurred: false
repair_authorized: false
fix_tasks_created: false
physical_cleanup_occurred: false
files_deleted: false
files_moved: false
files_renamed: false
files_archived: false
files_compressed: false
scripts_consolidated: false
docs_compressed: false
m77_started: false
m81_started: false
blocker_codes:
  - "none"
warning_codes:
  - "LOW_RISK_PLANNING_CANDIDATES_PRESENT"
  - "UNKNOWN_BLOCKED_REFERENCES_PRESENT"
  - "PROTECTED_DO_NOT_TOUCH_REFERENCES_PRESENT"
  - "REQUIRES_HUMAN_CHECKPOINT_REFERENCES_PRESENT"
  - "M76_5_WARNINGS_CARRIED_FORWARD"

scope_lock_items:
  - candidate_id: "M76-CAND-001"
    path: "scripts/__pycache__/agent-complete.cpython-314.pyc"
    risk_class_from_76_4: "LOW_RISK_CLEANUP"
    scope_group: "low_risk_cleanup_planning_candidates"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "not_required"
    executable_cleanup_item_in_m77: true
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Tracked bytecode cache can be considered in future planning only."
    notes: "One of six tracked pycache candidates."

  - candidate_id: "M76-CAND-002"
    path: "scripts/__pycache__/agent-fail.cpython-314.pyc"
    risk_class_from_76_4: "LOW_RISK_CLEANUP"
    scope_group: "low_risk_cleanup_planning_candidates"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "not_required"
    executable_cleanup_item_in_m77: true
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Tracked bytecode cache can be considered in future planning only."
    notes: "One of six tracked pycache candidates."

  - candidate_id: "M76-CAND-003"
    path: "scripts/__pycache__/agent-next.cpython-314.pyc"
    risk_class_from_76_4: "LOW_RISK_CLEANUP"
    scope_group: "low_risk_cleanup_planning_candidates"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "not_required"
    executable_cleanup_item_in_m77: true
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Tracked bytecode cache can be considered in future planning only."
    notes: "One of six tracked pycache candidates."

  - candidate_id: "M76-CAND-004"
    path: "scripts/__pycache__/generate-task-contract.cpython-314.pyc"
    risk_class_from_76_4: "LOW_RISK_CLEANUP"
    scope_group: "low_risk_cleanup_planning_candidates"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "not_required"
    executable_cleanup_item_in_m77: true
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Tracked bytecode cache can be considered in future planning only."
    notes: "One of six tracked pycache candidates."

  - candidate_id: "M76-CAND-005"
    path: "scripts/__pycache__/validate-task.cpython-314.pyc"
    risk_class_from_76_4: "LOW_RISK_CLEANUP"
    scope_group: "low_risk_cleanup_planning_candidates"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "not_required"
    executable_cleanup_item_in_m77: true
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Tracked bytecode cache can be considered in future planning only."
    notes: "One of six tracked pycache candidates."

  - candidate_id: "M76-CAND-006"
    path: "scripts/__pycache__/validate-verification.cpython-314.pyc"
    risk_class_from_76_4: "LOW_RISK_CLEANUP"
    scope_group: "low_risk_cleanup_planning_candidates"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "not_required"
    executable_cleanup_item_in_m77: true
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Tracked bytecode cache can be considered in future planning only."
    notes: "One of six tracked pycache candidates."

  - candidate_id: "M76-CAND-007"
    path: "scripts/audit-m27 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-001"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Duplicate audit script copy needs future human review before any deletion."
    notes: "Part of the audit-script duplicate cluster."

  - candidate_id: "M76-CAND-008"
    path: "scripts/audit-m27-level1 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-001"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Duplicate audit script copy needs future human review before any deletion."
    notes: "Part of the audit-script duplicate cluster."

  - candidate_id: "M76-CAND-009"
    path: "scripts/audit-metadata-consistency 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-001"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Duplicate audit script copy needs future human review before any deletion."
    notes: "Part of the audit-script duplicate cluster."

  - candidate_id: "M76-CAND-010"
    path: "scripts/audit-pre-merge-corridor 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-001"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Duplicate audit script copy needs future human review before any deletion."
    notes: "Part of the audit-script duplicate cluster."

  - candidate_id: "M76-CAND-011"
    path: "scripts/audit-validation-integration 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-001"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Duplicate audit script copy needs future human review before any deletion."
    notes: "Part of the audit-script duplicate cluster."

  - candidate_id: "M76-CAND-012"
    path: "scripts/build-index 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-002"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Duplicate index builder copy needs future human review before any deletion."
    notes: "Single duplicate script candidate."

  - candidate_id: "M76-CAND-013"
    path: "scripts/check-commit-push-preconditions 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-003"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Duplicate validation copy needs future human review before any deletion."
    notes: "Single duplicate script candidate."

  - candidate_id: "M76-CAND-014"
    path: "scripts/check-github-platform-enforcement 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-004"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Duplicate validation copy needs future human review before any deletion."
    notes: "Single duplicate script candidate."

  - candidate_id: "M76-CAND-015"
    path: "scripts/check-pre-merge-scope 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-005"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Duplicate pre-merge checker copy needs future human review before any deletion."
    notes: "Single duplicate script candidate."

  - candidate_id: "M76-CAND-016"
    path: "scripts/check-scope-compliance 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-006"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Duplicate scope checker copy needs future human review before any deletion."
    notes: "Single duplicate script candidate."

  - candidate_id: "M76-CAND-017"
    path: "scripts/test-ci-advisory-config 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-007"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Duplicate CI-advisory copy needs future human review before any deletion."
    notes: "Single duplicate script candidate."

  - candidate_id: "M76-CAND-018"
    path: "scripts/test-commit-push-preconditions-fixtures 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-008"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Duplicate fixture copy needs future human review before any deletion."
    notes: "Part of the fixture duplicate cluster."

  - candidate_id: "M76-CAND-019"
    path: "scripts/test-enforcement-fixtures 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-008"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Duplicate fixture copy needs future human review before any deletion."
    notes: "Part of the fixture duplicate cluster."

  - candidate_id: "M76-CAND-020"
    path: "scripts/test-m22-guardrails 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-008"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Duplicate fixture copy needs future human review before any deletion."
    notes: "Part of the fixture duplicate cluster."

  - candidate_id: "M76-CAND-021"
    path: "scripts/test-m27-level1-fixtures 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-008"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Duplicate fixture copy needs future human review before any deletion."
    notes: "Part of the fixture duplicate cluster."

  - candidate_id: "M76-CAND-022"
    path: "scripts/test-pre-merge-corridor-fixtures 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-009"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Duplicate pre-merge fixture copy needs future human review before any deletion."
    notes: "Part of the pre-merge fixture duplicate cluster."

  - candidate_id: "M76-CAND-023"
    path: "scripts/test-pre-merge-scope-fixtures 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-009"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Duplicate pre-merge fixture copy needs future human review before any deletion."
    notes: "Part of the pre-merge fixture duplicate cluster."

  - candidate_id: "M76-CAND-024"
    path: "scripts/test-scope-compliance-fixtures 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-010"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Duplicate scope-compliance fixture copy needs future human review before any deletion."
    notes: "Single duplicate script candidate."

  - candidate_id: "M76-CAND-025"
    path: "scripts/validate-boundary-claims 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-011"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Duplicate validator copy needs future human review before any deletion."
    notes: "Single duplicate script candidate."

  - candidate_id: "M76-CAND-026"
    path: "scripts/validate-frontmatter 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-012"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Duplicate validator copy needs future human review before any deletion."
    notes: "Single duplicate script candidate."

  - candidate_id: "M76-CAND-027"
    path: "scripts/validate-index 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-013"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Duplicate validator copy needs future human review before any deletion."
    notes: "Single duplicate script candidate."

  - candidate_id: "M76-CAND-028"
    path: "scripts/validate-required-sections 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-014"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Duplicate validator copy needs future human review before any deletion."
    notes: "Single duplicate script candidate."

  - candidate_id: "M76-CAND-029"
    path: "scripts/validate-status-semantics 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-015"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Duplicate validator copy needs future human review before any deletion."
    notes: "Single duplicate script candidate."

  - candidate_id: "M76-CAND-030"
    path: "scripts/agent-complete.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-016"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Legacy entrypoint may still be used by human or CI workflows."
    notes: "Legacy entrypoint."

  - candidate_id: "M76-CAND-031"
    path: "scripts/agent-fail.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-016"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Legacy entrypoint may still be used by human or CI workflows."
    notes: "Legacy entrypoint."

  - candidate_id: "M76-CAND-032"
    path: "scripts/agent-next.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-016"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Legacy entrypoint may still be used by human or CI workflows."
    notes: "Legacy entrypoint."

  - candidate_id: "M76-CAND-033"
    path: "scripts/agentos.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-017"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Legacy entrypoint may still be used by human or CI workflows."
    notes: "Legacy entrypoint."

  - candidate_id: "M76-CAND-034"
    path: "scripts/run-active-task.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-017"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Legacy entrypoint may still be used by human or CI workflows."
    notes: "Legacy entrypoint."

  - candidate_id: "M76-CAND-035"
    path: "HANDOFF 2.md"
    risk_class_from_76_4: "UNKNOWN_BLOCKED"
    scope_group: "unknown_blocked"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-018"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Purpose is uncertain, so it remains blocked reference only."
    notes: "Unknown-blocked copy file."

  - candidate_id: "M76-CAND-036"
    path: "llms.txt"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-019"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Bootstrap gateway document must not be changed without human review."
    notes: "Bootstrap document."

  - candidate_id: "M76-CAND-037"
    path: "AGENTS.md"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-019"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Bootstrap adapter document must not be changed without human review."
    notes: "Bootstrap document."

  - candidate_id: "M76-CAND-038"
    path: "CLAUDE.md"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-019"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Bootstrap adapter document must not be changed without human review."
    notes: "Bootstrap document."

  - candidate_id: "M76-CAND-039"
    path: "GEMINI.md"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-019"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Bootstrap adapter document must not be changed without human review."
    notes: "Bootstrap document."

  - candidate_id: "M76-CAND-040"
    path: "README.md"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-019"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Project readme must not be changed without human review."
    notes: "Bootstrap document."

  - candidate_id: "M76-CAND-041"
    path: "scripts/agentos-validate.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-020"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Active validation authority must not be changed without human review."
    notes: "Validation wrapper."

  - candidate_id: "M76-CAND-042"
    path: "scripts/check-dangerous-commands.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-020"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Active validation authority must not be changed without human review."
    notes: "Validation wrapper."

  - candidate_id: "M76-CAND-043"
    path: "scripts/check-execution-authorization.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-020"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Active validation authority must not be changed without human review."
    notes: "Validation wrapper."

  - candidate_id: "M76-CAND-044"
    path: "scripts/check-execution-readiness.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-020"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Active validation authority must not be changed without human review."
    notes: "Validation wrapper."

  - candidate_id: "M76-CAND-045"
    path: "scripts/check-human-approval.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-020"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Active validation authority must not be changed without human review."
    notes: "Validation wrapper."

  - candidate_id: "M76-CAND-046"
    path: "scripts/check-lifecycle-mutation.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-020"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Active validation authority must not be changed without human review."
    notes: "Validation wrapper."

  - candidate_id: "M76-CAND-047"
    path: "scripts/check-readiness-assertions.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-020"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Active validation authority must not be changed without human review."
    notes: "Validation wrapper."

  - candidate_id: "M76-CAND-048"
    path: "scripts/check-validator-authority-boundary.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-020"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Active validation authority must not be changed without human review."
    notes: "Validation wrapper."

  - candidate_id: "M76-CAND-049"
    path: "scripts/validate-lifecycle-apply.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-020"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Active validation authority must not be changed without human review."
    notes: "Validation wrapper."

  - candidate_id: "M76-CAND-050"
    path: "scripts/validate-task.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    scope_group: "requires_human_checkpoint_before_cleanup"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-020"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Active validation authority must not be changed without human review."
    notes: "Validation wrapper."

  - candidate_id: "M76-CAND-051"
    path: "reports/m71-script-inventory.json"
    risk_class_from_76_4: "UNKNOWN_BLOCKED"
    scope_group: "unknown_blocked"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-021"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Consumer and regeneration dependency are unknown, so this stays blocked reference only."
    notes: "Unknown-blocked derived index artifact."

  - candidate_id: "M76-CAND-052"
    path: "repo-map.md"
    risk_class_from_76_4: "UNKNOWN_BLOCKED"
    scope_group: "unknown_blocked"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-021"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Consumer and regeneration dependency are unknown, so this stays blocked reference only."
    notes: "Unknown-blocked derived index artifact."

  - candidate_id: "M76-CAND-053"
    path: "ROUTES-REGISTRY.md"
    risk_class_from_76_4: "PROTECTED_DO_NOT_TOUCH"
    scope_group: "protected_do_not_touch"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-022"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Protected canonical routing authority must remain do-not-touch."
    notes: "Protected canonical file."

  - candidate_id: "M76-CAND-054"
    path: "core-rules/MAIN.md"
    risk_class_from_76_4: "PROTECTED_DO_NOT_TOUCH"
    scope_group: "protected_do_not_touch"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-022"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Protected canonical governance authority must remain do-not-touch."
    notes: "Protected canonical file."

  - candidate_id: "M76-CAND-055"
    path: "state/MAIN.md"
    risk_class_from_76_4: "PROTECTED_DO_NOT_TOUCH"
    scope_group: "protected_do_not_touch"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-022"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Protected canonical state authority must remain do-not-touch."
    notes: "Protected canonical file."

  - candidate_id: "M76-CAND-056"
    path: "workflow/MAIN.md"
    risk_class_from_76_4: "PROTECTED_DO_NOT_TOUCH"
    scope_group: "protected_do_not_touch"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-022"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Protected canonical workflow authority must remain do-not-touch."
    notes: "Protected canonical file."

  - candidate_id: "M76-CAND-057"
    path: "quality/MAIN.md"
    risk_class_from_76_4: "PROTECTED_DO_NOT_TOUCH"
    scope_group: "protected_do_not_touch"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-022"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Protected canonical quality authority must remain do-not-touch."
    notes: "Protected canonical file."

  - candidate_id: "M76-CAND-058"
    path: "security/MAIN.md"
    risk_class_from_76_4: "PROTECTED_DO_NOT_TOUCH"
    scope_group: "protected_do_not_touch"
    source_evidence: "reports/m76-optimization-risk-map.md"
    checkpoint_id: "M76-CHK-022"
    executable_cleanup_item_in_m77: false
    cleanup_authorized_by_76_6: false
    approval_created_by_76_6: false
    risk_lowered_by_scope_lock: false
    reason: "Protected canonical security authority must remain do-not-touch."
    notes: "Protected canonical file."
```
