---
name: formula-driven-production
description: Find, derive and validate mathematical models and algorithms for procedural generation, geometry, motion, materials, sound, video and AI controls. Use when creative behavior needs controllable parameters, a reference needs an implementation, or an existing formula fails the task.
metadata:
  version: "1.0.0"
---

# Formula-driven production

Turn the user's desired behavior into an appropriate mathematical model and working
implementation. Select the mathematics from the problem. A formula, algorithm,
constraint system, probability model or measured lookup table may be the right answer.
Do not force every creative task into a closed-form equation or a fixed formula bank.

## Define the problem before choosing mathematics

Identify the observable effect, controllable inputs, required outputs, references,
units, time/coordinate conventions, target tool/model and success criterion. Separate
hard constraints from artistic preferences. Resolve ordinary choices with explicit
assumptions; ask only for a missing decision that materially changes the result.

Read [model selection, research and derivation](references/method.md) for the core
workflow. Choose support by the current problem, not by the original tutorial:
- [Procedural generation](references/procedural.md): distributions, noise, geometry,
  spatial constraints and parameter fitting.
- [Motion, sound and video](references/media.md): representative models and traps;
  use them as examples, then search beyond them when the task differs.
- [AI/tool adapters](references/ai-adapters.md): turn a verified model into code,
  supported parameters, control artifacts or a clearly approximate prompt.

The supporting examples are an open starting set. Prefer the simplest model that
captures the defining behavior. Record when richer physics or a different family is
needed. Reuse the project's existing implementation when it already solves the task.

## Find, adapt, derive or fit

Find established models in primary sources by mechanism and assumptions. Record
the exact source/section and distinguish the published relationship from local
notation, derivation and tuning. Do not trust a source merely because it looks mathematical.

When adapting a model identify the changed assumption and its consequence. Derive
new relationships from constraints when needed; fit parameters from data when useful.
Do not call an arbitrary curve a new physical law. Mark parameters measured, derived,
proposed or fitted. Check dimensions, boundary/initial conditions and limiting cases.

For nontrivial reusable results use [FORMULA_CARD_RU.md](assets/FORMULA_CARD_RU.md).
Small tasks need only the relevant fields beside the code. An unavailable coefficient,
unreadable video symbol or hidden source implementation remains unknown.

## Implement and challenge the model

Choose an analytic/discrete closed form when sufficient. Otherwise specify solver,
step size, tolerances and stability limits. Distinguish audio sampling, simulation
timestep, animation FPS, world units and normalized image coordinates. State whether
vectors are local/world/camera space and whether angles are radians or degrees.

Expose controls tied to intent: density, scale, smoothness, spacing, decay, travel
time, brightness or contact strength. Document the mapping from each art control to
mathematical parameters and any correlations it introduces.

Run a minimal representative case and meaningful checks: endpoints, boundedness,
distribution, geometry constraints, conservation where applicable, sampling, or
behavior under a different step size. Use an independent calculation, alternative
implementation or known limit. Tests that repeat the same mistake are not validation.

[scripts/formula_lab.py](scripts/formula_lab.py) provides a dependency-free CPU lab
for a few representative families; read [lab.md](references/lab.md). Extend or replace
it for other problems. It is not a general symbolic proof system or a required renderer.

When a model fails, identify whether the cause is a bad assumption, equation, numeric
method, parameter choice, integration or artistic mismatch. Change that layer and
retain evidence. Do not hide instability with clamps that invalidate the intended model.

## Adapt to real tools and AI models

Inspect the actual schema, installed adapter or official documentation. Classify
each intended control as supported input, externally generated reference, approximate
prose instruction or unsupported. Record the distinction. Never invent API fields,
transfer another model's parameter scale blindly, or imply that a formula in a media
prompt will be executed exactly.

For a code agent provide the model, units, data shapes, minimal example and tests.
For a compatible generator export curves, masks, geometry, depth, pose or previs as
needed. For prompt-only systems describe the observable effect and verify output
empirically. Preserve the user's chosen tools; proposing a mathematically attractive
alternative does not authorize a model migration, paid run or training job.

## Deliver and retain the result

Deliver the model and its explanation, editable parameters, code/control artifact,
sources and tests. Distinguish mathematical argument, numerical verification,
perceptual review, integration and user acceptance. A correct equation does not prove
good art, a finished product or compliance by an opaque AI model.

Route accepted outputs to existing project production skills where useful: procedural
audio, game audio, animation/blockout, VFX or film postproduction. Those integrations
are not prerequisites to derive or test a model.

Save reusable knowledge in the project's canonical cards and evidence area: exact
recipe, source URLs, versions/hashes, findings, failures, limits and next experiment.
Append corrections without rewriting historical evidence.

User-ready prompt: [MASTER_FORMULA_BRIEF_RU.md](assets/MASTER_FORMULA_BRIEF_RU.md).
Source lineage and researched examples: [sources.md](references/sources.md).
