# SECourses IndexTTS: подтверждённый контракт обучения

Проверено по установленному приложению **6.22**, commit `a776268d8c532e19836a1fa90f4e8d28b9ea20fe`, 04.10.2026. Главные файлы: `indextts/training/train_config.py`, `dataset_prep.py`, `docs/TRAINING_SELECTION.md`, `tools/train_lora.py`, `ui/generation_tab.py`, `indextts/runtime/vram_presets.py`. Перед новой работой сверить HEAD и прочитать изменившиеся поля. Patreon/поисковый индекс может описывать другую ревизию: например, извлечённая страница называла alpha 129, а текущие код и локальный README задают **128**. Приоритет для запуска — фактический сохранённый config установленной версии.

## Что действительно обучается

| Механизм | Назначение | Ограничение |
|---|---|---|
| Reference cloning | Получить голос из короткого аудио без изменения весов | Сильно зависит от референса и языка |
| GPT LoRA / DoRA | Адаптировать преобразование текста в речевые коды; в авторском варианте также обучается speaker projection | Не гарантирует произношение на новом языке или исправление плохой записи |
| Voice decoder adapter | Адаптировать следующий этап, преобразование кодов в акустическое представление/тембр | Может улучшить reconstruction и одновременно ухудшить настоящую генерацию |
| Emotion reference/vector | Изменить текущую подачу | Не заменяет устойчивую идентичность и актёрскую режиссуру |
| EQ / de-esser / room effect | Подготовить воспроизведение в сцене | Не восстанавливает пропущенные слова |

DoRA дополнительно разделяет адаптацию направления и величины весов. Статья DoRA не является доказательством лучшего голоса для любого датасета. В приложении DoRA — разумная стартовая гипотеза; LoRA может оказаться достаточно хорошей и дешевле. Выбор требует одинакового бюджета и речевого сравнения.

## План до запуска

Создать новую папку опыта и имя адаптера; сохранить voice card, план split, исходный manifest, модель/commit, software freeze и экспорт настроек UI. Иметь base samples, фиксированный набор новых реплик и достаточную VRAM под **все** стадии. Пресет 8 GB, используемый вместе с игровой LLM, не является доказательством бюджета обучения. Сначала проверить свободную память, не закрывать чужие GPU-процессы без соответствующего поручения.

`assets/secourses-config-overrides.json` — документированные **частичные** настройки для обсуждения/подготовки, не готовый обучающий запуск: там нет dataset_dir/name/model paths. Применять их к экспорту TrainConfig, подставлять абсолютные пути и проверять импорт конфигурации без вызова trainer. Обычный импорт этого контракта не загружает веса; не импортировать весь trainer ради проверки JSON.

Подтверждённые стартовые значения GPT:

| Поля | Значение | Как принимать решение |
|---|---|---|
| adapter_type, rank, alpha, dropout | dora, 128, 128, 0.05 | Начальная конфигурация автора; меньший rank — отдельный экономичный опыт, не автоматическое улучшение |
| target_attention / target_mlp / train_spk_proj | true / true / true | Дополнительные emotion layers и mel embed/head сначала false |
| train_full_modules_fp32 | true | Полностью обучаемые модули и мелкие обновления сохраняют точность |
| base_variant / mixed_precision | bf16 / bf16 | Проверить через VRAM preset текущего GPU |
| optimizer / learning_rate | adamw / 4e-5 | Не повышать LR из-за медленного прогресса без проверки датасета |
| lr_scheduler / warmup_steps | cosine / 200 | Сопоставить с общим числом **optimizer updates** |
| epochs / max_steps | 10 / 0 | Верхний бюджет, не обязательная длительность |
| batch_size / grad_accumulation | 1 / 1 | Изменение accumulation меняет число обновлений и обучение |
| gradient_checkpointing / max_grad_norm | true / 1.0 | Средства памяти/стабильности, не показатели качества |
| speaker_ref_mode / emo_ref_mode | other / follow_speaker | Другой clip того же speaker; сохранить реальный reference selection |
| val_split_mode / val_fraction | source / 0.05 | Проверить, какие записи фактически выделены; 5% недостаточно как абстрактное обещание покрытия |
| val_every_steps / val_max_batches | 250 / 0 | Полная доступная validation и epoch-end checks |
| save_best / save_train_state | true / true | Сохранить и лучший checkpoint, и возможность продолжения |

