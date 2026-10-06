# Failure diagnosis

Do not treat all DLSS wrappers as sharing a log, runtime ABI or repair. First identify the exact OFX/node and version. Use a small, bounded retry after one supported change; stop repeating an identical native failure and preserve evidence.

## Evidence ladder

| Observation | Proves | Does not prove |
|---|---|---|
| Bundle exists | files present | correct build or active plugin |
| Hashes equal pinned release | byte identity with that release | safety certification, rights, inference |
| OFX cache lists plugin | host registration | Feature 18 execution |
| `NGX Core Init succeeded` | core initialized | feature accepted or evaluated |
| `Feature 18 CreateFeature succeeded` | feature created | a processed frame |
| `Feature 18 EvaluateFeature succeeded: frame=…` in current run window | at least one runtime evaluation completed | all frames processed or better quality |
| Export differs from matched bypass | pipeline changed pixels | accurate detail/temporal quality |

Log: `%LOCALAPPDATA%/ResolveDlss5/ResolveDlss5.log`. It appends local timestamps. Success is logged for the first three frames and every 120th evaluation; absence of a line for every frame is expected. Counts can restart per runtime. Multiple instances share the log and it does not identify a source clip, so correlate the timestamp window, test project and saved settings. Preserve before/after offsets or copy the run window rather than deleting historical logs.

`scripts/probe_resolve.py --since "2026-09-30 03:00:00"` parses known events but cannot certify the current clip. Use the actual start time, not this example. Without a timestamp it labels evidence historical. A new success followed by a failure is a mixed result, not a pass.

## Symptom → next discriminating check

| Symptom | Check and bounded response |
|---|---|
| Effect absent | verify full `ResolveDlss5.ofx.bundle/Contents/Win64` layout and expected OFX hash; host must start after install; inspect Preferences plugin list and OFX cache; don't blindly delete the whole cache |
| Registered but unchanged image | actual effect instance, enabled, Output Mix, output wiring, current project/clip and fresh cache; inspect EvaluateFeature vs fallback; Difference x10 uses gray baseline |
| `source fallback`, `Feature 18 is inactive` | original frame is intentional failure fallback, not successful enhancement; preserve exact error and runtime identity |
| Missing private runtime | verify `Contents/Win64/runtime/nvngx_dlssnr.dll`; compare pinned package hash; restore same package, not a gaming DLL beside Resolve.exe |
| CreateFeature fails / `0xBAD00001` | capture call site, GPU/driver/runtime hashes; compatibility is not inferred from “RTX” alone; one reset after a supported correction; no blind driver/Resolve update |
| `0xBAD00002` or SEH/HRESULT | inspect exact preceding operation; hex code alone is insufficient diagnosis; preserve log, avoid repeated GPU crashes or mixed runtime bundles |
| Black/stale output | inspect OFX persistent message, other nodes and alpha; plugin claims source fallback, so black output may be elsewhere; simplify a duplicate comp |
| Wrong colour/exposure | inspect actual input encoding, project transforms, levels and proxy clipping; Automatic is not detection; don't correct a double transform with artistic strength sliders |
| Flicker after scrubbing | compare sequential export to isolated preview; check reset/time discontinuity; source OFX has no real MV/depth |
| Cut contamination | segment shots/use separate instances; explicit reset; consecutive frame indices alone don't indicate a cut |
| Periodic seam in Comfy | identify wrapper; native chunks may reset history; inspect overlap/persistent mode and loader frame order; don't transplant another wrapper's controls |
| Sluggish preview | baseline CPU↔D3D12 copies and serialization; use a short relevant segment, an isolated lower-resolution diagnostic or rendered cache; final quality needs full-size test |
| Out of memory | observe active tasks, shorten input/reduce test size or batch; don't kill unrelated Python/Comfy/Toolkit processes or unload their models without authorization |
| MCP cannot connect | use existing launch/bridge remediation for 21.0.x Free; keep host fixed; no upgrade to 21.1 as a repair |

## Reset versus restart versus rollback

Use the effect's Reset button before restarting the host. Save before a host restart; verify no render/unsaved work would be interrupted. Reset can release a latched failure but cannot create missing GPU/runtime support. Do not make a retry loop.

If the newly installed bundle destabilizes Resolve, preserve logs and hashes, close the host normally after saving, verify the absolute target is exactly `C:/Program Files/Common Files/OFX/Plugins/ResolveDlss5.ofx.bundle`, then move only that folder to a named backup outside the scan directory. Windows native file operations and admin rights may be required. Preserve the release archive and documentation; never remove Topaz or unrelated OFX. On reopen confirm host/MCP function separately from the registry update.

Do not infer that a community-modified runtime is malicious solely from Authenticode HashMismatch, or that it is safe because a maintainer publishes a hash. Report provenance accurately; never disable Defender/security or ignore a real block to finish installation.
