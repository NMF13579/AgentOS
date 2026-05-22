---
contract_version: 2
task_id: bad_hardcoded_style
task_category: app_feature_ui
source_ux: tests/fixtures/ux-to-task/positive/approved-ux-with-ui-contract.md
source_ui_contract: docs/UI-SEMANTIC-COMPONENT-CONTRACT.md
ui_contract_required: true
ui_contract_present: true
---

Forbidden examples:
- hardcoded color #FF5733
- hardcoded spacing 16px
- hardcoded typography
- hardcoded animation
- new design token without review

Note: future linting should classify this as a UI task decomposition violation.
