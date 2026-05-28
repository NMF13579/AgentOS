# M66 Unified Runner Input Contract

## 1. Purpose

This document defines the production input package contract for M66 Unified Runner.

M66 is a read-only subprocess orchestrator for M63/M64/M65 checkers.
M66 input contract defines what the runner may consume in production mode.
M66 input contract does not implement the runner.
M66 input contract does not approve or complete tasks.
Human review remains required.

## 2. Scope

66.2 defines:
- production input package fields
- checker descriptors
- source package paths
- runner options
- no_execute input behavior
- human review boundary
- non-authority boundary
- production checker allowlist
- mock checker boundary
- unresolved mock-execution validation path for 66.5/66.6

66.2 does not:
- implement runner
- define final aggregation semantics
- define final claim boundary
- create fixtures
- create integration/action/evidence/completion reports
- start M67

## 3. Source Package Model

M66 input points to source packages.
M66 does not rely on precomputed result files as primary authority.
M66 executes checkers to obtain results.
task_validation_result_path is not a required field.

## 4. Top-Level Fields

- contract_version
- package_type
- task_id
- task_brief_path
- task_validation_package_path
- agent_evidence_path
- acceptance_criteria_package_path
- expected_checkers
- runner_options
- human_review_required
- non_authority_boundary

## 5. Checker Descriptors

Each expected checker descriptor contains:
- checker_id
- script_path
- input_arg
- input_path_field
- required

Allowed checker IDs: task_validation_contract_checker, agent_task_evidence_checker, acceptance_criteria_checker
Allowed script paths: scripts/check-task-validation-contract.py, scripts/check-agent-task-evidence.py, scripts/check-acceptance-criteria.py
Allowed input args: --package, --evidence

## 6. Required Checker Mapping

task_validation_contract_checker → scripts/check-task-validation-contract.py → --package → task_validation_package_path
agent_task_evidence_checker → scripts/check-agent-task-evidence.py → --evidence → agent_evidence_path
acceptance_criteria_checker → scripts/check-acceptance-criteria.py → --package → acceptance_criteria_package_path

Any mismatch must block future runner execution.

## 7. input_path_field Semantics

input_path_field is the name of a top-level field in the unified runner input package.
input_path_field is not the file path itself.
The runner must resolve the actual file path by reading package[input_path_field].

For example,
input_path_field: agent_evidence_path
means:
package["agent_evidence_path"]
not literal path:
input_path_field

## 8. Production Checker Allowlist

scripts/check-task-validation-contract.py
scripts/check-agent-task-evidence.py
scripts/check-acceptance-criteria.py

Production runner inputs must not execute arbitrary scripts.
Production runner inputs must not execute mock checkers.
Production runner inputs must not execute paths outside the production checker allowlist.

## 9. Mock Checker Boundary

Mock checkers are allowed only in mock-execution fixture mode.
Mock checkers must use a separate test allowlist.
Mock checker paths must be rejected outside mock-execution fixture mode.
Production runner inputs must not execute mock checkers.
Mock-execution fixtures validate runner mechanics, not full M63/M64/M65 validation.
Mock-execution fixtures do not replace real execution fixtures.

Allowed future mock path prefix:
tests/fixtures/m66-unified-runner/mock-execution/mock-checkers/

## 10. Mock-Execution Validation Path

The production schema intentionally rejects mock checker paths.
Therefore, mock-execution fixtures in 66.6 must use an explicit test-only validation path.

Allowed future approaches:
1. separate mock fixture schema;
2. runner test mode with separate mock_checker_allowlist;
3. fixture package wrapper that declares fixture_mode: mock_execution;
4. schema-compatible production input plus mock checker substitution controlled outside the production input.

The chosen mechanism must be defined in 66.5 and 66.6.
No mock-execution mechanism may weaken production runner input validation.
No mock-execution mechanism may allow production inputs to execute mock checkers.
Mock-execution validation cannot replace real execution validation for M66 completion.

## 11. runner_options

- strict
- json
- timeout_seconds
- execution_mode

## 12. runner_options.json Boundary

