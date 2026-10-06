---
name: godot-character-animation
description: Prepare and integrate rigged 3D characters, retargeted clips and AnimationTree locomotion in Godot. Use for game character animation and deformation checks.
---

# Verify animation in the game

Read the character route in `E:/Krea_tren_AI/GamesDev/Docs/ASSET_FACTORY.md`. Define camera distance, silhouette, required actions and facial needs before spending on topology or rig detail. Do not treat a turntable or video clip as a skeleton animation asset.

Finalize topology before skinning; mesh reconstruction can invalidate weights and animation bindings. Keep an unmodified source and a rigged working revision. Check rest pose, root, bone hierarchy, scale and orientation before retargeting. Common bone names alone are insufficient; Godot's BoneMap/SkeletonProfile addresses rest-pose differences. Use SkeletonProfileHumanoid only for suitable humanoids; unusual creatures need an explicit mapping or their own rig.

Export actual action clips with intended duration, loop boundaries and names; bake unsupported constraints to transforms. Check whether the exchange preserved skin weights, shape keys and accessories. Never claim glTF carries Blender's rig controllers, drivers and every constraint unchanged.

Use AnimationPlayer for clips and AnimationTree for blending/state control. Query the existing tree before setting parameter paths; root state-machine playback commonly lives at `parameters/playback`, but nested paths depend on the authored tree. Blend spaces use their actual `blend_position` parameter. Do not copy invented `state_machine`, `process(delta)` or generic `speed` paths from tutorials.

Choose in-place versus root-motion locomotion explicitly. CharacterBody3D movement and animation must have one translation owner; never apply the same root displacement twice. Test idle/walk/run transitions, turns, starts/stops, slopes, contact events and representative extreme poses. Inspect shoulder/hip collapse, foot sliding, hand intersections and detached accessories in engine.

Acceptance includes actual clip playback and transition evidence plus known limitations. The current studio starter has a capsule controller, not a completed character rig; report this boundary rather than inferring rig validation from a successful GLB prop import.
