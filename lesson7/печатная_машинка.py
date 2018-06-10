import sys
from time import sleep

def typewriter(line):
    for letter in line:
        print(letter, end='')
        sys.stdout.flush()
        sleep(0.03)
    print("\n")

typewriter("Этот текст выглядит как напечатанный только что, круто?)")
typewriter("Такой эффект достигается очень легко, стоит только напечатать каждую букву с задержкой")
