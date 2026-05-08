---
type: register
module: m26-pre-merge-corridor
status: active
task_id: 26.7.1
milestone: M26
---

# Known Limitations Register

## KL-01

- description: Машинная проверка коридора невозможна до выполнения 26.10.1
- affected_tasks: [26.1.1, 26.5.1]
- mitigation: ручная проверка по шаблону `pre-merge-execution-review.md`
- resolved_in: 26.10.1

## KL-02

- description: Enforcement только документальный — нет runtime блокировки до M27
- affected_tasks: [26.2.1, 26.3.1]
- mitigation: агент следует политике добровольно
- resolved_in: M27

## KL-03

- description: Нет автоматической блокировки push при нарушении
- affected_tasks: [26.6.1]
- mitigation: `NO-DIRECT-PUSH-POLICY.md` как декларативное правило
- resolved_in: M27

## KL-04

- description: Permission model не интегрирована с CI
- affected_tasks: [26.2.1]
- mitigation: ручная проверка уровня разрешений
- resolved_in: M27

## KL-05

- description: Violation log пока только шаблон без runtime
- affected_tasks: [26.8.1]
- mitigation: ручное заполнение при нарушении
- resolved_in: 26.8.1 + M27
