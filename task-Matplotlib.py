# task-Matplotlib
'''Знакомство и работа с библиотекой Matplotlib'''
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
import matplotlib.gridspec as gridspec
# -----------------------------------------------------
# plt.plot([i for i in range(5)], [i for i in range(5)])
# plt.show()

# print(matplotlib.__version__)

# '''построение линейной зависимости'''
# x_axis = np.linspace(10, 100, 50)
# y_axis = x_axis

# '''Построение графика'''
# plt.title('Линейная зависимость y(x) = x')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.grid()
# plt.plot(x_axis, y_axis, 'r--') # r-- красная пунктирная
# plt.show()
#
# '''построение линейной зависимости'''
# x_axis = np.linspace(10, 100, 50)
# y_axis = x_axis
# ------------------------------------------------------------------
# '''Построение нескольких зависемостей на однои графике'''
# plt.title('Зависимости: y1 = x, y2 = x^2')
# x_axis = np.linspace(10, 100, 50)
# y_axis_1 = x_axis
# y_axis_2 = [number ** 2 for number in x_axis]
# plt.xlabel('x')
# plt.ylabel('y1 , y2')
# plt.grid()
# # plt.plot(x_axis, y_axis_1, x_axis, y_axis_2) # r-- красная пунктирная
# plt.plot(x_axis, y_axis_1)
# plt.scatter(x_axis, y_axis_2) #вариант точками
# plt.legend(('y1 = x', 'y2 = x^2'), loc = 0) # прорисовка легенды
# plt.minorticks_on()# добавление дополнительных тиков на осях
# plt.show()
# -----------------------------------------------------------------------
# '''Построение нескольких зависемостей на разных графиках'''
#
# x_axis = np.linspace(10, 100, 50)
# y_axis_1 = x_axis
# y_axis_2 = [number ** 2 for number in x_axis]
# '''.figure - функция для задания глобальных параметров
# отображения графиков. В нее, в качестве аргумента, мы передаем
# кортеж, определяющий размер общего поля.'''
# plt.figure(figsize = (9, 9))
# '''subplot() - функция для задания местоположения поля с
# графиком. Существует несколько способов задания областей для
# вывода графиков. В примере мы воспользовались вариантом,
# который предполагает передачу трех аргументов: первый аргумент
# - количество строк, второй - столбцов в формируемом поле, третий
# - индекс (номер поля, считаем сверху вниз, слева направо).'''
# plt.subplot(2, 1, 1)
# plt.plot (x_axis, y_axis_1)
# plt.title('Зависимости: y1 = x, y2 = x^2')
# plt.ylabel('y1')
# plt.grid()
# plt.subplot(2, 1, 2)
# plt.plot(x_axis, y_axis_2) # r-- красная пунктирная
# plt.xlabel('x')
# plt.ylabel('y2')
# plt.grid()
# plt.show()
# -------------------------------------------------------------------------------
'''Построение барами'''
# fruits = ['яблоки', 'груши', 'апельсины', 'бананы', 'киви']
# values = [34, 45, 12, 50, 12]
# plt.bar(fruits, values)
# plt.legend('  ')
# plt.title('Количество проданных фруктов')
# plt.xlabel('тип фрукта', fontsize = 14)
# plt.ylabel('Количество', fontsize = 14)
# plt.minorticks_on()
# plt.grid()
# plt.show()
# --------------------------------------------------------------------------------
# '''Построение с минорными тиками и минорными сетками, использование легенды с метками'''
# x = np.linspace(0, 10, 50)
# y1 = 4*x
# y2 = [i**2 for i in x]
# fig, ax = plt.subplots(figsize=(8, 6))
# ax.set_title('Графики зависимостей: y1=4*x, y2=x^2', fontsize=16)
# ax.set_xlabel('x', fontsize=14)
# ax.set_ylabel('y1, y2', fontsize=14)
# ax.grid(which='major', linewidth=1.2)
# ax.grid(which='minor', linestyle='--', color='gray', linewidth=0.5)
# ax.scatter(x, y1, c='red', label='y1 = 4*x')
# ax.plot(x, y2, label='y2 = x^2')
# ax.legend()
# ax.xaxis.set_minor_locator(AutoMinorLocator())
# ax.yaxis.set_minor_locator(AutoMinorLocator())
# ax.tick_params(which='major', length=10, width=2)
# ax.tick_params(which='minor', length=5, width=1)
# plt.show()
# --------------------------------------------------------------------------------
# '''Использование suplots()
# Функция subplots() возвращает два объекта,
# первый - это Figure, подложка, на которой будут размещены поля с
# графиками, второй - объект (или массив объектов) Axes, через который
# можно получить полных доступ к настройке внешнего вида
# отображаемых элементов.
# '''
# x = [1, 5, 10, 15, 20]
# y1 = [1, 7, 3, 5, 11]
# y2 = [i*1.2 + 1 for i in y1]
# y3 = [i*1.2 + 1 for i in y2]
# y4 = [i*1.2 + 1 for i in y3]
# # Настройка размеров подложки
# figure, axs = plt.subplots(2, 2, figsize=(12, 7))
# axs[0, 0].plot(x, y1, '-', label = 'line y1')
# axs[0, 1].plot(x, y2, '--', label = 'line y2')
# axs[1, 0].plot(x, y3, '-.', label = 'line y3')
# axs[1, 1].plot(x, y4, ':', label = 'line y4')
# plt.legend()
# plt.show()
# ------------------------------------------------------------------------------
# '''Работа с легендой
# Для отображения легенды на графике используется функция legend().
# Возможны следующие варианты ее вызова:
# legend()
# legend(labels)
# legend(handles, labels)
# '''
# x = [1, 5, 10, 15, 20]
# y1 = [1, 7, 3, 5, 11]
# y2 = [4, 3, 1, 8, 12]
# y3 = [(numbers + 2) for numbers in x]
# y4 = [(numbers + 2) for numbers in y2]
# plt.figure(figsize = (10, 5))
#--------
# plt.plot(x, y1, 'o-r', label='line 1')
# plt.plot(x, y2, 'o-.g', label='line 2')
# plt.plot(x, y3, 'o--b', label='line 3')
# plt.plot(x, y4, 'o:m', label='line 4')
# # plt.legend() # legend явно принимает названия из .plot
# ----------
# # plt.plot(x, y1, 'o-r')
# # plt.plot(x, y2, 'o-.g')
# # plt.plot(x, y3, 'o--b')
# # plt.plot(x, y4, 'o:m')
# # plt.legend(['L1', 'L2', 'L3', 'L4']) # второй вариант с labels внутри legend
# -----------
# # line1, = plt.plot(x, y1, 'o-r')
# # line2, = plt.plot(x, y2, 'o-.g')
# # line3, = plt.plot(x, y3, 'o--b')
# # line4, = plt.plot(x, y4, 'o:m')
# # plt.legend((line1, line2, line3, line4), ['line L1', 'line L2', 'line L3', 'line L4']) #третий вариант с кортежом
# '''
# Для более гибкого управление расположением объекта можно
# воспользоваться параметром bbox_to_anchor функции legend().
# Этому параметру присваивается кортеж, состоящий из четырех или двух
# элементов:
# bbox_to_anchor = (x, y, width, height)
# bbox_to_anchor = (x, y)
# framealpha = Прозрачность легенды None или float
# frameon - рамка,
# facecolor - Цвет заливки None или str
# edgecolor - Цвет рамки
# '''
# plt.legend(bbox_to_anchor=(1, 0.6), frameon = False) # Расположение легенды вне поля графика, нужно открыть 1 вар
# plt.show()
# -----------------------------------------------------------------------------------------------------------------
'''
Класс GridSpec, позволяет задавать геометрию сетки и расположение на
ней полей с графиками. На первый взгляд может показаться, что работа
с GridSpec довольно неудобна и требует написания лишнего кода, но,
если требуется расположить поля с графиками нетривиальным образом,
то этот инструмент становится незаменимым. Перед тем как работать с
GridSpec импортируйте его

Объект класса GridSpec, создается в строке:
gridspec.GridSpec(ncols=2, nrows=1, figure=fg)
В конструктор класса передается количество столбцов, строк и Фигура,
на которой все будет отображено.
Альтернативный вариант создания объекта GridSpec выглядит так:
gs = fg.add_gridspec(1, 2)
Здесь fg - это объект Figure, у которого есть метод add_gridspec(),
позволяющий добавить на него сетку с заданными параметрами (в
нашем случае одна строка и два столбца).
'''
x = [1, 2, 3, 4, 5]
y1 = [9, 4, 2, 4, 9]
y2 = [1, 7, 6, 3, 5]
y3 = [-7, -4, 2, -4, -7]
# ---- Свободная компоновка трех графиков
# fg = plt.figure(figsize=(9, 4), constrained_layout=True)
# gs = fg.add_gridspec(2, 2)
# fig_ax_1 = fg.add_subplot(gs[0, :])
# plt.plot(x, y2)
# fig_ax_2 = fg.add_subplot(gs[1, 0])
# plt.plot(x, y1)
# fig_ax_3 = fg.add_subplot(gs[1, 1])
# plt.plot(x, y3)
# ---- Свободная компановка без графиков
# fg = plt.figure(figsize=(9, 9), constrained_layout=True)
# gs = fg.add_gridspec(5, 5)
# fig_ax_1 = fg.add_subplot(gs[0, :3])
# fig_ax_1.set_title('gs[0, :3]')
# fig_ax_2 = fg.add_subplot(gs[0, 3:])
# fig_ax_2.set_title('gs[0, 3:]')
# fig_ax_3 = fg.add_subplot(gs[1:, 0])
# fig_ax_3.set_title('gs[1:, 0]')
# fig_ax_4 = fg.add_subplot(gs[1:, 1])
# fig_ax_4.set_title('gs[1:, 1]')
# fig_ax_5 = fg.add_subplot(gs[1, 2:])
# fig_ax_5.set_title('gs[1, 2:]')
# fig_ax_6 = fg.add_subplot(gs[2:4, 2])
# fig_ax_6.set_title('gs[2:4, 2]')
# fig_ax_7 = fg.add_subplot(gs[2:4, 3:])
# fig_ax_7.set_title('gs[2:4, 3:]')
# fig_ax_8 = fg.add_subplot(gs[4, 3:])
# fig_ax_8.set_title('gs[4, 3:]')
# ------ Можно заранее задать размеры областей и передать их в качестве параметров в виде массивов:
fg = plt.figure(figsize=(5, 5),constrained_layout=True)
widths = [1, 3]
heights = [2, 0.7]
gs = fg.add_gridspec(ncols=2, nrows=2, width_ratios=widths,
height_ratios=heights)
fig_ax_1 = fg.add_subplot(gs[0, 0])
fig_ax_1.set_title('w:1, h:2')
fig_ax_2 = fg.add_subplot(gs[0, 1])
fig_ax_2.set_title('w:3, h:2')
fig_ax_3 = fg.add_subplot(gs[1, 0])
fig_ax_3.set_title('w:1, h:0.7')
fig_ax_4 = fg.add_subplot(gs[1, 1])
fig_ax_4.set_title('w:3, h:0.7')
plt.show()
# ---------------------------------------------------------------------------------------------------------------




