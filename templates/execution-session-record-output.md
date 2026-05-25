# Execution Session Record / Output

## Metadata

- record_id: exec-session-record-<task_id>-<YYYYMMDDHHMMSS>
- task_id: <task_id>
- session_id: <session_id>
- request_id: <request_id>
- preconditions_id: <preconditions_id>
- boundary_id: <boundary_id>
- record_status: EXECUTION_SESSION_RECORD_DRAFT
- created_at: <YYYY-MM-DD>
- created_by: <agent_or_human_identifier>

## Source References

- source_references:
  - m58_intake_report_path: reports/m58-m57-completion-intake.md
  - m58_architecture_path: docs/CONTROLLED-EXECUTION-SESSION-ARCHITECTURE.md
  - request_contract_path: docs/EXECUTION-SESSION-REQUEST-CONTRACT.md
  - preconditions_contract_path: docs/EXECUTION-SESSION-PRECONDITIONS-CONTRACT.md
  - boundary_contract_path: docs/EXECUTION-SESSION-BOUNDARY-CONTRACT.md
  - execution_session_request_path: <path/to/session/request/artifact>
  - execution_session_preconditions_path: <path/to/preconditions/result/artifact>
  - execution_session_boundary_path: <path/to/boundary/result/artifact>

## Session State Summary

- session_state_summary:
  - initial_state: <SESSION_NOT_STARTED|SESSION_READY_FOR_CONTROLLED_OPEN>
  - final_state: <SESSION_NOT_STARTED|SESSION_BLOCKED|SESSION_ABORTED|SESSION_CLOSED_PENDING_M59_VERIFICATION>
  - session_opened: <true|false>
  - session_paused: <true|false>
  - session_blocked: <true|false>
  - session_aborted: <true|false>
  - session_closed_pending_m59: <true|false>

## Boundary Snapshot

- boundary_snapshot:
  - scope_boundary_result: <SCOPE_BOUNDARY_SATISFIED|SCOPE_BOUNDARY_SATISFIED_WITH_WARNINGS|SCOPE_BOUNDARY_NOT_SATISFIED|SCOPE_BOUNDARY_BLOCKED>
  - command_boundary_result: <COMMAND_BOUNDARY_SATISFIED|COMMAND_BOUNDARY_SATISFIED_WITH_WARNINGS|COMMAND_BOUNDARY_NOT_SATISFIED|COMMAND_BOUNDARY_BLOCKED>
  - write_boundary_result: <WRITE_BOUNDARY_SATISFIED|WRITE_BOUNDARY_SATISFIED_WITH_WARNINGS|WRITE_BOUNDARY_NOT_SATISFIED|WRITE_BOUNDARY_BLOCKED>
  - protected_path_boundary_result: <PROTECTED_PATH_BOUNDARY_SATISFIED|PROTECTED_PATH_BOUNDARY_SATISFIED_WITH_WARNINGS|PROTECTED_PATH_BOUNDARY_NOT_SATISFIED|PROTECTED_PATH_BOUNDARY_BLOCKED>
  - session_state_boundary_result: <SESSION_STATE_BOUNDARY_SATISFIED|SESSION_STATE_BOUNDARY_SATISFIED_WITH_WARNINGS|SESSION_STATE_BOUNDARY_NOT_SATISFIED|SESSION_STATE_BOUNDARY_BLOCKED>
  - session_close_boundary_result: <SESSION_CLOSE_BOUNDARY_SATISFIED|SESSION_CLOSE_BOUNDARY_SATISFIED_WITH_WARNINGS|SESSION_CLOSE_BOUNDARY_NOT_SATISFIED|SESSION_CLOSE_BOUNDARY_BLOCKED>
  - violation_classification: <NO_BOUNDARY_VIOLATION|BOUNDARY_WARNING|BOUNDARY_NOT_SATISFIED|BOUNDARY_BLOCKER|BOUNDARY_UNSAFE|BOUNDARY_CONTRADICTORY|BOUNDARY_PREMATURE_DOWNSTREAM>

## Command Records

- command_records:
  - commands_requested: []
  - commands_allowed: []
  - commands_blocked: []
  - unknown_commands_detected: false
  - dangerous_commands_detected: false

## Write Records

- write_records:
  - write_paths_requested: []
  - write_paths_allowed: []
  - write_paths_blocked: []
  - protected_write_attempts: 0
  - m59_artifact_write_attempts: 0
  - approval_record_write_attempts: 0
  - lifecycle_state_write_attempts: 0

## Blocked Action Records

- blocked_action_records:
  - execution_start_blocked: false
  - command_blocked: false
  - write_blocked: false
  - protected_path_blocked: false
  - approval_creation_blocked: false
  - lifecycle_mutation_blocked: false
  - commit_blocked: false
  - push_blocked: false
  - merge_blocked: false
  - m59_artifact_blocked: false

## Session Close

- session_close:
  - close_status: SESSION_CLOSE_NOT_CLOSED
  - closed_at: null
  - close_reason: <reason or empty>
  - closed_pending_m59_verification: false
  - task_completion_claimed: false
  - result_verification_claimed: false
  - lifecycle_mutation_claimed: false

## M59 Handoff

- m59_handoff:
  - handoff_required: true
  - handoff_ready: false
  - expected_m59_inputs:
    - <description of expected M59 input 1>
  - known_warnings: []
  - known_blockers: []
  - unresolved_questions: []

## Warnings

- warnings: []

## Blockers

- blockers: []

## Non-Authority Acknowledgement

This execution session record does not approve task completion.
This execution session record does not verify execution result.
This execution session record does not authorize merge, push, or release.
This execution session record does not mutate lifecycle state.
This execution session record only records controlled execution session output for M59 verification.

## Final Record Status

- final_record_status: EXECUTION_SESSION_RECORD_DRAFT
