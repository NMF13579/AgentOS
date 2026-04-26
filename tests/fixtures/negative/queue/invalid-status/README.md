# Negative Fixture - invalid-status

## Category

queue

## Purpose

Verify that queue validator rejects an entry with an unrecognised status value.

## Expected Tool

future queue validator / guard test runner

## Expected Result

FAIL - status must be one of: queued, blocked, in_progress, done, dropped

## Notes

Payload file: queue-entry.md (added in Task 7.1.2)

## Manual Verification

Command: future queue validator / guard test runner

Expected: FAIL

Reason: queue entry status is not one of: queued, blocked, in_progress, done, dropped
