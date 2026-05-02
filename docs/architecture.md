# Architecture

## Purpose
Этот документ описывает архитектуру AgentOS на верхнем уровне, без рекламных утверждений о готовности.

## AgentOS Definition
- AgentOS is a Markdown-first guardrail framework.
- AgentOS is a deterministic validation layer.
- AgentOS is a controlled lifecycle workflow.
- AgentOS is a structured guardrail system for AI-assisted coding.

## Architecture Overview
AgentOS связывает документы, проверки и контрольные ворота в один управляемый процесс.

## Markdown-First Model
Источник правил и контракта — Markdown-документы. Скрипты читают и проверяют эти правила.

## Core Artifact Groups
- Контрактные документы (`docs/`)
- Проверяющие скрипты (`scripts/`)
- Фикстуры для воспроизводимых проверок (`tests/fixtures/`)
- Отчёты с доказательствами (`reports/`)

## Gate Pipeline Overview
INTENT
→ POLICY
→ APPROVAL_REQUIREMENT
→ APPROVAL_EVIDENCE
→ PRECONDITIONS
→ CONTROLLED_APPLY
→ VALIDATION
→ AUDIT
→ EVIDENCE

## Release Readiness Layer
M20 добавляет слой оценки готовности релиза на базе уже существующих safety-границ M19.

## What AgentOS Does Not Do
- AgentOS is not an autonomous agent platform.
- AgentOS is not a backend service.
- AgentOS is not a vector database.
- AgentOS is not a RAG platform.
- AgentOS does not guarantee bug-free AI output.

## Relationship to Milestone 19
M19 ввёл единый non-bypass gate contract и машинно-проверяемые маркеры.

## Relationship to Milestone 20
M20 определяет критерии Stable MVP readiness, но не объявляет готовность автоматически.

## Non-Goals
- Не вводить новую safety-layer сверх M19.
- Не объявлять production readiness.
- Не объявлять MVP-ready в этом документе.
