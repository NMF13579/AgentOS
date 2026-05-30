# Docs-to-Code Candidates
## M68.1 Boundary
This map is an M68.1 planning and review artifact.
This map does not authorize cleanup, deletion, compression, consolidation, or docs-to-code conversion.
This map does not create approval.
This map does not create lifecycle mutation.
This map does not complete M68.
Human review remains required before M68.2.

## Active Task Record
- active_task_id: task-68.1

## Inputs Used
- reports/m68-docs-to-code-drift.json
- reports/m68-inventory.json
- reports/m68-duplicates.json
- reports/m68-owner-gaps.json
- reports/m68-protected-artifacts.json
- reports/m68-prompt-metrics.json
- reports/m68-repo-raw-inventory.md

## Candidate Selection Rules
- Rule must be stable (не меняется случайно между запусками).
- Rule must be deterministic (одинаковый вход → одинаковый результат).
- Rule must be repeatable and fixture-testable (можно проверить на тест-наборах).

## Non-Candidate Rules
- Не включать философию AgentOS, стратегию, архитектурные объяснения и человеческие решения.
- Не включать “почему PASS не approval” как код-правило: это управленческая граница, не детерминированный чек.

## Inventory Freshness Check Candidates
- Validate presence of `generated_at` and scan timestamp fields.
- Track stale inventory age thresholds as explicit candidate checks.

## Duplicate / Backup Filename Check Candidates
- Reuse categories from `m68-duplicates.json`.
- Candidate checks for copy/backup/numbered/cache naming patterns.

## Owner Gap Check Candidates
- Check CODEOWNERS existence and placeholder markers.
- Verify no obvious owner coverage gaps for protected artifacts.

## Protected Artifact Presence Check Candidates
- Check required M61–M67 protected paths are present.
- Candidate includes file/directory type and optional hash presence.

## Idle-State Format Check Candidates
- Detect `No active task yet` / `status: none` text patterns in task-related files.

## Task Ledger vs Reports Sync Check Candidates
- Candidate rule for sync between active task ID and report references.
- Candidate rule for scan-generated artifacts freshness.

## Adapter Drift Check Candidates
- Candidate scan based on adapter keyword/path signal counts.

## Workflow Permissions Check Candidates
- Candidate pattern checks for permission-related workflow drift.

## Large Generated Artifact Policy Check Candidates
- Candidate thresholds for large generated files under `reports/`.

## Final Status Validation Candidates
- Candidate parser/checker for allowed `FINAL_STATUS` tokens per artifact type.

## Readiness Field Validation Candidates
- Candidate checks for forbidden readiness claims in non-authority artifacts.

## Non-Authority Boundary Validation Candidates
- Candidate checks for required non-authority disclaimers in generated review maps.

## Forbidden Approval / Completion Claim Candidates
- Candidate rules to flag `APPROVED`, `CAN_DELETE`, `CAN_DEPRECATE`, similar terms.

## Forbidden Mxx Auto-Start Claim Candidates
- Candidate rules to flag automatic-start statements for later milestones.

## Candidate Priority Summary
- High: status/readiness/approval claim checks, protected artifact presence checks.
- Medium: duplication filename checks, workflow permission drift checks.
- Medium: owner placeholder checks, inventory freshness checks.
- Lower: style-level repeated narrative blocks that need human interpretation.

## Explicit Non-Implementation Boundary
M68.1 identifies docs-to-code candidates only.
M68.1 does not implement validators.
M68.1 does not decide final M71 scope.

## Final Status
FINAL_STATUS: M68_DOCS_TO_CODE_CANDIDATES_COMPLETE_WITH_WARNINGS
