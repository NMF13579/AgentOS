---
contract_version: 2
task_id: bad_raw_import_task
task_category: app_feature_ui
source_ux: tests/fixtures/ux-to-task/positive/approved-ux-with-ui-contract.md
source_ui_contract: docs/UI-SEMANTIC-COMPONENT-CONTRACT.md
ui_contract_required: true
ui_contract_present: true
---

Forbidden example:
- Import directly from components/ui/* in feature code.
- Import directly from @radix-ui/* in feature code.

Note: future linting should classify this as a UI task decomposition violation.
