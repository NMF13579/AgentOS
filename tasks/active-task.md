---
task_id: task-m37-pilot-readiness-package
task_number: "37.1.1"
task_name: M37 Pilot Readiness Package
milestone: M37
state: completed
mode: EXECUTION
repository: AgentOS
branch: dev
task:
  id: task-m37-pilot-readiness-package
  goal: >
    Complete the full M37 Pilot Readiness documentation and fixture package sequentially.
  expected_result: >
    All pilot docs (scope, safety, eligibility, onboarding, non-claims), templates, and smoke fixtures created and passing audit.
  in_scope:
    - docs/pilot-*.md
    - templates/pilot-*.md
    - tests/fixtures/pilot-smoke/
    - reports/m37-*.md
    - .github/workflows/agentos-validation.yml
  out_of_scope:
    - scripts/
    - schemas/
  files_or_areas:
    - docs/
    - templates/
    - tests/fixtures/
    - reports/
  risk_level: LOW
  risk_reason: "Documentation-heavy task with safe fixtures."
  requires_owner_approval: false
  rollback_plan: "Git restore modified files."
  acceptance_criteria:
    - "docs/pilot-scope.md created"
    - "docs/pilot-safety-boundaries.md created"
    - "docs/pilot-eligibility-policy.md created"
    - "docs/pilot-onboarding.md created"
    - "templates/pilot-feedback.md created"
    - "docs/pilot-support-escalation.md created"
    - "reports/m37-pilot-smoke-report.md created"
    - "docs/pilot-non-claims.md created"
    - "reports/m37-pilot-readiness-evidence-report.md created"
  verification_plan:
    - "python3 scripts/agentos-validate.py all"
    - "bash scripts/run-all.sh"
scope_control:
  allowed_paths:
    - tasks/active-task.md
    - docs/
    - templates/
    - tests/fixtures/pilot-smoke/
    - reports/
    - .github/workflows/agentos-validation.yml
  forbidden_paths:
    - scripts/
    - schemas/
  allow_new_files: true
  allowed_new_files:
    - docs/pilot-scope.md
    - docs/pilot-safety-boundaries.md
    - docs/pilot-eligibility-policy.md
    - docs/pilot-onboarding.md
    - docs/pilot-support-escalation.md
    - docs/pilot-non-claims.md
    - templates/pilot-feedback.md
    - templates/pilot-issue-report.md
    - templates/pilot-validation-failure-report.md
    - tests/fixtures/pilot-smoke/README.md
    - reports/m37-pilot-smoke-report.md
    - reports/m37-pilot-readiness-evidence-report.md
    - reports/m37-completion-review.md
  forbidden_new_files:
  allow_modify_existing: true
  allow_deletes: false
  allow_renames: false
  sensitive_paths:
    - .github/workflows/agentos-validation.yml
---

# Task 37.1.1 — M37 Pilot Readiness Package
