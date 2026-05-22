---
type: ux-traceability-policy
status: canonical
authority: ux-structure
version: 1.0.0
created: 2026-05-21
owner: human
---

# M47 UX Traceability Policy

## Purpose
Определить канонические правила трассируемости (связи UX-артефактов с источниками Product Spec) для M47.

## Role in M47
Политика трассируемости помогает держать UX Contract согласованным с Product Spec и выявлять расхождения при изменениях.

## Relationship to Product Spec
Product Spec остаётся источником продуктовых требований. Трассируемость только ссылается на Product Spec и не заменяет его.

## Relationship to UX Contract
UX Contract должен хранить traceability-записи для ключевых UX-артефактов.

## Relationship to UX Element Vocabulary
Каждый используемый UX-элемент должен иметь объяснимую связь с Product Spec через traceability.

## Relationship to UX Screen & State Model
Ссылки экранов и состояний на Product Spec должны быть явными и проверяемыми.

## Relationship to UX Flow Policy
Потоки, точки решения/риска/одобрения и блокировки в UX Flow должны быть обоснованы traceability.

## Relationship to Best-Practice Layout Policy
Рекомендации layout должны иметь traceability как поддерживающее объяснение, а не как обязательное правило исполнения.

## Traceability Definition
- UX traceability links UX structure back to Product Spec sources.
- UX traceability helps detect drift when Product Spec changes.
- UX traceability helps reviewers understand why a UX artifact exists.
- UX traceability must be preserved for screens, states, flows, UX elements, layouts, risk points, approval points, edge cases, and open questions.
- UX traceability does not replace Product Spec.
- UX traceability does not approve UX structure.
- UX traceability does not authorize task generation.
- UX traceability does not authorize execution planning.
- UX traceability does not authorize implementation.

## Required Traceability Fields
Every UX Contract traceability record must include:
```yaml
traceability:
  spec_id:
  spec_version:
  product_spec_path:
  ux_contract_id:
  source_sections:
```

- spec_id identifies the source Product Spec.
- spec_version identifies the source Product Spec version used by the UX Contract.
- product_spec_path identifies the Product Spec file path.
- ux_contract_id identifies the UX Contract containing the UX artifact.
- source_sections identifies one or more Product Spec sections that justify the UX artifact.
- source_sections must be plural.
- source_sections must be an array or list.
- Every traceability record must use source_sections.

## Traceability Record Format
traceability:
  spec_id:
  spec_version:
  product_spec_path:
  ux_contract_id:
  source_sections:
    - 

Example:
```yaml
traceability:
  spec_id: SPEC-agent-action-review
  spec_version: 0.1.0
  product_spec_path: specs/agent-action-review.md
  ux_contract_id: UX-agent-action-review
  source_sections:
    - goals.agent_action_review
    - requirements.risk_visibility
    - requirements.human_approval_boundary
```

## Artifact Traceability Requirements
These UX Contract artifact types require traceability:
- screens
- states
- flows
- ux_elements
- user_actions
- risk_approval_points
- edge_cases
- accessibility_notes
- non_goals
- open_ux_questions
- layout_recommendations
- non_authority_boundary

- Every screen must include traceability.
- Every state reference must include traceability or inherit traceability from its screen with an explicit reference.
- Every flow must include traceability.
- Every UX element instance must include traceability.
- Every user action must include traceability.
- Every risk or approval point must include traceability.
- Every edge case must include traceability.
- Every accessibility note should include traceability where derived from Product Spec.
- Every open UX question must include traceability to the Product Spec gap or ambiguity.
- Non-Goals must preserve traceability where they constrain UX behavior.

## Screen Traceability
- Screen traceability must explain why the screen exists.
- Screen traceability must reference Product Spec sections that justify the screen.
- Screen traceability must not be inferred silently.
- Screen traceability must not be replaced by screen title alone.

```yaml
screen_id: agent_action_review
screen_title: Agent Action Review
traceability:
  spec_id: SPEC-agent-action-review
  spec_version: 0.1.0
  product_spec_path: specs/agent-action-review.md
  ux_contract_id: UX-agent-action-review
  source_sections:
    - requirements.review_before_risky_action
```

## State Traceability
- State traceability must explain why a state is needed.
- blocked state traceability must identify the blocking Product Spec requirement or missing information.
- needs_clarification state traceability must identify the Product Spec ambiguity or gap.
- approval_required state traceability must identify the Product Spec requirement for human decision.
- execution_not_authorized state traceability must identify the non-authority boundary.

Execution planning is blocked because approval owner is undefined.

## Flow Traceability
- Flow traceability must identify which Product Spec sections justify the flow.
- Flow traceability must cover decision points, risk points, approval points, blocked states, exit states, and next steps.
- Flow traceability must not convert conceptual flow into execution permission.
- Flow traceability must preserve not_authorized.

