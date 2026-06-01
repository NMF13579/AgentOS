---
task:
  id: "task-77.6"
  goal: "Create reports/m77-human-checkpoint-requirements.md"
  expected_result: "Human checkpoint requirements package for all cleanup items requiring human review before M78 or M80."
  in_scope:
    - "Reading reports/m77-rollback-plan.md"
    - "Reading reports/m77-prewrite-check.md"
    - "Reading reports/m77-cleanup-plan.md"
    - "Reading reports/m77-protected-artifact-review.md"
    - "Reading reports/m77-classification-review.md"
    - "Reading M76 source reports (read-only)"
    - "Creating reports/m77-human-checkpoint-requirements.md"
  out_of_scope:
    - "Physical cleanup of any files"
    - "Creating approval or simulating approval"
    - "Creating human checkpoint artifact as agent"
    - "Authorizing cleanup"
    - "Executing rollback"
    - "Creating M77 completion review"
    - "Creating M78, M80, M81 artifacts"
    - "Starting M78, M80, M81"
  files_or_areas:
    - "tasks/active-task.md"
    - "reports/m77-human-checkpoint-requirements.md"
  risk_level: "LOW"
  risk_reason: "Read-only checkpoint requirements documentation. One new file created. No files deleted or modified."
  requires_owner_approval: false
  rollback_plan: "Delete reports/m77-human-checkpoint-requirements.md and revert tasks/active-task.md."
  acceptance_criteria:
    - "reports/m77-human-checkpoint-requirements.md exists and is readable"
    - "checkpoint_requirement_is_approval: false"
    - "approval_claim_created: false"
    - "agent_created_human_checkpoint: false"
    - "cleanup_authorized_by_77_6: false"
    - "physical_cleanup_occurred: false"
    - "m76_findings_overridden: false"
    - "Human Summary consistent with machine-readable fields"
    - "FINAL_STATUS is one of: M77_HUMAN_CHECKPOINT_REQUIREMENTS_COMPLETE | M77_HUMAN_CHECKPOINT_REQUIREMENTS_COMPLETE_WITH_WARNINGS | M77_HUMAN_CHECKPOINT_REQUIREMENTS_BLOCKED"
  verification_plan:
    - "grep -E 'FINAL_STATUS' reports/m77-human-checkpoint-requirements.md"
    - "grep -E 'may_prepare_m77_7' reports/m77-human-checkpoint-requirements.md"
    - "grep -E 'approval_claim_created: false' reports/m77-human-checkpoint-requirements.md"
    - "grep -E 'physical_cleanup_occurred: false' reports/m77-human-checkpoint-requirements.md"
---
