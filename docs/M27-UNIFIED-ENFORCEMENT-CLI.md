# M27 Unified Enforcement CLI

## Purpose

`agentos-enforce.py` is the mandatory M27 orchestration surface for guarded checks.
It routes to existing guard subsystems and does not replace them.

## Relationship to M27 Runtime Boundary

The CLI enforces one controlled entrypoint for risky checks; subsystem guard decisions remain authoritative.

## Relationship to 27.2.1 Permission State

`permission` routes to `scripts/agentos-permission-state.py`.

## Relationship to 27.3.1 Command Guard

`check-command` routes to `scripts/agentos-command-guard.py`.

## Relationship to 27.4.1 Write Guard

`check-write` routes to `scripts/agentos-write-guard.py`.

## Relationship to 27.5.1 Git Guard

- `check-commit` routes to git guard with `--action commit`
- `check-push` routes to git guard with `--action push`

## Relationship to 27.7.1 Audit Log

`audit` routes to `scripts/agentos-audit-log.py`.

## Relationship to 27.8.1 Human Gate

`human-gate` routes to `scripts/agentos-human-gate.py`.

## Relationship to 27.9.1 Violation Enforcement

`violation` routes to `scripts/agentos-violation-enforce.py`.

## Relationship to 27.10.1 Retry Enforcement

`retry` routes to `scripts/agentos-retry-enforce.py`.

## Supported Subcommands

- `audit`
- `check-command`
- `check-write`
- `check-commit`
- `check-push`
- `human-gate`
- `violation`
- `retry`
- `permission`

## Routing Table

- `audit` -> `agentos-audit-log.py`
- `check-command` -> `agentos-command-guard.py`
- `check-write` -> `agentos-write-guard.py`
- `check-commit` -> `agentos-git-guard.py check --action commit ...`
- `check-push` -> `agentos-git-guard.py check --action push ...`
- `human-gate` -> `agentos-human-gate.py`
- `violation` -> `agentos-violation-enforce.py`
- `retry` -> `agentos-retry-enforce.py`
- `permission` -> `agentos-permission-state.py`

## Result Mapping

Allow -> `ENFORCE_ALLOWED`:
- `COMMAND_ALLOWED`, `WRITE_ALLOWED`, `GIT_ALLOWED`, `HUMAN_GATE_APPROVED`, `RETRY_ALLOWED`, `PERMISSION_OK`, `AUDIT_OK`, `AUDIT_APPENDED`, `SANCTION_REQUIRED`, `SANCTION_APPLIED`

Blocked/policy -> `ENFORCE_BLOCKED` or `ENFORCE_POLICY_VIOLATION`:
- blocked/task/agent/retry blocked -> `ENFORCE_BLOCKED`
- policy violation results -> `ENFORCE_POLICY_VIOLATION`

Approval/review -> `ENFORCE_NEEDS_APPROVAL` / `ENFORCE_NEEDS_REVIEW`.
Invalid results -> `ENFORCE_INVALID`.
Unknown/malformed subsystem output -> `ENFORCE_SUBSYSTEM_ERROR`.
Missing subsystem script -> `ENFORCE_SUBSYSTEM_MISSING`.

## Exit Semantics

- `ENFORCE_ALLOWED` => exit 0
- all other `ENFORCE_*` => exit 1

## Evaluation Order

1. Parse top-level subcommand.
2. Validate supported subcommand.
3. Resolve subsystem script.
4. Fail closed if missing.
5. Forward args preserving intent.
6. Execute subsystem as subprocess.
7. Capture underlying `RESULT` and exit code.
8. Map to top-level `ENFORCE_*`.
9. Preserve reason context where available.
10. Return top-level result.

## Failure Behavior

- missing/unsupported subcommand => `ENFORCE_INVALID`
- missing subsystem => `ENFORCE_SUBSYSTEM_MISSING`
- timeout/crash => `ENFORCE_SUBSYSTEM_ERROR`
- unknown subsystem result => `ENFORCE_SUBSYSTEM_ERROR`
- inconsistent subsystem result/exit semantics => `ENFORCE_SUBSYSTEM_ERROR`

## check-write Forwarded Flags

`check-write` forwards at minimum:
- `--path`
- `--operation`
- `--path-class`

Supported `--path-class` values are inherited from 27.4.1.

## Non-Authorization Clauses

- `ENFORCE_ALLOWED` is not approval.
- It does not authorize commit/push/merge/release.
- It does not bypass M25.
- It does not override M26 corridor boundaries.
- It does not enable Level 2 platform enforcement.

## CLI Examples

```text
RESULT: ENFORCE_ALLOWED
REASON: mapped from COMMAND_ALLOWED; REASON: command passed guard checks
```

```text
RESULT: ENFORCE_POLICY_VIOLATION
REASON: mapped from GIT_POLICY_VIOLATION; REASON: direct push to dev is blocked
```

## Execution Boundary

This CLI does not execute risky actions itself.
This CLI does not replace underlying guards.
