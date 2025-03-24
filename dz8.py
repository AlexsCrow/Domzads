# # ВЫЧИСЛИТЬ ПЛОЩАДИ ФИГУР
import math

shape = int(input("Выбор фигуры: \n1-треугольник\n2-прямоугольлник\n3-круг"))
s = None  # переменная (площадь), которая будет объявлена позже прописывается как None
if shape == 1:
    a = int(input("Введите длину стороны a = "))
    b = int(input("Введите длину стороны b = "))
    c = int(input("Введите длину стороны c = "))
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
elif shape == 2:
    a = int(input("Введите длину стороны a = "))
    b = int(input("Введите длину стороны b = "))
    s = a * b
elif shape == 3:
    radius = a = int(input("Введите радиус = "))
    s = math.pi * radius ** 2
else:
    print("Такой фигуры нет")
print(round(s, 2))  # округление до двух символов после точки (round)
