# Explanation Vocabulary (M31)

## Purpose
Этот файл описывает словарь статусов для M31.
Словарь — единый источник смысла для отображения статуса.

Главное правило:
- если рендерер (Rich/Textual/Web) показывает смысл иначе, чем словарь, исправляют рендерер.
- словарь важнее рендерера.

## Source Of Truth
- `data/explanations/status-vocabulary.yml` — единый источник объяснений.
- Рендереры и будущие команды должны брать смысл только из словаря и View Model.

## Status Code vs Severity vs Authority
- `status_code` — машинный код статуса.
- `severity` — уровень внимания/риска.
- `authority` — кто принимает решение дальше.

Цвет и иконка — только визуальная подсказка.
Цвет не является правом на действие.

## Canonical Combinations
| Status | Severity | Authority |
|---|---|---|
| AGENTOS_STATUS_OK | OK | NONE |
| AGENTOS_STATUS_WARN | WARNING | HUMAN_REVIEW_OPTIONAL |
| AGENTOS_STATUS_NEEDS_REVIEW | NEEDS_REVIEW | HUMAN_REVIEW_OPTIONAL |
| AGENTOS_STATUS_BLOCKED | BLOCKED | SYSTEM_BLOCKED |
| AGENTOS_STATUS_UNKNOWN | UNKNOWN | SYSTEM_BLOCKED |
| STATUS_STALE | WARNING | HUMAN_REVIEW_OPTIONAL |
| STATUS_SOURCE_MISSING | UNKNOWN | SYSTEM_BLOCKED |
| STATUS_SOURCE_DAMAGED | BLOCKED | SYSTEM_BLOCKED |
| HUMAN_GATE_REQUIRED | HUMAN_GATE | HUMAN_GATE_REQUIRED |
| OWNER_REVIEW_REQUIRED | HUMAN_GATE | OWNER_REVIEW_REQUIRED |
| PROTECTED_ACTION_BLOCKED | BLOCKED | SYSTEM_BLOCKED |

## Icon/ASCII Rules
Обязательно одновременно:
- icon
- ascii_label
- severity
- текстовое объяснение

Иконки/лейблы по умолчанию:
- OK: ✅ / [OK]
- INFO: ℹ️ / [INFO]
- WARNING: ⚠️ / [WARNING]
- NEEDS_REVIEW: 🔎 / [REVIEW]
- BLOCKED: ⛔ / [BLOCKED]
- HUMAN_GATE: 👤 / [HUMAN]
- UNKNOWN: ❓ / [UNKNOWN]

No icon-only status.
No color-only risk indication.

## View Model Compatibility
Словарь хранит данные, достаточные для будущей View Model:
- title/summary/why
- source
- freshness
- next_safe_steps
- blocked_actions
- renderer_hints

Правило:
- `next_safe_step` в UI = первый элемент `next_safe_steps`.
- рендерер не придумывает новые шаги.

## UNKNOWN Rule
UNKNOWN — это не OK.
Для UNKNOWN обязательно:
- явно сказать, что статус неизвестен;
- сказать, что продолжать нельзя или нужно проверить;
- показать шаг восстановления источника статуса.

## Language Rules
Простой режим (`simple_ru`) должен быть коротким и понятным:
- что случилось;
- почему важно;
- что проверить;
- следующий безопасный шаг.

Для NEEDS_REVIEW/BLOCKED обязательно:
- blocked_actions, либо явная фраза, что продолжать нельзя.

## Safety Rules
Словарь не даёт право на действие.
`next_safe_step` — подсказка, не выполнение.

Запрещены шаги с dangerous verbs:
- fix, go, approve, ready, commit, push, merge, promote, mark ready, bypass.

## Renderer Separation
- Vocabulary задаёт смысл.
- Aggregator определяет машинный статус.
- View Model готовит структуру для экрана.
- Renderer только рисует.

Rich replaceable.
Vocabulary and status JSON are not.

## Non-Approval Boundary
- checklist is not approval
- explanation is not approval
- next step is not execution
- Human Gate remains approval authority
