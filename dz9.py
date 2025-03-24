# # НАПИСАТЬ ФУНКЦИЮ, КОТОРАЯ ИМЕЕТ 20 СИМВОЛОВ И СИМВОЛ "-"
# В КАЧЕСТВЕ АРГУМЕНТОВ ПО УМОЛЧАНИЮ И ВЫВОДИТИ НА ЭКРАН
# НАБОР ПРОИЗВОЛЬНЫХ СИМВОЛОВ ЗАДАННОЙ ДЛИНЫ

def set_param(count=20, symbol="-"):
    print(count * symbol)


set_param(count=10, symbol="+")
set_param(count=5, symbol="*")
set_param(count=15, symbol="#")
set_param(7)
set_param()
