## СОЗДАТЬ КЛАСС ДЛЯ ПОДСЧЁТА ПЛОЩАДИ ГЕОМЕТРИЧЕСКИХ ФИГУР
from math import sqrt


class Area:
    __count = 0  # (закрытая переменная) здесь подсчитываем, сколько раз вызывалась Area

    @staticmethod
    def triangle_area(a, b, c):  # 3 стороны треугольника

        p = (a + b + c) / 2  # полупериметр
        Area.__count += 1  # устанавливаем подсчёт обращений к площади
        return sqrt(p * (p - a) * (p - b) * (p - c))  # формула Герона

    @staticmethod
    def triangle_area2(a, h):  # 1 сторона и высота
        p = 0.5 * a * h
        Area.__count += 1
        return p

    @staticmethod
    def square_area(a):  # 2 стороны квадрата
        p = a ** 2
        Area.__count += 1
        return p

    @staticmethod
    def rectangle_area(a, b):
        p = a * b
        Area.__count += 1
        return p

    @staticmethod
    def get_count():  # метод (получить подсчёт)
        return Area.__count  # вернуть подсчёт


print("Площадь треугольника по формуле Герона =", Area.triangle_area(3, 4, 5))  # здесь пишем значения сторон
print("Площадь треугольника через основание и высоту =", Area.triangle_area2(6, 7))
print("Площадь квадрата =", Area.square_area(7))
print("Площадь прямоугольника =", Area.rectangle_area(2, 6))
print("Количество подсчётов площади:", Area.get_count())
