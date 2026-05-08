# M27 Violation Enforcement Runtime

## Purpose

Runtime evaluation of violation records into required sanctions and next permission state.

## Relationship to M26 Violation Policy

M26 defines violation/sanction policy; M27 enforces policy as runtime decisions.

## Relationship to M27 Runtime Boundary

This runtime is mandatory boundary logic, not optional helper tooling.

## Relationship to 27.2.1 Permission State

Optional permission-state input is validated through `scripts/agentos-permission-state.py` subprocess.

## Relationship to 27.6.1 Identity Boundary

Agent cannot self-clear violations, reduce severity, or mark false positive.

## Relationship to 27.7.1 Audit Log

If `--audit-log` is provided, enforcement decision is appended through `scripts/agentos-audit-log.py`.

## Relationship to 27.8.1 Human Gate

If `--human-gate-record` is provided, it is validated through `scripts/agentos-human-gate.py`.

## Violation Categories

- `SCOPE_VIOLATION`
- `FORBIDDEN_COMMAND`
- `FORBIDDEN_WRITE`
- `UNAPPROVED_PUSH`
- `DIRECT_PROTECTED_BRANCH_PUSH`
- `FORCE_PUSH_ATTEMPT`
- `REMOTE_BRANCH_DELETE_ATTEMPT`
- `VALIDATION_BYPASS`
- `EVIDENCE_TAMPERING`
- `PERMISSION_ESCALATION_ATTEMPT`
- `APPROVAL_SIMULATION`
- `AUTO_MERGE_ATTEMPT`
- `REPEATED_FAILURE`
- `UNBOUNDED_RETRY`
- `HUMAN_IMPERSONATION`
- `AGENT_ADMIN_TOKEN_EXPOSURE`
- `RUNNER_CREDENTIAL_LEAK`
- `UNKNOWN_VIOLATION`

## Severity Values

- `LOW`
- `MEDIUM`
- `HIGH`
- `CRITICAL`
- `UNKNOWN`

## Sanction Values

- `RECORD_ONLY`
- `REQUIRE_HUMAN_REVIEW`
- `REDUCE_TO_READ_ONLY`
- `BLOCK_TASK`
- `RESET_TO_LAST_SAFE_STATE`
- `RETRY_WITH_REDUCED_PERMISSIONS`
- `ESCALATE_TO_OWNER`
- `DISALLOW_AUTOPILOT`
- `BLOCK_AGENT`

## Result Value Exit Semantics

- `SANCTION_REQUIRED` => exit 0
- `SANCTION_APPLIED` => exit 0
- `TASK_BLOCKED` => exit 1
- `AGENT_BLOCKED` => exit 1
- `NEEDS_OWNER_REVIEW` => exit 1
- `NEEDS_HUMAN_REVIEW` => exit 1
- `VIOLATION_INVALID` => exit 1
- `VIOLATION_NEEDS_REVIEW` => exit 1
- `PERMISSION_INVALID` => exit 1

## Evaluation Order

1. Parse arguments.
2. Load violation record.
3. Validate required fields.
4. Validate category/severity.
5. Detect self-clear/downgrade/false-positive attempts.
6. Load permission state if provided.
7. Validate permission state via 27.2.1 subprocess.
8. Map category/severity to sanctions.
9. Apply CRITICAL escalation rules.
10. Compute next permission state.
11. Validate human gate if provided.
12. On apply: write only to `--state-out`.
13. Append audit only if `--audit-log` is provided.
14. Return final result.

## Sanction Mapping

- LOW => at least `RECORD_ONLY`
- MEDIUM => at least `REQUIRE_HUMAN_REVIEW`
- HIGH => at least `REDUCE_TO_READ_ONLY` + `REQUIRE_HUMAN_REVIEW`
- CRITICAL => `BLOCK_TASK` or `BLOCK_AGENT` + `ESCALATE_TO_OWNER`

Hard CRITICAL categories:
- `EVIDENCE_TAMPERING`
- `APPROVAL_SIMULATION`
- `HUMAN_IMPERSONATION`
- `AGENT_ADMIN_TOKEN_EXPOSURE`
- `DIRECT_PROTECTED_BRANCH_PUSH`

`UNBOUNDED_RETRY` requires `DISALLOW_AUTOPILOT` and human review.

## Permission State Behavior

- If permission state is provided, validate via subprocess.
- If invalid => `PERMISSION_INVALID`.
- If already blocked => continuation remains blocked.
- `REDUCE_TO_READ_ONLY` computes next permission `READ_ONLY`.
- `BLOCK_TASK`/`BLOCK_AGENT` compute blocked state + `BLOCKED` permission.
- Enforcement never increases permission.
- Enforcement never resets `retry_count`.
- Enforcement never clears `open_violations`.

## Apply Behavior

- `evaluate` is read-only.
- `apply` writes only to `--state-out`.
- `apply` must not overwrite input permission state.
- `apply` fails if `--state-out` missing.
- `apply` does not clear violation records.

## Human Gate Behavior

- Human gate can be required for restoration/continuation exceptions.
- If record provided, validate through 27.8.1.
- Agent-created human gate record is invalid.
- Human gate approval alone does not clear violations.
- Exit from BLOCKED requires owner/admin process (not implemented here).

## Audit Behavior

- If `--audit-log` provided, append enforcement decision through 27.7.1 script.
- If audit append fails, enforcement fails closed as `VIOLATION_NEEDS_REVIEW`.
- Audit record is not approval and does not authorize continuation.

## Prohibitions

- Self-clear prohibition: enforced.
- Severity downgrade prohibition: enforced.
- False-positive prohibition: enforced.
- `BLOCK_TASK`/`BLOCK_AGENT` override continuation.

## CLI Output Examples

```text
RESULT: SANCTION_REQUIRED
REASON: sanction computed
```

```text
RESULT: TASK_BLOCKED
REASON: critical sanction requires blocking task
```

```text
RESULT: NEEDS_OWNER_REVIEW
REASON: severity downgrade attempt detected
```

## Non-Authorization Clauses

- This runtime is not approval.
- It does not authorize commit.
- It does not authorize push.
- It does not authorize merge.
- It does not authorize release.
- It does not authorize retry.
- It does not clear violations by itself.
