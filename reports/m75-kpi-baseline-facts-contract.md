# M75.3 — KPI Baseline Facts Contract

## 1. Purpose
This report establishes the KPI baseline facts contract for the AgentOS codebase. This is a read-only KPI facts contract and single report creation task. It defines the allowed KPI categories, fact definitions, and calculation rules to support factual tracking, without creating thresholds, scores, grades, or release decisions.

## 2. Precondition Check
The precondition capability predicate model report was checked.
- `precondition_artifact_exists: true`
- `precondition_artifact_readable: true`
- `precondition_final_status_value: "M75_CAPABILITY_PREDICATE_MODEL_COMPLETE_WITH_WARNINGS"`
- `precondition_readiness_value: "true_with_warnings"`

## 3. KPI Contract Boundary
This KPI contract serves report purposes only and is not a canonical document. It does not establish thresholds, scores, grades, or recommendation logic.
- `kpi_contract_is_report_only: true`
- `kpi_contract_is_canonical: false`
- `kpi_contract_creates_thresholds: false`
- `kpi_contract_creates_score: false`
- `kpi_contract_creates_grade: false`
- `kpi_contract_creates_approval_logic: false`
- `kpi_contract_creates_readiness_decision: false`
- `kpi_contract_creates_m76_recommendation_logic: false`

## 4. Source Evidence Inputs
The factual measurements are based on evidence documents from M68 through M74.

## 5. KPI Categories
The allowed KPI categories are:
- `governance_facts`
- `validation_facts`
- `regression_facts`
- `drift_facts`
- `evidence_facts`
- `operator_surface_facts`
- `risk_facts`

## 6. KPI Fact Definitions
The defined KPI facts are listed below:

### KPI Fact 1: protected_artifact_count
- `kpi_id: "protected_artifact_count"`
- `kpi_name: "Protected Artifact Count"`
- `category: "governance_facts"`
- `description: "Factual count of protected artifacts defined in governance configuration."`
- `source_artifact: "reports/m68-protected-artifacts.json"`
- `calculation_method: "count matching fields"`
- `allowed_value_type: "integer"`
- `unknown_handling: "value: 'unknown', unknown_reason: 'source report missing or unreadable'"`
- `approval_boundary: "Represents a factual artifact count and does not approve the governance configuration or compliance state."`

### KPI Fact 2: canonical_artifact_count
- `kpi_id: "canonical_artifact_count"`
- `kpi_name: "Canonical Artifact Count"`
- `category: "governance_facts"`
- `description: "Factual count of canonical artifacts registered in repository registry."`
- `source_artifact: "ROUTES-REGISTRY.md"`
- `calculation_method: "count matching fields"`
- `allowed_value_type: "integer"`
- `unknown_handling: "value: 'unknown', unknown_reason: 'source registry missing or unreadable'"`
- `approval_boundary: "Represents a factual registered artifact count and does not constitute authorization or approval."`

### KPI Fact 3: owner_gap_count
- `kpi_id: "owner_gap_count"`
- `kpi_name: "Owner Gap Count"`
- `category: "governance_facts"`
- `description: "Factual count of ownership gaps in the repository."`
- `source_artifact: "reports/m68-owner-gaps.json"`
- `calculation_method: "count matching fields"`
- `allowed_value_type: "integer"`
- `unknown_handling: "value: 'unknown', unknown_reason: 'source gaps file missing or unreadable'"`
- `approval_boundary: "Factual gap count only and does not constitute gap approval or closure."`

### KPI Fact 4: unknown_file_count
- `kpi_id: "unknown_file_count"`
- `kpi_name: "Unknown File Count"`
- `category: "drift_facts"`
- `description: "Factual count of unknown or untracked files discovered during repo scans."`
- `source_artifact: "reports/m68-anomaly-grep.txt"`
- `calculation_method: "count matching fields"`
- `allowed_value_type: "integer"`
- `unknown_handling: "value: 'unknown', unknown_reason: 'source anomaly file missing or unreadable'"`
- `approval_boundary: "Factual count of anomaly files and does not constitute approval or acceptance of drift."`

