# Problem Interview Architecture

## 1. Purpose
Problem Interview Layer переводит сырую идею пользователя в структурированное interview evidence (структурированная запись ответов интервью).

M45 не делает следующее:
- create industrial specifications
- create UX designs or UX briefs
- create task contracts
- create queue entries
- authorize execution or implementation
- approve anything
- start autopilot
- generate M46 artifacts

Interview evidence is not industrial spec.
Interview completeness is not execution readiness.
No interview evidence → no industrial spec.
No interview evidence -> no industrial spec.

The Unicode arrow form is the preferred canonical form.
The ASCII form exists only for copy/paste and plain-text compatibility.
Both forms have the same meaning.

## 2. Problem Interview Definition
Problem interview — это guided requirements elicitation process (управляемый процесс сбора требований), который помогает не-техническим пользователям описать:
- the problem
- target users
- current pain
- current workaround
- desired outcome
- success criteria
- constraints
- risks
- non-goals
- unknowns
- assumptions
- follow-up questions

The interview is not a specification.

## 3. Inputs
Допустимые входы:
- free-form user idea
- rough feature request
- business problem
- product improvement request
- user pain description
- incomplete requirement draft
- partial notes from a previous discussion
- verbal or informal product request converted into text

Raw input is allowed to be incomplete.
Incomplete input must produce follow-up questions, not invented requirements.

## 4. Outputs
Ожидаемые выходы M45:
- structured interview answer record
- unknowns list
- assumptions list
- answered questions
- unanswered questions
- follow-up questions
- interview status
- non-approval warning

M45 may record user-provided success_criteria as interview evidence.
M45 must not transform those signals into industrial acceptance criteria.
Industrial acceptance criteria belong to M46.

M45 не должен выдавать:
- industrial specifications
- functional requirements
- non-functional requirements
- industrial acceptance criteria
- validation strategies
- task contracts
- queue entries
- execution plans
- UX briefs

## 5. Interview Evidence vs Industrial Spec
Interview evidence:
- records what the user said
- records what is missing
- records assumptions and unknowns
- prepares input for M46
- is not actionable for implementation

Industrial spec:
- transforms interview evidence into requirements
- defines functional requirements
- defines non-functional requirements
- defines industrial acceptance criteria
- defines validation strategy
- may become actionable only after review and approval

Interview evidence is not industrial spec.

## 6. Required Data
Минимально обязательные поля интервью:
- `problem_summary`
- `target_users`
- `desired_outcome`
- `success_criteria`
- `constraints` or explicit `NONE`
- `risks` or explicit `NONE`
- `non_goals` or explicit `NONE`
- `unknowns`
- `follow_up_questions` when important unknowns exist
- `non_approval_warning`

If a required field is missing from user input, it must be recorded as MISSING_FROM_INTERVIEW.

## 7. Optional Data
Опциональные (не всегда обязательные), но полезные поля:
- `current_workaround`
- `business_context`
- `technical_context`
- `UX_expectations`
- `integrations`
- `data_privacy_notes`
- `edge_cases`
- `examples`
- `references`

Правила:
- optional fields are recorded if provided
- missing optional fields do not normally block status progression
- optional fields may become important if their absence creates a known risk, unresolved contradiction, or major ambiguity

## 8. Unknowns Handling
Правила обработки неизвестного:
- unknowns must be explicit
- unknowns must appear in the `unknowns` field
- unknowns must not be silently resolved
- missing information must be recorded as `MISSING_FROM_INTERVIEW`
- assumptions must be marked as assumptions, not facts
- every important unknown should produce a follow-up question unless explicitly deferred
- deferred unknowns must remain visible and must not be treated as resolved

Missing information must be recorded as MISSING_FROM_INTERVIEW, not inferred.

Примеры:
- missing target users: `target_users: MISSING_FROM_INTERVIEW`
- vague success criteria: `success_criteria: MISSING_FROM_INTERVIEW` + уточняющий вопрос о метрике успеха
- explicit no constraints: `constraints: NONE`
- silent constraints: `constraints: MISSING_FROM_INTERVIEW`
- user gives solution but not problem: `problem_summary: MISSING_FROM_INTERVIEW`

