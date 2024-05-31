import time

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970


# Write your code below 👇


def speed_calc_decorator(func):
    def wrapper():
        before = time.time()
        func()
        after = time.time()
        print(f"{func.__name__} run speed: {after - before}s")

    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


slow_function()
fast_function()