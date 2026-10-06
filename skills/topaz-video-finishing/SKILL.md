---
name: topaz-video-finishing
description: Enhance, denoise, upscale and retime video with the installed Topaz Video on Windows, prepare reproducible CLI jobs, compare models and return verified media to Resolve through MCP. Use for Topaz video finishing; not Topaz Photo/Gigapixel or game DLSS.
metadata:
  version: "1.0.0"
---

# Topaz video finishing

Use the existing Topaz installation to solve a visible shot defect. Preserve composition, character identity, intended cadence, sound and colour. Choose the lightest treatment that passes a moving comparison; a newer or more expensive model is a candidate, not a quality result.

## Local contract

- **Never update this user's Resolve Free 21.0.3.7.** The user froze it on 2026-09-30 to preserve MCP; only an explicit reversal changes this. Do not change Resolve/driver/Comfy dependencies to make Topaz research work.
- Topaz Video **1.7.0.0** is installed. Proteus `prob-4` 2x completed a real render on 2026-09-21; the ProRes result was subsequently imported through the Resolve bridge. Do not repeat the obsolete claim that Topaz is untested or needs purchasing.
- The working route is **Topaz standalone/CLI → new media file → existing Resolve MCP**. No dedicated Topaz MCP tool was found in the 2026-09-30 tool catalog. The official OFX requires Resolve Studio; finding its bundle on disk does not make it usable in Free.
- On this single RTX 4090, serialize heavy GPU work. Research, skill preparation and metadata checks do not authorize starting/stopping GPU jobs or cloud renders. A request to process a clip does authorize the scoped render; don't ask again merely because this skill has a preview stage.
- Read `E:/Krea_tren_AI/Knowledge/00_HOME.md`, then the relevant Topaz card. Canonical skill source is `Tools/skills/topaz-video-finishing`; the installed copy is managed with `Tools/manage_film_skills.py`.

## Pick the relevant depth

| Task | Read |
|---|---|
| Installation, existing success, exact paths | [Local evidence](references/local-state.md) |
| Faces, noise, sharpness, newer diffusion models | [Models and controls](references/models-controls.md) |
| CLI job, missing encoder/model, memory error | [Windows CLI](references/windows-cli.md) |
| Timing, audio, colour and Resolve MCP return | [Round trip](references/resolve-roundtrip.md) |
| Model comparison, moving QA, acceptance | [Evaluation](references/evaluation.md) |
| Tutorials, GitHub skills and claim provenance | [Learning and sources](references/learning-sources.md) |

For editing/grades/audio design beyond the Topaz handoff use `film-postproduction`. For DLSS Neural Rendering use `dlss5-video-finishing`; DLSS relighting and Topaz restoration are different operations. Don't add both merely because both exist.

## Operational loop

1. Identify the source and delivery contract: source hash/path, progressive/interlaced, rational FPS and cadence, integer source range, dimensions/SAR, SDR/HDR/colour tags, audio tracks, output size and approved motion. Inspect media; filenames and presets are not measurements.
2. For a clean AI-generated shot, start the comparison with the proven conservative Proteus route. Select one alternative for the actual defect. For artificial skin with sound geometry, consider Starlight Precise 2.6 as an **untested local candidate**; verify its GUI availability, model data and resources before promising a render.
3. Freeze a recipe with exact model ID/version, GUI mode or exported command, source range, encoder, model directories, colour/audio treatment and output path. `scripts/prepare_baseline.py` writes a **plan only** for the narrow historical H.264 SDR progressive 2x route. It does not process video, download weights or validate activation. Unsupported input needs a tailored plan, not forced conversion to fit the helper.
4. When processing is requested, compare a short moving interval, then render the selected settings to a new revision. Use non-overwriting outputs, argv lists rather than shell interpolation, explicit logs and exit codes. GUI slider numbers do not map universally to CLI floats; derive unfamiliar modes from the installed app's exported command and local help.
5. Validate frames/PTS, dimensions, audio and colour, then inspect motion. A successful filter call, licence heartbeat, metadata probe or still frame alone is not final acceptance. Reimport through MCP only into the intended project/timeline revision and read back the result.
6. Append evidence and unresolved issues to `Knowledge/07_Journal/YYYY-MM-DD.md`, update `Knowledge/04_Procedures/Topaz_Video_Finishing.md`. Preserve old records with dated corrections. Tutorials remain externally supported until an actual local experiment demonstrates their result.

Report separately: prepared, locally executed, technically passed, visually/audibly reviewed, accepted by user. Do not claim a universal best model or infer a fresh account entitlement from an old successful run.
