# Продемонстрируйте и объясните в режиме live-coding:
# - Упаковку аргументов с args для списков и кортежей
# - Упаковку аргументов с kwargs для словарей
# - Распаковку с операторами * и **

print('# - Упаковку аргументов с *args для списков и кортежей')
# def sum_squares(a, b, c, d):
#     return a*a + b*b + c*c + d*d
#
def sum_squares_args(*args):
    print(type(args))
    return sum([i ** 2 for i in args])

print(sum_squares_args(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3))  # Вывод: 56


# Упаковка именованных аргументов с **kwargs
print('# Упаковка именованных аргументов с **kwargs')
def show_info(**kwargs):
    separator = '\n'
    if 'separator' in kwargs:
        separator = kwargs.get('separator')
        del kwargs['separator']
    for key, value in kwargs.items():
        print(f"{key}: {value}", end=separator)

show_info(name="Alice", age=30, grade='middle', separator=' - ')
# name: Alice - age: 30 - grade: middle -
print()
print()
show_info(name="Alice", age=30, city='New York', salary=5000, height=158)
# name: Alice
# age: 30
# city: New York
# salary: 5000
# height: 158

# - Распаковка с операторами * и **
print()
print('# - Распаковка с операторами * и **')
l1 = [1, 2, True, 'value', 17, 9]
# v1, v2, v3, v4, v5, v6 = [1, 2, True, 'value', 17, 9]
x, y, *z = l1
print(x)
print(y)
print(z)
#
print()
*x, y, z = l1
print(x)
print(y)
print(z)
#
print()
x, *y, z = l1
print(x)
print(y)
print(z)
#
print()
print(l1, sep=' - ')
# print([1, 2, True, 'value', 17, 9], sep=' - ')
# [1, 2, True, 'value', 17, 9]
print(*l1, sep=' - ')
# print(1, 2, True, 'value', 17, 9, sep=' - ')
# 1 - 2 - True - value - 17 - 9

print()
l2 = [*l1]
# l2 = [1, 2, True, 'value', 17, 9]
print(l2)

#
#
# # Распаковка словаря с помощью **
# print('# Распаковка словаря с помощью **')
# data = {"name": "Bob", "age": 25}
# def print_info(name, age):
#     return f"Name: {name}, Age: {age}"
#
# print(print_info(**data))
# # Вывод: Name: Bob, Age: 25
#
#
# # Продемонстрируйте в режиме live-coding и объясните работу:
# # - Глобальных и локальных переменных
# # - Ключевых слов global и nonlocal
# # - Вложенных функций
# # - Замыкания
#
print()
print('#####################################')
print('# - Глобальныe и локальныe переменныe')
gl_var = 0

def f():
    gl_var = 1
    print(gl_var + 10)

f()
print(gl_var)
#
# # глобальная область видимости ничего не знает о переменных расположенных в локальных областях видимости (то есть в функциях)
# def f2():
#     a = 10
#     print(a)
# print(a)
#
print()
print('оператор global')
gl_var2 = 1
print(f'gl_var2 = {gl_var2}')

def f3():
    global gl_var2
    gl_var2 += 1
    return gl_var2

def f4():
    f3()

f3()
f3()
f3()
print(f'gl_var2 = {gl_var2}')
f4()
print(f'gl_var2 = {gl_var2}')
#
# Использование ключевого слова nonlocal
print()
print('# Использование ключевого слова nonlocal')
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner
#
counter1 = outer()
print(counter1())  # Вывод: 1
print(counter1())  # Вывод: 2
print(counter1())  # Вывод: 3
# print(outer()())
# print(outer()())
# print(outer()())
#
#
# print()
# print('# global')
# x = 1  # global
# def func1():
#     x = 2
#     def func2():
#         global x
#         print('New print: ', x)
#         x = 3
#         print(f'Func2: {x}')
#     func2()
#     print(f'Func1: {x}')
#
# func1()
# print(f'Global: {x}')
