# M30 Unified Context Pipeline Check

## Purpose
- Unified Context Pipeline Check aggregates M30.2, M30.3, M30.4 gate outputs.
- Fresh Index + Valid Context Pack + Context Compliance = CONTEXT_PIPELINE_READY.
- Unified Context Pipeline Check is not approval.
- Unified Context Pipeline Check does not authorize protected actions.
- Unified Context Pipeline Check does not replace Human Gate.
- Unified Context Pipeline Check does not replace M27 runtime enforcement.
- Unified Context Pipeline Check does not weaken M28 context control.
- Unified Context Pipeline Check does not weaken M29 bypass resistance boundaries.
- Human Gate remains approval authority.

## CLI
- `python3 scripts/check-context-pipeline.py`
- `python3 scripts/check-context-pipeline.py --json`
- `python3 scripts/check-context-pipeline.py --strict`
- `python3 scripts/check-context-pipeline.py --mode plan|verification|both`

## Mode Semantics
- mode changes only the compliance gate mode.
- --mode does not skip index/context-pack gates.
- Preferred behavior: invoke all three gates independently.
- Skipping nested validation flags does not skip the corresponding gate.

## Result Values
- `CONTEXT_PIPELINE_READY`
- `CONTEXT_PIPELINE_READY_WITH_WARNINGS`
- `CONTEXT_PIPELINE_MISSING`
- `CONTEXT_PIPELINE_INVALID`
- `CONTEXT_PIPELINE_STALE`
- `CONTEXT_PIPELINE_VIOLATION`
- `CONTEXT_PIPELINE_INCOMPLETE`
- `CONTEXT_PIPELINE_NEEDS_REVIEW`
- `CONTEXT_PIPELINE_BLOCKED`

## Exit Semantics
- `CONTEXT_PIPELINE_READY => exit 0`
- others => `exit 1`
- Exit code alone is not readiness.

## Result Escalation
- Stricter result wins.

## Gate Invocation
- Unified pipeline must not silently skip required gates.
- all subprocess invocations use `shell=False`.
- default timeout should be 30 seconds per gate subprocess.

## Mapping
- index stale => pipeline stale
- context pack stale => pipeline stale
- compliance violation => pipeline violation
- any blocked gate => pipeline blocked

## JSON output
- includes gate results, command, result, exit_code, parsed_json
- Finding severity mapping rules
- severity: error must correspond to a non-ready result

## Source-of-truth and authorization boundary
- Pipeline readiness is not approval.
- Tests passing is not context compliance.
- Command success does not override context violation.
- Git stores meaning.
- JSON provides navigation.
- SQLite accelerates lookup.

## Non-Authorization Boundary
Unified Context Pipeline Check is not approval.
Unified Context Pipeline Check does not authorize commit, push, merge, release, deployment, or protected changes.
Unified Context Pipeline Check does not authorize bypassing AgentOS guardrails.
Unified Context Pipeline Check does not replace Human Gate.
Unified Context Pipeline Check does not weaken, disable, or reduce any guardrail.
Unified Context Pipeline Check must not weaken M27 runtime enforcement.
Unified Context Pipeline Check must not weaken M28 context control.
Unified Context Pipeline Check must not weaken M29 bypass resistance boundaries.
Human Gate remains approval authority.

- Unified pipeline must not silently skip required gates.
- gate-exit-result-mismatch
- severity: error must correspond to a non-ready result
