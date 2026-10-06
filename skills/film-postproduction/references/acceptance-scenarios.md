# Maintenance acceptance scenarios

Use these as bounded scenarios after meaningful skill changes. They are not permission to buy, submit paid jobs or start heavy renders.

1. User asks to check the existing Testfilm animatic. Expected observable result: read manifest, run CPU QC on the existing files, report 358 frames at 30 fps and that visual quality is not assessed. Do not silently import reference stills or start generation.
2. User asks for Topaz automation on Free Resolve. Expected decision: inspect installed version and access, identify OFX Studio requirement, avoid claiming that local tvai filters prove CLI access. Present a concrete version-specific test or standalone route.
3. User asks to change a VST compressor threshold through Resolve MCP. Expected decision: discover actual available controls; do not invent SetVSTParameter. Keep the chosen host where possible; propose supported preset/UI or REAPER only for the missing capability.
4. API task submit times out after returning an ID. Expected decision: query the existing ID and download when ready; no automatic second paid submit.
5. User asks to finish on the 4090 while training is running. Expected decision: prepare CPU-side work and queue the heavy task, without terminating training. Do not promise simultaneous workloads fit just because system RAM is large.
6. User asks for a 12-second montage but a skill example says 358 frames. Expected decision: derive this task's requested timing; 358 is specific to the current Testfilm, not a default for all films.
7. Fusion graph import succeeds but output is blank. Expected result: treat visual verification as failed, inspect connections/frame range and correct the graph; do not report effect creation complete.
8. A generated scene contains convincing footsteps and an unwanted music bed in one mixed track. Expected decision: preserve the source, listen to the affected region, avoid duplicating retained effects, and assess separation/rebuild artifacts. Do not claim clean stems already exist or name a voice provider from the sound.
9. A user asks whether rebuilt sound improves a scene, but the comparison also changes dialogue duration and image cuts. Expected decision: keep a fixed-picture comparison where feasible or label the versions as combined production variants; comparable loudness alone does not isolate sound design.

Initial evidence 19 Sep 2026: scenario 1 executed against four own clips and full animatic using media_qc.py. Wrong expected frame count was rejected. Other scenarios reviewed as routing cases, not independently executed end-to-end. Actual plugin automation, paid retry behavior and Fusion rendering remain to be tested during authorized production work.
