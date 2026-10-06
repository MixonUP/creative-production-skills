# Источники, примеры и происхождение

Проверено 07.10.2026. Навык создан локально по запросу пользователя. Пользователь
уточнил: главное — самостоятельно находить/создавать подходящую математику для
разных задач; примеры из ролика служат отправной точкой, не границей навыка.

## Видео как пример метода

[Студия Игор, 7:55](https://www.youtube.com/watch?v=tB147SYClzU&t=475s): крупным
планом прочитаны частота от скорости и интеграл фазы, дисперсия струны и сумма
затухающих мод. В [задании 7:35–7:40](https://www.youtube.com/watch?v=tB147SYClzU&t=455s)
видна связь референсов, процедурного результата и страницы для оценки.
Исходные файлы автора не получены; просмотр этих кадров не равен аудиту реализации
или слуховой экспертизе. Экспорт стенограммы снова не дал текста.

## Первичные технические источники

- Robert Bridson, [Fast Poisson Disk Sampling in Arbitrary Dimensions](https://www.cs.ubc.ca/~rbridson/docs/bridson-siggraph07-poissondisk.pdf), SIGGRAPH 2007: пространственная выборка с минимальной дистанцией.
- Ken Perlin, [Improving Noise](https://mrl.cs.nyu.edu/~perlin/paper445.pdf), 2002: gradient noise и гладкость интерполяции.
- Khronos, [smoothstep — исходник справочника](https://github.com/KhronosGroup/OpenGL-Refpages/blob/main/gl4/smoothstep.xml): кубическая интерполяция и порядок границ.
- SciPy, [chirp](https://docs.scipy.org/doc/scipy-1.17.0/reference/generated/scipy.signal.chirp.html): мгновенная частота и фаза.
- Julius O. Smith III, [Modal Representation](https://www.dsprelated.com/freebooks/pasp/Modal_Representation.html): модальная форма.
- Julius O. Smith III, [The Dispersive 1D Wave Equation](https://www.dsprelated.com/freebooks/pasp/Dispersive_1D_Wave_Equation.html): жёсткость, частотно-зависимое распространение, allpass-представление.
- Daniel Holden, [Spring-It-On](https://theorangeduck.com/page/spring-roll-call): затухание и пружины с учётом шага времени.
- University of Illinois, [Inverse Kinematics lecture](https://publish.illinois.edu/ece470-intro-robotics/files/2021/10/ECE470Lec11-2.pdf): аналитическая кинематика двух звеньев.
- Ho, Salimans, [Classifier-Free Diffusion Guidance](https://arxiv.org/abs/2207.12598): сочетание условного/безусловного предсказания.
- Zhang et al., [ControlNet](https://arxiv.org/abs/2302.05543): архитектура пространственного conditioning; не универсальный API всех генераторов.

Формулы в справочниках записаны в согласованных локальных обозначениях. Стандартные
геометрические/алгебраические выводы и численные примеры добавлены нами; не приписывать
их ролику. Код лаборатории написан локально, исходники перечисленных авторов не копировались.
Список открыт: новые задачи требуют новых релевантных источников.

Полный разбор: E:/Krea_tren_AI/Knowledge/06_Sources/StudioIgor_Formulas_2026-10-07.md.
Процедура: E:/Krea_tren_AI/Knowledge/04_Procedures/Formula_Driven_Production.md.
