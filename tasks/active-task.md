---
task_id: task-governance-claim-guard
task_number: "37.11.0"
task_name: Add Rule — Governance Claim Guard (Readiness Assertions)
milestone: M37
state: completed
mode: EXECUTION
repository: AgentOS
branch: dev
task:
  id: task-governance-claim-guard
  goal: >
    Prevent premature readiness claims that bypass completion review decisions.
    Implement validation rule that requires explicit completion review result tokens.
  expected_result: >
    New rule implemented, integrated into validation flow, and passing for existing docs/reports (or identifying violations).
  in_scope:
    - scripts/agentos-validate.py
    - scripts/check-readiness-assertions.py
    - reports/governance-claim-guard-report.md
  out_of_scope:
    - docs/
    - templates/
  files_or_areas:
    - scripts/
    - reports/
  risk_level: LOW
  risk_reason: "Safe addition of validation rule."
  requires_owner_approval: false
  rollback_plan: "Git restore scripts."
  acceptance_criteria:
    - "scripts/check-readiness-assertions.py created"
    - "integrated into agentos-validate.py"
    - "honestly identifies current repository readiness claims"
  verification_plan:
    - "python3 scripts/check-readiness-assertions.py"
    - "python3 scripts/agentos-validate.py all"
scope_control:
  allowed_paths:
    - tasks/active-task.md
    - scripts/agentos-validate.py
    - scripts/check-readiness-assertions.py
    - reports/
    - README.md
    - docs/
  forbidden_paths:
    - src/
  allow_new_files: true
  allowed_new_files:
    - scripts/check-readiness-assertions.py
    - reports/governance-claim-guard-report.md
  forbidden_new_files:
  allow_modify_existing: true
  allow_deletes: false
  allow_renames: false
  sensitive_paths:
    - scripts/agentos-validate.py
---

# Task 37.11.0 — Governance Claim Guard (Readiness Assertions)
