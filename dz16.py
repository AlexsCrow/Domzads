## ДЗ 16 - ВВОДИМ ЛЮБОЕ КОЛИЧЕСТВО ЧИСЕЛ И ВЫЧИСЛЯЕМ СРЕДНЕЕ АРИФМЕТИЧЕСКОЕ
def avg(fn):
    def wrap(*args):
        print("Среднее арифметическое:", *args, "=", fn(*args) / len(args))

    return wrap  # возвращаем вложенную функцию


@avg
def summa(*args):  # любое количество чисел
    print("Сумма чисел:", *args, "=", sum(args))
    return sum(args)  # возвращаем сумму


summa(2, 3, 3, 4)  # сюда передаём числа
