# M75.2 — Deterministic Core Capability Predicate Model

## 1. Purpose
This report defines the deterministic core capability predicate model for the AgentOS codebase. This is a read-only predicate model and single report creation task. It defines factual checks for subsequent evaluation but does not assign scores, levels, overall evaluation grades, or release decisions.

## 2. Precondition Check
The precondition evidence inventory was successfully checked.
- `precondition_artifact_exists: true`
- `precondition_artifact_readable: true`
- `precondition_final_status_value: "M75_EVIDENCE_INVENTORY_COMPLETE_WITH_WARNINGS"`
- `precondition_readiness_value: "true_with_warnings"`

## 3. Predicate Model Boundary
This model is for reporting purposes only and is not a canonical document. It does not create rules, scores, or decisions.
- `predicate_model_is_report_only: true`
- `predicate_model_is_canonical: false`
- `predicate_model_creates_approval_rule: false`
- `predicate_model_creates_score: false`
- `predicate_model_creates_maturity_level: false`
- `predicate_model_creates_release_decision: false`

## 4. Source Evidence Inputs
The predicate model relies on factual evidence from M68 through M74 reports, including intake, inventory, and regression results.

## 5. Allowed Predicate Format
Each predicate defines:
1. `predicate_id` and `predicate_name`
2. `required_facts` to be evaluated
3. `source_artifacts` containing the facts
4. Deterministic conditions for `true_condition`, `false_condition`, and `unknown_condition`
5. `approval_boundary` separating facts check from authorization

## 6. Core Capability Predicate Definitions
The capability predicates are defined below:

### Predicate 1: core_facts_measured
- `predicate_id: "core_facts_measured"`
- `predicate_name: "Core Factual Inputs Measured"`
- `required_facts:`
  - "Presence and readability of M75 completion intake and evidence inventory."
- `source_artifacts:`
  - "reports/m75-m74-completion-intake.md"
  - "reports/m75-evidence-inventory.md"
- `true_condition: "Both reports/m75-m74-completion-intake.md and reports/m75-evidence-inventory.md exist, are readable, and contain non-empty status values."`
- `false_condition: "Either reports/m75-m74-completion-intake.md or reports/m75-evidence-inventory.md is missing or unreadable."`
- `unknown_condition: "Either file exists but the final status value cannot be parsed or verified."`
- `approval_boundary: "Verifies the presence of intake and inventory facts; does not constitute approval of those facts."`

### Predicate 2: core_evidence_inventory_present
- `predicate_id: "core_evidence_inventory_present"`
- `predicate_name: "Core Evidence Inventory Present"`
- `required_facts:`
  - "Presence, readability, and content structure of M68-M74 inventory."
- `source_artifacts:`
  - "reports/m75-evidence-inventory.md"
- `true_condition: "reports/m75-evidence-inventory.md exists, is readable, contains artifact_inventory list, and artifact_count is greater than 0."`
- `false_condition: "reports/m75-evidence-inventory.md does not exist, is unreadable, or contains an empty inventory."`
- `unknown_condition: "reports/m75-evidence-inventory.md exists but its internal inventory structure is malformed or unparseable."`
- `approval_boundary: "Confirms presence of the inventory matrix; does not constitute validation or approval of the inventoried files."`

### Predicate 3: core_validation_authority_facts_present
- `predicate_id: "core_validation_authority_facts_present"`
- `predicate_name: "Core Validation Authority Facts Present"`
- `required_facts:`
  - "Verification of validation registry entrypoints and thin-dispatcher contracts."
- `source_artifacts:`
  - "reports/m73-thin-dispatcher-contract-creation-report.md"
  - "reports/m73-thin-dispatcher-implementation-report.md"
  - "reports/m73-validation-entrypoint-inventory.md"
- `true_condition: "All three source reports exist, are readable, and record thin-dispatcher registry mapping details without relying on prose claims."`
- `false_condition: "Any of the three source reports is missing or unreadable."`
- `unknown_condition: "The files exist but their internal structures are malformed or missing key mappings."`
- `approval_boundary: "Records presence of validation metadata; does not approve validation authority or dispatcher implementation."`

### Predicate 4: core_governance_facts_present
- `predicate_id: "core_governance_facts_present"`
- `predicate_name: "Core Governance Facts Present"`
- `required_facts:`
  - "Verification of owner mappings, protected artifacts, and checkpoint compliance."
- `source_artifacts:`
  - "reports/m68-protected-artifacts.json"
  - "reports/m68-owner-gaps.json"
- `true_condition: "Both reports exist, are readable, and contain owner and protected artifact datasets."`
- `false_condition: "Either reports/m68-protected-artifacts.json or reports/m68-owner-gaps.json is missing or unreadable."`
- `unknown_condition: "The files are present but their JSON datasets are malformed or unparseable."`
- `approval_boundary: "Verifies the presence of governance files; does not approve governance configurations or platform-level status."`

### Predicate 5: core_regression_protection_facts_present
- `predicate_id: "core_regression_protection_facts_present"`
- `predicate_name: "Core Regression Protection Facts Present"`
- `required_facts:`
  - "Verification of M74 regression test executions and safe values."
