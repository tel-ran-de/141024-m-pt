# Простой декоратор
def my_decorator(func):
    def wrapper():
        print("Что-то происходит перед функцией.")
        func()
        print("Что-то происходит после функции.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Вывод:
# Что-то происходит перед функцией.
# Hello!
# Что-то происходит после функции.


# Декоратор с аргументами функции
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Аргументы функции:", args, kwargs)
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name, age):
    print(f"Привет, {name}. Тебе {age} лет.")

greet("Алиса", 30)
# Вывод:
# Аргументы функции: ('Алиса', 30) {}
# Привет, Алиса. Тебе 30 лет.


# Декоратор с параметрами
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Привет!")

say_hello()
# Вывод:
# Привет!
# Привет!
# Привет!