---
name: godot-gameplay-production
description: Build and debug playable Godot systems with typed GDScript, scene composition and engine verification. Use for gameplay, interactions, saves or agent handoffs in a Godot project.
---

# Produce a playable change

Start from the project's actual engine manifest and existing scenes. For this workspace, read `E:/Krea_tren_AI/GamesDev/START_HERE.md`; use the pinned executable in `engine.json`. Do not infer APIs from another engine or a skill's version label.

Specify the player's action, observable result and failure case before implementing a new mechanic. Keep one owner for movement and physics; use Resources for authored data and signals for events across components. Do not create a large global framework for a single interaction. Autoload names and global `class_name` identifiers must not collide.

Inspect node paths, imported scene boundaries and signal connections before edits. Preserve `.uid` and import sidecars; keep behavior in wrapper scenes around imported GLB content. Prefer engine serialization over hand-writing complex PackedScene structures. When programmatically packing an instance, own its root but do not recursively replace owners inside the imported instance.

Run the smallest engine check that proves the change: import/parse, a behavioral scenario, then a rendered or playable check when appearance or interaction changed. Headless success proves neither visual quality nor GPU frame rate. Tests need a meaningful success marker and bounded execution; report engine errors even with exit code zero. Free temporary scene roots before quitting test runners.

For Codex/Claude collaboration use the file contract in `E:/Krea_tren_AI/GamesDev/Docs/CODEX_CLAUDE.md`. Another agent reviews a diff and evidence; avoid simultaneous writes to the same `.tscn`, `.blend` or shared project settings. Parallel sessions require separate working copies when authorized.

Completion evidence: changed scene/script, exact command and result, relevant interaction outcome, remaining untested platforms. Starter harness: `E:/Krea_tren_AI/GamesDev/Tools/verify_setup.py`. Its current checks cover the lab only; add a relevant check for a new mechanic instead of treating it as a full game test suite.