Оценка бюджета для одного GPU: updates/epoch примерно `ceil(число train clips / batch_size / accumulation)`, с поправкой на фактический loader, отбрасывание batches и пропуски. Не путать microsteps и optimizer updates. На крошечном датасете warmup 200 и early-stop min_steps 1000 могут занять весь эксперимент: сначала показать расчёт и скорректировать ограничения как отдельный опыт. Не повторять клипы ради красивого числа steps.

## Пилот и основной запуск

При разрешении запуска сначала 10–30 updates для проверки путей, finite loss, cache, сохранения и чтения checkpoint. Это наш технический smoke budget, **не** обучение принятого голоса. Для такого smoke явно отключить долгие decoder/sweep/speech-eval/probe стадии и подписать ограничения; не переносить их отключение в качественный production config незаметно. Затем новый полноценный run с validation и речевым сравнением.

Настоящее выполнение через UI: **LoRA / DoRA Training → dataset → новое имя → Start fresh → сохранение config → Start**. Эквивалент CLI установленного автора: из Vendor/SECourses независимым Python запустить `tools/train_lora.py --config <absolute-config.json>`. Не запускать автоматически при чтении этого навыка. Команды сборки данных/cache и её ASR тоже могут использовать GPU.

Early stopping этой версии учитывает validation loss и речевые probes. Defaults loss patience 6, min delta 0.005, min steps 1000 и min epochs 2. Возможна одна попытка с LR ×0.5 и grace 1000 updates внутри общего бюджета. Probe может отложить loss-stop, если речь ещё улучшается, или выявить рост word errors. Skipped/failed probe не означает PASS. Сохранять фактическую причину остановки.

`Weights only` начинает новый optimizer/schedule с выбранными весами; `Continue run` требует train state и восстанавливает состояние. Это разные опыты. Не продолжать старый optimizer после изменения speaker, базовой модели, rank/architecture или набора данных, называя это точным продолжением.

## Декодер: отдельный эксперимент и отдельная приёмка

В текущем полном training workflow decoder adaptation и decoding sweep по умолчанию включены. Планировать их дополнительное время/память. GPT training завершён ≠ весь workflow завершён. Для изучения эффекта можно заранее отключить вторую фазу и добавить позже, но точно записать это решение.

Default decoder: DoRA r128, alpha128, LR2e-4, 10epochs, codes=`real`. Не путать LR декодера с 4e-5 GPT. Mixed/GPT codes, EMA и averaging — дополнительные гипотезы, не обязательный пакет «максимального качества».

В авторском расследовании фиксированный prompt давал убедительный выигрыш на восстановлении реальных кодов, но ухудшал голос при генерации. Исправленный decoder trainer меняет same-speaker conditioning clip между target/epoch; настоящая приёмка проходит через text → generated codes → decoder → waveform. Этот вывод переносим как метод проверки, не как гарантию всех метрик автора на нашей машине.

Сравнить GPT adapter без decoder и с decoder при одной и той же реплике, reference, seed и остальных настройках. Авторский автоматический gate проверяет strengths 1.0 и 0.6, identity gain и регрессию речи; отвергнутые варианты сохраняет отдельно. «Auto» может ничего не подключить или связать approved decoder: проверить metadata, фактический путь и strength. Не убирать gate через `--no-test`, чтобы принудительно объявить удачный тембр.

## Выходы, которые надо сохранить

- `best/<name>_best.safetensors` (loss), `best/<name>_probe_best.safetensors` (speech probe), final/epoch candidates; не подменять одно другим.
- Saved run config, manifest + cache provenance, реальные optimizer steps, seed, logs/metrics, peak VRAM и время.
- `analysis/checkpoint_eval.json`, `analysis/probe/`, `analysis/speech_evaluation/report.json` и `.md`, `listening_review.html`.
- При наличии: `analysis/decoder_adapter.json`, `analysis/decoding.json`, speaking-rate metadata, `.s2mel.safetensors` и результаты независимого теста.

Автоматическая рекомендация сравнивает validation-подсказки и несколько seeds с Base. Она может выбрать Base. Стандартные guards (WER increase 0.02, speaker drop 0.03) и score weight4 являются эвристикой автора; interval guard оценивает ограниченную выборку. Они не доказывают приятность, не гарантируют каждый важный игровой термин и не заменяют прослушивание.

Русский язык не поддержан как штатный язык IndexTTS-2.5 на дату исследования. Результат нашей пробы RU плохой. Языковая адаптация потребовала бы отдельного исследовательского проекта, данных и критериев — не обещать её как обычное обучение voice LoRA. Для текущего русского продукта сохранять Qwen и исследовать его родные средства отдельно.
