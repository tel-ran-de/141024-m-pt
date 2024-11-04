def limit_calls(max_calls):
    def decorator(func):
        calls = 0
        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls < max_calls:
                calls += 1
                return func(*args, **kwargs)
            else:
                print(f'Лимит вызова функции {func.__name__} превышен')
        return wrapper
    return decorator


@limit_calls(5)
def say_hi():
    print('Hi!')


say_hi()
say_hi()
say_hi()
say_hi()
say_hi()
say_hi()
say_hi()
say_hi()
say_hi()
say_hi()
