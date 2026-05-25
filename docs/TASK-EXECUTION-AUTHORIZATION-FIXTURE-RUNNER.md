---
type: fixture-runner-documentation
milestone: M57
task: 57.8
title: Execution Authorization Fixture Runner
status: draft
script: scripts/check-m57-execution-authorization-fixtures.py
source_cli: scripts/check-execution-authorization.py
source_positive_fixtures: tests/fixtures/execution-authorization/positive/
source_negative_fixtures: tests/fixtures/execution-authorization/negative/
authority: fixture-runner-documentation-only
execution_authorized: false
execution_started: false
approval_created: false
lifecycle_mutation_authorized: false
m58_authorized: false
m58_started: false
---

# 1. Purpose

This document describes the M57 execution authorization fixture runner.
The fixture runner is a test harness only.
The fixture runner is not execution authorization.
The fixture runner does not authorize execution.
The fixture runner does not start execution.
The fixture runner does not start M58.
The fixture runner does not create approval records.
The fixture runner does not authorize lifecycle mutation.
The fixture runner does not modify tasks/active-task.md.
The fixture runner is not approval.
The fixture runner is not evidence approval.
The fixture runner is not completion review.
Exit code 0 is not execution.
Exit code 0 does not start M58.
M58 planning may be considered only after M57 completion review.

# 2. Runner Summary

The runner executes the M57 CLI against positive and negative fixtures.

# 3. Invocation

```bash
python3 scripts/check-m57-execution-authorization-fixtures.py --explain
python3 scripts/check-m57-execution-authorization-fixtures.py --json
python3 scripts/check-m57-execution-authorization-fixtures.py --strict --json
python3 scripts/check-m57-execution-authorization-fixtures.py --positive --json
python3 scripts/check-m57-execution-authorization-fixtures.py --negative --json
```

# 4. Arguments

- `--fixtures-root PATH`: path to fixtures.
- `--positive`: run positive fixtures.
- `--negative`: run negative fixtures.
- `--json`: output JSON.
- `--strict`: stop at first failure.
- `--explain`: print explain output and exit.

# 5. Fixture Sets

Positive and negative fixture sets.

# 6. Case Manifest Contract

The runner loads `case-manifest.json` from each fixture set.

# 7. JSON Output Mode

Provides full JSON payload.

# 8. Human Output Mode

Provides human readable text.

# 9. Explain Mode

Prints explanatory text.

# 10. Strict Mode

In strict mode, the cases array must contain only the executed cases up to and including the first CASE_FAIL or CASE_BLOCKED.

# 11. Timeout Handling

Every CLI invocation must use timeout=30.
subprocess.TimeoutExpired must produce CASE_BLOCKED.
One or more timed out cases must produce M57_FIXTURE_RUNNER_BLOCKED and exit 2.

# 12. Path Safety

The fixture runner must reject any case path that resolves outside the fixture root.
The fixture runner must reject paths that point to tasks/, approvals/, or generated/.
The fixture runner must reject absolute case paths.

# 13. Forbidden Path Rejection

Protected directories are forbidden.

# 14. Result Statuses

M57_FIXTURE_RUNNER_PASS
M57_FIXTURE_RUNNER_FAIL
M57_FIXTURE_RUNNER_BLOCKED

# 15. Exit Codes

M57_FIXTURE_RUNNER_PASS -> 0
M57_FIXTURE_RUNNER_FAIL -> 1
M57_FIXTURE_RUNNER_BLOCKED -> 2

# 16. Case Results

CASE_PASS
CASE_FAIL
CASE_BLOCKED

# 17. Non-Authority Boundary

M57 fixture runner result is not execution authorization.
M57 fixture runner result does not authorize execution.
M57 fixture runner result does not start execution.
M57 fixture runner result does not create approval records.
M57 fixture runner result does not authorize lifecycle mutation.
M57 fixture runner result does not authorize M58.
M57 fixture runner result does not start M58.
M57 fixture runner result does not modify tasks/active-task.md.

# 18. No Side Effects

The fixture runner must not write files.
The fixture runner must not use shell=True.
The fixture runner must not use network access.
The fixture runner must not execute active tasks.
The fixture runner must not create M58 artifacts.

# 19. Relationship to M57 CLI

The runner wraps the CLI to verify determinism.

# 20. Relationship to M58

M58 is controlled execution session.

# 21. Examples

See invocation block.

# 22. Summary

End of doc.

## Final Status

FINAL_STATUS: M57_FIXTURE_RUNNER_DEFINED
may_proceed_to_57_9: true
