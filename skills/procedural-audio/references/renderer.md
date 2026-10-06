# Bundled renderer

Requires Python 3 and NumPy. No other package, network, GPU or external sample bank.
Example from the skill directory (choose a new output revision):

```powershell
python scripts/render_bank.py --config assets/mech-study.json --out E:/Krea_tren_AI/output/audio/mech-study-v001
```

The output folder must not exist. The script validates and renders all cues before
creating it; it refuses overwrite. Output is mono PCM16 WAV for compact audition and
runtime prototypes, not a multichannel or high-resolution mastering engine.

## Config schema 1

- sample_rate: integer 8000..96000; seed: integer; cues: nonempty list.
- cue id: safe filename ID; label; role; event; reference_property; duration in seconds;
  loop: boolean; events: list, or mix: list of earlier cue IDs.
- event start and duration in seconds, amplitude >= 0; type tone/noise.
- tone: f0/f1 in Hz (linear sweep), partials [[frequency ratio, gain, decay_seconds], ...].
- noise: optional lowpass_hz; seeded independently per cue/event.
- attack/release in seconds; decay in seconds (positive). A one-shot tail must fit.
- loop cues wrap events/tails across the boundary. Musical loops should use whole bars
  and intentional note endpoints. A nonzero start sample is not itself a bad loop.
- mix cues combine earlier cues of equal duration; use it to audition aligned stems.

Tone phase integrates the frequency ramp; it is not sin(2*pi*f(t)*t).
Partials at/above Nyquist are omitted; rejection occurs if no valid partial remains.
This is additive/modal synthesis with a simple noise filter, not a full physical
simulation, pitch-shifting service, dispersive-wave solver or automatic composition model.
High-frequency quality and filter character still require listening.

One common attenuation is applied to the entire bank only if needed to keep sample
peaks at/below 0.8. Relative balances and sum-of-stems are preserved before quantization.
This is safety headroom, not target loudness mastering. Per-stem PCM rounding means
the exported mix can differ from a sum of quantized stems by a few least significant bits.

Output: config.json, WAVs, manifest.json, report.json, audition.html. The report includes
sample count, sample peak, RMS, mean/DC, first-to-last boundary step and a file hash.
The boundary step is a diagnostic, not an automatic seamless-loop verdict.
Playback and artistic acceptance are pending until someone actually reviews the audio.

The renderer deliberately has no inference, uploads, live engine, Resolve or payment
actions. A film delivery can resample/convert through the approved postproduction
route after the cue is chosen; recheck the resulting file.

