# M30 Enforced RAG-Light Pipeline

## 1. Purpose

M28 created RAG-light.
M30 enforces RAG-light.
M30 enforces context freshness and context compliance.
M30 does not grant approval.
M30 does not replace Human Gate.
M30 does not replace M27 runtime enforcement.
M30 does not bypass M29 bypass-resistance boundaries.
Human Gate remains approval authority.

M27 = runtime enforcement  
M28 = context control  
M29 = bypass resistance testing  
M30 = enforced RAG-light context pipeline

## 2. Core Pipeline

Docs changed
↓
Context Index Freshness Gate
↓
Required Context Pack Gate
↓
Context Compliance Required Gate
↓
Unified Context Pipeline Check
↓
CI Required Check
↓
Evidence Report
↓
Completion Review

- Markdown/YAML source files are semantic source of truth.
- data/context-index.json is generated navigation.
- reports/context-pack.md is task-specific selected context.
- reports/context-selection-record.md is audit evidence.
- reports/context-verification.md is verification evidence.
- SQLite cache is optional and rebuildable.
- SQLite is not source of truth.

Markdown/YAML = meaning  
JSON = navigation  
SQLite = speed  
Context Pack = task-applicable context  
Verification = compliance evidence

## 3. Enforced Guarantees

- stale context-index cannot silently pass
- missing context-index cannot silently pass
- missing Context Pack cannot silently pass
- stale Context Pack cannot silently pass
- Context Pack without selected reasons cannot silently pass
- plan silence on selected required context cannot silently pass
- verification silence on selected context cannot silently pass
- skipped validation cannot be reported as pass
- Context Pack cannot be treated as approval
- SQLite cannot be treated as source of truth

- Markdown/YAML changed + stale context-index = blocked.
- No valid Context Pack -> No Context-Compliant Execution.
- Silence is not compliance.
- Command success does not override context violation.
- Skipped validation is not passed validation.
- Context Pack is not approval.
- SQLite freshness must not override Markdown/YAML or data/context-index.json freshness.
- SQLite being newer than JSON does not make SQLite authoritative.
- SQLite stale or fresh state must never replace the committed context-index freshness check.

## 4. Context Index Freshness Gate

- data/context-index.json is generated but committed.
- CI may rebuild index and compare with committed version.
- Diff after rebuild means stale index.
- Stale index must not be treated as ready.
- Gate fails when index is missing, stale, invalid, absolute-path based, schema-violating, or claims semantic authority.
- If the context index generator script is missing, the gate must fail with INCOMPLETE, not skip silently.
- A freshness gate cannot be considered enforceable unless the index can be regenerated or deterministically checked.

Markdown/YAML changed + context-index not updated = CI fail.

## 5. Required Context Pack Gate

- Gate fails, blocks, or requires review when Context Pack is missing, stale, mismatched, incomplete, or claims approval.
- context_index_hash in Context Pack must match the hash of the currently committed data/context-index.json.
- context_index_hash in Context Pack must match.
- Mismatch means stale Context Pack and must produce blocked or needs_review behavior.
- Task mismatch, missing selected reasons, missing checklist, missing non-authorization block, and missing source references are violations.

No valid Context Pack -> No Context-Compliant Execution.

## 6. Context Compliance Required Gate

- selected required context is acknowledged
- selected required context is not contradicted
- plan does not pass by silence
- verification does not pass by silence
- changed files do not violate declared scope/context
- known lesson patterns are not repeated
- command success is not used as context compliance
- Context Pack is not treated as approval

- Undeclared changed files must be treated as scope/context violation, not as neutral.
- Undeclared changed files must be treated as scope/context violation.
- A changed file outside declared task scope or selected context must require explicit justification or return blocked/needs_review.

Silence is not compliance.  
Command success does not override context violation.

## 7. Unified Context Pipeline Check

Future command:
- `python3 scripts/check-context-pipeline.py`
- `python3 scripts/check-context-pipeline.py --json`
- `python3 scripts/check-context-pipeline.py --root <repo-root>`
- `python3 scripts/check-context-pipeline.py --task tasks/active-task.md`
- `python3 scripts/check-context-pipeline.py --context reports/context-pack.md`
- `python3 scripts/check-context-pipeline.py --plan reports/plan.md`
- `python3 scripts/check-context-pipeline.py --verification reports/context-verification.md`

Expected result values:
- CONTEXT_PIPELINE_READY
- CONTEXT_PIPELINE_READY_WITH_WARNINGS
- CONTEXT_PIPELINE_INCOMPLETE
- CONTEXT_PIPELINE_NEEDS_REVIEW
- CONTEXT_PIPELINE_BLOCKED

Exit semantics:
- CONTEXT_PIPELINE_READY => exit 0
- everything else => exit 1

