---
name: godot-atmospheric-worlds
description: Design and build explorable Godot 3D levels with landmarks, modular geometry, readable routes and controlled procedural dressing. Use for atmospheric environments and level layout.
---

# Build space the player can read

Use the current game brief and target camera. This project's default is Windows atmospheric exploration, not a commitment to a particular story. Read `E:/Krea_tren_AI/GamesDev/Docs/RESEARCH.md` for the chosen route and `Presets/atmospheric_exploration.json` for starting dimensions.

Plan a route graph before dressing: entrance, visible landmark, occluded approach, reveal, optional discovery and return. Specify the player's expected line of sight and activity at each beat. A beautiful fixed camera does not prove a useful exploration level. Test at actual player eye height, in both travel directions.

Set modular dimensions, pivots, door clearances and material families before producing variations. Keep hero landmarks deliberately placed. Use seeded scatter for secondary rocks, debris and vegetation, with exclusion masks derived from the same gameplay paths. Save the seed and recipe; avoid rebuilding static dressing every frame.

Choose native instanced scenes for small authored levels. Consider Terrain3D only when sculpted terrain materially helps; verify its pinned binary against the actual engine before adoption. Use GridMap for regular modular grids, ordinary scenes for interactable objects. Prototype CSG may be baked when its cost or shipping workflow warrants it; do not claim all static CSG recomputes every frame.

Check render meshes, collision and navigation separately. Doorways need actual body traversal as well as a visible opening. Navigation reachability is a separate test if NPCs exist. Inspect joins, undersides, interiors and terrain contacts from multiple angles. Budget scene detail by distance and use spatially partitioned MultiMeshes, mesh LOD, HLOD and occlusion where measured useful.

Deliver an editable scene, route description, scale contract and player-height review images. Record what the player can actually traverse; label a decorative mockup accordingly. Do not infer that a generator's advertised map size implies shippable content or performance.
