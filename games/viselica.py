import random
WORDS = [
    'developer',
    'macos',
    'github',
]

MAX_ERRORS = 5

def return_random_word():
    return random.choice(WORDS)

def handle_user_input():
    user_input = input('Please, input letter: ')
    return user_input

def get_initial_statuses(word):
    statuses = []
    for letter in word:
        statuses.append(False)
    return statuses

def is_game_finished(statuses, current_lives):
    if current_lives >= MAX_ERRORS:
        return True

    for status in statuses:
        if not status:
            return False

    return True

def perform_check_action(word, statuses, letter):
    if letter not in word:
        return False
    for index, l in enumerate(word):
        if letter == l:
            statuses[index] = True
    return True

def print_word(word, statuses):
    for index, letter in enumerate(word):
        if statuses[index]:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print()

def main():
    word = return_random_word()
    statuses = get_initial_statuses(word)
    current_errors = 0

    while not is_game_finished(statuses, current_errors):
        print('Errors left: ', MAX_ERRORS - current_errors)
        print_word(word, statuses)
        letter = handle_user_input()
        result = perform_check_action(word, statuses, letter)

        if not result:
            current_errors += 1

    if current_errors >= MAX_ERRORS:
        print('You lose!')
    else:
        print('You win!')

main()
