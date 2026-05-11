# AgentOS User Modes

## Simple Mode

Default mode.

Shows:

- first task path
- current task
- risk
- next safe action
- basic validation result

Hides:

- audit internals
- context internals
- advanced policies
- adapter details

## Advanced Mode

Shows:

- validation details
- report links
- dry-run summaries
- troubleshooting details

## Full Mode

Shows:

- policies
- advanced templates
- audit internals
- adapter docs
- context internals

## Permission Boundary

Changing user mode does not grant the agent extra permissions.

Full Mode does not authorize:

- bypassing human gates
- bypassing validation
- automatic approval
- destructive workflows
- raw push
- production use