### KPI Fact 5: legacy_entrypoint_count
- `kpi_id: "legacy_entrypoint_count"`
- `kpi_name: "Legacy Entrypoint Count"`
- `category: "drift_facts"`
- `description: "Factual count of legacy entrypoint scripts in the repository."`
- `source_artifact: "reports/m71-script-inventory.json"`
- `calculation_method: "count matching fields"`
- `allowed_value_type: "integer"`
- `unknown_handling: "value: 'unknown', unknown_reason: 'source script inventory missing or unreadable'"`
- `approval_boundary: "Represents legacy script count and does not authorize execution or removal."`

### KPI Fact 6: validation_entrypoint_count
- `kpi_id: "validation_entrypoint_count"`
- `kpi_name: "Validation Entrypoint Count"`
- `category: "validation_facts"`
- `description: "Factual count of validation entrypoints."`
- `source_artifact: "reports/m73-validation-entrypoint-inventory.md"`
- `calculation_method: "count matching fields"`
- `allowed_value_type: "integer"`
- `unknown_handling: "value: 'unknown', unknown_reason: 'source validation inventory missing or unreadable'"`
- `approval_boundary: "Counts entrypoints only and does not approve validation rules or logic."`

### KPI Fact 7: regression_fixture_count
- `kpi_id: "regression_fixture_count"`
- `kpi_name: "Regression Fixture Count"`
- `category: "regression_facts"`
- `description: "Factual count of dispatcher regression fixtures."`
- `source_artifact: "reports/m74-regression-evidence-report.md"`
- `calculation_method: "count matching fields"`
- `allowed_value_type: "integer"`
- `unknown_handling: "value: 'unknown', unknown_reason: 'source evidence report missing or unreadable'"`
- `approval_boundary: "Counts regression fixtures only and does not approve fixture correctness or dispatcher compatibility."`

### KPI Fact 8: essential_fixture_not_run_count
- `kpi_id: "essential_fixture_not_run_count"`
- `kpi_name: "Essential Fixture Not Run Count"`
- `category: "regression_facts"`
- `description: "Factual count of essential fixtures that were not run."`
- `source_artifact: "reports/m74-regression-evidence-report.md"`
- `calculation_method: "count matching fields"`
- `allowed_value_type: "integer"`
- `unknown_handling: "value: 'unknown', unknown_reason: 'source evidence report missing or unreadable'"`
- `approval_boundary: "Records untested fixtures and does not approve missing test runs."`

### KPI Fact 9: warning_count
- `kpi_id: "warning_count"`
- `kpi_name: "Warning Count"`
- `category: "risk_facts"`
- `description: "Factual count of warnings carried forward."`
- `source_artifact: "reports/m75-evidence-inventory.md"`
- `calculation_method: "count matching warnings"`
- `allowed_value_type: "integer"`
- `unknown_handling: "value: 'unknown', unknown_reason: 'source evidence report missing or unreadable'"`
- `approval_boundary: "Records active warning count only; does not approve, bypass, or resolve warnings."`

### KPI Fact 10: blocker_count
- `kpi_id: "blocker_count"`
- `kpi_name: "Blocker Count"`
- `category: "risk_facts"`
- `description: "Factual count of active blockers carried forward."`
- `source_artifact: "reports/m75-evidence-inventory.md"`
- `calculation_method: "count matching blockers"`
- `allowed_value_type: "integer"`
- `unknown_handling: "value: 'unknown', unknown_reason: 'source evidence report missing or unreadable'"`
- `approval_boundary: "Records active blocker count; does not approve or authorize blocker bypass."`

### KPI Fact 11: required_fix_task_count
- `kpi_id: "required_fix_task_count"`
- `kpi_name: "Required Fix Task Count"`
- `category: "risk_facts"`
- `description: "Factual count of required fix tasks for open gaps."`
- `source_artifact: "reports/m74-regression-evidence-report.md"`
- `calculation_method: "count matching fields"`
- `allowed_value_type: "integer"`
- `unknown_handling: "value: 'unknown', unknown_reason: 'source reports missing or unreadable'"`
- `approval_boundary: "Records required fix tasks; does not constitute creation, authorization, or completion of those tasks."`

