"""Prepare, never execute, the local Proteus 2x SDR baseline. Stdlib only."""
import argparse
import hashlib
import json
import re
import subprocess
from datetime import datetime
from fractions import Fraction
from pathlib import Path

TOPAZ = Path('C:/Program Files/Topaz Labs LLC/Topaz Video')
MODELS = Path('C:/ProgramData/Topaz Labs LLC/Topaz Video/models')
PROBE = Path('C:/FFmpeg_exe/ffprobe.exe')
FILTER = ('tvai_up=model=prob-4:scale=2:device=0:vram=0.35:download=0:'
          'details=0.1:blur=0:noise=0:compression=0.1:blend=0.2')


def read_command(argv):
    result = subprocess.run([str(x) for x in argv], shell=False, capture_output=True,
                            text=True, encoding='utf-8', errors='replace', timeout=60)
    if result.returncode:
        raise ValueError(f'Read-only probe failed: {Path(argv[0]).name}, exit {result.returncode}')
    return result.stdout, result.stderr


def file_identity(path):
    st = path.stat()
    return {'path': str(path), 'bytes': st.st_size, 'mtime_ns': st.st_mtime_ns}


def validate_media(metadata, sdr_confirmed, assume_square=False):
    streams = metadata.get('streams', [])
    videos = [s for s in streams if s.get('codec_type') == 'video']
    if len(videos) != 1 or videos[0].get('disposition', {}).get('attached_pic'):
        raise ValueError('Baseline requires exactly one video stream, not a cover image')
    v = videos[0]
    if v.get('codec_name') != 'h264' or v.get('pix_fmt') not in ('yuv420p', 'nv12'):
        raise ValueError('This baseline is limited to H.264 8-bit 4:2:0; prepare another recipe')
    if v.get('field_order') != 'progressive':
        raise ValueError('Progressive scan must be established before this baseline')
    sar = v.get('sample_aspect_ratio')
    if sar != '1:1' and not (sar in (None, 'N/A', '0:1') and assume_square):
        raise ValueError('Square pixels required; missing SAR needs an explicit interpretation')
    if not sdr_confirmed:
        raise ValueError('Establish SDR provenance; --sdr-confirmed does not perform a colour conversion')
    if (v.get('color_transfer') in ('smpte2084', 'arib-std-b67')
            or '2020' in v.get('color_primaries', '')
            or '2020' in v.get('color_space', '')):
        raise ValueError('HDR/wide-gamut input needs a separate colour-managed recipe')
    try:
        fps = Fraction(v['avg_frame_rate'])
        nominal = Fraction(v['r_frame_rate'])
    except (KeyError, ValueError, ZeroDivisionError):
        raise ValueError('Valid rational source FPS is required') from None
    if fps <= 0 or fps != nominal:
        raise ValueError('Unknown/unequal rates: inspect VFR/cadence before preparing this baseline')
    if min(int(v.get('width', 0)), int(v.get('height', 0))) <= 0:
        raise ValueError('Missing dimensions')
    return v


