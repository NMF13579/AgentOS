---
type: ux-to-task-proposal-validation
milestone: M49
status: canonical
authority: validation
version: 1.0.0
created: 2026-05-21
owner: human
---

# M49 UX-to-Task Proposal Validation

## Purpose
UX-to-Task Proposal Validator validates non-executable task contract proposal artifacts.

UX-to-Task Proposal Validator does not create task drafts.
UX-to-Task Proposal Validator does not create task contract proposals.
UX-to-Task Proposal Validator does not create executable tasks.
UX-to-Task Proposal Validator does not authorize implementation.
UX-to-Task Proposal Validator does not authorize execution.

Validator PASS is not approval.
Validator PASS is not task generation.
Validator PASS is not implementation authorization.
Validator PASS is not execution authorization.

## Role in M49
This validator is a structure checker for proposal artifacts in M49.
It verifies that non-executable boundaries are preserved.

## Relationship to Task Contract Proposal Template
The validator enforces required fields and boundaries defined in `templates/task-contract-proposal.md`.
It checks status values, boundary flags, carry-forward fields, and source traceability markers.

## Relationship to Decomposition Policy
The validator enforces that proposals do not break decomposition boundaries.
It checks that blocked readiness decisions fail, and authority-claim lines fail.

## Validator Scope
The validator checks:
- frontmatter structure and required keys;
- required body model keys;
- required sections;
- carry-forward presence;
- boundary booleans for non-executable behavior;
- forbidden positive authority claims.

The validator is read-only and only validates files.

## Validator Non-Authority Boundary
Validation result is evidence only.
Validation result does not authorize implementation.
Validation result does not authorize execution.

## Validation Modes
- `--proposal <path>` validates one proposal file.
- `--fixtures` validates all fixture files in valid and negative fixture directories.
- `--explain` prints validator rules only.
- `--json` emits machine-readable JSON.

--explain does not validate a proposal.
--explain returns UX_TO_TASK_PROPOSAL_VALIDATION_OK and exit 0 if rules can be displayed.
--fixtures must return aggregate fixture summary.
--json mode must write only valid JSON to stdout; all non-JSON diagnostics must go to stderr.

## Result Tokens
- `UX_TO_TASK_PROPOSAL_VALIDATION_OK`
- `UX_TO_TASK_PROPOSAL_VALIDATION_FAILED`
- `UX_TO_TASK_PROPOSAL_VALIDATION_BLOCKED`

## Exit Semantics
- `UX_TO_TASK_PROPOSAL_VALIDATION_OK => exit 0`
- `UX_TO_TASK_PROPOSAL_VALIDATION_FAILED => exit 1`
- `UX_TO_TASK_PROPOSAL_VALIDATION_BLOCKED => exit 2`

## JSON Output Contract
For `--proposal --json`:

```json
{
  "mode": "proposal",
  "result": "UX_TO_TASK_PROPOSAL_VALIDATION_OK",
  "errors": [],
  "warnings": [],
  "checked_file": "<path>"
}
```

For `--fixtures --json`:

```json
{
  "mode": "fixtures",
  "result": "UX_TO_TASK_PROPOSAL_VALIDATION_OK",
  "fixture_summary": {
    "positive_passed": 1,
    "positive_failed": 0,
    "negative_failed_as_expected": 13,
    "negative_unexpectedly_passed": 0
  },
  "errors": [],
  "warnings": []
}
```

For `--explain --json`:

```json
{
  "mode": "explain",
  "result": "UX_TO_TASK_PROPOSAL_VALIDATION_OK",
  "rules": []
}
```

`rules` must be non-empty.

## Required Proposal Checks
The validator checks:
- frontmatter exists;
- `type: task-contract-proposal`;
- `proposal_id` exists;
- `proposal_status` exists and is allowed;
- `source_draft_id` exists;
- `source_task_draft_path` exists;
- `source_ux_contract` exists;
- `source_readiness_report` exists;
- `source_boundary_policy` exists;
- `execution_authorized` is false;
- `implementation_authorized` is false;
- `human_authorization_required` is true;
- required body sections exist;
- `task_contract_proposal` model exists;
- `source_sections` exists;
- `source_section` is absent;
- `ux_contract_validation_result` is `UX_CONTRACT_VALIDATION_OK`;
- `readiness_validation_result` is `UX_PLANNING_READINESS_VALIDATION_OK`;
- `readiness_decision` is `UX_PLANNING_READY` or `UX_PLANNING_READY_WITH_LIMITATIONS`;
- `blocking_gaps` absent or empty;
- `accepted_limitations` exists;
- `open_questions` exists;
- `downstream_limits` exists;
- `non_authority_boundary` exists;
- `active_task_allowed` is false;
- `task_queue_allowed` is false;
- forbidden positive authority claims are absent.

