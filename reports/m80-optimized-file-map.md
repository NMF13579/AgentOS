## Human Summary

- Can next M80 task be prepared: true_with_warnings
- Does this create new baseline: false
- Does this authorize cleanup: false
- Does this update repo-map/context-index: false
- Does this start M81: false
- Main blockers:
  - "none"
- Main warnings:
  - "M80_1_WARNINGS_CARRIED_FORWARD"
  - "M79_WARNINGS_CARRIED_FORWARD"
  - "M78_WARNINGS_CARRIED_FORWARD"
  - "LOW_CONFIDENCE_CLASSIFICATIONS_PRESENT"
  - "HEURISTIC_CLASSIFICATIONS_PRESENT"
  - "PATH_PATTERN_EVIDENCE_USED"
  - "REMAINING_COPY_OR_DUPLICATE_FILES_PRESENT"
  - "REMAINING_STALE_REPORTS_PRESENT"
  - "GENERATED_OR_CACHE_FILES_PRESENT"
  - "GIT_STATUS_HAS_UNRELATED_CHANGES"
- Tracked files mapped: 5252
- Unknown files: 0
- Unknown file ratio: 0.00%
- Low-confidence classifications: 340
- Path-pattern evidence items: 340
- Items requiring 80.4 review: 340
- Required primary areas mapped: true
- Files allowed for cleanup by 80.2: 0
- M81 artifacts created: false
- M81 task briefs created: false
- Next readiness field: "may_prepare_m80_3: true_with_warnings"
Human Summary must match machine-readable fields.

# Title
M80.2 Optimized File Map v2

# Purpose
Build a bounded file map of the repository as it exists now. This is mapping only. It does not authorize cleanup, mutation, or downstream milestone start.

# 80.1 Evidence Intake Check
- `reports/m80-consolidation-evidence-intake.md` exists: true
- `reports/m80-consolidation-evidence-intake.md` readable: true
- `m80_1_final_status_detected`: `FINAL_STATUS: M80_CONSOLIDATION_EVIDENCE_INTAKE_COMPLETE_WITH_WARNINGS`
- `m80_1_final_status_acceptable`: true
- `m80_1_readiness_detected`: `may_prepare_m80_2: true_with_warnings`
- `m80_1_readiness_acceptable`: true

# Mapping Method
I used tracked-file inventory from `git ls-files`, tree inspection for generated cache, and bounded path-based classification. Clear path conventions were treated as structural evidence. Ambiguous copy-like and legacy-like names were marked low confidence and carried to 80.4.

# Bounded Inference Rules Used
- `E1_DIRECT_EVIDENCE` for explicit authority, canonical, or source-of-truth declarations.
- `E2_STRUCTURAL_EVIDENCE` for stable path, directory role, and repository convention.
- `E3_HEURISTIC_EVIDENCE` for copy-like, legacy-like, or stale-report names.
- `E0_UNKNOWN` only if a file cannot be classified safely.

# Fallback Evidence Rule Usage
Path-pattern evidence was used only for low-confidence duplicate, legacy, and stale-report items. It was not upgraded to direct evidence and did not authorize cleanup or mutation.

# Repository File Inventory
- Tracked files from `git ls-files`: 5252
- Generated/cache files found in the tree but not tracked: 76
- Total mapped items in this file map: 5328
- Unmapped items: 0
- Top-level inventory snapshot:
  - `tests`: 3679
  - `reports`: 483
  - `docs`: 346
  - `templates`: 220
  - `scripts`: 203
  - `schemas`: 69
  - `examples`: 46
  - `tools`: 43
  - `fixtures`: 42
  - `tasks`: 29
  - `.github`: 15
  - `memory-bank`: 10
  - `shared`: 7
  - `prompt-packs`: 5
  - `prompts`: 5
  - `data`: 5
  - `architecture`: 3
  - `stages`: 2
  - `lessons`: 2
  - `handoff`: 2
  - `core-rules`: 2
  - `.githooks`: 2
  - single-file top-level items: `workflow`, `state`, `security`, `quality`, `README.md`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `llms.txt`, `ROUTES-REGISTRY.md`, `repo-map.md`, `requirements.txt`, `opencode.json`, `install.sh`, `VERSION`, `SYSTEM_PROMPT.md`, `START.md`, `INIT.md`, `ARCHITECTURE.md`, `CHANGELOG.md`, `CHECKLIST.md`, `FAQ.md`, `HANDOFF.md`, `HANDOFF 2.md`, `LICENSE`, `RELEASE-CHECKLIST.md`

