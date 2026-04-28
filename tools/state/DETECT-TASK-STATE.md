# Detect Task State

## Purpose

`scripts/detect-task-state.py` is a read-only detector for Task State Report v1.1.
It inspects task evidence and returns a JSON report for the current task state.
It does not validate transitions and does not execute transitions.

## Command

```bash
python3 scripts/detect-task-state.py tasks/{task-id}
```

## Inputs

The detector accepts one positional argument:

- path to a task directory

If the argument is missing or `--help` is requested, the detector prints usage and exits with code `2`.

## Output Format

The detector prints Task State Report v1.1 as JSON.

Required fields:

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

`schema_version` is always `"1.1"`.
`generated_at` is a UTC ISO 8601 timestamp.

## analysis_status

| analysis_status | Meaning |
|---|---|
| `ok` | Evidence is consistent and the state was detected cleanly. |
| `invalid` | Evidence is present, but the current state is not fully consistent. |
| `conflict` | Mutually exclusive evidence was found. |

If mutually exclusive evidence is found, the detector returns `state_conflict` and `analysis_status: conflict`.
If evidence is incomplete or inconsistent, the detector keeps the detected state and returns `analysis_status: invalid`.

## Evidence

`evidence` is an array of structured objects.
Each item has:

- `type`
- `path`
- `status`
- `note`

Allowed `evidence.status` values:

- `present`
- `missing`
- `valid`
- `invalid`
- `conflicting`
- `planned`

`warnings` is always present and is emitted as `[]` when there are no warnings.

## Read-Only Guarantee

The detector is read-only.
It only reads evidence and returns a JSON report.
It does not modify task files.
It does not create approval markers.
It does not create `tasks/failed/`.
It does not replace `tasks/active-task.md`.
It does not move queue entries.

## Exit Codes

- `0` - JSON report successfully produced, including `state_conflict`
- `1` - runtime or fatal error, such as an unreadable filesystem or unexpected exception
- `2` - CLI usage error or `--help`

## Safety Boundaries

The detector does not:

- validate transitions
- execute transitions
- modify task files
- create approval markers
- create `tasks/failed/`
- replace `tasks/active-task.md`
- move queue entries
- grant execution authority

## Example Usage

```bash
python3 scripts/detect-task-state.py tasks/task-123
python3 scripts/detect-task-state.py tasks/nonexistent-task
```
