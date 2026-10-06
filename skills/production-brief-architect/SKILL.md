---
name: production-brief-architect
description: Turn a rough game or video idea and references into a detailed production brief, executable agent prompt and observable acceptance criteria. Use to author or strengthen a master prompt, specification or production handoff; not to start the build or media generation.
metadata:
  version: "1.1.0"
---

# Production brief architect

Produce a brief another capable agent can execute without reconstructing the user's
intent from the conversation. Strength comes from decisions, consistent constraints,
concrete examples and observable outcomes, not length, prestige adjectives or commands
to ignore limitations.

Write in the user's language. Reuse accepted decisions and project facts. Reading this
skill or drafting a kickoff does not execute the kickoff.

## 1. Establish the assignment

Identify the medium, desired audience experience, deliverable and requested depth.
Choose game, video, or a hybrid with separate runtime and editorial deliverables.
Read only relevant project instructions, existing specifications and supplied references.
Do not replace an existing engine, style, cast, story or approved pipeline by default.

For a reference-led assignment or tool interaction plan, read
[reference and tool loop](references/reference-tool-loop.md). Connect each selected
reference property to a controllable parameter, a concrete first artifact and a review.

Distinguish:
- confirmed user requirement;
- observed project fact, with path/source;
- proposed design decision;
- working assumption, with downstream impact;
- unresolved dependency or blocking conflict.

If two consequential requirements conflict, expose the tradeoff and propose a resolution.
Do not silently weaken either. Ask only the few questions that change feasibility or
the core experience; continue independent design work. For optional choices give a
recommended assumption and keep it visible. Missing paid-tool access is not permission
to invent access, buy credits, or switch the approved provider.

## 2. Make the experience concrete

Define the premise, the experience that makes it distinctive, and a few design principles.
Turn each principle into a player/viewer consequence, an implementation direction and
a review test. Separate stable vision from this delivery's scope and later ambitions.

Describe one distinctive playable or cinematic moment through setup, action, response
and consequence. Let the first representative test preserve that experience even when
secondary detail is simplified; a polished generic moment does not test the premise.

Describe the actual experience in order, including transitions, quiet moments, decisions,
payoffs and recovery where relevant. Add creative detail that serves the idea; label
new substantive choices as proposals. When the user already chose a direction, deepen
it rather than reopening it with an unrelated menu of concepts.

Make numbers legible: unit, source/status and reason. A proposed 60 FPS budget, lens,
population, duration or retry count is a target, not measured capability.

## 3. Expand the correct production contract

Read [game contracts](references/game-contracts.md) for games and
[video contracts](references/video-contracts.md) for video. Load both only for a hybrid.

For every consequential element connect:
intent → concrete behavior or visible beat → input/asset → owner or production method
→ dependency → acceptance evidence → known limitation.

Use an explicit full-scope versus first-delivery split. Reduce secondary breadth before
cutting the defining experience. Prove a representative end-to-end chain before scaling
the asset/shot library. Do not prescribe one fixed time budget or milestone count.

Keep host-independent design separate from a dated tool adapter. Verify current primary
documentation when naming an API capability, supported mode, model ID, price or limit.
If the tool isn't selected or documentation unavailable, produce a usable semantic
contract and mark the adapter unresolved; do not fabricate executable fields.

## 4. Write the deliverable pack

Default to three useful Markdown artifacts (or three clearly delimited sections when
files cannot be written):

1. MASTER_BRIEF: the full, specific assignment written for the production agent;
   requirements, creative direction, contracts, production order and constraints.
2. KICKOFF: a short entry prompt naming the brief, relevant project root, first real
   step, verification loop and completion boundary. It must carry critical constraints
   so they are not lost, but should not duplicate the entire brief.
3. ACCEPTANCE: stable criteria IDs and repeatable scenarios, expected results, evidence
   types and current status. All unexecuted checks remain not-run.

Scale the structure to the work. A single shot can use one compact file. A long film can
split shot list and per-shot generation briefs into linked documents without duplicating
the same requirements. When the user requests one prompt only, return one self-contained
copyable prompt with these elements.

Use the stand-alone [game meta-prompt](assets/MASTER_GAME_BRIEF_RU.md) or
[video meta-prompt](assets/MASTER_VIDEO_BRIEF_RU.md) when the user wants reusable input
they can paste into another assistant. Both work without this skill being installed.

## 5. Review the brief before delivery

Apply [quality review](references/quality-review.md). Fix contradictions and omissions,
then give a concise record of what changed, unresolved decisions and readiness.
Test the specification mentally against an ordinary use, an interruption and a missing
dependency; for video also check edit-time arithmetic and continuity across a cut.

No self-assigned score proves production quality. Do not mark a feature implemented,
a shot rendered, a paid route available or the user's taste accepted from a document.
Keep failed criteria visible; changing them requires a documented decision.

## Environment fit and handoff

In the Krea workspace use Knowledge/00_HOME.md and relevant current cards. Existing
GamesDev and film workflows retain their ownership; source knowledge is local Markdown.
For GamesDev, preserve Main/RnD separation and engine.json choices. DaVinci Resolve
21.0.3.7 Free is pinned by the user; this skill never makes an upgrade a prerequisite.
Do not turn an unrelated new video/game into an AIWAIFU production merely because
that project is present.

For actual execution, route to the relevant available gameplay/animation/UI/VFX/audio
or film planning/visual development/production skills. Skill names are optional routing,
not imaginary installed dependencies. Parallel lanes are a design option; do not spawn
agents or create autonomous schedules from this authoring request.

[Provenance and evidence limits](references/sources.md).

