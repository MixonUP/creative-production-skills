---
name: krea-lora-testing
description: Prepare and evaluate repeatable ComfyUI XY Plot comparisons of Krea2 LoRA checkpoints, weights and prompts in E:/Krea_tren_AI; record workflows and visual findings.
---

# Krea LoRA tests

Read `E:/Krea_tren_AI/Knowledge/00_HOME.md`, the relevant run card and `Knowledge/04_Procedures/XY_Testing.md`.

Identify the exact base checkpoint, quantization, encoder, VAE and LoRA filenames from the loaded/exported workflow. The LoRA training base and inference base are separate recorded fields. Preserve author workflows that the user wants unchanged; use a named copy for experiments.

Compare checkpoints with the same prompts, seeds, resolution, sampling settings and LoRA strength. Include a no-LoRA baseline where the test calls for measuring the learned effect. Compare LoRA weights as a separate axis. Use several scenes/seeds when drawing general conclusions. Upscalers and other LoRAs can mask identity/style differences; evaluate raw outputs first, then the intended production chain.

Project triggers: style captions used `Style ohwx, ohwx`; prior requested test variants were `Style ohwx` and `ohwx`. Girl: `veyra17`. Rider: `dravorn17`. Choose the trigger matching the test. An earlier 40-image test queue was cancelled; do not resume it without a new request.

Record the exported workflow, hashes/steps of LoRAs, prompts/seeds, output paths, and observations about identity, pose, prompt adherence, artifacts and style. Separate user ratings from automatic measurements. Do not infer that the final checkpoint or lowest loss gives the best image.

Before a requested launch, check the existing queue/server read-only to avoid duplicate work. Preparing prompts or a workflow alone is not a request to submit a queue. Do not launch another ComfyUI instance if its existing API responds. Update the test card and journal after meaningful results.
