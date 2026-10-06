"""Read-only speech-manifest audit. No models, network, conversion or training.

Dependencies: numpy and soundfile (already in the isolated IndexTTS environment).
Exit 0: technical checks clear; 1: review/incomplete split; 2: invalid input/leakage.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys

import numpy as np
import soundfile as sf


def sha256_file(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def group_key(value):
    return str(value or "").strip().replace("\\", "/").casefold()


def normalized_text(value):
    return " ".join(re.findall(r"\w+", str(value).casefold(), flags=re.UNICODE))


def audit(manifests, split_map=None, expected_rate=24000, min_duration=4.0, max_duration=16.0):
    errors, warnings, records, inputs = [], [], [], []
    seen_ids = set()
    split_map = split_map or {}
    for manifest in map(Path, manifests):
        manifest = manifest.resolve()
        try:
            inputs.append({"path": str(manifest), "sha256": sha256_file(manifest)})
            lines = manifest.read_text(encoding="utf-8-sig").splitlines()
        except (OSError, UnicodeError) as exc:
            errors.append({"code": "manifest_unreadable", "manifest": str(manifest), "detail": str(exc)})
            continue
        for line_no, line in enumerate(lines, 1):
            if not line.strip():
                continue
            location = {"manifest": str(manifest), "line": line_no}
            try:
                row = json.loads(line)
                if not isinstance(row, dict):
                    raise ValueError("row must be an object")
            except (ValueError, TypeError) as exc:
                errors.append({"code": "invalid_json_row", **location, "detail": str(exc)})
                continue
            record = {**location, "id": str(row.get("id", "")).strip()}
            records.append(record)
            rid = record["id"]

            def issue(target, code, **detail):
                target.append({"code": code, **location, "id": rid, **detail})

            if not rid:
                issue(errors, "missing_id")
            elif rid in seen_ids:
                issue(errors, "duplicate_id")
            seen_ids.add(rid)
            row_split = str(row.get("split") or "").lower().strip()
            map_split = str(split_map.get(rid) or "").lower().strip()
            if row_split and map_split and row_split != map_split:
                issue(errors, "conflicting_split", row_split=row_split, map_split=map_split)
            record["split"] = map_split or row_split or "unassigned"
            if record["split"] not in {"train", "val", "test", "unassigned"}:
                issue(errors, "invalid_split", value=record["split"])
            for field in ("text", "source_media", "speaker", "language"):
                if not isinstance(row.get(field), str) or not row[field].strip():
                    issue(errors, "missing_or_invalid_field", field=field)
            record["text_key"] = normalized_text(row.get("text", ""))
            record["speaker"] = str(row.get("speaker", ""))
            record["language"] = str(row.get("language", ""))
            record["source_key"] = group_key(row.get("source_media"))
            record["session_key"] = group_key(row.get("session_id"))
            if not isinstance(row.get("audio"), str) or not row["audio"].strip():
                issue(errors, "missing_audio")
                continue
            audio = Path(row["audio"])
            if not audio.is_absolute():
                audio = manifest.parent / audio
            audio = audio.resolve()
            record["audio"] = str(audio)
            try:
                info = sf.info(audio)
                if not info.frames or info.samplerate <= 0 or info.duration > 300:
                    raise ValueError("empty audio or duration exceeds 300-second audit limit")
                waveform, rate = sf.read(audio, dtype="float32", always_2d=True)
                if not np.isfinite(waveform).all():
                    raise ValueError("non-finite samples")
                record.update({"file_sha256": sha256_file(audio), "sample_rate": rate,
                               "channels": int(waveform.shape[1]), "duration_s": len(waveform) / rate})
                pcm = hashlib.sha256(f"{rate}:{waveform.shape}".encode("ascii"))
                pcm.update(waveform.astype("<f4", copy=False).tobytes())
                record["pcm_sha256"] = pcm.hexdigest()
                peak = float(np.max(np.abs(waveform)))
                record["peak_dbfs"] = float(20 * np.log10(peak)) if peak else None
                record["clip_ratio"] = float(np.mean(np.abs(waveform) >= 0.999))
                record["dc_offset_abs"] = float(np.max(np.abs(np.mean(waveform, axis=0, dtype=np.float64))))
                frame = max(1, round(rate * 0.02))
                powers = np.mean(waveform.astype(np.float64) ** 2, axis=1)
                rms = np.sqrt(np.array([np.mean(powers[i:i + frame]) for i in range(0, len(powers), frame)]))
                record["quiet_frame_ratio_below_minus40_dbfs"] = float(np.mean(rms < 0.01))
                if peak == 0:
                    issue(errors, "silent_audio")
                if rate != expected_rate:
                    issue(warnings, "sample_rate", actual=rate, expected=expected_rate)
                if waveform.shape[1] != 1:
                    issue(warnings, "not_mono")
                if not min_duration <= record["duration_s"] <= max_duration:
                    issue(warnings, "duration_outside_profile", actual=record["duration_s"])
                if record["clip_ratio"] > 0.001:
                    issue(warnings, "possible_clipping", ratio=record["clip_ratio"])
                if record["dc_offset_abs"] > 0.01:
                    issue(warnings, "dc_offset_review", value=record["dc_offset_abs"])
                if peak and record["peak_dbfs"] < -35:
                    issue(warnings, "very_quiet_peak")
                if record["quiet_frame_ratio_below_minus40_dbfs"] > 0.5:
                    issue(warnings, "many_quiet_frames_review")
                declared = float(row.get("duration_s", 0))
                if not np.isfinite(declared) or declared <= 0:
                    issue(errors, "invalid_declared_duration")
                elif abs(declared - record["duration_s"]) > 0.05:
                    issue(warnings, "declared_duration_mismatch", declared=declared, actual=record["duration_s"])
            except (OSError, RuntimeError, ValueError, TypeError) as exc:
                issue(errors, "audio_or_metadata_invalid", detail=str(exc))

    if not records:
        errors.append({"code": "empty_dataset"})
    for field in ("source_key", "session_key", "file_sha256", "pcm_sha256", "text_key"):
        grouped = defaultdict(list)
        for record in records:
            if record.get(field):
                grouped[record[field]].append(record)
        for group in grouped.values():
            splits = {r["split"] for r in group} - {"unassigned"}
            if len(splits) > 1:
                destination = warnings if field == "text_key" else errors
                destination.append({"code": "cross_split_" + field, "ids": [r["id"] for r in group], "splits": sorted(splits)})
            elif len(group) > 1 and field in {"file_sha256", "pcm_sha256"}:
                warnings.append({"code": "duplicate_" + field, "ids": [r["id"] for r in group]})
    speakers = sorted({r.get("speaker", "") for r in records} - {""})
    if len(speakers) > 1:
        warnings.append({"code": "multiple_speakers_review", "speakers": speakers})
    split_counts = Counter(r["split"] for r in records)
    if split_counts.get("unassigned"):
        warnings.append({"code": "split_not_frozen", "count": split_counts["unassigned"]})
    for needed in ("train", "val"):
        if not split_counts.get(needed):
            warnings.append({"code": "missing_split", "split": needed})
    if not split_counts.get("test"):
        warnings.append({"code": "no_independent_test_in_audit", "detail": "Test may be reserved elsewhere; no final-test claim is possible here."})
    status = "FAIL" if errors else "NEEDS_SPLIT" if split_counts.get("unassigned") else "REVIEW" if warnings else "PASS"
    return {
        "schema_version": 1, "recorded_at": datetime.now(timezone.utc).isoformat(),
        "status": status, "meaning": "Technical screening only; no ASR, speaker verification, LUFS, training or listening.",
        "settings": {"expected_rate": expected_rate, "min_duration": min_duration, "max_duration": max_duration},
        "inputs": inputs, "records": records, "errors": errors, "warnings": warnings,
        "summary": {"clips": len(records), "minutes": sum(r.get("duration_s", 0) for r in records) / 60, "splits": dict(split_counts), "speakers": speakers},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", action="append", required=True, type=Path)
    parser.add_argument("--split-map", type=Path, help="JSON object mapping unique clip IDs to train/val/test; does not alter manifest")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--expected-rate", type=int, default=24000)
    parser.add_argument("--min-duration", type=float, default=4.0)
    parser.add_argument("--max-duration", type=float, default=16.0)
    args = parser.parse_args()
    if args.expected_rate <= 0 or not 0 < args.min_duration <= args.max_duration <= 300:
        parser.error("Invalid audit profile")
    try:
        split_map = json.loads(args.split_map.read_text(encoding="utf-8-sig")) if args.split_map else {}
        if not isinstance(split_map, dict):
            raise ValueError("split-map must be an object")
        report = audit(args.manifest, split_map, args.expected_rate, args.min_duration, args.max_duration)
        if args.split_map:
            report["split_map"] = {"path": str(args.split_map.resolve()), "sha256": sha256_file(args.split_map)}
        protected = {p.resolve() for p in args.manifest}
        if args.split_map:
            protected.add(args.split_map.resolve())
        protected.update(Path(r["audio"]).resolve() for r in report["records"] if "audio" in r)
        if args.output.resolve() in protected:
            raise ValueError("Output must not overwrite source audio, manifests or split map")
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    except (OSError, ValueError, TypeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    print(json.dumps({"status": report["status"], **report["summary"], "report": str(args.output.resolve())}, ensure_ascii=False))
    return 2 if report["errors"] else 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
