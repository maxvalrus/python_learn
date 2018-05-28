try:
    value_in = int(input('Введите число: '))
except:
    raise SystemExit("Введите число, а не строку!")

try:
    if value_in % 2 == 0:
        raise ValueError
    if value_in < 0:
        raise TypeError
    if value_in > 10:
        raise IndexError

except ValueError:
    print('Число четное')
except TypeError:
    print('Число меньше 0')
except IndexError:
    print('Число больше 10')