# Primary File Class Summary
- `ACTIVE_REQUIRED`: 258
- `ACTIVE_REFERENCE`: 944
- `LEGACY_OR_DEPRECATED`: 10
- `PROTECTED_OR_CANONICAL`: 7
- `GENERATED_OR_CACHE`: 76
- `REMAINING_COPY_OR_DUPLICATE`: 329
- `REMAINING_STALE_REPORT`: 1
- `ARCHIVED_OR_REFERENCE`: 3622
- `SOURCE_OF_TRUTH`: 76
- `DERIVED_NAVIGATION_OR_INDEX`: 5
- `UNKNOWN`: 0

# Evidence Level Summary
- `E1_DIRECT_EVIDENCE`: 13
- `E2_STRUCTURAL_EVIDENCE`: 4975
- `E3_HEURISTIC_EVIDENCE`: 340
- `E0_UNKNOWN`: 0

# Confidence Summary
- high: 13
- medium: 4975
- low: 340
- unknown: 0

# Path-Pattern Evidence Summary
Path-pattern evidence was used for 340 low-confidence items: copy-like paths, one stale report, and explicit legacy/deprecated names. It remained visible as heuristic evidence and was not upgraded.

# Required Primary Area Coverage
- reports area mapped: true
- scripts area mapped: true
- docs area mapped: true
- data area mapped: true
- github area mapped: true
- root bootstrap/adapter area mapped: true
- required primary areas mapped: true

# Active Required Files
```yaml
optimized_file_map:
  - path: "scripts/agentos-validate.py"
    file_class: "ACTIVE_REQUIRED"
    area: "scripts"
    evidence_level: "E2_STRUCTURAL_EVIDENCE"
    evidence_source:
      - "git_ls_files"
    classification_confidence: "medium"
    source_of_truth_status: "reference"
    protected_or_canonical: false
    active_status: "active"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Core validation entrypoint."
  - path: "scripts/audit-agentos.py"
    file_class: "ACTIVE_REQUIRED"
    area: "scripts"
    evidence_level: "E2_STRUCTURAL_EVIDENCE"
    evidence_source:
      - "git_ls_files"
    classification_confidence: "medium"
    source_of_truth_status: "reference"
    protected_or_canonical: false
    active_status: "active"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Audit command named in llms.txt."
  - path: "scripts/build-context-index.py"
    file_class: "ACTIVE_REQUIRED"
    area: "scripts"
    evidence_level: "E2_STRUCTURAL_EVIDENCE"
    evidence_source:
      - "git_ls_files"
    classification_confidence: "medium"
    source_of_truth_status: "reference"
    protected_or_canonical: false
    active_status: "active"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Active index builder."
  - path: "scripts/generate-repo-map.py"
    file_class: "ACTIVE_REQUIRED"
    area: "scripts"
    evidence_level: "E2_STRUCTURAL_EVIDENCE"
    evidence_source:
      - "git_ls_files"
    classification_confidence: "medium"
    source_of_truth_status: "reference"
    protected_or_canonical: false
    active_status: "active"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Active repo-map generator."
  - path: "scripts/check-false-pass-resistance.py"
    file_class: "ACTIVE_REQUIRED"
    area: "scripts"
    evidence_level: "E2_STRUCTURAL_EVIDENCE"
    evidence_source:
      - "git_ls_files"
    classification_confidence: "medium"
    source_of_truth_status: "reference"
    protected_or_canonical: false
    active_status: "active"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Validation support for false-pass semantics."
  - path: "scripts/check-template-integrity.py"
    file_class: "ACTIVE_REQUIRED"
    area: "scripts"
    evidence_level: "E2_STRUCTURAL_EVIDENCE"
    evidence_source:
      - "git_ls_files"
    classification_confidence: "medium"
    source_of_truth_status: "reference"
    protected_or_canonical: false
    active_status: "active"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Template integrity checker."
  - path: "scripts/run-all.sh"
    file_class: "ACTIVE_REQUIRED"
    area: "scripts"
    evidence_level: "E2_STRUCTURAL_EVIDENCE"
    evidence_source:
      - "git_ls_files"
    classification_confidence: "medium"
    source_of_truth_status: "reference"
    protected_or_canonical: false
    active_status: "active"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Top-level runner."
  - path: ".githooks/pre-commit"
    file_class: "ACTIVE_REQUIRED"
    area: "github"
    evidence_level: "E2_STRUCTURAL_EVIDENCE"
    evidence_source:
      - "git_ls_files"
    classification_confidence: "medium"
    source_of_truth_status: "reference"
    protected_or_canonical: false
    active_status: "active"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Hook file; active guardrail."
  - path: ".githooks/commit-msg"
    file_class: "ACTIVE_REQUIRED"
    area: "github"
    evidence_level: "E2_STRUCTURAL_EVIDENCE"
    evidence_source:
      - "git_ls_files"
    classification_confidence: "medium"
    source_of_truth_status: "reference"
    protected_or_canonical: false
    active_status: "active"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Hook file; active guardrail."
```

