# Negative Fixture - missing-decision-rationale

## Category

trace

## Purpose

Verify that validator rejects a Trace with no decision rationale section.

## Expected Tool

future trace validator / guard test runner

## Expected Result

FAIL - decision rationale is required

## Notes

Payload file: TRACE.md (added in Task 7.1.2)

## Manual Verification

Command: future trace validator / guard test runner

Expected: FAIL

Reason: TRACE.md does not explain why the task was shaped this way
