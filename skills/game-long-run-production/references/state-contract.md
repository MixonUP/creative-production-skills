# Compact state and acceptance

Create these only when starting or continuing an actual implementation run. Resolve
their paths against the selected game project. Templates are examples; preserve an
existing working project format.

## Docs/state/STATE.md

- Updated timestamp, branch/revision, current playable checkpoint.
- Current task and latest user correction.
- Now: one active integration item.
- Next: a few concrete actions, with paths and acceptance IDs.
- Running: known job IDs, owner and receipt path.
- Health: compile/runtime status, material resource concerns.
- Evidence: most recent native check and remaining failures.

Keep it concise enough to restore context; archive completed history without discarding
source evidence. Do not forbid reading an older file if a contradiction requires it.

## Acceptance record

Each item needs an ID, criterion, priority, required scenario, status, checked revision,
evidence path, assistance used and unresolved issue. Allowed statuses include
not-run, passed, failed, partial and blocked. Failed/partial is not passed.
Store human visual acceptance separately.

A changed criterion needs an attributable user/design decision, not only a new score.
Report both the original and revised target when comparing results.

## External-job ledger

Append provider, job ID, submitted time, input hashes, output location, status and
actual cost/credits when available. Keep estimates separate from billed cost.
Store secret values in the configured credential mechanism, not in the ledger.

## Optional work-lane card

Task, owner, allowed paths, inputs, outputs, interface assumptions, test scenario,
integration dependency, evidence path and result. For concurrent execution establish
exclusive editor ownership. Long output belongs in files; short handoffs state result,
paths, evidence, cost and remaining issue. Size limits are adjustable, not universal.

## Run boundary

Record the task's actual deadline/budget and completion condition, if provided.
Unknown spending authorization does not become a numeric allowance.
Use the host's goal/automation feature only when the user explicitly requests it.
Keep this metadata separate from Claude hook-specific session_window.json.