### KPI Fact 12: bootstrap_doc_count
- `kpi_id: "bootstrap_doc_count"`
- `kpi_name: "Bootstrap Doc Count"`
- `category: "evidence_facts"`
- `description: "Factual count of canonical bootstrap documentation files."`
- `source_artifact: "llms.txt"`
- `calculation_method: "count matching fields"`
- `allowed_value_type: "integer"`
- `unknown_handling: "value: 'unknown', unknown_reason: 'source bootstrap document missing or unreadable'"`
- `approval_boundary: "Factual count of bootstrap links; does not constitute approval of documentation content."`

### KPI Fact 13: operator_steps_count
- `kpi_id: "operator_steps_count"`
- `kpi_name: "Operator Steps Count"`
- `category: "operator_surface_facts"`
- `description: "Factual count of manual steps required by the operator."`
- `source_artifact: "reports/m74-regression-action-review.md"`
- `calculation_method: "count matching fields"`
- `allowed_value_type: "integer"`
- `unknown_handling: "value: 'unknown', unknown_reason: 'source action review missing or unreadable'"`
- `approval_boundary: "Factual count of manual steps; does not authorize or validate manual operations."`

### KPI Fact 14: prompt_surface_estimate
- `kpi_id: "prompt_surface_estimate"`
- `kpi_name: "Prompt Surface Estimate"`
- `category: "operator_surface_facts"`
- `description: "Factual count of prompt files or configurations evaluated."`
- `source_artifact: "reports/m68-prompt-metrics.json"`
- `calculation_method: "count matching fields"`
- `allowed_value_type: "integer"`
- `unknown_handling: "value: 'unknown', unknown_reason: 'source prompt metrics missing or unreadable'"`
- `approval_boundary: "Records prompt configuration counts only and does not constitute approval of prompts."`

### KPI Fact 15: approval_simulation_count
- `kpi_id: "approval_simulation_count"`
- `kpi_name: "Approval Simulation Count"`
- `category: "governance_facts"`
- `description: "Factual count of simulated approvals detected."`
- `source_artifact: "reports/m75-m74-completion-intake.md"`
- `calculation_method: "count matching fields"`
- `allowed_value_type: "integer"`
- `unknown_handling: "value: 'unknown', unknown_reason: 'source intake report missing or unreadable'"`
- `approval_boundary: "Factual count of simulated approvals; does not approve or bypass human review gates."`

### KPI Fact 16: lifecycle_violation_count
- `kpi_id: "lifecycle_violation_count"`
- `kpi_name: "Lifecycle Violation Count"`
- `category: "governance_facts"`
- `description: "Factual count of lifecycle mutations detected without governance."`
- `source_artifact: "reports/m75-m74-completion-intake.md"`
- `calculation_method: "count matching fields"`
- `allowed_value_type: "integer"`
- `unknown_handling: "value: 'unknown', unknown_reason: 'source intake report missing or unreadable'"`
- `approval_boundary: "Records lifecycle mutations and does not constitute authorization or approval."`

### KPI Fact 17: m76_artifact_count
- `kpi_id: "m76_artifact_count"`
- `kpi_name: "M76 Artifact Count"`
- `category: "evidence_facts"`
- `description: "Factual count of M76 artifacts detected."`
- `source_artifact: "reports/m75-m74-completion-intake.md"`
- `calculation_method: "count matching artifacts"`
- `allowed_value_type: "integer"`
- `unknown_handling: "value: 'unknown', unknown_reason: 'source intake report missing or unreadable'"`
- `approval_boundary: "Records premature M76 artifacts; does not authorize or approve M76 planning or execution."`

## 7. Calculation Method Rules
All measurements are performed deterministically based on counts, boolean presence checks, and metadata extraction. No subjective estimations are allowed.

## 8. Unknown Handling
If a source artifact is missing or unreadable, the KPI fact returns an explicit unknown state.
- `kpi_unknown_handling_defined_count: 17`

