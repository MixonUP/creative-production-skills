---
name: blender-game-asset-factory
description: Prepare, clean and export Blender or AI-generated assets into Godot with scale, PBR, collision and provenance checks. Use for game props, modular kits and Tripo handoffs, not film-only previs.
---

# Turn candidates into engine assets

Read `E:/Krea_tren_AI/GamesDev/Docs/ASSET_FACTORY.md` for the relevant asset route. Use `START_BLENDER_GAME.bat` for the isolated game profile. Its MCP endpoint is `blender_games`, port 9877; the film endpoint is different. Confirm the open `.blend`, port and target collection before mutation. If native MCP tools are absent, the existing project-local MCP client or background bpy is an alternative; never report a live connection from configuration alone.

Preserve original generated/downloaded input and make a working revision. Record source, model/version, request parameters when available, permitted use, task ID, seed, attempts and manual repair time. A successful generation is `generated_candidate`, not an accepted game asset.

Prefer modular modeling for architecture and mechanical dimensions; use Tripo candidates for shapes where generation helps. Krea concepts or Blender-projected reference images can guide appearance but do not automatically constitute relightable PBR textures. Inspect baked-in lighting, view seams, unseen sides and thin parts.

Use meters. Apply transforms deliberately before rigging/export; do not blindly apply an armature's transforms after animation authoring. Export glTF 2.0 with the exporter converting Blender Z-up to Godot Y-up; avoid a second manual 90-degree correction. Keep the DCC source outside Godot's runtime asset tree and publish the selected GLB revision into it.

Retopologize for silhouette and deformation needs, unwrap UVs, bake detail, and validate normal orientation and PBR channels. Procedural Blender node graphs need baking or an intentional engine shader. Produce gameplay collision independently of render detail. Reserve UV2 for lightmapping when required. LODs must preserve important silhouettes and character deformation.

Before acceptance: reopen the GLB in Godot, measure bounds, inspect pivots/materials from several directions, test relevant collisions, and record integrated cost. The template's three-part gate proves this exchange only; it does not validate every imported character or Tripo mode. Preparing this route does not start GPU generation or paid provider jobs.
