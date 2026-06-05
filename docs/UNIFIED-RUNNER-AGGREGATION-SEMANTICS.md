# M66 Unified Runner Aggregation Semantics

## 1. Purpose

This document defines how M66 aggregates child checker results.

M66 executes known M63/M64/M65 checkers.
M66 captures stdout/stderr/exit codes.
M66 parses JSON outputs.
M66 enforces exit-code/result consistency.
M66 aggregates validation signals.
M66 returns one unified validation signal.
M66 aggregation semantics is not approval.
Human review remains required.

## 2. Scope

66.3 defines:
- M66 result values
- priority order
- checker-specific allowed result sets
- child checker result mapping
- subprocess failure mapping
- exit-code/result consistency
- no_execute result boundary
- mock-execution limitations
- M66 exit codes

66.3 does not:
- implement runner
- create claim boundary
- create fixtures
- create integration summary
- create action review
- create evidence report
- create completion review
- create M67 artifacts
- integrate completion gate

## 3. Inputs to Aggregation

Aggregation consumes child checker execution records.

Each child checker execution record should contain:
- checker_id
- script_path
- input_arg
- input_path_field
- resolved_input_path
- executed
- exit_code
- stdout
- stderr
- stdout_json_valid
- parsed_json
- result
- exit_code_consistent_with_result
- duration_ms, if practical
- warnings
- blockers

## 4. M66 Result Values

Exactly these M66 result values are allowed:
- M66_UNIFIED_RUN_PASS
- M66_UNIFIED_RUN_PASS_WITH_WARNINGS
- M66_UNIFIED_RUN_BLOCKED
- M66_UNIFIED_RUN_NOT_ENOUGH_EVIDENCE

No other M66 result value is allowed.

## 5. Priority Order

Priority order:
1. M66_UNIFIED_RUN_BLOCKED
2. M66_UNIFIED_RUN_NOT_ENOUGH_EVIDENCE
3. M66_UNIFIED_RUN_PASS_WITH_WARNINGS
4. M66_UNIFIED_RUN_PASS

Higher-priority result always wins over lower-priority result.
BLOCKED dominates all other outcomes.
NOT_ENOUGH_EVIDENCE dominates PASS_WITH_WARNINGS and PASS.
PASS_WITH_WARNINGS dominates PASS.

## 6. Checker-Specific Allowed Result Sets

M63 task validation contract checker allowed result families:
- PASS
- PASS_WITH_WARNINGS
- BLOCKED

M63 exact tokens should be taken from the M63 contract/checker documentation. If current M63 implementation uses different exact tokens, M66 must document the accepted token set before implementation.

M63 has no NOT_ENOUGH_EVIDENCE unless explicitly added by M63 contract.

M64 agent evidence checker allowed result values:
- M64_EVIDENCE_CHECK_PASS
- M64_EVIDENCE_CHECK_PASS_WITH_WARNINGS
- M64_EVIDENCE_CHECK_BLOCKED
- M64_EVIDENCE_CHECK_NOT_ENOUGH_EVIDENCE

M65 acceptance criteria checker allowed result values:
- M65_ACCEPTANCE_CHECK_PASS
- M65_ACCEPTANCE_CHECK_PASS_WITH_WARNINGS
- M65_ACCEPTANCE_CHECK_BLOCKED
- M65_ACCEPTANCE_CHECK_NOT_ENOUGH_EVIDENCE

Unknown child checker result:
M66_UNIFIED_RUN_BLOCKED

## 7. Child Result Family Classification

PASS-family:
- PASS
- *_PASS

PASS_WITH_WARNINGS-family:
- PASS_WITH_WARNINGS
- *_PASS_WITH_WARNINGS

BLOCKED-family:
- BLOCKED
- *_BLOCKED

NOT_ENOUGH_EVIDENCE-family:
- NOT_ENOUGH_EVIDENCE
- *_NOT_ENOUGH_EVIDENCE

Family matching must not replace checker-specific allowed result validation.
First validate that result is allowed for the specific checker.
Then classify into family.

If result family is recognized but token is not allowed for that checker:
M66_UNIFIED_RUN_BLOCKED

## 8. Child Checker Result Mapping

Any required child checker BLOCKED-family result:
M66_UNIFIED_RUN_BLOCKED

Any required child checker NOT_ENOUGH_EVIDENCE-family result:
M66_UNIFIED_RUN_NOT_ENOUGH_EVIDENCE unless any checker blocks

Any required child checker PASS_WITH_WARNINGS-family result:
M66_UNIFIED_RUN_PASS_WITH_WARNINGS unless any checker blocks or not-enough exists

All required child checkers PASS-family:
M66_UNIFIED_RUN_PASS

If optional checkers are introduced later, their failures must not silently disappear.
Optional checker BLOCKED should produce at least PASS_WITH_WARNINGS unless policy says it blocks.
Optional checker unknown result must still block if executed and parsed.

## 9. Exit-Code / Result Consistency

M66 must verify that child checker exit_code matches parsed JSON result.

PASS-family result → child exit 0
PASS_WITH_WARNINGS-family result → child exit 0
BLOCKED-family result → child exit 1
NOT_ENOUGH_EVIDENCE-family result → child exit 1
CLI/internal checker error → child exit 2

If child checker exit_code and parsed result disagree:
M66_UNIFIED_RUN_BLOCKED

Examples:
exit 0 + result BLOCKED → M66_UNIFIED_RUN_BLOCKED
exit 1 + result PASS → M66_UNIFIED_RUN_BLOCKED
exit 2 + any result → M66_UNIFIED_RUN_BLOCKED
exit 0 + invalid JSON → M66_UNIFIED_RUN_BLOCKED
exit 1 + invalid JSON → M66_UNIFIED_RUN_BLOCKED

