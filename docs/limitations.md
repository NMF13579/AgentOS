# Limitations and Non-Claims

This document records the current limitations and non-claims of AgentOS in its MVP state.

## Current MVP Boundary

AgentOS is a programmable guardrail layer for AI-assisted coding workflows. It is not a general-purpose application framework or an autonomous agent platform.

## Non-Goals

- **No production-grade guarantees:** AgentOS provides process verification, not product certification.
- **No autonomous execution:** AgentOS does not execute tasks without human oversight.

## Safety Limitations

- **Dependency on Inputs:** AgentOS depends on the accuracy of task briefs, contracts, and reports.
- **Human Responsibility:** Guardrails block dangerous scenarios but do not replace the engineer's final responsibility.
- **Fail-Closed by Default:** If validation is not run, the state remains NOT_READY.

## What AgentOS Does Not Provide

To avoid confusion, note that AgentOS is **NOT**:
- A backend service or API.
- A cloud or server platform.
- A Web UI or dashboard.
- A vector database or RAG system.
- An autonomous agent like Devin or OpenDevin.
- A model router (LLM gateway).
- A CI/CD platform (though it can be used within one).
- A guarantee of bug-free AI output.

## Known Gaps (Milestone 36)

- **Installation Packaging:** AgentOS is copied directly; it is not yet a `pip` or `npm` package.
- **Automated Repair:** AgentOS identifies blockers but does not fix them automatically.
- **Web Interface:** All interactions are via CLI and Markdown.

## Relationship to MVP Readiness

- **Missing Implementation:** If a feature is marked NOT_IMPLEMENTED, it is not a failure but a known gap.
- **NOT_IMPLEMENTED is not PASS:** A missing feature cannot be treated as ready.
- **NOT_RUN is not PASS:** A skipped check provides zero evidence of readiness.
- **NOT_APPLICABLE:** Requires a written justification in the relevant report.
