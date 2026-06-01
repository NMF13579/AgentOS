---
task:
  id: "task-76.4"
  goal: "Perform read-only risk classification of all cleanup candidates and produce reports/m76-optimization-risk-map.md."
  expected_result: "Create reports/m76-optimization-risk-map.md classifying all 58 candidates into allowed M76 risk classes."
  in_scope:
    - "Checking that reports/ directory exists"
    - "Reading reports/m76-cleanup-candidate-inventory.md"
    - "Reading reports/m76-pre-cleanup-baseline.md"
    - "Classifying every candidate into one of: SAFE_READONLY, LOW_RISK_CLEANUP, REQUIRES_HUMAN_CHECKPOINT, PROTECTED_DO_NOT_TOUCH, UNKNOWN_BLOCKED"
    - "Creating reports/m76-optimization-risk-map.md"
  out_of_scope:
    - "Physical deletion, renaming, or moving of any files"
    - "Modifying scripts or runtime code"
    - "Authorizing or creating cleanup plan"
    - "Creating human checkpoint plan or scope lock"
    - "Starting subsequent tasks (76.5+) or milestones (M77, M81)"
  files_or_areas:
    - "tasks/active-task.md"
    - "reports/m76-optimization-risk-map.md"
  risk_level: "LOW"
  risk_reason: "This is a read-only risk classification and reporting task. No files are modified or deleted."
  requires_owner_approval: false
  rollback_plan: "Discard changes to tasks/active-task.md and delete reports/m76-optimization-risk-map.md."
  acceptance_criteria:
    - "reports/m76-optimization-risk-map.md exists and is readable"
    - "All 58 candidates from 76.2 are classified in the risk map"
    - "Every candidate has exactly one valid risk class"
    - "Protected/canonical targets are PROTECTED_DO_NOT_TOUCH"
    - "cleanup_authorized_by_76_4: false on every item"
    - "The report has FINAL_STATUS: M76_OPTIMIZATION_RISK_MAP_COMPLETE_WITH_WARNINGS"
    - "All boundary fields (approval_claim_created, physical_cleanup_occurred, etc.) are false"
  verification_plan:
    - "python3 scripts/validate-task.py"
    - "python3 scripts/audit-agentos.py"
    - "git status"
---
