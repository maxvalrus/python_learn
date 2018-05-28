import random
import os

#Победные комбинации
final = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )

def initial_field():
    """
    Генерация поля игры
    :return: поле игры
    """
    field = list(range(0, 9))
    return field

def print_field(field, comment=''):
    """
    Отрисовка поля игры
    :param field: текущее поле игры
    :return: -
    """

    if comment == '':
        print('После хода поле имеет вид:')
    else:
        print('\n', comment)
    for i in range(0, 9, 3):
        print("\t", field[i], "|", field[i+1], "|", field[i+2])
        if i < 5:
            print('\t ---------')
    print('\n')

def clear_field(field):
    """
    Очищаем поле игры
    :param field: поле до очистки
    :return: чистое игровое поле
    """
    for i in field:
        field[i] = " ";
    return field

def human_step(field):
    """
    Тут описывается ход игрока
    :param field: текущее состояние поля
    :return: изменяется поле игры
    """
    while True:
        avaible_index = avaible_turn(field)
        try:
            index = int(input('Введите индекс поля для хода: '))
        except:
            print('\t Вводить можно только число!')
            continue

        if index not in avaible_index:
            print('\t Данная ячейка не может быть выбрана!')
        else:
            field[index] = "X"
            return

def sosednie(field, index):
    list = [
        (1, 4, 3), (0, 2, 4), (1, 4, 5),
        (0, 4, 6), tuple(range(0,9)), (3, 4, 8),
        (3, 4, 7), (6, 4, 8), (5, 4, 7),
    ]

    final_list = []
    for i in list[index]:
        if field[i] == " ":
            final_list.append(i)
    return final_list

def cpu_step(field):
    print('\t Сейчас ходит CPU.')

    # Прогоним варики, где уже 2 ячейки заполнены и осталась одна для победы
    for com in final:
        hum_com, cpu_com = 0, 0
        for i in com:
            if field[i] == "X":
                hum_com += 1
            elif field[i] == "O":
                cpu_com += 1
        if cpu_com == 2 and hum_com == 0:
            write_cpu_field(field, com)
            return
        elif hum_com == 2 and cpu_com == 0:
            write_cpu_field(field, com)
            return
    # Если победных ячеек нету, попробуем заполнить соседнюю ячейку с уже заполненой
    for key, value in enumerate(field):
        if value == "O":
            sosedi = sosednie(field, key)
            if len(sosedi) > 0:
                field[random.choice(sosedi)] = 'O'
                return
    field[random.choice(avaible_turn(field))] = 'O'

def write_cpu_field(field, com):
    """
    Вспомогательная функция для хода cpu, чтобы избежать дублирования кода
    :param field: текущее игровое поле
    :param com: временный объект итерации цикла
    :return: -
    """
    if field[com[0]] == " ":
        field[com[0]] = 'O'
    elif field[com[1]] == " ":
        field[com[1]] = 'O'
    elif field[com[2]] == " ":
        field[com[2]] = 'O'

def avaible_turn(field):
    """
    Получает возможные ходы
    :param field: текущее поле игры
    :return: список доступных индексов клеток
    """
    list = []
    for key, value in enumerate(field):
        if value == " ":
            list.append(key)
    return list

def is_game_finished(field):
    """
    Функция проверяет окончена ли игра
    :param field: текущее поле
    :return: True - игра окончена
    """
    for i in final:
        if field[i[0]] == field[i[1]] == field[i[2]] != " ":
            return True

    if " " not in field:
        return True

    return False

def main():
    """
    Основная логика игры
    :return: -
    """
    field = initial_field()
    print('Игра крестики-нолики.')
    print('X - человек, О - CPU')
    print('Выберете ячейку, указав ее индекс')
    print_field(field, 'Индексы ячеек выглядят так:')
    field = clear_field(field)

    answer = None
    while answer not in ('y', 'n'):
        answer = input('Хотите ходить первым? (y/n): ')
    if  answer == 'y':
        current_turn = 'human'
    else:
        current_turn = 'cpu'

    total_turn = 0

    while True:
        total_turn += 1

        print('Ход № ', total_turn)

        if current_turn == 'human':
            human_step(field)
            print_field(field)
            current_turn = 'cpu'
        else:
            cpu_step(field)
            print_field(field)
            current_turn = 'human'

        if is_game_finished(field):
            print('Игра окончена!')
            input('Для новой игры нажмите Enter')
            return


if __name__ == '__main__':
   while True:
       main()
