---
name: cinema-visual-development
description: Design film character and world bibles, camera and lighting language, continuity references and shot-specific generation briefs. Use to develop or repair a coherent film look; not for executing LoRA training or replacing detailed Blender shot planning.
metadata:
  version: "1.1.0"
---

# Make a visual language that survives cuts

Translate the brief into observable properties: shape, palette, value structure, texture, staging, movement and sound-image relationship. A famous director or brand name is only a research lead. Describe the chosen properties without assuming every film by that creator shares them.

## Lock what matters

Build only the references the sequence needs. A character bible records invariant identity, proportions, wardrobe/materials, voice and behavioral signature; a scene state records allowed changes such as wet clothes, injuries and emotional progression. Do not confuse consistency with a frozen expression. World continuity covers layout, scale, entrances, practical lights, weather, recurring objects and material rules.

For every asset record ID/version, path, provenance, role and accepted/pending status. Distinguish appearance images, performance references and spatial guides. Include useful angles and expressions rather than dozens of redundant portraits. Test a representative change of angle/action before calling an identity stable across the film.

For a reusable generated cast/world, read [asset-locks.md](references/asset-locks.md). It separates identity from shot appearance, tracks state variants and actual attachments, and defines small stress tests and localized edits without assuming a particular model or reference-sheet layout always works.

## Choose camera and lighting deliberately

Use [visual-recipes.md](references/visual-recipes.md) as adaptable starting points. Lens numbers require sensor/FOV, camera distance and framing; perspective is determined by viewpoint. A prompt saying 85mm is an aesthetic request, not verified optical metadata. Moving the camera and zooming are different decisions. Pick motivation, start/end framing, subject distance, screen axis and movement pace.

Specify the light's direction, apparent source size, hardness, practical motivation, color relationship and background separation. Make intended exposure and palette changes traceable across cuts. Do not prescribe a LUT as a substitute for consistent source interpretation.

## Compile a generation brief

Write the necessary subject/action, spatial relations, camera, light, reference roles and essential invariants. Remove contradictory movements and unnecessary prestige words. State positive desired behavior; use negative controls only where the exact endpoint supports them. A provider adapter translates the brief into API fields and attachment syntax.

Deliver bibles, asset manifest, continuity states and shot briefs. Use `film-shot-planning` for time/geometry contracts, `blender-film-blockout` for exact staging and `krea-character-training` only when actual training is needed. ControlNet, IP Adapter and LoRA compatibility must be checked for the actual model/workflow; their names do not establish compatibility with Krea or hosted video endpoints.
