---
name: godot-look-performance
description: Develop and verify Godot lighting, materials, atmosphere and rendering performance together. Use for visual quality passes, shader work and optimization on target hardware.
---

# Judge appearance and cost together

Read the actual renderer and target hardware first. For this project use `E:/Krea_tren_AI/GamesDev/Presets/atmospheric_exploration.json`; numeric budgets are proposals, not measurements. RTX 4090 is the authoring machine and must not silently become the minimum player specification.

Build a reference frame at player height using large shapes, material values and a motivated key light before adding postprocessing. For mostly static final layouts evaluate LightmapGI with UV2 and reflection probes. Evaluate VoxelGI for bounded spaces or SDFGI for suitable larger/dynamic-layout cases; choose one based on constraints, leaks and cost. Do not enable every GI and screen-space effect by default.

The prepared Balanced and Atmosphere resources use direct/ambient lighting, fog and optional volumetric fog; no lightmap has been baked. GI adoption needs a separate real bake/runtime test. Emissive appearance alone is not proof that surrounding objects receive emission lighting.

Use the engine's actual shader language and ClassDB. In Godot 4 use `source_color` for relevant color uniforms and declared screen samplers for screen reads. `vertex()` is a stage, not a `shader_type vertex`. Read property names from the installed version when a snippet fails; do not repair by guessing similarly named API members.

Optimize the measured bottleneck: shader fill/overdraw, shadows, materials/draw calls, mesh complexity, physics or scripting. Split MultiMeshes spatially so culling can work; automatic LOD does not repair every skinned mesh. Alpha-heavy foliage and fog require motion checks, not just triangle counts.

Capture before/after with the same camera, exposure, resolution and scene state. Measure representative gameplay after warm-up, reporting frame-time distribution and hitching with GPU/CPU context. Headless timing is not a graphics benchmark; a tiny lab on a 4090 is not a release performance certification. Inspect images and movement for temporal artifacts before accepting an optimization.
