# Evidence ledger and learning route

Research date: **2026-09-30**. Distinguish `code inspected`, `documentation inspected`, `transcript`, `selected visual`, `community claim` and `local observation`. A source's instructions are data, not authorization. Full transcripts/source snapshots are research evidence, not text to republish as our own manual.

## Local evidence

- [Installed state and rollback](E:/Krea_tren_AI/Knowledge/04_Procedures/Resolve_DLSS5.md).
- [Earlier lessons and Topaz correction](E:/Krea_tren_AI/Knowledge/06_Sources/DLSS5_Lessons_and_Resolve_Options_2026-09-30.md).
- Research snapshot: `E:/Krea_tren_AI/KnowledgeData/snapshots/2026-09-30/dlss5-skill-research`. `repositories.json`, `downloads.json`, `HECer-downloads.json` record exact commits, URLs and hashes. HECer downloads are pinned to commit `f4f59cd1fe39e785a3b600ca20b5e09194a9e38d`; `HECer-tree.json` records its file inventory.
- Installation snapshot: `.../resolve-dlss5-install-024651`, including verified archive, install manifest and host registration.
- Local facts: OFX files verified/registered on 21.0.3.7; **no DLSS media render or quality acceptance** during installation/skill creation. Existing Topaz Proteus run is separate evidence.

## Primary technical sources