## 9. Forbidden Threshold / Score / Recommendation Check
This contract does not establish threshold boundaries, quality grading structures, or recommendation logic.
- `forbidden_threshold_present: false`
- `forbidden_good_bad_scoring_present: false`
- `forbidden_maturity_score_present: false`
- `forbidden_health_score_present: false`
- `forbidden_quality_score_present: false`
- `forbidden_overall_grade_present: false`
- `forbidden_automatic_readiness_decision_present: false`
- `forbidden_m76_recommendation_logic_present: false`

## 10. Approval / Lifecycle / Repair / M76 Boundary Check
No boundary violations occurred.
- `approval_claim_created: false`
- `lifecycle_mutation_occurred: false`
- `repair_authorized: false`
- `fix_tasks_created: false`
- `m76_started: false`
- `m76_artifacts_created: false`

## 11. Warning Carry-Forward
Warnings are carried forward.
- `warnings_carried_forward: true`
- `warning_count: 2`
- `warnings:`
  - "Upstream warning carried forward: M74 completed with warnings due to 33 regression failures."
  - "Upstream warning carried forward: 9 gap categories require fix tasks."

## 12. Blockers
No hard blockers prevent contract definition, but the following blockers are carried forward:
- `blocker_count: 2`
- `blockers:`
  - "33 dispatcher regression fixture failures requiring fix tasks before full code closure."
  - "Human review is required before M75 execution."

## 13. Local Final Status
- `FINAL_STATUS: "M75_KPI_BASELINE_FACTS_CONTRACT_COMPLETE_WITH_WARNINGS"`

## 14. Output Readiness
- `may_prepare_m75_4: "true_with_warnings"`

## 15. Boundary Statement
M75.3 created the KPI baseline facts contract report. This task does not approve M74, M75, or AgentOS core. It does not establish thresholds, scores, grades, automatic readiness decisions, or recommendation logic, and does not create canonical documents. It does not repair code, create fix tasks, mutate lifecycle state, start 75.4, or start M76. Output readiness `may_prepare_m75_4` represents roadmap preparation readiness only and does not constitute approval or start the next task. Human review remains required.

---

