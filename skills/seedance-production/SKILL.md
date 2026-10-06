---
name: seedance-production
description: Prepare, generate, edit, extend and troubleshoot Seedance 2.5 shots in BytePlus ModelArk, including reference prompts, Blender previs and Draft-to-1080p workflows. Use for Seedance production and result review; adapt separately for other providers.
metadata:
  version: "1.0.0"
---

# Seedance production

Turn the user's shot intent into a usable prompt, correct settings and, when requested, a verified video handoff. Default to our BytePlus ModelArk workflow; preserve a different provider explicitly chosen by the user. Explain in Russian unless requested otherwise.

## Route

- For generation/API work, read [BytePlus contract](references/byteplus.md). Recheck current schema before submitting; dated documentation is not a live account check.
- For prompts, Blender, sound or failed takes, read [direction and repair](references/direction.md).
- For provenance and differences from public skills, read [evidence](references/evidence.md).

## Workflow

1. Establish the visible event, start/end state, duration, frame, sound and available assets. Preserve approved film design. Infer routine choices; ask only for missing information that prevents useful work.
2. Choose text, first/last frame, reference, edit or extend before writing prose. Draft is a two-stage output workflow. Do not import another service's UI modes or API fields into BytePlus.
3. Map identity, wardrobe, environment, action, camera, timing and sound to actual reference tags. One asset may control several compatible properties; remove competing authorities. Do not invent uploads or claim unseen media was inspected.
4. Write observable action and its cause, environment/look, camera and sound. Use timestamps when ordering matters, without promising frame accuracy. For editing name the source, target, change, interval and preserved elements.
5. Validate inputs and agreement between prompt and task type. Keep API settings separate from artistic prose. First/last frames should have matching aspect ratios.
6. Use Draft when uncertain staging warrants selection; direct generation may suit a settled shot. Count both stages. Respect existing spending authorization without asking repeatedly within scope. Research or prompt writing alone does not authorize paid jobs.
7. Record task ID immediately. After an uncertain POST, reconcile existing tasks before resubmitting. Recover known jobs through polling/download. Stop at the authorized spend/attempt limit or repeated unresolved failure.
8. Download promptly and review the whole take: action, camera, contacts, object count, identity, temporal artifacts, audio and edit handles. Compare Draft/final by time. Measure media metadata and verify editor import, preserving originals.

## Deliver

For prompt-only requests return settings, a reference map when needed, and one complete paste-ready prompt. For generation provide local media, acceptance status, material defects and usage/cost when available. State what was watched, heard or measured.

Continue our Blender → Seedance → Resolve/Fusion workflow. A local repair may preserve good acting; a broken core action usually needs a new generation plan. Do not introduce training or tools merely because they exist.