def make_plan(source, output, metadata, ffmpeg, model_dir, data_dir, sdr_confirmed, assume_square=False):
    source = Path(source).resolve(strict=True)
    output = Path(output).resolve()
    if not source.is_file():
        raise ValueError('Source must be a local file')
    if output == source or output.exists():
        raise ValueError('Output must be new; source and existing files are preserved')
    if output.suffix.lower() != '.mov' or not output.parent.is_dir():
        raise ValueError('Use a .mov in an existing output directory')
    ffmpeg = Path(ffmpeg).resolve(strict=True)
    model_dir = Path(model_dir).resolve(strict=True)
    data_dir = Path(data_dir).resolve(strict=True)
    if not ffmpeg.is_file() or not model_dir.is_dir() or not data_dir.is_dir():
        raise ValueError('Invalid binary/model directories')
    definition = model_dir / 'prob-4.json'
    if not definition.is_file():
        raise ValueError('Missing prob-4 model definition')
    v = validate_media(metadata, sdr_confirmed, assume_square)
    vf = FILTER if v.get('sample_aspect_ratio') == '1:1' else FILTER + ',setsar=1'
    argv = [str(ffmpeg), '-hide_banner', '-nostdin', '-n', '-c:v', 'h264_cuvid',
            '-i', str(source), '-map', '0:v:0', '-map', '0:a?', '-vf', vf,
            '-c:v', 'prores_ks', '-profile:v', '3', '-pix_fmt', 'yuv422p10le',
            '-fps_mode', 'passthrough', '-c:a', 'pcm_s24le', '-ar', '48000',
            '-map_metadata', '0', str(output)]
    warnings = ['Not rendered; model weights and current activation are not verified.',
                'Matching average/nominal FPS does not establish constant frame timestamps.',
                'GPU availability and output nonexistence must be rechecked before execution.',
                'Colour appearance, metadata/timecode and audio sync require output review.']
    if any(s.get('codec_type') not in ('video', 'audio') for s in metadata.get('streams', [])):
        warnings.append('Non-audio/video streams are not mapped; plan their separate preservation.')
    if v.get('sample_aspect_ratio') != '1:1':
        warnings.append('Input SAR is missing; explicitly interpreted as square, output setsar=1.')
    if any(v.get(k) in (None, 'unknown', 'unspecified') for k in
           ('color_range', 'color_space', 'color_transfer', 'color_primaries')):
        warnings.append('Some colour tags are absent; SDR was asserted by provenance, not inferred.')
    count = v.get('nb_frames')
    return {
        'schema_version': 1, 'at': datetime.now().astimezone().isoformat(),
        'status': 'planned_not_rendered', 'recipe': 'historical-seedance-proteus-2x-v1',
        'command_reconstruction': 'Based on recorded settings and current help; not original argv.',
        'source': file_identity(source), 'output': str(output),
        'argv': argv, 'shell': False,
        'environment_overrides': {'TVAI_MODEL_DIR': str(model_dir),
                                  'TVAI_MODEL_DATA_DIR': str(data_dir)},
        'model_definition_sha256': hashlib.sha256(definition.read_bytes()).hexdigest(),
        'expected': {'width': int(v['width']) * 2, 'height': int(v['height']) * 2,
                     'fps': str(Fraction(v['avg_frame_rate'])),
                     'frames_from_metadata': int(count) if str(count).isdigit() else None,
                     'audio_streams': sum(s.get('codec_type') == 'audio'
                                         for s in metadata.get('streams', [])),
                     'audio_treatment': 'PCM 24-bit 48 kHz; content preserved, re-encoded'},
        'source_probe': metadata, 'warnings': warnings,
        'pixel_aspect_basis': 'tag' if v.get('sample_aspect_ratio') == '1:1' else 'explicit_interpretation',
    }


def check_capabilities(ffmpeg):
    observations = {}
    for key, args in {'upscale': ['-h', 'filter=tvai_up'],
                      'encoders': ['-encoders'], 'decoders': ['-decoders'],
                      'full_help': ['-h', 'full']}.items():
        out, err = read_command([ffmpeg, '-hide_banner', *args])
        observations[key] = out + err
    required = {'upscale': ('tvai_up', 'download', 'vram', 'blend'),
                'encoders': ('prores_ks', 'pcm_s24le'),
                'decoders': ('h264_cuvid',), 'full_help': ('fps_mode',)}
    for key, values in required.items():
        for value in values:
            if not re.search(r'(?<![A-Za-z0-9_])' + re.escape(value) + r'(?![A-Za-z0-9_])', observations[key]):
                raise ValueError(f'Installed FFmpeg does not advertise {value}')
    return {k: hashlib.sha256(v.encode()).hexdigest() for k, v in observations.items()}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('source', type=Path); p.add_argument('output', type=Path)
    p.add_argument('--topaz-dir', type=Path, default=TOPAZ)
    p.add_argument('--ffprobe', type=Path, default=PROBE)
    p.add_argument('--model-dir', type=Path, default=MODELS)
    p.add_argument('--data-dir', type=Path, default=MODELS)
    p.add_argument('--sdr-confirmed', action='store_true')
    p.add_argument('--assume-square-pixels', action='store_true',
                   help='Interpret only MISSING SAR as 1:1; never override a known non-square SAR')
    p.add_argument('--save', type=Path, help='Create a new plan JSON; never overwrite')
    a = p.parse_args()
    source = a.source.resolve(strict=True)
    if not source.is_file():
        p.error('Expected a local source file')
    if a.save and (a.save.resolve() in (source, a.output.resolve()) or a.save.exists()):
        p.error('Plan must be a new file separate from source and media output')
    out, _ = read_command([a.ffprobe, '-v', 'error', '-show_streams', '-show_format',
                           '-of', 'json', str(source)])
    plan = make_plan(source, a.output, json.loads(out), a.topaz_dir / 'ffmpeg.exe',
                     a.model_dir, a.data_dir, a.sdr_confirmed, a.assume_square_pixels)
    plan['capability_help_sha256'] = check_capabilities(a.topaz_dir / 'ffmpeg.exe')
    serialized = json.dumps(plan, ensure_ascii=False, indent=2)
    if a.save:
        with a.save.open('x', encoding='utf-8') as handle:
            handle.write(serialized + '\n')
    print(serialized)


if __name__ == '__main__':
    main()
