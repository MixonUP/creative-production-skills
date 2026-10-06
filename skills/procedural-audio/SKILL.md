---
name: procedural-audio
description: Design and synthesize reproducible sound effects, tonal cues and short musical sketches with code, then deliver WAVs, editable recipes and an audition page. Use for mechanical sounds, UI, impacts, transitions and adaptive music prototypes for games or film.
metadata:
  version: "1.0.0"
---

# Procedural audio for games and film

Translate a reference into an editable sound recipe: excitation, resonances, pitch
motion, amplitude envelope, noise, rhythm and space. Choose synthesis when parameter
control or reproducible variation is useful. Recorded Foley, licensed samples and
dedicated music models remain valid routes for natural performances or rich scores.
Do not make an all-code challenge a restriction on the user's production.

## Reference and cue contract

Read [reference and listening method](references/reference-method.md). Establish cue
ID, role, triggering event or picture frame, duration/tail, distance, variation range
and source permission. Distinguish a viewed spectrum, a listened-to excerpt, a written
description and an inferred recipe. A spectrum alone does not prove timbre quality.

For music separate the score (notes, rhythm, harmony, form) from the instrument and
mix. Keep an original motif. For adaptive layers share bar count, tempo, time origin,
sample count and harmonic plan; equal durations alone do not make layers compatible.
A music sketch is not a finished orchestral performance.

## Build a small editable candidate

Pick the smallest cue that tests the hard part. Example: servo pitch follows speed;
a metal contact combines a short excitation with inharmonic decaying resonances.
Expose useful controls such as weight, brightness, attack, damping and speed.

Use [the renderer contract](references/renderer.md) for the bundled CPU renderer.
It uses Python + NumPy and standard-library WAV output; no API key, GPU or DAW is
required. Discover a working Python with NumPy; do not install into training or
ComfyUI environments. Keep recipes and output revisions outside this skill.

Keep random seeds, units, renderer/config hashes and source provenance. Regenerate
a new revision, not the accepted original. The bundled demo is an original technical
study, not extracted audio or reconstructed code from the source video.

## Review before integrating

Deliver an audition page with cue IDs, visible variants, direct playback, measured
waveforms and the reference property each candidate tests. Avoid narration over the
audition. Compare at reasonable, comparable playback levels; sample peak matching is
not perceptual loudness matching. Listen both alone and in the actual scene.

Check sample rate/channels/sample count, clipping, DC, unwanted silence and loop
boundaries separately from aesthetic judgement. The bundled report measures sample
peaks/RMS and a boundary step; it does not measure true peak/LUFS or certify a loop.
Listen over several repeats and check tails at the actual trigger rate.
If listening is unavailable, say so and leave listening/selection pending.

## Handoff

For a game, hand selected cues to game-audio-workflow when available: contacts, cancel,
cooldowns, voice limits, distance and mixer ownership. Do not generate an impact on
a missed hit. For a film, use the current editor/film-postproduction: exact picture
revision, frame-to-sample mapping, handles and aligned stems. Do not launch an editor,
change a timeline or upgrade Resolve merely to prepare a library.

Return WAVs, editable config/score, script version, technical report, audition page,
cue-to-event/shot map and review state. Never claim engine integration or a listener
preference from a successful WAV write.

[Source and adoption limits](references/source.md).