- `source_artifacts:`
  - "reports/m74-regression-evidence-report.md"
  - "reports/m74-completion-review.md"
- `true_condition: "M74 reports exist and verify that 35 fixtures were run, no fixture NOT_RUN was counted as PASS, and the following values are explicitly recorded: unknown_became_pass is false, not_run_became_pass is false, warnings_hidden_by_exit_0 is false, and ci_green_treated_as_approval is false."`
- `false_condition: "M74 reports do not exist or are unreadable."`
- `unknown_condition: "Reports exist but fail to state the required regression metrics or safe values."`
- `approval_boundary: "Verifies that regression metrics were collected; does not approve runner, fixtures, or dispatcher behavior."`

### Predicate 6: core_release_candidate_input_facts_present
- `predicate_id: "core_release_candidate_input_facts_present"`
- `predicate_name: "Core Release Candidate Input Facts Present"`
- `required_facts:`
  - "Verifies presence of M75 intake and model artifacts for planning review."
- `source_artifacts:`
  - "reports/m75-evidence-inventory.md"
  - "reports/m75-core-capability-predicate-model.md"
- `true_condition: "All preceding M75 reports and milestone reviews exist and contain valid status and readiness tokens indicating complete facts consolidation."`
- `false_condition: "Preceding M75 or M74 reviews are missing or contain blocked status tokens."`
- `unknown_condition: "Reports are present but their status tokens are unparseable."`
- `approval_boundary: "Defines inputs for future reviews; does not approve release candidate status or milestones."`

## 7. Unknown Handling
If any required fact cannot be verified, the predicate evaluates to `unknown`. It does not fall back to true, false, or partial success.
- `predicate_unknown_handling_defined_count: 6`

## 8. Forbidden Scoring / Leveling Check
This model does not contain maturity levels, scores, overall evaluation grades, or release decisions.
- `forbidden_maturity_score_present: false`
- `forbidden_health_score_present: false`
- `forbidden_quality_score_present: false`
- `forbidden_overall_grade_present: false`
- `forbidden_subjective_level_assignment_present: false`
- `forbidden_release_decision_present: false`

## 9. Approval / Lifecycle / Repair / M76 Boundary Check
No boundary violations occurred.
- `approval_claim_created: false`
- `lifecycle_mutation_occurred: false`
- `repair_authorized: false`
- `fix_tasks_created: false`
- `m76_started: false`
- `m76_artifacts_created: false`

## 10. Warning Carry-Forward
Warnings are carried forward.
- `warnings_carried_forward: true`
- `warning_count: 2`
- `warnings:`
  - "Upstream warning carried forward: M74 completed with warnings due to 33 regression failures."
  - "Upstream warning carried forward: 9 gap categories require fix tasks."

## 11. Blockers
No hard blockers prevent model definition, but the following blockers are carried forward:
- `blocker_count: 2`
- `blockers:`
  - "33 dispatcher regression fixture failures requiring fix tasks before full code closure."
  - "Human review is required before M75 execution."

## 12. Local Final Status
- `FINAL_STATUS: "M75_CAPABILITY_PREDICATE_MODEL_COMPLETE_WITH_WARNINGS"`

## 13. Output Readiness
- `may_prepare_m75_3: "true_with_warnings"`

## 14. Boundary Statement
M75.2 created the capability predicate model report. This task does not approve M74, M75, or AgentOS core. It does not create scores, grades, levels, or release decisions, and does not create canonical documents. It does not repair code, create fix tasks, mutate lifecycle state, start 75.3, or start M76. Output readiness `may_prepare_m75_3` represents roadmap preparation readiness only and does not constitute approval or start the next task. Human review remains required.

---

