def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

x = fib()
for i in range(0, 10):
    print(next(x))