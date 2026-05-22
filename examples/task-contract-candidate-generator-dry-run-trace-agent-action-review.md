# Example Task Contract Candidate Generator Dry-Run Trace — Agent Action Review

## Purpose
Показать dry-run trace (след) для генератора M51 на примере `agent-action-review`.

## Example Boundary
Example artifact is not approval.
Example artifact does not authorize execution.
Example artifact does not authorize queue placement.
Example artifact does not authorize active-task replacement.
Example artifact does not authorize implementation.
Example artifact does not create active task state.
Example artifact does not create queue entry.
M51 example artifacts are documentation only.
M51 example artifacts must not be copied into tasks/active-task.md.
M51 example artifacts must not be placed into tasks/queue/.
M51 example artifacts require later M52 validation and M53 placement review before lifecycle movement.

## Command
```bash
python3 scripts/generate-task-contract-candidate.py \
  --input examples/task-contract-candidate-generator-input-agent-action-review.md \
  --json
```

## Dry-Run Mode Note
Note: this example intentionally omits the --dry-run CLI flag.

Dry-run behavior is still expected because:
- dry-run is the default generator behavior when --write is not provided;
- the input file also declares generation_mode: dry_run.

The --dry-run flag may be used explicitly, but it is not required for this example.

## Expected Result
Expected result: TASK_CONTRACT_CANDIDATE_GENERATION_DRY_RUN_OK
Expected exit code: 0

## Expected JSON Shape
```json
{
  "result": "TASK_CONTRACT_CANDIDATE_GENERATION_DRY_RUN_OK",
  "exit_code": 0,
  "dry_run": true,
  "written": false,
  "output_path": null,
  "generated_candidate_path": null,
  "primary_validator_target": null,
  "would_write_to": "generated/task-contract-candidates/agent-action-review.generated-conversion-package.md",
  "findings": [],
  "warnings": [],
  "non_authority_markers": []
}
```

## Dry-Run Semantics
Dry-run predicted output path is not a written artifact.
Dry-run does not create lifecycle state.
Dry-run does not create primary_validator_target.
Dry-run does not create generated_conversion_package_path.
Dry-run does not create generated_candidate_path.

would_write_to is predicted.
output_path remains null.
generated_candidate_path remains null.
primary_validator_target remains null.
written remains false.
dry_run remains true.

## Predicted Output Path
generated/task-contract-candidates/agent-action-review.generated-conversion-package.md

## Non-Authority Rules
This dry-run trace is not approval.
This dry-run trace does not authorize execution.
This dry-run trace does not authorize queue placement.
This dry-run trace does not authorize active-task replacement.
This dry-run trace does not authorize implementation.
This dry-run trace does not create generated artifacts.

GENERATOR_DOES_NOT_AUTHORIZE_EXECUTION
GENERATOR_DOES_NOT_PLACE_TASK_IN_QUEUE
GENERATOR_DOES_NOT_MODIFY_ACTIVE_TASK
GENERATOR_DOES_NOT_CREATE_APPROVAL_RECORDS
GENERATOR_OUTPUT_REQUIRES_LATER_PLACEMENT_GATE
GENERATOR_PASS_IS_NOT_APPROVAL
GENERATOR_PASS_IS_NOT_EXECUTION_PERMISSION
GENERATOR_PASS_IS_NOT_QUEUE_PLACEMENT
GENERATOR_PASS_IS_NOT_ACTIVE_TASK_REPLACEMENT
GENERATOR_PASS_IS_NOT_IMPLEMENTATION_AUTHORIZATION

## Explicit Non-Goals
Task 51.7 does not do:
- create real generated artifacts
- write to generated/task-contract-candidates/
- create queue entries
- modify tasks/active-task.md
- modify tasks/queue/
- create approval records
- create files under approvals/
- authorize execution
- authorize queue placement
- authorize active-task replacement
- authorize implementation
- create fixtures
- modify generator CLI
- create evidence reports
- create lessons entries
- create completion reviews
- commit
- push
- merge
- deploy
- release
