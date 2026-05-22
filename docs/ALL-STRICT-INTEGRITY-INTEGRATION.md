# All Strict Integrity Integration

## Purpose
This document explains how `all --strict` includes integrity checks while preserving strict boundaries.

all --strict may include integrity checks, but it must not turn validation PASS into human approval.
INTEGRITY_WARNING is not clean PASS.
Unified status is navigation metadata, not replacement for source token.
all --strict must not parse human-readable summary output.
Human approval remains above every PASS.

## Integration Relationship
- `all --strict` runs existing strict checks.
- It also runs `integrity --strict --fixtures --json`.
- Integrity integration is additive and must preserve existing `all --strict` behavior.

## Source Token Preservation
- The integrity run keeps source tokens in nested integrity output.
- `all --strict` preserves minimum required details:
  - integrity command run
  - integrity result
  - exit code
- Optional fields (source tokens, counts, next safe action) are included when available.

## Warning Behavior
- `INTEGRITY_WARNING` may keep exit code zero.
- `INTEGRITY_WARNING` is not clean PASS.

## Blocking Behavior
- `INTEGRITY_VIOLATION` -> exit 1 (non-zero)
- `INTEGRITY_BLOCKED` -> exit 1 (non-zero)
- `INTEGRITY_NEEDS_REVIEW` -> exit 1 (non-zero)

## JSON Behavior
- `all --strict` must consume integrity JSON internally.
- It must not parse human-readable summary output.
- If integrity JSON parsing fails, strict integration must fail non-zero.

## Non-approval Boundary
M41.5 does not create new validators.
M41.5 does not create new security policy.
M41.5 does not change source-token semantics.
M41.5 does not replace human approval.
