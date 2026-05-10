---
task_id: task-m37-1-0-task-id-sync-hardening
state: queue
created_at: 2026-05-10T06:41:00Z
created_by: human-approved-command
milestone: M37

task:
  id: task-m37-1-0-task-id-sync-hardening
  goal: >
    Навсегда устранить класс ошибок "verification.task_id does not match task.id"
    через три уровня защиты: (1) обновление шаблонов с {{TASK_ID}} placeholder,
    (2) скрипт синхронизации scripts/sync-task-ids.py,
    (3) новый шаг в CI workflow который блокирует merge при расхождении ID.
  expected_result: >
    Невозможно создать PR где task_id != task.id != verification.task_id.
    CI автоматически блокирует merge при любом расхождении.
    Агент получает единственное место для заполнения ID — {{TASK_ID}} в шаблоне.
  in_scope:
    - tasks/templates/task-contract.md
    - reports/templates/
    - scripts/sync-task-ids.py
    - .github/workflows/agentos-validate.yml
  out_of_scope:
    - src/
    - docs/
    - reports/
    - tasks/active-task.md
  files_or_areas:
    - tasks/templates/task-contract.md
    - reports/templates/verification.md
    - scripts/sync-task-ids.py
    - .github/workflows/agentos-validate.yml
  risk_level: MEDIUM
  risk_reason: >
    Затрагивает .github/workflows/ (CI pipeline) и scripts/ (валидация).
    Ошибка в workflow может сломать все последующие PR.
    Требует тщательного тестирования перед коммитом.
  requires_owner_approval: false
  rollback_plan: >
    Восстановить .github/workflows/agentos-validate.yml из git history.
    Удалить scripts/sync-task-ids.py.
    Восстановить шаблоны из git history.
  acceptance_criteria:
    - tasks/templates/task-contract.md содержит {{TASK_ID}} вместо "task-template" в поле task.id
    - reports/templates/verification.md содержит {{TASK_ID}} в поле verification.task_id
    - scripts/sync-task-ids.py существует и выводит PASS при совпадении ID
    - scripts/sync-task-ids.py выводит FAIL при расхождении ID
    - .github/workflows/agentos-validate.yml содержит шаг проверки ID consistency ДО check-pr-quality.py
    - CI падает с понятным сообщением если IDs расходятся
    - check-pr-quality.py продолжает работать как раньше
    - python3 scripts/agentos-validate.py all -> PASS после изменений
  verification_plan:
    - python3 scripts/sync-task-ids.py --check tasks/active-task.md reports/verification.md
    - python3 scripts/validate-task.py tasks/active-task.md
    - python3 scripts/agentos-validate.py all
    - bash scripts/run-all.sh

scope_control:
  allowed_paths:
    - tasks/templates/
    - reports/templates/
    - scripts/
    - .github/workflows/agentos-validate.yml
  forbidden_paths:
    - src/
    - docs/
    - reports/m
    - tasks/active-task.md
  allow_new_files: true
  allowed_new_files:
    - scripts/sync-task-ids.py
    - reports/templates/verification.md
    - reports/m37-task-id-sync-hardening-report.md
  forbidden_new_files: []
  allow_modify_existing: true
  allow_deletes: false
  allow_renames: false
  sensitive_paths:
    - .github/workflows/agentos-validate.yml
    - scripts/sync-task-ids.py

context:
  problem: >
    Трижды подряд CI падал с ошибкой "verification.task_id does not match task.id"
    (PR #112, #114, #115). Причина: task_id прописывается вручную в трёх местах
    (frontmatter task_id, task.id, verification.task_id) и агент рассинхронизирует их.
  root_cause: Нет единого источника истины для task_id и нет автоматической проверки на входе.
  solution_levels:
    level_1: "Шаблоны с {{TASK_ID}} — одно место для замены"
    level_2: "scripts/sync-task-ids.py — синхронизация по требованию"
    level_3: "CI шаг — блокировка merge при расхождении"

dependencies:
  required_before_start: []
  blocks:
    - M37 все последующие задачи (чистый CI — базовое условие)

recommended_model: gemini-3-flash-preview

notes: >
  Это инфраструктурная задача M37. Должна быть первой в milestone.
  После выполнения — класс ошибок task_id mismatch исчезает навсегда.
  Изменение .github/workflows/ требует особой аккуратности — тестировать
  на отдельном коммите перед финальным push.
---
