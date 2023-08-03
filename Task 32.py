# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
import random

# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

minimum = int(input("Введите минимум: "))
maximum = int(input("Введите максимум: "))

numbers = [random.randint(-10, 100) for item in range(10)]
print(numbers)
result = [index for (index, value) in enumerate(numbers) if minimum < value < maximum]
print(result)
