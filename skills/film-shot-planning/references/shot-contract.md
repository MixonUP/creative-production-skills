# Shot contract v1

Use a JSON document with:

- `schema_version`, `project_id`, `revision`, `units`, `coordinate_system`.
- `timeline`: `fps`, `width`, `height`, `frame_start`, `frame_end` inclusive. State the convention once; edit intervals use `[in_frame, out_frame_exclusive)`.
- `reference_policy`: analysis sources, permitted usage and production input restrictions.
- `subjects`: stable IDs, approximate scale, role, appearance provenance.
- `shots[]`: ID, edit interval, camera ID, observed action/framing, estimated camera transform/lens, start/end poses, contact invariants, continuity and acceptance notes.
- `assets[]`: ID, path, role, origin, `allowed_as_generation_input`, parent asset IDs when derived.
- `delivery`: scene/master/per-shot paths, colorspace, FPS, audio policy, trim/hold handling.
- `adapter_ref`: nullable link to an endpoint card. Model settings never alter the meaning of the core timeline.

The scene may use frame 1 for source time 0. At 30 FPS, a cut at 2.6667 seconds becomes frame 81 for the next shot; the preceding shot is frames 1–80. Store this relationship and verify frame counts after encoding.

An adapter card records model identity separately from provider identity, mode, schema URL, check date, input roles, documented limits, attachment syntax, output/seed/audio semantics, billing basis and unresolved fields. Distinguish documented, demonstrated by others, locally tested and accepted in this project. Add another card when changing provider even if the model name is unchanged.

Acceptance values are project choices, not accuracy guarantees. Contact drift may be an immediate rejection even when aggregate image similarity is high. Keep measured values, visual assessment and user acceptance separate.

## Scene continuity and sound handoff

Extend the project's existing manifest only as needed; preserve its parser compatibility. For connected audiovisual work record:

- Reference asset IDs and revisions for identity, costume, location and prop states; distinguish a source sheet from the actual attached crop/image.
- The action's dramatic purpose and observable change in behavior, so visual acceptance is not limited to appearance.
- Sound cue ID, triggering action or edit-relative frame/range, source position/distance, continuity across cuts, and wanted/unwanted dialogue or music. Unknown timings remain provisional until the picture is assembled.
- Planned audio route (native audiovisual generation, external performance, editorial sound or mixed), provider support evidence and intended keep/replace decision. This is not proof the route ran.
- For speaking shots, dialogue take/revision and dependencies on lip sync and picture timing when known. An external voice is not mandatory when the native performance is accepted.

In AI Films use the existing scene-level `E:/AI_films/Tools/AudioStudio/cues_template.csv` and voice card when applicable; link the cues by shot IDs or ranges instead of maintaining contradictory cue lists in multiple files.

## Compile and audit a scene packet

Keep a stable location map separate from the shot's action. State landmarks, the camera side of the action axis, first-frame positions, eyelines, intended path and important distances. Translate world positions into frame-left/right for each actual camera; copying screen-left literally into a reverse angle can contradict the world map. An intentional axis crossing needs a readable staging or edit, not an automatic prohibition.

Select the necessary blocks: context and intended change; actual reference roles; first-frame blocking; single take or planned cuts; framing/camera/focus; feasible timed actions; contact/weight; motivated light; speech and sound; scene-specific performance; protected features. These are production fields, not mandatory headings or a word-count target for every provider.

Check for conflicting common prefixes and shot details: daylight-only versus fluorescent interior; closed hand versus visible object; wardrobe description versus action mentioning an absent jacket; one continuous take versus requested hard cuts. Preserve exact spoken text separately from previous-line context and production notes. Do not pass prestige tags such as 8K as actual resolution metadata.

When a difficult action repeatedly fails, consider splitting approach, contact and consequence, or beginning already in the critical action. Preserve the story's cause and effect in the cut. Do not promote this fallback into a claim that all transition motion is impossible. Record the rejected recipe and why the simpler coverage still serves the scene.

Source-specific evidence and uncertainties are in `E:/Krea_tren_AI/Knowledge/06_Sources/Hell_Grind_Transfer_2026-10-01.md`; these checks improve the specification and do not prove the model obeys it.
