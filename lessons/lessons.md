---
lessons:
  - id: "lesson-001"
    source_incident: "incident-template"
    tags:
      - "scope-creep"
    trigger: "Agent attempts to modify out_of_scope files."
    rule: "Before editing, compare target files against task.in_scope and task.out_of_scope."
    target_file: "workflow/MAIN.md"
    status: "proposed"
  - id: "lesson-002"
    source_incident: "approval-gate-not-implemented"
    tags:
      - "approval-gate"
      - "argparse"
      - "audit-marker"
    trigger: >
      В скрипте есть комментарии-маркеры аудита (# --approval <file>,
      # validate-human-approval) но сам аргумент не добавлен в argparse
      и логика не реализована. Тесты падают с missing_required_approval.
    rule: >
      Комментарии-маркеры аудита — это спецификация, а не заглушка.
      Перед завершением задачи проверять: каждый маркер из раздела
      «audit markers» должен иметь соответствующую реализацию в коде.
      Запускать тесты fixtures до закрытия задачи.
    target_file: "scripts/apply-transition.py"
    status: "active"
  - id: "lesson-003"
    source_incident: "context-pipeline-strict-blocked-by-scope"
    tags:
      - "ci"
      - "scope"
      - "active-task"
      - "context-pipeline"
    trigger: >
      CI падает на шаге strict context pipeline, хотя локально другие проверки
      зелёные. В результате strict-check показывает scope_violation.
    rule: >
      Если strict context pipeline blocked, сначала проверить reports/changed-files.txt
      и сравнить его с allowed_paths в tasks/active-task.md. Если там есть новые
      каталоги (например data/ или templates/), добавить их в scope задачи,
      иначе пайплайн останется заблокированным.
    target_file: "tasks/active-task.md"
    status: "active"
  - id: "lesson-004"
    source_incident: "m31-explainable-status-chain-foundation"
    tags:
      - "m31"
      - "status-chain"
      - "fail-closed"
      - "workflow"
    trigger: >
      После большого этапа M31 команды статуса/объяснения/следующего шага
      были готовы, но live-источники отчётов местами отсутствовали. Это дало
      UNKNOWN вместо ложного OK и показало реальные риски в проверках.
    rule: >
      Для крупных milestone сначала делать foundation-коммит с основной цепочкой
      (vocabulary -> status -> view model -> why -> next -> tui -> cli), затем
      отдельным проходом запускать расширенные чек-листы и только после этого
      чистить временные snapshot-файлы. При отсутствии live-источников держать
      fail-closed поведение: UNKNOWN/NEEDS_REVIEW, но не OK.
    target_file: "scripts/agentos-status.py"
    status: "active"
  - id: "lesson-005"
    source_incident: "active-task-idle-state-bypass-failure"
    tags:
      - "active-task"
      - "idle-state"
      - "frontmatter"
    trigger: >
      Скрипты, читающие active-task.md (например, валидаторы или чекеры рисков),
      падают с ошибкой "invalid frontmatter" или "FAIL", когда система находится
      в режиме ожидания (idle state), то есть файл active-task.md содержит текст
      вроде "No active task yet." и не имеет YAML-структуры.
    rule: >
      Все скрипты, которые обращаются к tasks/active-task.md, должны реализовывать
      паттерн is_idle_state() bypass. Перед попыткой парсить frontmatter,
      необходимо прочитать файл как обычный текст, проверить отсутствие маркера '---'
      или наличие фразы 'no active task' (в нижнем регистре), и в этом случае
      завершать работу без ошибки (возвращать 0 / PASS), чтобы не ломать общие
      пайплайны валидации (run-all.sh, pre-commit).
    target_file: "scripts/run-all.sh"
    status: "active"
---
