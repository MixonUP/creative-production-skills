---
name: character-sheet-pipeline
description: Prepare consistent front, side and part references from an approved character image for 3D modeling. Use for reference packs and component extraction before mesh or rig production.
---

# Character reference pack

Use the supplied design as authority. Establish the required body/accessory inventory,
anatomy, rest pose and downstream modeling use. Reuse approval already given.
An A-pose suits many humanoids; select an appropriate neutral pose for other anatomy.
Do not infer a new character design, added equipment or bilateral symmetry.

1. Inspect the input and separate intentional asymmetry from camera perspective.
2. Create a full, neutral front reference with visible extremities and flat lighting.
   Check identity, silhouette and pose before extracting parts.
3. Extract agreed body, clothing, hair and accessory components from that same
   accepted source. Preserve scale cues, camera, pose and material colours.
4. Review each result against the input. Use pass, soft failure or hard failure with
   specific reasons. Missing essential geometry or significant perspective drift
   prevents treating the image as a production front reference.
5. Side/back views may help the modeling task. Identify unseen geometry as a proposed
   reconstruction; obtain a design decision where it materially changes identity.
   Optional turntable video is a separate requested and budgeted deliverable.
6. Deliver a part inventory, source hashes, actual prompts, tool/model, output files
   and review states. Distinguish a technically usable reference from user approval.

Use the available image-generation/editing tool required by the host. An explicit
provider choice remains part of the task; use an available permitted route and verify
its current schema. This skill requires neither fal nor a separate vision API.
Do not copy historical model IDs, prices, paid retry defaults or provider bans.

Read [prompt patterns and review](references/prompts-and-review.md) when constructing
image instructions or evaluating a candidate. Adapt them to the actual anatomy.
A consistent drawing does not prove topology, texture quality, rigging or animation.
Route subsequent mesh work to the existing asset pipeline.

[Source and adaptations](references/source.md).

