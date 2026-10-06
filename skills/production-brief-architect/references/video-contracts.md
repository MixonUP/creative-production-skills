# Video brief: a filmable and editable sequence

## Choose the form and outcome

Identify whether this is narrative film, ad, product demonstration, music video,
social short, documentary/explainer, game trailer or one-shot study. State audience,
distribution/aspect constraints, intended feeling or information, and the decisive
viewer takeaway. A CTA belongs only where the actual format needs it.

Distinguish recreation, adaptation and original work inspired by particular properties.
Inspect accessible media before claiming observation. An article/transcript supports
what was said, not lens metadata, visual quality or a frame-by-frame viewing.

## Story, performance and edit

Connect beats through cause and consequence. Each shot should change information,
emotion, relationship, attention or rhythm. Prefer specific playable behavior over
"be cinematic" or a list of handsome images. Preserve user-supplied speech exactly
when requested. Estimate spoken duration from a read/recording where available;
otherwise mark the estimate and leave timing margin.

Plan the rough assembly early. Cover meaningful look/action/reaction and edit points
without generating redundant angles. An uninterrupted take and an invisible cut are
different promises. Simplify choreography, extend time or introduce a motivated cut
when one short generation cannot plausibly contain the requested actions.

## Shot contract

For each relevant shot record:

- stable shot/scene ID and narrative purpose;
- edit interval [start, end), selected duration, intended cut/transition;
- character/costume/location/prop reference IDs and state on entry;
- first composition and last composition: size, placement, depth, eyeline, occlusion;
- action beats, contacts, pauses and emotional intention;
- camera viewpoint, path or locked position, framing change and motivation;
- screen direction, action axis and continuity dependencies;
- light direction/source size, exposure relationship, palette and atmosphere;
- dialogue/sound/music events, perspective and continuity across the cut;
- needed source images/previs/plates/voice and role of each;
- generation/control route, unresolved provider capability, likely failure and fallback;
- visible acceptance and final status.

Not every shot needs a numeric focal length. If one is useful, state the sensor/FOV
assumption and treat it as a production choice. Moving camera, zoom and crop have
different effects. A prompt cannot make an unverified "camera lock" guarantee.

## Time arithmetic and sound

Specify delivery frame rate/timebase when known; keep source and timeline rates
separate. At constant FPS, frames correspond to intervals, not a duplicate inclusive
end frame. For straight cuts, edit durations sum to total duration. If listed durations
are source clip lengths and clips overlap in dissolves, subtract each overlap once;
do not subtract it again from already positioned timeline intervals.

Keep source generation duration, selected edit duration, handles and retiming distinct.
Do not pad the story merely to meet a model's minimum output length. Music structure and
dialogue must fit the selected edit, not just individual clips in isolation.

Audio has its own event map: speech, breaths, steps, contacts, ambience, musical change
and silence. Note which sound is in-world, off-screen or editorial. Keep dialogue masters
and stems where editability matters. Generation with audio, TTS, lip-sync and final mix
are distinct routes. Define cancellation/re-timing effects on lip-sync where relevant.

## Consistency without frozen acting

Record invariant identity, costume/prop construction and world geography separately
from state changes: dirt/wetness, open/closed props, moved objects, emotion and time of day.
A change across a cut is allowed when the story explains it. Avoid using an entire
reference library indiscriminately; select only assets the shot needs.

A consistency plan needs a representative angle/action test before scaling. An identity
sheet or LoRA filename alone does not prove continuity. LoRA, depth, motion reference,
first/last frames and face animation are not universally interchangeable capabilities.

## Compile two different prompts

The production-agent prompt owns the complete workflow, files, assets, edit, QA and
handoffs. The video-model prompt describes only the intended shot and the references
the selected route can consume. Do not send the entire production bible to a model.

For the shot prompt use:
subject and stable identity → concrete action with temporal order → spatial relations
→ camera → light/material/atmosphere → necessary continuity → sound if supported.

Translate attachment IDs, durations and optional negative prompts with a verified
provider adapter. If no provider is selected, supply a semantic shot prompt and list
the required capabilities; do not fabricate JSON endpoints or promise exact timing.
Use only essential negative constraints grounded in observed failure or user direction.

## Production and acceptance

Choose the smallest representative risky moment before a full batch: a hand contact,
an identity-changing angle, a multi-character exchange or an exact camera move.
Then concept/asset preparation → rough timing/animatic where useful → draft shots →
assembly → targeted repair → final sound/color/finishing → master QC.

Keep scene, shot and master acceptance separate. Review starts/ends, contacts, maximum
motion and cuts; inspect actual normal-speed playback. Technical metadata cannot certify
good acting, emotional clarity or consistency. A preview cannot certify the requested
delivery format. Record unavailable viewing/listening capability explicitly.

Delivery states include planned, prepared, submitted, received, technically checked,
visually/audibly reviewed, selected and user accepted. Do not advance status because
the generating API returned success. Preserve source media and accepted revisions.

