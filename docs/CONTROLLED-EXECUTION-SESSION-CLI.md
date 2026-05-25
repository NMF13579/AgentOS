# Controlled Execution Session CLI

## Purpose

This document defines the interface, behavior, and output model of the Controlled Execution Session CLI for M58.

The CLI evaluates the readiness of the controlled execution session chain against the defined preconditions, boundaries, record outputs, and policy rules. It does not open an execution session. It does not execute task work. It does not verify final results. It does not approve task completion. It does not mutate lifecycle state.

## Preconditions

Before evaluating execution session readiness, the CLI validates that:
- The required input files exist.
- All input paths resolve within the repository root.
- The files are valid JSON.
- Top-level statuses are present and recognized.

## Position in M58

This is task 58.7. It consumes the artifacts from 58.2 through 58.5, applies the policy defined in 58.6, and serves as the readiness intake for 58.8 fixtures, 58.9 fixture runner, 58.10 integration summary, and eventually M59 handoff.

## CLI Inputs

The CLI accepts four primary input artifacts:
1. Request Contract (--request)
2. Preconditions Result (--preconditions)
3. Boundary Result (--boundary)
4. Record/Output Contract (--record)

## CLI Arguments

The CLI supports the following command-line arguments:
- `--request <path>`: Path to request contract artifact.
- `--preconditions <path>`: Path to preconditions result artifact.
- `--boundary <path>`: Path to boundary result artifact.
- `--record <path>`: Path to record/output artifact.
- `--json`: Emit classification results as valid JSON to stdout.
- `--explain`: Print human-readable explanations of the evaluation.
- `--strict`: Enable strict mode, converting warnings into blockers.
- `--root <path>`: Override the repository root for path resolution.
- `--help`: Print the help message and exit.

## Input Path Safety

The CLI implements rigorous path safety:
- It resolves the repository root path.
- It resolves each input path.
- It rejects any path resolving outside the repository root.
- Absolute paths pointing outside the repository root are rejected.
- Path traversal escapes (e.g. symlinks pointing outside) fail closed.
- Path safety rejections produce a result of `CONTROLLED_EXECUTION_SESSION_BLOCKED` and exit with code 2.

## Status Interpretation

The CLI interprets statuses across all inputs:
- Request: `EXECUTION_SESSION_REQUEST_READY_FOR_PRECONDITIONS` may proceed. `EXECUTION_SESSION_REQUEST_DRAFT` is NOT_READY. All others are BLOCKED.
- Preconditions: `EXECUTION_SESSION_PRECONDITIONS_READY` may proceed. `EXECUTION_SESSION_PRECONDITIONS_READY_WITH_WARNINGS` is a READY_WITH_WARNINGS candidate. `EXECUTION_SESSION_PRECONDITIONS_NOT_READY` is NOT_READY. All others are BLOCKED.
- Boundary: `EXECUTION_SESSION_BOUNDARY_SATISFIED` may proceed. `EXECUTION_SESSION_BOUNDARY_SATISFIED_WITH_WARNINGS` is a READY_WITH_WARNINGS candidate. `EXECUTION_SESSION_BOUNDARY_NOT_SATISFIED` is NOT_READY. All others are BLOCKED.
- Record: `EXECUTION_SESSION_RECORD_READY_FOR_POLICY` and `EXECUTION_SESSION_RECORD_CLOSED_PENDING_M59_VERIFICATION` may proceed. `EXECUTION_SESSION_RECORD_DRAFT` is NOT_READY. All others are BLOCKED.

## Policy Decision Mapping

The CLI maps internal policy decisions to final outcomes:
- `M58_SESSION_POLICY_READY` -> `CONTROLLED_EXECUTION_SESSION_READY`
- `M58_SESSION_POLICY_READY_WITH_WARNINGS` -> `CONTROLLED_EXECUTION_SESSION_READY_WITH_WARNINGS`
- `M58_SESSION_POLICY_NOT_READY` -> `CONTROLLED_EXECUTION_SESSION_NOT_READY`
- `M58_SESSION_POLICY_BLOCKED` -> `CONTROLLED_EXECUTION_SESSION_BLOCKED`

## Result Values

The final output result will be exactly one of:
- `CONTROLLED_EXECUTION_SESSION_READY`
- `CONTROLLED_EXECUTION_SESSION_READY_WITH_WARNINGS`
- `CONTROLLED_EXECUTION_SESSION_NOT_READY`
- `CONTROLLED_EXECUTION_SESSION_BLOCKED`

## Exit Code Mapping

The CLI maps results to the following exit codes:
- `CONTROLLED_EXECUTION_SESSION_READY` -> exit 0
- `CONTROLLED_EXECUTION_SESSION_READY_WITH_WARNINGS` -> exit 0
- `CONTROLLED_EXECUTION_SESSION_NOT_READY` -> exit 1
- `CONTROLLED_EXECUTION_SESSION_BLOCKED` -> exit 2

Exit code 0 does not authorize execution. Exit code 0 does not approve task completion. Exit code 0 does not verify result. Exit code 0 does not permit merge, push, release, or lifecycle mutation.

