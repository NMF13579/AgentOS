# Problem Interview Template Guide

## 1. Purpose
Этот шаблон помогает записать структурированное interview evidence из сырого или неполного пользовательского запроса.

Interview evidence is not industrial spec.

## 2. Template Authority
- `docs/PROBLEM-INTERVIEW-ARCHITECTURE.md` задает концептуальные границы.
- `templates/problem-interview.md` применяет эти границы на практике.
- Шаблон не может переопределять архитектурный документ.

Reference: docs/PROBLEM-INTERVIEW-ARCHITECTURE.md

## 3. When to Use This Template
Используйте шаблон, когда:
- пользователь дает сырую идею
- пользователь дает неполное требование
- пользователь описывает проблему обычным языком
- пользователь не может дать готовую спецификацию
- AgentOS нужен структурированный interview evidence до M46

Шаблон не используется для создания task contracts, UX briefs, queue entries или execution approvals.

## 4. Field Definitions
- `interview_id`: уникальный идентификатор интервью.
- `created_at`: дата/время создания записи.
- `interview_status`: текущий статус интервью.
- `source_user_input`: исходный текст пользователя.
- `idea_summary`: короткое нейтральное резюме исходного текста.
- `problem_summary`: описание проблемы.
- `target_users`: целевые пользователи.
- `current_workaround`: текущий обходной путь.
- `desired_outcome`: желаемый результат.
- `success_criteria`: пользовательские признаки успеха.
- `constraints`: ограничения.
- `risks`: риски.
- `non_goals`: что не входит в цель.
- `unknowns`: список неизвестного.
- `assumptions`: список предположений.
- `answered_questions`: вопросы с ответами.
- `unanswered_questions`: вопросы без ответов.
- `follow_up_questions`: уточняющие вопросы.
- `non_approval_warning`: явное предупреждение, что это не approval.

idea_summary is a neutral short summary of the user's raw input.
It must not improve, complete, or reinterpret the user idea.
idea_summary must not add information not present in source_user_input.

Дополнительно:
- `idea_summary` must be shorter, neutral, and less specific than `source_user_input`.
- `idea_summary` must not add new features, constraints, risks, users, integrations, acceptance criteria, or implementation details.
- if `source_user_input` is unclear, `idea_summary` must preserve that uncertainty instead of improving the idea.

## 5. Status Model
Разрешены только статусы:
- `INTERVIEW_DRAFT`
- `INTERVIEW_NEEDS_CLARIFICATION`
- `INTERVIEW_READY_FOR_SPEC`
- `INTERVIEW_BLOCKED`

INTERVIEW_READY_FOR_SPEC does not mean approved for implementation.

Расшифровка:
- `INTERVIEW_DRAFT`: интервью начато, но структурно не завершено.
- `INTERVIEW_NEEDS_CLARIFICATION`: не хватает обязательных данных или есть неоднозначность/противоречие.
- `INTERVIEW_READY_FOR_SPEC`: обязательные поля заполнены и пригодны для M46.
- `INTERVIEW_BLOCKED`: внешний блокер не дает продолжить.

## 6. Missing Information Rules
Missing information must be recorded as MISSING_FROM_INTERVIEW, not inferred.
Missing information must become follow-up questions, not hallucinated requirements.

Пояснение:
- `MISSING_FROM_INTERVIEW` используется, когда пользователь не дал обязательные данные.
- Обязательные пустые поля нельзя заполнять догадками.
- Пустые обязательные поля должны порождать `follow_up_questions`.
- Молчание пользователя не означает разрешение «додумать» ответ.

## 7. NONE Rules
`NONE` допустимо только если пользователь явно сказал, что ограничений/рисков/non-goals нет.

Use NONE only when the user explicitly says there are no constraints.
Use NONE only when the user explicitly says there are no risks.
Use NONE only when the user explicitly says there are no non-goals.

Дополнительно:
- `NONE` — это явный ответ пользователя.
- `MISSING_FROM_INTERVIEW` — пользователь не ответил.
- `NONE` и `MISSING_FROM_INTERVIEW` не взаимозаменяемы.

## 8. Success Criteria Boundary
M45 records user-level success_criteria.
M45 does not create formal industrial acceptance criteria.
Formal acceptance criteria belong to M46.

Пояснение:
- user-level `success_criteria` — как пользователь поймет, что стало лучше.
- formal industrial acceptance criteria — артефакт M46.
- шаблон не должен превращать пользовательские сигналы в implementation-ready критерии.

## 9. Non-Approval Boundary
Interview evidence is not industrial spec.
Interview completeness is not execution readiness.
INTERVIEW_READY_FOR_SPEC does not mean approved for implementation.

Шаблон не дает права на:
- implementation
- task creation
- queue entry creation
- autopilot
- commit
- push
- merge
- release
- deployment

## 10. M45 to M46 Boundary
No interview evidence → no industrial spec.
No interview evidence -> no industrial spec.
M45 = ask correctly, record answers, detect gaps.
M46 = transform interview evidence into industrial specification.

Пояснение:
- M45 записывает и проверяет полноту interview evidence.
- M46 может использовать interview evidence как вход.
- M45 не должен генерировать M46 artifacts.
- Unicode arrow — canonical.
- ASCII-compatible form — только для copy/paste и plain-text compatibility.

## 11. Template Use Examples
1. Missing target users:
- `target_users: MISSING_FROM_INTERVIEW`
- `follow_up_questions: ["Кто будет основным пользователем решения?"]`

2. Explicit no constraints:
- пользователь явно сказал «ограничений нет»
- `constraints: NONE`

3. Vague success criteria:
- `success_criteria: MISSING_FROM_INTERVIEW`
- `unknowns: ["Не определен измеримый сигнал успеха"]`
- `follow_up_questions: ["По какому признаку вы поймете, что проблема решена?"]`

4. User gives solution but not problem:
- `problem_summary: MISSING_FROM_INTERVIEW`
- `idea_summary`: коротко повторяет исходную идею без расширения
- `follow_up_questions: ["Какую именно проблему эта идея должна решить?"]`

5. Unknowns without follow-up questions (неправильно):
- `unknowns` заполнены, но `follow_up_questions: []`
- правильно: добавить уточняющие вопросы к важным unknowns.

6. idea_summary non-invention:
- `source_user_input`: "Хочу, чтобы пользователи быстрее оформляли заказ, сейчас это долго и непонятно."
- `idea_summary`: "Пользователь хочет ускорить и упростить оформление заказа."
- корректно, потому что summary короче и не добавляет новых требований.

## 12. Final Boundary
Interview evidence is not industrial spec.
Interview completeness is not execution readiness.
No interview evidence → no industrial spec.
No interview evidence -> no industrial spec.
Missing information must be recorded as MISSING_FROM_INTERVIEW, not inferred.
Missing information must become follow-up questions, not hallucinated requirements.
INTERVIEW_READY_FOR_SPEC does not mean approved for implementation.
idea_summary must not add information not present in source_user_input.
M45 = ask correctly, record answers, detect gaps.
M46 = transform interview evidence into industrial specification.
