---
task_id: task-m39-4-1-metadata
task_number: "39.4.1"
task_name: Version / Changelog / Release Notes
milestone: M39
state: completed
mode: EXECUTION
repository: AgentOS
branch: dev
task:
  id: task-m39-4-1-metadata
  goal: >
    Create or update release candidate metadata for M39: VERSION, CHANGELOG.md, and docs/release-notes.md.
    Clearly distinguish the release candidate from final public release completion.
  expected_result: >
    Release metadata files created or updated; reports/m39-version-changelog-release-notes-report.md created.
  in_scope:
    - VERSION
    - CHANGELOG.md
    - docs/release-notes.md
    - reports/m39-version-changelog-release-notes-report.md
    - tasks/active-task.md
  out_of_scope:
    - modifying first-user docs
    - modifying scripts
    - running smoke tests
  files_or_areas:
    - docs/
    - reports/
    - .
  risk_level: LOW
  risk_reason: "Safe release metadata preparation."
  requires_owner_approval: false
  rollback_plan: "Git restore modified metadata files."
  acceptance_criteria:
    - "VERSION uses rc format"
    - "CHANGELOG.md includes M39 entry"
    - "docs/release-notes.md exists"
    - "no unsupported claims found in metadata"
  verification_plan:
    - "grep -Eq \"^[0-9]+\\.[0-9]+\\.[0-9]+-rc\\.[0-9]+$\" VERSION"
    - "python3 scripts/agentos-validate.py all"
scope_control:
  allowed_paths:
    - tasks/active-task.md
    - reports/
    - docs/
    - VERSION
    - CHANGELOG.md
  forbidden_paths:
    - src/
    - scripts/
    - schemas/
  allow_new_files: true
  allowed_new_files:
    - VERSION
    - CHANGELOG.md
    - docs/release-notes.md
    - reports/m39-version-changelog-release-notes-report.md
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
    - VERSION
    - CHANGELOG.md
    - docs/release-notes.md
    - reports/m39-version-changelog-release-notes-report.md
    - tasks/active-task.md
  forbidden_write_paths:
    - src/
    - scripts/
  may_modify_files: true
  may_approve: false
  may_change_task_state: true
  may_create_handoff: true
---

# Task 39.4.1 — Version / Changelog / Release Notes
