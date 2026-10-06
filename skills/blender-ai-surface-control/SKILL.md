---
name: blender-ai-surface-control
description: Prepare camera matches, stable 3D textures, masks and depth references using fSpy, Camera Shakify, StableGen and ComfyUI-Blender. Use for controlled Blender-to-AI/Fusion handoffs; not character training or selecting a video model without a request.
metadata:
  version: "1.0.0"
---

# Controlled surfaces and camera handoffs

Start from the actual shot, source image/clip and intended edit. Read [local operating guide](references/operations.md), then only the relevant section in its linked canonical documentation. Inspect `E:/AI_films/Tools/FilmExtensions/registry.json` before assuming an installed component is usable. File installation, successful import, functional execution and visual acceptance are separate evidence levels.

## Choose the smallest useful route

- Perspective from a still: fSpy, then proxy geometry and a camera comparison. A generated image may have inconsistent vanishing points; solve the required region and report approximation.
- Repeated prop appearance across views: StableGen on a fixed mesh, then unseen-view and bake checks. Do not infer face consistency from a prop test.
- Comfy controls inside Blender: ComfyUI-Blender only when it improves the current iteration loop. First validate the workflow in ComfyUI. A bridge does not create temporal consistency.
- Camera character: Camera Shakify on an approved base move; compare bypass and avoid double shake in generation.
- Fusion handoff: beauty plus the necessary masks/data. Prefer separate masks when EXR/Cryptomatte support is unverified.

## Preserve the control contract

Record image size, FPS, explicit frame range convention, camera transforms, focal/sensor assumptions, object IDs, alpha convention and color/data roles. Keep data passes outside display transforms. Use one near/far mapping across an entire depth sequence; confirm near-white/near-black with the selected receiver. Inspect background values and silhouettes. `depth_prepare.py` converts an existing depth array; it does not estimate depth or produce a complete model workflow.

Do not encode a preferred video brand into the handoff. The user's current model choice and actual input support determine the adapter. Read recipes for current choices: LTX is an experimental reserve, while Wan/MiniMax work is deferred. These are local decisions, not permanent prohibitions on future explicit requests. Never activate a deferred backend just to prepare depth.

## Execute and judge

Use the existing Blender MCP for live work after inspecting addon/scene status. Preserve the user scene. Background Blender is appropriate for isolated installation or functional tests; factory startup belongs only in a new process. Keep project revisions, not a reset of the active scene. Read the actual installed API before manipulating unfamiliar operators.

For ComfyUI, distinguish the running process from newly installed files. Do not clear or interrupt an unrelated queue. Save workflow JSON, node/model versions, seed, source hashes and output provenance. Serialize GPU tasks; do not infer permission to interrupt training.

Inspect the camera render and full temporal result when pixels are produced. Check perspective, contact, occlusion, seams, temporal stability and identity separately. Save a bypass/baseline and explicit remaining defects. Use registry evidence/decisions for reusable conclusions; do not mark a tool adopted based only on registration.
