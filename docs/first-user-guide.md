# First-User Guide

Welcome to AgentOS! This guide is for first-time users who have successfully installed or copied AgentOS and want to understand how to use it safely with their AI coding agent.

## 1. What AgentOS is
AgentOS is a programmable guardrail layer for AI-assisted coding workflows. It helps structure tasks, scope, validation, evidence, and human checkpoints.

## 2. What AgentOS is not
AgentOS is **not**:
- A backend or cloud platform.
- A vector database or RAG system.
- A full autonomous agent platform.
- A guarantee of bug-free AI output.
- A replacement for human approval.
- Production deployment approval.

## 3. Who this guide is for
New users who want to see AgentOS in action without risking their existing project codebase.

## 4. Before you start
Ensure you have installed AgentOS into your repository. See [docs/installation.md](installation.md) if you haven't done this yet.

## 5. First safe path
The recommended first path is to verify your current state and then perform a tiny, non-functional change to understand the feedback loop.

## 6. First commands to run
Run these to confirm your baseline:
```bash
# 1. Validate the active task contract
python3 scripts/validate-task.py tasks/active-task.md

# 2. Run the core validation suite
bash scripts/run-all.sh

# 3. Run full unified validation (if available)
python3 scripts/agentos-validate.py all

# 4. Check MVP readiness audit (if available)
python3 scripts/audit-mvp-readiness.py
```

## 7. How to inspect reports
After running validation, check the `reports/` directory. Each major validator writes its evidence there. If a command fails, the report will tell you why.

## 8. How to choose a tiny first task
Start with something that cannot break your app:
- Documentation wording improvement.
- README clarity improvement.
- Quickstart review.
- Example scenario reading / validation-only check.

**Do not start with:** Script changes, schema changes, or security/policy rewrites.

## 9. How to ask an AI coding agent to help
Copy the prompt from `prompts/first-user-agent.md` and give it to your AI tool. It instructs the agent to respect AgentOS rules.

## 10. What to do after PASS
If validation passes, you have successfully completed a cycle! You can now move on to slightly more complex documentation or low-risk tasks.

## 11. What to do after WARNING
Read the warning in the terminal or report. If you understand the gap and it doesn't block your current goal, you can continue. If unsure, stop.

## 12. What to do after BLOCKED / NOT_READY / FAIL / INCONCLUSIVE
- **BLOCKED:** Stop and resolve the specific blocker mentioned.
- **NOT_READY:** Do not claim readiness; inspect the relevant report.
- **FAIL:** Stop, inspect output, fix only the scoped issue, and rerun.
- **INCONCLUSIVE:** Evidence is not trustworthy; rerun or inspect manually.

## 13. When to ask for human review
Ask for review when you see a **BLOCKED** status or if you need to modify core AgentOS files (scripts, schemas, templates).

## 14. What not to do
- Do not ignore failed validation.
- Do not delete checks to make a command pass.
- Do not treat PASS as release approval.

## 15. Non-claims
Public MVP candidate usage does not include web UI, cloud/server platform, IDE plugins, or multi-agent orchestration.