## UX Element Traceability
- UX element traceability must identify why the element appears in the UX Contract.
- approval_card traceability must identify the Product Spec requirement for human review or approval point.
- risk_banner traceability must identify the Product Spec risk requirement.
- non_authority_notice traceability must identify the M47 non-authority boundary.
- UX elements must not appear without traceability unless explicitly marked as derived from a traceable parent artifact.

## Layout Traceability
- Layout traceability must identify why a layout pattern is recommended.
- Layout traceability must not override Product Spec.
- Layout traceability must not override UX Contract.
- Layout traceability must not make best-practice layout mandatory where UX Contract requires a different structure.
- Layout traceability is supporting explanation only.

## Risk and Approval Traceability
- Risk points must trace to Product Spec risk, safety, compliance, or review requirements.
- Approval points must trace to Product Spec or governance requirements.
- Unknown risk must be traceable to the missing or ambiguous source.
- Undefined approval owner must be traceable to a Product Spec gap or governance gap.
- Traceability must not create approval.
- Traceability must not simulate human approval.
- Traceability must not authorize execution.

## Open Question Traceability
- Open UX questions must trace to the Product Spec section, gap, ambiguity, or conflict that produced the question.
- Open UX questions must not be silently converted into assumptions.
- Open UX questions must not be treated as resolved without explicit update.
- If open questions affect risk, approval, or execution-sensitive UX, the related screen or flow must include blocked or needs_clarification.

## Staleness Rules
- If Product Spec changes, UX Contract may become stale.
- If spec_version changes, related UX Contract traceability must be reviewed.
- If product_spec_path changes, traceability must be reviewed.
- If a referenced source_sections entry is removed or renamed, traceability must be reviewed.
- Stale UX Contract must not be treated as current UX authority.
- Stale traceability must not authorize task generation.
- Stale traceability must not authorize execution planning.
- Stale traceability must not authorize implementation.

If Product Spec changes, UX Contract may become stale.
Stale UX Contract must not be treated as current UX authority.
Traceability is not approval.
Traceability is not execution authorization.

## Traceability Review Rules
- Traceability review checks whether UX artifacts still point to valid Product Spec sources.
- Traceability review checks whether UX artifacts still match the referenced Product Spec meaning.
- Traceability review checks whether stale references exist.
- Traceability review does not approve UX Contract.
- Traceability review does not authorize task generation.
- Traceability review does not authorize execution planning.
- Traceability review does not authorize implementation.

## HTML Preview Boundary
- Static HTML Preview may display traceability references.
- HTML Preview may show spec_id, ux_contract_id, and source_sections.
- HTML Preview rendering is visual explanation only.
- HTML Preview is not source of truth.
- HTML Preview is not implementation.
- HTML Preview must not convert traceability into approval.
- HTML Preview must not convert traceability into implementation permission.
- HTML Preview must display non-authority boundaries.

HTML Preview is optional visual explanation only.
HTML Preview is not source of truth.
HTML Preview is not implementation.

## Forbidden Uses
UX traceability must not be used to:
- replace Product Spec;
- approve UX Contract;
- create approval;
- simulate human approval;
- authorize task generation;
- authorize execution planning;
- authorize implementation;
- authorize commit, push, merge, deploy, or release;
- bypass open questions;
- bypass blocked states;
- treat stale UX artifacts as current;
- hide Product Spec conflicts;
- hide Product Spec gaps.

## Non-Authority Boundary
Traceability links UX structure to Product Spec sources.
Traceability is not Product Spec.
Traceability is not approval.
Traceability does not authorize task generation.
Traceability does not authorize execution planning.
Traceability does not authorize implementation.
Traceability does not authorize commit, push, merge, deploy, or release.
Traceability does not make stale UX artifacts current.
Traceability may support review.
Traceability must not replace review.
HTML Preview is optional visual explanation only.

## Future Validator Notes
- Future validate-ux-contract.py should check that every UX Contract has top-level traceability.
- Future validate-ux-contract.py should check that source_sections is present.
- Future validate-ux-contract.py should check that source_sections is a list.
- Future validate-ux-contract.py should check that source_section is not used.
- Future validate-ux-contract.py should check that screens include traceability.
- Future validate-ux-contract.py should check that flows include traceability.
- Future validate-ux-contract.py should check that UX elements include traceability.
- Future validate-ux-contract.py should check that risk and approval points include traceability.
- Future validate-ux-contract.py should check for stale spec_version where detectable.
- Future validate-ux-contract.py should check that traceability does not claim approval or execution authority.
- M47.7 does not implement the validator.

## Summary
Документ задаёт каноническую политику traceability для M47: как привязывать UX-структуру к Product Spec, контролировать устаревание и сохранять границы неавторизации.
