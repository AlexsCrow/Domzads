# # ЗАПОЛНИТЬ СПИСОК ИЗ 10 ЭЛЕМЕНТОВ СЛУЧАЙНЫМИ ЧИСЛАМИ. УДАЛИТЬ ВСЕ ЭЛЕМЕНТЫ ПЕРЕД МИНИМАЛЬНЫМ ЧИСЛОМ.
import random

mas1 = [random.randint(0, 100) for i in range(10)]
print(mas1)
mas = mas1.copy()
mas.sort()
# print(mas)
min_ = mas[0]
print("Min = ", min_)
ind = mas1.index(min_)
print("Index min =", ind)
del mas1[:ind]
print(mas1)

