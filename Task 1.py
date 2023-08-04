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
import os
import time


def clear():
    os.system('cls')


field = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]


def symbol(value):
    if value == 0:
        return " "
    elif value == 1:
        return "X"
    elif value == -1:
        return "O"
    else:
        return "!!!"


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
                       .upper())
        if len(player_side) > 1:
            print("Некорректный ввод")
            continue
        if player_side != "X" and player_side != "O":
            print("Сторона не выбрана")
            continue
        is_side_selected = True

    return 1 if player_side == "X" else -1


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

        if field[move[0]][move[1]] != 0:
            print("Ячейка уже заполнена")
            continue

        is_correct_input = True

    return move[0], move[1]


def ai_move():
    free_fields = []
    for (row_index, row) in enumerate(field):
        for (column_index, column) in enumerate(row):
            if column == 0:
                free_fields.append((row_index, column_index))
    return random.choice(free_fields)


def is_finished():
    # Check win in rows
    for row in field:
        if sum(row) == 3 or sum(row) == -3:
            return True

    # Check win in columns
    col1, col2, col3 = field
    columns = list(zip(col1, col2, col3))
    columns_sums = [sum(item) for item in columns]
    if 3 in columns_sums or -3 in columns_sums:
        return True

    # Check win in diagonals
    if abs(sum((field[0][0], field[1][1], field[2][2]))) == 3 or abs(sum((field[0][2], field[1][1], field[2][0]))) == 3:
        return True

    # Check available moves
    free_fields = []
    for (row_index, row) in enumerate(field):
        for (column_index, column) in enumerate(row):
            if column == 0:
                free_fields.append((row_index, column_index))
    if len(free_fields) == 0:
        return True

    return False


player = select_side()
draw_field()
if player == -1:
    ai = 1

    time.sleep(2)
    clear()
    print("Ход компьютера")
    r, c = ai_move()
    field[r][c] = ai
    draw_field()

else:
    ai = -1
while True:
    r, c = user_move()
    field[r][c] = player
    draw_field()
    if is_finished():
        break

    time.sleep(2)
    clear()

    print("Ход компьютера")
    r, c = ai_move()
    field[r][c] = ai
    draw_field()
    if is_finished():
        break
