# Script Exit-Code Standard

## Task Boundary

This file records the active task only.

It does not modify scripts.

It does not create validators.

It does not decide final validation authority.

It does not approve M69.

Human review remains required.

## Active Task Record

- `id: task-69.4`
- `milestone: M69`
- `name: "Script Output / Exit-Code Contract Audit"`
- `status: active`
- `mode: "EXECUTION / READ-ONLY SCRIPT CONTRACT AUDIT"`
- `branch: dev`
- `started_at: "2026-05-28"`

## Inputs Reviewed

- `docs/SCRIPT-LIFECYCLE-POLICY.md`
- `docs/SCRIPT-RESPONSIBILITY-MAP.md`
- `reports/m69-script-inventory-intake.md`
- `reports/m69-m68-completion-intake.md`
- `scripts/VALIDATORS.md`
- `.github/workflows/agentos-validate.yml`
- observed `scripts/` files with `sys.exit(...)`, explicit numeric exit codes, and JSON result output

## M69.3 Lifecycle Classification Status

M69.3 is complete with warnings.

The lifecycle policy exists, but it does not settle final validation authority.

## Observed Exit-Code Patterns

- Many scripts use `sys.exit(main())` or `sys.exit(main(sys.argv[1:]))`, which means the script result is carried by the function return value.
- Some scripts return only `0` or `1`, usually for success/failure or pass/fail.
- Some scripts use `2` for invalid input, CLI misuse, or unsafe evaluation.
- Some scripts use a wider numeric range, such as `3`, which creates inconsistency across the repo.
- A few scripts map result labels to exit codes through lookup tables, so the code is tied to a named result token rather than a plain boolean.
- `scripts/agentos-validate.py` writes JSON with an `exit_code` field and also uses an internal `_honest_exit()` mapping.

## Proposed Future Exit-Code Standard

Future M69/M71/M73 work should use one clear model:

- `exit 0` = successful execution with result not blocked
- `exit 1` = deterministic failure, blocked result, or validation failure
- `exit 2` = CLI misuse, invalid input, internal error, or unable to evaluate safely

This is a future standard only.

It does not claim current compliance.

## Exit 0 Semantics

Use `exit 0` only when the script finished normally and the result is not blocked.

`PASS` may map to `exit 0`.

`UNKNOWN` must not map to `PASS`.

`NOT_RUN` must not map to `PASS`.

`BLOCKED` must not map to `exit 0` unless a later human note explicitly marks it as advisory-only and still not PASS.

## Exit 1 Semantics

Use `exit 1` for deterministic failure, blocked result, validation failure, or any result that must visibly stop the flow.

Warnings must stay visible.

Warnings must not be silently downgraded to success.

## Exit 2 Semantics

Use `exit 2` for CLI misuse, invalid input, internal error, parse failure, or any case where the script cannot evaluate safely.

`exit 2` is not a success code.

## UNKNOWN / NOT_RUN Semantics

`UNKNOWN` means the script did not produce a trustworthy answer.

`NOT_RUN` means the script did not actually run the intended check.

Neither one is PASS.

Neither one should be treated as approval.

## Warning Semantics

Warnings must remain visible in both text and JSON output.

Warnings must not be hidden inside a success code without an explicit note.

Warnings may allow later human review, but they do not create approval.

## JSON Result / Exit-Code Consistency

Exit code and JSON result must agree.

If JSON says blocked or failed, the exit code must not say success.

If JSON says unknown, not-run, warning, or needs-review, the exit code must not imply approval.

If the two disagree, the script should be treated as inconsistent and require human review.

## Scripts Requiring Later Exit-Code Review

- `scripts/agentos-validate.py`
- `scripts/check-execution-result-verification.py`
- `scripts/check-execution-authorization.py`
- `scripts/check-scope-compliance.py`
- `scripts/check-single-role-execution.py`
- `scripts/check-template-cleanliness.py`
- `scripts/check-template-integrity.py`
- `scripts/check-risk.py`
- `scripts/check-pr-quality.py`
- `scripts/run-task-validation.py`
- `scripts/check-task-validation-contract.py`

## Explicit Non-Implementation Boundary

This script exit-code standard documents observed and proposed exit-code behavior only.

This script exit-code standard does not modify scripts.

This script exit-code standard does not create validators.

This script exit-code standard does not decide final validation authority.

This script exit-code standard does not approve M69.

Human review remains required.

## M69.5 Preparation Decision

may_prepare_m69_5: true_with_warnings

may_prepare_m69_5 is roadmap preparation only.

may_prepare_m69_5 does not start M69.5.

may_prepare_m69_5 is not approval.

## Final Status

FINAL_STATUS: M69_SCRIPT_EXIT_CODE_STANDARD_COMPLETE_WITH_WARNINGS
