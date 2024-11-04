import time


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Функция {func.__name__} выполнялась {end_time - start_time} секунд')
        return result
    return wrapper


@timer_decorator
def add(a, b):
    time.sleep(3)  # поток выполнения приостанавливается на 3 секунды
    return a + b

@timer_decorator
def factorial(n):
    result = 1
    while n != 1:
        result *= n
        n -= 1
    return result

print(add(10, 100))
print(factorial(1000))
