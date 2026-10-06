# Учебный маршрут и источники

Проверено 30.09.2026. Основные факты получены из официальной документации, CLI-help установленного Topaz и наших старых артефактов. Reddit — опыт участников, не подтверждённая техническая спецификация. Сторонние skills прочитаны как материал, их команды автоматически не выполнялись.

## Наиболее полезные уроки для нас

1. **Topaz Labs — [Enhancing Low Quality Video](https://www.youtube.com/watch?v=XBEkVHd2tmw)**, 13.11.2024. Подробный пример 320×240 → 4x с Nyx и вторым проходом Theia. 01:32 первый проход, 04:37 режимы параметров, 08:21 второй, 12:05 другая сцена. Изучена английская авторасшифровка, включая ветку добавления небольшого шума против нежелательной фактуры. Применимый урок — сравнивать результат по сценам и понимать назначение каждого прохода; конкретные числа из архива не переносить на наш Seedance. Полный визуальный просмотр не проводился.
2. **Topaz Labs — [Parameters & 2nd Enhancement (v6)](https://www.youtube.com/watch?v=kBirVbMk0T0)**, 12.02.2025. Компактное продолжение по управлению и последовательности enhancement. Проверены заголовок/описание и размещение в официальной библиотеке; расшифровка не разобрана. Полезно перед экспериментами с двумя моделями.
3. **Topaz Labs — [Video AI — Frame Interpolation](https://www.youtube.com/watch?v=HKqB5QyV2hQ)**, 02.12.2024. 03:19 связь FPS и slow motion, 04:51 модели, 07:08 дубликаты, 08:57 ограничения. Проверены описание/главы, технические выводы сверены с официальной статьёй и нашим `tvai_fi -h`. Учебная версия v5; настройки интерфейса 1.7 могут отличаться.
4. **[Официальная библиотека уроков](https://docs.topazlabs.com/topaz-video/video-tutorials)**. Выбрать Enhancements #2, #3, Set Tab Comparison, Export и Tips & Tricks. В Tips & Tricks особенно 06:34 Recover Detail, 08:37 память. Это серия Video AI v5/v6, не демонстрация новых diffusion-моделей 1.7.

Из первого ролика сохранена авторасшифровка: `KnowledgeData/snapshots/2026-09-30/topaz-skill-033054/lesson-XBEkVHd2tmw.txt`. Она доказывает содержание объяснения, но не локальное качество и не точность всех автоматических подписей.

## Основные первоисточники

| Источник | Что обосновывает |
|---|---|
| [Enhancement](https://docs.topazlabs.com/topaz-video/filters/enhancement) | Назначения моделей и различие восстановления/смешивания детали |
| [Second Pass](https://docs.topazlabs.com/topaz-video/advanced-functions/second-pass-enhancement) | Промежуточное разрешение, отдельные последовательные экспорты |
| [Frame Interpolation](https://docs.topazlabs.com/topaz-video/filters/frame-interpolation) | Отдельные решения о slowmo/FPS/дубликатах, оговорка про звук |
| [Preferences](https://docs.topazlabs.com/topaz-video/reference-guide/preferences) | GPU, память, parallel processes, decode; значения зависят от версии |
| [Plugins](https://docs.topazlabs.com/topaz-video/plugins) | Официальный OFX требует Resolve Studio; Free не поддержан |
| [Starlight Precise 2.5/2.6](https://docs.topazlabs.com/topaz-video/project-starlight-series/starlight-precise-25) | 2.6 с версии 1.7, отдельный Neuroserver, ограничения и короткий Export |
| [Starlight Mini](https://docs.topazlabs.com/topaz-video/project-starlight-series/starlight-mini) | Отдельная архивная модель, требования и изменение доступа в 1.7 |
| [Sharp](https://docs.topazlabs.com/topaz-video/project-starlight-series/starlight-sharp), [Fast 2](https://docs.topazlabs.com/topaz-video/project-starlight-series/starlight-fast-2-local) | Доступ и требования других вариантов не переносить на Precise |
| [Video AI vs Topaz Video](https://docs.topazlabs.com/topaz-video/tvai-vs-tv) | Разные поколения продукта и нумерация |
| [CLI, legacy](https://docs.topazlabs.com/video-ai/advanced-functions-in-topaz-video-ai/command-line-interface) | Bundled FFmpeg и две TVAI environment variables; локальный help приоритетнее старого примера |

## Сообщество и готовые skills: что принято, что отклонено

- [Topaz Community — Order of Using AI Models](https://community.topazlabs.com/t/order-of-using-ai-models/101683), 27–28.03.2026. Сотрудник `kyle.topazlabs` рекомендует короткие отдельные previews кандидатов. Звёздочки GUI не требуют последовательно запускать все рекомендованные модели. Принят метод сравнения, не личный рейтинг участника.
- [Reddit — Question about the workflow](https://www.reddit.com/r/TopazLabs/comments/1mdv8m3/question_about_the_workflow/). Пользователь описывает ghosting/морфинг после необоснованной последовательности из ответа ChatGPT; советы в комментариях расходятся. Это аргумент не выдавать универсальный порядок «interpolate → stabilize → denoise → enhance» за факт. Рецепты из комментариев не приняты как наш baseline.
- [billyhargroveofficial/billy-skills-hub — topaz-video-cli](https://github.com/billyhargroveofficial/billy-skills-hub/blob/main/topaz-video-cli/SKILL.md). Прочитан skill для macOS. Полезны явные model dirs и раздельная обработка сцен. Не перенесены Apple encoders, оценки скорости, автоматическое удаление звука и формула замедления без измерений. Исправлено расхождение: автор называет `rdt` scene-change threshold, локальный help — duplicate threshold; авторский default Apollo также не соответствует нашему default Chronos. Код не установлен и не запускался.
- [thy950523/topaz-video-cli](https://github.com/thy950523/topaz-video-cli). Прочитаны индексированные README-примеры CLI/skills; прямой fetch root SKILL.md вернул 404. Полный code audit не выполнен, Windows-совместимость не подтверждена. Не ставить отдельную Python-обвязку в Comfy/Toolkit по одному README.
- [inference-sh AI video skill](https://github.com/inference-sh/skills/blob/main/tools/video/ai-video-generation/SKILL.md) использует сторонний облачный Topaz endpoint. Это не автоматизация нашего локального приложения, в навык не включён.

Поиск X по Topaz/Proteus Natural не дал отдельного проверенного подробного руководства, которое добавило бы пользу к первоисточникам. Это не утверждение, что таких публикаций нет. Список намеренно ориентирован на применимость и проверяемость, а не число ссылок.

## Как обновлять знания

При новом уроке сохранить author/title/URL/date, просмотренные главы, inspection depth и применимость к установленной версии. Сначала captured/assessed, затем отдельный local trial. Изменения навыка делать в `Tools/skills`, проверить registry drift и установить через существующий manager с backup. Дату изменения и результаты внести в Knowledge-журнал. Новая документация не отменяет пользовательский запрет обновления Resolve.
