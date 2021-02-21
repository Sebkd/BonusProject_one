# task-Matplotlib
'''Знакомство и работа с библиотекой Matplotlib'''
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

# plt.plot([i for i in range(5)], [i for i in range(5)])
# plt.show()

# print(matplotlib.__version__)

'''построение линейной зависимости'''
x_axis = np.linspace(10, 100, 50)
y_axis = x_axis

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

'''Построение нескольких графиков'''
plt.title('Линейная зависимость y(x) = x')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.plot(x_axis, y_axis, 'r--') # r-- красная пунктирная
plt.show()