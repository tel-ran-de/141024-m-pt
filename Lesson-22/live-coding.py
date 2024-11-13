# Тема: map, filter, zip
# Покажите в режиме live-coding и объясните:
# - Использование функций map, filter, zip
# # Пример 1: Применение функции ко всем элементам списка с помощью map
# def square(x):
#     return x * x
#
# numbers = [1, 2, 3, 4, 5]
# map первым аргументом принимают функцию, а вторым итерируемый объект
# и возвращает итератор
# squared_numbers = map(square, numbers)
# print(list(squared_numbers))  # Результат: [1, 4, 9, 16, 25]

# C помощью цикла
# squares = []
# for number in numbers:
#     squares.append(square(number))
# print(squares)
#
# # Пример 2: Фильтрация списка с помощью функции filter
# def is_even(x):
#     return x % 2 == 0
#
# numbers = [1, 2, 3, 4, 5, 6]
# # filter первым аргументом принимают функцию, а вторым итерируемый объект
# # и возвращает итератор
# even_numbers = filter(is_even, numbers)
# print(list(even_numbers))  # Результат: [2, 4, 6]
#
# # Пример 3: Объединение двух списков в список кортежей с помощью zip
# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]
# cities = ["Tashkent", "Tbilisi", "Warsaw"]
# zip попарно объединяет элементы из двух последовательностей в кортежи
# combined = zip(names, ages, cities)
# print(list(combined))  # Вывод: [('Alice', 25, 'Tashkent'), ('Bob', 30, 'Tbilisi'), ('Charlie', 35, 'Warsaw')]
#
# # Пример 4: Итерация по двум спискам одновременно с помощью zip
# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]
# d = {}
# for name, age in zip(names, ages):
#     d[name] = age
#     print(f"{name} is {age} years old")
# print(d)









# Тема: map, filter, zip для итераторов, генераторов и файлов с лямбда функциями
# Покажите в режиме live-coding и объясните:
# - Использование lambda-функций в map, filter, zip
# - Использование map, filter, zip при работе с генераторами, файлами

# # Пример 5: Лямбда-функция для сложения двух чисел
# add = lambda x, y: x + y
#
# # Эквивалентная обычная функция
# def add(x, y):
#     return x + y
#
# # Пример 6: Лямбда-функции для различных операций
# # лямбда функция
# concat_strings = lambda s1, s2: s1 + " " + s2
#
# # аналог через обычную функцию
# def concat_strings_def(s1, s2):
#     return s1 + " " + s2
#
# # лямбда функция
# abs_value = lambda x: x if x >= 0 else -x
#
# # аналог через обычную функцию
# def abs_value_def(x):
#     return x if x >= 0 else -x
#
# # Пример 7: Применение лямбда-функции ко всем элементам списка с помощью map
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = map(lambda x: x * x, numbers)
# print(list(squared_numbers))  # Результат: [1, 4, 9, 16, 25]
#
# # Пример 8: Фильтрация списка с помощью лямбда-функции и filter

# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = filter(lambda x: x % 2 == 0, numbers)
# print(list(even_numbers))  # Результат: [2, 4, 6]
#
# # Пример 9: Генерация последовательности и применение функции к ее элементам
# def number_generator(n):
#     for i in range(n):
#         yield i
#
# gen = number_generator(5)
# squared = map(lambda x: x ** 2, gen)
# print(list(squared))  # [0, 1, 4, 9, 16]
#
# # Пример 10: Чтение строк из файла и фильтрация с помощью лямбда-функции
def file_reader(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# def filter_lines(line):
#     return 'Python' in line

lines = file_reader('text_files/example.txt')
filtered_lines = filter(lambda line: 'Python' in line, lines)
print(list(filtered_lines))










