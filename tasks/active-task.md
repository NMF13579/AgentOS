---
task:
  id: "task-76.3"
  goal: "Perform read-only baseline measurement of the repository state and produce reports/m76-pre-cleanup-baseline.md."
  expected_result: "Create reports/m76-pre-cleanup-baseline.md containing all 10 baseline fields, confidence metrics, and boundary checks."
  in_scope:
    - "Checking that reports/ directory exists"
    - "Reading reports/m76-cleanup-candidate-inventory.md"
    - "Measuring baseline count metrics (unknown files, duplicate scripts, legacy entrypoints, copy files, stale reports, bootstrap docs, validation entrypoints)"
    - "Deterministic counting of tracked pycache compiled files"
    - "Estimating prompt surface and adapter duplication counts as unknown"
    - "Creating reports/m76-pre-cleanup-baseline.md"
  out_of_scope:
    - "Physical deletion, renaming, or moving of any files"
    - "Modifying scripts or runtime code"
    - "Creating optimization risk maps or scope locks"
    - "Starting subsequent tasks (76.4+) or milestones (M77, M81)"
  files_or_areas:
    - "tasks/active-task.md"
    - "reports/m76-pre-cleanup-baseline.md"
  risk_level: "LOW"
  risk_reason: "This is a read-only baseline measurement and reporting task. No files are modified or deleted."
  requires_owner_approval: false
  rollback_plan: "Discard changes to tasks/active-task.md and delete reports/m76-pre-cleanup-baseline.md."
  acceptance_criteria:
    - "reports/m76-pre-cleanup-baseline.md exists and is readable"
    - "The report contains all 10 required baseline fields with confidence metrics"
    - "Unknown baseline metrics include honest reasons and block later claims"
    - "The report has FINAL_STATUS: M76_PRE_CLEANUP_BASELINE_COMPLETE_WITH_WARNINGS"
    - "All boundary fields (approval_claim_created, physical_cleanup_occurred, etc.) are false"
  verification_plan:
    - "python3 scripts/validate-task.py"
    - "python3 scripts/audit-agentos.py"
    - "git status"
---
