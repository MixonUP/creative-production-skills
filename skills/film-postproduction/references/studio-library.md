# AI Films studio library

For sound design, voiceover, ADR or reusable Resolve setup in this studio, start at
E:/AI_films/Knowledge/Resolve_Studio/START_HERE.md. Read only the relevant card:

- SOUND_AND_VOICE.md: performance-first dialogue, ADR, source perspective, layers, mix and stem delivery.
- CAPABILITY_MAP.md: Resolve tool families, local version versus server stub, Fairlight API limits and test route.
- SOURCES.md: what was actually read and what is still untested.

Reusable assets: E:/AI_films/Tools/AudioStudio/session_template.json,
cues_template.csv and voice_template.json. These are planning templates, NOT
installed Fairlight presets or proof of routing. Adapt frame rate, ranges,
track layout and delivery specification to the actual project.

Use audio_qc.py in that directory for read-only per-audio-stream measurements,
optional sample-rate/channel/loudness checks and equal-duration checks. It
requires FFmpeg/ffprobe on PATH and writes only a NEW report; it does not
normalize media. For video-level checks retain the existing media_qc.py.

Important decisions:
- Audio dubbing does not alter mouth motion. Independently generated dialogue
  cannot be waveform-synced to picture with no shared recording.
- Preserve performance and pronunciation across voice conversions; source claims
  of emotional preservation are not per-take acceptance.
- Do not infer complete mixer access from an audio-capabilities response. Probe
  exact operations; route unsupported EQ, buses or automation through observed
  UI or a tested preset. A preset can overwrite the mix.
- Stems share a start, length and sample rate. Separately normalizing stems
  changes balance; nonlinear master processing can prevent summed stems from
  reconstructing the master exactly.
- Compare full-program LUFS only to a matching measurement contract. Report
  dialogue-gated compliance as unmeasured unless a matching meter was used.

Trial plan: E:/AI_films/Experiments/Audio_Lab_v001/PLAN.md. Record local tests
separately from source study; never label an unplayed mix artistically accepted.
