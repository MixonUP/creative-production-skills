# BytePlus contract — checked 2026-10-05

Source: https://docs.byteplus.com/en/docs/modelark/seedance-2-5 (live page, dated September 28). Recheck its linked Create video generation task API for implementation details.

Model: `dreamina-seedance-2-5-260628`. Base: `https://ark.ap-southeast.bytepluses.com/api/v3`. Create: `POST /contents/generations/tasks`; retrieve: `GET /contents/generations/tasks/{id}`. Keep credentials in the authorized runtime environment, never prompts or receipts.

## Modes

| Intent | Content / task type | Settings |
|---|---|---|
| Text generation | text | duration 4–30 integer seconds or -1 |
| First frame, optionally last | image roles first_frame, last_frame | first_frame required; ratio adaptive |
| New scene from references | reference_image/video/audio; omni_reference_task_type reference | supported ratio and duration |
| Modify source | reference_video; type edit; explicit editing intent | ratio adaptive, duration -1; every video 4–30 s |
| Continue source | reference_video; type extend; explicit continuation intent | ratio adaptive; duration 4–30 or -1 |

Explicit task types move checks earlier but do not prevent asynchronous TaskTypeMismatch when prose contradicts the type. TaskTypeConstraint indicates incompatible parameters. Fix the cause before retrying. Auto infers intent and can classify an apparent reference prompt as edit.

Ratios: 21:9, 16:9, 4:3, 1:1, 3:4, 9:16, adaptive. For text/reference, adaptive chooses a supported ratio, not arbitrary source dimensions. Output: 480p/720p/1080p; mp4/mov. Explicitly choose audio behavior. A seed is not a guarantee of identical regenerated motion.

## Inputs

| Asset | Limits |
|---|---|
| Images | Up to 30 references; JPEG/PNG/WebP/BMP/TIFF/GIF/HEIC/HEIF; each <30 MB; sides 300–6000 px; width/height 0.4–2.5; URL/Base64/asset ID |
| Video | Up to 10, sum ≤30 s; each 2–30 s, or 4–30 s for edit; ≤200 MB; MP4/MOV; 24–60 FPS; URL/asset ID, no Base64 |
| Video dimensions | 480p/720p/1080p/4K documented; sides 300–6000 px; ratio 0.4–2.5; pixel area 407696–8295044 |
| Audio | Up to 10, sum ≤30 s; each 2–30 s, ≤15 MB; WAV/MP3; URL/Base64/asset ID |

Total ceiling 50 assets; body ≤64 MB. Ceilings are not target counts. Audio-only reference is supported. MP4 input supports AVC/HEVC with AAC/MP3; MOV also supports PCM. Validate codecs, not extensions alone.

For real-face inputs, check the current supported authorization/portrait route: https://docs.byteplus.com/en/docs/modelark/seedance-portrait-asset-guide . The tutorial restricts direct uploads; do not assume a locally generated portrait is automatically accepted. A public-bucket example is not a reason to publish private assets.

## Draft → final

Create a valid request with `draft:true`, `resolution:"480p"`. Wait for succeeded, download and review. Store ID and created_at. Promote the accepted ID within seven days FROM created_at:

```json
{
  "model": "dreamina-seedance-2-5-260628",
  "content": [{"type": "draft_task", "draft_task": {"id": "<accepted-task-id>"}}],
  "resolution": "1080p",
  "output_format": "mov"
}
```

Request-shape example only. Same model required; omit draft or set false; only 1080p promotion supported. Do NOT resend prompt, images, video, audio, duration, ratio, seed, generate_audio or omni_reference_task_type—even identical values cause errors. They are inherited. Creative revisions require a new Draft. Reuploading the Draft as a video reference is a different operation.

Output_format, return_last_frame, watermark and permitted service fields can be specified again. Omitted values use defaults, not Draft settings. Check current API restrictions before setting service_tier, execution_expires_after, priority, callback_url or safety_identifier.

Both stages are billed. HD accounting uses original input video duration; the Draft is not counted as another video input. Inherited settings do not prove unchanged acting, pixels or audio; inspect final output.

## Output and operations

- Task records: seven days. Output URL: 24 hours, at most 100 downloads. Archive locally promptly.
- 1080p is documented as HEVC/10-bit; the general MOV section describes AVC/yuv444p/PCM. Measure actual output instead of assuming the generic description applies to every resolution. Ten-bit alone is not HDR.
- Edit tolerance conflicts: tutorial says up to 0.4 s shorter, prompt guide about 0.3 s. Plan for 0.4 s and measure. MOV is recommended for edit/extend; verify Resolve playback and audio.
- Recheck https://docs.byteplus.com/en/docs/modelark/model-pricing before estimates. Include input-video duration, minimum token floors, rejected takes, and both Draft/HD stages. Actual usage/billing is authoritative; no permanent dollar price is embedded here.
- Historical calculations: E:/Krea_tren_AI/Knowledge/06_Sources/Seedance25_Draft_Mode_2026-10-02.md. Historical balances do not prove current funds or spending authorization.
- After timeout reconcile existing jobs. Handle 429 with backoff and current account limits; do not loop duplicate paid submissions or buy credits implicitly.
