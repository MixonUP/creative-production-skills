# Direction and repair

Source inspected 2026-10-05: https://docs.byteplus.com/en/docs/modelark/seedance-2-5-prompt-guide . Provider recipes plus studio judgment below are not measured success-rate claims.

## Prompt construction

Describe the action's cause, visible change and ending. Express performance through gaze, posture, hesitation, contact and reaction. Give the camera a readable purpose. Match action/dialogue complexity to duration. Avoid competing camera moves and incompatible style references.

Use ordered time intervals for multiple beats; simple clips need not have timestamps. Multi-shot generation is supported within the request limit, but separate shots can give more editorial control. Choose according to the actual scene.

Keep uploaded tags exact. Identify each character and bind voice/wardrobe consistently. Say what each reference controls and what it should not transfer. Remove unused assets. Intermediate keyframes are semantic guidance, not automatically locked timeline frames. First/last images should share ratio to avoid stretching.

## Blender and storyboards

- Coarse blockout: simple geometry communicates paths, blocking, camera and timing. Pair with approved appearance/environment images; map proxies explicitly and separate their crude materials from final appearance.
- Fine re-render: provide a clean complete preview without viewport axes, trajectory lines or camera cones. Reference is for new interpretation; edit modifies the source. Match prose and API mode.
- Storyboard sheet: state panel order/times and full-frame output without visible grid. It guides composition, not exact frames.
- Test the critical action before investing in prettier blockout geometry. Do not presume perfect camera transfer.

Original example, to adapt only after actual references exist:

```text
Create one continuous five-second shot. @Video 1 supplies camera movement,
blocking and timing. The tall proxy represents the single girl in @Image 1;
@Image 1 supplies her appearance and clothing. @Image 2 supplies the snowy
setting and illustrated surface treatment. She notices a moving shadow,
stops, then turns her gaze toward the path. Follow the camera trajectory
and action order of @Video 1. Render proxies as the specified characters
and environment. End on her held reaction. No additional cuts.
```

This is an illustrative prompt, not a tested take or default art style. Add sound per the brief and audio flag.

## Audio

Specify ambience, motivated effects, music intent, and dialogue speaker/language. BytePlus recommends () for music, <> for effects, {} for speech and 【】 for subtitles. These are prose conventions, not separate stems or guarantees.

If unwanted music appears, the guide suggests strengthening the constraint at beginning/end and naming unwanted musical textures. Use only as needed. Demanding voices alone can remove wanted ambience; vocal separation also removes effects, which may need rebuilding.

Russian is absent from the tutorial's 11 documented native languages. Treat Russian speech as a trial, not a proven impossibility or guaranteed capability. Check pronunciation, voice assignment and lipsync on the final. Extension may change loudness; audition joins.

## Targeted repairs

| Defect | Intervention to test |
|---|---|
| Mode mismatch | Align task type, prompt, ratio and duration; inspect error |
| Identity drift | Remove competing appearance references and clarify character mapping |
| Camera ignores previs | Give video camera/timing responsibility; remove conflicting prose; test hard segment |
| Local defect, good performance | Compare targeted edit with Fusion repair; preserve original |
| Need new aspect ratio | Edit locks ratio; use reference regeneration with timeline or conventional reframing |
| Fingerprint-like foliage | Official workaround: resize overly large AI image copy to no greater than output resolution, while respecting minimum input dimensions |
| Complex added trajectory fails | Guide proposes reference animation first, then edit into original; justify extra cost |
| Bubbling/echo audio | Remove unnecessary water/wave/echo cues diagnostically; preserve essential scene intent and repair sound separately when needed |
| HD drifts from Draft | Judge action, identity, timing and audio in final; repair/reject on its merits |

Change one suspected cause per diagnostic attempt where practical. Record hypothesis and result. Provider examples establish candidate recipes, not statistically best methods.

## Acceptance

Watch the full clip: composition, causal action, contacts, eye lines, object count, anatomy, background motion, temporal texture and edit handles. Listen to dialogue/effects/joins. Draft can select staging but not certify fine detail. Measure dimensions, duration, FPS, codec and color metadata; verify import into current Resolve. Keep originals before compatibility conversion.

Per take retain provider/model, prompt revision, settings, reference roles/order/hashes, task ID, parent Draft ID, created_at, status/error, usage/cost, local paths and acceptance decision. Compare by elapsed time, not frame numbers when FPS differs.
