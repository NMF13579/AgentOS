# Execution Session Boundary

## Metadata

- boundary_id: exec-session-boundary-<task_id>-<YYYYMMDDHHMMSS>
- task_id: <task_id>
- request_id: <request_id>
- preconditions_id: <preconditions_id>
- boundary_status: EXECUTION_SESSION_BOUNDARY_NOT_SATISFIED
- checked_at: <YYYY-MM-DD>
- checked_by: <agent_or_human_identifier>

## Source References

- source_references:
  - m58_intake_report_path: reports/m58-m57-completion-intake.md
  - m58_architecture_path: docs/CONTROLLED-EXECUTION-SESSION-ARCHITECTURE.md
  - request_contract_path: docs/EXECUTION-SESSION-REQUEST-CONTRACT.md
  - request_schema_path: schemas/execution-session-request.schema.json
  - preconditions_contract_path: docs/EXECUTION-SESSION-PRECONDITIONS-CONTRACT.md
  - preconditions_schema_path: schemas/execution-session-preconditions.schema.json
  - execution_session_request_path: <path/to/session/request/artifact>
  - execution_session_preconditions_path: <path/to/preconditions/result/artifact>

## Scope Boundary

- scope_boundary:
  - scope_summary_present: <true|false>
  - allowed_files_declared: <true|false>
  - allowed_dirs_declared: <true|false>
  - out_of_scope_declared: <true|false>
  - max_file_count_declared: <true|false>
  - scope_expansion_allowed: false
  - scope_expansion_policy: <human_checkpoint_required|not_applicable>
  - scope_boundary_result: <SCOPE_BOUNDARY_SATISFIED|SCOPE_BOUNDARY_SATISFIED_WITH_WARNINGS|SCOPE_BOUNDARY_NOT_SATISFIED|SCOPE_BOUNDARY_BLOCKED>

## Command Boundary

- command_boundary:
  - allowed_commands_declared: <true|false>
  - forbidden_commands_declared: <true|false>
  - unknown_commands_policy: <treat_as_forbidden|requires_review>
  - dangerous_commands_absent_from_allowed: <true|false>
  - human_checkpoint_commands_declared: <true|false>
  - command_boundary_result: <COMMAND_BOUNDARY_SATISFIED|COMMAND_BOUNDARY_SATISFIED_WITH_WARNINGS|COMMAND_BOUNDARY_NOT_SATISFIED|COMMAND_BOUNDARY_BLOCKED>

## Write Boundary

- write_boundary:
  - requested_write_paths_declared: <true|false>
  - write_paths_within_scope: <true|false>
  - write_paths_exclude_m59_artifacts: <true|false>
  - write_paths_exclude_approval_records: <true|false>
  - write_paths_exclude_lifecycle_state: <true|false>
  - write_paths_exclude_unscoped_protected_reports: <true|false>
  - write_boundary_result: <WRITE_BOUNDARY_SATISFIED|WRITE_BOUNDARY_SATISFIED_WITH_WARNINGS|WRITE_BOUNDARY_NOT_SATISFIED|WRITE_BOUNDARY_BLOCKED>

## Protected Path Boundary

- protected_path_boundary:
  - protected_paths_declared: <true|false>
  - protected_paths_acknowledged: <true|false>
  - protected_paths_excluded_from_writes: <true|false>
  - protected_path_override_requested: false
  - protected_path_human_checkpoint_required: <true|false>
  - protected_path_boundary_result: <PROTECTED_PATH_BOUNDARY_SATISFIED|PROTECTED_PATH_BOUNDARY_SATISFIED_WITH_WARNINGS|PROTECTED_PATH_BOUNDARY_NOT_SATISFIED|PROTECTED_PATH_BOUNDARY_BLOCKED>

## Session State Boundary

- session_state_boundary:
  - session_already_open: false
  - conflicting_session_record_exists: false
  - session_state_claimed_by_request: <NONE|OPEN|ACTIVE|CLOSED>
  - allowed_initial_state: <true|false>
  - session_state_boundary_result: <SESSION_STATE_BOUNDARY_SATISFIED|SESSION_STATE_BOUNDARY_SATISFIED_WITH_WARNINGS|SESSION_STATE_BOUNDARY_NOT_SATISFIED|SESSION_STATE_BOUNDARY_BLOCKED>

## Session Close Boundary

- session_close_boundary:
  - allowed_close_state: PENDING_M59_VERIFICATION
  - m59_handoff_required: true
  - task_completion_claim_absent: <true|false>
  - result_verification_claim_absent: <true|false>
  - lifecycle_mutation_claim_absent: <true|false>
  - session_close_boundary_result: <SESSION_CLOSE_BOUNDARY_SATISFIED|SESSION_CLOSE_BOUNDARY_SATISFIED_WITH_WARNINGS|SESSION_CLOSE_BOUNDARY_NOT_SATISFIED|SESSION_CLOSE_BOUNDARY_BLOCKED>

## Violation Classification

- violation_classification: <NO_BOUNDARY_VIOLATION|BOUNDARY_WARNING|BOUNDARY_NOT_SATISFIED|BOUNDARY_BLOCKER|BOUNDARY_UNSAFE|BOUNDARY_CONTRADICTORY|BOUNDARY_PREMATURE_DOWNSTREAM>

## Warnings

- warnings: []

## Blockers

- blockers: []

## Handoff to 58.5 Record / Output Contract

- handoff_to_record_output_contract: false

## Non-Authority Acknowledgement

This execution session boundary result does not open an execution session.
This execution session boundary result does not authorize execution.
This execution session boundary result does not approve task completion.
This execution session boundary result does not verify execution result.
This execution session boundary result does not mutate lifecycle state.
This execution session boundary result only determines whether the request may proceed to M58 record/output modeling.

## Final Boundary Status

- final_boundary_status: EXECUTION_SESSION_BOUNDARY_NOT_SATISFIED
