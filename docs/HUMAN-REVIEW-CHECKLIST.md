# Human Review Checklist (31.9)

## Что это
Лёгкий чеклист для ручной проверки, когда статус требует review / Human Gate / owner review / blocked / unknown.

## Что это НЕ
- не approval;
- не запись approval;
- не замена Human Gate;
- не замена Owner Review;
- не разрешение на выполнение;
- не разрешение на commit/push/merge/READY.

## Когда использовать
- severity: NEEDS_REVIEW / BLOCKED / HUMAN_GATE / UNKNOWN
- authority: HUMAN_GATE_REQUIRED / OWNER_REVIEW_REQUIRED
- missing approval / protected action / stale or damaged status source

## Обязательные разделы
- Review context
- Current status
- Why review is needed
- What to inspect
- Safe next step
- Blocked actions
- Human Gate / Owner Review requirement
- Confirmation of understanding
- Non-approval disclaimer

## Запрещённая формулировка
Нельзя писать активные утверждения вроде:
- I approve this action
- I authorize execution
- Mark READY
- Можно выполнять

## Язык
- коротко и ясно;
- одна мысль на строку;
- без успокаивающих опасных фраз.

## Source/Freshness
Если источник stale/unknown/missing/damaged:
- показывать это явно;
- не рекомендовать обычное продолжение.

## Boundary
Этот чеклист информирует.
Этот чеклист не даёт право на действие.
