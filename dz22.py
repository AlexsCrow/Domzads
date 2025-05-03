## DZ 22 ЗАМЕНИТЬ СТРОКУ
import os
f = open("test3.txt", "w")
f.write("Замена строки в текстовом файле;\nИзменить строку в списке\nЗаписать список в файл;\n")
f.close()

f = open("test3.txt", "r")
read_line = f.readlines()
print(read_line)
f.close()

pos1 = int(input("Введите индекс строки pos1 = "))
pos2 = int(input("Введите индекс строки замены pos2 = "))

if 0 <= pos1 < len(read_line) and 0 <= pos2 < len(read_line):
    read_line[pos1], read_line[pos2] = read_line[pos2], read_line[pos1]
else:
    print("Такого индекса в списке строк - нет! Вводите от 0 до 2")
print(read_line)
f = open("test3.txt", "w")
f.writelines(read_line)
f.close()
print(os.getcwd())


