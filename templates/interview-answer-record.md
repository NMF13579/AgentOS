# Interview Answer Record

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

idea_summary must not add information not present in source_user_input.
idea_summary must be shorter, neutral, and less specific than source_user_input.

## 3. Problem Understanding
```yaml
problem_summary: "MISSING_FROM_INTERVIEW"
target_users: "MISSING_FROM_INTERVIEW"
current_workaround: "MISSING_FROM_INTERVIEW"
desired_outcome: "MISSING_FROM_INTERVIEW"
success_criteria: "MISSING_FROM_INTERVIEW"
```

M45 records user-level success_criteria.

## 4. Boundaries
```yaml
constraints: "MISSING_FROM_INTERVIEW"
risks: "MISSING_FROM_INTERVIEW"
non_goals: "MISSING_FROM_INTERVIEW"
```

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

Missing information must be recorded as MISSING_FROM_INTERVIEW, not inferred.
Missing information must become follow-up questions, not hallucinated requirements.
Assumptions must be marked as assumptions, not facts.

## 6. Non-Approval Warning
Interview evidence is not approval. Interview readiness does not authorize implementation, task creation, queue entry creation, autopilot, commit, push, merge, release, or deployment.

Interview evidence is not industrial spec.
Interview completeness is not execution readiness.
INTERVIEW_READY_FOR_SPEC does not mean approved for implementation.

## 7. M45/M46 Boundary
No interview evidence → no industrial spec.
No interview evidence -> no industrial spec.

M45 = ask correctly, record answers, detect gaps.
M46 = transform interview evidence into industrial specification.

The Unicode arrow form is canonical. The ASCII-compatible form exists only for copy/paste and plain-text compatibility.
