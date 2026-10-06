# ComfyUI and external adapters

Snapshot date 2026-09-30. These are candidates unless local evidence says otherwise. A Resolve request remains a Resolve request; explain a limitation before proposing an external path. A feature list is not a quality ranking.

| Route | Fits | Critical boundary |
|---|---|---|
| Installed SAOG OFX 0.3.1 | editable same-size NR in Resolve | zero guides, synchronous bridge, personal experimental package |
| OreX/Ox, commit `739208e7` | author's Russian lesson, image/VIDEO, chunks | resizing then NR; not native SR; J/K/L/M reserved |
| HECer, commit `f4f59cd1` | research into real SR+NR, depth/motion guides | extra isolated runtime/models; alpha; full Comfy IMAGE batches still occupy memory |
| Blueforcer Enhancer | process-isolated file worker | documented Merserk v3.0/protocol 4 pairing; latest standalone is not a drop-in worker |
| Merserk Visual Enhancer, commit `63ec8793` | standalone finishing with broader controls | separate application; v13.2 is not the Resolve plugin or Blueforcer runtime |
| lisitskyaa NR | specialized in-process NR/NVIDIA Optical Flow trial | native failures may affect host; runtime/GPU compatibility must be tested |

See the [source ledger](sources.md), project lesson card and each version's current instructions before installing. Choose one route for a specific gap. Preserve the exact user's workflow when asked to reproduce it, including dependencies; don't silently replace its nodes with similarly named ones.

## OreX/Ox semantics that prevent wasted tests

The inspected README reports defaults v0.9.28. Current instructions require a separately supplied compatible runtime; an older tutorial saying it downloads automatically is not a current installation contract. Use the actual Comfy interpreter/venv, inspect requirements before changing packages and keep knowledge tooling separate.

`1x` isolates NR. Higher output-size modes resize before NR; their game-like Quality/Performance labels do not establish DLSS SR inference. The model-preset widget J/K/L/M is reserved: comparing it alone cannot establish a model difference. Intensity above 1 is documented as having no added effect on this runtime. The skin control is gated by auto-mask per this adapter; don't transfer that as proven behaviour of every wrapper.

`temporal_mode=auto` detects cuts by luminance change; `none` keeps history after the first frame, rather than disabling temporal processing. Warmup repeats evaluations after reset. Preview starts fresh and is not equivalent to the same frame in a completed sequence. `gpu_mode=OFF` still runs the neural bridge on a GPU: it changes staging, not CPU inference.

Chunking can reduce the processing working set while the full output tensor remains. Estimate one RGB float32 batch as `frames × width × height × 3 × 4 bytes`, then account for input/output, guides, model weights and temporary copies. Never use that arithmetic as an exact VRAM prediction. A claimed RTX 5090 speed is not a measured RTX 4090 speed.

## HECer guided video: when useful

Use only when a measured need for SR or temporal guides justifies extra setup. Workflows separate stills, persistent video, bounded overlap, VDA-S, FlashDepth and optional FG. The source release notes, not an assumed easy preset, identify actual guide models.

The persistent path retains native history for a sequence; bounded mode uses overlapping windows but retains full Comfy batches. Motion is current-to-previous in the documented RAFT path. Inspect motion/depth and cut resets if trails or periodic changes appear. Guide estimates from pixels are not engine-authored geometry/material data.

Workflows 04/05 end at an image preview in this revision; an encoder and correct source FPS are still required. Never report them as saved video merely because preview succeeded. Frame Generation requires its own runtime setup and requested rate change; it is unnecessary for an ordinary same-FPS finish.

A runtime-status “present” or Python import “pass” is not inference. Some workflow source trees use Git LFS; a pointer text file is not a DLL. Keep guide/backend Python environments isolated as the author specifies; don't upgrade the active Comfy Torch stack to satisfy an optional model without an explicit scope decision.

## Handoff to Resolve

Persist source path/hash, integer frame range, source FPS/time base, actual output frames/dimensions, audio, colour conversion and runtime identity. Send a new output revision to Resolve, relink only the intended copy/shot and verify duration against the original. Keep original audio when the image-only route omits it. Verify audio stream copy versus transcoding instead of assuming preservation from a node type.

Do not expose local paths, tokens, prompts/workflow metadata or private footage in public issue reports. Source research never authorizes posting. Each project's source code license and bundled runtime/model licenses have separate scopes.
