# Negative Fixture - blocked-without-blocked-by

## Category

queue

## Purpose

Verify that queue validator rejects a blocked entry with an empty blocked_by list.

## Expected Tool

future queue validator / guard test runner

## Expected Result

FAIL - blocked status requires at least one blocked_by entry

## Notes

Payload file: queue-entry.md (added in Task 7.1.2)

## Manual Verification

Command: future queue validator / guard test runner

Expected: FAIL

Reason: blocked queue entry has empty blocked_by list
