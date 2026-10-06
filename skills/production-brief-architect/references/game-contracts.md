# Game brief: enough specificity to build and test

## Player experience and scope

State the player role, immediate activity, meaningful choice, feedback and reason to
repeat. Describe the first playable route from ordinary launch to a recognizable result.
Specify session structure and progression only to the level required by this delivery.

Keep separate: overall ambition, representative first delivery, later roadmap. A
multi-character vision need not require a dozen finished characters in the first test,
but the first slice should test the real scaling assumption rather than hard-code one
hero everywhere. Do not add combat, crafting or an economy to a peaceful exploration
game simply because a template has headings for them.

Translate artistic principles into decisions:
"Uneasy intimacy" could mean close conversational camera, restrained background noise,
a character who remembers a relevant previous promise, and one visible hesitation.
It does not by itself require horror monsters, a new lore system or a combat loop.

## System contracts

Use the following fields for systems that affect play; group trivial systems:

| Field | Decision needed |
| --- | --- |
| Purpose | What the player gains or understands |
| Inputs | Actions/devices, preconditions, valid targets |
| State | States, entry/exit conditions, authoritative owner |
| Outcome | State mutation and visible/audible feedback |
| Timing | Duration/cooldown/markers; source or proposed tuning |
| Interruption | Cancel, death, pause, menu, target disappears |
| Repetition | Double input, retriggering, concurrency, idempotence |
| Persistence | What survives save/load/restart, if in scope |
| Integration | Events/data contracts and affected systems |
| Verification | Ordinary route, important boundary, failure case |

A hit effect must follow confirmed contact, not every attack button press. UI values
come from gameplay state; overlapping UI/world input needs a declared owner. Root
translation and facing must have a single owner. These are integration requirements,
not instructions to introduce an unnecessary framework.

For AI NPCs, separate identity, temporary state, personal memory, relationship to the
player, perceived world facts, and allowed actions. Define what the engine validates
before changing the world. A model saying "the door is open" cannot be the saved door
state. Add unavailable-model, timeout/cancel and voice interruption behavior when relevant.
Do not promise emergent personalities or stable long-term memory from tags alone.

## World and art

Describe readable routes, landmarks, entrances/exits, scale, elevation and encounter
placement. State how navigation/collision and camera obstruction will be checked.
A top-down sketch is not proof that the normal controller can traverse the route.

For visual direction specify silhouette, value separation, palette roles, materials,
lighting motivation, density, camera height/FOV behavior and motion style. For every
reference record which property to borrow and which property is irrelevant. Exact
camera/material values may be proposed; do not present them as recovered metadata.

Asset families need identity/variation rules, units/axes, pivots, materials, collision,
rig/clip contracts and intended on-screen size as appropriate. Separate source meshes
and generated originals from runtime exports. Test one representative family member
through the real engine import before multiplying assets.

Use an asset matrix when the cast or world is substantial:
ID; purpose; source/route; first-delivery quantity; final ambition; fidelity priority;
runtime needs; dependencies; acceptance. A missing provider should not erase the
design; give a reversible placeholder route and its explicit replacement point.

## Technology and budget

Reuse the project stack and scene/component conventions. Specify responsibilities,
source of truth and interfaces before file trees. Inventing 50 filenames is not an
architecture. Cite existing paths when actually inspected; mark proposed ones.

Tie performance targets to device, output resolution, renderer, representative scene,
measurement method and frame-time metric. Average FPS cannot describe stutters.
A development RTX 4090 is not automatically the minimum user machine. Until hardware
is chosen, label budgets provisional and define the first measurement.

Separate verified local capability, proposed setup and unavailable dependency. Preserve
tool version locks. Reuse stable asset/character IDs and data-driven variants where
scaling needs them. Avoid speculative framework work for future features outside scope.

## Production and acceptance

Useful order, adapted to the task:

- capability/path check only where necessary;
- playable greybox route with real controls and result;
- one representative asset/rig/effect chain in the engine;
- complete required behavior and actual progression;
- coherent visuals/audio/UI on representative load;
- ordinary packaged launch and release checks if a build is requested.

A milestone requires an observable exit condition, prerequisites and named evidence.
Do not call a stage complete solely because its allotted time expired.
Keep debug-assisted progression separate from actual progression; report both.

An acceptance row has ID, requirement, setup, player actions, expected outcome, failure
signals, evidence type, tested revision and status. Include visual review separately
from deterministic state checks. Use motion evidence for motion, native captures for
appearance, logs/state readback for behavior, and an actual build for release claims.

Example of a precise requirement:
"With clue C01 found, interact with door D01. One interaction begins opening. A second
press during opening creates no second reward. Leaving the interaction zone cancels
an uncommitted request. If save/load is included, the opened state persists after restart."
The exact clue, timings and cancel policy must come from the user's game or be marked
proposed; this example is not a mandatory mechanic.

