---
name: film-shot-planning
description: Break a film reference or brief into shots and prepare a model-independent plan for Blender previs, image references, video generation and editing. Use for matching composition, timing, continuity or choosing a generation route; not for LoRA training.
metadata:
  version: "1.2.0"
---

# Plan shots that survive a change of model

Read the project's knowledge index and only the relevant brief, source and experiment cards. In `E:/Krea_tren_AI`, start at `Knowledge/04_Procedures/Film_Workbench.md`. Preserve the user's current authorization; an old note postponing Blender does not override a new request to build it.

## Establish the shot contract

Inspect the actual reference when available. Record source dimensions, duration and frame timestamps; do not assume nominal FPS equals constant FPS. Separate observations from estimated camera values. A plausible lens chosen for a reconstruction is not recovered source metadata.

Describe each shot with stable ID, half-open edit interval, subject action, start/end pose, framing, eyeline, screen direction, contacts, overlaps, background, light and sound intention. Use one common scene coordinate system. Record what must match and what may change. Mark mixed transitions separately from hard cuts. Keep the artistic target concrete: palette, contour, shape, texture and temporal behavior, not just a named style.

Keep a machine-readable shot plan beside the human-readable review. Follow [the handoff contract](references/shot-contract.md). The contract belongs to the project and has its own revision; it must not embed provider-specific parameter names.

For a connected scene, map each shot to the relevant versions of character, costume, location and prop state; choose readable references for that shot instead of passing the entire library. Express sound as timed events and perspective: what starts it, where it is, what continues across the cut, and whether dialogue/music is wanted. The sound contract is an intention; an AUDIO prompt does not prove execution or final use. Keep one scene-level event map even when video is generated shot by shot.

Compile the generation handoff from the scene packet, not the full screenplay. Audit active references, first-frame geography, feasible action beats and exact speech against each other. Keep a same-shot continuation distinct from a hard cut even when an author's prompt labels both as SHOT. Use the compilation checks in the handoff reference for ambiguous or contradictory source prompts.

## Choose the control route

- Use a 3D animatic when spatial layout, camera, contacts or repeated angles are important. Ask `blender-film-blockout` for the scene when available; otherwise perform that work directly.
- Use first/last frames only when the selected endpoint supports that exact mode and the two images describe one coherent action/camera.
- Treat video reference, motion transfer, image conditioning, depth and explicit camera controls as distinct capabilities. Similar marketing names do not make them interchangeable.
- Match a route to a dated **provider + model ID + endpoint + mode** card. Check current primary documentation before spending money or asserting compatibility. Unknown means unverified, not supported.
- Keep exact edit timing, reusable shadow elements and a continuous audio master in the editor when that gives more control. A prompt requesting exact camera preservation is not a technical lock.

## Prepare a generation handoff

Keep structure and appearance roles explicit: the project's animatic sets framing/motion; owned appearance images set identity, costume and style. Number/reference attachments according to the selected adapter, not a universal token syntax. Audit actual selected assets and their derivation chain against the brief. A reference restricted to viewing may inform written observations, but must not become a generation input, texture or reconstructed camera track.

Export a clean master and independent shots. Include handles/holds only when needed by a selected endpoint; preserve the edit interval in a trim manifest. Do not stretch an action to fill a provider's minimum length. Do not assume a LoRA file can be passed to a hosted video API.

Estimate cost for the exact request category, including reference-video input, attempts and useful seconds retained. Prepared request manifests do not authorize paid submissions. Once a paid run is authorized, avoid duplicate submissions on uncertain status; record the provider request ID before retrying.

## Accept based on observable results

Compare matching time positions, not equal frame numbers at different FPS. Inspect first, last, contact and maximum-motion frames. Evaluate framing/occlusion, contacts, motion timing, identity/style and sound separately. A completed render is not an accepted shot. Set a small experiment budget appropriate to the task; repeated identical failures call for an input/route change.

Record original inputs, plan and adapter versions, actual request, output, latency/cost if known, and visual findings. Update the affected card and journal. Keep future ideas in the backlog rather than expanding the current production automatically.
