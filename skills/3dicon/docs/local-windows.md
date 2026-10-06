# 3dicon in our shared tools

Installed for the user globally in Codex; usable across projects. Source:
`https://github.com/samyost1/3dicon`, pinned revision in `../UPSTREAM.json`.
The unmodified downloaded package is preserved in the snapshot named there.
The MIT license is kept in `../LICENSE`.

## Local runtime

- Canonical source: `E:/Krea_tren_AI/Tools/skills/3dicon`.
- Python: `E:/Krea_tren_AI/Tools/3dicon-runtime/.venv/Scripts/python.exe`.
- Launcher: `E:/Krea_tren_AI/Tools/3dicon-runtime/run_3dicon.py`.
- Config: `E:/Krea_tren_AI/Tools/3dicon-runtime/.env` (local credentials, not a skill asset).
- Existing FFmpeg: `C:/FFmpeg_exe/ffmpeg.exe`.

Run the launcher with an absolute output directory for the current project:

```powershell
& 'E:/Krea_tren_AI/Tools/3dicon-runtime/.venv/Scripts/python.exe' 'E:/Krea_tren_AI/Tools/3dicon-runtime/run_3dicon.py' --out 'E:/Krea_tren_AI/GamesDev/output/icons/example' animate --still 'E:/path/to/approved.png' --strategy event --energy calm --motion 'The latch opens once and closes again' --dry-run
```

The example is a dry run; replace the still with an existing actual path. It does
not call a model. Use the same launcher for the `still`, `animate`, `matte`,
`encode` and `verify` stages documented in SKILL.md. Do not install dependencies
into Toolkit, ComfyUI, voice or the bundled Codex runtime. Local dependency
versions are saved alongside the launcher in `requirements-lock.txt`.

The local config selects OpenRouter for both image and video, resolving the
upstream mismatch where the README says one key but image generation defaults
to direct OpenAI. Configure OPENROUTER_API_KEY locally when generation is
requested; do not print its value or put it in project notes. No credential was
added during installation. Model availability and prices must be checked at
execution time; numbers in upstream prose are observations, not our guarantee.

Matting uses the CPU runtime here. Its model weights are downloaded on first use;
the installation check does not invoke matting or a paid API. A successful help,
dry run or sample-file check does not prove a complete newly generated icon.

## Use in games and interfaces

The output is raster animation with a 3D appearance, not a mesh, GLB or rig.
Useful for inventory, outfits, accessories, personality/emotion badges and menus.
For Godot, test the actual import/playback path; export alpha PNG frames for a
SpriteFrames resource or an atlas when needed. Do not assume an animated WebP
automatically plays as an animated Texture2D. Keep a static icon alternative.

Keep the upstream still and motion review stages unless the user already
specified or approved those exact choices. For image editing in Codex, use the
available image-editing tool when required by its higher-level instructions,
then pass the resulting approved still to this pipeline. Apply subsequent image
and video stages according to the tools and authorizations of that task.

Local code adjustment: authenticated OpenRouter polling is limited to its HTTPS
origin; bearer credentials are not attached to off-origin unsigned video URLs.
No request was sent to test an account during setup.
