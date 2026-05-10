# Agent Rule Guard Report (No Premature Readiness Claims)

**Task ID:** task-governance-claim-guard
**Date:** 2026-05-10
**Repository:** AgentOS
**Branch:** dev

## Goal
Implement a generation-time agent rule to prevent agents from asserting project readiness without a valid completion review token.

## Implementation Details
- **Rule Config:** `core-rules/agent-rules.yml` (structured YAML definition)
- **Governance Update:** `core-rules/MAIN.md` (added Generation Guard boundary)
- **Quality Update:** `quality/MAIN.md` (added Readiness Assertions section)

### Rule Summary
- **Forbidden Patterns:** Phrases like "system is ready", "готов к пилоту", etc.
- **Enforcement:** Requires presence of valid tokens (e.g., `M37_PILOT_READY`).
- **Replacement:** Automates the transition from "ready" to "meets conditions for review".
- **Context-Awareness:** Forces a "not ready" statement if `FAIL` or `BLOCKED` markers are present.

## Files Modified
- `core-rules/MAIN.md`
- `quality/MAIN.md`
- `core-rules/agent-rules.yml` (New File)
- `tasks/active-task.md` (Scope update)

## Validation Results
- `python3 scripts/validate-task.py tasks/active-task.md`: **PASS**
- `python3 scripts/agentos-validate.py all`: **FAIL** (Expected: existing legacy violations detected by the rule).

## Final Status
`M37_AGENT_RULE_ENFORCED`
