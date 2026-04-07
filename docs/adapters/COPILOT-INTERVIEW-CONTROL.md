# GitHub Copilot — контроль интервью (self-check стража)

## Когда применять

Когда в среде с Copilot (VS Code, GitHub и т.д.) ведёте интервью по [`docs/PROJECT-INTERVIEW.md`](../PROJECT-INTERVIEW.md). Отдельного сабагента стража нет — **self-check** в каждом ответе агента.

## Читать перед интервью

1. [`START.md`](../../START.md)
2. [`docs/PROJECT-INTERVIEW.md`](../PROJECT-INTERVIEW.md)
3. [`INTERVIEWER.md`](../../INTERVIEWER.md)
4. [`INTERVIEW-GUARDIAN.md`](../../INTERVIEW-GUARDIAN.md)
5. [`AGENT-CONTRACT.md`](../../AGENT-CONTRACT.md)

Учитывайте [`.github/copilot-instructions.md`](../../.github/copilot-instructions.md).

## Обязательный формат каждого ответа

1. Вопрос владельцу (один смысловой шаг).
2. Блок **СТРАЖ** — полная таблица из 7 проверок [`INTERVIEW-GUARDIAN.md`](../../INTERVIEW-GUARDIAN.md).
3. `СТРАЖ: ✅` / `⚠️` / `❌`.
4. Следующий шаг маршрута — **только** если нет **❌**. Иначе — исправление + повтор чеклиста (**stop-block**).

## Stop-block

Как в [`INTERVIEW-GUARDIAN.md`](../../INTERVIEW-GUARDIAN.md): при **❌** не продвигаться по этапам интервью до исправления.

## Журнал

[`memory-bank/interview-session.md`](../../memory-bank/interview-session.md); указывайте `control-mode: copilot-self-check`.
