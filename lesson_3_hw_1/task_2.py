"""Оператор ‘*’ для строк – копирование 
строки заданное количество раз:
"""
string = "hillel"
n = 3
print(string * n)

"""Оператор ‘*’ для списков  - 
копирование списка заданное 
количество раз:
"""
list = ["h", "i", "l", "l", "e", "l"]
n = 2
print(list * n)

"""а также как способ построить новый 
список, применяя выражение к каждому 
элементу последовательности:
"""
list = [list * 3 for list in "haha"]
print(list)
