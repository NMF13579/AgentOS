---
task_id: task-m36-6-0-scope-control-maintenance
task_number: "36.6.0"
task_name: Scope Control Maintenance Hotfix
milestone: M36
state: completed
mode: EXECUTION
repository: AgentOS
branch: dev
task:
  id: task-m36-6-0-scope-control-maintenance
  goal: >
    Исправить накопленный системный долг в блоке scope_control файла tasks/active-task.md:
    добавить все обязательные поля, которых не хватает для прохождения check-scope-compliance.py,
    а также включить в scope все отчёты, созданные в рамках M36 (36.4.1 и смежных задач),
    чтобы agentos-validate.py all возвращал PASS.
  expected_result: >
    tasks/active-task.md содержит полный и валидный блок scope_control.
    agentos-validate.py all → PASS.
    check-scope-compliance.py → PASS.
    Создан отчёт reports/m36-scope-control-maintenance-report.md.
  in_scope:
    - tasks/active-task.md
    - reports/
  out_of_scope:
    - scripts/
    - docs/
    - .github/
    - src/
  files_or_areas:
    - tasks/active-task.md
    - reports/m36-scope-control-maintenance-report.md
  risk_level: LOW
  risk_reason: >
    Изменяются только метаданные контракта (scope_control) и добавляется отчёт.
    Никакой логики, скриптов или защищённых путей не затрагивается.
  requires_owner_approval: false
  rollback_plan: >
    Восстановить tasks/active-task.md из git history.
    Удалить reports/m36-scope-control-maintenance-report.md если создан.
  acceptance_criteria:
    - tasks/active-task.md содержит все обязательные поля scope_control (allowed_paths, forbidden_paths, allow_new_files, allowed_new_files, forbidden_new_files, allow_modify_existing, allow_deletes, allow_renames, sensitive_paths)
    - Все отчёты M36 включены в allowed_new_files или allowed_paths
    - check-scope-compliance.py → PASS
    - agentos-validate.py all → PASS
    - Отчёт reports/m36-scope-control-maintenance-report.md создан с описанием изменений
  verification_plan:
    - python3 scripts/validate-task.py tasks/active-task.md
    - python3 scripts/check-scope-compliance.py tasks/active-task.md
    - python3 scripts/agentos-validate.py all
    - bash scripts/run-all.sh
---

# Task 36.6.0 — Scope Control Maintenance Hotfix

## Goal
Исправить накопленный системный долг в блоке scope_control файла tasks/active-task.md:
добавить все обязательные поля, которых не хватает для прохождения check-scope-compliance.py,
а также включить в scope все отчёты, созданные в рамках M36,
чтобы agentos-validate.py all возвращал PASS.

## Scope
Allowed to modify:
- tasks/active-task.md

Allowed to create:
- reports/m36-scope-control-maintenance-report.md

## Success Criteria
- tasks/active-task.md содержит все обязательные поля scope_control.
- Все отчёты M36 включены в allowed_new_files.
- agentos-validate.py all → PASS.

scope_control:
  allowed_paths:
    - tasks/active-task.md
    - reports/
    - schemas/task.schema.json
    - README.md
    - docs/quickstart.md
    - docs/installation.md
    - docs/first-project-onboarding.md
    - HANDOFF.md
    - memory-bank/
  forbidden_paths:
    - scripts/
    - .github/
    - src/
  allow_new_files: true
  allowed_new_files:
    - reports/m36-external-mvp-usability-intake.md
    - reports/m36-external-user-journey-inspection.md
    - reports/m36-readme-first-user-entry-hardening.md
    - reports/m36-installation-quickstart-inspection.md
    - reports/m36-installation-quickstart-hardening.md
    - reports/m36-first-project-onboarding-inspection.md
    - reports/m36-first-project-onboarding-scenario.md
    - reports/m36-troubleshooting-error-message-inspection.md
    - reports/m36-scope-control-maintenance-report.md
    - reports/m36-external-usability-smoke-test.md
    - reports/m36-external-mvp-usability-evidence-report.md
    - reports/m36-completion-review.md
    - scripts/audit-mvp-readiness.py
    - docs/installation.md
    - docs/first-project-onboarding.md
  forbidden_new_files:
  allow_modify_existing: true
  allow_deletes: false
  allow_renames: false
  sensitive_paths:
    - schemas/task.schema.json
