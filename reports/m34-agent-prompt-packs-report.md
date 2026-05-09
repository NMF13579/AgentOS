# M34 Agent Prompt Packs Report

## Summary
Scoped prompt pack hardening completed using only files allowed by 34.7.0. Prompt instructions now explicitly include fail-closed context rules, human-gate boundaries, validation honesty rules, and non-claims.

## Preconditions
- `reports/m34-release-readiness-intake.md` with `M34_RELEASE_READINESS_INTAKE_COMPLETE`: PASS
- `reports/m34-documentation-hardening-report.md` with `M34_DOCUMENTATION_HARDENING_COMPLETE`: PASS
- `reports/m34-example-scenarios-report.md` with `M34_EXAMPLE_SCENARIOS_COMPLETE`: PASS
- `reports/m34-agent-prompt-packs-inspection.md` with `M34_AGENT_PROMPT_PACKS_INSPECTION_COMPLETE`: PASS
- `Files Allowed for 34.7.1` section present: PASS
- `NO_EXISTING_AGENT_PROMPT_PACK_PATH_FOUND` marker: NOT PRESENT

## Inspection Report Used
- `reports/m34-agent-prompt-packs-inspection.md`

## Files Allowed by 34.7.0
- `prompts/cursor.md`
- `prompts/claude-code.md`
- `prompts/codex.md`
- `prompts/generic-agent.md`
- `AGENTS.md`
- `CLAUDE.md`

## Files Modified
- `prompts/cursor.md`
- `prompts/claude-code.md`
- `prompts/codex.md`
- `prompts/generic-agent.md`
- `AGENTS.md`
- `CLAUDE.md`

## Prompt Packs Created
- None

## Prompt Packs Updated
- `prompts/cursor.md`
- `prompts/claude-code.md`
- `prompts/codex.md`
- `prompts/generic-agent.md`
- `AGENTS.md`
- `CLAUDE.md`

## AgentOS Rules Included
Added/standardized explicit rules for:
- read `tasks/active-task.md` first
- respect scope and avoid unrelated changes
- use Context Pack before execution
- do not execute without valid context
- do not stage unrelated files
- do not push unless explicitly allowed

## Fail-Closed Rules Included
Added/standardized explicit rules for:
- `No Context Pack -> No Execution`
- missing Context Pack blocks execution
- empty Context Pack blocks execution
- `Required Context: none` blocks execution
- `CONTEXT_PIPELINE_INVALID` blocks execution
- `UNKNOWN` must not become `PASS`
- `STATUS_SOURCE_DAMAGED` must not become `READY`
- `BLOCKED / NEEDS_REVIEW` must be explained and not bypassed

## Human Gate Rules Included
Added/standardized explicit rules for:
- human approval must come from human
- agent must not self-approve
- TUI/status output is not approval
- completion review is a decision record, not a repair step

## Validation Honesty Rules Included
Added/standardized explicit rules for:
- do not claim `PASS` without proof
- do not treat skipped validation as passed
- report failed commands honestly
- report missing commands honestly

## Non-Claims Added
Added/retained non-claims so prompts do not imply:
- release readiness from prompt packs alone
- bypassing context gates
- self-approval authority
- replacing human gates with status output

## Tool-Specific Guidance Added
- Cursor: scoped edits, honest validation, no out-of-scope auto-fixes
- Claude Code: file inspection first, strict gate boundaries
- Codex: minimal patch-oriented changes, explicit validation evidence
- Generic Agent: universal protocol `Task -> Context Pack -> Plan -> Scoped Execution -> Validation -> Evidence -> Stop`

## Prompt Pack Readiness Impact
Prompt packs are now more consistent with M33 fail-closed behavior and M34 honesty requirements. This improves safe external usage guidance, but does not prove MVP release readiness.

## Validation Evidence
Commands run:
- Pre-modification:
  - `test -f reports/m34-agent-prompt-packs-inspection.md`
  - `grep -q "M34_AGENT_PROMPT_PACKS_INSPECTION_COMPLETE" reports/m34-agent-prompt-packs-inspection.md`
  - `grep -q "Files Allowed for 34.7.1" reports/m34-agent-prompt-packs-inspection.md`
- Content checks:
  - `grep -R "No Context Pack" prompts AGENTS.md CLAUDE.md 2>/dev/null || true`
  - `grep -R "do not claim PASS without proof" prompts AGENTS.md CLAUDE.md 2>/dev/null || true`
  - `grep -R "do not self-approve" prompts AGENTS.md CLAUDE.md 2>/dev/null || true`
  - `grep -R "TUI/status output is not approval" prompts AGENTS.md CLAUDE.md 2>/dev/null || true`
  - `grep -R "do not push unless explicitly allowed" prompts AGENTS.md CLAUDE.md 2>/dev/null || true`
- Repository checks:
  - `bash scripts/run-all.sh || true` (FAIL observed from task validation schema mismatch)
  - `python3 scripts/agentos-validate.py all || true` (Overall result: FAIL)
  - `python3 scripts/audit-agentos.py || true` (Result: PASS_WITH_WARNINGS)

## Known Gaps
- Validation command set is not fully green in current repository state (`run-all.sh` and `agentos-validate.py all` report failures unrelated to prompt-file syntax).
- Existing working tree contains broad unrelated modifications; this task intentionally did not alter scope beyond allowed files.

## Final Status
`M34_AGENT_PROMPT_PACKS_COMPLETE`
