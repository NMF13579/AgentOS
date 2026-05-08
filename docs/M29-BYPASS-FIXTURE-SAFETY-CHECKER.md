# M29 Bypass Fixture Safety Checker

## Purpose

Bypass fixture checker is not approval.
Bypass fixture checker does not authorize protected actions.
Bypass fixture checker does not execute bypass attempts.
Bypass fixture checker does not weaken M27 runtime enforcement.
Bypass fixture checker does not weaken M28 context control.
Bypass fixture checker must never become a bypass guide.
Human Gate remains approval authority.

## CLI

- `python3 scripts/check-bypass-fixtures.py`
- `python3 scripts/check-bypass-fixtures.py --json`
- `python3 scripts/check-bypass-fixtures.py --root <repo-root>`
- `python3 scripts/check-bypass-fixtures.py --fixtures tests/fixtures/m29-m28-context-bypass`
- `python3 scripts/check-bypass-fixtures.py --fixtures tests/fixtures/m29-m27-runtime-bypass`

## Result Values

- BYPASS_FIXTURES_OK
- BYPASS_FIXTURES_OK_WITH_WARNINGS
- BYPASS_FIXTURES_INVALID
- BYPASS_FIXTURES_UNSAFE
- BYPASS_FIXTURES_NEEDS_REVIEW

## Exit Semantics

- `BYPASS_FIXTURES_OK` => exit 0
- all other results => exit 1

## Fixture Roots

Default roots:
- `tests/fixtures/m29-m28-context-bypass/`
- `tests/fixtures/m29-m27-runtime-bypass/`

The checker verifies root existence, `README.md`, required files, and unsafe/disallowed files.

## Required Structure Checks

- required fixture directory exists
- `bypass-test-case.md` exists
- `fixture-notes.md` exists
- fixture root exists but contains zero valid fixture directories => invalid

## Frontmatter Checks

Required fields:
- `type`
- `test_id`
- `status`
- `category`
- `target_boundary`
- `expected_status`
- `safety_level`
- `created_by`
- `created_at`
- `review_required`

Rules:
- `created_by must not retain the template placeholder value`
- `created_at must not be in the future`
- duplicate test_id values are invalid
- forbidden expected statuses (`BYPASS_ALLOWED`, `APPROVED`, `AUTHORIZED`) are unsafe

## Body Section Checks

Required sections:
- Simulated Attempt
- Expected Guardrail
- Expected Result
- Evidence Required
- Forbidden Real Behavior
- Safety Notes
- Non-Authorization Statement

Rules:
- missing required section => invalid
- empty Evidence Required section => invalid
- empty Forbidden Real Behavior section => invalid
- empty Safety Notes => needs review
- Evidence must reference the specific guardrail or boundary

## Non-Authorization Checks

Required block lines are validated as strict statements.
The checker also checks weakened/missing boundary text.
The checker does not flag negated non-authorization statements as forbidden claims.

## File Safety Checks

- checker must not execute files
- no executable files or executable bit
- no shebang files
- no disallowed script extensions
- no symlinks
- only `.md`/`.json`

## Secret / Credential Checks

Detects patterns such as private keys, AWS keys, GitHub tokens, Slack tokens, Bearer token phrases, `password=`, `secret=`.

`secret_pattern_detected` findings are redacted in output.

Context-sensitive detection is required for generic patterns such as password=.
patterns found inside Simulated Attempt, Forbidden Real Behavior, or Safety Notes sections are classified by defensive context.

## Production Target Checks

Flags likely production/external targets for review and unsafe instructions.

## Bypass-Guide Pattern Checks

Detects instruction-like bypass phrasing and classifies by context.
Category example: `bypass_guide_pattern`.

## Category Coverage Checks

Checker validates required M28/M27 category directories for default fixture roots.

## JSON Output Behavior

- valid JSON object
- includes findings, warnings, errors, result
- no secrets in full form
- repository-relative paths

## No-Write Behavior

Checker is read-only and does not create, modify, delete, chmod, or execute files.

## Validation Notes

Using || true must not convert checker findings into successful validation.
