# Локальное состояние — проверено 30.09.2026

| Компонент | Подтверждение | Граница знания |
|---|---|---|
| Topaz Video | `C:/Program Files/Topaz Labs LLC/Topaz Video/Topaz Video.exe`, FileVersion 1.7.0.0 | Установленная версия, не рекомендация обновлять |
| CLI | В той же папке `ffmpeg.exe`, `ffprobe.exe`; фильтры `tvai_up`, `tvai_fi`, `tvai_pe`, `tvai_cpe`, `tvai_stb` | Справка успешно прочитана без inference |
| Обычный FFmpeg | `C:/FFmpeg_exe/ffmpeg.exe` и `ffprobe.exe` | Доставка/QC; фильтров Topaz здесь не предполагаем |
| Определения моделей | `C:/ProgramData/Topaz Labs LLC/Topaz Video/models` | JSON не доказывает наличие нужных весов/доступ к модели |
| Resolve | Free 21.0.3.7; существующий `resolve_krea` MCP | Версия закреплена пользователем, обновление запрещено |
| GPU | RTX 4090 24 GB, одна карта | Память может быть занята Comfy/обучением; не останавливать их |

`TVAI_MODEL_DIR` и `TVAI_MODEL_DATA_DIR` не заданы на Process/User/Machine уровнях в снимке. Для отдельного CLI задавать только окружение дочернего процесса, сверив фактическую папку definitions и weights. В models обнаружены 658 файлов `.tz3`; это не проверка полноты любой конкретной модели. Не читать/копировать `auth.tpz`, `.lic`, аккаунт и токены в отчёты.

Есть исторические записи Video AI 7.0.0 и Gigapixel 7.2.2. Не смешивать их с работающим **Topaz Video 1.7**: нумерация продукта началась заново. `minAppVersion` внутри старых model JSON также может относиться к прежней линейке; не делать вывод о несовместимости простым сравнением 1.7 < 7.0.

## Наш успешный исходный рецепт

21.09.2026: `Films/Testfilm/Resolve/Seedance_Finish_v001/Source/seedance_original.mp4`, 992×432, 24 fps, 265 кадров, AAC 32 kHz. Фильтр:

```text
tvai_up=model=prob-4:scale=2:device=0:vram=0.35:download=0:details=0.1:blur=0:noise=0:compression=0.1:blend=0.2
```

Это зафиксированные параметры одного успешного ролика, не универсальный пресет. Остальные параметры тогда явно не зафиксированы: не выдавать реконструированную команду за побайтовый оригинал. Текущие defaults доступны в snapshot справки.

Результаты в `Films/Testfilm/Resolve/Seedance_Finish_v001/Exports/`:
- `Seedance_Topaz_2x_Master.mov`: 1984×864, 24 fps, 265 кадров, ProRes 422 HQ 10 bit + PCM 48 kHz.
- `Seedance_Topaz_2x.mp4`: H.264 CRF16 + AAC256k, те же размеры и число кадров.

Свидетельства: `topaz_render.log`, `Preview/topaz_test.log`, `resolve_import.json` рядом; карточка `Knowledge/06_Sources/Film_MCP_Stack_2026-09-19.md`. Декодирование проверено, контактные листы осматривались. Полная пользовательская оценка движения и звука не записана. Исторический heartbeat успешен; текущий аккаунт не проверялся. Интерполяции и очистки звука в этом проходе не было.

В README v001 осталось раннее «импорт НЕ выполнен». **Поздняя запись 21.09 09:54 и resolve_import.json подтверждают импорт** в `Testfilm_MCP / Seedance_Topaz_2x_24fps_v001`. История сохраняется, свежий вывод берётся из поздней записи.

Последующий `Seedance_Finish_2K_v002` — масштабирование 1984→2048 Lanczos, внешняя запечённая коррекция и обработка звука, **не новый Topaz inference**. Финальная сборка — `Seedance_2K_Finish_v003`, четыре плана 63/86/51/65 кадров. Не путать её с неудачной v002 сборкой.

Свежие свидетельства: `E:/Krea_tren_AI/KnowledgeData/snapshots/2026-09-30/topaz-skill-033054/`. Файлы `model-definitions.json`, `tvai_*-help.txt`, `encoders.txt`, `local-installation.json`; определения захешированы, активация/веса новых моделей не тестировались.
