---
type: cli-documentation
milestone: M57
task: 57.6
title: Execution Authorization CLI
status: draft
script: scripts/check-execution-authorization.py
source_policy: docs/TASK-EXECUTION-AUTHORIZATION-POLICY.md
source_output_contract: docs/TASK-EXECUTION-AUTHORIZATION-OUTPUT-CONTRACT.md
authority: cli-documentation-only
execution_authorized: false
execution_started: false
approval_created: false
lifecycle_mutation_authorized: false
m58_authorized: false
m58_started: false
---

# Execution Authorization CLI Documentation

## 1. Purpose

This document describes the M57 execution authorization CLI.

## 2. CLI Summary

The M57 execution authorization CLI is read-only.
The M57 execution authorization CLI does not authorize execution by side effect.
The M57 execution authorization CLI does not start execution.
The M57 execution authorization CLI does not start M58.
The M57 execution authorization CLI does not create approval records.
The M57 execution authorization CLI does not authorize lifecycle mutation.
The M57 execution authorization CLI does not modify tasks/active-task.md.
The M57 execution authorization CLI is not approval.
The M57 execution authorization CLI is not evidence approval.
The M57 execution authorization CLI is not completion review.
Exit code 0 is not execution.
Exit code 0 does not start M58.
Exit code 0 is not lifecycle mutation.
Exit code 0 is not approval.
M56 COMPLETE does not automatically authorize M58.
M58 planning may be considered only after M57 completion review.

## 3. Invocation

The CLI can be invoked using Python 3:
```bash
python3 scripts/check-execution-authorization.py --explain
python3 scripts/check-execution-authorization.py --input templates/task-execution-authorization-input.md --preconditions templates/task-execution-authorization-preconditions.md --m56-completion-review reports/m56-completion-review.md --json
python3 scripts/check-execution-authorization.py --input templates/task-execution-authorization-input.md --preconditions templates/task-execution-authorization-preconditions.md --m56-completion-review reports/m56-completion-review.md
```

## 4. Arguments

The CLI arguments are defined as:
* `--input PATH`
* `--preconditions PATH`
* `--m56-completion-review PATH`
* `--json`
* `--explain`

## 5. Explain Mode

Explain mode is triggered by passing `--explain`.
In explain mode, the CLI emits markers and does not require inputs.

## 6. JSON Output Mode

JSON output mode is triggered by passing `--json`.
The CLI output contains the required root object:
* `execution_authorization_result`

## 7. Human Output Mode

Without `--json`, the CLI outputs human-readable status, results, and boundary details.

## 8. Result Statuses

The CLI supports the following result statuses:
* `EXECUTION_AUTHORIZATION_CONFIRMED`
* `EXECUTION_AUTHORIZATION_CONFIRMED_WITH_LIMITATIONS`
* `EXECUTION_AUTHORIZATION_NOT_CONFIRMED`
* `EXECUTION_AUTHORIZATION_BLOCKED`

## 9. Exit Codes

The exit code mapping is:
* `EXECUTION_AUTHORIZATION_CONFIRMED -> 0`
* `EXECUTION_AUTHORIZATION_CONFIRMED_WITH_LIMITATIONS -> 0`
* `EXECUTION_AUTHORIZATION_NOT_CONFIRMED -> 1`
* `EXECUTION_AUTHORIZATION_BLOCKED -> 2`

## 10. Decision Priority

The decision priority is:
* `EXECUTION_AUTHORIZATION_BLOCKED > EXECUTION_AUTHORIZATION_NOT_CONFIRMED > EXECUTION_AUTHORIZATION_CONFIRMED_WITH_LIMITATIONS > EXECUTION_AUTHORIZATION_CONFIRMED`

## 11. Input Parsing

The CLI parses input JSON/Markdown. Fenced json blocks are supported.

## 12. M56 Completion Review Parsing

The CLI parses frontmatter variables from M56 completion reviews to verify statuses.

## 13. Fail-Closed Behavior

Any unknown status, malformed data, claim violations, or performed action violations will trigger a blocked decision.

## 14. Unsafe Authority Claims

The CLI scans input files and blocks unsafe authority claims:
* `execution is approved`
* `execution is authorized`
* `M58 is authorized`
* `M58 may start`
* `M58 started`
* `approval has been created`
* `lifecycle mutation has been authorized`
* `tasks/active-task.md was modified by M57`

## 15. Non-Authority Boundary

This document describes the M57 execution authorization CLI.

## 16. No Side Effects

The no-side-effects rules:
* `The CLI must not write files.`
* `The CLI must not run shell commands.`
* `The CLI must not use subprocess.`
* `The CLI must not use network access.`
* `The CLI must not execute active tasks.`
* `The CLI must not create M58 artifacts.`

## 17. Relationship to M56

The CLI checks the readiness results of M56 before running policy logic.

## 18. Relationship to M57 Policy

The CLI is a deterministic implementation of the policy document.

## 19. Relationship to M58

The CLI prevents planning controlled sessions in M58 when not authorized.

## 20. Examples

Refer to section 3 for invocation patterns.

## 21. Summary

The summary of boundaries and behavior:
* `M57 CLI result is not execution.`
* `M57 CLI result does not authorize execution by side effect.`
* `M57 CLI result does not start M58.`
* `M57 CLI result does not create approval records.`
* `M57 CLI result does not mutate lifecycle state.`
* `M57 CLI result does not modify tasks/active-task.md.`

## Final Status

FINAL_STATUS: M57_CLI_DEFINED
may_proceed_to_57_7: true

This means only that the CLI script and documentation exist and are valid.
It does not mean execution is authorized.
It does not mean M57 is complete.
It does not mean M58 may start.
