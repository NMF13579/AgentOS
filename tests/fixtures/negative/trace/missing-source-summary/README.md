# Negative Fixture - missing-source-summary

## Category

trace

## Purpose

Verify that validator rejects a Trace with no source summary section.

## Expected Tool

future trace validator / guard test runner

## Expected Result

FAIL - source summary is required

## Notes

Payload file: TRACE.md (added in Task 7.1.2)

## Manual Verification

Command: future trace validator / guard test runner

Expected: FAIL

Reason: TRACE.md does not summarize the source discussion or input
