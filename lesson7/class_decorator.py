class decor(object):
    count = 0

    @staticmethod
    def decorate(fn):
        def dd():
            fn()
            decor.count += 1
            print(fn.__name__, "количество выполнений:", decor.count)
        return dd


@decor.decorate
def my_func2():
    print("Я функция 2")


if __name__ == "__main__":
    for j in range(1, 4):
        my_func2()