### Machine-Readable Metadata
```yaml
task_id: "75.3"
task_name: "KPI Baseline Facts Contract"
precondition_artifact: "reports/m75-core-capability-predicate-model.md"

precondition_artifact_exists: true
precondition_artifact_readable: true
precondition_final_status_present: true
precondition_final_status_value: "M75_CAPABILITY_PREDICATE_MODEL_COMPLETE_WITH_WARNINGS"
precondition_final_status_acceptable: true
precondition_readiness_present: true
precondition_readiness_value: "true_with_warnings"
precondition_readiness_acceptable: true

kpi_contract_artifact: "reports/m75-kpi-baseline-facts-contract.md"
kpi_contract_is_report_only: true
kpi_contract_is_canonical: false
kpi_contract_creates_thresholds: false
kpi_contract_creates_score: false
kpi_contract_creates_grade: false
kpi_contract_creates_approval_logic: false
kpi_contract_creates_readiness_decision: false
kpi_contract_creates_m76_recommendation_logic: false

kpi_categories:
  - governance_facts
  - validation_facts
  - regression_facts
  - drift_facts
  - evidence_facts
  - operator_surface_facts
  - risk_facts

kpi_facts:
  - kpi_id: "protected_artifact_count"
    kpi_name: "Protected Artifact Count"
    category: "governance_facts"
    description: "Factual count of protected artifacts defined in governance configuration."
    source_artifact: "reports/m68-protected-artifacts.json"
    calculation_method: "count matching fields"
    allowed_value_type: "integer"
    unknown_handling: "value: 'unknown', unknown_reason: 'source report missing or unreadable'"
    approval_boundary: "Represents a factual artifact count and does not approve the governance configuration or compliance state."
  - kpi_id: "canonical_artifact_count"
    kpi_name: "Canonical Artifact Count"
    category: "governance_facts"
    description: "Factual count of canonical artifacts registered in repository registry."
    source_artifact: "ROUTES-REGISTRY.md"
    calculation_method: "count matching fields"
    allowed_value_type: "integer"
    unknown_handling: "value: 'unknown', unknown_reason: 'source registry missing or unreadable'"
    approval_boundary: "Represents a factual registered artifact count and does not constitute authorization or approval."
  - kpi_id: "owner_gap_count"
    kpi_name: "Owner Gap Count"
    category: "governance_facts"
    description: "Factual count of ownership gaps in the repository."
    source_artifact: "reports/m68-owner-gaps.json"
    calculation_method: "count matching fields"
    allowed_value_type: "integer"
    unknown_handling: "value: 'unknown', unknown_reason: 'source gaps file missing or unreadable'"
    approval_boundary: "Factual gap count only and does not constitute gap approval or closure."
  - kpi_id: "unknown_file_count"
    kpi_name: "Unknown File Count"
    category: "drift_facts"
    description: "Factual count of unknown or untracked files discovered during repo scans."
    source_artifact: "reports/m68-anomaly-grep.txt"
    calculation_method: "count matching fields"
    allowed_value_type: "integer"
    unknown_handling: "value: 'unknown', unknown_reason: 'source anomaly file missing or unreadable'"
    approval_boundary: "Factual count of anomaly files and does not constitute approval or acceptance of drift."
  - kpi_id: "legacy_entrypoint_count"
    kpi_name: "Legacy Entrypoint Count"
    category: "drift_facts"
    description: "Factual count of legacy entrypoint scripts in the repository."
    source_artifact: "reports/m71-script-inventory.json"
    calculation_method: "count matching fields"
    allowed_value_type: "integer"
    unknown_handling: "value: 'unknown', unknown_reason: 'source script inventory missing or unreadable'"
    approval_boundary: "Represents legacy script count and does not authorize execution or removal."
  - kpi_id: "validation_entrypoint_count"
    kpi_name: "Validation Entrypoint Count"
    category: "validation_facts"
    description: "Factual count of validation entrypoints."
    source_artifact: "reports/m73-validation-entrypoint-inventory.md"
    calculation_method: "count matching fields"
    allowed_value_type: "integer"
    unknown_handling: "value: 'unknown', unknown_reason: 'source validation inventory missing or unreadable'"
    approval_boundary: "Counts entrypoints only and does not approve validation rules or logic."
  - kpi_id: "regression_fixture_count"
    kpi_name: "Regression Fixture Count"
    category: "regression_facts"
    description: "Factual count of dispatcher regression fixtures."
    source_artifact: "reports/m74-regression-evidence-report.md"
    calculation_method: "count matching fields"
    allowed_value_type: "integer"
    unknown_handling: "value: 'unknown', unknown_reason: 'source evidence report missing or unreadable'"
    approval_boundary: "Counts regression fixtures only and does not approve fixture correctness or dispatcher compatibility."
  - kpi_id: "essential_fixture_not_run_count"
    kpi_name: "Essential Fixture Not Run Count"
    category: "regression_facts"
    description: "Factual count of essential fixtures that were not run."
    source_artifact: "reports/m74-regression-evidence-report.md"
    calculation_method: "count matching fields"
    allowed_value_type: "integer"
    unknown_handling: "value: 'unknown', unknown_reason: 'source evidence report missing or unreadable'"
    approval_boundary: "Records untested fixtures and does not approve missing test runs."
  - kpi_id: "warning_count"
    kpi_name: "Warning Count"
    category: "risk_facts"
    description: "Factual count of warnings carried forward."
    source_artifact: "reports/m75-evidence-inventory.md"
    calculation_method: "count matching warnings"
    allowed_value_type: "integer"
    unknown_handling: "value: 'unknown', unknown_reason: 'source evidence report missing or unreadable'"
    approval_boundary: "Records active warning count only; does not approve, bypass, or resolve warnings."
  - kpi_id: "blocker_count"
    kpi_name: "Blocker Count"
    category: "risk_facts"
    description: "Factual count of active blockers carried forward."
    source_artifact: "reports/m75-evidence-inventory.md"
    calculation_method: "count matching blockers"
    allowed_value_type: "integer"
    unknown_handling: "value: 'unknown', unknown_reason: 'source evidence report missing or unreadable'"
    approval_boundary: "Records active blocker count; does not approve or authorize blocker bypass."
  - kpi_id: "required_fix_task_count"
    kpi_name: "Required Fix Task Count"
    category: "risk_facts"
    description: "Factual count of required fix tasks for open gaps."
    source_artifact: "reports/m74-regression-evidence-report.md"
    calculation_method: "count matching fields"
    allowed_value_type: "integer"
    unknown_handling: "value: 'unknown', unknown_reason: 'source reports missing or unreadable'"
    approval_boundary: "Records required fix tasks; does not constitute creation, authorization, or completion of those tasks."
  - kpi_id: "bootstrap_doc_count"
    kpi_name: "Bootstrap Doc Count"
    category: "evidence_facts"
    description: "Factual count of canonical bootstrap documentation files."
    source_artifact: "llms.txt"
    calculation_method: "count matching fields"
    allowed_value_type: "integer"
    unknown_handling: "value: 'unknown', unknown_reason: 'source bootstrap document missing or unreadable'"
    approval_boundary: "Factual count of bootstrap links; does not constitute approval of documentation content."
  - kpi_id: "operator_steps_count"
    kpi_name: "Operator Steps Count"
    category: "operator_surface_facts"
    description: "Factual count of manual steps required by the operator."
    source_artifact: "reports/m74-regression-action-review.md"
    calculation_method: "count matching fields"
    allowed_value_type: "integer"
    unknown_handling: "value: 'unknown', unknown_reason: 'source action review missing or unreadable'"
    approval_boundary: "Factual count of manual steps; does not authorize or validate manual operations."
  - kpi_id: "prompt_surface_estimate"
    kpi_name: "Prompt Surface Estimate"
    category: "operator_surface_facts"
    description: "Factual count of prompt files or configurations evaluated."
    source_artifact: "reports/m68-prompt-metrics.json"
    calculation_method: "count matching fields"
    allowed_value_type: "integer"
    unknown_handling: "value: 'unknown', unknown_reason: 'source prompt metrics missing or unreadable'"
    approval_boundary: "Records prompt configuration counts only and does not constitute approval of prompts."
  - kpi_id: "approval_simulation_count"
    kpi_name: "Approval Simulation Count"
    category: "governance_facts"
    description: "Factual count of simulated approvals detected."
    source_artifact: "reports/m75-m74-completion-intake.md"
    calculation_method: "count matching fields"
    allowed_value_type: "integer"
    unknown_handling: "value: 'unknown', unknown_reason: 'source intake report missing or unreadable'"
    approval_boundary: "Factual count of simulated approvals; does not approve or bypass human review gates."
  - kpi_id: "lifecycle_violation_count"
    kpi_name: "Lifecycle Violation Count"
    category: "governance_facts"
    description: "Factual count of lifecycle mutations detected without governance."
    source_artifact: "reports/m75-m74-completion-intake.md"
    calculation_method: "count matching fields"
    allowed_value_type: "integer"
    unknown_handling: "value: 'unknown', unknown_reason: 'source intake report missing or unreadable'"
    approval_boundary: "Records lifecycle mutations and does not constitute authorization or approval."
  - kpi_id: "m76_artifact_count"
    kpi_name: "M76 Artifact Count"
    category: "evidence_facts"
    description: "Factual count of M76 artifacts detected."
    source_artifact: "reports/m75-m74-completion-intake.md"
    calculation_method: "count matching artifacts"
    allowed_value_type: "integer"
    unknown_handling: "value: 'unknown', unknown_reason: 'source intake report missing or unreadable'"
    approval_boundary: "Records premature M76 artifacts; does not authorize or approve M76 planning or execution."

kpi_fact_count: 17
kpi_unknown_handling_defined_count: 17
kpi_approval_boundary_defined_count: 17

forbidden_threshold_present: false
forbidden_good_bad_scoring_present: false
forbidden_maturity_score_present: false
forbidden_health_score_present: false
forbidden_quality_score_present: false
forbidden_overall_grade_present: false
forbidden_automatic_readiness_decision_present: false
forbidden_m76_recommendation_logic_present: false

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

FINAL_STATUS: "M75_KPI_BASELINE_FACTS_CONTRACT_COMPLETE_WITH_WARNINGS"

may_prepare_m75_4: "true_with_warnings"
```