- READY_WITH_WARNINGS is exit 1 by design.
- NEEDS_REVIEW is not pass.
- BLOCKED is blocking.
- INCOMPLETE is not pass.
- Result distinction must be read from stdout or JSON.
- Exit code alone is not enough for detailed diagnosis.
- exit 0 without CONTEXT_PIPELINE_READY in stdout or JSON must not be treated as success.
- If exit code is 0 but result value is missing, malformed, or not CONTEXT_PIPELINE_READY, treat as CONTEXT_PIPELINE_INCOMPLETE.
- Required gates must read the explicit result value, not only the process exit code.

## 8. CI Required Check Contract

- CI required check should validate index freshness, Context Pack validity/freshness, compliance, non-authorization boundary, skipped validation handling, and JSON output validity.
- CI must fail on stale/missing required context.
- CI must fail on context pipeline blocked/incomplete results.
- CI must not auto-commit generated files.
- CI must not treat || true as success.
- CI must not require SQLite.
- CI must not approve protected actions.
- CI must not replace Human Gate.
- CI may report warnings, but strict gate must not silently pass warnings.
- CI must not infer context compliance from test results alone.
- CI must not infer context compliance from test results alone.
- Passing unit tests, lint, or build checks does not prove Context Pack coverage.
- Context compliance must come from explicit context pipeline result values.

|| true may be used only for evidence collection, never for required gate success.

## 9. Protected Branch Boundary

- M30 can define required status checks.
- M30 can provide setup guidance.
- M30 cannot silently configure protected branch rules without permission.
- Platform enforcement is separate from repo-local checker implementation.
- Human/admin setup may be required.
- Missing protected branch setup must be recorded honestly.
- Advisory CI is not the same as required CI.
- Required status check must be explicit.

## 10. Relationship to M27

- M30 does not replace M27 runtime enforcement.
- M30 enforces context readiness, not command execution permissions.
- M27 still controls commands, writes, commits, pushes, Human Gate, audit, retry, and identity boundaries.
- Passing M30 does not authorize runtime actions.

M30 context readiness is not runtime permission.

## 11. Relationship to M28

- M30 builds on M28 artifacts.
- M30 makes M28 checks enforceable.
- M30 does not change Markdown/YAML source-of-truth principle.
- M30 does not make SQLite authoritative.
- M30 does not create full RAG.
- M30 does not replace Context Pack or verification records.

M30 enforces M28; it does not redefine M28 source-of-truth boundaries.

## 12. Relationship to M29

- M29 tested bypass resistance.
- M30 must preserve M29 safety boundaries.
- M30 must not create bypass runner.
- M30 must not turn context checks into bypass instructions.
- M30 must not downgrade BYPASS_DETECTED findings.
- M30 must preserve non-authorization boundaries.

M30 enforcement must not become a bypass guide.

## 13. SQLite Boundary

- SQLite is optional.
- SQLite is local cache only.
- SQLite is rebuildable.
- SQLite must be gitignored.
- SQLite must not be required in CI.
- SQLite must not be source of truth.
- SQLite stale state must not override JSON/Markdown/YAML.
- SQLite freshness does not replace data/context-index.json freshness check.
- SQLite freshness must not override Markdown/YAML or data/context-index.json freshness.
- SQLite being newer than JSON does not make SQLite authoritative.
- SQLite stale or fresh state must never replace the committed context-index freshness check.

Git stores meaning.  
JSON provides navigation.  
SQLite accelerates lookup.

## 14. Non-Authorization Boundary

M30 enforced context pipeline is not approval.
M30 enforced context pipeline does not authorize commit, push, merge, release, deployment, or protected changes.
M30 enforced context pipeline does not authorize bypassing AgentOS guardrails.
M30 enforced context pipeline does not replace Human Gate.
M30 enforced context pipeline does not weaken, disable, or reduce any guardrail.
M30 enforced context pipeline must not weaken M27 runtime enforcement.
M30 enforced context pipeline must not weaken M28 context control.
M30 enforced context pipeline must not weaken M29 bypass resistance boundaries.
Human Gate remains approval authority.

## 15. Non-Goals

M30 does not implement:
- full RAG
- vector DB
- embeddings requirement
- remote backend
- LangGraph/CrewAI dependency
- autonomous memory backend
- SQLite source of truth
- bypass runner
- runtime enforcement replacement
- approval automation
- protected action executor
- M31

## 16. Planned M30 Task Sequence

- 30.1 — Enforced RAG-Light Pipeline Architecture
- 30.2 — Context Index Freshness Gate
- 30.3 — Required Context Pack Gate
- 30.4 — Context Compliance Required Gate
- 30.5 — Unified Context Pipeline Check
- 30.6 — CI Required Check Contract
- 30.7 — Protected Branch / Required Status Guide
- 30.8 — Context Pipeline Fixtures
- 30.9 — Context Pipeline Evidence Report
- 30.10 — M30 Completion Review

Later tasks are planned, not implemented by 30.1.
