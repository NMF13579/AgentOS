# M66 Unified Runner Architecture

## 1. Purpose

This document defines the architecture for M66 Unified Runner.

M66 is a read-only subprocess orchestrator for M63/M64/M65 checkers.
M66 executes known validators.
M66 captures stdout/stderr/exit codes.
M66 parses JSON outputs.
M66 enforces exit-code/result consistency.
M66 aggregates validation signals.
M66 returns one unified validation signal.

## 2. Scope

66.1 defines architecture only.

66.1 does not define the final input schema.
66.1 does not implement the runner.
66.1 does not create fixtures.
66.1 does not create integration summary.
66.1 does not create action review.
66.1 does not create evidence report.
66.1 does not complete M66.
66.1 does not start M67.

## 3. Prior-Layer Relationship

M63 validates task validation contract.
M64 validates agent output evidence.
M65 validates acceptance criteria satisfaction signals.
M66 orchestrates M63/M64/M65 checkers as one read-only validation pipeline.
M67 will handle false PASS resistance and completion gate hardening.

## 4. Selected Model: Execute Checkers

M66 uses execute-checkers model.

M66 explicitly rejects read-precomputed-results as the primary model.

If M66 only reads ready-made result files, it becomes an aggregator of claims.
If M66 executes checkers itself, it becomes a validation runner.

Precomputed result files may be used only as optional reference/evidence, not as primary authority.

## 5. High-Level Pipeline

unified runner input
↓
run M63 checker
↓
run M64 checker
↓
run M65 checker
↓
capture stdout/stderr/exit_code
↓
parse JSON outputs
↓
enforce exit-code/result consistency
↓
aggregate result
↓
emit one unified validation signal

## 6. Source Inputs

M66 input must point to source packages, not authoritative precomputed result files.

Required source input paths:
task_validation_package_path
agent_evidence_path
acceptance_criteria_package_path

task_validation_result_path must not be a required input for M66.

## 7. Checker Set

task_validation_contract_checker
agent_task_evidence_checker
acceptance_criteria_checker

Expected production script paths:
scripts/check-task-validation-contract.py
scripts/check-agent-task-evidence.py
scripts/check-acceptance-criteria.py

## 8. Checker Descriptor Concept

Each checker descriptor should include:
checker_id
script_path
input_arg
input_path_field
required

input_path_field is the name of a top-level field in the unified runner input package.
input_path_field is not the file path itself.
The runner must resolve the actual file path by reading package[input_path_field].

## 9. Subprocess Boundary

The runner may require a Python subprocess execution environment.
This does not permit shell=True.
The runner itself must use shell=False.

subprocess.run
shell=False
capture_output=True
text=True
timeout required
stdout captured
stderr captured
exit code captured

Forbidden execution patterns:
shell=True
os.system
arbitrary command strings from input
unbounded subprocess execution
network execution
repository mutation

## 10. Command Construction Boundary

Commands must be constructed only from validated structured fields.
Commands must not be assembled from arbitrary user-controlled command strings.
Only allowlisted checker IDs, script paths, input args, and resolved input paths may be used.

python3 <script_path> <input_arg> <resolved_input_path> --json

Optional:
--strict

## 11. Timeout Policy

default timeout_seconds: 30
allowed range: 1–300
invalid timeout blocks
checker timeout blocks

Full timeout semantics will be defined in 66.3 and implemented in 66.5.

## 12. Child Output Capture

checker_id
script_path
input_arg
input_path_field
resolved_input_path
executed
exit_code
stdout
stderr
parsed_json
result
exit_code_consistent_with_result
stdout_json_valid
duration_ms, if practical

## 13. Exit-Code / Result Consistency

M66 must verify that child checker exit_code matches parsed JSON result.

PASS-family result must exit 0.
Fail-closed result must exit 1.
CLI/internal error must exit 2.

exit 0 + result BLOCKED → M66_UNIFIED_RUN_BLOCKED
exit 1 + result PASS → M66_UNIFIED_RUN_BLOCKED
exit 2 + any result → M66_UNIFIED_RUN_BLOCKED
exit 0 + invalid JSON → M66_UNIFIED_RUN_BLOCKED

## 14. Checker-Specific Result Sets

M63 task validation contract checker:
- PASS
- PASS_WITH_WARNINGS
- BLOCKED

M63 has no NOT_ENOUGH_EVIDENCE unless explicitly added by M63 contract.

M64 agent evidence checker:
- PASS
- PASS_WITH_WARNINGS
- BLOCKED
- NOT_ENOUGH_EVIDENCE

M65 acceptance criteria checker:
- PASS
- PASS_WITH_WARNINGS
- BLOCKED
- NOT_ENOUGH_EVIDENCE