# Active Reference Files
```yaml
optimized_file_map:
  - path: "docs/VALIDATION.md"
    file_class: "ACTIVE_REFERENCE"
    area: "docs"
    evidence_level: "E2_STRUCTURAL_EVIDENCE"
    evidence_source:
      - "git_ls_files"
    classification_confidence: "medium"
    source_of_truth_status: "reference"
    protected_or_canonical: false
    active_status: "active"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Validation guidance."
  - path: "docs/REQUIRED-EVIDENCE-POLICY.md"
    file_class: "ACTIVE_REFERENCE"
    area: "docs"
    evidence_level: "E2_STRUCTURAL_EVIDENCE"
    evidence_source:
      - "git_ls_files"
    classification_confidence: "medium"
    source_of_truth_status: "reference"
    protected_or_canonical: false
    active_status: "active"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Policy reference."
  - path: "docs/FALSE-PASS-RESISTANCE-SEMANTICS.md"
    file_class: "ACTIVE_REFERENCE"
    area: "docs"
    evidence_level: "E2_STRUCTURAL_EVIDENCE"
    evidence_source:
      - "git_ls_files"
    classification_confidence: "medium"
    source_of_truth_status: "reference"
    protected_or_canonical: false
    active_status: "active"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Result-semantics reference."
  - path: "reports/m80-consolidation-evidence-intake.md"
    file_class: "ACTIVE_REFERENCE"
    area: "reports"
    evidence_level: "E2_STRUCTURAL_EVIDENCE"
    evidence_source:
      - "git_ls_files"
    classification_confidence: "medium"
    source_of_truth_status: "reference"
    protected_or_canonical: false
    active_status: "archived"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Current M80 evidence intake report."
  - path: "reports/m79-completion-review.md"
    file_class: "ACTIVE_REFERENCE"
    area: "reports"
    evidence_level: "E2_STRUCTURAL_EVIDENCE"
    evidence_source:
      - "git_ls_files"
    classification_confidence: "medium"
    source_of_truth_status: "reference"
    protected_or_canonical: false
    active_status: "archived"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "M79 completion proof."
  - path: "examples/ux-to-task-proposals-agent-action-review.md"
    file_class: "ACTIVE_REFERENCE"
    area: "other"
    evidence_level: "E2_STRUCTURAL_EVIDENCE"
    evidence_source:
      - "git_ls_files"
    classification_confidence: "medium"
    source_of_truth_status: "reference"
    protected_or_canonical: false
    active_status: "active"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Example review artifact."
```

