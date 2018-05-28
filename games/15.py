import random

EMPTY_MARK = 'x'

MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}
def shuffle_field():
    """
    Создает поле игры
    :return: list из 16 рандомных клеток
    """
    field = list(range(1, 17))
    field[-1] = EMPTY_MARK
    #random.shuffle(field)

    possible_moves = list(MOVES.keys())
    for move in range(10):
        random_move = random.choice(possible_moves)
        try:
            field = perform_move(field, random_move)
        except IndexError:
            continue

    return field

def print_field(field):
    """
    Печатает поле игры в консоль
    :param field:
    :return:
    """
    for i in range(0, 16, 4):
        print(field[i:i+4])
    print('\n')

def is_game_finished(field):
    ideal = list(range(1, 16))
    ideal.append(EMPTY_MARK)
    return ideal == field

def handle_user_input():
    while True:
        user_move = input('Please, input your move: ')
        if user_move in MOVES.keys():
            return user_move

def perform_move(field, key):
    delta = MOVES[key]
    current_position = field.index(EMPTY_MARK)

    if key == 's' and current_position > 12:
        raise IndexError('Cant move down')
    if key == 'd' and current_position % 4 == 3:
        raise IndexError('Cant move right')
    if key == 'w' and current_position < 4:
        raise IndexError('Cant move up')
    if key == 'a' and current_position % 4 == 0:
        raise IndexError("Cant move left")

    delta = MOVES[key]
    field[current_position], field[current_position + delta] = \
        field[current_position + delta], field[current_position]

    return field

def main():
    field = shuffle_field()

    while not is_game_finished(field):
        try:
            print_field(field)
            move = handle_user_input()
            field = perform_move(field, move)
        except IndexError as e:
            print(e)

    print('Game is finished!')

main()

