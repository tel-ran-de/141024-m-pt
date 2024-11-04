# Тема: Декораторы
#
# Продемонстрируйте создание и использование декораторов на примерах.
# Объясните механизм работы декоратора, передачу аргументов.
#
# Например, напишите декоратор timeit, который замеряет и выводит время выполнения декорируемой функции.
# В качестве декорируемых функций используйте две функции, одна из которых генерит четные числа от 0 до 10 000
# через цикл for и метод append. А другая генерит эти же цифры через генератор списков.


# Простой декоратор
print('# Простой декоратор')
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Что-то происходит перед функцией.")
        func(*args, **kwargs)
        print("Что-то происходит после функции.")
    return wrapper


# def say_hello(name):
#     print(f'Hello, {name}!')


# decorated_say_hello = my_decorator(say_hello)
# decorated_say_hello('Alice')


@my_decorator
def say_hello(name):
    print(f'Hello, {name}!')


say_hello('Alice')