## 9. Follow-up Question Policy
Follow-up questions должны быть:
- specific
- user-facing
- understandable to non-programmers
- tied to a missing field, ambiguity, contradiction, risk, deferred decision, or blocked condition
- not leading the user toward an invented answer
- phrased as clarification, not hidden design instruction

Примеры корректных вопросов:
1. «Кто именно будет основным пользователем этого решения?»
2. «Как вы поймёте, что проблема решена: по какому признаку или метрике?»
3. «Какие ограничения обязательны: сроки, бюджет, безопасность, юридические требования?»
4. «Что сейчас происходит, когда пользователь сталкивается с этой проблемой?»
5. «Какие варианты вы точно не хотите реализовывать (non-goals)?»

Анти-паттерн (leading question):
- «Правильно ли я понимаю, что вам точно нужен микросервис на Kubernetes?»

## 10. Interview Status Model
Допустимы только следующие статусы:
- `INTERVIEW_DRAFT`
- `INTERVIEW_NEEDS_CLARIFICATION`
- `INTERVIEW_READY_FOR_SPEC`
- `INTERVIEW_BLOCKED`

Определения:
- `INTERVIEW_DRAFT` means the interview has started but is not structurally complete and is not ready for M46
- `INTERVIEW_NEEDS_CLARIFICATION` means required information is missing, ambiguous, contradictory, or insufficient
- `INTERVIEW_READY_FOR_SPEC` means required fields are present and usable for M46
- `INTERVIEW_BLOCKED` means the interview cannot proceed until an external blocker is resolved

INTERVIEW_READY_FOR_SPEC does not mean approved for implementation.

## 11. Non-Approval Boundary
- interview evidence is not approval
- interview completeness is not execution readiness
- interview readiness does not authorize implementation
- interview readiness does not authorize task creation
- interview readiness does not authorize queue entry creation
- interview readiness does not authorize autopilot
- interview readiness does not authorize commit, push, merge, release, or deployment
- interview evidence does not replace human review
- interview evidence does not replace approval evidence

Interview completeness is not execution readiness.

## 12. M45 to M46 Boundary
M45 формирует структурированное понимание проблемы и пробелов.
M46 превращает это понимание в:
- industrial spec
- functional requirements
- non-functional requirements
- industrial acceptance criteria
- validation strategy
- risk mapping
- constraint mapping
- implementation-facing requirement structure

M45 may list what M46 is expected to produce, but M45 must not produce those artifacts.
References to industrial spec, functional requirements, non-functional requirements, industrial acceptance criteria, validation strategy, risk mapping, and constraint mapping describe M46 responsibilities only.
They are not allowed outputs of M45.

No interview evidence → no industrial spec.
No interview evidence -> no industrial spec.
M45 = ask correctly, record answers, detect gaps.
M46 = transform interview evidence into industrial specification.

## 13. Failure / Blocked Conditions
Интервью не готово к M46, если есть хотя бы одно из условий:
- no `problem_summary`
- no `target_users`
- no `desired_outcome`
- no `success_criteria`
- `constraints` missing and not marked `NONE`
- `risks` missing and not marked `NONE`
- `non_goals` missing and not marked `NONE`
- important unknowns exist without follow-up questions
- unanswered questions are silently ignored
- assumptions are presented as facts
- user request is too ambiguous to structure
- user request conflicts with project boundaries
- user request requires legal decision before requirements work
- user request requires security decision before requirements work
- user request requires owner decision before requirements work
- interview record attempts to approve implementation
- interview record attempts to create task contracts
- interview record attempts to create queue entries
- interview record attempts to start autopilot

A blocked interview must not be converted into a spec by inference.

## 14. Final Architecture Summary
M45 = ask correctly, record answers, detect gaps.
M46 = transform interview evidence into industrial specification.

Interview evidence is not industrial spec.
Interview completeness is not execution readiness.
No interview evidence → no industrial spec.
No interview evidence -> no industrial spec.
Missing information must be recorded as MISSING_FROM_INTERVIEW, not inferred.
INTERVIEW_READY_FOR_SPEC does not mean approved for implementation.
