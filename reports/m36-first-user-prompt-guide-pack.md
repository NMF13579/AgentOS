# M36 First-User Prompt and Guide Pack

**Task ID:** task-m36-first-user-prompt-guide-pack
**Date:** 2026-05-10
**Repository:** AgentOS
**Branch:** dev

## Preconditions
- M36 README, Installation, Onboarding, and Troubleshooting hardening reports exist: PASS

## Files Created
- `docs/first-user-guide.md`
- `prompts/first-user-agent.md`

## Guide Content Summary
- **Definition:** Defined AgentOS as a programmable guardrail layer for AI workflows.
- **Path:** Recommended a sequence starting with README and ending with a tiny documentation task.
- **Safety:** Explicitly warns against starting with scripts or security files.
- **Statuses:** Provides plain-language definitions for all AgentOS status codes.

## Prompt Content Summary
- **Compliance:** Instructs agents to respect `scope_control` and reading orders.
- **Honesty:** Mandates honest reporting of validation failures and prevents fake PASS claims.
- **Control:** Forbids self-approving human gates or autonomous staging/committing.

## Result Semantics Preserved
- PASS, WARN, BLOCKED, NOT_READY, FAIL, and INCONCLUSIVE are explained in both documents with actions mapped to them.

## Non-Goals Included
- Explicitly excludes web UI, cloud platforms, vector DBs, and multi-agent orchestration.

## Remaining Gaps
- None. First-user entry and agent-onboarding documents are in place.

## Deferred Findings
- Verification of agent performance using the new prompt pack (36.7.1).

## Non-Claims
- This guide pack does not make AgentOS externally usable by itself.
- This guide pack does not run install smoke.
- This guide pack does not run example smoke.
- This guide pack does not approve release publication.
- This guide pack does not authorize UI dashboard, hosted diagnostics, IDE plugin, cloud/server, vector DB, or M37 feature work.
- This guide pack does not replace M36 completion review.

## Final Status
`M36_FIRST_USER_PROMPT_GUIDE_PACK_COMPLETE`
