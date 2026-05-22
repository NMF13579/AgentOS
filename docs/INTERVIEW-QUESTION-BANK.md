# Interview Question Bank

## 1. Purpose
Этот документ задает стандартный набор вопросов для структурированного problem interview в M45.

- question bank supports M45 interview evidence
- question bank does not create industrial specs
- question bank does not create UX
- question bank does not create task contracts
- question bank does not create queue entries
- question bank does not authorize execution
- question bank does not approve anything

Question bank suggests questions, not requirements.

## 2. Question Principles
- вопросы должны быть понятными
- вопросы должны быть non-leading (не подталкивать к нужному ответу)
- вопросы должны быть понятны не-программистам
- каждый вопрос должен быть привязан к конкретному полю интервью, unknown, ambiguity, contradiction, risk или blocked condition
- вопросы не должны придумывать фичи
- вопросы не должны навязывать способ реализации
- вопросы не должны навязывать технологию
- вопросы не должны превращать user answers в formal industrial acceptance criteria
- вопросы должны сохранять смысл, который дал пользователь
- вопросы должны выявлять missing information
- вопросы должны поддерживать `follow_up_questions`

Missing information must become follow-up questions, not hallucinated requirements.

## 3. Anti-Patterns
Запрещенные шаблоны вопросов:
- leading questions
- solution-inventing questions
- implementation-presuming questions
- technology-presuming questions
- questions that hide assumptions
- questions that ask multiple unrelated things at once
- questions that turn `success_criteria` into formal industrial acceptance criteria
- questions that imply approval or execution readiness

Bad:
Should we build a mobile app and web dashboard?

Почему плохо: навязывает конкретное решение вместо выяснения проблемы.

Bad:
Do you want PostgreSQL for the database?

Почему плохо: навязывает технологию до понимания задачи.

Bad:
Should the system use AI to solve this automatically?

Почему плохо: навязывает реализацию и расширяет scope без подтверждения пользователя.

Bad:
Should we add admin roles, analytics, export, and notifications?

Почему плохо: объединяет много несвязанных решений в одном вопросе и добавляет не подтвержденные фичи.

Bad:
Should this be ready for implementation now?

Почему плохо: создаёт ложный сигнал о readiness/approval.

## 4. Problem Framing Questions
Поле: `problem_summary`

- What problem are you trying to solve?
- What is happening today that should change?
- Why is this problem important now?
- What happens if this problem is not solved?
- What part of the current process feels broken, slow, confusing, expensive, or risky?
- Is this mainly a user problem, business problem, operational problem, technical problem, or something else?

Problem framing must capture the problem before jumping to a solution.

## 5. Target User Questions
Поле: `target_users`

- Who will use this?
- Who is affected by this problem?
- Are the users internal staff, customers, partners, admins, operators, managers, or someone else?
- Are there different user groups with different needs?
- Who experiences the pain most strongly?
- Who decides whether the result is acceptable?

Missing target users must be recorded as MISSING_FROM_INTERVIEW.

## 6. Current Pain Questions
Поля: `problem_summary`, `current_workaround`, `unknowns`, `follow_up_questions`

- What is difficult or frustrating today?
- Where do users lose time?
- Where do errors happen?
- What causes confusion?
- What is the most expensive or risky part of the current process?
- What do users complain about most often?
- What currently requires manual effort?

Answers from Current Pain Questions must first be recorded as user-provided current-state evidence.
If the answer describes how users currently cope with the pain, record it in current_workaround.
If the answer clarifies the core problem, use it to update problem_summary without adding information not present in the user answer.
Current pain answers must not be converted into requirements, solutions, or acceptance criteria.

If the pain is clear but the core problem is still not explicitly understood, problem_summary must remain MISSING_FROM_INTERVIEW and the agent must add a follow-up question.

## 7. Current Workaround Questions
Поле: `current_workaround`

- How do users handle this today?
- What tools, documents, chats, spreadsheets, forms, or manual steps are used now?
- What works acceptably in the current workaround?
- What fails often in the current workaround?
- What should not be lost from the current workaround?
- Who owns or maintains the current workaround?

## 8. Desired Outcome Questions
Поле: `desired_outcome`

- What should be different after this is solved?
- What should the user be able to do that they cannot do now?
- What should become faster, safer, simpler, clearer, or more reliable?
- What would a good result look like in plain language?
- What should the user see, know, receive, or experience when the solution works?
- What would make the current pain disappear or become acceptable?

## 9. Success Criteria Questions
Поле: `success_criteria`

M45 records user-level success_criteria.
M45 does not create formal industrial acceptance criteria.
Formal acceptance criteria belong to M46.

- How will you know this is working?
- What result would make you say this solved the problem?
- What should improve compared to today?
- What should become measurable, visible, or easier?
- What would make you reject the result as unsuccessful?
- What would make users trust that the problem is solved?
- What would be an early sign that the solution is useful?

Vague success criteria must be preserved as user input and clarified with follow-up questions, not converted into formal acceptance criteria.

## 10. Constraint Questions
Поле: `constraints`

- Are there any hard limits we must respect?
- Are there budget, timeline, team, platform, legal, or technical limits?
- Are there tools or systems that must be used?
- Are there tools or systems that must not be used?
- Are there existing project rules this must follow?
- Are there deadlines or external dependencies?
- Are there limits caused by existing users, data, architecture, or business process?

Use NONE only when the user explicitly says there are no constraints.
Silence about constraints means MISSING_FROM_INTERVIEW, not NONE.

## 11. Risk Questions
Поле: `risks`

- What could go wrong?
- What would make this unsafe, unreliable, or unusable?
- What mistake would be expensive or dangerous?
- What should the system avoid doing?
- What would make users lose trust?
- What data, workflow, or decision would be risky to handle incorrectly?
- What failure would be unacceptable?

