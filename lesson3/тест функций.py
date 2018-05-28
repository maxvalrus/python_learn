def my_func(x,y):
    try:
        x = int(x)
        y = int(y)
    except:
        raise SystemExit('Введите число!')

    if x > 0 and y > 0:
        return x + y
    elif x < 0 and y < 0:
        return x - y
    elif (x < 0 and y > 0) or (x > 0 and y < 0):
        return 0

x = input('Введите Х: ')
y = input('Введите Y: ')

print(my_func(x, y))
