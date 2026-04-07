# Cursor — контроль интервью (self-check стража)

## Когда применять

Когда в Cursor ведёте интервью по [`docs/PROJECT-INTERVIEW.md`](../PROJECT-INTERVIEW.md) (новый проект, сбор контекста). Отдельного агента `@guardian` в Cursor нет — проверку делает **тот же агент** в каждом ответе.

## Читать перед интервью

1. [`START.md`](../../START.md) — этап 0, уровень проекта.
2. [`docs/PROJECT-INTERVIEW.md`](../PROJECT-INTERVIEW.md) — маршрут вопросов.
3. [`INTERVIEWER.md`](../../INTERVIEWER.md) — протокол и формат сообщения.
4. [`INTERVIEW-GUARDIAN.md`](../../INTERVIEW-GUARDIAN.md) — чеклист из 7 пунктов.
5. [`AGENT-CONTRACT.md`](../../AGENT-CONTRACT.md) — принципы и модули.

Соблюдайте также `.cursor/rules/10-communication.mdc` (один вопрос, entry flow).

## Обязательный формат каждого ответа

1. Вопрос владельцу (или резюме + «Правильно понимаю?» — один шаг).
2. Блок **СТРАЖ** — таблица из [`INTERVIEW-GUARDIAN.md`](../../INTERVIEW-GUARDIAN.md) (все 7 строк с колонками ✅/⚠️/❌ и кратким доказательством).
3. Строка вердикта: `СТРАЖ: ✅` / `СТРАЖ: ⚠️` / `СТРАЖ: ❌`.
4. Если **не ❌** — можно следующий шаг или уточнение. Если **❌** — только исправленный один вопрос и снова полный блок СТРАЖ (**stop-block**: без следующего вопроса по маршруту).

## Stop-block

При **❌** по критическим пунктам (1, 2, 3, 6, 7) в [`INTERVIEW-GUARDIAN.md`](../../INTERVIEW-GUARDIAN.md): не задавать следующий вопрос из `PROJECT-INTERVIEW.md` до исправления и нового прохода чеклиста.

## Журнал

После каждого ответа владельца (когда ведёте журнал) — запись в [`memory-bank/interview-session.md`](../../memory-bank/interview-session.md); в поле вердикта укажите `control-mode: cursor-self-check`.
