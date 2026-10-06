---
name: krea-character-training
description: Prepare and document Krea2 LoRA character or style training in E:/Krea_tren_AI with AI Toolkit, including dataset manifests, actual configs and evidence. Use for this project's training preparation or diagnosis.
---

# Krea training

Read `E:/Krea_tren_AI/Knowledge/00_HOME.md`, the target run card, and `Knowledge/04_Procedures/Training.md`. For reported failures also read the relevant entry in `Knowledge/05_Troubleshooting/Known_Fixes.md`.

Find the user's intended base and current installed Toolkit support before choosing fields. Raw, Base, Turbo and Kreamania must not be silently substituted. Captioning with Qwen3-VL-4B is distinct from choosing an inference text encoder. Consult installed loader/config code when validating local formats and paths.

Use the actual completed run config as a baseline, not an unrelated example YAML. Preserve it and give the new experiment a unique name. The project's 32/32 rank, LR 0.00005, 1600-step character recipe is a baseline, not a universal optimum. The creator's LR 0.0005/cosine recommendation is in `Knowledge/06_Sources/Krea2_Creator_Advice.md` and is not yet validated here.

Before training, capture image/TXT hashes, image count, caption conventions, duplicates, synthetic/video provenance and data version. Keep style and character triggers distinct (`ohwx`, `veyra17`, `dravorn17`). User requested a 1024 training bucket; confirm other resolutions in the intended experiment. Preserve aspect ratios and identify low-resolution inputs rather than claiming resizing adds detail.

Record LR scheduler separately from noise scheduler and timestep sampling. Do not treat epochs and optimizer steps as independent targets; check repeats, batch, accumulation and multi-resolution behavior.

Validate config syntax and supported fields, existing model/encoder/VAE/dataset paths and output name. Report what was checked; parsing does not establish runtime or visual quality. Do not start training merely to validate a prepared config. Follow current user authorization for actual launches.

On completion, verify the Toolkit status and safetensors training_info, then record the real steps. Select quality with repeatable inference tests. Update the experiment card and append to the action journal with evidence and outstanding uncertainty.
