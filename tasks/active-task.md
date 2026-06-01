---
task:
  id: "task-76.2"
  goal: "Perform read-only cleanup candidate inventory and produce reports/m76-cleanup-candidate-inventory.md."
  expected_result: "Create reports/m76-cleanup-candidate-inventory.md containing detailed lists of candidates, categories, and boundary variables."
  in_scope:
    - "Checking that reports/ directory exists"
    - "Reading reports/m76-optimization-intake.md"
    - "Identifying candidate files (duplicate scripts, pycache files, legacy entrypoints, stale reports, bootstrap docs, validation wrappers, protected/canonical files, derived index files)"
    - "Assigning candidate confidence and proposed later actions"
    - "Creating reports/m76-cleanup-candidate-inventory.md"
  out_of_scope:
    - "Physical deletion, renaming, or moving of any files"
    - "Modifying scripts or runtime code"
    - "Creating pre-cleanup baselines, risk maps, or scope locks"
    - "Starting subsequent tasks (76.3+) or milestones (M77, M81)"
  files_or_areas:
    - "tasks/active-task.md"
    - "reports/m76-cleanup-candidate-inventory.md"
  risk_level: "LOW"
  risk_reason: "This is a read-only candidate identification and reporting task. No files are modified or deleted."
  requires_owner_approval: false
  rollback_plan: "Discard changes to tasks/active-task.md and delete reports/m76-cleanup-candidate-inventory.md."
  acceptance_criteria:
    - "reports/m76-cleanup-candidate-inventory.md exists and is readable"
    - "The report inventories all expected cleanup candidate categories"
    - "The report has correct candidate confidence and proposed action mapping"
    - "Protected/canonical files are explicitly categorized as DO_NOT_TOUCH"
    - "The report has FINAL_STATUS: M76_CLEANUP_CANDIDATE_INVENTORY_COMPLETE_WITH_WARNINGS"
    - "All boundary fields (approval_claim_created, physical_cleanup_occurred, etc.) are false"
  verification_plan:
    - "python3 scripts/validate-task.py"
    - "python3 scripts/audit-agentos.py"
    - "git status"
---
