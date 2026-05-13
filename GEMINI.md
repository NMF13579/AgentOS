<!-- ROLE: CANONICAL ENTRYPOINT -->
<!-- AUTHORITY: NON-AUTHORITY -->
<!-- SOURCE_OF_TRUTH: no -->

Read `llms.txt` first. Follow it exactly.
Follow the five canonical runtime modules listed there.
Use `ROUTES-REGISTRY.md` only to confirm ownership and routing.
Adapters are not runtime authority.
Do not browse files independently.
Do not invent structure or rules.
If the task is clear — do it.
If something is missing or contradictory — briefly say what is missing and stop.

## Foundation Mandates

1. **Single-Role Execution:** Every agent run must declare exactly one role (implementor, auditor, etc.) in the task contract. Do not mix roles (e.g., Auditor must not fix findings in the same run). Enforced by `scripts/check-single-role-execution.py`.
2. **Readiness Assertions:** No premature readiness claims (pilot-ready, production-ready) allowed without explicit completion tokens. Enforced by `scripts/check-readiness-assertions.py`.
3. **YAML Safety:** Do not use empty JSON brackets `[]` in YAML blocks (e.g., `sensitive_paths`); leave the field empty or remove it to prevent parser failure.
4. **Idle-State Bypass:** Any scripts parsing `active-task.md` must implement an `is_idle_state()` bypass before attempting to parse YAML frontmatter. This gracefully handles the system's "idle state" (no active task) and prevents `run-all.sh` or CI pipelines from failing. Return `0` (or `PASS`) if `no active task` is present or if `---` is missing.

When explaining issues: Russian first, no internal terminology, say only what is wrong / why / what to change.
When fixing: make the smallest possible change, show only the corrected content, no commentary.
