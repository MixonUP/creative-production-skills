# Resolve / Fusion operations

## The local connection

Current tested route (19 Sep 2026): Resolve Free 21.0.3.7, samuelgursky MCP 4.8.13, in-app authenticated loopback bridge. Read Tools/ResolveMCP/README.md for startup. Do not upgrade based only on a newer version number: 21.1 Free changed Python availability. Do not launch another Resolve merely because a sandboxed client says RESOLVE_NOT_RUNNING; our successful countercheck was the same read-only client with access to the live process/loopback.

Use the installed official Scripting/README.txt under C:/ProgramData/Blackmagic Design/DaVinci Resolve/Support/Developer as version-specific API evidence. Vendor docs under E:/Krea_tren_AI/Tools/ResolveMCP/vendor/docs provide relevant kernels and limitations. Inspect the actual tool schema rather than inventing action names.

Tested calls: project_manager/get_current; project_settings/get_setting and project_summary; media_analysis/capabilities; timeline/audio_capabilities and fairlight_boundary_report. Extension capability listing worked, but does not prove each extension can render on Free. The audit helper Tools/ResolveMCP/audit_capabilities.py is read-only and writes dated evidence.

## Editorial assembly

Plan clip placement from source ranges and record-frame positions. Resolve 21.0 lacks general position/trim setters for existing timeline items; reconstruct a new timeline from clipInfos when appropriate instead of claiming a nonexistent move operation. Re-list items and confirm source, track, start and length. Check transition handles and actual rendered transition behavior.

Our timeline frame-rate setter worked; playback-frame-rate setter returned false. The latter was set in the UI and read back. Treat this as the tested build's behavior, not a universal prohibition. If UI access is needed, load the available computer-use skill and observe the current interface.

## Build a reusable effect

Prefer a Fusion node graph with a small set of meaningful controls. For a cast shadow those might be geometry/mask transform, opacity, softness and timed motion; for snow, depth layers, particle size/density and speed. Preserve independent art direction and avoid baking the entire scene into one uncontrollable effect.

First make one composition render correctly on a disposable or authorized timeline. Verify MediaIn/MediaOut connections, alpha premultiplication, frame range and color treatment. Then package as .setting with public controls and reapply it to a second clip of different length. A successful graph import is not enough: confirm visible output and compare parameter changes.

Reference: vendor/docs/authoring/setting-files/README.md and templates; official Developer/Fusion Fuse examples for a custom node. Use a Fuse when existing nodes cannot express the effect efficiently, not as the first response to every look. Reactor is a package manager, not evidence that every downloaded node suits this build. DCTL/OFX/Workflow Integration availability must be checked against edition and plugin requirements.

Do not promise generic access to every third-party plugin parameter through Resolve MCP. When API access is missing, prefer a supported preset, file-based handoff or justified UI step. Keep that limitation visible in the result.
