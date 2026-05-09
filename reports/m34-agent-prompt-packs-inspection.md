# M34 Agent Prompt Packs Inspection

## Summary
Read-only inspection completed for agent prompt packs and profile/rule structure. Existing prompt packs are present in `prompts/`, but dedicated `profiles/`, `.cursor/`, and `.claude/` directories are missing. Repository already contains core guardrail instructions in prompt packs and root agent instruction files.

## Preconditions
- `reports/m34-release-readiness-intake.md` with `M34_RELEASE_READINESS_INTAKE_COMPLETE`: PASS
- `reports/m34-documentation-hardening-report.md` with `M34_DOCUMENTATION_HARDENING_COMPLETE`: PASS
- `reports/m34-example-scenarios-report.md` with `M34_EXAMPLE_SCENARIOS_COMPLETE`: PASS

## Inspection Method
Used read-only filesystem and grep commands only:
- directory/file existence checks for prompts/profiles/agent rule roots
- `find` for prompt/rule file discovery
- `grep -R` for rule coverage: active task, context pack, no-context gate, validation honesty, human gate, approval boundaries

## Prompt Directories Found
- `prompts/`: FOUND
- `profiles/`: MISSING
- `.cursor/`: MISSING
- `.claude/`: MISSING

## Agent Profile Files Found
- `AGENTS.md`: FOUND
- `CLAUDE.md`: FOUND
- `GEMINI.md`: FOUND

## Cursor Prompt / Rules Status
- `prompts/cursor.md`: FOUND
- Cursor-specific guidance present.
- Classification: `READY_FOR_PROMPT_PACK`

## Claude Code Prompt / Rules Status
- `prompts/claude-code.md`: FOUND
- Claude Code-specific guidance present.
- Classification: `READY_FOR_PROMPT_PACK`

## Codex Prompt / AGENTS Status
- `prompts/codex.md`: FOUND
- `AGENTS.md`: FOUND
- Classification: `READY_FOR_PROMPT_PACK`

## Generic Agent Prompt Status
- `prompts/generic-agent.md`: FOUND
- Classification: `READY_FOR_PROMPT_PACK`

## Existing AgentOS Instructions Found
Evidence found across prompts/docs/root instructions for:
- read active task first (`tasks/active-task.md` references)
- context pack and `No Context Pack` fail-closed rule
- validation requirements and honesty rules
- human gate boundaries and non-self-approval constraints
- approval boundary language (`status/TUI is not approval` style statements in docs/prompts)

## Missing Prompt Pack Areas
- Missing dedicated agent profile directory: `profiles/`
- Missing tool-native rule directories: `.cursor/`, `.claude/`
- No explicit separate prompt pack file discovered for “other agent profiles” beyond existing root/prompt files

## Prompt Pack Readiness Classification
- prompts directory: `READY_FOR_PROMPT_PACK`
- Cursor prompt pack: `READY_FOR_PROMPT_PACK`
- Claude Code prompt pack: `READY_FOR_PROMPT_PACK`
- Codex prompt pack: `READY_FOR_PROMPT_PACK`
- generic agent prompt pack: `READY_FOR_PROMPT_PACK`
- agent profiles: `MISSING`
- Cursor rules: `MISSING`
- Claude rules: `MISSING`
- AGENTS.md / Codex-style instructions: `READY_FOR_PROMPT_PACK`
- active task instruction: `PARTIALLY_READY`
- scope compliance instruction: `PARTIALLY_READY`
- Context Pack instruction: `PARTIALLY_READY`
- No Context Pack → No Execution instruction: `PARTIALLY_READY`
- validation proof instruction: `READY_FOR_PROMPT_PACK`
- human gate instruction: `PARTIALLY_READY`
- no self-approval instruction: `PARTIALLY_READY`
- known gaps honesty instruction: `PARTIALLY_READY`

## Recommended Scope for 34.7.1
Update existing prompt packs and root instruction files only, to standardize required M33 fail-closed, human-gate, and validation-honesty wording across supported agent tools.

## Files Allowed for 34.7.1
- `prompts/cursor.md`
- `prompts/claude-code.md`
- `prompts/codex.md`
- `prompts/generic-agent.md`
- `AGENTS.md`
- `CLAUDE.md`

## Files Forbidden for 34.7.1
- `profiles/` (missing path; do not create in 34.7.1 without separate decision)
- `.cursor/` (missing path; do not create in 34.7.1 without separate decision)
- `.claude/` (missing path; do not create in 34.7.1 without separate decision)
- any file not explicitly listed in Files Allowed for 34.7.1

## Potential New Files Requiring Human Decision
- `profiles/` (directory and profile files)
- `.cursor/rules/*.md` (or repository-native equivalent)
- `.claude/*.md` rule files (or repository-native equivalent)

## Required Behavior for 34.7.1
Future 34.7.1 must ensure prompt packs instruct agents to:
- read active task first
- respect scope
- use context pack and enforce no-context gate
- not execute without valid context
- not claim PASS without proof
- run validation and report failed/missing commands honestly
- stop at human gates
- avoid self-approval
- avoid treating TUI/status as approval
- avoid unrelated file edits/staging/push

Future 34.7.1 must not:
- create product-marketing prompts
- hide known gaps
- weaken fail-closed behavior
- permit execution without context pack
- permit self-approval
- claim release readiness without M34 evidence and completion review

## Validation Evidence
Commands run:
- `test -f reports/m34-release-readiness-intake.md`
- `grep -q "M34_RELEASE_READINESS_INTAKE_COMPLETE" reports/m34-release-readiness-intake.md`
- `test -f reports/m34-documentation-hardening-report.md`
- `grep -q "M34_DOCUMENTATION_HARDENING_COMPLETE" reports/m34-documentation-hardening-report.md`
- `test -f reports/m34-example-scenarios-report.md`
- `grep -q "M34_EXAMPLE_SCENARIOS_COMPLETE" reports/m34-example-scenarios-report.md`
- prompt/rule discovery and grep inspection commands from task contract

## Known Gaps
- No `profiles/` structure found.
- No `.cursor/` or `.claude/` rule directories found.
- Some required behaviors are present but not yet uniformly standardized across all prompt files.

## Final Status
`M34_AGENT_PROMPT_PACKS_INSPECTION_COMPLETE`
