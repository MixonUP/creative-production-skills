# Источники и границы доказательств

Исследование 2026-10-04. Ни один источник не объявлен доказательством «лучших голосов в мире». Ни обучение, ни новые аудиогенерации при создании этого навыка не запускались. Здесь оригинальная прикладная методика, ссылки и проверенные поля, а не копия платного руководства.

## Материалы SECourses

- [Приобретённый пост IndexTTS](https://www.patreon.com/SECourses/posts/indextts-2-5-and-139297407): доступный веб-текст подтверждает LoRA/DoRA, dataset preparation, emotion control, checkpoint comparison. Страница/индекс могут отставать от установленного кода; архив повторно не скачивался.
- [Авторское приложение](https://github.com/FurkanGozukara/Premium_IndexTTS2_SECourses/tree/a776268d8c532e19836a1fa90f4e8d28b9ea20fe): локальный checkout в `E:/Krea_tren_AI/GamesDev/RnD/IndexTTS/Vendor/SECourses`. Прочитаны относящиеся к задаче разделы README и код подготовки/конфигурации/интеграции. Проверенные defaults и хеши прочитанных файлов сохраняются в evidence этого исследования.
- [Выбор обучения/checkpoint](https://github.com/FurkanGozukara/Premium_IndexTTS2_SECourses/blob/a776268d8c532e19836a1fa90f4e8d28b9ea20fe/docs/TRAINING_SELECTION.md): прочитана локальная версия; source split, отдельные loss/probe best, blind review, deployment comparison и independent final test.
- [Эксперимент декодера](https://github.com/FurkanGozukara/Premium_IndexTTS2_SECourses/blob/a776268d8c532e19836a1fa90f4e8d28b9ea20fe/VOICE_DECODER_ADAPTER_2026-09-08.md): изучены архитектура и неудачный первый проход. Его измерения — результаты автора на его голосе, не наша репликация. Главный перенос: reconstruction недостаточен для приёмки TTS.
- [Связанное автором видео](https://www.youtube.com/watch?v=YbgFVKWB7hs): ссылка найдена в Patreon. Получить содержимое/транскрипт через web не удалось; видео **не просмотрено**, выводы по его таймкодам не делались. Навык основан на доступных письменных первоисточниках и установленном коде.

## Другие первоисточники

- [IndexTeam, основной репозиторий](https://github.com/index-tts/index-tts) и [model card 2.5](https://huggingface.co/IndexTeam/IndexTTS-2.5): пять заявленных языков ZH/EN/JA/ES/AR, reference cloning, управляемые эмоции; русский не заявлен. Не смешивать окружение upstream с SECourses installer. Условия применения проверять по конкретной лицензии артефактов перед релизом; наличие подписки само по себе не устанавливает все права.
- [DoRA, ICML 2024](https://arxiv.org/abs/2402.09353): прочитана аннотация о разделении magnitude/direction. Опубликованные задачи не дают универсального voice-quality рейтинга LoRA против DoRA.
- [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS): опубликованы VoiceDesign, CustomVoice и Base; русский перечислен среди поддерживаемых языков. Это основание отдельного RU-маршрута, а не доказательство локальной установки VoiceDesign.
- [Официальный Qwen fine-tuning](https://github.com/QwenLM/Qwen3-TTS/blob/main/finetuning/README.md): single-speaker SFT, audio/text/ref_audio, extraction codes и sft_12hz. Не называть этот рецепт LoRA. Общий ref_audio рекомендован именно там; не переносить Index decoder sampling механически.
- [Shure: запись вокала](https://www.shure.com/en-US/insights/how-to-record-and-mix-vocals): поп-фильтр, выбор позиции и влияние движения на звук. Это принципы записи, не тест нашего FIFINE. Дистанции/план объёма в навыке — наши пробные ориентиры.

## Наши фактические результаты до создания навыка

`E:/Krea_tren_AI/GamesDev/aiwaifu-versions-handoff.json` фиксирует версии и пути. Main/Qwen RU speech и IndexTTS EN game chain прошли технические проверки; Index RU провалил диагностическую разборчивость. `RnD/IndexTTS/Evidence/voice-check/20261004-005728`, `russian-probe/20261004-010219`, `integration-runs/20261004-010822` — фактические отчёты.

Ни один локальный voice LoRA/DoRA run не объявлен обученным. ASR-тесты не подменяют субъективного прослушивания. 20–40 минут пилотной речи, кастинг 6–10 строк, smoke 10–30 updates и компактный benchmark — наши настраиваемые рабочие бюджеты. Отбирать их заново под язык/персонажа/оборудование, а не выдавать за требования SECourses.
