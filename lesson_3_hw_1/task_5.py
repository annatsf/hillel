"""З використанням рядків
"""
numbers = input("Enter a three-digit number: ")
# конвертирую string в list
# убираю в списке возможый '-' c помощью метода strip()
suma = sum([int(i) for i in numbers.strip("-")])
print("Sum of digits is", suma)

"""Без використання рядків
"""
# перевожу в формат integer, избавляюсь
# функцией abs() от возможного "-"
number = abs(int(input("Enter a three-digit number: ")))


def sum(number):
    sum = 0
    while number > 0:
        # нахожу остаток от деления на 10, использую
        # целочисленное деление
        a = number % 10
        sum = sum + a
        number = number // 10
    return f"Sum of digits is {sum}"


print(sum(number))
