# Куда класть файлы и как они связаны

## Структура размещения

```text
твой-проект/                        ← корень репозитория
│
├── START.md                        ← общий вход: новый проект / есть код, уровень 0–2
├── INTERVIEWER.md                  ← протокол интервьюера (OpenCode + эталон для других IDE)
├── INTERVIEW-GUARDIAN.md           ← единый чеклист стража (OpenCode subagent или self-check)
│
├── AGENT-CONTRACT.md               ← уже есть ✓
├── SCOPE-CREEP-GUARD.md            ← уже есть ✓
├── HANDOFF.md                      ← уже есть ✓
│
├── opencode.json                   ← секция "agent": interviewer + guardian
│                                     (в этом репозитории — готовый файл в корне)
│
├── docs/
│   ├── PROJECT-INTERVIEW.md        ← маршрут вопросов интервью
│   └── adapters/                   ← self-check стража для Cursor / Copilot / Claude / Gemini
│
└── memory-bank/
    ├── interview-session.md        ← канонический сырой журнал шагов интервью
    └── project-context-draft.md    ← только редирект на interview-session (совместимость)
```

---

## Связи между файлами

```text
opencode.json
├── agent.interviewer.prompt
│   ├── читает → INTERVIEWER.md             (роль + протокол)
│   ├── читает → START.md                   (этап 0, уровень, контекст проекта)
│   ├── читает → docs/PROJECT-INTERVIEW.md  (маршрут вопросов)
│   ├── читает → AGENT-CONTRACT.md          (правила поведения)
│   └── читает → HANDOFF.md                 (контекст сессии)
│
└── agent.guardian.prompt
    ├── читает → INTERVIEW-GUARDIAN.md      (чеклист + вердикты)
    ├── читает → docs/PROJECT-INTERVIEW.md  (маршрут — эталон проверки)
    ├── читает → AGENT-CONTRACT.md          (правила — эталон проверки)
    └── читает → SCOPE-CREEP-GUARD.md       (защита скоупа)

Во время сессии:
INTERVIEWER → вызывает @guardian после каждого шага (если OpenCode не делает это сам — интервьюер обязан вызвать вручную)
GUARDIAN    → возвращает вердикт ✅/⚠️/❌
INTERVIEWER → пишет ответы в memory-bank/interview-session.md
INTERVIEWER → обновляет HANDOFF.md по завершении

**Потом (после подтверждённого резюме):** содержание журнала переносится в продуктовые файлы discovery и далее по `START.md` / `AGENT-CONTRACT.md` — см. `docs/PROJECT-INTERVIEW.md` и [`docs/DOCS-MAP.md`](docs/DOCS-MAP.md).
```

---

## Что делать с opencode.json

Если у вас **уже есть** `opencode.json` с провайдерами — **добавь** в него секцию `agent` из этого репозитория (скопируй блок `agent` из корневого [`opencode.json`](opencode.json) здесь), не удаляя свои ключи `provider` и прочие.

Если отдельного файла агентов не было — используй готовый корневой `opencode.json` шаблона как основу и дополни своими провайдерами по [документации OpenCode](https://opencode.ai).

---

## Как запустить

1. Положи файлы согласно структуре выше.
2. Открой OpenCode в папке проекта.
3. Напиши: «Собрать интервью» или «@interviewer начни интервью».
4. Интервьюер ведёт шаги; страж — по вызову `@guardian` (или автоматически, если ваша версия OpenCode это поддерживает).

---

## Модель для guardian

`guardian` использует `claude-opus-4-5` (более точная проверка).
Если хочешь сэкономить токены — замени на `claude-sonnet-4-5`,
но тогда строгость проверки будет ниже.

Через AITUNNEL обе модели доступны по `baseURL https://api.aitunnel.ru/v1/`.

---

## Не OpenCode (Cursor, Copilot, Claude, Gemini)

Тот же контроль, что у стража, выполняется **внутри ответа интервьюера** (self-check):

- индекс: [`docs/adapters/README.md`](docs/adapters/README.md);
- после **каждого** шага — полная таблица из [`INTERVIEW-GUARDIAN.md`](INTERVIEW-GUARDIAN.md) и строка `СТРАЖ: ✅/⚠️/❌`;
- при критическом **❌** — **stop-block**: следующий вопрос по маршруту не задаётся до исправления;
- журнал: [`memory-bank/interview-session.md`](memory-bank/interview-session.md) с указанием `control-mode` (например `cursor-self-check`).

Общий вход и правило описаны в [`START.md`](START.md) (раздел «Кросс-IDE контроль интервью»).
