---
name: influencer-pipeline
description: Coordinate a repeatable AI influencer production batch across character identity, content, Krea LoRA images, voice, video and Resolve. Use for pipeline design, batch preparation and bottleneck diagnosis; not for implementing the InfluencerOS application.
metadata:
  version: "1.0.0"
---

# Produce a measurable batch

In E:/Krea_tren_AI read Knowledge/04_Procedures/Influencer_Pipeline.md and the relevant character/run card. Read only the stage needed now. Preserve the user's chosen format, tools, budget and existing authorizations. A request to prepare a pipeline or install skills does not start training, GPU queues, paid calls or publishing.

## Route the work

- Identity/reference pack: influencer-identity.
- Topics, hooks, narration: influencer-content.
- Dataset/configuration: existing krea-character-training; checkpoint/weight comparisons: krea-lora-testing.
- Shot-level image/audio/video handoff: influencer-video. Complex composition or repeated camera geometry: film-shot-planning, then blender-film-blockout if useful.
- Editing, sound and export: film-postproduction.
- A requested sellable workbook/template/product: influencer-product. Monetization is optional, not a prerequisite for production.

Use those skills when available, otherwise read their canonical copies under Tools/skills. Keep generic provider-independent planning separate from a verified provider/model/endpoint adapter. Higgsfield is a platform, not one model; a local image LoRA is not a hosted video input.

## Work from artifacts, not chat recollection

Each batch has a manifest with stable character, content and shot IDs; a character bible version; references; scripts; voice identity and exact speech tracks; provider/workflow versions; raw outputs; selected takes; QA; and render details. The initial manifest is created by `Tools/InfluencerPipeline/pipeline.py init PATH`. `check PATH` validates evidence and dependencies offline; it never runs an external app. Read its JSON report before calling a batch complete.

Distinguish planned, prepared, generated, accepted and rejected assets. Prepared means an input/specification exists, not that the model has run. Generated means a recorded run returned an artifact, not visual acceptance. Acceptance requires an attributed QA record and a file hash. Human approval to publish is a separate action and cannot be inferred from accepted visual QA.

Schedule cheap work first: scripts and reference selection, image contact sheets, voice tests, one short video pilot, then the batch. Expand only when the pilot meets the brief. Don't retrain an accepted character for every post or use expensive video to discover an unresolved face. Maintain one heavy GPU job at a time on the documented 24 GB RTX 4090 setup; inspect the queue before a launch the user requested. Do not stop a user's job to make room.

## Optimize the observed bottleneck

Measure identity, realism, prompt adherence, anatomy, motion, lip sync, voice and editorial usefulness separately. Use matched scene briefs across routes; same numeric seeds across different models are not matched latent samples. Compare raw outputs before enhancement. Record accepted/attempted, elapsed and hands-on time, credit/currency units and actual cost per accepted clip or retained second. Unknown price is unknown, not zero. Never sum unlike currencies or credits.

Use a bounded pilot with an agreed attempt/cost limit before paid work. A repeated failure calls for a changed input, simpler shot or different route; don't burn retries with the same prompt. Existing authorization covers actions within its scope; don't add approval gates for routine drafting or reversible preparation.

The existing film exchange is Testfilm-specific and CPU-smoke-tested, not an end-to-end influencer generator. Adapt paths/project IDs in a named copy and inspect readback before using it on a new project. InfluencerOS desktop is documentation-only at the recorded revision; do not make it a required running dependency.

Append results, paths and remaining uncertainty to the project journal. Provider claims stay hypotheses until tested. Preserve original recipes and raw outputs; don't overwrite earlier evidence.
