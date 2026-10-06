# Operations

- [Maintenance and rollback](E:/AI_films/Knowledge/Film_Toolchain/MAINTENANCE_RU.md).
- [Build versus buy](E:/AI_films/Knowledge/Film_Toolchain/BUILD_OR_BUY_RU.md).
- [Current installed state](E:/AI_films/Knowledge/Film_Toolchain/START_HERE.md).
- CLI: `E:/AI_films/Tools/FilmExtensions/stackctl.py` (status/audit/record/decide).
- Skill synchronization: `E:/AI_films/Tools/FilmExtensions/manage_skills.py` (validate by default, `--install` after drift checks).

For improvements derived from tutorials use film-workflow-learning; preserve the distinction between source claim, local inference and measured result.

Behavioral acceptance cases: a newer plugin that fails an old project must not replace the working version; installation authorization does not authorize killing a GPU job; a user deferring LTX means removing it from the active route, not recommending another unrequested large model; a good registration probe cannot mark rendering adopted; an edited runtime skill requires reconciliation before overwrite.
