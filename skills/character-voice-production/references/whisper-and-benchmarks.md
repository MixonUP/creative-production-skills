# Whisper preparation and evidence-based voice selection

Checkpoint: 2026-10-04. Recheck changing models and leaderboards before recommending a winner.

## Installed studio

- Full SECourses Whisper-WebUI v13: `E:/Krea_tren_AI/GamesDev/RnD/WhisperWebUI/Vendor/SECourses`, commit `613bebaf0200ebbfdf4ca3b649a1466ebb92a796`.
- Launcher `RnD/WhisperWebUI/START_WHISPER_STUDIO.bat`, localhost 7866. Full IndexTTS Studio remains localhost 7865. Common menu `RnD/START_VOICE_LAB.bat`.
- Independent Python 3.12 environment under WhisperWebUI/.venv. Preserve `local-constraints.txt`: PyAV 19.0.1 failed on the pinned app's `metadata_errors`; 16.1.0 passed actual WAV decoding/transcription. Do not globally downgrade other environments. Author installer freeze listed 17.0.1; our verified compatibility pin is deliberately separate.
- Profile AIWAIFU Russian - Quality: standard large-v3, Russian, no English translation, FP16, batch 1, beam 5, temperature 0; word timestamps and normalized output; VAD/UVR/diarization off initially. It is a starting profile, not proof of best quality.
- large-v3 weights and offline diarization bundle downloaded. All tabs opened; not all optional backends/model weights were exercised. DeepL requires external access/key and was not invoked.
- Evidence: `RnD/WhisperWebUI/Evidence/russian-smoke/report.json`, `Evidence/install/ui-tabs.json`, `startup-v2.err.log`. One 3.12 s synthetic Russian sentence was transcribed exactly; six formats exported. Separate UI run reported 4 s including model load. Neither establishes broad accuracy, warm throughput or p95.
- Illustrated Russian manual: `E:/Krea_tren_AI/GamesDev/RnD/VoiceLab/index.html`.

## Dataset handoff

Whisper performs speech-to-text. IndexTTS performs text-to-speech. Canary-Qwen-2.5B is an English ASR model and is not a Russian alternative to Whisper.

1. Preserve original media and hash inputs. Transcribe the original spoken language; translation is not an aligned training transcript.
2. Review names, numbers, negations, accent/stress-sensitive words and clip endings against the actual audio. Do not regard ASR output as ground truth.
3. Inspect the exported schema. Word timestamp inference with normalized output may still export segment-level JSON/SRT. Do not promise word-level alignment solely because the checkbox is on.
4. Use VAD, UVR and diarization only where needed; compare to originals. Speaker labels do not identify a real person. Separation can damage timbre; short/quiet speech can be dropped by VAD.
5. Split train/validation/final test by source/session before deriving adjacent clips. Continue with dataset.md and the existing manifest auditor.

## Comparing providers and languages

Keep a dated observation record: exact model ID, revision, dataset, language, reference/voice mode, scorer, hardware, sample count and uncertainty. Leave unavailable fields unknown.

- [Artificial Analysis Controlled Voice Arena](https://artificialanalysis.ai/text-to-speech/leaderboard/controlled-voice) evaluates a controlled voice setting. Provider Voice Arena uses providers' own voices. Scores are not interchangeable; language scores are not on one common scale. Record provisional badges and ranking ranges.
- [Open TTS Leaderboard](https://huggingface.co/spaces/hf-audio/open_tts_leaderboard) measures WER/CER, speaker similarity and speed. Filter the intended language/dataset and cloning mode. Its H200 batch timings are not RTX 4090 first-audio latency. Objective similarity is not a listening rating.
- [Method description](https://github.com/huggingface/blog/blob/main/open-tts-leaderboard.md) explains those limits. A model missing from a leaderboard has not thereby lost.
- [Qwen3-TTS report](https://arxiv.org/html/2601.15621v1) compares older ElevenLabs Multilingual v2; do not call it an independent victory over current Eleven v4. Qwen-Audio-3.1-TTS-Plus is also not local Qwen3-TTS.
- [Verli STT benchmark](https://github.com/verliapp/stt-benchmark) provides outputs/scoring but concerns ASR, with English datasets and implementation caveats. Never use ASR ranking as evidence of voice beauty.

Current decision: preserve Main Qwen for Russian; installed IndexTTS Russian remains unproven/failed diagnostic. VoxCPM2 is a next candidate, not installed/accepted here. Its [model card](https://huggingface.co/openbmb/VoxCPM2) lists Russian, voice design, cloning, streaming and LoRA; validate deployment before promoting it. Check current model terms for commercial release; the best objective score may belong to a noncommercial model such as OmniVoice.

The user selected no credit consumption for this audit. That decision does not authorize future ElevenLabs/DeepL requests. External demos and local smoke tests must not be presented as a performed paired listening test.
