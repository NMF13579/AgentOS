# Missing Information Detection

## 1. Purpose
Missing Information Detection checks whether interview evidence includes enough explicit information for M46 input review.

Missing Information Detection checks completeness, not approval.

## 2. Relationship to Previous M45 Artifacts
- 45.1 defines architecture boundary.
- 45.2 defines interview template.
- 45.3 defines safe question patterns.
- 45.4 defines interview answer record contract.
- 45.5 checks whether required interview information is present and usable.

## 3. Result Namespace
Completeness checker returns:
- `COMPLETENESS_COMPLETE`
- `COMPLETENESS_INCOMPLETE`
- `COMPLETENESS_NEEDS_CLARIFICATION`
- `COMPLETENESS_BLOCKED`
- `COMPLETENESS_CHECK_FAILED`

Completeness result values are checker outcomes, not interview_status values.

## 4. Required Fields
Required fields:
- `interview_id`
- `created_at`
- `interview_status`
- `source_user_input`
- `idea_summary`
- `problem_summary`
- `target_users`
- `current_workaround`
- `desired_outcome`
- `success_criteria`
- `constraints`
- `risks`
- `non_goals`
- `unknowns`
- `assumptions`
- `answered_questions`
- `unanswered_questions`
- `follow_up_questions`
- `non_approval_warning`

## 5. Required Information Rules
- `problem_summary`, `target_users`, `desired_outcome`, and `success_criteria` must not remain `MISSING_FROM_INTERVIEW`.
- `constraints`, `risks`, and `non_goals` must be user text or explicit `NONE`.
- Silence is not `NONE`.
- Missing information must produce follow-up questions.

Missing information must be recorded as MISSING_FROM_INTERVIEW, not inferred.
Missing information must become follow-up questions, not hallucinated requirements.

## 6. Unknowns and Follow-up Questions
In M45.5, unknowns must be paired with follow-up questions.

Unknowns without follow_up_questions are incomplete interview evidence.

## 7. Status vs Completeness
- `interview_status` belongs to the record.
- completeness result belongs to checker output.
- `INTERVIEW_READY_FOR_SPEC` does not override missing data.
- `INTERVIEW_BLOCKED` forces blocked result.
- `INTERVIEW_DRAFT` and `INTERVIEW_NEEDS_CLARIFICATION` cannot produce `COMPLETENESS_COMPLETE`.
- if no malformed input, missing required field, invalid status, invalid warning, blocked status, or unknowns-without-followup condition exists, both `INTERVIEW_DRAFT` and `INTERVIEW_NEEDS_CLARIFICATION` produce `COMPLETENESS_NEEDS_CLARIFICATION`.

Interview status cannot override missing information.
If interview_status is INTERVIEW_DRAFT and no higher-priority failure exists, result must be COMPLETENESS_NEEDS_CLARIFICATION.
If interview_status is INTERVIEW_NEEDS_CLARIFICATION and no higher-priority failure exists, result must be COMPLETENESS_NEEDS_CLARIFICATION.

## 8. Schema Validity Boundary
- Schema validity checks record shape.
- Completeness detection checks content readiness.
- Completeness detection is still not approval.

Schema validity is not interview completeness.

## 9. Output Stream Rules
- All expected checker output must be written to stdout.
- `RESULT`, `INTERVIEW_STATUS`, `RECORD_PATH`, warnings, blockers, and JSON output must be written to stdout.
- stderr is reserved for unexpected internal diagnostics only.

All expected checker output, including RESULT, must be written to stdout.

## 10. Non-Approval Boundary
Completeness check is not approval.
Completeness check does not authorize implementation.
Completeness check does not authorize M46 by itself.
Interview completeness is not execution readiness.

## 11. Final Boundary
Interview evidence is not industrial spec.
Interview completeness is not execution readiness.
Schema validity is not interview completeness.
Completeness check is not approval.
No interview evidence → no industrial spec.
No interview evidence -> no industrial spec.
Missing information must be recorded as MISSING_FROM_INTERVIEW, not inferred.
Missing information must become follow-up questions, not hallucinated requirements.
INTERVIEW_READY_FOR_SPEC does not mean approved for implementation.
M45 = ask correctly, record answers, detect gaps.
M46 = transform interview evidence into industrial specification.
