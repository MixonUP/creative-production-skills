---
name: blender-film-blockout
description: Build and revise editable Blender proxy scenes, cameras and animatics from a shot plan for video-model references. Use for spatial blocking and reproducible previs, including local MCP or background bpy execution; not for final character sculpting.
metadata:
  version: "1.0.0"
---

# Editable previs before detailed assets

Read the shot contract and applicable project environment card. In Krea, also read `Tools/BlenderMCP/README.md`. The installed Blender version and current scene determine the API and safe edit scope.

## Work in the actual scene safely

Use the connected Blender MCP when available for interactive edits and inspection. Read addon status and scene before modifying them. If native MCP tools have not loaded, a verified stdio client or the installed Blender CLI is a valid route; report which route was used. Do not claim a connection merely because config exists.

For a new project, create a versioned `.blend` and a reproducible build script/config. For an existing scene, preserve a version before editing and do not clear user objects. Avoid factory reset in a live user session. Save inside the project. A request to build previs includes proportionate local previews, not paid generation or unrelated GPU jobs.

## Build only geometry that communicates the action

Use distinct collections for environment, subjects, cameras, lights and reusable effects. Stable object IDs and editable controls matter more than polygon count. Include head/torso/pelvis, separate limbs/contact surfaces, hair/clothing masses and recognizable animal silhouettes where the shot needs them. Simple primitives should still show which direction a subject faces.

Use one shared placement for all cameras. Never move a character per shot merely to conceal a camera error without documenting that cheat. Keep primary contacts fixed during holds; settle weight before secondary motion. Use a rig, constraints or a reproducible pose map appropriate to the scope. Label baked geometry animation honestly; do not call it a fully rigged character.

Fit camera elevation, framing, focal length and subject scale from the image as estimates. Inspect the camera render, not just the perspective viewport. Preserve eyelines and intentional crops. Prefer restrained distinguishable proxy colors; saturated identity colors can leak into generated appearance. ID masks are compositing helpers unless the endpoint explicitly supports them.

## Render and inspect

Render a few diagnostic frames before the entire timeline. Check subject silhouette, head/hand/hoof contacts, clipping, occlusion order and transitions. Fix the scene, then render a clean animatic without grid, selection, labels or gizmos. Use a constant FPS and the agreed aspect ratio. Keep review contact sheets with labels separate from generation inputs.

Check renderer/API settings in the installed Blender; do not assume copied version-specific fields exist. PNG frames plus an external H.264 encoder are a useful fallback when Blender's video output API changes. Keep local preview compute modest and do not interrupt existing jobs.

Save scene, build parameters, camera transforms, representative keyframes and export/trim manifest. Verify encoded dimensions, FPS, frame count and duration. For a handoff, include the exact edit master plus per-shot clips when useful. A placeholder shadow must be identified as such; do not present a flat projected silhouette as a physically validated cast shadow.

Report what is visually verified, which details remain approximate and the next focused revision. If the scene will feed a generative model, clarify that the model receives rendered pixels and may alter the controlled geometry.
