# AgentOS — Руководство на русском

> AgentOS — это **не автономный агент**. Это набор guardrails (ограничительных правил) для AI-assisted разработки с обязательным участием человека на каждом шаге.

---

## Что такое AgentOS

AgentOS — это фреймворк на основе Markdown-файлов, который добавляет структуру, валидацию и границы безопасности в рабочий процесс с AI-агентами (Cursor, Windsurf, Claude, GPT и др.).

**Ключевые принципы:**
- Вся конфигурация — человекочитаемые Markdown-файлы
- Ни одна задача не выполняется без явного одобрения человека
- `tasks/active-task.md` — единственный исполняемый контракт задачи
- PASS в проверке ≠ готовность к production. NOT_RUN ≠ PASS

---

## Требования

- Git-репозиторий
- Bash
- Python 3
- pip

---

## Установка

### Минимальный шаблон

Подходит для старта: базовые схемы, шаблоны задач и отчётов, две проверки.

```bash
cd /путь/к/вашему/проекту
bash /путь/к/AgentOS/install.sh --minimal --dry-run  # сначала посмотреть что будет
bash /путь/к/AgentOS/install.sh --minimal            # установить
```

### Полный шаблон

Полный набор guardrails, вспомогательных файлов и проверок.

```bash
cd /путь/к/вашему/проекту
bash /путь/к/AgentOS/install.sh --full --dry-run  # сначала посмотреть что будет
bash /путь/к/AgentOS/install.sh --full            # установить
```

### Что входит в шаблоны

| | Minimal | Full |
|---|---|---|
| Базовые схемы и шаблоны задач | ✅ | ✅ |
| Шаблоны отчётов и верификации | ✅ | ✅ |
| run-all.sh | ✅ | ✅ |
| Guardrails документы | ❌ | ✅ |
| Документация по ограничениям | ❌ | ✅ |
| Примеры использования | ❌ | ✅ |

### Что НЕ входит

- Backend, RAG, векторная БД, оркестрация агентов
- Docker-образ, pip-пакет, npm-пакет

---

## Проверка установки

После установки запустите проверки:

```bash
# Полная проверка всего
python3 scripts/agentos-validate.py all

# С выводом в JSON
python3 scripts/agentos-validate.py all --json
```

Отдельные проверки для отладки:

```bash
python3 scripts/agentos-validate.py template   # структура шаблона
python3 scripts/agentos-validate.py negative   # негативные фикстуры
python3 scripts/agentos-validate.py guard      # проверки безопасности
python3 scripts/agentos-validate.py audit      # общий аудит
python3 scripts/agentos-validate.py queue      # очередь задач
python3 scripts/agentos-validate.py runner     # раннер
```

Проверка установщика:

```bash
bash scripts/test-install.sh
bash scripts/test-example-project.sh
```

Оба должны вернуть `PASS`.

---

## Как работать с задачами

АгентOS управляет задачами через несколько этапов:

### 1. Инициализация проекта
```
/init → создаёт project/PROJECT.md
```

### 2. Создание задачи
```
/spec → создаёт tasks/{task-id}/TASK.md
```
Файл TASK.md — **описание**, не исполняемый контракт.

### 3. Валидация задачи
```bash
python3 scripts/validate-task-brief.py tasks/{task-id}/TASK.md
```

### 4. Ревью и трейс
- Создаётся `REVIEW.md` — результат ревью
- Создаётся `TRACE.md` — трейс выполнения

### 5. Генерация контракта
```bash
python3 scripts/generate-task-contract.py tasks/{task-id}/TASK.md
```
Создаёт черновик в `tasks/drafts/{task-id}-contract-draft.md`. Черновик — **не активный контракт**.

### 6. Одобрение человеком
Человек проверяет черновик и явно его одобряет или запрашивает правки.

### 7. Активация задачи
Одобренный черновик переводится в `tasks/active-task.md`.
**Только `tasks/active-task.md` является исполняемым контрактом.**

---

## Слои валидации

Запускайте в следующем порядке:

```bash
# 1. Целостность структуры шаблона
python3 scripts/check-template-integrity.py --strict

# 2. Тесты самого проверяльщика
python3 scripts/test-template-integrity.py

# 3. Негативные фикстуры — убеждаемся что невалидные данные отклоняются
python3 scripts/test-negative-fixtures.py

# 4. Проверки guard-сбоев
python3 scripts/test-guard-failures.py

# 5. Общий аудит релизной готовности
python3 scripts/audit-agentos.py
```

---

## Границы безопасности

| Граница | Что защищает |
|---|---|
| **Граница выполнения задачи** | Только `tasks/active-task.md` исполняем; TASK.md — нет |
| **Граница контракта** | Черновики требуют ревью человека перед активацией |
| **Граница очереди** | Элементы очереди не перемещаются автономно |
| **Чекпойнт одобрения** | Человек должен одобрить замену активной задачи |
| **Граница раннера** | Раннер работает в dry-run режиме; автономное выполнение не реализовано |

---

## Важные предупреждения

- `PASS` в проверке **не означает** что AgentOS готов к production
- `NOT_RUN` **не равно** `PASS` — непройденная проверка не даёт никаких гарантий
- AgentOS **не является** backend, RAG-системой или векторной БД
- AgentOS **не автономен** — человеческий контроль обязателен для всех решений о выполнении

---

## Дальнейшее изучение

- [`docs/GETTING-STARTED.md`](GETTING-STARTED.md) — подробное введение (англ.)
- [`docs/VALIDATION.md`](VALIDATION.md) — полный справочник по валидации (англ.)
- [`docs/SAFETY-BOUNDARIES.md`](SAFETY-BOUNDARIES.md) — детальные границы безопасности (англ.)
- `llms.txt` — порядок загрузки для AI-агентов
- `workflow/MAIN.md` — поток выполнения
