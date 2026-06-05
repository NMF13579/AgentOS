---
type: contract
module: m73-dispatcher-io
status: draft
authority: supporting
created: 2026-05-30
source_of_truth: markdown
derived: false
---
This document is a Markdown contract artifact for M73 planning and implementation.
It is not approval.
It is not completion review.
It does not implement dispatcher behavior.
It does not update M72 registries.
It does not automatically become a protected artifact.
It does not automatically become a canonical artifact.
If future governance requires protection/canonical registration, that must be handled by a separate explicit task with M72 protected-change rules.

# Dispatcher IO / Exit-Code Contract

## Purpose
This document defines the input/output boundaries, exit codes, result tokens, failure mapping, and warning visibility rules for the validation dispatcher.

## Scope of This Contract
This contract governs dispatcher output results, exit codes, JSON envelopes, and warning visibility. It does not implement dispatcher logic or select the dispatcher script.

## Dispatcher Result Tokens
The allowed dispatcher results are:
- `DISPATCHER_PASS`
- `DISPATCHER_PASS_WITH_WARNINGS`
- `DISPATCHER_BLOCKED`
- `DISPATCHER_NOT_RUN`
- `DISPATCHER_UNKNOWN`
- `DISPATCHER_ERROR`

Dispatcher result is not approval.
Dispatcher result is not task completion.
Dispatcher result is not lifecycle mutation.
Dispatcher result is not protected write authorization.
No other dispatcher result token is allowed unless added by a future explicit contract update.
Unknown child result tokens must fail closed.
Unknown dispatcher result tokens must fail closed.

## Exit Code Semantics
The validation dispatcher exit codes must conform to:
- `exit 0` = validation completed without blockers
- `exit 1` = validation completed with blockers / fail-closed condition
- `exit 2` = CLI misuse / internal dispatcher error

Exit code is not approval.
Exit code is not task completion.
Exit code is not lifecycle mutation.
Exit code is not human review.

## Required Result / Exit-Code Matrix
The dispatcher result maps strictly to exit codes as follows:
DISPATCHER_PASS -> exit 0
DISPATCHER_PASS_WITH_WARNINGS -> exit 0
DISPATCHER_BLOCKED -> exit 1
DISPATCHER_NOT_RUN -> exit 1
DISPATCHER_UNKNOWN -> exit 1
DISPATCHER_ERROR -> exit 2

DISPATCHER_NOT_RUN must never use exit 0.
DISPATCHER_UNKNOWN must never use exit 0.
DISPATCHER_ERROR must never be reported as PASS.
DISPATCHER_PASS_WITH_WARNINGS is not clean PASS.

## Required Failure Mapping
The dispatcher must map failure conditions as follows:
Malformed child output -> DISPATCHER_BLOCKED / exit 1
Missing child validator -> DISPATCHER_BLOCKED / exit 1
Child exit/result mismatch -> DISPATCHER_BLOCKED / exit 1
Unsupported runtime validator state -> DISPATCHER_BLOCKED / exit 1
CLI misuse -> DISPATCHER_ERROR / exit 2
Internal dispatcher exception -> DISPATCHER_ERROR / exit 2
Unsupported command syntax -> DISPATCHER_ERROR / exit 2

Fail-closed conditions must not be converted into DISPATCHER_PASS.
Fail-closed conditions must not be hidden by aggregation.

## Child Validator Output Contract
Child validators may expose:
* stdout
* stderr
* exit code
* machine-readable output when available
* documented result token when available
* warnings
* blockers
* unknowns
* not-run signals

The dispatcher must preserve child validator evidence.
The dispatcher must not invent missing child validator evidence.
The dispatcher must not treat absent child evidence as clean PASS.

## Child Exit / Result Consistency
Child exit/result mismatch must fail closed.

Examples:
- child result PASS with non-zero blocker exit -> fail closed
- child result BLOCKED with exit 0 -> fail closed
- child result UNKNOWN with exit 0 -> fail closed
- child result NOT_RUN with exit 0 -> fail closed
- child missing result with success exit -> fail closed unless child contract explicitly allows no-result success

If a child validator has no declared machine-readable output contract, the dispatcher must not infer clean PASS from prose alone.

## Malformed Output Handling
Malformed child output must fail closed.
Malformed output includes:
* invalid JSON when JSON is expected
* missing required result field
* unknown result token
* contradictory result fields
* impossible result / exit-code combination
* truncated machine output
* unparseable wrapped output

