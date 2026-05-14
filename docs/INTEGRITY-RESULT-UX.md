# Integrity Result UX

## Purpose
This document defines a user-facing explanation layer for integrity results.

UX explains results. UX must not change authority.
Unified status is navigation metadata, not replacement for source token.
PASS is a validation signal, not authorization.
Checker PASS is validation signal, not approval.
Human approval remains above every PASS.
INTEGRITY_WARNING is not clean PASS.
Summary output is user guidance, not evidence authority.

## Result UX Layer
M41.4 adds explanation and summary modes so users can understand outcomes and next safe actions.
The UX layer explains results; it does not alter checker authority, result authority, or approval boundaries.

## Source Token and Unified Token
- Source tokens come from domain checks.
- Unified tokens (`INTEGRITY_*`) are navigation tokens.
- Source tokens must be preserved in machine output.

## Modes
- `integrity --explain-results`: explains all integrity result tokens.
- `integrity --explain-result <TOKEN>`: explains one token.
- `integrity --fixtures --summary`: prints human summary for non-strict run.
- `integrity --strict --fixtures --summary`: prints human summary for strict run.

## Next Safe Action
Each integrity result maps to a next safe action:
- `INTEGRITY_OK`: continue normal validation or maintainer review.
- `INTEGRITY_WARNING`: review warnings and limitations before claiming completion.
- `INTEGRITY_VIOLATION`: stop completion, fix cause, rerun.
- `INTEGRITY_NEEDS_REVIEW`: require maintainer or human review.
- `INTEGRITY_BLOCKED`: fix dependency/precondition first.

## Strict-Mode Interpretation
Strict summary keeps warning visibility and reminds that warnings are not clean pass.
Warnings do not become blocking in M41.4.

## Human Approval Boundary
Integrity checks and summaries do not grant approval.
Human approval remains above every PASS.

## Limitation Language
- Summary explains results but is not evidence authority.
- UX can guide action, but it cannot authorize state transition.

## Non-goals
M41.4 does not create new validators.
M41.4 does not create new security policy.
M41.4 does not change source-token semantics.
M41.4 does not replace human approval.
