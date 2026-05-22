# Interview Completeness Smoke

## 1. Purpose
Interview Completeness Smoke verifies representative end-to-end behavior of the M45 interview layer using fixtures and the completeness checker.

Interview Completeness Smoke verifies the interview layer, not industrial spec generation.

## 2. Relationship to Previous M45 Artifacts
- 45.1 defines architecture.
- 45.2 defines template.
- 45.3 defines safe questions.
- 45.4 defines answer record contract.
- 45.5 defines missing information detection.
- 45.6 verifies representative end-to-end behavior.

## 3. Smoke Scope
Smoke verifies:
- checker can read valid interview records
- complete record produces `COMPLETENESS_COMPLETE`
- missing target users produces `COMPLETENESS_NEEDS_CLARIFICATION`
- missing success criteria produces `COMPLETENESS_NEEDS_CLARIFICATION`
- unknowns without follow-up produces `COMPLETENESS_INCOMPLETE`

The smoke runner calls the checker in default text mode and parses the checker result from the first stdout line that starts with "RESULT:".

The smoke runner must not assume that RESULT is the first stdout line.
It must scan all checker stdout lines and use the first line that starts with "RESULT:".

## 4. Smoke Result Namespace
- `INTERVIEW_LAYER_SMOKE_PASS`
- `INTERVIEW_LAYER_SMOKE_FAIL`
- `INTERVIEW_LAYER_SMOKE_CHECK_FAILED`

Smoke result values are smoke outcomes, not interview_status values.

## 5. Checker Result Expectations
Smoke cases:
- `complete-interview.json` => `COMPLETENESS_COMPLETE`, exit 0
- `missing-user.json` => `COMPLETENESS_NEEDS_CLARIFICATION`, exit 1
- `missing-success-criteria.json` => `COMPLETENESS_NEEDS_CLARIFICATION`, exit 1
- `unknowns-without-followup.json` => `COMPLETENESS_INCOMPLETE`, exit 1

## 6. Smoke Parser Rule
- smoke calls checker without `--json` or `--explain` for normal case execution
- smoke reads checker stdout
- smoke scans all checker stdout lines
- parse checker RESULT from the first stdout line that starts with "RESULT:"
- smoke does not parse checker result from stderr
- treat missing RESULT line as INTERVIEW_LAYER_SMOKE_CHECK_FAILED
- do not assume RESULT is the first stdout line
- scan all checker stdout lines and use the first line that starts with "RESULT:"

## 7. Fixture Failure Reason Boundary
Smoke fixtures must fail for their intended completeness condition only.

They must not fail because of malformed JSON, missing unrelated required fields, invalid status, invalid warning, forbidden fields, or missing base shape.

## 8. Non-Approval Boundary
Smoke PASS is not approval.
Smoke PASS does not create industrial spec.
Smoke PASS does not authorize implementation.
Smoke PASS does not authorize M46 by itself.
Smoke PASS does not authorize task creation or queue entry creation.

## 9. Fixture Policy
- Smoke fixtures are representative examples.
- Smoke fixtures are not production specs.
- Smoke fixtures must not include M46 fields.
- Smoke fixtures must not include execution readiness fields.
- Smoke fixtures must use only allowed interview statuses.

## 10. Final Boundary
Interview evidence is not industrial spec.
Interview completeness is not execution readiness.
Schema validity is not interview completeness.
Completeness check is not approval.
Smoke PASS is not approval.
No interview evidence → no industrial spec.
No interview evidence -> no industrial spec.
Missing information must be recorded as MISSING_FROM_INTERVIEW, not inferred.
Missing information must become follow-up questions, not hallucinated requirements.
INTERVIEW_READY_FOR_SPEC does not mean approved for implementation.
M45 = ask correctly, record answers, detect gaps.
M46 = transform interview evidence into industrial specification.
