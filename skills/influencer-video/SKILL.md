---
name: influencer-video
description: Turn an influencer script and approved identity references into provider-specific video shot specifications, voice handoffs and QA criteria. Use for talking clips, b-roll, interviews, motion transfer or continuations; not for general content ideation or automatic paid submission.
metadata:
  version: "1.0.0"
---

# From accepted image and speech to a usable shot

Adapted from Tilbury's ugc-influencer-video; see E:/Krea_tren_AI/Knowledge/06_Sources/Tilbury_Skills_Adaptation_2026-09-23.md. Read the content card, character bible, voice spec and selected provider adapter. Use film-shot-planning for multi-shot timing and film-postproduction for assembly.

## Verify the route

Record provider, exact model ID, endpoint/mode, checked date, supported inputs, duration, aspect ratio/resolution, audio behavior and credit/cost unit. Unknown capability remains unverified. Do not carry over a fixed 30-second limit, @image syntax or continuation behavior from a different service. Check current documentation before a paid call. Prompt-only requests require a complete prompt with assumptions, not an unwanted test generation.

Input roles are explicit: identity reference; scene/start frame; optional pose/motion reference; voice identity; exact speech track. A short voice sample identifies timbre; it is NOT the narration file for every script. Each script needs its own speech track. An endpoint accepting audio may use it for lip sync, sound conditioning or something else: verify which. Never claim a prompt guarantees exact speech or locked identity.

## Choose a format

- Talking head: accepted start frame plus measured speech, speech-driven animation if supported. Begin with a simple shot when testing a new route.
- Silent b-roll: a clear short action, space for captions if needed, dialogue disabled when supported. Add captions in Resolve for reliable wording.
- Interview: label speakers and off-camera/on-camera roles. Split shots when the chosen route cannot reliably handle speaker changes.
- Motion transfer: use an allowed driving performance and a matching character frame; record framing/body visibility requirements. This is distinct from camera control or general video reference.
- Continuation: use actual last frame/video only in a verified continuation mode. Otherwise plan a deliberate editorial cut; do not promise seamless continuation through prompt wording.

## Write the shot

State identity anchors, scene, light, camera, action, relevant props, dialogue language and timing. Explain why the character is speaking and what they want; support that acting task with a few visible beats. Keep prompts concise enough for the actual provider. A tripod is valid; handheld wobble, autofocus changes, film grain and a phone look are choices, not quality requirements.

Match subject lighting to the location when compositing references: coherent key/fill, contact shadows and plausible reflections. Preserve illumination when the brief requires it. Avoid unnecessary forced relighting of an already accepted start frame. Establish props before the action; inspect object permanence and hand contact. Don't add wardrobe or body restrictions unrelated to the request.

Keep full clean dialogue verbatim in the requested language. Separate speech, room tone, music and effects for editorial control where available. If the track exceeds the provider limit, tighten or split at a meaningful edit point; don't silently speed up the user's approved voice. Exact output duration is measured, not inferred from word count.

## Accept and record

Inspect first/last frames, maximum head turn, hand contact and speaking/silent intervals. Score identity, anatomy, motion, lip sync, voice, lighting and continuity. Keep raw and selected outputs separately. An enhancer can change facial details: compare before/after before accepting. Count all attempts and retained seconds; stop at the authorized limit and change route on repeated failure.

Deliver shot IDs, actual reference paths, prompt, provider assumptions/settings, audio timing, QA checklist and any requested request manifest. Actual launch follows existing scope and budget authorization; record request_id before retrying an uncertain submission. This skill never implies publishing permission.
