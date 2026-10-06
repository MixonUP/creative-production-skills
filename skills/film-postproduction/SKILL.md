---
name: film-postproduction
description: Assemble and finish film shots in Resolve through MCP, author reusable Fusion effects, plan consistent audio stems and validate exports. Use for editing, compositing, sound postproduction or upscale integration; not LoRA training or initial Blender scene construction.
metadata:
  version: "1.4.0"
---

# Film postproduction

Turn selected shots into an editable, reviewable sequence. Preserve the user's chosen editor, visual style, timing and approved creative decisions. A narrower request such as measuring one file does not require the complete production workflow.

## Get the working contract

For this user's local installation, **never update DaVinci Resolve**: the user fixed Free 21.0.3.7 on 2026-09-30 to preserve MCP. A plugin install or troubleshooting request does not revoke this choice. Consult `Knowledge/01_Project/Environment.md`; only an explicit user reversal changes it.

For DLSS Neural Rendering in Resolve or a ComfyUI-to-Resolve finishing pass, use the installed `dlss5-video-finishing` skill; local state is `Knowledge/04_Procedures/Resolve_DLSS5.md`. For Topaz model selection, CLI enhancement, denoise or retiming use `topaz-video-finishing`; return here for editing, grade and sound beyond that handoff.

For E:/Krea_tren_AI read Knowledge/00_HOME.md and only relevant cards. Current integration assessment: Knowledge/06_Sources/Film_MCP_Stack_2026-09-19.md. Live setup: Tools/ResolveMCP/README.md. These are dated observations; probe before depending on version-specific behavior.

Use the existing shot manifest when available. In this project Tools/FilmPipeline/testfilm_manifest.json is previs, not approved final footage. Establish project/timeline identity, input provenance, selected takes, frame rate, frame ranges, aspect ratio, audio roles and delivery requirements from available evidence. Do not silently promote a candidate take to an approved one.

Read only the reference matching the requested operation:
- [Resolve and Fusion](references/resolve-fusion.md): live editing, effect authoring and API gaps.
- [Sound and finishing](references/sound-finishing.md): stems, audio automation, upscaling and output QC.
- For an editable synthesized effect or short score sketch, route to procedural-audio
  when available; return here for picture sync, sound perspective and final mix.
- For native AI-video sound, dialogue replacement or an original-versus-rebuilt sound comparison, use the source-audio triage in that reference before discarding or separating the soundtrack.
- [Cinematic voices and scene sound](references/cinematic-voice.md): stable voice identity, scene performance, editable voice treatment and continuous sound design; distinguish an observed creator method from our proposed FX chain.
- [Studio sound and Resolve library](references/studio-library.md): detailed voice/ADR/Foley workflow, project templates, audio QC and current MCP capability boundaries for E:/AI_films.
- [Acceptance scenarios](references/acceptance-scenarios.md): evaluating changes to this skill; not a mandatory per-task checklist.

## Make operations observable

Use installed MCP tool schemas and capabilities, then inspect current state. A method's presence is not proof of Free-edition support. Prefer the existing API/CLI to adding a second server for the same application.

For a mutation, retain enough before-state to explain the change; choose the actual target by project name/ID and timeline identity, not an incidental GUI selection. Apply a small meaningful operation, read its result, and verify the generated artifact or viewer when pixels/sound changed. An API true result proves neither visibility nor artistic quality. Use new timeline/output revisions for rebuilds, keeping source media intact unless the user explicitly requests replacement.

Represent positions in integer frames with an explicit range convention. Translate inclusive/exclusive ends at each API boundary; account for timeline start timecode separately. Preserve source handles needed by transitions. Avoid repeated lossy exports between stages.

Keep one writer per live project. On this single-4090 machine serialize heavy GPU jobs; CPU metadata analysis can run independently. Do not infer permission to interrupt training from an editing/integration task.

For paid generation routes, persist provider/model/task ID and input identity after submit, then query that task after timeouts. A timeout is not permission to resubmit and incur another charge. This skill does not select or purchase a provider when the task is postproduction only.

## Separate creative and technical acceptance

Judge reference matching on composition, silhouette, camera motion, action timing, character identity, graphic texture and sound continuity. Numerical QC is a separate result. For stylized animation, do not automatically smooth motion, denoise intentional texture or add film grain to improve a generic quality score.

Report the delivered artifact, checks actually performed and material unresolved items. Distinguish prepared, installed, callable, executed and visually/audibly accepted. If no media was rendered, say so. Record meaningful outcomes and corrections in the project's journal and affected card; new tutorials remain untested until a relevant experiment passes.
