# M47 UX Contract Validation

## Purpose
Определить детерминированную (однозначную) проверку структуры UX Contract.

## Role in M47
Проверка подтверждает соответствие UX Contract правилам M47 по структуре, traceability и границам неавторизации.

## Relationship to UX Contract Schema
Проверка дополняет схему `schemas/ux-contract.schema.json` и проверяет Markdown-структуру, которую схема JSON сама не покрывает.

## Relationship to UX Element Vocabulary
For M47, validate-ux-contract.py uses a hardcoded allowlist derived from docs/UX-ELEMENT-VOCABULARY.md.

## Relationship to Screen & State Model
Валидатор требует обязательные состояния и защитные состояния.

## Relationship to Flow Policy
Валидатор требует наличие хотя бы одного потока и проверяет, что контракт не сводится к happy-path-only.

## Relationship to Layout Policy
Валидатор не оценивает красоту layout и не делает визуальную экспертизу.

## Relationship to Traceability Policy
Валидатор проверяет canonical поле `source_sections` и запрещает `source_section`.

## Validator Scope
UX Contract validation is structural validation.
UX Contract validation is not design approval.
UX Contract validation is not implementation approval.
UX Contract validation does not authorize task generation.
UX Contract validation does not authorize execution planning.
UX Contract validation does not authorize implementation.
UX Contract validation does not authorize commit, push, merge, deploy, or release.

## Validator Non-Goals
- визуальная оценка дизайна;
- генерация HTML preview;
- создание задач;
- авторизация исполнения;
- интеграция в CI в рамках M47.

## CLI Usage
```bash
python3 scripts/validate-ux-contract.py --contract examples/ux-contract-example.md
python3 scripts/validate-ux-contract.py --fixtures
python3 scripts/validate-ux-contract.py --contract examples/ux-contract-example.md --json
python3 scripts/validate-ux-contract.py --explain
```

## Explain Mode
`--explain` не валидирует контракт, а выводит правила.
`--explain` возвращает `UX_CONTRACT_VALIDATION_OK` (exit 0), если сводка правил доступна.

## Input Reading Rules
- UTF-8 чтение входного файла;
- не-UTF-8, нечитаемые файлы и файлы больше 1 MB: `UX_CONTRACT_VALIDATION_BLOCKED`;
- чтение только входа, без модификации.

Unreadable files, non-UTF-8 files, and files larger than 1 MB return UX_CONTRACT_VALIDATION_BLOCKED.

## Frontmatter Parsing Rules
- ручной line-by-line парсинг frontmatter;
- только `key: value` строки;
- без YAML-библиотек;
- `execution_locked` принимается только как `true`;
- `type: ux-contract` не считается UX-элементом;
- M47 intentionally does not support generic type: fields as UX element declarations.

## Result Tokens
- `UX_CONTRACT_VALIDATION_OK`
- `UX_CONTRACT_VALIDATION_FAILED`
- `UX_CONTRACT_VALIDATION_BLOCKED`

## Exit Semantics
- `OK` => `0`
- `FAILED` => `1`
- `BLOCKED` => `2`

## Validation Checks
- читаемость/размер/UTF-8;
- frontmatter ключи/значения;
- обязательные разделы;
- source product spec блок;
- canonical traceability;
- required UX states;
- наличие screen/flow;
- allowlist UX elements;
- required terms for `approval_card`/`risk_banner`;
- non-authority boundary;
- forbidden authority claims;
- forbidden implementation fields;
- execution lock.

## Hardcoded Vocabulary Allowlist
`validate-ux-contract.py` использует `ALLOWED_UX_ELEMENTS`.
VOCABULARY_VERSION = 1.0.0

## Vocabulary Version Boundary
Vocabulary-file parsing is not implemented in M47.

## Fixture Strategy
Проверка идёт по 1 позитивной и 16 негативным фикстурам.

## Positive Fixtures
- `tests/fixtures/ux-contract/valid/valid-agent-action-review.md`

## Negative Fixtures
- `missing-required-section.md`
- `missing-source-product-spec.md`
- `source-section-singular.md`
- `unknown-ux-element.md`
- `approval-card-missing-owner.md`
- `forbidden-authority-claim.md`
- `missing-required-state.md`
- `execution-locked-false.md`
- `implementation-field.md`
- `happy-path-only.md`

## Fixture Failure Semantics
- если позитивная фикстура падает: итог `FAILED`, `positive_failed: 1`;
- если негативная фикстура неожиданно проходит: итог `FAILED`, `negative_unexpectedly_passed > 0`;
- если структура фикстур отсутствует: итог `BLOCKED`.

## Forbidden Authority Claims
Валидатор блокирует утверждения об авторизации исполнения/имплементации UX Contract и HTML Preview.

## Forbidden Implementation Fields
Валидатор блокирует поля:
`react_component`, `vue_component`, `svelte_component`, `css_class`, `api_endpoint`, `database_table`, `backend_service`, `deploy_target`, `runtime_command`.

## HTML Preview Boundary
HTML Preview is optional visual explanation only.
HTML Preview is not source of truth.
HTML Preview is not implementation.

## Non-Authority Boundary
UX Contract validation checks structure.
UX Contract validation is not Product Spec approval.
UX Contract validation is not UX approval.
UX Contract validation is not implementation approval.
UX Contract validation does not authorize task generation.
UX Contract validation does not authorize execution planning.
UX Contract validation does not authorize implementation.
UX Contract validation does not authorize commit, push, merge, deploy, or release.
Validator PASS is not approval.
Validator PASS is not execution permission.
HTML Preview is optional visual explanation only.

## Future Extension Notes
- Future validator versions may parse vocabulary files after the vocabulary format is stable.
- Future validator versions may perform deeper schema validation.
- Future validator versions may compare spec_version against Product Spec metadata.
- Future validator versions may validate layout recommendations.
- Future validator versions may validate stale traceability more deeply.
- Future validator versions may expand forbidden implementation field patterns.
- M47 validator MVP intentionally avoids full semantic design review.

## Summary
Документ фиксирует M47 MVP-правила для детерминированной проверки UX Contract без расширения в дизайн-ревью или авторизацию исполнения.