Malformed output must map to:
DISPATCHER_BLOCKED / exit 1
unless the dispatcher itself crashes or misuses CLI parsing, in which case:
DISPATCHER_ERROR / exit 2

## Missing Child Validator Handling
Missing child validator must fail closed.
Missing child validator includes:
* referenced script does not exist
* referenced script is not executable when execution is required
* referenced command cannot be resolved
* referenced validator is not in the known allowlist
* validator path is ambiguous
* validator contract is missing when required

Missing child validator must map to:
DISPATCHER_BLOCKED / exit 1

## NOT_RUN Handling
NOT_RUN is not PASS.
DISPATCHER_NOT_RUN must never use exit 0.
NOT_RUN must be carried forward as not-run evidence.
NOT_RUN must not be converted into PASS.
NOT_RUN must not be converted into PASS_WITH_WARNINGS.
If a required child validator is not run, dispatcher must report:
DISPATCHER_BLOCKED / exit 1
or:
DISPATCHER_NOT_RUN / exit 1
depending on the documented reason.

## UNKNOWN Handling
UNKNOWN is not OK.
DISPATCHER_UNKNOWN must never use exit 0.
UNKNOWN must be carried forward as uncertainty.
UNKNOWN must not be converted into PASS.
UNKNOWN must not be converted into PASS_WITH_WARNINGS.
If a required child validator returns unknown and no contract permits advisory unknown, dispatcher must report:
DISPATCHER_BLOCKED / exit 1
or:
DISPATCHER_UNKNOWN / exit 1
depending on the documented reason.

## PASS_WITH_WARNINGS Handling
DISPATCHER_PASS_WITH_WARNINGS is not clean PASS.
Warnings must be preserved.
Warnings must not be hidden.
Warnings must not become approval.
Warnings must not become task completion.
If downstream logic requires clean PASS, DISPATCHER_PASS_WITH_WARNINGS must not satisfy that clean PASS requirement unless explicitly allowed by the downstream contract.

If DISPATCHER_PASS_WITH_WARNINGS maps to exit 0, warnings must be visible in stdout and/or persisted evidence artifacts, not only in JSON output.

## Warning Visibility Boundary
Warnings are user-facing review signals.
Warnings must remain visible even when the dispatcher exit code is 0.
If DISPATCHER_PASS_WITH_WARNINGS maps to exit 0, the dispatcher must ensure that warnings are visible in at least one human-reviewable channel:
* stdout
* persisted evidence report
* CI artifact
* dispatcher summary artifact

Warnings must not be stored only in JSON if that JSON is not surfaced to the human reviewer.
Warnings must not be hidden behind CI green status.
Warnings must not be collapsed into clean PASS.

pass_with_warnings_exit_0_requires_visible_warning_evidence: true

## Dispatcher Output Envelope
The recommended dispatcher machine-readable envelope format includes:
- `dispatcher_result`
- `dispatcher_exit_code`
- `command`
- `execution_mode`
- `child_results`
- `warnings`
- `blockers`
- `unknowns`
- `not_run`
- `evidence`
- `approval_created`
- `lifecycle_mutation_occurred`

Value rules:
- `approval_created` must be false.
- `lifecycle_mutation_occurred` must be false.
The envelope is a recommended contract for future implementation. M73.4 does not implement it.

## JSON Output Boundary
JSON output is machine-readable evidence only.
JSON output is not source of truth.
JSON output is not approval.
JSON output is not lifecycle mutation.
If JSON output conflicts with Markdown/YAML contract, the contract wins.
If JSON output is malformed, the dispatcher must fail closed.
JSON must not become a new authority layer.
Warnings must not be visible only in JSON output when DISPATCHER_PASS_WITH_WARNINGS maps to exit 0.

## Stdout / Stderr Boundary
stdout and stderr are execution evidence.
stdout and stderr are not approval.
The dispatcher must capture stdout and stderr when invoking child validators.
The dispatcher must not hide stderr if a child validator fails.
The dispatcher must not convert clean-looking stdout into PASS when exit/result evidence is blocked, unknown, malformed, or missing.
If dispatcher result is DISPATCHER_PASS_WITH_WARNINGS, stdout and/or persisted evidence artifacts must make warning status visible to the human reviewer.