Use NONE only when the user explicitly says there are no risks.
Unresolved legal, privacy, security, or safety concerns may produce INTERVIEW_BLOCKED.

## 12. Non-Goal Questions
Поле: `non_goals`

- What should definitely not change?
- What should not be built in this version?
- What is outside the scope of this request?
- What existing behavior must be preserved?
- What tempting feature should be avoided for now?
- What would make this task too broad?
- What should be postponed to a later milestone?

Use NONE only when the user explicitly says there are no non-goals.
Missing non-goals should not be treated as permission to expand scope.

## 13. UX Expectation Questions
Поля: `desired_outcome`, `unknowns`, `follow_up_questions`, optional `UX_expectations`

- What should the user experience feel like?
- Should this be simple, guided, detailed, fast, visual, minimal, or something else?
- Where does the user currently get confused?
- What information should be visible to the user?
- What should be hidden unless needed?
- What would make the experience feel trustworthy?
- What should the user be able to understand without help?

UX expectation questions collect interview evidence. They do not create UX briefs.

Answers from UX Expectation Questions must be recorded as interview evidence.
If the answer describes the desired user experience outcome, record it in desired_outcome.
If the answer introduces unresolved UX uncertainty, record it in unknowns and add follow_up_questions.
If the template supports UX_expectations, record UX-specific expectations there.
UX expectation answers must not become UX briefs, wireframes, designs, or implementation requirements.

## 14. Data / Privacy / Security Questions
- What data will be involved?
- Is any data sensitive, private, regulated, confidential, or business-critical?
- Who should be allowed to see the data?
- Who should be allowed to change the data?
- What must never be exposed?
- Are there audit, consent, retention, or compliance concerns?
- Is there a legal or security decision that must happen before specification work continues?

Unresolved legal, privacy, or security concerns may lead to INTERVIEW_BLOCKED.

## 15. Integration Questions
- Does this need to connect to any existing tools or systems?
- Where does the data come from?
- Where should the result go?
- Are there existing APIs, exports, imports, files, forms, chats, or manual processes?
- What system is the source of truth today?
- What systems must not be changed?
- What integration failure would be unacceptable?

## 16. Edge Case Questions
- What unusual situations should still work?
- What happens when data is missing?
- What happens when the user makes a mistake?
- What happens when two users do conflicting things?
- What should happen when the system cannot complete the request?
- What happens if the current workaround fails?
- What should happen if the user does not know the answer?

## 17. Contradiction Questions
- These two answers seem to conflict. Which one should take priority?
- You mentioned both speed and manual approval. Which matters more in this case?
- You said there are no constraints, but also mentioned a required tool. Should that be recorded as a constraint?
- You said this is urgent, but also that it needs review. What is the safest next step?
- You described the solution, but the problem is still unclear. What problem should be solved first?
- You mentioned several user groups. Do they all need the same result?

Unresolved ordinary contradictions usually require INTERVIEW_NEEDS_CLARIFICATION.
Contradictions that require an external legal, security, owner, or business decision before continuing must produce INTERVIEW_BLOCKED.

If the user says "no approval is needed" but also says "legal must approve this", the interview must not resolve the contradiction by inference.
The correct status is INTERVIEW_BLOCKED until the required authority resolves the conflict.

## 18. Blocked Condition Questions
- Does this require a legal, security, owner, or business decision before we continue?
- Is there a policy or rule that must be checked first?
- Is there someone who must approve the direction before specification work starts?
- Is the request outside the current project boundary?
- Is there missing authority to decide this?
- Is there a known conflict with existing project rules?

Questions may identify a blocked condition, but the question bank does not approve or unblock anything.

## 19. Assumption Questions
- I do not have enough information about this. Should it remain unknown or should we make an explicit assumption?
- If we continue with this assumption, what risk should be recorded?
- Who should confirm this assumption later?
- Should this assumption block M46 or be carried forward as a known uncertainty?
- What would happen if this assumption is wrong?
- Is this assumption based on user input, project context, or guesswork?

Assumptions must be marked as assumptions, not facts.
Assumptions must not replace missing user answers.

## 20. Status Mapping
Используются только:
- INTERVIEW_DRAFT
- INTERVIEW_NEEDS_CLARIFICATION
- INTERVIEW_READY_FOR_SPEC
- INTERVIEW_BLOCKED

Incomplete or unprocessed interview records must stay INTERVIEW_DRAFT unless a blocking condition is already known.
Missing required answers must produce INTERVIEW_NEEDS_CLARIFICATION unless the missing answer depends on an external legal, security, owner, or business decision.
Ambiguous, contradictory, or insufficient answers must produce INTERVIEW_NEEDS_CLARIFICATION unless they require external authority to resolve.
Contradictions requiring external legal, security, owner, or business decision must produce INTERVIEW_BLOCKED.
Unresolved external decisions must produce INTERVIEW_BLOCKED.
Complete required answers may produce INTERVIEW_READY_FOR_SPEC only when required fields are present, unknowns are documented, and no blocker exists.
INTERVIEW_READY_FOR_SPEC is not approval.

INTERVIEW_READY_FOR_SPEC does not mean approved for implementation.

## 21. Final Boundary
Interview evidence is not industrial spec.
Interview completeness is not execution readiness.
No interview evidence → no industrial spec.
No interview evidence -> no industrial spec.
Missing information must be recorded as MISSING_FROM_INTERVIEW, not inferred.
Missing information must become follow-up questions, not hallucinated requirements.
Question bank suggests questions, not requirements.
M45 = ask correctly, record answers, detect gaps.
M46 = transform interview evidence into industrial specification.

The Unicode arrow form is canonical. The ASCII-compatible form exists only for copy/paste and plain-text compatibility.
