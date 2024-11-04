import time


def delay_decorator(delay):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f'Ждём {delay} сек. до запуска функции {func.__name__}')
            time.sleep(delay)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@delay_decorator(1)
def factorial(n):
    result = 1
    while n != 1:
        result *= n
        n -= 1
    return result


print(factorial(100))
