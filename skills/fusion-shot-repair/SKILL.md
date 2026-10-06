---
name: fusion-shot-repair
description: Diagnose and repair local shot defects in Resolve Fusion using masks, planar tracking, patches and optional mesh workflows. Use for compositing repair and Blender pass integration; not general editing or promises to reconstruct severely inconsistent AI geometry.
metadata:
  version: "1.0.0"
---

# Repair the measured defect

Read [repair operations](references/operations.md) for local paths and relevant recipe. Inspect the source clip and current project/timeline before making changes. Identify the defect, affected frame range, required output, available source handles and acceptable changes. If only a still is available, do not claim temporal acceptance.

## Select by failure type

- Rigid planar patch: begin with native Planar Tracker/Planar Transform and masks.
- Deforming cloth/skin: consider mesh tracking and unwarp/edit/rewarp; first determine if pixels remain visible and geometry remains coherent.
- Mask from Blender: verify exported channels/metadata and host support. Native Cryptomatte and the open Fuse are separate implementations. Use separate mattes when support is unresolved.
- Noise: compare temporal detail and ghosting before denoising. Denoising does not restore changing anatomy.
- Color/look: establish the actual input transform before grade, grain or halation. Respect intended animation texture and motion.
- Large topology change or disappearing object: compare repair effort with a shorter edit or regenerated shot; do not promise a tracker will recover missing content.

## Build a reversible repair

Preserve source media and original composition. Use a new comp/timeline revision. Keep tracking region, reference frame, patch source, mask/feather, mix and bypass accessible. Separate tracking from final appearance adjustments. Match occlusions, lighting, sharpness, motion blur and grain only as needed for the shot.

For mesh workflows, edit between unwarp and rewarp stages; watch fold collapse, stretching and newly revealed areas. This is not a guarantee of recovered information. Consult the installed plugin's actual docs and license status before executing commercial operations.

Use existing Resolve MCP after verifying project identity and capability. A successful API call does not prove the node exists in Free or that pixels are correct. When a GUI/API step cannot be completed, save a concrete composition/recipe and state which operation remains unverified rather than inventing a result.

## Accept and preserve

Review the full repaired range at normal speed and inspect difficult frames. Compare baseline/bypass with track drift, edge artifacts, color continuity and temporal stability; inspect exported output, not only viewer stills. Technical and artistic acceptance are separate.

Save source identity, exact frames/FPS, node/plugin versions, parameters, before/after and editable comp. Record failures and effort. For repeated gaps, use the build-or-buy procedure; create the narrowest own macro/Fuse/script with a test instead of claiming equivalence to an entire commercial package. Keep old dependencies for old projects until migration is verified.
