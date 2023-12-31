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
import re
import time


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
    while True:
        player_side = (input("Введите сторону (X или O): "))
        if re.match(r"[xX]$", player_side):
            return 1
        elif re.match(r"[oO0]$", player_side):
            return -1
        else:
            print("Некорректный ввод")
            continue


def user_move():
    while True:
        move = input("Введите клетку адрес клетки через запятую: ").replace(" ", "")
        move = re.match(r"^[1-3],[1-3]$", move)
        if move:
            move = move.group()
        else:
            print("Некорректный ввод")
            continue
        column, row = move.split(",")
        column, row = int(column) - 1, int(row) - 1
        if field[column][row] != 0:
            print("Ячейка уже заполнена")
            continue

        return column, row


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

    print("Ход компьютера")
    r, c = ai_move()
    field[r][c] = ai
    draw_field()
    if is_finished():
        break