# Legacy / Deprecated Files
```yaml
optimized_file_map:
  - path: "docs/DEPRECATED-DOCS-REGISTRY.md"
    file_class: "LEGACY_OR_DEPRECATED"
    area: "docs"
    evidence_level: "E3_HEURISTIC_EVIDENCE"
    evidence_source:
      - "path_pattern"
    classification_confidence: "low"
    source_of_truth_status: "reference"
    protected_or_canonical: false
    active_status: "legacy"
    review_needed_in_80_4: true
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Name explicitly says deprecated."
  - path: "docs/HONEST-PASS-LEGACY-COMPATIBILITY.md"
    file_class: "LEGACY_OR_DEPRECATED"
    area: "docs"
    evidence_level: "E3_HEURISTIC_EVIDENCE"
    evidence_source:
      - "path_pattern"
    classification_confidence: "low"
    source_of_truth_status: "reference"
    protected_or_canonical: false
    active_status: "legacy"
    review_needed_in_80_4: true
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Legacy compatibility marker."
  - path: "docs/SCRIPT-LEGACY-AND-DUPLICATE-MAP.md"
    file_class: "LEGACY_OR_DEPRECATED"
    area: "docs"
    evidence_level: "E3_HEURISTIC_EVIDENCE"
    evidence_source:
      - "path_pattern"
    classification_confidence: "low"
    source_of_truth_status: "reference"
    protected_or_canonical: false
    active_status: "legacy"
    review_needed_in_80_4: true
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Legacy/duplicate mapping note."
  - path: "tasks/tech-debt.md"
    file_class: "LEGACY_OR_DEPRECATED"
    area: "tasks"
    evidence_level: "E3_HEURISTIC_EVIDENCE"
    evidence_source:
      - "path_pattern"
    classification_confidence: "low"
    source_of_truth_status: "reference"
    protected_or_canonical: false
    active_status: "legacy"
    review_needed_in_80_4: true
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Explicit tech-debt file."
  - path: "tests/fixtures/context-index/deprecated-file/example.md"
    file_class: "LEGACY_OR_DEPRECATED"
    area: "other"
    evidence_level: "E3_HEURISTIC_EVIDENCE"
    evidence_source:
      - "path_pattern"
    classification_confidence: "low"
    source_of_truth_status: "reference"
    protected_or_canonical: false
    active_status: "legacy"
    review_needed_in_80_4: true
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Deprecated fixture path."
```

# Protected / Canonical Files
```yaml
optimized_file_map:
  - path: "README.md"
    file_class: "PROTECTED_OR_CANONICAL"
    area: "root"
    evidence_level: "E1_DIRECT_EVIDENCE"
    evidence_source:
      - "git_ls_files"
    classification_confidence: "high"
    source_of_truth_status: "source_of_truth"
    protected_or_canonical: true
    active_status: "active"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Root bootstrap file."
  - path: "AGENTS.md"
    file_class: "PROTECTED_OR_CANONICAL"
    area: "root"
    evidence_level: "E1_DIRECT_EVIDENCE"
    evidence_source:
      - "git_ls_files"
    classification_confidence: "high"
    source_of_truth_status: "source_of_truth"
    protected_or_canonical: true
    active_status: "active"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Agent instructions entrypoint."
  - path: "llms.txt"
    file_class: "PROTECTED_OR_CANONICAL"
    area: "root"
    evidence_level: "E1_DIRECT_EVIDENCE"
    evidence_source:
      - "git_ls_files"
    classification_confidence: "high"
    source_of_truth_status: "source_of_truth"
    protected_or_canonical: true
    active_status: "active"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Canonical bootstrap order."
  - path: "ROUTES-REGISTRY.md"
    file_class: "PROTECTED_OR_CANONICAL"
    area: "root"
    evidence_level: "E1_DIRECT_EVIDENCE"
    evidence_source:
      - "git_ls_files"
    classification_confidence: "high"
    source_of_truth_status: "source_of_truth"
    protected_or_canonical: true
    active_status: "active"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Canonical route registry."
  - path: ".github/copilot-instructions.md"
    file_class: "PROTECTED_OR_CANONICAL"
    area: "github"
    evidence_level: "E1_DIRECT_EVIDENCE"
    evidence_source:
      - "git_ls_files"
    classification_confidence: "high"
    source_of_truth_status: "source_of_truth"
    protected_or_canonical: true
    active_status: "active"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Canonical GitHub instructions."
```

# Generated / Cache Files
```yaml
optimized_file_map:
  - path: "scripts/__pycache__/agentos-validate.cpython-314.pyc"
    file_class: "GENERATED_OR_CACHE"
    area: "scripts"
    evidence_level: "E2_STRUCTURAL_EVIDENCE"
    evidence_source:
      - "find"
    classification_confidence: "medium"
    source_of_truth_status: "cache"
    protected_or_canonical: false
    active_status: "generated"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Generated bytecode cache under scripts/__pycache__."
  - path: "scripts/__pycache__/check-context-index-freshness.cpython-314.pyc"
    file_class: "GENERATED_OR_CACHE"
    area: "scripts"
    evidence_level: "E2_STRUCTURAL_EVIDENCE"
    evidence_source:
      - "find"
    classification_confidence: "medium"
    source_of_truth_status: "cache"
    protected_or_canonical: false
    active_status: "generated"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Generated bytecode cache under scripts/__pycache__."
  - path: "scripts/__pycache__/validate-policy.cpython-314.pyc"
    file_class: "GENERATED_OR_CACHE"
    area: "scripts"
    evidence_level: "E2_STRUCTURAL_EVIDENCE"
    evidence_source:
      - "find"
    classification_confidence: "medium"
    source_of_truth_status: "cache"
    protected_or_canonical: false
    active_status: "generated"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Generated bytecode cache under scripts/__pycache__."
```

