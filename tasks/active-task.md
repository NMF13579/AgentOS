---
task_id: task-m40-single-role-guard-mvp
task_number: "40.1.0"
task_name: Single-Role Execution Guard MVP
milestone: M40
state: completed
mode: EXECUTION
repository: AgentOS
branch: dev
task:
  id: task-m40-single-role-guard-mvp
  goal: >
    Implement Single-Role Execution Guard to prevent role mixing (e.g. Auditor + Implementor).
    Ensure each agent execution operates under exactly one declared role with clear boundaries.
  expected_result: >
    Policy created, schema defined, checker script implemented, fixtures added, and integrated into validation flow.
  in_scope:
    - docs/SINGLE-ROLE-EXECUTION-POLICY.md
    - schemas/execution-role.schema.json
    - scripts/check-single-role-execution.py
    - tests/fixtures/single-role-execution/
    - templates/role-handoff-request.md
    - reports/m40-single-role-execution-evidence-report.md
    - scripts/agentos-validate.py
    - tasks/active-task.md
  out_of_scope:
    - multi-agent orchestration
    - automatic role switching
  files_or_areas:
    - docs/
    - schemas/
    - scripts/
    - tests/fixtures/
    - templates/
    - reports/
  risk_level: MEDIUM
  risk_reason: "Changes core validation flow and adds new enforcement rules."
  requires_owner_approval: false
  rollback_plan: "Git restore modified files."
  acceptance_criteria:
    - "Checker script correctly identifies role/scope violations"
    - "Maintainer cannot self-modify role authority"
    - "Implementor cannot weaken own verification authority"
    - "Integrated into agentos-validate.py"
  verification_plan:
    - "python3 scripts/check-single-role-execution.py tasks/active-task.md"
    - "python3 scripts/test-single-role-execution-fixtures.py"
    - "python3 scripts/agentos-validate.py all"
execution_role:
  role: maintainer
  mode: maintenance_scoped
  allowed_write_paths:
    - docs/SINGLE-ROLE-EXECUTION-POLICY.md
    - schemas/execution-role.schema.json
    - scripts/check-single-role-execution.py
    - tests/fixtures/single-role-execution/
    - templates/role-handoff-request.md
    - reports/m40-single-role-execution-evidence-report.md
    - scripts/agentos-validate.py
    - tasks/active-task.md
    - scripts/test-single-role-execution-fixtures.py
  forbidden_write_paths:
    - src/
  may_modify_files: true
  may_approve: false
  may_change_task_state: true
  may_create_handoff: true
scope_control:
  allowed_paths:
    - tasks/active-task.md
    - reports/
    - docs/
    - templates/
    - tests/fixtures/single-role-execution/
    - schemas/execution-role.schema.json
    - scripts/check-single-role-execution.py
    - scripts/agentos-validate.py
    - scripts/test-single-role-execution-fixtures.py
    - README.md
    - docs/guardrails.md
    - docs/architecture.md
  forbidden_paths:
    - src/
  allow_new_files: true
  allowed_new_files:
    - docs/SINGLE-ROLE-EXECUTION-POLICY.md
    - schemas/execution-role.schema.json
    - scripts/check-single-role-execution.py
    - templates/role-handoff-request.md
    - reports/m40-single-role-execution-evidence-report.md
    - scripts/test-single-role-execution-fixtures.py
    - tests/fixtures/single-role-execution/valid/valid-auditor-readonly-report-only.md
    - tests/fixtures/single-role-execution/valid/valid-implementor-scoped-write.md
    - tests/fixtures/single-role-execution/valid/valid-planner-plan-only.md
    - tests/fixtures/single-role-execution/valid/valid-tutor-explain-only.md
    - tests/fixtures/single-role-execution/valid/valid-researcher-research-only.md
    - tests/fixtures/single-role-execution/valid/valid-maintainer-maintenance-scoped.md
    - tests/fixtures/single-role-execution/invalid/invalid-missing-execution-role.md
    - tests/fixtures/single-role-execution/invalid/invalid-unknown-role.md
    - tests/fixtures/single-role-execution/invalid/invalid-auditor-with-scoped-write.md
    - tests/fixtures/single-role-execution/invalid/invalid-broad-write-path-root.md
    - tests/fixtures/single-role-execution/invalid/invalid-role-scope-too-many-paths.md
    - tests/fixtures/single-role-execution/invalid/invalid-maintainer-self-policy-edit.md
    - tests/fixtures/single-role-execution/changed-files/auditor-report-only-pass.txt
    - tests/fixtures/single-role-execution/changed-files/auditor-modifies-src-fail.txt
    - tests/fixtures/single-role-execution/changed-files/implementor-in-scope-pass.txt
    - tests/fixtures/single-role-execution/changed-files/implementor-modifies-validator-needs-review.txt
    - tests/fixtures/single-role-execution/changed-files/maintainer-self-policy-edit-fail.txt
    - tests/fixtures/single-role-execution/changed-files/maintainer-normal-doc-pass.txt
  forbidden_new_files:
  allow_modify_existing: true
  allow_deletes: false
  allow_renames: false
  sensitive_paths:
    - scripts/agentos-validate.py
---

# Task 40.1.0 — Single-Role Execution Guard MVP
