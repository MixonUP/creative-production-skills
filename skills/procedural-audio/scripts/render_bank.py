"""Deterministic CPU sound-bank renderer; an original local implementation."""
import argparse
import hashlib
import html
import json
import math
import re
import sys
import wave
from pathlib import Path

import numpy as np

VERSION = "1.0.0"


def finite(value, name, low=None, high=None):
    if isinstance(value, bool):
        raise ValueError(f"{name}: boolean is not a number")
    value = float(value)
    if not math.isfinite(value) or (low is not None and value < low) or (high is not None and value > high):
        raise ValueError(f"{name}: out of range")
    return value


def integer(value, name, low=None, high=None):
    number = finite(value, name, low, high)
    if int(number) != number:
        raise ValueError(f"{name}: expected integer")
    return int(number)


def voice(event, sr, seed):
    duration = finite(event["duration"], "event duration", 0.001, 120)
    n = round(duration * sr)
    t = np.arange(n, dtype=np.float64) / sr
    actual = n / sr
    amp = finite(event.get("amplitude", 0.2), "amplitude", 0, 4)
    attack = finite(event.get("attack", 0.003), "attack", 0, duration)
    release = finite(event.get("release", 0.02), "release", 0, duration)
    decay = finite(event.get("decay", duration), "decay", 0.0001, 1000)
    envelope = np.exp(-t / decay)
    if attack:
        envelope *= np.minimum(t / attack, 1.0)
    if release:
        envelope *= np.minimum((n - 1 - np.arange(n)) / (sr * release), 1.0)
    kind = event["type"]
    if kind == "tone":
        f0 = finite(event["f0"], "f0", 1, sr / 2)
        f1 = finite(event.get("f1", f0), "f1", 1, sr / 2)
        phase = 2 * np.pi * (f0 * t + (f1 - f0) * t * t / (2 * actual))
        signal = np.zeros(n, dtype=np.float64)
        active = 0
        partials = event.get("partials", [[1, 1, 1000]])
        if not isinstance(partials, list) or not 1 <= len(partials) <= 64:
            raise ValueError("partials: expected 1..64 triples")
        for partial in partials:
            ratio, gain, damping = partial
            ratio = finite(ratio, "partial ratio", 0.001, 1000)
            gain = finite(gain, "partial gain", 0, 4)
            damping = finite(damping, "partial damping", 0.0001, 1000)
            if max(f0, f1) * ratio >= sr / 2:
                continue
            signal += gain * np.sin(phase * ratio) * np.exp(-t / damping)
            active += 1
        if not active:
            raise ValueError("No tone partial below Nyquist")
    elif kind == "noise":
        signal = np.random.default_rng(seed).uniform(-1, 1, n)
        if "lowpass_hz" in event:
            cutoff = finite(event["lowpass_hz"], "lowpass_hz", 1, sr / 2)
            alpha = 1 - math.exp(-2 * math.pi * cutoff / sr)
            state = 0.0
            for index in range(n):
                state += alpha * (signal[index] - state)
                signal[index] = state
    else:
        raise ValueError(f"Unknown voice type: {kind}")
    return amp * envelope * signal


def synthesize(config):
    if config.get("schema_version") != 1:
        raise ValueError("Expected schema_version 1")
    sr = integer(config.get("sample_rate", 48000), "sample_rate", 8000, 96000)
    seed = integer(config.get("seed", 0), "seed", 0, 2**32 - 1)
    cues = config.get("cues", [])
    if not isinstance(cues, list) or not 1 <= len(cues) <= 128:
        raise ValueError("Expected 1..128 cues")
    arrays = {}
    for cue in cues:
        cue_id = cue["id"]
        if not isinstance(cue_id, str) or not re.fullmatch(r"[a-z][a-z0-9_-]{0,63}", cue_id) or cue_id in arrays:
            raise ValueError("Unsafe or duplicate cue ID")
        if not isinstance(cue.get("loop", False), bool):
            raise ValueError("loop must be a boolean")
        n = round(finite(cue["duration"], "cue duration", 0.01, 120) * sr)
        out = np.zeros(n, dtype=np.float64)
        if "mix" in cue:
            if "events" in cue or not cue["mix"]:
                raise ValueError("A mix needs source IDs and cannot also contain events")
            for source_id in cue["mix"]:
                if source_id not in arrays or len(arrays[source_id]) != n:
                    raise ValueError("Mix sources must precede mix and share its duration")
                out += arrays[source_id]
        else:
            events = cue.get("events", [])
            if not isinstance(events, list) or not 1 <= len(events) <= 2048:
                raise ValueError("Expected 1..2048 events per cue")
            for index, event in enumerate(events):
                start = round(finite(event.get("start", 0), "start", 0, 120) * sr)
                child_seed = int.from_bytes(hashlib.sha256(f"{seed}:{cue_id}:{index}".encode()).digest()[:8], "little")
                signal = voice(event, sr, child_seed)
                if start >= n or len(signal) > n:
                    raise ValueError("Event starts outside cue or is longer than cue")
                if cue.get("loop", False):
                    np.add.at(out, (start + np.arange(len(signal))) % n, signal)
                elif start + len(signal) > n:
                    raise ValueError("One-shot tail does not fit; extend cue explicitly")
                else:
                    out[start:start + len(signal)] += signal
        if not np.isfinite(out).all():
            raise ValueError("Non-finite rendered samples")
        arrays[cue_id] = out
    peak = max(float(np.max(np.abs(v))) for v in arrays.values())
    gain = min(1.0, 0.8 / peak) if peak else 1.0
    return sr, {key: value * gain for key, value in arrays.items()}, gain


