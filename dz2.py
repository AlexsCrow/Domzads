# # ЗАПРАШИВАЕМ У ПОЛЬЗОВАТЕЛЯ 5 ЗНАЧНОЕ ЧИСЛО. НАХОДИМ ПРОИЗВЕДЕНИЕ ВСЕХ ЧИСЕЛ И СРЕДНЕЕ АРИФМЕТИЧЕСКОЕ

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))
num4 = int(input("Введите четвёртое число: "))
num5 = int(input("Введите пятое число: "))

sum2 = num1 + num2 + num3 + num4 + num5
sum3 = num1 * num2 * num3 * num4 * num5
sum4 = (num1 + num2 + num3 + num4 + num5) / 5
print("Ваше число: ", num1*10000+num2*1000+num3*100+num4*10+num5) # Выводим всё число
print("Сумма всех чисел: ", sum2)
print("Произведение всех чисел: ", sum3)
print("Среднее арифметическое: ", round(sum4, 2))



