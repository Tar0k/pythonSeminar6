# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_element = int(input("Введите первый элемент: "))
difference = int(input("Введите разность: "))
quantity = int(input("Введите количество: "))


def formula(a, n, d):
    return a + (n - 1) * d


result = [formula(first_element, num, difference) for num in range(1, quantity + 1)]
print(result)