def waveform(values):
    chunks = np.array_split(values, min(180, len(values)))
    peaks = [float(np.max(np.abs(part))) for part in chunks]
    width = len(peaks)
    bars = ''.join(f'<path d="M{i} {32-p*30:.2f}V{32+p*30:.2f}"/>' for i, p in enumerate(peaks))
    return f'<svg viewBox="0 0 {width} 64" aria-label="Measured waveform" role="img">{bars}</svg>'


def audition(cues, arrays):
    cards = []
    for cue in cues:
        cue_id = cue["id"]
        loop = ' loop' if cue.get("loop") else ''
        label = html.escape(str(cue.get("label", cue_id)))
        detail = html.escape(str(cue.get("reference_property", "")))
        event = html.escape(str(cue.get("event", "")))
        cards.append(f'<article><small>{cue_id} · {"LOOP CANDIDATE" if loop else "ONE SHOT"}</small><h2>{label}</h2><p>{detail}</p>{waveform(arrays[cue_id])}<audio controls preload="metadata"{loop} src="{cue_id}.wav"></audio><p class="event">{event}</p><a href="{cue_id}.wav" download>WAV</a></article>')
    return '''<!doctype html><html lang="ru"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Процедурный звук — прослушивание</title>
<style>body{background:#121719;color:#e7eeed;font:17px system-ui;margin:0;padding:32px;max-width:1180px;margin:auto}h1{font-size:36px}header{max-width:900px;margin-bottom:30px}small,.event{color:#a8b9b7}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:18px}article{background:#1c2528;border:1px solid #34494c;border-radius:12px;padding:20px}h2{font-size:22px}p{line-height:1.55}svg{width:100%;height:70px;stroke:#81d9bf;stroke-width:.7}audio{width:100%}a{color:#81d9bf}footer{margin-top:28px;color:#a8b9b7}</style>
<header><small>ЛОКАЛЬНЫЙ CPU-СИНТЕЗ · РЕДАКТИРУЕМЫЕ РЕЦЕПТЫ</small><h1>Звук, который можно менять</h1><p>Новые технические примеры: металл, механизмы, сигналы и короткий музыкальный эскиз. Сначала тихо прослушайте отдельные варианты, затем сравните их в сцене. Один плеер за раз.</p><p>Статус: файлы синтезированы. Слуховая оценка, выбор дублей и интеграция ещё не выполнены. Графики показывают амплитуду, а не качество.</p><a href="config.json">Рецепты</a> · <a href="manifest.json">Карта звуков</a> · <a href="report.json">Технический отчёт</a></header><main>''' + ''.join(cards) + '''</main><footer>Начните с умеренной громкости. LOOP CANDIDATE повторяется: оцените шов после нескольких циклов. Файлы 48 kHz только если такой sample_rate указан в config; фактический формат — в отчёте.</footer><script>document.querySelectorAll('audio').forEach(a=>{a.volume=.55;a.addEventListener('play',()=>document.querySelectorAll('audio').forEach(b=>{if(b!==a)b.pause()}))})</script></html>'''


def render(config_path, output):
    config_path, output = Path(config_path), Path(output)
    if output.exists():
        raise FileExistsError(f"Output exists; choose a new revision: {output}")
    raw = config_path.read_bytes()
    config = json.loads(raw)
    sr, arrays, gain = synthesize(config)
    output.mkdir(parents=True, exist_ok=False)
    (output / 'config.json').write_bytes(raw)
    records = []
    for cue in config['cues']:
        cue_id = cue['id']
        pcm = np.rint(arrays[cue_id] * 32767).astype('<i2')
        path = output / f'{cue_id}.wav'
        with wave.open(str(path), 'wb') as stream:
            stream.setnchannels(1)
            stream.setsampwidth(2)
            stream.setframerate(sr)
            stream.writeframes(pcm.tobytes())
        decoded = pcm.astype(np.float64) / 32768
        records.append({'id': cue_id, 'file': path.name, 'sample_rate': sr, 'channels': 1, 'bits': 16,
                        'samples': len(pcm), 'duration': len(pcm)/sr, 'sample_peak': float(np.max(np.abs(decoded))),
                        'rms': float(np.sqrt(np.mean(decoded**2))), 'dc_mean': float(np.mean(decoded)),
                        'boundary_step': float(abs(decoded[-1]-decoded[0])),
                        'clipped_samples': int(np.count_nonzero((pcm == -32768) | (pcm == 32767))),
                        'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
    report = {'renderer_version': VERSION, 'numpy_version': np.__version__, 'python_version': sys.version.split()[0],
              'renderer_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'config_sha256': hashlib.sha256(raw).hexdigest(), 'common_gain': gain, 'files': records,
              'listening': 'not-run', 'loop_audition': 'not-run', 'integration': 'not-run',
              'limits': 'Sample peak/RMS/DC only; not true peak, LUFS, aesthetic or perceptual loop validation.'}
    (output / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    manifest = {'schema_version': 1, 'cues': [{**c, 'file': c['id']+'.wav', 'state': 'synthesized-unreviewed'} for c in config['cues']]}
    (output / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    (output / 'audition.html').write_text(audition(config['cues'], arrays), encoding='utf-8')
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', required=True, type=Path)
    parser.add_argument('--out', required=True, type=Path)
    args = parser.parse_args()
    report = render(args.config, args.out)
    print(json.dumps({'output': str(args.out.resolve()), 'files': len(report['files']), 'common_gain': report['common_gain'], 'listening': report['listening']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
