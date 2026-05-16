## Purpose
Map runtime/diagnostic risks before any CLI simplification action.

## Runtime Risk Categories
| Script Path | Risk | Why |
| --- | --- | --- |
| scripts/agentos-validate.py | HIGH | orchestrates many subprocess validations and output contracts |
| scripts/test-integrity-regression.py | HIGH | regression command orchestration and token semantics |
| scripts/check-validator-authority-boundary.py | MEDIUM | standalone validation checker |
| scripts/check-role-separation.py | MEDIUM | standalone validation checker |
| scripts/check-evidence-immutability.py | MEDIUM | standalone validation checker |
| scripts/install-agentos.py | CRITICAL | install path can change repository state |
| scripts/__pycache__/* | UNKNOWN | cache artifacts not runtime-authoritative |

## Diagnostic Preservation Principles
CLI simplification must not hide failure classes.
CLI simplification must not convert NEEDS_REVIEW into PASS.
CLI simplification must not convert WARNING into clean PASS.
CLI simplification must not make NOT_RUN appear as PASS.
CLI simplification must not turn validation evidence into approval.

## Security-Sensitive Patterns
- shell=True: found
- subprocess.run: found
- os.system: found
- eval(: not_found
- exec(: not_found
- git push: found
- git commit: found
- approval file writes: not_found
- fixture writes: not_found
- report writes: not_found
- task file writes: not_found

## shell=True Review
- shell=True: found

## Subprocess Boundary Review
- subprocess.run: found
- os.system: found

## JSON Output Preservation
- Wrappers must preserve JSON shape and result token source.

## Exit Code Preservation
- Wrappers must preserve non-zero/zero exit semantics.

## Source Token Preservation
- Wrappers must preserve originating checker token semantics.

## Do-Not-Touch Scripts
- scripts/agentos-validate.py
- scripts/test-integrity-regression.py
- scripts/check-validator-authority-boundary.py
- scripts/check-role-separation.py
- scripts/check-evidence-immutability.py

## Risk Summary
- Highest risk: simplification that hides source diagnostics or alters exit/token semantics.
