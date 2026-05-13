# Clean Template Boundary

## Purpose

This document defines the boundary between the AgentOS source repository, the AgentOS clean template, and a user project instance.

## Core Rule

A user who starts from the AgentOS clean template must receive a clean project instance, not AgentOS development history.

## Repository Types

### AgentOS Source Repository

Contains:

- AgentOS development history
- milestone reports
- evidence reports
- completion reviews
- dogfooding records
- roadmap notes
- source templates
- source scripts
- source docs

The source repository must not be copied directly into user projects.

### AgentOS Clean Template

Contains:

- full-capable AgentOS structure
- Simple Mode enabled by default
- minimal first-user docs
- user mode documentation
- task templates
- verification templates
- validation scripts
- empty task structure
- empty report structure
- runtime directory placeholder
- GitHub issue template for first task creation

The clean template must not contain previous project evidence.

### User Project Instance

Contains:

- user project files
- local AgentOS tasks
- local AgentOS reports
- local verification evidence
- local runtime status
- local known limitations

## Default Mode

The clean template defaults to Simple Mode.

Simple Mode exposes only:

- first task path
- current task status
- risk
- next safe action
- basic validation result
- human decision request if needed

Advanced and Full modes may expose more details only by explicit user intent.

Full Mode must not grant additional permissions.

## Must Include

The required clean template file list is defined in:

- templates/agentos-clean/template-manifest.yml

## Must Not Include

The clean template must not include:

- milestone reports from AgentOS source repo
- reports/m37*
- reports/m38*
- reports/m39*
- reports/m40*
- completed task history
- failed task history
- old active-task content
- previous completion reviews
- previous evidence reports
- source repo context index
- runtime cache
- local STATUS.md
- user-specific notes
- personal roadmap notes
- dogfooding evidence
- old context packs

## Runtime Boundary

Runtime/generated files belong under \`.agentos/runtime/\` and must be gitignored.

Runtime files are not source of truth.

## GitHub Template Boundary

GitHub "Use this template" should produce a repository that is ready without requiring the user to run cleanup scripts manually.

Bootstrap automation may validate cleanliness.

Bootstrap automation must not silently approve, commit, push, or modify protected files.

## User Simplicity Rule

The user-facing path should be:

1. Use this template.
2. Create repository.
3. Create an AgentOS task through the visible Simple Mode path.

After that, the repository must already be clean and prepared for first task creation.

## Non-Claims

This clean template does not claim:

- production readiness
- production-grade sandboxing
- guaranteed safe AI output
- automatic approval safety
- SaaS readiness
- public release completion
