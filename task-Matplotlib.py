# task-Matplotlib
'''Знакомство и работа с библиотекой Matplotlib'''
import matplotlib
import matplotlib.pyplot as plt

plt.plot([i for i in range(5)], [i for i in range(5)])
plt.show()

print(matplotlib.__version__)