# Remaining Copy / Duplicate Files
```yaml
optimized_file_map:
  - path: "tests/fixtures/index/invalid/duplicate-path.json"
    file_class: "REMAINING_COPY_OR_DUPLICATE"
    area: "other"
    evidence_level: "E3_HEURISTIC_EVIDENCE"
    evidence_source:
      - "path_pattern"
    classification_confidence: "low"
    source_of_truth_status: "reference"
    protected_or_canonical: false
    active_status: "legacy"
    review_needed_in_80_4: true
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Duplicate-like filename pattern."
  - path: "tests/fixtures/index/invalid/duplicate-path 3.json"
    file_class: "REMAINING_COPY_OR_DUPLICATE"
    area: "other"
    evidence_level: "E3_HEURISTIC_EVIDENCE"
    evidence_source:
      - "path_pattern"
    classification_confidence: "low"
    source_of_truth_status: "reference"
    protected_or_canonical: false
    active_status: "legacy"
    review_needed_in_80_4: true
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Duplicate-like filename pattern."
  - path: "tests/fixtures/template-integrity/missing-gitignore-drafts/tasks/drafts/.gitkeep"
    file_class: "REMAINING_COPY_OR_DUPLICATE"
    area: "other"
    evidence_level: "E3_HEURISTIC_EVIDENCE"
    evidence_source:
      - "path_pattern"
    classification_confidence: "low"
    source_of_truth_status: "reference"
    protected_or_canonical: false
    active_status: "legacy"
    review_needed_in_80_4: true
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Path-pattern heuristic only; copy-like legacy fixture area."
```

# Remaining Stale Reports
```yaml
optimized_file_map:
  - path: "reports/m68-duplicates.json"
    file_class: "REMAINING_STALE_REPORT"
    area: "reports"
    evidence_level: "E3_HEURISTIC_EVIDENCE"
    evidence_source:
      - "path_pattern"
    classification_confidence: "low"
    source_of_truth_status: "reference"
    protected_or_canonical: false
    active_status: "archived"
    review_needed_in_80_4: true
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Report filename indicates duplicate/stale evidence."
```

# Archived / Reference Files
```yaml
optimized_file_map:
  - path: "tests/fixtures/ux-contract/valid/valid-agent-action-review.md"
    file_class: "ARCHIVED_OR_REFERENCE"
    area: "other"
    evidence_level: "E2_STRUCTURAL_EVIDENCE"
    evidence_source:
      - "git_ls_files"
    classification_confidence: "medium"
    source_of_truth_status: "reference"
    protected_or_canonical: false
    active_status: "archived"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Fixture/reference asset."
  - path: "templates/agentos-full/templates/verification.md"
    file_class: "ARCHIVED_OR_REFERENCE"
    area: "templates"
    evidence_level: "E2_STRUCTURAL_EVIDENCE"
    evidence_source:
      - "git_ls_files"
    classification_confidence: "medium"
    source_of_truth_status: "reference"
    protected_or_canonical: false
    active_status: "archived"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Template asset."
  - path: "reports/m79-baseline-comparison-report.md"
    file_class: "ARCHIVED_OR_REFERENCE"
    area: "reports"
    evidence_level: "E2_STRUCTURAL_EVIDENCE"
    evidence_source:
      - "git_ls_files"
    classification_confidence: "medium"
    source_of_truth_status: "reference"
    protected_or_canonical: false
    active_status: "archived"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Reference report for baseline comparison."
```

