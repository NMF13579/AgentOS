# M76.5 - Human Checkpoint Plan

## Title
- Task: `76.5 - Human Checkpoint Plan`
- Mode: read-only checkpoint planning / no approval creation

## Purpose
This report records where future human review is required before later M77, M78, or M80 cleanup planning or execution.
It does not approve anything, and it does not lower risk.

## 76.4 Risk Map Check
- `reports/m76-optimization-risk-map.md` exists and is readable.
- `m76_4_final_status_detected: "M76_OPTIMIZATION_RISK_MAP_COMPLETE_WITH_WARNINGS"`
- `m76_4_readiness_detected: "true_with_warnings"`
- 76.4 preconditions passed.

## Checkpoint Planning Method
- Use 76.4 risk classes as the source for checkpoint planning.
- Keep protected/canonical items protected.
- Keep unknown-blocked items visible as blocked reference only.
- Group only when the category, reason, and future human evidence are the same.
- Treat a checkpoint plan as future human work only, not approval.

## Required Human Checkpoint Categories
- `protected_canonical`: protected canonical docs that must not change without human review.
- `bootstrap_adapter`: startup and adapter docs that gate future agent bootstrap behavior.
- `validation_authority`: active validators and wrappers that affect authority or readiness checks.
- `other`: duplicate scripts and legacy entrypoints that may still be referenced by name.
- `unknown_blocked_reference`: items with unknown consumer or dependency status.
- No separate `workflow_codeowners` candidates were identified in 76.4.
- No separate `evidence_report_deletion` candidates were identified in 76.4.
- No separate `source_of_truth_structure` candidates were identified outside the protected and bootstrap sets.

## Checkpoint Requirements
- 22 checkpoint requirements are recorded below.
- 43 candidates remain in the `REQUIRES_HUMAN_CHECKPOINT` class.
- 6 candidates remain protected/canonical.
- 3 candidates remain unknown-blocked reference only.

## Protected/Canonical Checkpoint Requirements
- The six canonical governance files remain protected and require future human decision before any change.
- They are listed as protected, not approved for cleanup.

## Bootstrap/Adapter Checkpoint Requirements
- The five bootstrap documents remain checkpointed because changes can alter startup behavior and navigation authority.
- Compression, consolidation, or rewrite is not authorized here.

## Validation Authority Checkpoint Requirements
- The ten validation wrappers remain checkpointed because they affect validation authority, readiness, and boundary checks.
- Removal or modification needs future human review.

## Workflow/CODEOWNERS Checkpoint Requirements
- No workflow or CODEOWNERS candidates were identified in 76.4.
- This section is present for completeness only.

## Evidence/Report Deletion Checkpoint Requirements
- No evidence-report deletion candidates were identified in 76.4.
- This section is present for completeness only.

## Source-of-Truth Structure Checkpoint Requirements
- No separate source-of-truth structure candidates were identified beyond the protected and bootstrap sets.
- Any future structural change to source-of-truth routing or authority should still require human review.

## Unknown/Blocked Candidate Handling
- The unknown-blocked candidates stay blocked reference only.
- They are not executable, not approval-ready, and not cleanup-authorized.

## Non-Approval Boundary
- 76.5 does not authorize cleanup.
- 76.5 does not approve deletion.
- 76.5 does not approve archiving.
- 76.5 does not approve script consolidation.
- 76.5 does not approve bootstrap compression.
- 76.5 does not create approval.
- 76.5 does not start M77.
- Human review remains required.

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
- `scope_lock_created: false`
- `m77_started: false`
- `m81_started: false`

## Blockers
- `blocker_codes:`
  - `none`

## Warnings
- `warning_codes:`
  - `M76_4_WARNINGS_CARRIED_FORWARD`
  - `UNKNOWN_BLOCKED_REFERENCES_PRESENT`
  - `PROTECTED_CANONICAL_CHECKPOINTS_PRESENT`
  - `BOOTSTRAP_ADAPTER_CHECKPOINTS_PRESENT`
  - `VALIDATION_AUTHORITY_CHECKPOINTS_PRESENT`

## Local Final Status
- `FINAL_STATUS: "M76_HUMAN_CHECKPOINT_PLAN_COMPLETE_WITH_WARNINGS"`

