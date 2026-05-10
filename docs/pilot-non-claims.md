# Public Non-Claims and Positioning — M37 External Pilot

## Purpose
This document defines how AgentOS should be described during the M37 External Pilot to prevent false expectations and unsafe interpretation of pilot results.

## Positioning Summary
During M37, AgentOS is an **experimental repository-based guardrail framework** in a controlled pilot stage. It is not a commercial product or a production-ready security tool.

## What AgentOS Is
AgentOS may be described as:
- A programmable guardrail layer for AI coding workflows.
- A Markdown/YAML-first control and evidence structure.
- A task contract and validation framework for AI-assisted development.
- A tool to help make AI-generated changes more reviewable and structured.
- An experimental pilot-stage system requiring human oversight.

## What AgentOS Is Not
AgentOS is **NOT**:
- A SaaS platform or public release.
- Production-ready or a production deployment system.
- A production-grade secure sandbox.
- An autonomous safe execution platform.
- A replacement for human engineering judgment or review.
- A guarantee of bug-free AI output.
- A vector database or full RAG backend.
- LangGraph or CrewAI.

## Allowed Pilot Claims
- AgentOS is currently in a controlled pilot evaluation with selected users.
- AgentOS helps structure and validate AI-assisted coding tasks.
- AgentOS provides structured feedback and evidence reports.
- AgentOS aims to increase the transparency of AI-driven workflows.

## Forbidden Claims
- AgentOS is ready for production use.
- AgentOS makes AI coding safe by default without human review.
- AgentOS prevents all mistakes made by AI agents.
- AgentOS guarantees correct or optimal implementation.
- AgentOS can safely run autonomously without checkpoints.
- AgentOS is a SaaS product.

## Production Readiness Boundary
The M37 pilot is designed to test usability and workflow, not to prove production readiness. No results from the pilot should be used as evidence for production security certification.

## Human Review Boundary
AgentOS is built to assist human review, not to replace it. A `PASS` result in any AgentOS tool never replaces the need for an engineer to review the final code change.

## Validation Boundary
- Passing validation is **evidence**, not a guarantee.
- Missing, failed, or skipped validation is **not** PASS.
- Inconclusive results must be treated as FAIL until clarified.
- M37 pilot readiness is **not** public release readiness.

## Public Communication Rules
- Always mention that AgentOS is in a **controlled experimental pilot**.
- Always emphasize that **human review is required**.
- Use cautious, evidence-based language; avoid marketing hyperbole.
- Do not imply SaaS availability or hosted runner capabilities.

## Final Non-Claims Rule
Honesty over marketing. If a capability cannot be proven by the current validation suite, it must not be claimed as a feature of the M37 pilot.
