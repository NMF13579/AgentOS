# First Project Onboarding Guide

Welcome to AgentOS! This guide is for first-time users who have successfully installed or copied AgentOS and are ready to try it on a real or test project safely.

## 1. Purpose

The purpose of this guide is to bridge the gap between "installed" and "productive". It helps you navigate your first steps without risking your project's stability, ensuring that you understand the AgentOS guardrail workflow through practical application.

## 2. Recommended First Task

The safest way to start is with a **low-risk task**. This allows you to verify that your AI assistant (e.g., Cursor, Claude Code) respects the AgentOS boundaries before you trust it with complex changes.

**Recommended first tasks:**
- **Documentation-only change:** Update a README, add comments to a file, or fix a typo.
- **Wording improvement:** Refine the descriptions in your existing `docs/`.
- **Validation-only check:** Simply run the validation suite to confirm everything is green without changing any code.
- **Example walkthrough:** Inspect the `examples/` directory to see how AgentOS is applied in other scenarios.

**Avoid as your first task:**
- Production deployments.
- Security-sensitive changes (auth, permissions).
- Database migrations.
- Large architectural refactors.
- Modifying AgentOS core policies.
- Autonomous multi-step coding tasks.

## 3. First Safe Path

Before making any changes, run the validation suite to establish a "known good" baseline:

```bash
# 1. Run the official full unified validation
python3 scripts/agentos-validate.py all

# 2. Check MVP release readiness (if available)
python3 scripts/audit-mvp-readiness.py

# 3. Run the core validation suite (tasks and verification)
bash scripts/run-all.sh
```

*(Note: Some commands may return PASS_WITH_WARNINGS if optional components or future milestone checks are skipped. This is normal).*

## 4. First Project Workflow

Follow this recommended sequence for your first few tasks:

1. **Read README & Quickstart:** Understand the basic concepts.
2. **Run Validation:** Establish your baseline.
3. **Open this Guide:** You are here!
4. **Choose a Low-Risk Task:** Pick something from Section 2.
5. **Update Task Scope:** If your project uses the full template, define your task in `tasks/active-task.md`.
6. **Execute Task:** Use your AI assistant to perform the small change.
7. **Run Validation Again:** Confirm that the change stayed within scope and no rules were broken.
8. **Review Reports:** Check the generated artifacts in `reports/`.
9. **Decide Next Action:** If green, proceed to your next small task.

## 5. Result Interpretation

AgentOS provides specific status codes. Here is what they mean in plain language:

- **PASS:** Everything checked is correct. You are safe to proceed.
- **PASS_WITH_WARNINGS:** The area is usable, but non-critical gaps were found. Read the report.
- **WARNING:** Something requires your review. It is not an automatic failure, but don't ignore it.
- **BLOCKED:** A safety rule was triggered. **STOP** and fix the blocker before proceeding.
- **NOT_READY:** The system or task is not at the required maturity level yet.
- **FAIL:** A mandatory check failed.
- **INCONCLUSIVE:** The validator crashed or timed out. The result **cannot be trusted**.

**Rules:**
- **WARNING is not approval.** It is a signal to look closer.
- **BLOCKED means stop.** Do not try to bypass the guardrail.
- **Missing evidence is not success.** No proof = NOT_READY.
- **Skipped validation is not passed validation.**

## 6. What To Do If Something Fails

If a command fails or returns BLOCKED:
1. **Do not bypass the failure.** Guardrails are there to protect you.
2. **Do not mark the task as complete.**
3. **Open the relevant report** in the `reports/` directory.
4. **Identify the exact error.** The terminal output will point you to the right place.
5. **Fix only the scoped blocker.** Do not try to fix everything at once.
6. **Run validation again.**
7. **If unclear, stop and ask for a human review.**

## 7. Non-Claims

AgentOS is a programmable guardrail layer. It is **not**:
- A backend service or cloud platform.
- A vector database or RAG system.
- A fully autonomous agent platform.
- A guarantee of bug-free AI output.
- A replacement for human approval or engineering responsibility.

## 8. Next Safe Action

- **If validation passes:** Continue with another small, documentation-heavy or low-risk task to gain confidence in the workflow.
- **If validation fails:** Focus exclusively on fixing the validation path. A broken guardrail is more dangerous than no guardrail at all.
