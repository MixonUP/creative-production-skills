---
name: film-toolchain-maintenance
description: Install, verify, compare, upgrade or retire Blender/Fusion/ComfyUI extensions with versioned evidence and rollback. Use for film toolchain maintenance and scoped build-versus-buy decisions; not automatic monitoring or unrelated application management.
metadata:
  version: "1.0.0"
---

# Maintain capabilities with evidence

Read [maintenance operations](references/operations.md). The canonical installation/decision registry is `E:/AI_films/Tools/FilmExtensions/registry.json`; configurable route preferences are in `recipes.json`. Read only affected tool cards and current evidence. User choices override earlier recommendations. Distinguish deferred/rejected tools from unavailable tools.

## Install or change one capability

Inspect actual host versions, active jobs, existing files and local modifications. Reuse the existing app integration. Resolve official release/commit and requirements, stage into a new directory, retain download URL and SHA-256, inspect relevant installer/registration behavior, and preflight dependencies. A hash is provenance/integrity evidence, not a security certification.

Preserve previous preferences and touched component files. Avoid broad dependency upgrades when a narrow install suffices. A running process may retain old code; do not restart training or unrelated queues. Report active-session versus next-start availability. Respect the user's current installation authorization without repeatedly asking for the same reversible steps; purchases/accounts are separate from having an installer.

After change, verify files, registration, a small meaningful function and the actual task when feasible. A probe cannot certify creative quality. Keep the evidence and scope in the registry. Record blocked stages precisely, including missing weights, host/API limitations or activation.

## Improve or replace

Compare incumbent and challenger on the same relevant task and comparable budget. Establish must-pass conditions before scoring: host compatibility, required output, project reopenability and acceptable artifacts. Then compare quality, control, manual effort, runtime and cost. Do not invent scores. A newer model or feature list alone is not an improvement.

Adoption requires a real test artifact and a stated scope. Rejection preserves its reason; supersession names the replacement and affected use cases. Keep old versions needed by old projects. Registry edits are recommendations/history; they do not uninstall binaries. Check reverse dependencies and exact paths before any removal. A rollback of the registry alone does not restore host configuration.

## Own implementation

First compare native functionality and maintained open tools. If a recurring gap remains, choose a bounded macro/Fuse/add-on/node/script with explicit inputs, parameters, bypass and acceptance cases. Track original code versus upstream adaptations and retain licenses. Never claim a procedural approximation replicates a proprietary system without measurement. Stop expanding an MVP when a simpler solution meets the task.

## Maintain skills

Canonical skill sources live in project Tools/skills; runtime copies live in the user's Codex skills directory. Validate metadata and references, check source/runtime drift, backup prior runtime, then sync and verify hashes. Test decisions with realistic cases; wording validation alone is insufficient. Put volatile versions and creator claims in tool cards, not universal instructions. Preserve unrelated invocation policies. No background updater or scheduled monitor follows from a maintenance backlog.
