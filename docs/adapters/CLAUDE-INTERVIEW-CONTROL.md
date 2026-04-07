# Claude (Code / чат с репозиторием) — контроль интервью (self-check стража)

## Когда применять

Когда интервью ведётся через Claude с доступом к этому репозиторию и без OpenCode subagent «guardian». Проверка — **self-check** по тем же правилам, что в [`INTERVIEW-GUARDIAN.md`](../../INTERVIEW-GUARDIAN.md).

## Читать перед интервью

1. [`START.md`](../../START.md)
2. [`CLAUDE.md`](../../CLAUDE.md) — общий контракт сессии.
3. [`docs/PROJECT-INTERVIEW.md`](../PROJECT-INTERVIEW.md)
4. [`INTERVIEWER.md`](../../INTERVIEWER.md)
5. [`INTERVIEW-GUARDIAN.md`](../../INTERVIEW-GUARDIAN.md)
6. [`AGENT-CONTRACT.md`](../../AGENT-CONTRACT.md)

## Обязательный формат каждого ответа

1. Вопрос владельцу (один шаг по маршруту).
2. Блок **СТРАЖ**: таблица 7 пунктов из `INTERVIEW-GUARDIAN.md` с отметками и доказательствами.
3. Вердикт: `СТРАЖ: ✅` / `⚠️` / `❌`.
4. При **❌** — **stop-block**: только исправленный вопрос и снова чеклист; без следующего пункта `PROJECT-INTERVIEW.md`.

## Stop-block

См. раздел «Правило stop-block» в [`INTERVIEW-GUARDIAN.md`](../../INTERVIEW-GUARDIAN.md).

## Журнал

[`memory-bank/interview-session.md`](../../memory-bank/interview-session.md); `control-mode: claude-self-check`.
