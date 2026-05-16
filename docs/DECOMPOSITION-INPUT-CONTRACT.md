## Purpose
Этот документ задаёт входной контракт для M44: какие входные данные должны быть готовы до декомпозиции задач.

## Position in M44
M44 использует этот контракт как проверку готовности входов перед подготовкой task contracts (контрактов задач).

## Required Input Categories
- approved Spec
- approved UX brief
- screen map
- user flows
- state/error matrix
- UX acceptance criteria
- UI foundation / semantic component contract
- known constraints
- known risks

## Approved Spec Requirement
No approved Spec → no decomposition.

## Approved UX Requirement
No approved UX → no decomposition.

## Screen Map Requirement
Screen map должен быть указан и пригоден для декомпозиции UI/UX задач.

## User Flow Requirement
User flows должны быть явно описаны и связаны с UX brief.

## State and Error Matrix Requirement
State and error matrix должен покрывать основные состояния и ошибки.

## UX Acceptance Criteria Requirement
UX acceptance criteria обязательны для проверяемой декомпозиции.

## UI Contract Requirement
No UI Contract for UI work → no UI task decomposition.

## Known Constraints Requirement
Known constraints должны быть перечислены до декомпозиции.

## Known Risks Requirement
Known risks должны быть перечислены до декомпозиции.

## Input Readiness Rules
- No approved Spec → no decomposition.
- No approved UX → no decomposition.
- No UI Contract for UI work → no UI task decomposition.
- Если входы частично заполнены, результат: `DECOMPOSITION_INPUT_INCOMPLETE`.
- Если статус спорный или противоречивый, результат: `DECOMPOSITION_INPUT_NEEDS_REVIEW`.

## Result Tokens
- DECOMPOSITION_INPUT_READY
- DECOMPOSITION_INPUT_MISSING_SPEC_APPROVAL
- DECOMPOSITION_INPUT_MISSING_UX_APPROVAL
- DECOMPOSITION_INPUT_MISSING_UI_CONTRACT
- DECOMPOSITION_INPUT_INCOMPLETE
- DECOMPOSITION_INPUT_NEEDS_REVIEW

## Non-Approval Boundary
- Input readiness does not approve execution.
- Input readiness does not replace HumanApprovalGate.
- Decomposition input readiness is not task queue approval.
- Decomposition input readiness is not commit approval.
- Decomposition input readiness is not push approval.

## Relationship to Task Contract v2
Этот контракт определяет готовность входов до формирования Task Contract v2.
Он не запускает выполнение задач и не выдаёт approval.

## Relationship to Task Queue
Готовность входов нужна до подготовки записей для очереди задач.
Но readiness не является разрешением на выполнение задач.

## Known Gaps
KNOWN_GAP: `docs/UI-SEMANTIC-COMPONENT-CONTRACT.md` is missing.
KNOWN_GAP: `docs/DESIGN-TOKENS-POLICY.md` is missing.
KNOWN_GAP: `docs/UI-REPLACEABILITY-POLICY.md` is missing.
UI Contract dependency не может быть подтверждена полноценно, пока эти артефакты отсутствуют.
Missing upstream artifact documentation does not authorize task execution.
