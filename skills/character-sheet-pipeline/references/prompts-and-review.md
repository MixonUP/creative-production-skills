# Reference prompts and review

These are editable patterns, not a classifier or an API specification.

## Neutral master reference

Preserve the identity, proportions, intentional asymmetry, clothing and materials
of the supplied image. Show the complete subject in a stable front view, with the
front-facing anatomical plane parallel to the image plane. Use the neutral pose
suited to this anatomy and the target rig. Keep important joints and extremities
visible. Neutral background, even diffuse illumination, no dramatic perspective,
rim lights, baked highlights, floor clutter or cropped parts.

Specify concrete pose requirements for this character. Do not apply humanoid palms,
two legs, a fixed arm angle or equal silhouette widths to every creature.

## Isolated component

From the same accepted master image, isolate [component]. Keep its orientation,
proportions, visible details and colour. Do not add equipment or invent decoration.
Use neutral lighting and the same front camera. State whether paired pieces must
appear together or as separate left/right components. Preserve intentional differences.

## Side/back

Keep the accepted subject and rest pose. Show an exact [left/right profile/back]
reference with consistent scale. List ambiguities in hidden geometry before proposing
details. Cross-check features that appear in several views; different attractive
images are not automatically a consistent multiview set.

## Review record

Record source/candidate paths and hashes; view and component; expected anatomy and
pose; observed identity/camera/framing/lighting failures; verdict; next action.
Use qualitative angle estimates unless a calibrated measurement exists. A vision
judgement is not a geometrically calibrated orthographic camera.

- Pass: essential identity, anatomy, pose and view requirements are met.
- Soft failure: minor mismatch; describe what downstream work it affects. Keep as a
  candidate or usable-with-issue where the current task permits; do not invent owner approval.
- Hard failure: missing anatomy/essential parts, changed identity, wrong view or a
  major pose change. Correct the named failure within the available task budget.

Repeated failure should change the approach or expose the unresolved choice. Do not
silently purchase repeated generations or substitute a new provider. Keep rejected
attempts and selected sources distinct. Optional video is a motion reference, not
verified skeletal animation.

