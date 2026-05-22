# Task Contract Candidate Generator Policy

## Purpose
Task contract candidate generator policy defines allowed and forbidden behavior for future generator implementation.

Task contract candidate generator policy does not implement generator behavior.

Task contract candidate generator policy does not create generated artifacts.

Task contract candidate generator policy does not authorize execution.

## Policy Boundary
Generator policy is not generator implementation.
Generator policy is not approval.
Generator policy does not authorize execution.
Generator policy does not authorize queue placement.
Generator policy does not authorize active-task replacement.
Generator policy does not authorize implementation.
Generator policy does not create generated artifacts.
Generator policy does not create lifecycle state.

## Relationship to M51 Architecture
Task 51.1 defines generator architecture.
Task 51.2 defines generator input contract.
Task 51.3 defines generator output contract.
Task 51.4 defines generator policy only.

## Relationship to Generator Input Contract
M51 generator policy must preserve generator input boundaries from Task 51.2.

## Relationship to Generator Output Contract
M51 generator policy must preserve generator output boundaries from Task 51.3.
M51 generator policy must preserve M50 validator compatibility.

## Generator Default Behavior Policy
The future generator must default to dry-run behavior.

The future generator must not write files unless write mode is explicitly requested.

The future generator must not infer write mode from input readiness.

The future generator must not infer execution permission from successful generation.

The future generator must not infer queue eligibility from successful generation.

The future generator must not infer active-task eligibility from successful generation.

Generator PASS is not approval.
Generator PASS is not execution permission.
Generator PASS is not queue placement.
Generator PASS is not active-task replacement.
Generator PASS is not implementation authorization.

## Dry-Run Policy
Dry-run is the default safe mode.

Dry-run must not write files.

Dry-run must not create generated artifacts.

Dry-run must not create primary_validator_target.

Dry-run must not create output_path.

Dry-run must not create generated_conversion_package_path.

Dry-run may predict would_write_to.

Dry-run predicted output path is not a written artifact.

Dry-run does not create lifecycle state.

dry-run predicts would_write_to

## Write Policy
Write mode requires explicit write intent.

Write mode requires explicit output directory.

Write mode may write only to generated/task-contract-candidates/.

Write mode must write the primary generated artifact as a generated conversion package with embedded task_contract_candidate.

Write mode must not write standalone candidate-only artifacts as primary output.

Write mode must not write to tasks/active-task.md.

Write mode must not write inside tasks/queue/.

Write mode must not write inside approvals/.

Write mode must not create approval records.

Write to staging does not create lifecycle state.

write creates output_path
only write creates primary_validator_target

## Output Target Policy
Allowed output target family:

generated/task-contract-candidates/

output_target must resolve inside generated/task-contract-candidates/.
output_path must resolve inside generated/task-contract-candidates/.
generated_conversion_package_path must resolve inside generated/task-contract-candidates/.
primary_validator_target must resolve inside generated/task-contract-candidates/.
would_write_to must resolve inside generated/task-contract-candidates/.

Task 51.4 defines output target policy only.
Task 51.4 does not create generated/.
Task 51.4 does not write generated artifacts.

## Path Safety Policy
Path traversal is forbidden.

String-prefix path checks are not sufficient.

Future generator implementation must use resolved paths.

Future generator implementation must ensure output paths remain inside generated/task-contract-candidates/.

Future generator implementation must reject paths resolving outside generated/task-contract-candidates/.

Future generator implementation must reject absolute paths unless explicitly normalized and verified inside the staging boundary.

Path safety must be enforced before any write.

Path safety failure must block write behavior.

Path safety failure must not be downgraded to warning.

## Primary Output Format Policy
The primary generated artifact must be a generated conversion package with embedded task_contract_candidate.

Standalone candidate-only artifacts are not valid primary outputs in M51.

Optional secondary candidate-only artifacts are out of scope for M51 unless a later explicit task authorizes them.

Primary output format must remain generated_conversion_package_with_embedded_candidate.

generated/task-contract-candidates/<candidate-id>.generated-conversion-package.md

## M50 Validator Compatibility Policy
Generated output must be compatible with:

python3 scripts/validate-proposal-to-task-conversion.py --conversion <path>

M51 generated output must preserve the M50 conversion package shape expected by the M50 validator.

M51 must not generate a standalone candidate-only artifact as the primary validator target if M50 validator requires conversion_package + embedded task_contract_candidate.

Future generator output must pass M50 validator before it can be considered generation-successful.

A generated artifact that cannot pass M50 validator must be treated as failed or blocked.

M50 validator PASS is not execution approval.

M50 validator PASS is not queue placement approval.

M50 validator PASS is not active-task replacement approval.

## Generated Candidate Path Policy
In M51, generated_candidate_path must be null.

M51 primary output is the generated conversion package, not a standalone candidate-only artifact.

generated_candidate_path may become non-null only in a later explicit task that authorizes secondary candidate-only artifacts.

generated_candidate_path null in M51 is a semantic rule.

## would_write_to Policy
would_write_to is required by output record schema.

In dry-run mode, would_write_to must contain the predicted staging path.