# Source-of-Truth Files
```yaml
optimized_file_map:
  - path: "core-rules/MAIN.md"
    file_class: "SOURCE_OF_TRUTH"
    area: "core-rules"
    evidence_level: "E1_DIRECT_EVIDENCE"
    evidence_source:
      - "git_ls_files"
    classification_confidence: "high"
    source_of_truth_status: "source_of_truth"
    protected_or_canonical: false
    active_status: "active"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Canonical governance module."
  - path: "workflow/MAIN.md"
    file_class: "SOURCE_OF_TRUTH"
    area: "workflow"
    evidence_level: "E1_DIRECT_EVIDENCE"
    evidence_source:
      - "git_ls_files"
    classification_confidence: "high"
    source_of_truth_status: "source_of_truth"
    protected_or_canonical: false
    active_status: "active"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Canonical workflow module."
  - path: "schemas/task-state.schema.json"
    file_class: "SOURCE_OF_TRUTH"
    area: "other"
    evidence_level: "E2_STRUCTURAL_EVIDENCE"
    evidence_source:
      - "git_ls_files"
    classification_confidence: "medium"
    source_of_truth_status: "source_of_truth"
    protected_or_canonical: false
    active_status: "active"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Schema contract."
```

# Derived Navigation / Index Files
```yaml
optimized_file_map:
  - path: "data/context-index.json"
    file_class: "DERIVED_NAVIGATION_OR_INDEX"
    area: "data"
    evidence_level: "E2_STRUCTURAL_EVIDENCE"
    evidence_source:
      - "git_ls_files"
    classification_confidence: "medium"
    source_of_truth_status: "derived"
    protected_or_canonical: false
    active_status: "generated"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Derived navigation index."
  - path: "data/execution-verification-registry.json"
    file_class: "DERIVED_NAVIGATION_OR_INDEX"
    area: "data"
    evidence_level: "E2_STRUCTURAL_EVIDENCE"
    evidence_source:
      - "git_ls_files"
    classification_confidence: "medium"
    source_of_truth_status: "derived"
    protected_or_canonical: false
    active_status: "generated"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Derived verification registry."
  - path: "generated/task-contract-candidates/agent-action-review.generated-conversion-package.md"
    file_class: "DERIVED_NAVIGATION_OR_INDEX"
    area: "other"
    evidence_level: "E2_STRUCTURAL_EVIDENCE"
    evidence_source:
      - "git_ls_files"
    classification_confidence: "medium"
    source_of_truth_status: "derived"
    protected_or_canonical: false
    active_status: "generated"
    review_needed_in_80_4: false
    cleanup_action_allowed_by_80_2: false
    mutation_allowed_by_80_2: false
    notes: "Generated artifact candidate package."
```

# Unknown Files
None. The current mapping covers the tracked repository and the cache files found in the tree.

# Items Requiring 80.4 Review
- 329 remaining copy/duplicate files marked with `E3_HEURISTIC_EVIDENCE`
- 10 explicit legacy/deprecated files marked with `E3_HEURISTIC_EVIDENCE`
- 1 stale report marked with `E3_HEURISTIC_EVIDENCE`
- Total review-needed items: 340

# UNKNOWN Ratio Review
- unknown file ratio: 0.00%
- interpretation: acceptable

# No-Cleanup Authorization Boundary
No file was marked cleanup-allowed or mutation-allowed by 80.2. The file map is descriptive only.

# No-New-Baseline Boundary
No new baseline was created. No baseline was updated.

# No-Derived-Update Boundary
No derived artifacts were updated. No repo-map or context-index was updated.

# M81 Boundary Check
- M81 artifacts created by 80.2: false
- M81 task briefs created by 80.2: false
- M81 started by 80.2: false
- SaaS/UI artifacts created by 80.2: false
- autopilot enabled by 80.2: false

# Blockers
- none

# Warnings
- M80_1_WARNINGS_CARRIED_FORWARD
- M79_WARNINGS_CARRIED_FORWARD
- M78_WARNINGS_CARRIED_FORWARD
- LOW_CONFIDENCE_CLASSIFICATIONS_PRESENT
- HEURISTIC_CLASSIFICATIONS_PRESENT
- PATH_PATTERN_EVIDENCE_USED
- REMAINING_COPY_OR_DUPLICATE_FILES_PRESENT
- REMAINING_STALE_REPORTS_PRESENT
- GENERATED_OR_CACHE_FILES_PRESENT
- GIT_STATUS_HAS_UNRELATED_CHANGES

