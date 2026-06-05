# Acceptance Criteria Check Package Contract

## 1. Purpose
This document defines the structured input package for the M65 acceptance criteria checker.

## 2. Scope
65.2 defines input structure.
65.2 does not define final decision semantics.
65.2 does not implement checker.

## 3. Architecture Boundary
M65 checker must not infer full task meaning from free-form Markdown.
M65 checker must operate on structured acceptance criteria package.

## 4. Package Overview
Top-level fields:
- `contract_version`
- `package_type`
- `task_id`
- `task_brief_path`
- `acceptance_criteria`
- `expected_artifacts`
- `actual_artifacts`
- `changed_files`
- `evidence_result`
- `validation_outputs`
- `known_limitations`
- `warnings`
- `blockers`
- `human_review_required`
- `non_authority_boundary`

## 5. Acceptance Criteria Object
Each `acceptance_criteria` item requires:
- `criterion_id`
- `description`
- `required`
- `check_method`
- `expected_evidence`
- `notes`

Allowed `check_method` values:
- `artifact_presence`
- `validation_output`
- `declared_change`
- `manual_review_required`

Example:
```json
{
  "criterion_id": "AC-1",
  "description": "Required artifact exists",
  "required": true,
  "expected_evidence": ["docs/example.md"],
  "check_method": "artifact_presence",
  "notes": ""
}
```

## 6. Artifact Objects
`expected_artifacts` and `actual_artifacts` use object fields:
- required: `path`, `artifact_type`, `required`
- optional: `description`, `exists`, `source`

Allowed `artifact_type` values:
- `document`
- `schema`
- `script`
- `fixture`
- `report`
- `directory`
- `other`

## 7. Changed Files
`changed_files` supports:
- non-empty string path
- object form with `path` and `change_type`

Allowed `change_type` values:
- `created`
- `modified`
- `deleted`
- `renamed`
- `unknown`

## 8. Evidence Result
`evidence_result` requires:
- `source_path`
- `result`

Allowed `result` values:
- `M64_EVIDENCE_CHECK_PASS`
- `M64_EVIDENCE_CHECK_PASS_WITH_WARNINGS`
- `M64_EVIDENCE_CHECK_BLOCKED`
- `M64_EVIDENCE_CHECK_NOT_ENOUGH_EVIDENCE`
- `UNKNOWN`

Evidence result is a validation signal from M64.
Evidence result is not approval.
Evidence result is not proof that all acceptance criteria are satisfied.

## 9. Validation Outputs
Each `validation_outputs` item requires:
- `name`
- `command`
- `result`

Allowed `result` values:
- `PASS`
- `PASS_WITH_WARNINGS`
- `FAIL`
- `BLOCKED`
- `NOT_RUN`
- `UNKNOWN`

Optional fields:
- `exit_code`
- `output_path`
- `correlates_to_criteria`
- `notes`

## 10. Human Review Boundary
`human_review_required` must be true.
Acceptance criteria check package is not approval.
Acceptance criteria check package does not complete the task.
Human review remains required.

## 11. Forbidden Fields and Claims
The package must not contain fields or claims asserting:
- `approved`
- `task_complete`
- `completion_authorized`
- `completion_gate_passed`
- `merge_authorized`
- `push_authorized`
- `release_authorized`
- `production_ready`
- `human_review_not_required`

Full forbidden claim detection belongs to 65.4 and 65.5.

## 12. Boolean Strictness
true and false must be JSON booleans.
1 and 0 must not be accepted as boolean substitutes.

## 13. Invalid Package Handling
Missing top-level required field must make the package invalid.
Wrong-typed top-level required field must make the package invalid.
Missing or wrong-typed required fields inside a criterion must later map to M65_ACCEPTANCE_CHECK_BLOCKED.
Empty acceptance_criteria must make the package invalid.
human_review_required false must make the package invalid and later BLOCKED.

`check_method: manual_review_required` is valid, but manual-review-required criteria cannot produce automated clean PASS by structure alone.
Decision handling belongs to 65.3 and checker behavior belongs to 65.5.

## 14. Relationship to Later Tasks
65.3 defines decision semantics and priority order.
65.4 defines claim boundary.
65.5 implements checker behavior.
65.6 creates fixtures.
65.7 validates integration.
65.8 reviews actions.
65.9 collects evidence.
65.10 closes M65.

## 15. Final Status
FINAL_STATUS: M65_ACCEPTANCE_CRITERIA_CONTRACT_DEFINED_WITH_WARNINGS
