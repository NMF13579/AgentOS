# Interview Gap Decision Card Template

## 1. Metadata
```yaml
card_id: ""
created_at: ""
source_interview_id: ""
source_checker_result: ""
source_interview_status: ""
gap_type: ""
```

Allowed source_checker_result values:
- COMPLETENESS_INCOMPLETE
- COMPLETENESS_NEEDS_CLARIFICATION
- COMPLETENESS_BLOCKED
- COMPLETENESS_CHECK_FAILED

Allowed source_interview_status values:
- INTERVIEW_DRAFT
- INTERVIEW_NEEDS_CLARIFICATION
- INTERVIEW_READY_FOR_SPEC
- INTERVIEW_BLOCKED

Allowed gap_type values:
- MISSING_REQUIRED_FIELD
- AMBIGUOUS_ANSWER
- CONTRADICTION
- UNKNOWN_WITHOUT_FOLLOWUP
- EXTERNAL_DECISION_REQUIRED
- INVALID_RECORD_SHAPE
- INVALID_NON_APPROVAL_WARNING
- BLOCKED_CONDITION

## 2. Source Status Clarification
source_interview_status is the status stored in the interview record.
It is not the decision card result.
It is not proof that the interview is actually complete.
Checker results may override misleading interview_status when information is missing.

source_interview_status may say INTERVIEW_READY_FOR_SPEC while source_checker_result says COMPLETENESS_NEEDS_CLARIFICATION.
In that case, the checker result explains the gap and the card must not treat READY_FOR_SPEC as approval or true completeness.

## 3. What Is Missing or Unclear
```yaml
missing_or_unclear_information: ""
```

Describe only what is missing, unclear, contradictory, blocked, or invalid.
Do not invent the missing answer.

## 4. Why It Matters
```yaml
why_it_matters: ""
```

Explain why this information is needed before downstream specification work.

## 5. Risk If Skipped
```yaml
risk_if_skipped: ""
```

Explain the risk in simple language.
Do not reduce or hide the risk.

## 6. Recommended Follow-up Question
```yaml
recommended_follow_up_question: ""
```

Ask one clear, non-leading question.
Do not suggest a preferred implementation.

## 7. Assumption Option
```yaml
can_continue_with_assumption: "unknown"
assumption_warning: ""
```

Allowed can_continue_with_assumption values:
- yes
- no
- unknown

If an assumption is possible, it must be explicit and visible.
Assumptions must be marked as assumptions, not facts.

## 8. If User Does Not Know
```yaml
what_if_user_does_not_know: ""
```

Explain safe options if the user does not know the answer.

## 9. Safe Next Action
```yaml
safe_next_action: ""
```

Allowed examples:
- ask follow-up question
- keep unknown visible
- ask owner
- ask legal/security reviewer
- mark explicit assumption
- block until decision
- fix record shape before continuing

## 10. Internal Integrity Gap Note
INVALID_NON_APPROVAL_WARNING is an internal record integrity gap.
It should be shown to maintainers or agents, not directly to non-technical users.
If surfaced to a user, translate it as: "The interview record is missing a required safety warning, so it cannot be trusted yet."

## 11. Non-Approval Warning
```yaml
non_approval_warning: "Decision card explains. Decision card does not approve. Decision card does not invent answers. Decision card does not reduce risk. Decision card does not replace human gate."
```

## 12. Final Boundary
Interview evidence is not industrial spec.
Interview completeness is not execution readiness.
Decision card explains.
Decision card does not approve.
Decision card does not invent answers.
Decision card does not reduce risk.
Decision card does not replace human gate.
No interview evidence → no industrial spec.
No interview evidence -> no industrial spec.
M45 = ask correctly, record answers, detect gaps.
M46 = transform interview evidence into industrial specification.
