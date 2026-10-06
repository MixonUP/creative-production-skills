# Resolve: installed OFX contract

Scope: SAOG0721 v0.3.1, commit `a659e5c674388ea8026f4cf8df9f206826d12452`, inspected 2026-09-30. Read [sources](sources.md) before applying these details to another version.

## Host and editable integration

The installed effect is `DLSS Neural Video Experimental`, group `DLSS Experimental`, OFX ID `com.saog.resolve.dlss5`. Full bundle path and evidence are in the project card. The local host stays **21.0.3.7 Free**. Never update it for this workflow.

Prefer existing Resolve MCP actions for state, comp inspection, additions and exports. Consult the actual callable schemas. A bridge connection failure is a connection issue, not proof that this Free version cannot load OFX. The project's existing Free bridge is started through Workspace → Scripts → resolve_bridge. Do not assume Studio-only external scripting works. Avoid creating a second integration or overwriting its configuration.

Before editing, establish project, timeline and clip identity; save a copy/duplicate for trials. Query the live Fusion tool registry/input list before setting parameters. The identifiers below are **source OFX IDs**; Fusion wrappers may expose different input IDs. Use UI inspection when a genuine API gap remains. Do not issue guessed Lua or silently operate on whichever comp happens to be selected.

For a simple trial, connect source → DLSS → output in a new comp/timeline revision. For compositing, prepare the matte and colour treatment, combine foreground/background, then trial a single DLSS pass on the composite. Compare with a branch in which the completed composite bypasses NR. Inspect matte fringes because source alpha restoration does not guarantee correct premultiplied RGB at edges. Clip-local instances help prevent one shot's history from entering the next.

## Parameters from the tagged source

Defaults are developer defaults, **not an accepted look**. Numeric ranges are UI limits, not proof that every runtime responds linearly throughout the range.

| UI control / source ID | Default; valid values | Operational use |
|---|---|---|
| Enable / `nrEnabled` | true | false is the clean identity/bypass reference |
| NR Preset / `nrPreset` | index 0; 0–2 → runtime presets 1–3 | compare separately; no documented best preset |
| UI Correction / `nrUiCorrection` | false | diagnostic flag; not a face restoration control |
| Style / `nrStyle` | 0; 0, 1, 2 | UI labels are Style 0/1/2; “natural/cinematic” are creator interpretations |
| Intensity / `nrIntensity` | 1; 0–2 | overall neural strength; do not promise >1 helps |
| Local Tone / `nrLocalTone` | 1; 0–2 | isolate lighting/contrast contribution |
| Local Structure / `nrLocalStructure` | 1; 0–2 | isolate texture/structure; watch crawling edges |
| Skin Structure / `nrSkinStructure` | 1; 0–2 | test together with auto-mask; actual region response must be observed |
| Automatic Mask / `nrAutoMask` | false | an internal runtime flag, not an editable tracked face matte |
| Input Encoding / `nrInputEncoding` | 0 Automatic; 1 SDR/sRGB; 2 Linear/scRGB; 3 HDR/PQ | choose by actual signal at the node |
| Paper White / `nrPaperWhiteScale` | 1; 0.1–8 | linear proxy scale, not automatic exposure detection |
| HDR Transfer / `nrHdrTransferStrength` | 1; 0–1 | change interpolation for non-SDR branches |
| Guidance / `nrGuidanceMode` | 0 Force Zero; 1 Motion Only; 2 Depth Only; 3 Available | all currently receive zero guides; leave baseline at 0 |
| Depth Convention / `nrDepthConvention` | 0 Input; 1 Normal; 2 Inverted | does not generate depth |
| Motion X/Y / `nrMotionScaleX`, `nrMotionScaleY` | 1; −4–4 | does not generate motion; leave baseline at 1 |
| Output Mix / `nrOutputMix` | 1; 0–1 | explicit source/result blending after NR |
| Output View / `nrOutputView` | 0 Processed; 1 Difference x10; 2 Left/Right Compare | diagnostic views must be reset before delivery |
| Reset / `nrReset` | push button | clear history before a controlled rerun |

### Colour handling that matters

Inspection of `encodeProxy`/`decodeProxy` shows Automatic follows the same clamp path as SDR. **It does not query Resolve's colour management or automatically identify log/HDR.** Float host input is quantized to an RGBA8 neural proxy; float output or a 10-bit container cannot recover precision lost here.

For a conservative first experiment create an explicitly documented SDR test branch. Source log, DaVinci Wide Gamut/Intermediate, ACES linear and display SDR are different signals. Determine what reaches this node, including project transforms, rather than assuming a delivery tag describes it. Use existing colour-managed tools to form the intended input; save transforms. Do not globally switch the user's project colour management for a plugin.

Linear/scRGB uses `s/(1+s)` for nonnegative scaled input and the inverse on return. Negative values are lost; it is not a substitute for a validated colour pipeline. PQ is not a comprehensive HDR reconstruction path. Preserve HDR originals and mark any HDR round-trip experimental. Check scopes, neutral patches, highlights, black levels and skin, not only appearance in a compressed player.

### History and output modes

History resets when time is not previous time + 1, tracked settings change, or reset is requested. Scrubbing, reverse playback or isolated still preview can differ from a sequential export. A hard cut at consecutive timestamps does not itself trigger content-based cut detection in this OFX. Trial clip-local processing/separate shot segments; compare the opening frames and cuts.

`Difference x10` computes `clamp(0.5 + 10*(processed-original), 0, 1)`: unchanged pixels are mid-gray. It ignores Output Mix, so differences there do not prove that a mix=0 delivered image is changed. In split mode the left half is source, right is mixed result, with a white divider. A neutral difference can be legitimate on some material or a failure; resolve with current-window logs and a second suitable test shot.

The runtime restores source alpha, serializes NGX work globally and performs synchronous CPU/D3D12 copies. Multiple instances are not a speed optimization. Export sequentially to judge stability; slower-than-realtime preview does not imply missing frames in a completed export.
