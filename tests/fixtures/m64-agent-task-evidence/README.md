# M64 Agent Task Evidence Fixtures

## 1. Purpose
Набор входных данных для проверки `scripts/check-agent-task-evidence.py` на позитивных, warning, негативных и malformed случаях.

fixture_scope: agent_task_output_evidence_checker
checker_path: scripts/check-agent-task-evidence.py
expected_results_manifest: tests/fixtures/m64-agent-task-evidence/expected-results.json
creates_evidence_fixtures: true
modifies_evidence_checker: false
defines_acceptance_criteria_checker: false
defines_unified_runner: false
defines_false_pass_suite: false
integrates_completion_gate: false
approves_task_completion: false
human_review_required: true

## 2. Fixture Scope
M64 fixtures test evidence model/checker behavior.
M64 fixtures do not test full task acceptance.
M64 fixtures do not test unified runner behavior.
M64 fixtures do not test completion gate behavior.
M64 fixtures are not the M67 false PASS resistance suite.

## 3. Directory Structure
- `positive/`
- `warning/`
- `negative/`
- `malformed/`
- `expected-results.json`

## 4. Expected Result Values
- `M64_EVIDENCE_CHECK_PASS`
- `M64_EVIDENCE_CHECK_PASS_WITH_WARNINGS`
- `M64_EVIDENCE_CHECK_BLOCKED`
- `M64_EVIDENCE_CHECK_NOT_ENOUGH_EVIDENCE`

## 5. Positive Fixtures
- `valid-minimal-evidence.json`
- `valid-evidence-safe-forbidden-policy-terms.json`

## 6. Warning Fixtures
- `valid-evidence-with-warnings.json`
- `validation-results-without-commands-run.json`
- `created-artifact-claim-without-files-changed.json`
- `modified-artifact-claim-without-files-changed.json`
- `deleted-artifact-claim-without-files-changed.json`
- `hidden-blocker-as-warning.json`
- `mixed-pass-and-unknown-command.json`

## 7. Negative Fixtures
- `missing-required-field.json`
- `unsupported-contract-version.json`
- `wrong-evidence-type.json`
- `task-id-mismatch.json`
- `missing-agent-identity.json`
- `empty-agent-identity.json`
- `human-review-disabled.json`
- `forbidden-actions-performed.json`
- `approval-claim-present.json`
- `merge-authorized-claim-present.json`
- `completion-gate-passed-claim.json`
- `missing-non-authority-boundary.json`
- `missing-required-boundary-statement.json`
- `wrong-required-field-type.json`
- `numeric-boolean-human-review.json`
- `hidden-blocker-as-blocked.json`
- `required-command-failed.json`
- `required-validation-failed.json`
- `not-enough-evidence.json`
- `m65-m67-scope-absorption.json`

## 8. Malformed Fixtures
- `malformed-evidence-json.json` (намеренно сломан JSON)

## 9. Expected Results Manifest
`expected-results.json` задаёт ожидаемые result/exit-code для каждого fixture.

## 10. How to Run
Пример:
```bash
python3 scripts/check-agent-task-evidence.py \
  --evidence tests/fixtures/m64-agent-task-evidence/positive/valid-minimal-evidence.json \
  --json
```

Полная проверка по manifest выполняется скриптом в шаге валидации задачи.

## 11. Relationship to 64.5 Evidence Checker
64.6 использует checker как есть.
64.6 не меняет checker поведение.

## 12. Relationship to M67 False PASS Resistance
Эти fixtures покрывают только M64 evidence-checker уровень.
Полный false PASS resistance suite принадлежит M67.

## 13. Human Review Boundary
Human review remains required.
Fixtures не дают права на approval и не заменяют ручную проверку.

## 14. Non-Authority Boundary
M64 evidence fixtures are not approval.
M64 evidence fixtures do not replace human review.
M64 evidence fixtures do not validate completed agent tasks as a production gate.
M64 evidence fixtures are not the M67 false PASS resistance suite.
Human review remains required.

## 15. Final Status
FINAL_STATUS: M64_EVIDENCE_FIXTURES_COMPLETE_WITH_WARNINGS
