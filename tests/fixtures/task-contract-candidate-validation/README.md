# M52 Candidate Validation Fixtures

## Purpose

Fixture suite validates M52 candidate validator behavior for safe candidate readiness checks.

Candidate validation fixtures are not approval.
Candidate validation fixtures do not authorize execution.
Candidate validation fixtures do not authorize queue placement.
Candidate validation fixtures do not authorize active-task replacement.
Candidate validation fixtures do not authorize M53 placement.
Fixtures prove validator behavior; fixtures do not create lifecycle state.
Document fixtures test artifact validation.
CLI fixtures test invocation semantics.

## Directory Layout

- `positive/` valid generated conversion package candidates
- `negative/` malformed, missing, or authority-escalation candidates
- `cli-negative/` invocation semantics fixtures
- `sources/` baseline source/traceability fixtures

## Expected Result Classes

- `TASK_CONTRACT_CANDIDATE_VALIDATION_OK`
- `TASK_CONTRACT_CANDIDATE_VALIDATION_OK_WITH_LIMITATIONS`
- `TASK_CONTRACT_CANDIDATE_VALIDATION_FAILED`
- `TASK_CONTRACT_CANDIDATE_VALIDATION_BLOCKED`

## Expected M52 Result Metadata

Expected M52 Result:
- expected_result: TASK_CONTRACT_CANDIDATE_VALIDATION_FAILED

Expected M52 Result:
- expected_result: TASK_CONTRACT_CANDIDATE_VALIDATION_BLOCKED

## Invalid Test Content Metadata

Invalid Test Content:
- This forbidden language is present only to verify that the validator rejects it.
- This fixture does not authorize the forbidden action.

## Notes

- candidate-without-conversion-package-wrapper fixture verifies wrapper-required behavior
- missing-source-authorization fixture is BLOCKED because trusted lineage cannot be established