## Readiness for 76.6
- `may_prepare_m76_6: "true_with_warnings"`

## Final Boundary Statement
Task 76.5 only documents where future human review is required.
It does not create approval, does not simulate approval, does not authorize cleanup, does not lower risk, and does not start 76.6, M77, or M81.

### Machine-Readable Metadata
```yaml
task_id: "76.5"
task_name: "Human Checkpoint Plan"
reports_directory_exists: true
input_file_risk_map: "reports/m76-optimization-risk-map.md"
m76_4_risk_map_exists: true
m76_4_risk_map_readable: true
m76_4_final_status_detected: "M76_OPTIMIZATION_RISK_MAP_COMPLETE_WITH_WARNINGS"
m76_4_final_status_acceptable: true
m76_4_readiness_detected: "true_with_warnings"
m76_4_readiness_acceptable: true
human_checkpoint_plan_created: true
checkpoint_requirement_count: 22
requires_human_checkpoint_candidate_count: 43
protected_canonical_checkpoint_count: 6
bootstrap_adapter_checkpoint_count: 5
validation_authority_checkpoint_count: 10
workflow_codeowners_checkpoint_count: 0
evidence_report_deletion_checkpoint_count: 0
source_of_truth_checkpoint_count: 0
unknown_blocked_reference_count: 3
agent_may_create_checkpoint: false
agent_may_simulate_approval: false
approval_already_exists: false
checkpoint_plan_is_approval: false
checkpoint_plan_authorizes_cleanup: false
checkpoint_plan_lowers_risk: false
cleanup_authorized_by_76_5: false
downstream_m76_artifacts_exist: false
m77_artifacts_exist: false
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
scope_lock_created: false
m77_started: false
m81_started: false
blocker_codes:
  - "none"
warning_codes:
  - "M76_4_WARNINGS_CARRIED_FORWARD"
  - "UNKNOWN_BLOCKED_REFERENCES_PRESENT"
  - "PROTECTED_CANONICAL_CHECKPOINTS_PRESENT"
  - "BOOTSTRAP_ADAPTER_CHECKPOINTS_PRESENT"
  - "VALIDATION_AUTHORITY_CHECKPOINTS_PRESENT"

checkpoint_requirements:
  - checkpoint_id: "M76-CHK-001"
    candidate_id: "category-level"
    path: "scripts/audit-* 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    checkpoint_category: "other"
    reason: "Duplicate macOS Finder copies of audit scripts can still be referenced by name, so deletion needs future human review."
    checkpoint_required_before_stage: "M78"
    required_human_evidence: "manual review record and explicit human approval note"
    agent_may_create_checkpoint: false
    agent_may_simulate_approval: false
    approval_already_exists: false
    cleanup_authorized_by_checkpoint_plan: false
    risk_lowered_by_checkpoint_plan: false
    notes: "Covers M76-CAND-007, M76-CAND-008, M76-CAND-009, M76-CAND-010, M76-CAND-011."

  - checkpoint_id: "M76-CHK-002"
    candidate_id: "M76-CAND-012"
    path: "scripts/build-index 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    checkpoint_category: "other"
    reason: "The copy of the index-building script may still be referenced by name, so removal needs future human review."
    checkpoint_required_before_stage: "M78"
    required_human_evidence: "manual review record and explicit human approval note"
    agent_may_create_checkpoint: false
    agent_may_simulate_approval: false
    approval_already_exists: false
    cleanup_authorized_by_checkpoint_plan: false
    risk_lowered_by_checkpoint_plan: false
    notes: "Single duplicate script candidate."

  - checkpoint_id: "M76-CHK-003"
    candidate_id: "M76-CAND-013"
    path: "scripts/check-commit-push-preconditions 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    checkpoint_category: "other"
    reason: "The copy of the commit/push precondition checker can affect validation chains if removed without review."
    checkpoint_required_before_stage: "M78"
    required_human_evidence: "reviewed diff approval"
    agent_may_create_checkpoint: false
    agent_may_simulate_approval: false
    approval_already_exists: false
    cleanup_authorized_by_checkpoint_plan: false
    risk_lowered_by_checkpoint_plan: false
    notes: "Single duplicate script candidate."

  - checkpoint_id: "M76-CHK-004"
    candidate_id: "M76-CAND-014"
    path: "scripts/check-github-platform-enforcement 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    checkpoint_category: "other"
    reason: "The copy of the GitHub platform enforcement script can overlap with CI-facing behavior and needs future human review."
    checkpoint_required_before_stage: "M78"
    required_human_evidence: "reviewed diff approval"
    agent_may_create_checkpoint: false
    agent_may_simulate_approval: false
    approval_already_exists: false
    cleanup_authorized_by_checkpoint_plan: false
    risk_lowered_by_checkpoint_plan: false
    notes: "Single duplicate script candidate."

  - checkpoint_id: "M76-CHK-005"
    candidate_id: "M76-CAND-015"
    path: "scripts/check-pre-merge-scope 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    checkpoint_category: "other"
    reason: "The copy of the pre-merge scope checker overlaps with pre-merge validation and needs future human review."
    checkpoint_required_before_stage: "M78"
    required_human_evidence: "reviewed diff approval"
    agent_may_create_checkpoint: false
    agent_may_simulate_approval: false
    approval_already_exists: false
    cleanup_authorized_by_checkpoint_plan: false
    risk_lowered_by_checkpoint_plan: false
    notes: "Single duplicate script candidate."

  - checkpoint_id: "M76-CHK-006"
    candidate_id: "M76-CAND-016"
    path: "scripts/check-scope-compliance 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    checkpoint_category: "other"
    reason: "The copy of the scope compliance checker overlaps with dispatcher behavior and needs future human review."
    checkpoint_required_before_stage: "M78"
    required_human_evidence: "reviewed diff approval"
    agent_may_create_checkpoint: false
    agent_may_simulate_approval: false
    approval_already_exists: false
    cleanup_authorized_by_checkpoint_plan: false
    risk_lowered_by_checkpoint_plan: false
    notes: "Single duplicate script candidate."

  - checkpoint_id: "M76-CHK-007"
    candidate_id: "M76-CAND-017"
    path: "scripts/test-ci-advisory-config 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    checkpoint_category: "other"
    reason: "The copy of the CI advisory test script can overlap with CI-facing behavior and needs future human review."
    checkpoint_required_before_stage: "M78"
    required_human_evidence: "manual review record and explicit human approval note"
    agent_may_create_checkpoint: false
    agent_may_simulate_approval: false
    approval_already_exists: false
    cleanup_authorized_by_checkpoint_plan: false
    risk_lowered_by_checkpoint_plan: false
    notes: "Single duplicate script candidate."

  - checkpoint_id: "M76-CHK-008"
    candidate_id: "category-level"
    path: "scripts/test-* 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    checkpoint_category: "other"
    reason: "These copies are still part of validation chains, so future deletion needs human review."
    checkpoint_required_before_stage: "M78"
    required_human_evidence: "manual review record and explicit human approval note"
    agent_may_create_checkpoint: false
    agent_may_simulate_approval: false
    approval_already_exists: false
    cleanup_authorized_by_checkpoint_plan: false
    risk_lowered_by_checkpoint_plan: false
    notes: "Covers M76-CAND-018, M76-CAND-019, M76-CAND-020, M76-CAND-021."

  - checkpoint_id: "M76-CHK-009"
    candidate_id: "category-level"
    path: "scripts/test-pre-merge-* 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    checkpoint_category: "other"
    reason: "These pre-merge fixture copies have CI overlap potential, so future deletion needs human review."
    checkpoint_required_before_stage: "M78"
    required_human_evidence: "manual review record and explicit human approval note"
    agent_may_create_checkpoint: false
    agent_may_simulate_approval: false
    approval_already_exists: false
    cleanup_authorized_by_checkpoint_plan: false
    risk_lowered_by_checkpoint_plan: false
    notes: "Covers M76-CAND-022, M76-CAND-023."

  - checkpoint_id: "M76-CHK-010"
    candidate_id: "M76-CAND-024"
    path: "scripts/test-scope-compliance-fixtures 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    checkpoint_category: "other"
    reason: "The copy of the scope compliance fixture test overlaps with dispatcher behavior and needs future human review."
    checkpoint_required_before_stage: "M78"
    required_human_evidence: "manual review record and explicit human approval note"
    agent_may_create_checkpoint: false
    agent_may_simulate_approval: false
    approval_already_exists: false
    cleanup_authorized_by_checkpoint_plan: false
    risk_lowered_by_checkpoint_plan: false
    notes: "Single duplicate script candidate."

  - checkpoint_id: "M76-CHK-011"
    candidate_id: "M76-CAND-025"
    path: "scripts/validate-boundary-claims 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    checkpoint_category: "other"
    reason: "The copy of the boundary claim validator overlaps with validation authority and needs future human review."
    checkpoint_required_before_stage: "M77"
    required_human_evidence: "reviewed diff approval"
    agent_may_create_checkpoint: false
    agent_may_simulate_approval: false
    approval_already_exists: false
    cleanup_authorized_by_checkpoint_plan: false
    risk_lowered_by_checkpoint_plan: false
    notes: "Single duplicate script candidate."

  - checkpoint_id: "M76-CHK-012"
    candidate_id: "M76-CAND-026"
    path: "scripts/validate-frontmatter 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    checkpoint_category: "other"
    reason: "The copy of the frontmatter validator overlaps with validation authority and needs future human review."
    checkpoint_required_before_stage: "M77"
    required_human_evidence: "reviewed diff approval"
    agent_may_create_checkpoint: false
    agent_may_simulate_approval: false
    approval_already_exists: false
    cleanup_authorized_by_checkpoint_plan: false
    risk_lowered_by_checkpoint_plan: false
    notes: "Single duplicate script candidate."

  - checkpoint_id: "M76-CHK-013"
    candidate_id: "M76-CAND-027"
    path: "scripts/validate-index 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    checkpoint_category: "other"
    reason: "The copy of the index validator overlaps with validation authority and needs future human review."
    checkpoint_required_before_stage: "M77"
    required_human_evidence: "reviewed diff approval"
    agent_may_create_checkpoint: false
    agent_may_simulate_approval: false
    approval_already_exists: false
    cleanup_authorized_by_checkpoint_plan: false
    risk_lowered_by_checkpoint_plan: false
    notes: "Single duplicate script candidate."

  - checkpoint_id: "M76-CHK-014"
    candidate_id: "M76-CAND-028"
    path: "scripts/validate-required-sections 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    checkpoint_category: "other"
    reason: "The copy of the required sections validator overlaps with validation authority and needs future human review."
    checkpoint_required_before_stage: "M77"
    required_human_evidence: "reviewed diff approval"
    agent_may_create_checkpoint: false
    agent_may_simulate_approval: false
    approval_already_exists: false
    cleanup_authorized_by_checkpoint_plan: false
    risk_lowered_by_checkpoint_plan: false
    notes: "Single duplicate script candidate."

  - checkpoint_id: "M76-CHK-015"
    candidate_id: "M76-CAND-029"
    path: "scripts/validate-status-semantics 3.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    checkpoint_category: "other"
    reason: "The copy of the status semantics validator overlaps with validation authority and needs future human review."
    checkpoint_required_before_stage: "M77"
    required_human_evidence: "reviewed diff approval"
    agent_may_create_checkpoint: false
    agent_may_simulate_approval: false
    approval_already_exists: false
    cleanup_authorized_by_checkpoint_plan: false
    risk_lowered_by_checkpoint_plan: false
    notes: "Single duplicate script candidate."

  - checkpoint_id: "M76-CHK-016"
    candidate_id: "category-level"
    path: "scripts/agent-*.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    checkpoint_category: "other"
    reason: "These legacy entrypoints may still be used by CI or human-facing workflows, so removal needs future human review."
    checkpoint_required_before_stage: "M78"
    required_human_evidence: "repository owner decision"
    agent_may_create_checkpoint: false
    agent_may_simulate_approval: false
    approval_already_exists: false
    cleanup_authorized_by_checkpoint_plan: false
    risk_lowered_by_checkpoint_plan: false
    notes: "Covers M76-CAND-030, M76-CAND-031, M76-CAND-032."

  - checkpoint_id: "M76-CHK-017"
    candidate_id: "category-level"
    path: "scripts/agentos.py and scripts/run-active-task.py"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    checkpoint_category: "other"
    reason: "These legacy entrypoints may still be user-facing or CI-facing, so removal needs future human review."
    checkpoint_required_before_stage: "M78"
    required_human_evidence: "repository owner decision"
    agent_may_create_checkpoint: false
    agent_may_simulate_approval: false
    approval_already_exists: false
    cleanup_authorized_by_checkpoint_plan: false
    risk_lowered_by_checkpoint_plan: false
    notes: "Covers M76-CAND-033, M76-CAND-034."

  - checkpoint_id: "M76-CHK-018"
    candidate_id: "M76-CAND-035"
    path: "HANDOFF 2.md"
    risk_class_from_76_4: "UNKNOWN_BLOCKED"
    checkpoint_category: "unknown_blocked_reference"
    reason: "The copy file has uncertain purpose, so it stays blocked as reference only until a human confirms its role."
    checkpoint_required_before_stage: "M78"
    required_human_evidence: "manual review record confirming purpose and dependency status"
    agent_may_create_checkpoint: false
    agent_may_simulate_approval: false
    approval_already_exists: false
    cleanup_authorized_by_checkpoint_plan: false
    risk_lowered_by_checkpoint_plan: false
    notes: "Unknown-blocked reference only."

  - checkpoint_id: "M76-CHK-019"
    candidate_id: "category-level"
    path: "bootstrap docs"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    checkpoint_category: "bootstrap_adapter"
    reason: "Bootstrap documents affect startup authority and should not be compressed or changed without future human review."
    checkpoint_required_before_stage: "M78"
    required_human_evidence: "human-authored checkpoint report or maintainer-signed approval"
    agent_may_create_checkpoint: false
    agent_may_simulate_approval: false
    approval_already_exists: false
    cleanup_authorized_by_checkpoint_plan: false
    risk_lowered_by_checkpoint_plan: false
    notes: "Covers M76-CAND-036, M76-CAND-037, M76-CAND-038, M76-CAND-039, M76-CAND-040."

  - checkpoint_id: "M76-CHK-020"
    candidate_id: "category-level"
    path: "scripts/* validation wrappers"
    risk_class_from_76_4: "REQUIRES_HUMAN_CHECKPOINT"
    checkpoint_category: "validation_authority"
    reason: "Active validation authority files should not be removed or modified without future human review."
    checkpoint_required_before_stage: "M77"
    required_human_evidence: "reviewed diff approval or repository owner decision"
    agent_may_create_checkpoint: false
    agent_may_simulate_approval: false
    approval_already_exists: false
    cleanup_authorized_by_checkpoint_plan: false
    risk_lowered_by_checkpoint_plan: false
    notes: "Covers M76-CAND-041 through M76-CAND-050."

  - checkpoint_id: "M76-CHK-021"
    candidate_id: "category-level"
    path: "derived navigation/index artifacts"
    risk_class_from_76_4: "UNKNOWN_BLOCKED"
    checkpoint_category: "unknown_blocked_reference"
    reason: "Derived navigation and index artifacts have unknown consumers or regeneration dependencies, so they stay blocked as reference only."
    checkpoint_required_before_stage: "M80"
    required_human_evidence: "manual review record confirming consumer and regeneration dependency status"
    agent_may_create_checkpoint: false
    agent_may_simulate_approval: false
    approval_already_exists: false
    cleanup_authorized_by_checkpoint_plan: false
    risk_lowered_by_checkpoint_plan: false
    notes: "Covers M76-CAND-051, M76-CAND-052."

  - checkpoint_id: "M76-CHK-022"
    candidate_id: "category-level"
    path: "protected canonical docs"
    risk_class_from_76_4: "PROTECTED_DO_NOT_TOUCH"
    checkpoint_category: "protected_canonical"
    reason: "Protected canonical documents are source-of-truth files and require future human decision before any change."
    checkpoint_required_before_stage: "M77"
    required_human_evidence: "repository owner decision or maintainer-signed approval"
    agent_may_create_checkpoint: false
    agent_may_simulate_approval: false
    approval_already_exists: false
    cleanup_authorized_by_checkpoint_plan: false
    risk_lowered_by_checkpoint_plan: false
    notes: "Covers M76-CAND-053, M76-CAND-054, M76-CAND-055, M76-CAND-056, M76-CAND-057, M76-CAND-058."
```