### Machine-Readable Metadata
```yaml
task_id: "75.2"
task_name: "Deterministic Core Capability Predicate Model"
precondition_artifact: "reports/m75-evidence-inventory.md"

precondition_artifact_exists: true
precondition_artifact_readable: true
precondition_final_status_present: true
precondition_final_status_value: "M75_EVIDENCE_INVENTORY_COMPLETE_WITH_WARNINGS"
precondition_final_status_acceptable: true
precondition_readiness_present: true
precondition_readiness_value: "true_with_warnings"
precondition_readiness_acceptable: true

predicate_model_artifact: "reports/m75-core-capability-predicate-model.md"
predicate_model_is_report_only: true
predicate_model_is_canonical: false
predicate_model_creates_approval_rule: false
predicate_model_creates_score: false
predicate_model_creates_maturity_level: false
predicate_model_creates_release_decision: false

capability_predicates:
  - predicate_id: "core_facts_measured"
    predicate_name: "Core Factual Inputs Measured"
    required_facts:
      - "Presence and readability of M75 completion intake and evidence inventory."
    source_artifacts:
      - "reports/m75-m74-completion-intake.md"
      - "reports/m75-evidence-inventory.md"
    true_condition: "Both reports/m75-m74-completion-intake.md and reports/m75-evidence-inventory.md exist, are readable, and contain non-empty status values."
    false_condition: "Either reports/m75-m74-completion-intake.md or reports/m75-evidence-inventory.md is missing or unreadable."
    unknown_condition: "Either file exists but the final status value cannot be parsed or verified."
    approval_boundary: "Verifies the presence of intake and inventory facts; does not constitute approval of those facts."
  - predicate_id: "core_evidence_inventory_present"
    predicate_name: "Core Evidence Inventory Present"
    required_facts:
      - "Presence, readability, and content structure of M68-M74 inventory."
    source_artifacts:
      - "reports/m75-evidence-inventory.md"
    true_condition: "reports/m75-evidence-inventory.md exists, is readable, contains artifact_inventory list, and artifact_count is greater than 0."
    false_condition: "reports/m75-evidence-inventory.md does not exist, is unreadable, or contains an empty inventory."
    unknown_condition: "reports/m75-evidence-inventory.md exists but its internal inventory structure is malformed or unparseable."
    approval_boundary: "Confirms presence of the inventory matrix; does not constitute validation or approval of the inventoried files."
  - predicate_id: "core_validation_authority_facts_present"
    predicate_name: "Core Validation Authority Facts Present"
    required_facts:
      - "Verification of validation registry entrypoints and thin-dispatcher contracts."
    source_artifacts:
      - "reports/m73-thin-dispatcher-contract-creation-report.md"
      - "reports/m73-thin-dispatcher-implementation-report.md"
      - "reports/m73-validation-entrypoint-inventory.md"
    true_condition: "All three source reports exist, are readable, and record thin-dispatcher registry mapping details without relying on prose claims."
    false_condition: "Any of the three source reports is missing or unreadable."
    unknown_condition: "The files exist but their internal structures are malformed or missing key mappings."
    approval_boundary: "Records presence of validation metadata; does not approve validation authority or dispatcher implementation."
  - predicate_id: "core_governance_facts_present"
    predicate_name: "Core Governance Facts Present"
    required_facts:
      - "Verification of owner mappings, protected artifacts, and checkpoint compliance."
    source_artifacts:
      - "reports/m68-protected-artifacts.json"
      - "reports/m68-owner-gaps.json"
    true_condition: "Both reports exist, are readable, and contain owner and protected artifact datasets."
    false_condition: "Either reports/m68-protected-artifacts.json or reports/m68-owner-gaps.json is missing or unreadable."
    unknown_condition: "The files are present but their JSON datasets are malformed or unparseable."
    approval_boundary: "Verifies the presence of governance files; does not approve governance configurations or platform-level status."
  - predicate_id: "core_regression_protection_facts_present"
    predicate_name: "Core Regression Protection Facts Present"
    required_facts:
      - "Verification of M74 regression test executions and safe values."
    source_artifacts:
      - "reports/m74-regression-evidence-report.md"
      - "reports/m74-completion-review.md"
    true_condition: "M74 reports exist and verify that 35 fixtures were run, no fixture NOT_RUN was counted as PASS, and the following values are explicitly recorded: unknown_became_pass is false, not_run_became_pass is false, warnings_hidden_by_exit_0 is false, and ci_green_treated_as_approval is false."
    false_condition: "M74 reports do not exist or are unreadable."
    unknown_condition: "Reports exist but fail to state the required regression metrics or safe values."
    approval_boundary: "Verifies that regression metrics were collected; does not approve runner, fixtures, or dispatcher behavior."
  - predicate_id: "core_release_candidate_input_facts_present"
    predicate_name: "Core Release Candidate Input Facts Present"
    required_facts:
      - "Verifies presence of M75 intake and model artifacts for planning review."
    source_artifacts:
      - "reports/m75-evidence-inventory.md"
      - "reports/m75-core-capability-predicate-model.md"
    true_condition: "All preceding M75 reports and milestone reviews exist and contain valid status and readiness tokens indicating complete facts consolidation."
    false_condition: "Preceding M75 or M74 reviews are missing or contain blocked status tokens."
    unknown_condition: "Reports are present but their status tokens are unparseable."
    approval_boundary: "Defines inputs for future reviews; does not approve release candidate status or milestones."

predicate_count: 6
predicate_unknown_handling_defined_count: 6
predicate_approval_boundary_defined_count: 6

forbidden_maturity_score_present: false
forbidden_health_score_present: false
forbidden_quality_score_present: false
forbidden_overall_grade_present: false
forbidden_subjective_level_assignment_present: false
forbidden_release_decision_present: false

approval_claim_created: false
lifecycle_mutation_occurred: false
repair_authorized: false
fix_tasks_created: false
m76_started: false
m76_artifacts_created: false

warnings_carried_forward: true
warning_count: 2
warnings:
  - "Upstream warning carried forward: M74 completed with warnings due to 33 regression failures."
  - "Upstream warning carried forward: 9 gap categories require fix tasks."

blocker_count: 2
blockers:
  - "33 dispatcher regression fixture failures requiring fix tasks before full code closure."
  - "Human review is required before M75 execution."

FINAL_STATUS: "M75_CAPABILITY_PREDICATE_MODEL_COMPLETE_WITH_WARNINGS"

may_prepare_m75_3: "true_with_warnings"
```
