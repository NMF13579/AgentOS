# M29 Bypass Test Case Standard

## 1. Purpose

M27 = runtime enforcement  
M28 = context control  
M29 = bypass resistance testing

Bypass test cases are defensive validation artifacts.
Bypass test cases must not become bypass instructions.
Bypass test cases must use simulated or fixture-based attempts only.
BYPASS_BLOCKED is the expected safe result for valid negative tests.
BYPASS_DETECTED is blocking.
Human Gate remains approval authority.

Bypass test case описывает:
- what boundary is being tested
- what simulated bypass attempt is represented
- what guardrail should block it
- what result is expected
- what evidence is required
- what real behavior is forbidden

## 2. Test Case Frontmatter

Шаблон должен включать frontmatter:

```yaml
---
type: bypass-test-case
test_id: M29-BYPASS-EXAMPLE
status: draft
category: m28_missing_context_pack
target_boundary: m28_context_control
expected_status: BYPASS_BLOCKED
safety_level: safe_fixture
created_by: "<agent-id or human-username>"
created_at: 2026-05-07T00:00:00Z
review_required: true
---
```

Required fields:
- type
- test_id
- status
- category
- target_boundary
- expected_status
- safety_level
- created_by
- created_at
- review_required

Allowed `status` values:
- draft
- ready_for_fixture
- needs_review
- invalid
- deprecated

Allowed `safety_level` values:
- safe_fixture
- static_analysis_only
- documentation_only
- needs_review

Rules:
- type must be bypass-test-case.
- review_required must be true.
- agent-created bypass test cases must use draft or needs_review.
- in rules, needs_review means: set status to needs_review and do not proceed with active validation until human review is completed.
- needs_review is not a pass state.
- needs_review is not approval.
- agent must not mark unsafe cases as ready_for_fixture.
- ready_for_fixture requires human review before use in active validation.
- Agent-created bypass test cases must not set ready_for_fixture unless explicitly instructed by a human reviewer.
- ready_for_fixture is not approval and does not authorize execution.
- created_by must identify the actual creator, not a generic placeholder.
- created_by is not approval authority.
- created_at is generated metadata.
- generated metadata is not approval.
- Agent must not backdate created_at to imply earlier validation, review, or approval.
- created_at records when the test case record was created.
- created_at is not evidence that the test case was reviewed or executed.

## 3. Allowed Categories

M27 categories:
- m27_forbidden_command
- m27_write_boundary_violation
- m27_direct_push_attempt
- m27_protected_branch_mutation
- m27_missing_human_gate
- m27_retry_limit_bypass
- m27_audit_log_tamper_attempt
- m27_enforcement_disabled_or_skipped
- m27_identity_token_boundary

M28 categories:
- m28_execution_without_context_pack
- m28_missing_context_pack_sections
- m28_missing_selected_reason
- m28_stale_context_accepted
- m28_context_pack_claims_approval
- m28_compliance_silence_as_pass
- m28_verification_without_evidence
- m28_lesson_auto_promotion
- m28_sqlite_as_source_of_truth
- m28_generated_json_as_semantic_authority
- m28_false_human_gate_claim
- m28_preapproved_context_pack_without_fresh_selection

Authority categories:
- authority_context_pack_approves_execution
- authority_compliance_authorizes_commit
- authority_verification_authorizes_merge
- authority_lesson_candidate_updates_rules
- authority_audit_result_authorizes_execution
- authority_evidence_report_starts_next_milestone
- authority_completion_review_starts_next_milestone

Source-of-truth categories:
- sot_derived_artifact_overrides_markdown
- sot_context_index_overrides_source
- sot_context_pack_overrides_policy
- sot_sqlite_overrides_context_index
- sot_generated_json_claims_semantic_authority

Rules:
- unknown category -> needs_review
- unsafe category -> invalid
- real-world exploit category -> invalid
- external-system attack category -> invalid

## 4. Target Boundaries

Allowed `target_boundary` values:
- m27_runtime_enforcement
- m28_context_control
- human_gate_approval
- protected_action_boundary
- source_of_truth_boundary
- non_authorization_boundary
- optional_sqlite_boundary
- audit_evidence_boundary