runner_options.json is advisory only.
The runner's machine-readable output mode is controlled by CLI --json.
runner_options.json must not override CLI output mode.
If runner_options.json is false but CLI --json is provided, runner should emit JSON and record warning RUNNER_OPTIONS_JSON_FALSE_IGNORED.
If CLI --json is missing, treat as CLI misuse and exit 2.

## 13. Timeout Contract

timeout_seconds must be integer from 1 to 300.
Recommended default is 30.
Invalid timeout value must block future runner validation.
Checker timeout must block future runner validation.

## 14. execution_mode and --no-execute

execution_mode values:
execute
no_execute

CLI --no-execute forces effective_execution_mode to no_execute.
If package runner_options.execution_mode is no_execute and CLI --no-execute is absent, runner must still use no_execute behavior.
If package runner_options.execution_mode is execute and CLI --no-execute is present, CLI wins and effective_execution_mode becomes no_execute.
Effective execution_mode must be reported in JSON output.

## 15. no_execute Boundary

No execution means no validation proof.
No validation proof means no PASS.

effective_execution_mode: no_execute means child checkers are not executed.
M66_UNIFIED_RUN_PASS is forbidden.
M66_UNIFIED_RUN_PASS_WITH_WARNINGS is forbidden.
Allowed outcomes are M66_UNIFIED_RUN_NOT_ENOUGH_EVIDENCE or M66_UNIFIED_RUN_BLOCKED.

## 16. human_review_required

human_review_required must be true.
human_review_required false must block future runner validation.
Human review remains required regardless of runner result.

## 17. non_authority_boundary

Unified runner result is not approval.
Unified runner result does not complete the task.
Human review remains required.

Missing or empty non_authority_boundary must block future runner validation.

## 18. Forbidden Operational Fields

approved
task_approved
task_complete
task_completed
completion_approved
completion_authorized
completion_gate_passed
human_review_not_required
skip_human_review
merge_authorized
push_authorized
release_authorized
production_ready
ready_for_production
m67_started_automatically

If these appear as operative package fields, future runner validation must block.

## 19. Output Non-Authority

The input contract does not define approval.
The input contract does not define task completion.
The input contract does not authorize merge, push, release, or production deployment.
The input contract does not start M67.
Human review remains required.

## 20. Example Valid Package

```json
{
  "contract_version": "1.0.0",
  "package_type": "unified_runner_input",
  "task_id": "example-task",
  "task_brief_path": "tasks/active-task.md",
  "task_validation_package_path": "reports/task-validation-package.json",
  "agent_evidence_path": "reports/agent-task-output-evidence.json",
  "acceptance_criteria_package_path": "reports/acceptance-criteria-check-package.json",
  "expected_checkers": [
    {
      "checker_id": "task_validation_contract_checker",
      "script_path": "scripts/check-task-validation-contract.py",
      "input_arg": "--package",
      "input_path_field": "task_validation_package_path",
      "required": true
    },
    {
      "checker_id": "agent_task_evidence_checker",
      "script_path": "scripts/check-agent-task-evidence.py",
      "input_arg": "--evidence",
      "input_path_field": "agent_evidence_path",
      "required": true
    },
    {
      "checker_id": "acceptance_criteria_checker",
      "script_path": "scripts/check-acceptance-criteria.py",
      "input_arg": "--package",
      "input_path_field": "acceptance_criteria_package_path",
      "required": true
    }
  ],
  "runner_options": {
    "strict": false,
    "json": true,
    "timeout_seconds": 30,
    "execution_mode": "execute"
  },
  "human_review_required": true,
  "non_authority_boundary": [
    "Unified runner result is not approval.",
    "Unified runner result does not complete the task.",
    "Human review remains required."
  ]
}
```

## 21. Relationship to Later Tasks

66.3 defines aggregation semantics.
66.4 defines claim boundary.
66.5 implements runner and must define runtime mock-execution handling.
66.6 creates fixtures and must define mock-execution fixture contract.
66.7 validates integration.
66.8 reviews actions.
66.9 collects evidence.
66.10 closes M66.

## 22. Final Status

FINAL_STATUS: M66_UNIFIED_RUNNER_INPUT_CONTRACT_DEFINED_WITH_WARNINGS
