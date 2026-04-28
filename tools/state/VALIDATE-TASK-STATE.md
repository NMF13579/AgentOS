# Validate Task State

## Purpose

`scripts/validate-task-state.py` is a read-only validator for task state consistency.
It checks whether the report produced by `scripts/detect-task-state.py` is a valid Task State Report v1.1 and whether the detected state is consistent with the evidence.
It does not check requested transitions.
It does not execute transitions.

## Command

```bash
python3 scripts/validate-task-state.py tasks/{task-id}
```

## Inputs

The validator accepts one positional argument:

- path to a task directory

If the argument is missing or `--help` is requested, the validator prints usage and exits with code `2`.

## Outputs

The validator prints a human-readable report to stdout:

- `TASK STATE VALIDATION`
- `Task: ...`
- `Detected state: ...`
- `Result: PASS` or `Result: FAIL`
- `Reasons:` when validation fails

## Task State Report v1.1

The validator expects Task State Report v1.1.
The report must include:

- `schema_version`
- `generated_at`
- `task_id`
- `state`
- `analysis_status`
- `evidence`
- `missing_evidence`
- `allowed_next_states`
- `blocked_reason`
- `warnings`

If `schema_version != "1.1"`, the validator fails with `expected v1.1 report`.

## analysis_status Handling

- `analysis_status = ok` means the detector found consistent evidence.
- `analysis_status = invalid` means the detector found evidence, but the state is partially inconsistent.
- `analysis_status = conflict` means mutually exclusive evidence was found and the validator fails.

The invariant is:

- `state == "state_conflict"` implies `analysis_status == "conflict"`
- `analysis_status == "conflict"` implies `state == "state_conflict"`

## Evidence Handling

The validator reads structured evidence objects and checks that each item has:

- `type`
- `path`
- `status`
- `note`

It rejects any evidence item with `status = conflicting`.
It also applies state-specific consistency checks.

State-specific checks include:

- `review_ready` requires `REVIEW.md`, `execution_allowed: true`, and `READY` or `READY_WITH_EDITS`
- `review_blocked` requires `REVIEW.md` and a blocked review status
- `trace_written` requires `TRACE.md` and `REVIEW.md`
- `contract_drafted` requires a valid contract draft and `TRACE.md`
- `approved_for_execution` requires a valid approval marker and contract draft
- `active` requires `tasks/active-task.md` reference and a valid approval marker
- `completed` requires `tasks/done/` evidence and no active/failed/dropped evidence
- `failed` requires `tasks/failed/` evidence and no active/completed/dropped evidence
- `dropped` requires `tasks/dropped/` evidence and no active/completed/failed evidence

If `analysis_status = invalid`, the validator records a warning and only fails if the invalid evidence breaks the consistency rules for the current state.

`planned` evidence for `tasks/failed/` is not treated as a failure by itself when the task is not failed.

## Read-Only Guarantee

The validator is read-only.
It only reads the detector output and evaluates consistency.
It does not modify task files.
It does not modify detector output.
It does not grant execution authority.
It does not create approval markers.

## Exit Codes

- `0` - validation passed
- `1` - validation failed
- `2` - CLI usage error

## Safety Boundaries

The validator does not:

- execute transitions
- create approval markers
- replace `tasks/active-task.md`
- move queue entries
- create `tasks/failed/`
- modify task files
- modify detector output
- grant execution authority

## Example Usage

```bash
python3 scripts/validate-task-state.py tasks/task-123
python3 scripts/validate-task-state.py tasks/nonexistent-task
```