In write mode, would_write_to may equal output_path or be null, but must not be omitted.

write + would_write_to equals output_path or null is a semantic rule.

## Boundary Flag Policy
```yaml
boundaries:
  generated_candidate_is_active_task: false
  generated_candidate_is_queue_entry: false
  execution_authorized: false
  active_task_write_allowed: false
  queue_write_allowed: false
  approval_record_created: false
```

generated_candidate_is_active_task must remain false.
generated_candidate_is_queue_entry must remain false.
execution_authorized must remain false.
active_task_write_allowed must remain false.
queue_write_allowed must remain false.
approval_record_created must remain false.

Boundary flags must not be weakened.
Boundary flags must not be inferred from successful generation.
Boundary flags must not be changed by dry-run.
Boundary flags must not be changed by write to staging.

## Carry-Forward Preservation Policy
Accepted limitations must be preserved in generated output records.
Open questions must be preserved in generated output records.
Downstream limits must be preserved in generated output records.
Non-authority boundary must be preserved in generated output records.
Source traceability must be preserved in generated output records.

The generator must not silently erase accepted limitations.
The generator must not silently erase open questions.
The generator must not silently erase downstream limits.
The generator must not silently erase non-authority boundaries.
The generator must not silently erase source traceability.

## Forbidden Transformations
No silent scope expansion.
No inferred execution permission.
No inferred queue eligibility.
No inferred active-task eligibility.
No approval record generation.
No conversion of candidate into active task.
No conversion of candidate into queue entry.
No weakening of forbidden_changes.
No expansion of allowed_changes.
No removal of limitations, open questions, or downstream limits.
No generation of primary output incompatible with M50 validator.
No dry-run claim that a file was written.
No dry-run claim that primary_validator_target exists.
No standalone candidate-only artifact as primary output.
No generated_candidate_path value in M51.

## Blocking Policy Conditions
- source conversion package missing
- source generator input missing
- source generator input invalid
- source validator missing
- source validator does not reference M50 validator
- primary output format not M50-compatible
- standalone candidate-only artifact used as primary validator target
- output target outside staging area
- generated conversion package path outside staging area
- output_path outside staging area
- primary_validator_target outside staging area
- would_write_to outside staging area
- path traversal requested
- absolute path outside staging boundary
- active-task target requested
- queue target requested
- approvals target requested
- dry-run attempts to write files
- dry-run output_path non-null
- dry-run generated_conversion_package_path non-null
- dry-run primary_validator_target non-null
- dry-run written field indicates file write
- write output_path missing
- write generated_conversion_package_path missing
- write primary_validator_target missing
- write primary_validator_target mismatches output_path
- write generated_conversion_package_path mismatches output_path
- write would_write_to omitted despite required schema field
- generated_candidate_path non-null without explicit future authorization
- generated candidate marked as active task
- generated candidate marked as queue entry
- execution authorization claimed
- active task write allowed
- queue write allowed
- approval record creation claimed
- carry-forward preservation missing
- accepted limitations preservation missing
- open questions preservation missing
- downstream limits preservation missing
- non-authority boundary preservation missing

## Future CLI Policy Expectations
Future generator CLI must default to dry-run.

Future generator CLI write mode must require explicit write flag.

Future generator CLI write mode must require explicit output directory.

Future generator CLI must reject output directories outside generated/task-contract-candidates/.

Future generator CLI must emit machine-readable result tokens.

Future generator CLI must preserve non-authority markers.

Expected future result tokens:
- TASK_CONTRACT_CANDIDATE_GENERATION_DRY_RUN_OK
- TASK_CONTRACT_CANDIDATE_GENERATION_WRITE_OK
- TASK_CONTRACT_CANDIDATE_GENERATION_FAILED
- TASK_CONTRACT_CANDIDATE_GENERATION_BLOCKED

Future CLI policy expectations are not CLI implementation.

Task 51.4 does not create scripts/generate-task-contract-candidate.py.

## Non-Authority Rules
Task contract candidate generator policy is not approval.
Task contract candidate generator policy does not authorize execution.
Task contract candidate generator policy does not authorize queue placement.
Task contract candidate generator policy does not authorize active-task replacement.
Task contract candidate generator policy does not authorize implementation.
Task contract candidate generator policy does not create generated artifacts.
Task contract candidate generator policy does not create active task state.
Task contract candidate generator policy does not create queue entry.

Task 51.4 does not implement generator behavior.
Task 51.4 does not validate actual generation.
Task 51.4 does not create generated outputs.
Task 51.4 does not create examples.
Task 51.4 does not create fixtures.
Task 51.4 does not create CLI behavior.

## Explicit Non-Goals
Task 51.4 does not do:
- create generator CLI
- create generator behavior
- create generator implementation
- create schemas
- create templates
- create fixtures
- create examples
- create generated artifacts
- create queue entries
- modify tasks/active-task.md
- modify tasks/queue/
- create real approval records
- create files under approvals/
- authorize execution
- authorize queue placement
- authorize active-task replacement
- authorize implementation
- create evidence reports
- create lessons entries
- create completion reviews
- commit
- push
- merge
- deploy
- release
