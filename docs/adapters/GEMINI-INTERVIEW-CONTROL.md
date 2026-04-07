# Gemini — контроль интервью (self-check стража)

## Когда применять

Когда интервью ведётся через Gemini с этим репозиторием как контекстом. Отдельного агента-стража нет — выполняйте **self-check** по [`INTERVIEW-GUARDIAN.md`](../../INTERVIEW-GUARDIAN.md) в каждом ответе.

## Читать перед интервью

1. [`START.md`](../../START.md)
2. [`GEMINI.md`](../../GEMINI.md) — если есть в репозитории.
3. [`docs/PROJECT-INTERVIEW.md`](../PROJECT-INTERVIEW.md)
4. [`INTERVIEWER.md`](../../INTERVIEWER.md)
5. [`INTERVIEW-GUARDIAN.md`](../../INTERVIEW-GUARDIAN.md)
6. [`AGENT-CONTRACT.md`](../../AGENT-CONTRACT.md)

## Обязательный формат каждого ответа

1. Один вопрос (или резюме + «Правильно понимаю?»).
2. Блок **СТРАЖ** — таблица из 7 строк по `INTERVIEW-GUARDIAN.md`.
3. `СТРАЖ: ✅` / `⚠️` / `❌`.
4. Дальше по маршруту — только если не **❌**; при **❌** — stop-block и исправление.

## Stop-block

Без следующего вопроса по `PROJECT-INTERVIEW.md`, пока критический **❌** не устранён повторной проверкой.

## Журнал

[`memory-bank/interview-session.md`](../../memory-bank/interview-session.md); `control-mode: gemini-self-check`.
