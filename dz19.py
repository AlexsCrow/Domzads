## ЗАДАЧА – НАЙТИ КОЛИЧЕСТВО ОТРИЦАТЕЛЬНЫХ ЧИСЕЛ В МАССИВЕ С ПОМОЩЬЮ РЕКУРСИИ
## True или False

def negative_number(n):
    if len(n) == 0:  # можно ещё if not n:
        return 0
    count = 0
    if n[0] < 0:
        count += 1
    return count + negative_number(n[1:])


lst = [-2, 3, 8, -11, -4, 6]
print(negative_number(lst))
