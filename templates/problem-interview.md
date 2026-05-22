# Problem Interview Template

## 1. Metadata
```yaml
interview_id: ""
created_at: ""
interview_status: "INTERVIEW_DRAFT"
```

Allowed statuses:
- INTERVIEW_DRAFT
- INTERVIEW_NEEDS_CLARIFICATION
- INTERVIEW_READY_FOR_SPEC
- INTERVIEW_BLOCKED

INTERVIEW_READY_FOR_SPEC does not mean approved for implementation.

## 2. Source Input
```yaml
source_user_input: ""
idea_summary: ""
```

Rules:
- `source_user_input` records the raw user idea or request.
- `idea_summary` may summarize the idea in simple language.
- `idea_summary` must be shorter, neutral, and less specific than `source_user_input`.
- `idea_summary` must not add information not present in `source_user_input`.
- `idea_summary` must not add new features, constraints, risks, users, integrations, acceptance criteria, or implementation details.
- If `source_user_input` is unclear, `idea_summary` must preserve that uncertainty instead of improving the idea.
- The summary must not invent requirements.

idea_summary must not add information not present in source_user_input.

## 3. Problem Understanding
```yaml
problem_summary: "MISSING_FROM_INTERVIEW"
target_users: "MISSING_FROM_INTERVIEW"
current_workaround: "MISSING_FROM_INTERVIEW"
desired_outcome: "MISSING_FROM_INTERVIEW"
success_criteria: "MISSING_FROM_INTERVIEW"
```

Rules:
- `problem_summary` records the problem, not the solution.
- `target_users` records who is affected or who will use the result.
- `current_workaround` records what users do today.
- `desired_outcome` records what should improve.
- `success_criteria` records user-level success signals.
- `success_criteria` must not be transformed into formal industrial acceptance criteria.

M45 records user-level success_criteria.

## 4. Boundaries
```yaml
constraints: "MISSING_FROM_INTERVIEW"
risks: "MISSING_FROM_INTERVIEW"
non_goals: "MISSING_FROM_INTERVIEW"
```

Rules:
- Use `MISSING_FROM_INTERVIEW` when the user has not provided the information.
- Use `NONE` only when the user explicitly says there are no constraints, risks, or non-goals.
- Do not infer absence from silence.

Use NONE only when the user explicitly says there are no constraints.
Use NONE only when the user explicitly says there are no risks.
Use NONE only when the user explicitly says there are no non-goals.

## 5. Gaps and Clarifications
```yaml
unknowns: []
assumptions: []
answered_questions: []
unanswered_questions: []
follow_up_questions: []
```

Rules:
- Unknowns must remain explicit.
- Assumptions must be marked as assumptions, not facts.
- Every important missing field or unresolved ambiguity should produce a follow-up question unless explicitly deferred.
- Missing information must not be silently filled.

Missing information must be recorded as MISSING_FROM_INTERVIEW, not inferred.
Missing information must become follow-up questions, not hallucinated requirements.
Assumptions must be marked as assumptions, not facts.

## 6. Non-Approval Warning
```yaml
non_approval_warning: "Interview evidence is not approval. Interview readiness does not authorize implementation, task creation, queue entry creation, autopilot, commit, push, merge, release, or deployment."
```

Interview evidence is not industrial spec.
Interview completeness is not execution readiness.
No interview evidence → no industrial spec.
No interview evidence -> no industrial spec.
INTERVIEW_READY_FOR_SPEC does not mean approved for implementation.

The Unicode arrow form is canonical. The ASCII-compatible form exists only for copy/paste and plain-text compatibility.

## 7. Human-Readable Filling Notes
- Use the user's words when possible.
- Do not invent missing requirements.
- Mark missing required fields as `MISSING_FROM_INTERVIEW`.
- Use `NONE` only when the user explicitly says none.
- Write assumptions as assumptions, not facts.
- Generate follow-up questions for important unknowns.
- Preserve user intent.
- Do not create industrial spec content inside the interview template.
- Keep `idea_summary` neutral and shorter than `source_user_input`.
- Do not add information to `idea_summary` that is not present in `source_user_input`.
