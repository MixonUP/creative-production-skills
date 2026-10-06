"""Read-only OFX identity, registration and bounded log inspection. No DLL/GPU execution."""
import argparse
import hashlib
import json
import os
import re
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path

TIME = re.compile(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}(?:\.\d+)?) ")
EVENTS = (
    ("evaluation_success", "Feature 18 EvaluateFeature succeeded:"),
    ("create_success", "Feature 18 CreateFeature succeeded"),
    ("core_init", "NGX Core Init succeeded"),
    ("session_init", "Feature 18 D3D12 session initialized"),
    ("fallback", "OFX render returned source fallback:"),
    ("skipped", "OFX runtime skipped"),
    ("error", "ERROR:"),
)


def read_error(error):
    return {"state": "missing" if isinstance(error, FileNotFoundError) else "unavailable",
            "error_type": type(error).__name__, "message": str(error)}


def inspect_files(bundle, expected):
    results = []
    root = Path(bundle).resolve()
    for relative, expected_hash in expected["files"].items():
        path = (root / relative).resolve()
        if not path.is_relative_to(root):
            raise ValueError("Manifest path escapes the selected bundle")
        item = {"relative_path": relative, "expected_sha256": expected_hash}
        try:
            digest = hashlib.sha256()
            with path.open("rb") as stream:
                for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                    digest.update(chunk)
            item.update(state="read", sha256=digest.hexdigest(),
                        matches_pinned_release=digest.hexdigest().lower() == expected_hash.lower())
        except OSError as error:
            item.update(read_error(error))
        results.append(item)
    return results


def inspect_cache(path, plugin_id, bundle):
    try:
        root = ET.parse(path).getroot()
    except (OSError, ET.ParseError) as error:
        return read_error(error)
    plugins = [p for p in root.iter("plugin") if p.get("name") == plugin_id]
    selected = os.path.normcase(os.path.abspath(bundle))
    binaries = [dict(b.attrib) for b in root.iter("binary")
                if os.path.normcase(os.path.abspath(b.get("bundle_path", ""))) == selected]
    return {"state": "read", "plugin_registered": bool(plugins),
            "plugin_entries": [dict(p.attrib) for p in plugins], "binaries": binaries,
            "limitation": "Cache registration is not active Feature 18 inference."}


def parse_events(text, since=None):
    found = []
    for line in text.splitlines():
        match = TIME.match(line)
        if not match:
            continue
        try:
            stamp = datetime.fromisoformat(match.group(1))
        except ValueError:
            continue
        if since is not None and stamp < since:
            continue
        kind = next((key for key, needle in EVENTS if needle in line[match.end():]), None)
        if kind:
            found.append({"time": stamp.isoformat(sep=" "), "kind": kind, "line": line[:1800]})
    success = sum(e["kind"] == "evaluation_success" for e in found)
    errors = sum(e["kind"] in {"error", "fallback", "skipped"} for e in found)
    if since is None:
        status = "historical_only_no_run_window"
    elif success and errors:
        status = "evaluation_and_failure_observed"
    elif success:
        status = "evaluation_observed"
    elif errors:
        status = "failure_without_evaluation_evidence"
    elif found:
        status = "initialization_only"
    else:
        status = "no_matching_events"
    return {"window_status": status, "evaluation_success_lines": success,
            "failure_or_skip_lines": errors, "events": found[-30:],
            "event_count_in_tail": len(found), "clip_identity_verified": False,
            "all_frames_verified": False, "visual_quality": "not_assessed"}


def inspect_log(path, since=None):
    try:
        with Path(path).open("rb") as stream:
            size = stream.seek(0, 2)
            start = max(0, size - 2 * 1024 * 1024)
            stream.seek(start)
            if start:
                stream.readline()  # discard a potentially partial line
            content = stream.read().decode("utf-8", errors="replace")
        return {"state": "read", "bytes": size, "tail_only": bool(start),
                "since_local_time": since.isoformat(sep=" ") if since else None,
                **parse_events(content, since)}
    except OSError as error:
        return {**read_error(error), "window_status": "unknown", "visual_quality": "not_assessed"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path, default=Path(os.environ.get("CommonProgramFiles", "C:/Program Files/Common Files")) / "OFX/Plugins/ResolveDlss5.ofx.bundle")
    parser.add_argument("--cache", type=Path, default=Path(os.environ.get("APPDATA", "")) / "Blackmagic Design/DaVinci Resolve/Support/OFXPluginCacheV2.xml")
    parser.add_argument("--log", type=Path, default=Path(os.environ.get("LOCALAPPDATA", "")) / "ResolveDlss5/ResolveDlss5.log")
    parser.add_argument("--manifest", type=Path, default=Path(__file__).resolve().parents[1] / "assets/resolve-0.3.1.json")
    parser.add_argument("--since", help="Local log time YYYY-MM-DD HH:MM:SS; no timezone offset")
    parser.add_argument("--report", type=Path, help="New JSON file; existing files are never overwritten")
    args = parser.parse_args()
    if args.report and args.report.exists():
        parser.error("Report already exists; choose a new evidence filename")
    try:
        since = datetime.fromisoformat(args.since) if args.since else None
    except ValueError:
        parser.error("Invalid --since; use YYYY-MM-DD HH:MM:SS")
    if since and since.tzinfo is not None:
        parser.error("DLSS log timestamps are local and unzoned; supply local time without offset")
    expected = json.loads(args.manifest.read_text(encoding="utf-8-sig"))
    files = inspect_files(args.bundle, expected)
    result = {"observed_at": datetime.now().astimezone().isoformat(),
              "expected_release": expected["version"], "bundle": str(args.bundle),
              "files": files, "pinned_files_match": bool(files) and all(f.get("matches_pinned_release") is True for f in files),
              "registration": inspect_cache(args.cache, expected["plugin_id"], args.bundle),
              "runtime_log": inspect_log(args.log, since),
              "side_effects": "none except explicitly requested new report",
              "inference_started_by_probe": False, "creative_acceptance": "not_assessed"}
    serialized = json.dumps(result, ensure_ascii=False, indent=2)
    if args.report:
        with args.report.open("x", encoding="utf-8") as stream:
            stream.write(serialized + "\n")
    print(serialized)
    return 0 if result["pinned_files_match"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