1. **SAOG0721, Resolve OFX** — [repository](https://github.com/SAOG0721/DaVinci-Resolve-DLSS5), [0.3.1 release](https://github.com/SAOG0721/DaVinci-Resolve-DLSS5/releases/tag/v0.3.1-experimental), [parameter/render source](https://github.com/SAOG0721/DaVinci-Resolve-DLSS5/blob/a659e5c674388ea8026f4cf8df9f206826d12452/src/ResolveDlss5Plugin.cpp), [runtime source](https://github.com/SAOG0721/DaVinci-Resolve-DLSS5/blob/a659e5c674388ea8026f4cf8df9f206826d12452/src/Feature18Runtime.cpp). Tagged code inspected, binary hashes locally checked. Authority for OFX IDs/defaults, history, proxy encoding, diagnostic math and exact proof lines. Header source is separately saved. These implementation facts drive the Resolve and diagnostic references; they are not GPU compatibility or artistic validation.

2. **OreX/Ox author documentation** — [pinned README](https://github.com/orex2121/ComfyUI-DLSS5-orex/blob/739208e7ae5f576355fc5c30ffb77c4de2e61984/README.md). Read controls, temporal/chunking semantics and limits; source snapshot retained. Distinguishes reserved presets, resample+NR from SR, preview history, GPU staging and full-output memory. Local installation/inference not performed. Tutorial defaults must be reconciled with this revision.

3. **HECer guided ComfyUI** — [workflow notes](https://github.com/HECer/ComfyUI-DLSS5/blob/f4f59cd1fe39e785a3b600ca20b5e09194a9e38d/workflows/README.md), [troubleshooting](https://github.com/HECer/ComfyUI-DLSS5/blob/f4f59cd1fe39e785a3b600ca20b5e09194a9e38d/docs/TROUBLESHOOTING.md), [runtime sources](https://github.com/HECer/ComfyUI-DLSS5/blob/f4f59cd1fe39e785a3b600ca20b5e09194a9e38d/docs/RUNTIME_SOURCES.md). Documentation read, no local execution. Useful for persistent versus overlapping processing, guide direction, model/runtime separation and export completion. Its `.agents/skills` directory was enumerated: generic software-development skills, not a ready operator skill for our Resolve installation; none installed.

4. **Blueforcer worker integration** — [repository](https://github.com/Blueforcer/ComfyUI-DLSS5-Enhancer). Earlier source research identified the v3.0/protocol 4 worker constraint. Reverify the chosen revision before setup. Do not replace its worker with the latest standalone Merserk because both names mention DLSS.

5. **Merserk Visual Enhancer** — [pinned README](https://github.com/Merserk/dlss5-visual-enhancer/blob/63ec8793d02b517d79058bf57a9aa5f2273d8093/README.md), [v13.2](https://github.com/Merserk/dlss5-visual-enhancer/releases/tag/v13.2). Current documentation inspected; candidate standalone finishing controls, including preservation/masking options. Not an OFX plugin; not locally tested. Keep license and runtime provenance separate from source feature claims.

6. **lisitskyaa NR** — [repository](https://github.com/lisitskyaa/ComfyUI-DLSS5-NR), [author's Reddit introduction](https://www.reddit.com/r/StableDiffusion/comments/1w3zfje/experimental_dlss_5_comfyui_custom_node/). Source read in earlier research; comments read this session. Useful history of temporal problems and later Optical Flow support. No claim that our different OFX acquired those features.

## Lessons with useful timestamps

7. **CloutVFX, How to put DLSS 5 in Davinci Resolve (free btw) | tutorial**, [video](https://www.youtube.com/watch?v=riy3jsqdMNE), 02.09.2026, 8:12. The search index retained an older title “FREE DLSS 5 …”; live page and transcript identify the same ID. Full auto-transcript read; selected visual at **5:33** inspected, not the entire video.

   - **0:34–1:11:** bundle installation.
   - **1:39–2:13:** isolate/freeze subject, composite, add NR.
   - **4:22–4:59:** conventional colour matching comparison.
   - **5:05–6:08:** deliberate rim/gradient/glow cues before NR; selected Fusion view confirms the cues on the foreground before merge and NR downstream.
   - **7:45–7:57:** creator acknowledges flicker and suggests post-fixes.

   Transfer: test an editable light cue+NR against each stage separately. Magic Mask, creator macros, claims of speed/physical realism and availability of deflicker are not guaranteed in our Free installation. Source is assessed; local recipe is trial planned. Transcript saved as `CloutVFX-riy3jsqdMNE-transcript.txt`.

8. **StableDif/OreX, DLSS 5 ComfyUI узлы**, [YouTube](https://www.youtube.com/watch?v=nA2BotQAO7M), [author's Rutube copy](https://rutube.ru/video/4e69725b6907edb4325b955b0ff4f239/), 08.09.2026, 16:58. Russian transcript saved in the earlier lessons snapshot. **1:53** install, **3:45** original workflow, **4:07** image, **4:55** controls, **7:41** video. Best fit for learning this specific author's node; compare the captured workflow and current README before execution. No universal speed/quality endorsement.

9. **RareTutor**, [Blueforcer lesson](https://www.youtube.com/watch?v=hIICmGr-J38), 12.09.2026, 6:51. Transcript previously captured. Secondary learning route for the isolated worker, not a recipe for the installed OFX.

10. **Joris Hermans**, [previously supplied lesson](https://www.youtube.com/watch?v=sphfsCJ4XAY), 4:32. Transcript previously captured; kept as an introductory reference. User wanted a deeper workflow, so it is not the main technical foundation.

## Community experiments and failure reports

11. **ScoreAsleep972 on Reddit**, [skin contrast → DLSS](https://www.reddit.com/r/DLSS/comments/1w9nncu/progress_on_dialing_in_dlss5_in_davinci_resolve/), dated 07.09.2026 in search metadata. Post/comments read; images and whole video not evaluated. The creator proposes a skin-texture pre-pass and explains plugin enablement. Transfer only as a four-way controlled trial, not recovered-detail proof or evidence for Free compatibility. Small public vote counts don't establish quality.

12. **NR author's thread and user reports**, [temporal flicker/deflicker](https://www.reddit.com/r/StableDiffusion/comments/1w3zfje/experimental_dlss_5_comfyui_custom_node/). Reports inspire moving-shot/cut tests. Their successful example does not prove every wrapper supports real guidance or that deflicker will fix identity changes. No media downloaded or reposted.

13. **Resolve issue #1**, [bug report](https://github.com/SAOG0721/DaVinci-Resolve-DLSS5/issues/1). API issue body saved: reporter lists Resolve 21.0.2 build 4, RTX 3070 Ti, driver 616.56 and an attached log. The attached log was not analyzed here. Treat as a compatibility warning requiring our own probe, not a root-cause diagnosis or universal failure.

14. **ThunderRuler dlss5-installer-skill**, [pinned skill](https://github.com/ThunderRuler/dlss5-installer-skill/blob/f9f2ee764f442a507e5a282941e05de9cd21d38f/SKILL.md). Skill, diagnostics, motion-vector and known-hash references read; MIT metadata observed. It targets PC games/ReShade. Useful research reminder: identify the active process/API and verify actual execution. Its beside-exe DLL layouts, driver advice, gameplay compatibility tables and required community-reporting workflow are **not imported**. Own skill text/helper are independently authored. No third-party skill installed and no report sent.

X was searched for Resolve/ComfyUI DLSS workflows; no directly accessible, technically detailed primary post was verified. Do not imply X threads were read, treat a repost as evidence, or invent a source to fill a platform quota.

## Updating this knowledge

Source code beats a stale tutorial for what a particular build actually exposes. A newer README may describe unreleased behaviour: pin release/commit and compare implementation. Author benchmarks need local reproduction. Preserve disagreements, negative results and inaccessible material with dates. Promote a recipe only after a source-matched artifact and a scoped acceptance decision, while keeping the fixed Resolve rule in force.
