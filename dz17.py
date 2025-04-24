## dz 17
## I am learning Python. hello WORLD!

s = input("Введите строку: ")
a = s[:s.find('h')]
print(a)
c = s[s.rfind('h') + 1:]
print(c)
print(a + "  " + c)
b = s[s.find('h'):s.rfind('h') + 1]
print(a + "   " + b + "   " + c)
print(a + b[::-1] + c)
