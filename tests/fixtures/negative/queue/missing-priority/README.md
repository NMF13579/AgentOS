# Negative Fixture - missing-priority

## Category

queue

## Purpose

Verify that queue validator rejects an entry with no priority field.

## Expected Tool

future queue validator / guard test runner

## Expected Result

FAIL - priority is required

## Notes

Payload file: queue-entry.md (added in Task 7.1.2)

## Manual Verification

Command: future queue validator / guard test runner

Expected: FAIL

Reason: queue entry has no priority
