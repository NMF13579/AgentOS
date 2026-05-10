# Troubleshooting Guide

This guide helps you interpret AgentOS validation results and recover from common failure states.

## 1. Result Meaning Table

| Result | Meaning | First-user action |
|---|---|---|
| **PASS** | The checked area passed completely. | Continue to the next safe step. |
| **PASS_WITH_WARNINGS** | Required checks passed, but known gaps remain. | Read warnings before continuing. |
| **WARNING** | Review is needed, but it may not block first use. | Read warning and decide whether it is relevant. |
| **BLOCKED** | The system stopped because continuing would be unsafe or unsupported. | **Stop** and resolve or review the blocker. |
| **NOT_READY** | The system is not ready for the claimed use. | Do not claim readiness; inspect the relevant report. |
| **FAIL** | A required check failed. | **Stop**, inspect output, fix only the scoped issue, rerun. |
| **INCONCLUSIVE** | Evidence is not trustworthy enough. | Do not rely on result; rerun or inspect manually. |
| **COMMAND_NOT_AVAILABLE** | The command/script is missing. | Check docs or repository state; do not treat as pass. |
| **INPUT_NOT_AVAILABLE** | A required input file is missing. | Restore or create the required input through a scoped task. |
| **VALIDATION_GAP** | Validation could not prove the claim. | Treat as not proven; do not proceed as if passed. |

## 2. Command-to-Report Mapping

| Command | Checks | If it fails | Where to look |
|---|---|---|---|
| `python3 scripts/validate-task.py tasks/active-task.md` | Active task structure & frontmatter. | Fix syntax or missing fields in the task file. | Terminal output. |
| `bash scripts/run-all.sh` | Tasks and verification reports. | Fix specific task or report errors. | Terminal output. |
| `python3 scripts/agentos-validate.py all` | Full repository scope and compliance. | Resolve scope violations or audit failures. | `reports/` directory. |
| `python3 scripts/audit-mvp-readiness.py` | Overall MVP readiness status. | Address identified release blockers. | `reports/audit.md`. |
| `bash scripts/test-install.sh` | Installer script integrity. | Check if files were correctly copied. | Terminal output. |
| `bash scripts/test-example-project.sh` | Example project validation flow. | Fix example project configuration. | Terminal output. |

## 3. What To Do If Something Fails

If validation fails:
1. **Stop immediately.** Do not try to "vibe-code" around the failure.
2. **Do not treat failure as success.** A failed check means a guardrail is working.
3. **Read the command output.** It usually contains the exact line or file that failed.
4. **Check the matching report** in the `reports/` folder for more details.
5. **Identify the result type.** Is it a `FAIL`, `BLOCKED`, or `NOT_READY`?
6. **Fix only the specific blocker.** Avoid large unrelated changes during troubleshooting.
7. **Rerun the exact same command** to verify the fix.
8. **Do not proceed** to release, publish, or deployment until validation passes.

## 4. When to Ask for Human Review

Request a human review when:
- You encounter a **BLOCKED** result that you don't know how to resolve.
- The result is **NOT_READY** but you believe the task is complete.
- The result is **INCONCLUSIVE** (crashes or timeouts).
- The fix involves modifying core AgentOS files (scripts, schemas, templates, policies).
- The command output and the generated report disagree.

## 5. Safe Rerun Procedure

After fixing a blocker:
1. Rerun the command that failed.
2. Confirm the original error is resolved.
3. Check if any new, unrelated failures appeared (regressions).
4. Record any remaining non-blocking warnings honestly.
5. Only proceed when the result is **PASS** or **PASS_WITH_WARNINGS**.

## 6. Prohibited Actions

- **Do not ignore failed validation.**
- **Do not edit reports manually** to make a failure disappear.
- **Do not delete validation checks** from scripts to make them pass.
- **Do not treat warnings as approval.**
- **Do not treat PASS as release approval.**
- **Do not proceed to deployment** based on AgentOS validation alone.
