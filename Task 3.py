# Задача 1 необязательная. Напишите рекурсивную программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
#     *Пример:*
#     1+2*3 => 7;
#     (1+2)*3 => 9;
# Тут может помочь библиотека re
import re

# data = input()
data = "- 1.5 +(2 +  1)/9 "


def do_something(string):
    string = string.replace(" ", "")
    bracket_operation = re.search(r"\(.+?\)", string)
    if bracket_operation is not None:
        bracket_operation = bracket_operation.group().lstrip("(").rstrip(")")
        bracket_operation = do_something(bracket_operation)
        string = re.sub(r"\(.+?\)", bracket_operation, string)
        string = do_something(string)

    product_operation = re.search(r"[0-9.]+\*[0-9.]+", string)
    if product_operation is not None:
        product_operation = product_operation.group()
        factors = product_operation.split("*")
        product_operation = float(factors[0]) * float(factors[1])
        string = re.sub(r"[0-9.]+\*[0-9.]+", str(product_operation), string)
        string = do_something(string)

    divide_operation = re.search(r"[0-9.]+/[0-9.]+", string)
    if divide_operation is not None:
        divide_operation = divide_operation.group()
        dividers = divide_operation.split("/")
        divide_operation = round(float(dividers[0]) / float(dividers[1]), 3)
        string = re.sub(r"[0-9.]+/[0-9.]+", str(divide_operation), string)
        string = do_something(string)

    plus_operation = re.search(r"[0-9.]+\+[0-9.]+", string)
    if plus_operation is not None:
        plus_operation = plus_operation.group()
        plus_operation = sum([float(num) for num in plus_operation.split("+")])
        string = re.sub(r"[0-9.]+\+[0-9.]+", str(plus_operation), string)
        string = do_something(string)

    minus_operation = re.search(r"[0-9.]+-[0-9.]+", string)
    if minus_operation is not None:
        minus_operation = minus_operation.group()
        elements = minus_operation.split("-")
        minus_operation = float(elements[0]) - float(elements[1])
        string = re.sub(r"[0-9.]+-[0-9.]+", str(minus_operation), string)
        string = do_something(string)

    return string


print(do_something(data))
