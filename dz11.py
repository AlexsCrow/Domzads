# # НАЙТИ ВСЕ БУКВЫ В ПЕРВОЙ СТРОКЕ, КОТОРЫХ НЕТ ВО ВТОРОЙ

st1 = "Python"
st2 = "Programming language"
st = set(st1) - set(st2)
a = st
for i in a:
    print(i, end=" ")
