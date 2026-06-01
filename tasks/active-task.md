---
task:
  id: "task-76.1"
  goal: "Compile repository cleanup candidates and baseline current repository status without performing any physical cleanup."
  expected_result: "Create reports/m76-cleanup-candidates.md containing detailed lists of candidates, repository baseline metrics, and boundaries."
  in_scope:
    - "Identifying duplicate scripts ending with ' 3.py' under scripts/"
    - "Identifying tracked pycache bytecode files under scripts/__pycache__/"
    - "Identifying legacy entrypoint scripts under scripts/"
    - "Recording current repository baseline metrics"
    - "Creating reports/m76-cleanup-candidates.md"
  out_of_scope:
    - "Physical deletion, renaming, or moving of any files"
    - "Modifying scripts or runtime code"
    - "Starting subsequent tasks or milestones"
  files_or_areas:
    - "tasks/active-task.md"
    - "reports/m76-cleanup-candidates.md"
  risk_level: "LOW"
  risk_reason: "This is a read-only candidate identification and baseline reporting task. No files are modified or deleted."
  requires_owner_approval: false
  rollback_plan: "Discard changes to tasks/active-task.md and delete reports/m76-cleanup-candidates.md."
  acceptance_criteria:
    - "reports/m76-cleanup-candidates.md exists and is readable"
    - "The report correctly identifies the 23 duplicate scripts ending in ' 3.py'"
    - "The report correctly identifies the 6 tracked pycache files"
    - "The report lists the 5 legacy entrypoint scripts"
    - "The report records repo baseline metrics (git clean status, file counts)"
    - "The report has FINAL_STATUS: M76_CLEANUP_CANDIDATES_COMPLETE_WITH_WARNINGS"
    - "No physical file deletion or modification of runtime code occurred"
  verification_plan:
    - "python3 scripts/validate-task.py"
    - "python3 scripts/audit-agentos.py"
    - "git status"
---
