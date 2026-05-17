# Interview Gap Decision Card

## 1. Purpose
Human Decision Card explains interview gaps, not implementation readiness.

Карта используется, когда:
- не хватает обязательной информации интервью
- ответы неоднозначны
- ответы противоречат друг другу
- есть unknowns без достаточных follow-up
- может требоваться внешнее решение
- пользователю нужно простое объяснение, почему интервью нельзя безопасно продолжить

## 2. Relationship to Previous M45 Artifacts
- 45.1 defines the interview architecture
- 45.2 defines the basic interview template
- 45.3 defines safe follow-up questions
- 45.4 defines the answer record contract
- 45.5 detects missing information
- 45.6 proves representative completeness behavior
- 45.7 explains gaps to the human user

Decision cards translate checker findings into user-facing explanations.

## 3. Card Authority Boundary
Decision card explains.
Decision card does not approve.
Decision card does not invent answers.
Decision card does not reduce risk.
Decision card does not replace human gate.

Карта также не дает разрешение на:
- implementation
- task creation
- queue entry creation
- M46 by itself
- commit, push, merge, release, deployment
- превращение assumptions в facts
- превращение unknowns в requirements

## 4. When to Create a Card
Карту можно создавать, если результат checker:
- `COMPLETENESS_INCOMPLETE`
- `COMPLETENESS_NEEDS_CLARIFICATION`
- `COMPLETENESS_BLOCKED`
- `COMPLETENESS_CHECK_FAILED`

Карта обычно не нужна, если:
- `COMPLETENESS_COMPLETE`

COMPLETENESS_COMPLETE is not approval and does not require a decision card by itself.

## 5. Gap Types
Типы gap:
- `MISSING_REQUIRED_FIELD`
- `AMBIGUOUS_ANSWER`
- `CONTRADICTION`
- `UNKNOWN_WITHOUT_FOLLOWUP`
- `EXTERNAL_DECISION_REQUIRED`
- `INVALID_RECORD_SHAPE`
- `INVALID_NON_APPROVAL_WARNING`
- `BLOCKED_CONDITION`

Gap types are explanation categories, not interview_status values.

INVALID_NON_APPROVAL_WARNING is an internal record integrity gap.
It should be shown to maintainers or agents, not directly to non-technical users.
If surfaced to a user, it must be translated as: "The interview record is missing a required safety warning, so it cannot be trusted yet."

AMBIGUOUS_ANSWER means the answer is unclear.
CONTRADICTION means two or more answers conflict.

## 6. Required Card Fields
- `card_id`
- `created_at`
- `source_interview_id`
- `source_checker_result`
- `source_interview_status`
- `gap_type`
- `missing_or_unclear_information`
- `why_it_matters`
- `risk_if_skipped`
- `recommended_follow_up_question`
- `can_continue_with_assumption`
- `assumption_warning`
- `what_if_user_does_not_know`
- `safe_next_action`
- `non_approval_warning`

## 7. Source Status Clarification
source_interview_status is the status stored in the interview record.
source_interview_status is not the decision card result.
source_interview_status is not proof that the interview is actually complete.
Checker results may override misleading interview_status when information is missing.

source_interview_status may say INTERVIEW_READY_FOR_SPEC while source_checker_result says COMPLETENESS_NEEDS_CLARIFICATION.
In that case, the checker result explains the gap and the card must not treat READY_FOR_SPEC as approval or true completeness.

## 8. Explanation Rules
Правила объяснения:
- писать простым пользовательским языком
- избегать технического жаргона, если его не использовал сам пользователь
- один основной gap на одну карту
- не обвинять пользователя за отсутствие ответа
- не намекать, что ответ "очевиден"
- не предлагать предпочтительную реализацию
- не придумывать требования
- не скрывать риск
- не занижать риск
- не превращать missing information в `NONE`
- не превращать missing information в assumptions без явного подтверждения пользователя

Missing information must become follow-up questions, not hallucinated requirements.

## 9. Assumption Handling
- assumptions допустимы только при явной пометке
- assumptions должны оставаться видимыми
- assumptions не заменяют пользовательские ответы
- assumptions могут переносить неопределенность дальше только если это разрешат правила следующих этапов
- assumptions не дают approval
- assumptions не снимают риск

