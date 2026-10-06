# Sound, upscale and delivery

## Consistent sound across shots

Choose recorded/licensed material, native generated audio, an external audio model or
procedural synthesis according to the cue. Code-driven oscillators, noise, resonances
and envelopes can make controllable mechanical/UI effects and musical sketches. Use
the available procedural-audio skill for editable recipes and a local audition bank;
do not mistake that technical sketch for a performed film score or natural Foley.

Before a batch, compare a small set of meaningful variants at comparable listening
levels. Retain cue IDs, reference excerpt/property and the reason for the chosen take.
Audition without commentary over the sound, then against the fixed picture revision.
Transfer the chosen file with its cue start, tail/handles, sample rate and frame anchor.
Music stems need the same musical grid and harmony as well as equal file lengths.

Use independent stems with a shared sample rate, start and duration: ambience, Foley, character/creature events, music and dialogue when present. Generate or source missing events, then edit them to picture. Keep recurring sound identity and continuous ambience across cuts; do not regenerate unrelated complete mixes for every angle.

Use the host's native audio tools for straightforward jobs. Resolve API does not expose complete Fairlight plugin parameter graphs. For a task explicitly requiring detailed programmable FX automation, consider REAPER/ReaScript; first enumerate installed FX and parameter names, then read back changes. REAPER and its MCP are candidates here, not yet installed/tested. Do not substitute them when the user wants a simple Resolve edit.

Voice consistency requires a fixed authorized voice, pronunciation and delivery direction, not just a seed. Separation models such as SAM Audio isolate existing sound; Foley models generate it. Record generated/licensed source provenance. Choose loudness/true-peak requirements from the requested destination; do not normalize every mix to a single universal LUFS value. A loudness meter does not judge emotional timing, masking or unnatural room acoustics.

## Triage native AI-video sound

Listen with picture before choosing what to keep. Record source file, selected take and picture revision. Evaluate event synchronization, performance, unwanted speech/music, changing room tone and clipping separately. A source AUDIO prompt establishes requested sounds, not their audibility or use in the final edit.

- Keep an effective synchronized source region when it fits the scene; save the untouched original and edit a derivative.
- Supplement missing events and continuous ambience without accidentally doubling the same footsteps, impacts or room tone already present in the source mix.
- Replace or separate a problematic layer only when the expected benefit justifies it. A single mixed soundtrack does not contain clean deliverable stems; separated estimates can introduce artifacts and require listening. Do not label an incomplete dialogue-muted mix as M&E.

For external dialogue, select the performance in scene context before final mouth work where the production route permits. Preserve the dry accepted take and its revision. If a native generated performance already works, do not require a second voice provider. Changing speech duration can invalidate the lip sync and picture timing; recheck the dependent shots and mix boundaries.

For a sound-design comparison hold the picture version fixed and use comparable playback loudness. Record performance, causal timing, spatial continuity, masking, preference and repair effort separately. Without listeners, describe an editorial assessment rather than an audience preference result. When performance changes require new picture timing, label it a different combined production variant, not an isolated sound comparison.

## Upscale selection

First accept content and motion. Compare a short, representative moving segment at identical output dimensions and FPS: source baseline, available Topaz and available SeedVR2. Inspect eyes, contours, graphic texture and frame-to-frame stability; measure time and memory. Choose one final path unless a measured two-stage benefit justifies another pass. Do not enable optical-flow interpolation merely because 60 fps looks smoother; preserve the intended animation cadence.

Correction 2026-09-30: Topaz Video 1.7.0 completed a real Proteus prob-4 2x render on 2026-09-21; the ProRes master was imported into Resolve at 09:54. Earlier wording that activation/processing were untested is obsolete. Historical success is not proof of current account entitlement or every new model. Use `topaz-video-finishing` for exact evidence, models, CLI and round-trip QA. Official Topaz OFX requires Resolve Studio; our Free host uses standalone file handoff. Do not remove or upgrade the user's Topaz as part of ordinary integration research, and never update their fixed Resolve 21.0.3.7.

## Technical acceptance

E:/Krea_tren_AI/Tools/FilmPipeline/media_qc.py provides CPU-only ffprobe frame counting, average FPS/dimensions checks, decode-to-null and ebur128 measurement of the first audio stream. Run it using Tools/ResolveMCP/.venv/Scripts/python.exe; no package installation needed. Write reports separately from source media. It has a 180-second per-process timeout and is suitable for short clips; adapt deliberately for long jobs.

This helper does not establish constant per-frame PTS, correct color appearance, lip sync, absence of visual artifacts or artistic reference fidelity. If those matter, add timestamp checks and actual audiovisual review. Recheck duration/FPS, dimensions/aspect, channel layout, sample rate, color/range tags and peaks after the final encode; compare with the delivery contract. Do not call tag relabeling a real color transform.

For source-driven compositing preserve linear/scene-referred versus display-referred distinctions. Do not apply an additional display transform to AI video that already has a baked SDR appearance. OTIO is an editorial interchange, not a guarantee that every effect or grade survives a round trip.
