# Agent Evidence Claim Boundary

## 1. Purpose
Определить точную границу утверждений (claims) в agent evidence: что разрешено утверждать, что запрещено, что остаётся в зоне ответственности человека и следующих этапов.

claim_boundary_scope: agent_task_output_evidence_claim_boundary
schema_path: schemas/agent-task-output-evidence.schema.json
contract_path: docs/AGENT-TASK-OUTPUT-EVIDENCE-CONTRACT.md
integrity_rules_path: docs/AGENT-EVIDENCE-INTEGRITY-RULES.md
integrity_rules_available: true
defines_exact_claim_boundary: true
defines_forbidden_claim_inventory: true
forbidden_claim_inventory_grouped_by_category: true
defines_safe_context_rules: true
defines_required_non_authority_statements: true
defines_evidence_checker: false
defines_evidence_fixtures: false
defines_acceptance_criteria_checker: false
defines_unified_runner: false
defines_false_pass_suite: false
integrates_completion_gate: false
approves_task_completion: false
human_review_required: true

## 2. M64 Position in the Roadmap
M64 задаёт границы безопасных claims в evidence.
M65 проверяет критерии приёмки.
M66 объединяет слои в единый запуск.
M67 усиливает устойчивость к ложному PASS и completion gate.

## 3. Evidence Claim Boundary Purpose
Agent evidence may describe what the agent claims it did.
Agent evidence must not approve what the agent did.
Agent evidence must not complete the task.
Agent evidence must not disable human review.
Human review remains required.

## 4. Allowed Evidence Claims
Допустимы только evidence-level claims:
- task_id referenced
- task brief path referenced
- agent identity declared
- files_changed claimed
- created_artifacts claimed
- modified_artifacts claimed
- deleted_artifacts claimed
- commands_run claimed
- validation_results claimed
- known_limitations disclosed
- warnings disclosed
- blockers disclosed
- forbidden_actions_performed declared false
- human_review_required declared true
- non_authority_boundary preserved

Allowed evidence claims are still agent claims.
Allowed evidence claims must be checked, not trusted.
Allowed evidence claims do not prove task completion.
Allowed evidence claims do not replace human review.

## 5. Forbidden Evidence Claim Categories
Ниже категории запрещённых claims: смысл, причина запрета, пример, ожидаемый mapping.

- approval claims: выдают одобрение задачи. Запрещены, потому что approval не в зоне evidence. Пример: "task approved". Mapping: clear affirmative -> M64_EVIDENCE_CHECK_BLOCKED; ambiguous outside safe context -> M64_EVIDENCE_CHECK_PASS_WITH_WARNINGS; safe context mention -> not blocker by itself.
- task completion claims without human review: заявляют завершение без ручной проверки. Пример: "completed without review". Mapping аналогичный.
- human review bypass claims: отключают/обходят ручную проверку. Пример: "human review not required". Mapping аналогичный.
- merge authorization claims: Пример "merge authorized". Mapping аналогичный.
- push authorization claims: Пример "push authorized". Mapping аналогичный.
- release authorization claims: Пример "release authorized". Mapping аналогичный.
- deployment authorization claims: Пример "deployment authorized". Mapping аналогичный.
- lifecycle mutation claims: Пример "lifecycle mutated". Mapping аналогичный.
- completion gate claims: Пример "completion gate passed". Mapping аналогичный.
- production task acceptance gate claims: Пример "production task acceptance gate passed". Mapping аналогичный.
- downstream milestone start claims: Пример "M65 started automatically". Mapping аналогичный.
- acceptance criteria satisfaction claims as final authority: Пример "acceptance criteria approved". Mapping аналогичный.
- false production readiness claims: Пример "ready for production". Mapping аналогичный.

Это описание политики, не реализация кода.

## 6. Exact Forbidden Claim Inventory
Это initial boundary inventory, сгруппированный по категориям.

Approval claims:
- approved
- approval granted
- task approved
- task is approved
- task completion approved
- acceptance criteria approved
- task accepted by system
- auto-approved
- auto approval

