# Production contract

Suggested project records, scaled to scope:
- brief: intent, audience, format, cash/time constraints, artistic nonnegotiables, delivery requirements;
- development: chosen treatment/script revision and open creative decisions;
- visual bible and asset manifest: IDs, versions, roles, provenance and approvals;
- shot plan: IDs, half-open edit ranges, action and sound intention, continuity dependencies;
- generation log: request IDs, route version, inputs, all takes, cost and selection reason;
- edit manifest: selected take, source in/out, output range, retimes/transitions and audio mapping;
- delivery/QC: actual file specs, inspected content, defects, master path and acceptance status.

Shot states: planned → inputs_ready → submitted → downloaded → technically_checked → artistically_accepted → integrated → delivered. Failure, revision and superseded states retain original evidence. A downloaded shot can fail technical checks; a technically valid shot can fail the story.

Frame ranges use [start,end) internally. Translate to the actual destination API convention and read back counts. Keep source FPS, timeline FPS and any retime explicit. A five-second provider minimum does not justify stretching a two-second action. Handles are labeled and trimmed.

Minimum generation record: shot_id, take_id, input_hashes, adapter_revision, request_id, status, source_path, source_timebase, actual_cost_or_unknown, rejection_reason_or_selection. A retry after uncertain submission first checks the existing request.

Minimum change record: requested effect, changed assets, old/new revision, dependencies invalidated, verification and rollback reference. If a face or wardrobe changes, flag connected shots rather than silently overwriting their references.

Treat a changed voice take as a dependency change too: identify affected lip sync, dialogue timing, picture edit and mix. Recheck only affected operations and their boundaries; do not silently reuse an obsolete speaking shot.

For a scene-level production trial, retain preparation, selection and repair time alongside all attempt costs. Count unique accepted edit seconds, not the sum of alternative usable takes. No accepted seconds means no accepted result; unknown costs stay unknown. A creator's platform credits or generation counts alone do not establish their rejection rate or total production cost.

For post: carry source color interpretation, timeline/output color space, alpha behavior and audio sample rate. Do not infer HDR from ten-bit encoding or a color grade from container tags. Sound requires performance, ambience, Foley/effects and music decisions; normalization alone is not sound design.

## Scene-batch production and finishing

Prepare only the dependencies required for the next selected scene, with a representative performance/identity test where the risk warrants it. Do not demand that every asset for the entire film exist before a concept or pilot can progress.

Keep scene blocks linked to script revision, shot IDs and shared descriptor/state versions. Store the exact compiled prompt and actual attachment map for every request; changing a master description must create a revision and invalidate affected future requests, not rewrite historical evidence. Compare small targeted changes when diagnosing a defect; count all billed attempts and human effort.

Assemble candidate shots early enough to expose missing eyelines, contact inserts, reactions or transitions. Request a pickup with its editorial purpose and acceptance criteria. Do not regenerate a whole sequence merely because one shot is missing. A folder's asset count is not the count of failed takes or accepted shots.

Inspect clip edges and preserve handles; trim defects at actual useful boundaries rather than automatically cutting a fixed half-second from everything. Stabilize picture timing before expensive final cleanup, voice synchronization and final mix. Preliminary sound and color can help editorial decisions earlier.

Prioritize defects visible in the intended delivery, including faces, hands, text and temporal instability. Small repair versus new generation is a measured effort/quality decision. Match source interpretation and neighboring shots before the creative grade; protect the existing accepted look. Final dialogue, scene ambience, specific effects and music must be reviewed together. A finished-looking gallery still is not a final scene or a conformable edit.

If a late edit changes timing, revisit only dependent cleanup, audio cues, lip sync and mix transitions. Deliver the master with its selected-take map and actual acceptance limits. Adaptation evidence: `E:/Krea_tren_AI/Knowledge/06_Sources/Hell_Grind_Transfer_2026-10-01.md`.
