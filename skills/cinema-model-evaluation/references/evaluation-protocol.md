# Experiment and acceptance protocol

Record experiment ID/date, hypothesis, baseline/candidate, exact model IDs and modes, documentation date, source asset hashes, full prompts, request parameters without secrets, output IDs/paths, duration/FPS, cost currency, wall time, labor time, acceptance decision and reviewer.

Choose representative tests from: face/performance; hand/object contact; locomotion; two-character interaction; camera parallax; stylized texture; continuity across two angles; speech/audio synchronization. Use only those the project needs.

Set hard failures before viewing: identity substitution, wrong story action, impossible essential contact, missing product attribute, corrupted media, unacceptable sync or incompatible delivery. A high beauty score cannot average away a hard failure.

For nonfatal dimensions use 0–4 anchors: 0 unusable; 1 major repair; 2 repairable with named intervention; 3 production-acceptable; 4 unusually strong. Unknown/not inspected is null. Document the defect at a timecode and evaluate in the final edit context. These are local rubric scores, not VBench results.

Useful metrics:
- Take acceptance = accepted takes / evaluated takes, with pending takes and denominators visible.
- Yield = distinct useful accepted source seconds / total generated seconds; do not double-count loops or overlapping retained intervals.
- Cash per accepted second = all test generation/post cash / useful accepted seconds. With zero accepted seconds report undefined, not zero.
- Labor per accepted second and wall-time-to-accepted-shot measure different bottlenecks.
- Continuity defects per inspected transition require the number of inspected transitions.

For N paired comparisons report wins/losses/ties and conditions. If uncertainty intervals are needed, use a suitable method and note repeated shots/raters are not independent observations. Never infer a population rate from one selected demo.

Budgeted fallback ladder: repair input/reference → simplify nonessential action → change control route → composite a deterministic element → test another model. A retry repeats only if there is reason to expect new information. Upscale cannot repair wrong acting or contact; interpolation can invent artifacts and must be evaluated separately.

Primary methodological references, inspected 2026-09-24: [VBench-2.0 paper](https://arxiv.org/abs/2503.21755), [official implementation](https://github.com/Vchitect/VBench/tree/master/VBench-2.0). They organize evaluation around human fidelity, control, creativity, physics and commonsense. They do not certify the quality of a whole film. No benchmark is installed or run by merely reading this reference.
