# Задача FOOTBALL необязательная
# Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой
# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков
# Конкретный пример ввода-вывода приведён ниже.
# Порядок вывода команд произвольный.
# Пример входа:
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# Выход будет:
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6
import re


class GameLog:
    def __init__(self):
        self.game_log = {}

    def __str__(self):
        table_name = "\nСТАТИСТИКА\n"
        header = ["Команда", "Всего игр", "Побед", "Ничьих", "Поражений", "Очков"]
        header = " | ".join([item.center(11) for item in header]) + "\n"
        separator = "-" * len(header) + "\n"

        table_data = ""
        for team_name, stat in self.game_log.items():
            stats = [str(stat[item]).center(11) for item in stat]
            table_data += team_name.center(11) + " | " + " | ".join(stats) + "\n"
        return table_name + header + separator + table_data

    def add_records(self, records: dict):
        for key, value in records.items():
            if key not in self.game_log:
                self.game_log[key] = {"И": 0, "В": 0, "Н": 0, "П": 0, "О": 0}
            self.game_log[key]["И"] += 1
            self.game_log[key][value] += 1
            self.game_log[key]["О"] = self.game_log[key]["В"] * 3 + self.game_log[key]["Н"]


def add_match_data(match_number=1):
    user_input = ""
    is_input_correct = False
    while is_input_correct is False:
        user_input = input(f"Введите результат {match_number} матча (через пробел или ;): ")
        if len(re.findall(r"\w+? \d+?", user_input.replace(";", " "))) != 2:
            print("Неверный ввод")
            continue
        is_input_correct = True
    return user_input


nn = None
while type(nn) != int:
    nn = input("Введите количество завершенных игр: ")
    if nn.isnumeric():
        nn = int(nn)

games = []
number = 1
while nn > 0:
    games.append(add_match_data(number))
    nn -= 1
    number += 1

game_log = GameLog()
# games = ["Спартак;9;Зенит;10", "Локомотив;12;Зенит;3", "Спартак;8;Локомотив;15"]


for game in games:
    game_data = re.findall(r"\w+? \d+?", game.replace(";", " "))
    game_data = [(item.split()[0].lower().capitalize(), int(item.split()[1])) for item in game_data]

    data = {}
    if game_data[0][1] > game_data[1][1]:
        data[game_data[0][0]] = "В"
        data[game_data[1][0]] = "П"
    elif game_data[1][1] > game_data[0][1]:
        data[game_data[1][0]] = "В"
        data[game_data[0][0]] = "П"
    else:
        data[game_data[0][0]] = "Н"
        data[game_data[1][0]] = "Н"
    game_log.add_records(data)

print(game_log)
