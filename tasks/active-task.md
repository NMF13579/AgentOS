---
task_id: task-m39-5-1-final-smoke
task_number: "39.5.1"
task_name: M39 Final Smoke
milestone: M39
state: completed
mode: EXECUTION
repository: AgentOS
branch: dev
task:
  id: task-m39-5-1-final-smoke
  goal: >
    Run a final smoke check for M39 Release Candidate usability and safety signals.
    Verify all reports, metadata, and docs exist and are free of unsupported claims.
  expected_result: >
    reports/m39-final-smoke.md created with result M39_FINAL_SMOKE_PASS.
  in_scope:
    - reports/m39-final-smoke.md
    - tasks/active-task.md
  out_of_scope:
    - modifying docs
    - modifying code
    - running final audit
  files_or_areas:
    - reports/
  risk_level: LOW
  risk_reason: "Read-only verification smoke test."
  requires_owner_approval: false
  rollback_plan: "Delete the created report."
  acceptance_criteria:
    - "reports/m39-final-smoke.md exists"
    - "VERSION uses rc format"
    - "no unsupported claims found in public docs"
  verification_plan:
    - "python3 scripts/agentos-validate.py all"
scope_control:
  allowed_paths:
    - tasks/active-task.md
    - reports/
    - README.md
    - VERSION
    - CHANGELOG.md
    - docs/
  forbidden_paths:
    - src/
    - scripts/
    - schemas/
  allow_new_files: true
  allowed_new_files:
    - reports/m39-final-smoke.md
  forbidden_new_files:
  allow_modify_existing: true
  allow_deletes: false
  allow_renames: false
  sensitive_paths:
    - scripts/agentos-validate.py
execution_role:
  role: maintainer
  mode: maintenance_scoped
  allowed_write_paths:
    - reports/m39-final-smoke.md
    - tasks/active-task.md
  forbidden_write_paths:
    - src/
    - scripts/
  may_modify_files: true
  may_approve: false
  may_change_task_state: true
  may_create_handoff: true
---

# Task 39.5.1 — M39 Final Smoke
