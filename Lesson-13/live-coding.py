# Тема: функции
#
# Покажите в формате live-coding и объясните:
# - Процесс создания и вызова функции.
# - Использование оператора return для возврата значения из функции.
# - Использования именованных аргументов, что делает вызов функции более гибким.

# функция print() ничего не возвращает, она просто печатает значения в консоль
# это значит, что в этой функции нет оператора return
# print('Hello world!')
# x = print('Hello world!')
# print(x)
print('# Объявление и вызов функций')


def greet(name):
    print(f'Hello, {name}')


greet('Alice')  # Hello, Alice
greet(name='Bob')  # Hello, Bob
n = greet('Hanna')  # Hello, Hanna
print(n)  # None


print('\n# оператор return')


def add(a, b):
    return a + b


add_2_3 = add(a=2, b=3)
print(add_2_3)  # 5

add_3_5 = add(a=3, b=5)
print(add_3_5)  # 8


print('\n# параметры по умолчанию')


def greet(name, greeting='Hello'):
    print(f'{greeting}, {name}')


greet('Boris')  # Hello, Boris
greet('Boris', 'Hi')  # Hi, Boris
greet(name='Hanna', greeting='Merhaba')


# print('\n# функция, которая возвращает степень числа')
def get_power(base, power):
    return base ** power


print(get_power(3, 3))
print(get_power(2, 3))
print(get_power(2, 9))


print('\n# возврат нескольких значений из функции')
def get_square_cube(x):
    square = x ** 2
    cube = x ** 3
    return square, cube


square_7, cube_7 = get_square_cube(x=7)
print(square_7)  # 49
print(cube_7)  # 343


# Тема: args, kwargs
# Покажите в формате live-coding и объясните:
# - Как работать с произвольным числом параметров с помощью *args и *kwargs.
print('\n# *args произвольное количество неименованных (позиционные) аргументов')


def sum_even(*args):
    # result = 0
    # for i in args:
    #     if i % 2 == 0:
    #         result = result + i
    # return result
    print(type(args))
    return sum([i for i in args if i % 2 == 0])


print(sum_even(1, 2, 3, 4, 5, 6, 7, 8, 9))  # 20
print(sum_even(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))  # 42
print(sum_even(4))  # 4


print()
print('# poppuri')
def poppuri(*args):
    for el in args:
        if isinstance(el, str):
            print(f'{el} - строка')
        elif isinstance(el, int):
            print(f'{el} - целое число')
        else:
            print(f'Мы не знаем что такое {el}')

poppuri(1, 2, 3, 'stroka', 7.9, True, False, 10)
# 1 - целое число
# 2 - целое число
# 3 - целое число
# stroka - строка
# Мы не знаем что такое 7.9
# True - целое число
# False - целое число
# 10 - целое число


print('\n# **kwargs произвольное количество именованных аргументов')
# Примеры с *args и **kwargs


def describe_person(name, age, *args, **kwargs):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print("Additional info:", args)
    print("Other details:", kwargs)
    if kwargs.get('salary'):
        print(f'{name} зарабатывает {kwargs["salary"]} ')


describe_person('Alice', 30, 'Engineer', 'UK', salary=3000, hair='blond', height=168)
# Name: Alice
# Age: 30
# Additional info: ('Engineer', 'UK')
# Other details: {'salary': 3000, 'hair': 'blond', 'height': 168}
# Alice зарабатывает 3000

print()
describe_person('Bob', 27, 'Canada', height=175)
# Name: Bob
# Age: 27
# Additional info: ('Canada',)
# Other details: {'height': 175}
