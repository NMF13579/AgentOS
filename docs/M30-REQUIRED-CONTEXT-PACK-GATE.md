# M30 Required Context Pack Gate

## Purpose
- Required Context Pack Gate validates `reports/context-pack.md` before context-compliant execution.
- No valid Context Pack → No Context-Compliant Execution.
- Required Context Pack Gate is not approval.
- Required Context Pack Gate does not authorize protected actions.
- Required Context Pack Gate does not replace Human Gate.
- Required Context Pack Gate does not replace M27 runtime enforcement.
- Required Context Pack Gate does not weaken M28 context control.
- Required Context Pack Gate does not weaken M29 bypass resistance boundaries.
- Human Gate remains approval authority.

## CLI
- `python3 scripts/check-required-context-pack.py`
- `python3 scripts/check-required-context-pack.py --json`
- `python3 scripts/check-required-context-pack.py --root <repo-root>`
- `python3 scripts/check-required-context-pack.py --task tasks/active-task.md`
- `python3 scripts/check-required-context-pack.py --context reports/context-pack.md`
- `python3 scripts/check-required-context-pack.py --index data/context-index.json`
- `python3 scripts/check-required-context-pack.py --require-fresh-index`

## Result Values
- `CONTEXT_PACK_VALID`
- `CONTEXT_PACK_VALID_WITH_WARNINGS`
- `CONTEXT_PACK_MISSING`
- `CONTEXT_PACK_INVALID`
- `CONTEXT_PACK_STALE`
- `CONTEXT_PACK_INCOMPLETE`
- `CONTEXT_PACK_NEEDS_REVIEW`
- `CONTEXT_PACK_BLOCKED`

## Exit Semantics
- `CONTEXT_PACK_VALID => exit 0`
- all other results => `exit 1`
- Required gates must require both explicit `CONTEXT_PACK_VALID` and exit 0.

## Required Context Pack Structure
- Context Pack must be task-specific.
- Required sections: Selected Context, Required Context, Verification Checklist, Non-Authorization block.
- context_index_hash in Context Pack must match the hash of the currently committed data/context-index.json.
- Fresh Context Pack requires fresh context index.

## Task Binding Checks
- task file exists
- task_id in task exists
- task_id in context pack exists
- both task_id values must match

## context_index_hash Freshness
- missing hash => invalid
- format must be `sha256:<hex>`
- mismatch => stale

## Optional Fresh Index Check
- checker must call it as subprocess (`shell=False`) when `--require-fresh-index` is used.
- if freshness checker missing => incomplete

## repo_commit_hash Checks
- repo_commit_hash is generated metadata, not approval.
- repo_commit_hash mismatch alone must not automatically override a matching context_index_hash.

## Selected Context Reason Checks
- No reason → invalid Context Pack.
- placeholder reason => invalid
- role/status is absent, unreadable, or ambiguous => conservative handling

## Required Context Coverage
- Required context must be explicit.
- missing required context section => invalid

## Verification Checklist
- must include verification guidance
- Silence is not compliance.
- Command success does not override context violation.
- Context Pack is not approval.

## Source File Checks
- selected sources must exist
- path must be repository-relative and safe

## Source-of-Truth Boundary
- Context Pack is not approval.
- Markdown/YAML = meaning.
- JSON = navigation.
- SQLite = speed.

## SQLite Boundary
- SQLite is optional cache only
- SQLite must not override context-index/context-pack freshness

## JSON Output
Fields:
- result
- task_path
- context_path
- index_path
- checked_selected_items
- context_index_hash
- expected_context_index_hash
- repo_commit_hash
- warnings
- errors
- findings
- index_freshness_result (when requested)

Finding severity mapping rules:
- severity: blocking must correspond to result CONTEXT_PACK_BLOCKED or CONTEXT_PACK_INVALID.
- severity: needs_review must correspond to result CONTEXT_PACK_NEEDS_REVIEW or stricter non-ready result.
- severity: error must not correspond to CONTEXT_PACK_VALID.
- Finding severity must not imply success when result is non-ready.

## Template-dependent checks
- If `templates/context-pack.md` is missing, uncertainty must be reported, not silently passed.

## Fixtures
- Root: `tests/fixtures/required-context-pack-gate/`
- each fixture includes `fixture-notes.md` and `expected-result.txt`

## Non-Authorization Boundary
Required Context Pack Gate is not approval.
Required Context Pack Gate does not authorize commit, push, merge, release, deployment, or protected changes.
Required Context Pack Gate does not authorize bypassing AgentOS guardrails.
Required Context Pack Gate does not replace Human Gate.
Required Context Pack Gate does not weaken, disable, or reduce any guardrail.
Required Context Pack Gate must not weaken M27 runtime enforcement.
Required Context Pack Gate must not weaken M28 context control.
Required Context Pack Gate must not weaken M29 bypass resistance boundaries.
Human Gate remains approval authority.

## Limitations
- deterministic local checker
- not a semantic AI judge
- ambiguous cases => needs review
