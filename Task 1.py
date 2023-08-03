# Задача XO необязательная.
# Сделайте игру крестики - нолики, человек должен играть с ботом, поле 3*3.
# Конечно, бот не должен ходить на занятые поля
# Если есть желание, то можете наделить бота псевдоинтеллектом,чтоб он ходил как можно ближе к своим занятым клеткам
# После каждого хода на экран должна выводиться текущая обстановка на поле.
# Например,
#
# |     |  Х |
# |     |  O |
# |     |  O |
# При ходе пользователя у надо спрашивать номер строки и столбца, куда он хочет сделать ход
import random

field = [[1, 1, None],
         [-1, None, None],
         [-1, None, None]]


def symbol(value):
    if value is None:
        return " "
    elif value == 1:
        return "X"
    elif value == -1:

        return "O"


def draw_field():
    for row in field:
        print("----------")
        print(" | ".join([symbol(column) for column in row]))
    print("-----------")


def select_side():
    is_side_selected = False
    player_side = ""
    while is_side_selected is False:
        player_side = (input("Введите сторону (X или O): ")
                       .replace(" ", "")
                       .replace("0", "O")
                       .lower())
        if len(player_side) > 1:
            print("Некорректный ввод")
            continue
        if player_side != "x" and player_side != "o":
            print("Сторона не выбрана")
            continue
        is_side_selected = True
    return player_side


def user_move():
    is_correct_input = False
    move = None
    while is_correct_input is False:
        move = input("Введите клетку адрес клетки через запятую: ").replace(" ", "")
        if "," not in move:
            print("В вводе нет ,")
            continue

        move = move.split(",")
        if not move[0].isnumeric() or not move[1].isnumeric():
            print("Неверный формат чисел")
            continue

        move = int(move[0]) - 1, int(move[1]) - 1
        if move[0] > len(field) or move[1] > len(field):
            print("Значение за пределами поля")
            continue

        if field[move[0]][move[1]] is not None:
            print("Ячейка уже заполнена")
            continue

        is_correct_input = True
    return move[0], move[1]


def ai_move():
    free_fields = []
    for (row_index, row) in enumerate(field):
        for (column_index, column) in enumerate(row):
            if column is None:
                free_fields.append((row_index, column_index))
    return random.choice(free_fields)


def is_finished():
    for row in field:
        if sum(row) == 3 or sum(row) == -3:
            return True

draw_field()
print(user_move())
