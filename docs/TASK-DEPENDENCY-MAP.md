## Purpose
Документ описывает, как строить карту зависимостей задач.

## Position in M44
M44 строит контракты и порядок, но не запускает выполнение.

## Relationship to Task Contract v2
Карта использует поля task_id, depends_on, blocked_by, priority, risk_level.

## Relationship to Task Queue
Dependency map does not mark tasks ready in the real queue.

## Relationship to M45 Controlled Autopilot
M45 может позже читать порядок, но не получает разрешение на выполнение из этой карты.

## Frontmatter Parsing Contract
Frontmatter parsing uses simple line-by-line parsing between the first two --- markers.
Do not require PyYAML.

## Dependency Fields
Используются: `task_id`, `depends_on`, `blocked_by`, `priority`, `risk_level`.

## Dependency Semantics
Dependency map orders work.
Dependency map does not approve work.
Dependency map does not authorize execution.
Priority does not override blocked_by.
Priority does not override depends_on.
HIGH priority blocked task remains blocked.

## unblocks Semantics
unblocks is the reverse dependency list.
unblocks must be sorted by task_id ascending.

## Blocker Semantics
Если `blocked_by` не пустой, задача blocked.

## Priority Semantics
Приоритет влияет на важность, но не отменяет блокировки и зависимости.

## Risk Level Preservation
`risk_level` сохраняется в карте без изменения.

## execution_order_hint Format
execution_order_hint must be an integer starting from 1 for dependency-satisfied and unblocked tasks.
Blocked or invalid tasks must have execution_order_hint: null.

## Mandatory Graph Validation Order
1. parse frontmatter
2. validate required fields
3. detect duplicate task_id
4. detect missing dependency
5. detect circular dependency
6. build dependency map

## Mandatory Ordering Rules
- Сначала задачи без блокировок и с выполненными зависимостями.
- blocked-задачи не получают execution_order_hint.

## Protected Output Path Rules
Protected output path checks must use pathlib.Path(...).resolve() and os.path.commonpath().
String prefix checks are forbidden for protected path validation.

## Circular Dependency Handling
Circular dependency must fail closed.

## Missing Dependency Handling
Missing dependency must fail closed.

## Duplicate Task ID Handling
Duplicate task_id must fail closed.

## Invalid Task Handling
Missing task_id must fail closed.

## Output Map Fields
- task_id
- depends_on
- blocked_by
- priority
- risk_level
- readiness
- execution_order_hint
- unblocks

## CLI Usage
```bash
python3 scripts/build-task-dependency-map.py --help
python3 scripts/build-task-dependency-map.py --input <dir> --dry-run
python3 scripts/build-task-dependency-map.py --input <dir> --json
python3 scripts/build-task-dependency-map.py --input <dir> --out <dir> --write
```

## Dry-Run Behavior
По умолчанию dry-run.
Печатает Markdown и не создаёт файлы.

## Write Behavior
- `--write` требует `--out`
- `--out` — директория
- создаёт `dependency-map.md`
- Write mode must refuse to overwrite an existing dependency-map.md.
- `reports/` и `tasks/queue/` запрещены как output.
- --json and --write together are not supported in this MVP.

## JSON Output
`--json` без `--write` работает как dry-run JSON режим.

## Result Tokens
- TASK_DEPENDENCY_MAP_DRY_RUN_OK
- TASK_DEPENDENCY_MAP_WRITE_OK
- TASK_DEPENDENCY_MAP_BLOCKED_CIRCULAR_DEPENDENCY
- TASK_DEPENDENCY_MAP_BLOCKED_MISSING_DEPENDENCY
- TASK_DEPENDENCY_MAP_BLOCKED_DUPLICATE_TASK_ID
- TASK_DEPENDENCY_MAP_BLOCKED_INVALID_TASK
- TASK_DEPENDENCY_MAP_NEEDS_REVIEW
- TASK_DEPENDENCY_MAP_FAILED

## Exit Semantics
- TASK_DEPENDENCY_MAP_DRY_RUN_OK => exit 0
- TASK_DEPENDENCY_MAP_WRITE_OK => exit 0
- TASK_DEPENDENCY_MAP_BLOCKED_CIRCULAR_DEPENDENCY => exit 1
- TASK_DEPENDENCY_MAP_BLOCKED_MISSING_DEPENDENCY => exit 1
- TASK_DEPENDENCY_MAP_BLOCKED_DUPLICATE_TASK_ID => exit 1
- TASK_DEPENDENCY_MAP_BLOCKED_INVALID_TASK => exit 1
- TASK_DEPENDENCY_MAP_NEEDS_REVIEW => exit 1
- TASK_DEPENDENCY_MAP_FAILED => exit 1

## Non-Approval Boundary
Dependency map is not approval.
Dependency map does not authorize execution.
Dependency map does not authorize commit.
Dependency map does not authorize push.
Dependency map does not authorize merge.
Dependency map does not authorize deploy.
Dependency map does not replace HumanApprovalGate.
Queue placement does not authorize execution.
HumanApprovalGate remains separate from dependency ordering.

## Known Gaps
- This task does not implement task queue state changes.
- This task does not write into tasks/queue/.
- This task does not write into reports/.
- This task does not modify Task Contract v2 schema.
- This task does not perform full schema validation without external dependencies.
- This task does not attempt full YAML parsing.
- This task supports only simple frontmatter key/value fields and simple YAML-like lists.
- This task does not define final M45 execution behavior.
- TASK_DEPENDENCY_MAP_NEEDS_REVIEW is reserved for future ambiguous dependency cases.