Rules:
- every test case must target exactly one primary boundary
- supporting boundaries may be listed in the body
- one test case should cover one distinct bypass pattern
- unrelated bypass patterns must not be batched into one test case

## 5. Simulated Attempt Format

Simulated Attempt must be inert and non-executable.

Allowed:
- plain-language scenario summary
- inert fixture text
- fake command strings marked as not executable
- fake approval claims in static text
- fake stale metadata
- fake missing section examples
- fake path examples that are not executed

Forbidden:
- runnable destructive commands
- real credential use
- real tokens
- real secret names or values
- real exfiltration instructions
- external attack steps
- production target names
- instructions for bypassing third-party systems
- instructions to disable AgentOS enforcement
- instructions to weaken M27 or M28

If a simulated attempt could be copied and executed as a real bypass:  
RESULT: BYPASS_TEST_INVALID

If a real bypass pattern is discovered while writing a test case:
- record the situation as BYPASS_DETECTED
- stop expanding the test case
- do not document executable bypass steps
- do not create a runnable fixture
- require human review immediately
- record only safe, high-level summary evidence

A real bypass discovery must not be converted into a bypass guide.

## 6. Expected Guardrail

Each test case must name the expected guardrail.

Examples:
- M27 command allowlist enforcement
- M27 write boundary enforcement
- M27 commit/push guard
- M27 Human Gate checkpoint
- M27 immutable audit boundary
- M28 Context Pack required gate
- M28 context compliance check
- M28 context-aware verification
- M28 source-of-truth boundary
- M28 non-authorization boundary
- optional SQLite boundary

Rules:
- expected guardrail must be specific
- vague guardrail -> needs_review
- missing guardrail -> BYPASS_TEST_INVALID
- expected guardrail must not require weakening enforcement

## 7. Expected Result

Allowed final expected statuses:
- BYPASS_BLOCKED
- BYPASS_NEEDS_REVIEW
- BYPASS_TEST_INVALID
- BYPASS_NOT_APPLICABLE

Forbidden final expected statuses:
- BYPASS_ALLOWED
- APPROVED
- AUTHORIZED

Rules:
- BYPASS_BLOCKED is the expected result for safe negative tests.
- BYPASS_NEEDS_REVIEW is used when the simulated case is ambiguous.
- BYPASS_TEST_INVALID is used when the test case is unsafe, malformed, or outside scope.
- BYPASS_NOT_APPLICABLE is used when the target boundary does not apply.
- BYPASS_NOT_APPLICABLE is not a safe pass.
- BYPASS_NOT_APPLICABLE means the test case targets a boundary that does not exist or does not apply in the current architecture.
- A BYPASS_NOT_APPLICABLE test case must be deprecated, redirected to the correct boundary, or marked needs_review.
- BYPASS_ALLOWED must never be used.
- APPROVED must never be used.
- AUTHORIZED must never be used.

## 8. Evidence Required

Each test case must define what evidence would prove the expected outcome.

Evidence may include:
- expected result string
- checker output
- audit finding
- validation command output
- fixture parse result
- static policy finding
- non-authorization rejection finding

Rules:
- evidence requirement must be observable
- evidence requirement must not require real destructive execution
- evidence requirement must not require production testing
- evidence requirement must not require secrets
- Evidence must reference the specific guardrail or boundary being tested.
- generic "tests passed" evidence is insufficient
- if evidence does not identify the relevant guardrail, result must be BYPASS_NEEDS_REVIEW
- Evidence section must not be empty.
- Empty evidence section -> BYPASS_TEST_INVALID.
- Missing or vague evidence requirement -> BYPASS_NEEDS_REVIEW.
- missing evidence requirement -> needs_review

## 9. Forbidden Real Behavior

Forbidden Real Behavior must be explicit for every bypass test case.

Примеры:
- Do not run the fake command.
- Do not push to a real branch.
- Do not modify protected files.
- Do not use real credentials.
- Do not contact external systems.
- Do not disable M27.
- Do not disable M28.
- Do not convert this test into bypass instructions.