## JSON Output

When running in `--json` mode, the CLI outputs valid JSON only:
```json
{
  "result": "CONTROLLED_EXECUTION_SESSION_READY",
  "policy_decision": "M58_SESSION_POLICY_READY",
  "exit_code": 0,
  "warnings": [],
  "blockers": [],
  "inputs": {
    "request": "...",
    "preconditions": "...",
    "boundary": "...",
    "record": "..."
  },
  "non_authority": [
    "M58 CLI does not open an execution session.",
    "M58 CLI does not authorize task completion.",
    "M58 CLI does not verify execution result.",
    "M58 CLI does not create approval.",
    "M58 CLI does not authorize merge, push, or release.",
    "M58 CLI does not mutate lifecycle state."
  ]
}
```

## Human Output

By default, the CLI prints human-readable output:
- `RESULT: <result>`
- `POLICY_DECISION: <decision>`
- `EXIT_CODE: <exit_code>`
- `WARNINGS: <count>`
- `BLOCKERS: <count>`
Along with the required non-authority statements.

## Explain Output

When running in `--explain` mode, the CLI adds human-readable logs detailing:
- Why the result was selected.
- Which layer determined the result.
- Whether blockers or warnings were found.
- Whether M59 handoff is preserved.
- Why the result is not approval or verification.

## Strict Mode Behavior

When `--strict` is enabled, the CLI escalates warnings:
- Ambiguous or safety-relevant warning states are promoted to blockers.
- Any presence of warnings (or `READY_WITH_WARNINGS` status) causes the CLI to classify the session as `CONTROLLED_EXECUTION_SESSION_BLOCKED` (exit 2).
- Strict mode does not weaken blockers or convert blocked to warnings.
- Strict mode does not authorize execution.

## Fail-Closed Behavior

The CLI fails closed for any ambiguous, contradictory, unsafe, or premature downstream state.
- Missing or malformed artifacts immediately block the evaluation.
- M59 optional claims, protected path overrides without checkpoints, and unknown status values default to blocked.

## Unsafe Claim Detection

The CLI scans the raw text of parsed inputs for unsafe claims. It blocks if any input contains:
- `task complete` or `task is complete`
- `result verified` or `result is verified`
- `task approved` or `task is approved`
- `execution authorized` or `execution is authorized`
- `M59 verification optional` or `M59 is optional`
- `push allowed` or `push is allowed`
- `merge allowed` or `merge is allowed`
- `release allowed` or `release is allowed`
- `lifecycle mutation allowed` or `lifecycle state may be mutated`

## Performed Actions Checks

The CLI blocks if any of the following performed actions are true:
- `execution_session_started`
- `execution_session_opened`
- `execution_performed`
- `task_marked_done`
- `result_verified`
- `approval_record_created`
- `lifecycle_mutation_performed`
- `commit_created`
- `push_performed`
- `merge_performed`
- `m59_artifact_created`

## Forbidden Action Checks

The CLI blocks if any of the following forbidden actions are true:
- `approval_creation`
- `lifecycle_mutation`
- `task_completion_claim`
- `result_verification_claim`
- `commit`
- `push`
- `merge`
- `release`
- `m59_artifact_creation`
- `protected_path_violation`
- `raw_dangerous_command`

## M59 Handoff Checks

The CLI checks that:
- `handoff_to_m59_required` is true in the request.
- `handoff_required` is true in `m59_handoff` inside the record.
- Missing, optional, or false handoff claims immediately block execution.

## Non-Authority Rules

The CLI enforces non-authority boundaries:
- M58 CLI does not open an execution session.
- M58 CLI does not authorize task completion.
- M58 CLI does not verify execution result.
- M58 CLI does not create approval.
- M58 CLI does not authorize merge, push, or release.
- M58 CLI does not mutate lifecycle state.
- M58 CLI only classifies controlled execution session readiness.

## Relationship to 58.8 Fixtures

58.8 provides positive and negative JSON files representing various test scenarios. The CLI serves as the intake and evaluation engine for these test scenarios.

## Relationship to 58.9 Fixture Runner

58.9 executes the fixture runner. The fixture runner passes the M58 JSON fixtures to the CLI, checking that it evaluates them correctly and returns the expected exit codes.

## Relationship to M59 Verification

M59 verification consumes the closed record output only. The CLI ensures the record output is structurally sound and satisfies M58 policy before M59 verification begins.

## Forbidden Claims

This documentation does not claim:
- execution session is open
- execution is authorized
- task is complete
- result is verified
- task is approved
- human review is replaced
- M59 verification is optional
- commit is allowed
- push is allowed
- merge is allowed
- release is allowed
- lifecycle state may be mutated

## Final CLI Status

FINAL_STATUS: M58_CONTROLLED_EXECUTION_SESSION_CLI_DEFINED

This status means only that the CLI and CLI documentation exist.
It does not mean execution was authorized.
It does not mean execution session was opened.
It does not mean result was verified.