Allowed `proposal_status` values:
- `PROPOSED_ONLY`
- `PROPOSAL_READY_FOR_REVIEW`
- `PROPOSAL_BLOCKED`
- `PROPOSAL_INVALID`

## Required Fixture Checks
The validator checks one positive fixture and thirteen negative fixtures.
Positive must pass.
Every negative must fail.

## Fixture Runner Semantics
`--fixtures`:
- validates all files in `tests/fixtures/ux-to-task-proposal/valid`;
- validates all files in `tests/fixtures/ux-to-task-proposal/negative`;
- returns OK only if expected outcomes match;
- returns FAILED if one positive fails or one negative passes unexpectedly;
- returns BLOCKED if fixture directories are missing.

Required fixture summary fields:
- `positive_passed`
- `positive_failed`
- `negative_failed_as_expected`
- `negative_unexpectedly_passed`

Expected values:
- `positive_passed: 1`
- `positive_failed: 0`
- `negative_failed_as_expected: 13`
- `negative_unexpectedly_passed: 0`

## Frontmatter vs Body Model Semantics
Frontmatter may contain compact routing metadata.
Canonical body model contains the full proposal structure.
Validator must not require every body model field to exist in frontmatter.
Validator must distinguish frontmatter-level fields from body-model-level fields.

source_ux_contract may be a path in frontmatter and an object in the body model.
source_readiness_report may be a path in frontmatter and an object in the body model.
source_boundary_policy may be a path in frontmatter and an object in the body model.
active_task_allowed and task_queue_allowed are required in the body model boundaries block, not in frontmatter.

## Forbidden Authority Claims
Validation fails for positive authority claims like:
- task contract proposal authorizes implementation
- task contract proposal authorizes execution
- proposal authorizes implementation
- proposal authorizes execution
- PROPOSED_ONLY authorizes execution
- PROPOSAL_READY_FOR_REVIEW authorizes execution
- validator PASS authorizes implementation
- validator PASS authorizes execution
- readiness authorizes task generation
- readiness authorizes implementation
- readiness authorizes execution
- may be copied into tasks/active-task.md
- may be copied into tasks/queue/

Correct negative statements must pass, for example:
- Task contract proposal does not authorize implementation.
- Task contract proposal does not authorize execution.
- Task contract proposal must not be copied into tasks/active-task.md.

## Implementation Notes
Validator must treat source_section as a forbidden singular key.
Validator must fail if source_section: exists anywhere in frontmatter or body model.
This failure must be reported separately from missing source_sections.

Forbidden authority claim detection must target positive authority claims only.
Negative boundary statements such as "does not authorize implementation", "does not authorize execution", and "must not be copied into tasks/active-task.md" must not fail validation.

## What Validator Must Not Do
The validator must not:
- create task drafts;
- create task contract proposals;
- create executable task contracts;
- write to `tasks/active-task.md`;
- write to `tasks/queue/`;
- authorize implementation;
- authorize execution.

## Known Limitations
The validator uses deterministic text and regex checks.
It does not fully parse markdown semantics.
It validates structure and boundary constraints only.

## Non-Authority Boundary
UX-to-Task Proposal Validator is not task generation.
UX-to-Task Proposal Validator is not implementation approval.
UX-to-Task Proposal Validator does not create task drafts.
UX-to-Task Proposal Validator does not create task contract proposals.
UX-to-Task Proposal Validator does not create executable tasks.
UX-to-Task Proposal Validator does not create authorized task contracts.
UX-to-Task Proposal Validator does not authorize task generation.
UX-to-Task Proposal Validator does not authorize implementation.
UX-to-Task Proposal Validator does not authorize execution planning.
UX-to-Task Proposal Validator does not authorize commit, push, merge, deploy, or release.
UX-to-Task Proposal Validator may validate proposal structure only.
Future executable task contracts require separate human authorization.

## Summary
This validator enforces non-executable proposal structure and boundary rules.
It is read-only and fails closed for missing data, invalid structure, and authority-claim violations.
