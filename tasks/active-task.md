---
task_id: task-m35-fixup-intake
task_number: "35.1.1"
task_name: M35 MVP Fixup Intake and Scope Lock
milestone: M35
state: active
mode: EXECUTION
repository: AgentOS
branch: dev
---

# Task 35.1.1 — M35 MVP Fixup Intake and Scope Lock

M35 starts after M34 completion review concluded:

- M34_MVP_NOT_READY
- M34_COMPLETION_REVIEW_COMPLETE

M35 purpose:

Fix M34-proven MVP release-readiness blockers only.

Do not add new product features.

Do not start M36 work.

Do not execute 35.1.1 as part of Task 35.1.0.

scope_control:
  allowed_paths:
    - reports/
    - tasks/active-task.md
    - scripts/
    - schemas/
    - templates/
    - examples/
  forbidden_paths:
    - docs/
    - prompts/
    - data/
    - tests/
  allow_new_files: true
  allowed_new_files:
    - reports/m35-fixup-intake.md
    - reports/m35-validation-failure-inspection.md
    - reports/m35-active-task-run-all-repair.md
    - reports/m35-example-smoke-failure-inspection.md
    - reports/m35-example-smoke-repair.md
    - reports/m35-unified-validation-inspection.md
    - reports/m35-unified-validation-repair.md
    - reports/m35-mvp-audit-entrypoint-report.md
    - reports/m35-revalidation-matrix.md
    - reports/m35-mvp-fixup-evidence-report.md
    - scripts/audit-mvp-readiness.py
  forbidden_new_files:
  allow_modify_existing: true
  allow_deletes: false
  allow_renames: false
  sensitive_paths:
    - scripts/agentos-validate.py
    - schemas/task.schema.json
