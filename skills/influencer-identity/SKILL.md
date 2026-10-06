---
name: influencer-identity
description: Define an AI influencer identity and prepare consistent face, body, outfit and location references for local Krea or a chosen image provider. Use for character bibles, reference sheets and identity repairs; route actual LoRA preparation to krea-character-training.
metadata:
  version: "1.0.0"
---

# Identity before scene variations

Adapted from Tilbury's charsheet-soul; provenance and removed assumptions are in E:/Krea_tren_AI/Knowledge/06_Sources/Tilbury_Skills_Adaptation_2026-09-23.md. Read the chosen character's existing bible before inventing a replacement. Don't silently reuse veyra17, dravorn17 or the SpiderVerse style for a new photorealistic influencer.

Record character_id, version, explicit virtual persona, adult age if human, audience, role, voice/personality, recurring topics, appearance invariants, body proportions, permitted variations and reference provenance. If the task already identifies the character, use it; if several are equally plausible, clarify identity while doing independent preparation. A provisional creative choice must be labeled, not presented as the user's decision.

## Build reusable references

1. Select or create a strong face anchor; preserve the accepted original and hash. A revised identity gets a new version rather than a silent replacement.
2. Prepare front, three-quarter, profile and full-body views as the brief requires. Keep separate high-resolution images; a combined sheet is for review or providers that use it well, not automatically a training sample.
3. Describe stable facial features concretely. Add distinctive details only when wanted; do not force scars, freckles, slim bodies, makeup or a particular ethnicity.
4. Separate identity from costume, pose, scene and lighting. Keep outfit variants and location stills labeled. Don't bake one outfit/background into every training image unless it is intended to be inseparable.
5. Inspect cross-view face shape, age, hairline, eyes, body proportions, hands and accessories. Reject identity drift before including an image in a dataset. Editing a bad face can be useful, but requires rechecking the whole image.

For Krea use the actual selected base and recorded trigger; prepare training through krea-character-training and select quality through krea-lora-testing. For Soul or other hosted systems check their current reference/training requirements; the original author's prompt-length limit and claimed fixes are unverified provider-specific advice. LoRA strength, training steps and number of images are experiment variables, not magic constants.

## Prompt handoff

Deliver a complete prompt when requested, plus the attachment roles and editable variables. Use the user's language for communication; visual prompts may be English if appropriate for the model, but preserve the requested language. Aspect ratio follows the deliverable, not a fixed 16:9 rule. Camera/8K words are visual descriptions, not proof of actual resolution or optics.

For natural realism specify coherent light direction, plausible skin/material texture, exposure and contact shadows. Avoid conflicting instructions such as completely matte skin plus glossy highlights. A reference pose or photograph can guide composition without copying another person's identity. Respect the user's allowed assets and applicable rights; don't impose the source author's blanket bans on props, logos, clothing or real people.

Return the bible, reference inventory, prompts/specifications and unresolved QA items. No images exist until generated; no training is implied by preparing a character sheet.
