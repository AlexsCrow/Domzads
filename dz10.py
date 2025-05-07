# # ЗАДАЧА - НАПИСАТЬ ФУНКЦИЮ КОТОРАЯ БУДЕТ ГЕНЕРИТЬ 2 КОРТЕЖА ПО ЗАДАННЫМ ДИАПАЗОНАМ
import random
from random import randint


def ran(a, b):  # должно приходить 2 значения a и b, функцию назвали ran
    return tuple(randint(a, b) for i in range(10))


tpl1 = ran(0, 5)  # это кортеж, функцию назвали tpl1
print(tpl1)  # вывели генерацию от 0 до 5
tpl2 = ran(-5, 0)  # тоже самое
print(tpl2)  # вывели генерацию от -5 до 0

tpl3 = tpl1 + tpl2  # складываем два кортежа в третий
print(tpl3)
print("0 = ", tpl3.count(0))  # выводим количество нулей


