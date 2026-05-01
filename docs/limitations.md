# Limitations

## Purpose
Документ фиксирует текущие ограничения AgentOS в границах MVP.

## Current MVP Boundary
AgentOS ограничен ролью guardrail-слоя для AI coding workflows.

## Non-Goals
- Не заявлять production-grade гарантии.
- Не заявлять автономное выполнение без контроля.

## Safety Limitations
- AgentOS зависит от корректности входных артефактов и дисциплины выполнения проверок.
- Safety gates блокируют опасные сценарии, но не заменяют инженерную ответственность.

## Packaging Limitations
- Нет полного packaging/publishing контура в текущем объёме.

## Validation Limitations
- Если обязательные проверки не запущены, готовность не может считаться подтверждённой.

## Human Review Limitations
- Спорные или неполные данные требуют ручного решения через review.

## Known Not Implemented Areas
- install smoke
- example project smoke
- package publishing
- autonomous runner mode
- automatic approval
- web UI
- vector database
- backend service

## What AgentOS Does Not Guarantee
- AgentOS is not a backend.
- AgentOS is not RAG.
- AgentOS is not a vector DB.
- AgentOS is not an agent platform.
- AgentOS is not a model router.
- AgentOS is not a CI/CD platform.
- AgentOS does not guarantee bug-free AI output.
- AgentOS is a programmable guardrail layer for AI coding workflows.

## Relationship to MVP Readiness
- Missing implementation is not a failure if explicitly marked NOT_IMPLEMENTED in the release checklist.
- NOT_IMPLEMENTED is not PASS.
- NOT_RUN is not PASS.
- NOT_APPLICABLE requires a written reason.