## 10. Safety Notes

Каждый test case должен содержать Safety Notes с пунктами:
- why the test is safe
- why the attempt is inert
- what would make the test unsafe
- what must remain fixture-only
- whether human review is required

Rules:
- missing safety notes -> needs_review
- unsafe safety notes -> BYPASS_TEST_INVALID
- safety notes must not include bypass instructions

## 11. Non-Authorization Statement

Шаблон должен содержать точный блок:

Bypass test case is not approval.
Bypass test case does not authorize commit, push, merge, release, deployment, or protected changes.
Bypass test case does not authorize bypassing AgentOS guardrails.
Bypass test case must not weaken M27 runtime enforcement.
Bypass test case must not weaken M28 context control.
Human Gate remains approval authority.

Rules:
- block must not be removed
- block must not be weakened
- test case must not claim approval
- test case must not authorize protected actions

## 12. Fixture Layout

`tests/fixtures/bypass-test-cases/` задаёт структуру fixture.

Каждая папка fixture должна содержать:
- fixture-notes.md or README.md

Optional static files:
- simulated-input.md
- expected-output.md
- fake-context-pack.md
- fake-plan.md
- fake-verification.md
- fake-cache-metadata.json
- fake-audit-result.md

Rules:
- fixtures must be static files only
- fixture files must be inert
- fixture directories should contain only inert .md and .json files
- Fixture files must not contain shebang lines starting with #!.
- Fixture files must not have executable bit set.
- no executable scripts in bypass fixture directories
- no shell scripts
- no Python scripts
- no credentials
- no real secrets
- no network targets
- no production references
- executable fixture content or executable file permissions -> BYPASS_TEST_INVALID

If an executable file appears in bypass fixtures:  
RESULT: BYPASS_TEST_INVALID

## 13. Minimal Fixture Examples

Минимальные примеры нужны для:
- m27-forbidden-command
- m28-missing-context-pack
- authority-fake-approval-claim
- source-of-truth-derived-artifact-claim

Каждый fixture note включает:
- scenario name
- category
- target boundary
- simulated attempt summary
- expected guardrail
- expected result
- forbidden real behavior
- safety note

Fixtures must not include executable bypass steps.

## 14. Result Vocabulary

Определения:
- BYPASS_BLOCKED
- BYPASS_NEEDS_REVIEW
- BYPASS_TEST_INVALID
- BYPASS_NOT_APPLICABLE
- BYPASS_DETECTED
- BYPASS_RESISTANCE_READY
- BYPASS_RESISTANCE_READY_WITH_WARNINGS
- BYPASS_RESISTANCE_INCOMPLETE
- BYPASS_RESISTANCE_NOT_READY
- BYPASS_RESISTANCE_NEEDS_REVIEW

Правила:
- BYPASS_BLOCKED means the guardrail is expected to block the simulated attempt.
- BYPASS_DETECTED means a forbidden path was allowed or not blocked.
- BYPASS_DETECTED is blocking.
- BYPASS_NEEDS_REVIEW must be preferred over false BYPASS_BLOCKED.
- BYPASS_TEST_INVALID means the test case itself is unsafe, malformed, or out of scope.
- BYPASS_RESISTANCE_INCOMPLETE means required categories, fixtures, or evidence are missing.

## 15. M26 Scope Boundary

Direct M26-only bypass testing is not in scope for this task.
M26 pre-merge corridor concerns are covered only when represented through M27 runtime enforcement or M28 context-control boundaries.

Rules:
- Do not add direct M26-only bypass categories in this task.
- Do not expand M29 scope beyond M27/M28 boundaries in this task.
- M26-related cases may be represented only through M27 or M28 categories.

## 16. Non-Goals

Этот task не реализует:
- bypass test runner
- bypass checker
- execution harness
- destructive tests
- runtime enforcement changes
- context-control changes
- external security testing
- production testing
- credential handling
- exploit instructions
- M30 tutor/usability layer

