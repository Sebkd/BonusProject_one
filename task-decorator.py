# test decorator
'''тест для понимания декораторов'''

def simple_decor(func):
    def wrapper(arg):
        print(f'Run function {str(func.__name__)}()')
        func(arg)
        print('End function')
    return wrapper

@simple_decor
def sqrt(num):
    print(f'Корень квадратный из {num} =  {num ** 0.5}')

class Test():
    def __init__(self, x_axis, y_axis):
        self._x_axis = x_axis
        self._y_axis = y_axis

    @simple_decor
    def modul_vector(self):
        print(f'Модуль вектора равен = {(self._x_axis * 2 + self._y_axis * 2) ** 0.5}')
    pass

sqrt(5)
vector = Test(12, 6)
vector.modul_vector()
