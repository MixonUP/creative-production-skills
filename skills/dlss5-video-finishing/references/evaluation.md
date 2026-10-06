# Controlled recipes and acceptance

These are **local trial designs**, not validated presets. Use only the recipe that answers the user's request. Research/skill-authoring tasks do not execute them automatically.

## Build a fair comparison

Choose a short representative source with face/skin, fine fabric or hair, motion and a difficult light transition; include a hard cut only when testing cuts. For a quick trial, 3–5 seconds is usually enough to reveal an obvious failure, not to certify a film. Record source hash, frame range convention, source/working/output colour spaces, FPS, dimensions and audio. Keep one original reference, one matched-pipeline bypass and one NR candidate.

The matched-pipeline bypass distinguishes NR from resizing, colour transforms, denoising, codec differences and exposure changes. Assess at the same dimensions and display scaling, preferably with lossless/intraframe intermediates. Check raw result and an exposure/contrast-matched comparison; a simple tonal improvement may be achievable by ordinary grading. Do not describe plausible newly synthesized texture as recovered ground truth.

Record plugin/node commit, exact runtime hashes, driver/GPU, all non-default controls, input/output paths, wall time, peak memory if measured, warmup/history/scene-cut behaviour, and logs for the actual run window. Capture one variable change per candidate rather than an unbounded grid.

## Skin and natural detail

Begin with developer defaults at native size. Compare bypass, a restrained mix (for example 0.25 or 0.5), and full mix; those values are exploration points, not recommendations proven on this footage. If tone is doing most of the work, isolate Local Tone while keeping structure fixed. Then adjust structure and skin separately. Compare auto-mask off/on only if skin changes are needed.

Inspect eyes, teeth, hairline, moles, age, expression, skin pores, jewellery, text and fabric. Check moving close-ups and occlusions, not only a still. Reduce strength/mix or use a tracked local blend if identity shifts, edges crawl or pores look painted. Preserve logos/text with a separate matte when needed. Reject a superficially sharper result that changes identity or damages motion.

Reddit suggestions to add a skin-texture model before NR are an optional hypothesis: the pre-pass can invent detail and create a two-model feedback effect. Compare source, pre-pass alone, NR alone and their combination before adopting it. Do not install a texture model as an obligatory dependency.

## CGI/composite relighting

From the CloutVFX lesson, the transferable idea is to provide a deliberate lighting cue before the neural pass. Our independent trial layout:

`foreground + editable matte → colour alignment → optional local gradient/rim cue → merge over background → one NR pass → controlled source/result blend`.

The lesson uses Magic Mask and creator-specific nodes. Their availability/license is not established for our Free host. Recreate the **intent** with existing polygon/ellipse masks, a gradient, ColorCorrector and restrained Glow when appropriate; this is not an exact reproduction of the creator's proprietary macros. If exact reproduction is requested, identify missing assets first and preserve the supplied graph.

Compare four candidates only when necessary: composite baseline, conventional lighting alone, NR alone, cue+NR. A cue generated after NR cannot guide that already evaluated pass. Place final aesthetic grading later as a deliberate choice. Check shadow direction, local light wrap, geometry, moving edges and every opening frame after a cut. Treat ray-tracing/relighting language in demonstrations as appearance claims, not proof of physical lighting simulation.

Use NR as a lighting reference for manual grading if its temporal changes fail acceptance. That is a useful reference outcome, not a successful final DLSS render.

## Combine with the existing Topaz

Topaz is the existing upscaling/restoration baseline; DLSS NR addresses a different change. Do not replace a working tool because another looks more advanced.

If the request is only more natural shading at current size, try NR alone. For a required 2x output, compare **Topaz only**, **NR→Topaz**, and **Topaz→NR** with the same final dimensions, source timing and comparable settings. The two orders are hypotheses: Topaz may amplify NR artifacts, while NR after scaling may alter recovered or synthesized fine detail. The larger NR stage costs more memory/time.

Use standalone Topaz with Resolve Free as already established. Do not assume its installed OFX version is usable on Free. Avoid repeated H.264 generations; prefer the established high-quality intermediate route and explicitly preserve colour range and audio. The previous 21.09 Proteus result is historical evidence, not a DLSS comparison.

## Temporal problems and delivery

Watch the actual candidate at normal speed, reduced speed and selected consecutive frames. Look for lighting pumping, new pores flickering, boiling texture, ghosting, matte seams and cuts carrying the previous image. Static frame scores do not measure these well. A temporal metric without motion compensation can punish legitimate motion.

If unstable, first lower or localize NR and examine history handling. Deflicker/temporal denoise from tutorials may be Studio-only or soften motion; check actual availability before proposing them. Do not solve this by updating Resolve, purchasing Studio, or upgrading dependencies without a separate request. When no acceptable repair exists, bypass problematic shots.

Before export: Processed view, intended mix, no debug divider, correct shot range, native FPS unless retiming was requested, and original audio mapping. Afterwards: ffprobe dimensions/FPS/frame count/duration/colour tags/audio streams; full decode for errors; check sync at head/tail and shot boundaries; reopen the project and inspect the chosen clip if a reusable project is delivered.

Acceptance record: `technical_pass`, `identity_pass`, `temporal_pass`, `look_preference`, `runtime_cost`, `decision`, `scope`, `remaining_uncertainty`. Use unknown when unobserved. A successful EvaluateFeature call establishes runtime activity; exported pixel change establishes effect; only viewing the relevant shot establishes creative acceptance.
