from functools import wraps
from time import time, sleep

def time_deco(fn):
    @wraps(fn)
    def deco():
        start = time()
        fn()
        stop = time()
        print("Time:", stop-start)
    return deco

@time_deco
def my_func():
    sleep(1)
    print([i for i in range(1, 1000) if i % 2 == 0])

if __name__ == "__main__":
    my_func()