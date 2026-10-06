# Asset identity, state and attached reference

Use for repeated characters, locations or props across a sequence. An asset record connects a versioned description with usable media, provenance and acceptance evidence. Keep the description's meaning stable; adapt syntax and length to the actual endpoint.

## Separate three things

- Identity: recognizable face/body/material features that should survive a new angle or light.
- State: deliberate changes such as wetness, damage, wardrobe, visible/hidden prop, day/night lighting. Link variants to their parent; an ID suffix is a local naming convention, not a model command.
- Shot appearance: composition, light, action and camera for this particular image. Do not accidentally bake a dramatic grade into every identity reference.

Choose face crops, full-body views and reverse views for their actual readability. A collage with tiny faces can compete with the desired face reference; use a larger crop or separate attachments when supported. A headless body sheet is a source-specific candidate to compare, not a default rule. Neutral sheets can help identity evaluation; accepted dramatic keyframes remain separate.

For locations retain stable landmarks, entrances, relative dimensions, useful reverse angles and motivated lights. For props distinguish closed/open/held/concealed states when needed. A generated orbit or reverse angle is a candidate reconstruction: inspect geometry before promoting frames from it to canonical references. Exact geography may warrant a simple Blender proxy.

## Prove the asset in the intended workload

Pick a small budgeted sample covering the risks of the coming scene: close/wide framing, an alternate angle, a different motivated light and an interaction if needed. Record failures separately as identity, costume, spatial, texture or performance issues. Do not blame every failure on wording or declare stability from an isolated portrait. No single fixed number of successes proves general consistency.

Before submission make a role table: actual attachment number/ID/hash → asset revision → intended role (identity, location, composition, motion, material). Check that every active tag resolves to a supplied reference and that the supplied set contains no stale extras. A prompt mentioning three images does not prove three were attached. If a public project omits an input, record the gap rather than inventing the link.

## Edit locally when preservation matters

Write one intended change and the protected properties. Keep the accepted original; use a mask/crop or composite a changed region back when appropriate. Preserve crop coordinates, padding, resize, color interpretation and derivation history. A masked request does not guarantee unchanged pixels outside the region; inspect the returned image and the composite. For video also test tracking, occlusion, edge behavior and time consistency.

Avoid repeatedly processing the whole accepted reference solely to fix one detail. Whole-image regeneration can still be warranted for global changes; compare it deliberately. Provider rankings, negative-prompt support and input counts belong to dated adapters, not this guidance.

Evidence: procedural adaptation from HELL GRIND Brief/LIRA and a directly inspected generation card, 2026-10-01; local quality benefit untested. `E:/Krea_tren_AI/Knowledge/06_Sources/Hell_Grind_Transfer_2026-10-01.md` holds source-specific claims and limitations.
