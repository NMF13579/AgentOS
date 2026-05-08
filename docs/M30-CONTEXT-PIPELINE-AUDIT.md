# M30 Context Pipeline Audit

## Purpose
- M30.8 audits artifact presence and enforcement boundaries.
- Audit readiness is not approval.
- Audit readiness does not authorize protected actions.
- Audit readiness does not authorize M31.
- Audit does not configure branch protection.
- Human Gate remains approval authority.

## CLI
- `python3 scripts/audit-m30-context-pipeline.py`
- `python3 scripts/audit-m30-context-pipeline.py --json`
- `python3 scripts/audit-m30-context-pipeline.py --strict`

## Result values
- `M30_CONTEXT_PIPELINE_AUDIT_READY`
- `M30_CONTEXT_PIPELINE_AUDIT_READY_WITH_WARNINGS`
- `M30_CONTEXT_PIPELINE_AUDIT_NOT_READY`
- `M30_CONTEXT_PIPELINE_AUDIT_INCOMPLETE`
- `M30_CONTEXT_PIPELINE_AUDIT_NEEDS_REVIEW`
- `M30_CONTEXT_PIPELINE_AUDIT_BLOCKED`

## Strict mode semantics
- Strict mode semantics
- default behavior is strict

## Escalation
- Stricter audit result wins.

## Boundary checks
- SQLite is cache, not authority.
- Workflow existence is not branch protection.
- M30 must not become full RAG or platform automation.

## JSON field structure
- JSON field structure
- checked_artifacts is a summary object
- context-pipeline-ci allowed values are:
  - CONTEXT_PIPELINE_CI_PASS
  - CONTEXT_PIPELINE_CI_FAIL
  - CONTEXT_PIPELINE_CI_INVALID
  - CONTEXT_PIPELINE_CI_BLOCKED
  - CONTEXT_PIPELINE_CI_NEEDS_REVIEW

## Limitations
- audit checks repository artifacts, not live GitHub settings
- cannot prove branch protection enabled
- cannot approve completion

- Strict mode semantics
- default behavior is strict
- JSON field structure
- checked_artifacts is a summary object
- context-pipeline-ci allowed values are
- CONTEXT_PIPELINE_CI_PASS
- CONTEXT_PIPELINE_CI_NEEDS_REVIEW
- audit checks repository artifacts, not live GitHub settings