Human review bypass claims:
- complete without review
- completed without review
- human review not required
- human_review_required: false
- review not required

Merge / push / release / deployment claims:
- merged
- merge completed
- merge authorized
- push authorized
- pushed
- release authorized
- released
- deployment authorized
- deployed

Lifecycle mutation claims:
- lifecycle mutated
- lifecycle state mutated

Completion gate / production gate claims:
- completion gate passed
- production task acceptance gate passed
- production ready
- ready for production

Downstream milestone claims:
- M65 started automatically
- M66 started automatically
- M67 started automatically

This inventory is a boundary inventory, not checker implementation code.
64.5 implements deterministic detection behavior.
64.6 creates fixtures that test representative claims.
M67 later expands false PASS resistance across the full pipeline.

## 7. Safe-Context Rules
Safe contexts:
- forbidden claim inventory
- forbidden examples
- non-authority boundary statements
- policy declarations
- negative fixture descriptions
- claim boundary documentation

Правила:
- Фраза из forbidden inventory в safe context сама по себе не affirmative claim.
- Вне safe context такая фраза считается подозрительной.
- Чёткий affirmative claim вне safe context должен блокировать.
- Неоднозначный случай вне safe context не может дать clean PASS.

Safe examples:
- "Agent evidence must not claim task approved."
- "Forbidden claim example: merge authorized."
- "Human review not required is a forbidden claim."

Unsafe examples:
- "Task approved."
- "Merge authorized."
- "Human review not required."
- "Completion gate passed."

## 8. Approval Boundary
Agent evidence cannot approve task results.
Agent evidence cannot imply approval.
Agent evidence cannot record approval granted by itself.
Agent evidence cannot convert validation result into approval.

Evidence PASS is not approval.
Evidence PASS_WITH_WARNINGS is not approval.
Evidence NOT_ENOUGH_EVIDENCE is not approval.
Evidence BLOCKED is not approval.
Only explicit human approval can approve a task.

## 9. Completion Boundary
Agent evidence cannot complete the task.
Agent evidence cannot declare task completion accepted.
Agent evidence cannot claim completion review has passed.
Agent evidence cannot claim task lifecycle was mutated.

Forbidden examples:
- task completed
- completion accepted
- completion review passed
- lifecycle mutated
- task moved to completed

Allowed safe statement:
Agent evidence may state that the agent claims it finished its work, but this is not task completion approval.

Разделение:
- agent says work is done = claim
- AgentOS evidence checker passes = validation result
- human approves completion = separate authority

## 10. Human Review Boundary
human_review_required must remain true.
Agent evidence cannot disable human review.
Agent evidence cannot declare review unnecessary.
Agent evidence cannot replace manual review.
Agent evidence cannot bypass human approval.

Human review remains required.
Agent evidence does not replace human review.
Agent evidence cannot set human_review_required to false.
Agent evidence cannot claim human review is not required.

Любая попытка bypass human review должна мапиться в `M64_EVIDENCE_CHECK_BLOCKED`.
Это политика документа 64.4; реализация будет в 64.5.

## 11. Merge / Push / Release Boundary
Agent evidence cannot authorize merge.
Agent evidence cannot authorize push.
Agent evidence cannot authorize release.
Agent evidence cannot authorize deployment.
Agent evidence cannot claim these operations already occurred as an approved outcome.

Forbidden examples:
- merge authorized
- push authorized
- release authorized
- deployment authorized
- merged
- pushed
- released
- deployed

Agent evidence does not authorize merge, push, or release.

## 12. Lifecycle Mutation Boundary
Agent evidence cannot mutate lifecycle state.
Agent evidence cannot claim lifecycle mutation was performed.
Agent evidence cannot claim controlled completion was applied.
Agent evidence cannot claim task state moved forward.

Forbidden examples:
- lifecycle mutated
- task state updated to complete
- controlled completion applied
- completion gate passed

Agent evidence does not mutate lifecycle state.

