# State Transitions — Политика переходов состояний

Переход = событие + guard + side effect. Без выполненного guard переход не выполняется.  
Агент обновляет `LAYER-3/STATE.md` при каждом допустимом переходе.

## Где искать детали

- Таблицы переходов по доменам (Project / Session / Task) и запрещённые переходы — в **`ARCHITECTURE.md`**, раздел **State Control Plane** (если в вашей копии репозитория раздел включён).
- Жизненный цикл сессии (старт, конец задачи, напоминания, аудит, фичи) — **`LAYER-1/session-lifecycle.md`**.
- План, подтверждение, LOCKED, расширение скоупа — **`LAYER-1/plan-and-scope-gate.md`** и **`LAYER-1/scope-guard.md`**.
- Маршрутизация по этапам `stages/*` — **`LAYER-1/stage-routing.md`**.
- Приоритет источников при конфликте — **`LAYER-1/instruction-priority.md`** и **`shared/priority-order.md`**.
