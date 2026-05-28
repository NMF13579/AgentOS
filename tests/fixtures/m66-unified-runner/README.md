# M66 Unified Runner Fixtures

## 1. Purpose
This fixture suite validates the M66 Unified Runner.
M66 is a read-only subprocess orchestrator for M63/M64/M65 checkers. M66 executes known validators, captures stdout/stderr/exit codes, parses JSON outputs, enforces exit-code/result consistency, aggregates validation signals, and returns one unified validation signal.

Important limitations:
- M66 fixtures are not approval.
- M66 fixtures do not complete tasks.
- Human review remains required.

## 2. Fixture Layers
The suite is divided into three layers:
- `structure/`: Validates input package shape, `no_execute` behavior, boundary fields, and production schema constraints.
- `mock-execution/`: Validates runner mechanics through controlled mock checkers.
- `execution/`: Validates the actual M63/M64/M65 checker pipeline through real subprocess execution.

## 3. Structure Fixtures
Structure fixtures validate input package shape, `no_execute` behavior, boundary fields, and production schema constraints. Even valid structure cannot PASS without execution.

## 4. Mock-Execution Fixtures
Mock-execution fixtures validate runner orchestration mechanics only.
- mock-execution fixtures do not replace real execution fixtures.
- production runner inputs must not execute mock checkers.
- mock checker paths are test-only.

## 5. Real Execution Fixtures
Real execution fixtures validate actual M63/M64/M65 checker pipeline.
- Real execution fixtures remain required for M66 completion.
- If real execution fixtures cannot run, later integration/evidence/completion must block rather than infer results.
- `M66_UNIFIED_RUNNER_BLOCKED` in an incomplete runtime environment is expected behavior, not a plan failure.

## 6. Mock Checker Boundary
Mock checkers have the following constraints:
- Mock checkers write no files.
- Mock checkers use no network.
- Mock checkers are deterministic.
- Mock checkers are test-only.

## 7. Expected Results Manifest
`expected-results.json` acts as the source of truth for the suite. It contains expected outcomes (`expected_result` and `expected_exit_code`) for all fixtures across all layers, as well as metadata about mock checkers.

## 8. no_execute Boundary
- No execution means no validation proof.
- No validation proof means no PASS.
Therefore, `no_execute` operations must inherently block or require additional evidence for approval.

## 9. Non-Authority Boundary
- M66 fixture PASS is not approval.
- M66 fixture PASS does not complete the task.
- M66 fixture PASS does not authorize merge, push, release, or deployment.
- M66 fixture PASS does not start M67.
- Human review remains required.

## 10. Final Status
FINAL_STATUS: M66_UNIFIED_RUNNER_FIXTURES_COMPLETE_WITH_WARNINGS
