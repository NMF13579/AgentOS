---
task:
  id: "task-76.1"
  goal: "Perform read-only source facts intake and evidence inventory for M68–M75 reports, producing reports/m76-optimization-intake.md."
  expected_result: "Create reports/m76-optimization-intake.md containing detailed inventory results, baseline metrics, and validation checks."
  in_scope:
    - "Checking that reports/ directory exists"
    - "Reading reports/m76-m75-completion-intake.md"
    - "Checking expected M75 source reports"
    - "Listing M68–M74 source report groups"
    - "Checking git metadata and checking premature downstream M76/M77/M81 artifacts"
    - "Creating reports/m76-optimization-intake.md"
  out_of_scope:
    - "Physical deletion, renaming, or moving of any files"
    - "Modifying scripts or runtime code"
    - "Creating cleanup candidates, baselines, risk maps, or scope locks"
    - "Starting subsequent tasks (76.2+) or milestones (M77, M81)"
  files_or_areas:
    - "tasks/active-task.md"
    - "reports/m76-optimization-intake.md"
  risk_level: "LOW"
  risk_reason: "This is a read-only source facts intake and baseline reporting task. No files are modified or deleted."
  requires_owner_approval: false
  rollback_plan: "Discard changes to tasks/active-task.md and delete reports/m76-optimization-intake.md."
  acceptance_criteria:
    - "reports/m76-optimization-intake.md exists and is readable"
    - "The report inventories expected M75 reports and M68-M74 groups"
    - "The report records git metadata for checked files"
    - "The report verifies premature downstream M76/M77/M81 artifacts are absent"
    - "The report has FINAL_STATUS: M76_OPTIMIZATION_INTAKE_COMPLETE_WITH_WARNINGS"
    - "All boundary fields (approval_claim_created, physical_cleanup_occurred, etc.) are false"
  verification_plan:
    - "python3 scripts/validate-task.py"
    - "python3 scripts/audit-agentos.py"
    - "git status"
---