## CI Interpretation Boundary
CI PASS ≠ approval.
CI PASS ≠ task completion.
CI job success only means the configured command completed according to its configured semantics.
CI may interpret exit codes for job success/failure, but CI must not claim human approval.
CI must not claim platform enforcement unless verified by external platform evidence.
CI must not claim branch protection unless verified by external platform evidence.
Exit 2 must be interpreted explicitly by CI in M74 regression coverage.
If DISPATCHER_PASS_WITH_WARNINGS maps to exit 0, CI must still surface warnings through stdout and/or persisted evidence artifacts.
CI green must not hide dispatcher warnings.

## Evidence Boundary
Dispatcher output is evidence.
Evidence ≠ approval.
Dispatcher evidence may support review, but it does not approve work and does not complete tasks.
If evidence is incomplete, malformed, or missing, the dispatcher must not claim clean PASS.
Warning evidence must be preserved when dispatcher result is DISPATCHER_PASS_WITH_WARNINGS.

## Human Approval Boundary
Human approval cannot be simulated by dispatcher IO, exit codes, JSON output, stdout, stderr, CI, scripts, reports, wrappers, or agent-written claims.
The dispatcher IO contract must never claim:
* human approval
* human checkpoint completion
* protected write authorization
* task acceptance
* milestone completion

## Protected / Canonical Governance Boundary
M72 protected/canonical governance remains binding.
This contract does not authorize protected/canonical writes.
Dispatcher IO does not authorize protected/canonical writes.
UNKNOWN protected/canonical status blocks writes.
Readiness does not authorize writes.
Evidence does not authorize writes.
PASS does not authorize writes.
Any future dispatcher implementation that modifies protected/canonical artifacts requires explicit human checkpoint evidence before the write when M72 policy requires it.

## Relationship to M73.5
M73.4 defines dispatcher IO and exit-code semantics.
M73.5 creates the existing entrypoint alignment plan.
M73.4 does not align entrypoints.
M73.4 does not modify scripts, wrappers, docs references, or CI workflows.

## Relationship to M73.9
M73.9 may smoke-check dispatcher behavior against this IO contract.
M73.4 does not run smoke checks.
M73.4 does not create smoke reports.

## Relationship to M74
M73.4 does not create regression fixtures.
M73.4 does not start M74.
M74 owns dispatcher regression fixtures.

exit_2_semantics_requires_m74_regression_fixture: true
pass_with_warnings_exit_0_requires_visible_warning_evidence: true

M74 must add regression fixtures for:
* CLI misuse → exit 2
* internal dispatcher error → exit 2
* unsupported command syntax → exit 2
* runtime unsupported validator state → BLOCKED / exit 1
* CI interpretation of exit 2
* DISPATCHER_NOT_RUN never using exit 0
* DISPATCHER_UNKNOWN never using exit 0
* malformed child output blocking
* missing child validator blocking
* child exit/result mismatch blocking
* DISPATCHER_PASS_WITH_WARNINGS with exit 0 exposing warnings in stdout and/or persisted evidence artifacts

## Forbidden Claims
The document explicitly forbids these claims:
- Dispatcher PASS means approval.
- Dispatcher PASS means task completion.
- Dispatcher PASS means protected write authorization.
- Dispatcher exit 0 means approval.
- Dispatcher exit 0 means task completion.
- Dispatcher JSON is source of truth.
- Dispatcher stdout is approval.
- Dispatcher stderr can be hidden on failure.
- DISPATCHER_NOT_RUN can use exit 0.
- DISPATCHER_UNKNOWN can use exit 0.
- DISPATCHER_PASS_WITH_WARNINGS is clean PASS.
- DISPATCHER_PASS_WITH_WARNINGS warnings can be hidden because exit code is 0.
- Malformed child output can be ignored.
- Missing child validator can be ignored.
- Child exit/result mismatch can be ignored.
- CI PASS means approval.
- M73.4 starts M74.

## Final Boundary Statement
The Dispatcher IO / Exit-Code Contract defines dispatcher IO boundaries only.
It does not approve work.
It does not complete tasks.
It does not mutate lifecycle.
It does not authorize protected/canonical writes.
It does not implement dispatcher behavior.
It does not align entrypoints.
It does not run smoke checks.
It does not create regression fixtures.
It does not start M73.5.
It does not start M74.