# Local Final Status
FINAL_STATUS: M80_OPTIMIZED_FILE_MAP_COMPLETE_WITH_WARNINGS

# Readiness for 80.3
may_prepare_m80_3: true_with_warnings

# Final Boundary Statement
80.2 produced a bounded file map only. It did not authorize cleanup, did not mutate files, did not create a baseline, and did not start M81.

task_id: "80.2"
task_name: "Optimized File Map v2"
reports_directory_exists: true
input_file: "reports/m80-consolidation-evidence-intake.md"

m80_1_evidence_intake_exists: true
m80_1_evidence_intake_readable: true
m80_1_final_status_detected: "FINAL_STATUS: M80_CONSOLIDATION_EVIDENCE_INTAKE_COMPLETE_WITH_WARNINGS"
m80_1_final_status_acceptable: true
m80_1_readiness_detected: "may_prepare_m80_2: true_with_warnings"
m80_1_readiness_acceptable: true

optimized_file_map_created: true

tracked_file_count: 5252
mapped_file_count: 5328
unmapped_file_count: 0

active_required_file_count: 258
active_reference_file_count: 944
legacy_or_deprecated_file_count: 10
protected_or_canonical_file_count: 7
unknown_file_count: 0
unknown_file_ratio: "0.00%"
generated_or_cache_file_count: 76
remaining_copy_or_duplicate_file_count: 329
remaining_stale_report_count: 1
archived_or_reference_file_count: 3622
source_of_truth_file_count: 76
derived_navigation_or_index_file_count: 5

e1_direct_evidence_count: 13
e2_structural_evidence_count: 4975
e3_heuristic_evidence_count: 340
e0_unknown_evidence_count: 0

high_confidence_count: 13
medium_confidence_count: 4975
low_confidence_count: 340
unknown_confidence_count: 0

path_pattern_evidence_count: 340
path_pattern_evidence_upgraded_to_direct_count: 0
path_pattern_cleanup_authorization_count: 0

review_needed_in_80_4_count: 340

reports_area_mapped: true
scripts_area_mapped: true
docs_area_mapped: true
data_area_mapped: true
github_area_mapped: true
root_bootstrap_adapter_area_mapped: true

required_primary_areas_mapped: true

files_marked_cleanup_allowed_by_80_2_count: 0
files_marked_mutation_allowed_by_80_2_count: 0
classification_claim_without_evidence_count: 0
heuristic_classification_hidden: false
unknown_treated_as_ok: false
missing_evidence_treated_as_ok: false

new_baseline_created_by_80_2: false
baseline_updated_by_80_2: false
derived_artifacts_updated_by_80_2: false
repo_map_updated_by_80_2: false
context_index_updated_by_80_2: false
physical_cleanup_performed_by_80_2: false
files_deleted_by_80_2: false
files_moved_by_80_2: false
files_renamed_by_80_2: false
files_archived_by_80_2: false
files_compressed_by_80_2: false
scripts_consolidated_by_80_2: false
rollback_executed_by_80_2: false
repair_authorized_by_80_2: false
fix_tasks_created_by_80_2: false
lifecycle_mutation_by_80_2: false
approval_claim_created_by_80_2: false

m80_artifacts_created_by_80_2_beyond_file_map: false
m80_consolidation_started_by_80_2_beyond_file_map: false
m81_artifacts_created_by_80_2: false
m81_task_briefs_created_by_80_2: false
m81_started_by_80_2: false
saas_or_ui_artifacts_created_by_80_2: false
autopilot_enabled_by_80_2: false

human_summary_consistent_with_machine_fields: true

blocker_codes:
  - "none"
warning_codes:
  - "M80_1_WARNINGS_CARRIED_FORWARD"
  - "M79_WARNINGS_CARRIED_FORWARD"
  - "M78_WARNINGS_CARRIED_FORWARD"
  - "LOW_CONFIDENCE_CLASSIFICATIONS_PRESENT"
  - "HEURISTIC_CLASSIFICATIONS_PRESENT"
  - "PATH_PATTERN_EVIDENCE_USED"
  - "REMAINING_COPY_OR_DUPLICATE_FILES_PRESENT"
  - "REMAINING_STALE_REPORTS_PRESENT"
  - "GENERATED_OR_CACHE_FILES_PRESENT"
  - "GIT_STATUS_HAS_UNRELATED_CHANGES"
