my_list = [5, 'test', 19, 24, (5,6,7), 48, [1,2]]

inp = input('Введите индекс элемента: ')

try:
    inp = int(inp)
except:
    #dprint('Введите число, а не строку!')
    raise ValueError('Некорректное значение!')

if 0 > inp or inp > len(my_list) - 1:
    print('Индекс выходит за границы массива')
    raise SystemExit

print(my_list[inp])

