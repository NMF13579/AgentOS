# Scenario: Recovering from Failed Validation

This scenario demonstrates the correct process for an external user when a validation check fails.

## 1. Initial Failure

The user runs the unified validation entrypoint:
```bash
python3 scripts/agentos-validate.py all
```

**Result:**
```text
Overall result: FAIL
Checks run: 3
Failed checks: 1
Reason: scope violations detected
Violation details:
- changed file outside allowed_paths: README.md
```

## 2. Correct Interpretation

- **Do NOT** mark the task as complete.
- **Do NOT** try to push the change.
- **Result Type:** `FAIL` (a required structural rule was violated).

## 3. Investigation

1. Open the detailed scope report: `reports/write-scope/scope-report.md` (or terminal output).
2. Confirm which file was touched: `README.md`.
3. Check the current active task: `tasks/active-task.md`.
4. Observe that `README.md` is NOT in the `allowed_paths` list for this specific task.

## 4. Scoped Fix

1. Open `tasks/active-task.md`.
2. Add `README.md` to the `allowed_paths` list within the `scope_control:` block.
3. Save the task file.

## 5. Rerun and Verification

Rerun the exact same command:
```bash
python3 scripts/agentos-validate.py all
```

**Result:**
```text
Overall result: PASS
Checks run: 3
Failed checks: 0
Human action required: NO
```

## 6. Success

The user has now successfully resolved a blocker using the AgentOS feedback loop. They can now proceed to commit their changes.
