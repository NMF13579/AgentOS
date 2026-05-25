# Controlled Execution Session Negative Fixtures

## Purpose

This directory contains negative test fixture cases to validate the fail-closed and error handling behaviors of the M58 Controlled Execution Session CLI (`check-controlled-execution-session.py`).

## Fixture Cases

The following negative cases are defined:
- `negative-request-draft-not-ready`: Draft request must not proceed.
- `negative-request-blocked`: Blocked request status must fail closed.
- `negative-preconditions-blocked`: Blocked preconditions status must fail closed.
- `negative-boundary-not-satisfied`: Incomplete boundary input must produce NOT_READY status.
- `negative-boundary-blocked`: Blocked boundary status must fail closed.
- `negative-record-blocked`: Blocked record status must fail closed.
- `negative-record-aborted`: Aborted record status must fail closed.
- `negative-performed-action-violation`: Premature execution actions must be blocked.
- `negative-m59-handoff-disabled`: Handoff bypass attempts must be blocked.
- `negative-result-verification-claim`: Unauthorized verification claims must be blocked.
- `negative-task-complete-claim`: Premature completion claims must be blocked.
- `negative-push-allowed-claim`: Unauthorized push operations must be blocked.
- `negative-id-mismatch`: Identity mismatches across layers must block.
- `negative-unknown-status`: Unknown status values must fail closed.

## Expected Results

Expected outcome schemas, exit codes, and policy decisions are captured inside the `expected.json` oracle file inside each fixture case.

## Expected JSON as Oracle

Each fixture directory includes an `expected.json` containing the authoritative metadata oracle for checker evaluations.

## Fail-Closed Expectations

All safety hazards, contradictions, unknown configurations, and premature assertions must block evaluation, yielding `CONTROLLED_EXECUTION_SESSION_BLOCKED` and exit code 2.

## Not Ready vs Blocked Semantics

- **NOT_READY (exit 1)**: Represents configurations where the data is incomplete but does not present a safety or policy violation (e.g. draft statuses).
- **BLOCKED (exit 2)**: Represents safety violations, contradictions, or direct policy overrides.

## Non-Authority Rules

- M58 negative fixtures do not open an execution session.
- M58 negative fixtures do not authorize task completion.
- M58 negative fixtures do not verify execution result.
- M58 negative fixtures do not create approval.
- M58 negative fixtures do not authorize merge, push, or release.
- M58 negative fixtures do not mutate lifecycle state.
- M58 negative fixtures only provide fail-closed test data for the controlled execution session CLI.

## Relationship to 58.7 CLI

The CLI reads and validates these negative fixtures to ensure they correctly fail closed according to policy.

## Relationship to 58.8.1 Positive Fixtures

Positive fixtures cover valid readiness states, while negative fixtures assert that all policy restrictions are safely and strictly enforced.

## Relationship to 58.9 Fixture Runner

The fixture runner runs all positive and negative fixtures against the CLI, comparing actual outputs against the `expected.json` file.
