# Review rubric

| Layer | Diagnostic question | Evidence |
|---|---|---|
| Story | Can the intended viewer follow the change and its stakes? | Scene/action, actual audience responses if available |
| Performance | Does behavior belong to this character at this moment? | Full-speed performance and reaction timing |
| Visual language | Are composition, light and texture purposeful and coherent? | Shots in context and critical stills |
| Continuity | Do identity, space, state and screen direction survive cuts? | Adjacent shots and bible |
| Motion | Do contact, momentum, anatomy and camera obey the intended world? | Full playback plus event frames |
| Edit | Does shot duration support attention, information and emotion? | Rough/final assembly, not isolated clips |
| Sound | Are dialogue, space, impacts, silence and music working together? | Listening; stems and technical measurements |
| Color | Are sources interpreted correctly and intended matches maintained? | Actual pipeline and viewed output |
| Delivery | Does the actual file satisfy requested specs and decode? | Probe/decode, dimensions/FPS/count/audio and playback |

Severity: blocker prevents intended delivery/comprehension; major visibly harms essential performance or continuity; minor is repairable polish; suggestion is a creative alternative. Severity is consequence, not merely the number of malformed pixels.

A defect record has id, file version/hash, shot/time interval, category, severity, observation, evidence path, intended behavior, proposed repair, owner/status and recheck result. No made-up timecodes.

Possible technical checks include decode integrity, missing/black frames, unexpected freezes, cadence, duration, crop, color tags and clipping/loudness. Choose thresholds from delivery requirements and context. A purposeful hold, silence or black frame is not automatically an error. VMAF/PSNR comparisons need an appropriate reference and do not score original cinema or restored narrative information.
