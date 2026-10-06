---
name: game-long-run-production
description: Organize and continue a sustained AI-assisted game build using a playable milestone, compact state, job receipts, acceptance evidence and scoped integration. Use for a long implementation run or recovery after interruption.
---

# Sustained game production

Apply to the requested project and deliverable. Installing or reading this skill does
not start a run. Preserve the user's current engine, approvals, budget, tool versions
and stop/pause instructions. A long run is useful only while it produces the requested
game outcome; finishing it does not authorize inventing a new backlog.

## Define the build contract

Describe a short playable route from launch through the core action to its result.
Define priority criteria with stable IDs, target hardware and evidence type. Separate
visual quality, gameplay correctness and performance. Start with a functioning greybox,
then prove one representative asset end to end before multiplying characters/stages.

Keep planned criteria and measured results separate. Record later user changes with
date and rationale rather than lowering the original benchmark invisibly.
[Run templates](references/state-contract.md) provide a minimal state format.

## Work and recover

Use a concise STATE with current revision, changed files, latest evidence, next actions,
running job IDs and blockers. Keep acceptance, decisions and completed history outside
that hot state. After context recovery inspect current disk and any newer user input;
a saved next action is not authority to ignore a correction.

Advance through implement → integrate → run → inspect → repair. Keep the ordinary game
launch and player route alive after meaningful integration batches. Run builds against
a refreshed, successfully compiled revision; bind results to that revision. Distinguish
a bot-assisted scenario from a normal player progression test.

For external jobs save submission ID, provider, parameters/source hashes, intended
output and status. A network timeout means status unknown until checked: resume the
existing job before submitting a paid duplicate. Do not infer spending authorization
from sample budgets in an imported kit.

If parallel agent work is authorized by the current task/environment, give each lane
owned paths, inputs, interfaces, outputs and its verification. One integrator owns the
live engine/editor. Reconcile code before editor refresh, and declare builder order so
rebuilding geometry cannot silently erase dressing. Otherwise use these lanes as
sequential work packages; this skill does not itself authorize spawning agents.

## Bound resource use and continuation

Track active work separately from elapsed time and pauses. Check storage/RAM when
large imports, captures or generation batches warrant it. Do not kill unrelated
processes or delete source media to clear space. Identify processes started by this
run and their children before cleanup; stop only owned jobs within scope.

Respect the actual run boundary: user stop/pause, completed objective, authorized
budget/deadline, or a condition that cannot progress safely. Preserve state and report
remaining failed criteria. Do not treat missing/malformed run limits as unlimited work.
Creating a goal or a scheduled continuation requires the user's corresponding request;
a skill installation supplies neither. Do not silently create an automation.

## Review and handoff

Capture the real game path at normal camera/scale. Record realtime FPS separately
from offline frame-by-frame video; a smooth offline render proves no frame budget.
Check controls, real progression, cancellation, collision and saves where applicable,
rather than allowing debug assistance to stand in for them. Record assistance explicitly.

Use native clips for movement/transition claims and screenshots for detail. A generated
concept or reviewer score is not a passing engine result or human acceptance.
Deliver build/source paths, tested revision/scenarios, remaining failures and receipts.

## Host-specific hooks and public distribution

The original author's Claude hook kit is not included in this public edition.
Use the portable state, receipt and acceptance workflow above. Read
[host integration notes](references/claude-hooks.md) before considering hooks.
Do not claim that an external hook is installed or portable across agent hosts.

[Sources and scope](references/source.md).