This consistency check is deterministic, not optional.

## 10. Child Checker JSON Output Requirements

Child checker stdout must be valid JSON.
Child checker JSON must include a result field.
The result field must be a string.
The result value must be allowed for that checker.
Unknown result values block.
Missing result field blocks.
Non-string result field blocks.
Invalid JSON blocks.

## 11. Subprocess Failure Mapping

- missing checker script → M66_UNIFIED_RUN_BLOCKED
- checker FileNotFoundError → M66_UNIFIED_RUN_BLOCKED
- checker timeout → M66_UNIFIED_RUN_BLOCKED
- checker exits 2 → M66_UNIFIED_RUN_BLOCKED
- checker exits 0 but stdout invalid JSON → M66_UNIFIED_RUN_BLOCKED
- checker exits 1 but stdout invalid JSON → M66_UNIFIED_RUN_BLOCKED
- checker output has missing result field → M66_UNIFIED_RUN_BLOCKED
- checker result value unknown → M66_UNIFIED_RUN_BLOCKED
- checker exit code / result mismatch → M66_UNIFIED_RUN_BLOCKED
- checker creates/modifies files if detected → M66_UNIFIED_RUN_BLOCKED

## 12. Python Subprocess Execution Environment

M66 may require a Python subprocess execution environment.
This does not permit shell=True.
The runner itself must use shell=False.

If runtime execution is unavailable in integration/evidence/completion tasks:
- do not infer results
- do not infer exit codes
- block the relevant report
- record runtime_execution_available: false

## 13. no_execute Semantics

effective_execution_mode: no_execute means child checkers are not executed.

Sources of no_execute:
- CLI --no-execute
- package runner_options.execution_mode: no_execute

CLI --no-execute takes precedence and forces no_execute.

No execution means no validation proof.
No validation proof means no PASS.

## 14. no_execute Result Boundary

When effective_execution_mode is no_execute:

Forbidden results:
M66_UNIFIED_RUN_PASS is forbidden.
M66_UNIFIED_RUN_PASS_WITH_WARNINGS is forbidden.

Allowed results:
- M66_UNIFIED_RUN_NOT_ENOUGH_EVIDENCE
- M66_UNIFIED_RUN_BLOCKED

Mapping:
valid structure + no execution → M66_UNIFIED_RUN_NOT_ENOUGH_EVIDENCE
invalid structure + no execution → M66_UNIFIED_RUN_BLOCKED

Exit codes:
M66_UNIFIED_RUN_NOT_ENOUGH_EVIDENCE → exit 1
M66_UNIFIED_RUN_BLOCKED → exit 1

## 15. runner_options.json Advisory Boundary

runner_options.json is advisory only.
CLI --json controls machine-readable output.
runner_options.json false with CLI --json produces warning RUNNER_OPTIONS_JSON_FALSE_IGNORED, not block.
Missing CLI --json is CLI misuse and exits 2.
runner_options.json must not override CLI output mode.

## 16. Mock-Execution Semantics

mock-execution fixtures validate runner mechanics.
mock-execution fixtures may use mock checkers only through explicit test allowlist or fixture mechanism.
mock-execution fixtures do not replace real execution fixtures.
mock-only validation cannot support M66 completion.
Production runner inputs must not execute mock checkers.

No mock-execution mechanism may weaken production runner input validation.

## 17. Real Execution Requirement

Real execution fixtures validate the actual M63/M64/M65 checker pipeline.
Real execution fixtures remain required for M66 completion.
If real execution fixtures cannot run, later integration/evidence/completion must block rather than infer results.

M66_UNIFIED_RUNNER_BLOCKED in an incomplete runtime environment is expected behavior, not a plan failure.

## 18. Warning Aggregation

Warnings may come from:
- child PASS_WITH_WARNINGS result
- runner_options.json false ignored warning
- optional checker warning, if optional checkers exist later
- carried prior milestone warnings
- non-blocking runtime warnings

Warnings must not suppress blockers.
Warnings must not turn NOT_ENOUGH_EVIDENCE into PASS.
Warnings must not authorize approval or completion.

## 19. Blocker Aggregation

Blockers include at least:
- required child checker blocked
- missing required checker
- checker timeout
- invalid child JSON
- unknown child result
- exit-code/result mismatch
- no_execute attempting PASS
- mock checker used in production input
- human_review_required false
- forbidden operational field
- completion gate claim
- M67 auto-start claim
- repository mutation by runner if detected
- runtime execution unavailable when execution evidence is required

## 20. M66 Exit Codes

exit 0 — M66_UNIFIED_RUN_PASS
exit 0 — M66_UNIFIED_RUN_PASS_WITH_WARNINGS
exit 1 — M66_UNIFIED_RUN_BLOCKED
exit 1 — M66_UNIFIED_RUN_NOT_ENOUGH_EVIDENCE
exit 2 — CLI misuse / internal runner error

M66_UNIFIED_RUN_NOT_ENOUGH_EVIDENCE maps to exit 1 because validation is inconclusive and must not allow pipeline continuation as if validation passed.

## 21. Non-Authority Boundary

M66 aggregation result is a validation signal.
M66 aggregation result is not approval.
M66 aggregation result does not complete the task.
M66 aggregation result does not authorize merge, push, release, or production deployment.
M66 aggregation result does not create completion gate.
M66 aggregation result does not start M67.
Human review remains required.

## 22. Relationship to Later Tasks

66.4 defines claim boundary.
66.5 implements runner.
66.6 creates fixtures.
66.7 validates integration.
66.8 reviews actions.
66.9 collects evidence.
66.10 closes M66.

## 23. Final Status

FINAL_STATUS: M66_UNIFIED_RUNNER_AGGREGATION_SEMANTICS_DEFINED_WITH_WARNINGS
