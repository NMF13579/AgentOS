# M40.5 First-User Friction Map

## Path Mapping

| Step | Status | Evidence Source | Friction | Impact | Suggested Later Fix | Owner Milestone |
|---|---|---|---|---|---|---|
| 1. User receives AgentOS | CLEAR | README.md | None. | High | N/A | - |
| 2. User understands what AgentOS is | CLEAR | AGENTOS-WHY.md | Conceptual complexity of "AgentOS" vs "Template". | Medium | Visual architecture map. | M40.13 |
| 3. User installs or copies | UNCLEAR | `m40-installer-mvp-report.md` | `cp -an` is simple but manual; installer script is new and needs docs. | Medium | Formalize installer CLI guide. | M40.13 |
| 4. User follows quickstart | UNCLEAR | `m40-final-report.md` | "PASS with gaps" mentioned but not documented for user. | High | Fix quickstart gaps identified in M40. | M40.13 |
| 5. User creates first task | CLEAR | templates/TASK.md | Standard markdown, well understood. | Low | N/A | - |
| 6. User runs validation | MISSING | `reports/ci/` | `agentos-validate.py` output is technical and not linked to task view. | Medium | Unified CLI with human-readable validation summary. | M40.9 |
| 7. User understands result | MISSING | `reports/m40-final-report.md` | User relies on agent interpreting JSON; no direct "Honest PASS" UI. | High | Implement TUI/CLI result renderer. | M40.9 |
| 8. User knows next action | UNCLEAR | `agentos-next-step.py` | Tool exists but not consistently used in M40 reports. | Medium | Automate "Next Safe Step" suggestion in CLI. | M40.9 |

## Friction Summary
The primary friction is the **Evidence Interpretation Gap**. Users must trust the agent's summary of technical validation results because there is no unified, human-friendly "Proof View" that binds runner output to the PASS claim.

## Impact
M40 proved portability works, but the "user trust" layer remains dependent on agent honesty, which Honest PASS (M40.6+) must address.