## 13. Downstream Milestone Boundary
Agent evidence cannot start M65/M66/M67.
Agent evidence cannot claim downstream milestone completion.
Agent evidence cannot absorb downstream responsibility.

Forbidden examples:
- M65 started automatically
- M66 started automatically
- M67 started automatically
- acceptance criteria checker created
- unified runner created
- false PASS resistance suite created
- completion gate integration created

M64 evidence claim boundary does not create M65 acceptance criteria checking.
M64 evidence claim boundary does not create M66 unified runner.
M64 evidence claim boundary does not create M67 false PASS resistance.

## 14. Required Non-Authority Statements
Required statements for agent evidence:
- Agent evidence is not approval.
- Agent evidence does not complete the task.
- Agent evidence does not replace human review.
- Agent evidence does not authorize merge, push, or release.
- Human review remains required.

Recommended extended statements:
- Agent evidence does not mutate lifecycle state.
- Agent evidence does not start downstream milestones.
- Agent evidence does not validate completed agent tasks as a production gate.
- Agent evidence must be checked, not trusted.

## 15. Claim Detection Safety Rules
- Do not treat field names as affirmative claims by themselves.
- Do not treat non-authority boundary text as affirmative claims by itself.
- Do not treat forbidden examples as affirmative claims by themselves.
- Inspect string values recursively when implementing claim detection.
- Object keys are not affirmative claims by themselves.
- Ambiguous forbidden claims must not produce clean PASS.
- Clear affirmative forbidden claims must block.

Checker code в этой задаче не создаётся.

## 16. Relationship to 64.3 Integrity Rules
64.3 defines evidence integrity decision semantics.
64.4 defines exact evidence claim boundary.

Связь:
- 64.3 maps unsafe claims to BLOCKED or PASS_WITH_WARNINGS.
- 64.4 defines which claims are unsafe.
- 64.5 implements detection based on 64.3 and 64.4.

integrity_rules_available: true

## 17. Relationship to 64.5 Evidence Checker
64.5 implements evidence checker behavior.
64.4 provides the claim inventory and boundary rules for that checker.
This task does not create `scripts/check-agent-task-evidence.py`.
This task does not create `docs/AGENT-TASK-EVIDENCE-CHECKER.md`.

## 18. Relationship to 64.6 Fixtures
64.6 creates fixtures for valid and invalid evidence claim cases.
64.4 does not create fixtures.

Representative future fixture cases:
- approval-claim-present
- human-review-disabled
- merge-authorized-claim-present
- completion-gate-passed-claim
- safe-forbidden-policy-terms

## 19. Relationship to M65-M67
M65 will define acceptance criteria checking.
M66 will define unified agent task validation runner.
M67 will define full false PASS resistance and completion gate integration.

Разделение:
- M64 claim boundary prevents unsafe evidence claims.
- M65 checks whether task requirements were satisfied.
- M66 combines validation layers into one runner.
- M67 tests full pipeline false PASS resistance.

## 20. Non-Authority Boundary
M64 evidence claim boundary is not approval.
M64 evidence claim boundary does not replace human review.
M64 evidence claim boundary does not complete M64.
M64 evidence claim boundary does not start M65.
M64 evidence claim boundary does not validate completed agent tasks as a production gate.
M64 evidence claim boundary does not prove task completion.
M64 evidence claim boundary does not prove command execution authenticity.
M64 evidence claim boundary does not prove acceptance criteria satisfaction.
M64 evidence claim boundary does not create the evidence checker.
M64 evidence claim boundary does not create evidence fixtures.
M64 evidence claim boundary does not define acceptance criteria checking.
M64 evidence claim boundary does not create the unified agent task validation runner.
M64 evidence claim boundary does not create the false PASS resistance suite.
M64 evidence claim boundary does not integrate the completion gate.
M64 evidence claim boundary does not approve any agent task result.
M64 evidence claim boundary does not authorize merge, push, or release.
Human review remains required.

## 21. Final Status
FINAL_STATUS: M64_EVIDENCE_CLAIM_BOUNDARY_DEFINED_WITH_WARNINGS