Assumptions must be marked as assumptions, not facts.

## 10. Unknown Answer Handling
Если пользователь не знает ответ, безопасные варианты:
- оставить пункт как unknown
- спросить другого стейкхолдера
- отметить явное assumption
- блокировать до решения owner/legal/security/business
- переносить unknown дальше только если следующие правила это разрешают

User uncertainty must remain visible.

## 11. Blocked Conditions
Если требуется legal/security/owner/business решение, карта должна объяснить:
- какое решение нужно
- кто должен решить
- почему нельзя безопасно продолжить интервью
- какой следующий безопасный шаг

Decision card may explain a blocked condition, but it must not unblock it.

## 12. User-Facing Examples
### Example: Missing target users
- Gap: target users are missing.
- Why it matters: without target users, it is unclear who the solution is for.
- Risk if skipped: wrong scope and wrong assumptions.
- Recommended follow-up question: "Кто будет основным пользователем этого решения?"
- Safe next action: ask follow-up question.

### Example: Missing success criteria
- Gap: success criteria are missing.
- Why it matters: no clear way to understand if problem is solved.
- Risk if skipped: solution may be delivered but still fail user expectations.
- Recommended follow-up question: "По какому признаку вы поймете, что проблема решена?"
- Safe next action: keep gap visible and ask follow-up.

### Example: Ambiguous answer
- Gap: answer is too vague to use safely.
- Why it matters: vague answers create conflicting interpretations.
- Risk if skipped: wrong requirements may be inferred.
- Recommended follow-up question: "Что именно вы имеете в виду под ‘быстрее’ в этом контексте?"
- Safe next action: request clarification.

### Example: Unknowns without follow-up
- Gap: unknown exists but no follow-up question exists.
- Why it matters: unknown cannot be resolved later without a clear question.
- Risk if skipped: unresolved uncertainty is silently carried as hidden risk.
- Recommended follow-up question: "Кто отвечает за интеграцию с этой системой?"
- Safe next action: add follow-up question before continuing.

### Example: Contradiction requiring clarification
- Gap: two answers conflict.
- Why it matters: the direction is ambiguous.
- Risk if skipped: team may implement opposite expectations.
- Recommended follow-up question: "Какой из двух приоритетов важнее в этой версии?"
- Safe next action: resolve contradiction first.

### Example: Legal/security/owner decision required
- Gap: external authority decision is required.
- Why it matters: interview cannot safely proceed without that decision.
- Risk if skipped: policy or compliance breach.
- Recommended follow-up question: "Кто уполномочен принять это решение и когда?"
- Safe next action: block until decision.

### Example: Invalid non-approval warning (internal integrity)
Gap: The interview record is missing a required safety warning.
Why it matters: The system cannot safely treat this record as valid interview evidence.
Risk if skipped: The user may believe the interview authorizes implementation when it does not.
Recommended follow-up question: "Should we regenerate or repair the interview record before continuing?"
Safe next action: Fix the interview record shape before continuing.

## 13. Non-Approval Boundary
Decision card explains.
Decision card does not approve.
Decision card does not invent answers.
Decision card does not reduce risk.
Decision card does not replace human gate.
Interview completeness is not execution readiness.
INTERVIEW_READY_FOR_SPEC does not mean approved for implementation.

## 14. Final Boundary
Interview evidence is not industrial spec.
Interview completeness is not execution readiness.
Schema validity is not interview completeness.
Completeness check is not approval.
Smoke PASS is not approval.
Decision card explains.
Decision card does not approve.
Decision card does not invent answers.
Decision card does not reduce risk.
Decision card does not replace human gate.
No interview evidence → no industrial spec.
No interview evidence -> no industrial spec.
Missing information must be recorded as MISSING_FROM_INTERVIEW, not inferred.
Missing information must become follow-up questions, not hallucinated requirements.
INTERVIEW_READY_FOR_SPEC does not mean approved for implementation.
M45 = ask correctly, record answers, detect gaps.
M46 = transform interview evidence into industrial specification.
