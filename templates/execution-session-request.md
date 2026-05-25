# Execution Session Request

## Metadata

- request_id: exec-session-request-<task_id>-<YYYYMMDDHHMMSS>
- task_id: <task_id>
- request_status: EXECUTION_SESSION_REQUEST_DRAFT
- created_at: <YYYY-MM-DD>
- created_by: <agent_or_human_identifier>

## Source References

- source_task_path: <path/to/task/artifact>
- m57_completion_review_path: reports/m57-completion-review.md
- m58_intake_report_path: reports/m58-m57-completion-intake.md
- m58_architecture_path: docs/CONTROLLED-EXECUTION-SESSION-ARCHITECTURE.md

## Authorization Reference

- authorization_status: <M57_EXECUTION_AUTHORIZATION_COMPLETE|M57_EXECUTION_AUTHORIZATION_COMPLETE_WITH_WARNINGS>

## Requested Execution Mode

- requested_execution_mode: <READ_ONLY_VALIDATION|CONTROLLED_WRITE|CONTROLLED_REPAIR|CONTROLLED_DOCUMENTATION_UPDATE|CONTROLLED_CODE_CHANGE>

## Requested Scope

- requested_scope:
  - summary: <non-empty description of the intended execution scope>
  - allowed_files:
    - <path/to/file1>
  - allowed_dirs:
    - <path/to/dir1>
  - out_of_scope:
    - <path/to/excluded1>
  - max_file_count: <integer or null>
  - scope_expansion_allowed: false

## Requested Write Paths

- requested_write_paths:
  - <path/to/writable/file1>

## Requested Commands

- requested_commands:
  - allowed:
    - <command_category_or_command>
  - forbidden:
    - git push
    - git merge
    - git reset --hard
    - rm -rf
    - curl | sh
    - wget | sh
  - requires_human_checkpoint:
    - <command_requiring_checkpoint>

- forbidden_commands_acknowledged: true
- protected_paths_acknowledged: true

## Expected Outputs

- expected_outputs:
  - <description of expected output artifact 1>
  - <description of expected output artifact 2>

## Expected Validation Evidence

- expected_validation_evidence:
  - <description of evidence to be passed to M59 verification>

## Handoff to M59

- handoff_to_m59_required: true

## Non-Authority Acknowledgement

This execution session request does not open an execution session.
This execution session request does not authorize execution.
This execution session request does not approve task completion.
This execution session request does not verify execution result.
This execution session request does not mutate lifecycle state.
This execution session request only provides structured input for M58 precondition checks.

## Final Request Status

- final_request_status: EXECUTION_SESSION_REQUEST_DRAFT