Unknown child checker result must block.

## 15. Unified Result Values

M66_UNIFIED_RUN_PASS
M66_UNIFIED_RUN_PASS_WITH_WARNINGS
M66_UNIFIED_RUN_BLOCKED
M66_UNIFIED_RUN_NOT_ENOUGH_EVIDENCE

Priority order:
1. M66_UNIFIED_RUN_BLOCKED
2. M66_UNIFIED_RUN_NOT_ENOUGH_EVIDENCE
3. M66_UNIFIED_RUN_PASS_WITH_WARNINGS
4. M66_UNIFIED_RUN_PASS

Detailed aggregation semantics belong to 66.3.

## 16. execution_mode and --no-execute

runner_options.execution_mode values:
execute
no_execute

CLI flag:
--no-execute

CLI --no-execute forces effective_execution_mode to no_execute.
If package runner_options.execution_mode is no_execute and CLI --no-execute is absent, runner must still use no_execute behavior.
If package runner_options.execution_mode is execute and CLI --no-execute is present, CLI wins and effective_execution_mode becomes no_execute.
Effective execution_mode must be reported in JSON output.

No execution means no validation proof.
No validation proof means no PASS.

## 17. no_execute Result Boundary

effective_execution_mode: no_execute
means child checkers are not executed.

M66_UNIFIED_RUN_PASS is forbidden.
M66_UNIFIED_RUN_PASS_WITH_WARNINGS is forbidden.

Allowed no_execute outcomes:
M66_UNIFIED_RUN_NOT_ENOUGH_EVIDENCE
M66_UNIFIED_RUN_BLOCKED

## 18. runner_options.json Boundary

runner_options.json is advisory only.

The runner's machine-readable output mode is controlled by CLI --json.
runner_options.json must not override CLI output mode.
If runner_options.json is false but CLI --json is provided, runner should emit JSON and record warning RUNNER_OPTIONS_JSON_FALSE_IGNORED.
If CLI --json is missing, treat as CLI misuse and exit 2.

## 19. Fixture Strategy

structure/
mock-execution/
execution/

structure fixtures validate package shape, boundary, and no_execute behavior.
mock-execution fixtures validate runner subprocess mechanics and aggregation using controlled fake checkers.
execution fixtures validate the real M63/M64/M65 checker pipeline.

mock-execution fixtures may validate runner orchestration mechanics.
mock-execution fixtures do not replace real execution fixtures.
real execution fixtures remain required for M66 completion.
Only real execution validation can support M66_UNIFIED_RUN_PASS.
No-execute and mock-only validation cannot prove full task validation.

## 20. Mock Checker Boundary

Mock checkers are allowed only in mock-execution fixture mode.
Production runner inputs must not execute mock checkers.
Mock checkers must use a separate test allowlist.
Mock checker paths must be rejected outside mock-execution fixture mode.

Allowed mock path prefix:
tests/fixtures/m66-unified-runner/mock-execution/mock-checkers/

Mock-execution validates runner mechanics, not full M63/M64/M65 validation.

## 21. Runtime Environment Boundary

Python subprocess execution environment

If runtime execution is unavailable in integration/evidence/completion tasks, those tasks must block rather than infer results.
Unavailable runtime execution environment is not a plan bug.
It means executable validation evidence is unavailable.

## 22. Non-Authority Boundary

M66 result is a validation signal.
M66 result is not approval.
M66 result does not complete the task.
M66 result does not authorize merge, push, release, or production deployment.
M66 result does not create completion gate.
M66 result does not start M67.
Human review remains required.

## 23. Relationship to M67

M67 will handle false PASS resistance and completion gate hardening.
M66 must not create false PASS resistance suite.
M66 must not create completion gate.
M66 must not start M67 automatically.
ready_for_m67 later means roadmap readiness only.

## 24. Failure Modes

runner becomes result-reader instead of checker executor
runner trusts precomputed result files as authority
runner executes arbitrary commands
runner uses shell=True
runner lacks timeout
runner allows mock checkers in production
runner allows no_execute to PASS
runner ignores exit-code/result mismatch
runner treats unknown child result as warning
runner treats runtime unavailable as PASS
runner starts absorbing M67 completion gate scope

## 25. Later Task Responsibilities

66.2 defines input contract and schema.
66.3 defines aggregation semantics.
66.4 defines claim boundary.
66.5 implements runner.
66.6 creates fixtures.
66.7 validates integration.
66.8 reviews actions.
66.9 collects evidence.
66.10 closes M66.

## 26. Final Status

FINAL_STATUS: M66_UNIFIED_RUNNER_ARCHITECTURE_DEFINED_WITH_WARNINGS
