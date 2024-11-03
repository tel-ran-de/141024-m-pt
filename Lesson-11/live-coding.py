# Тема: Вложенные циклы: for вложенный в for, for вложенный в while.
# # Покажите и объясните использования вложенных циклов в формате live-coding.

# grades = [
#     ["Alice", 90, 85, 88],
#     ["Bob", 78, 81, 85],
#     ["Charlie", 92, 88, 91]
# ]

# в *scores попадает часть списка
# for student in grades:  # ["Alice", 90, 85, 88], ["Bob", 78, 81, 85], ["Charlie", 92, 88, 91]
#     name, *scores = student  # name = "Alice", scores = [90, 85, 88]
#     # name, score1, score2, score3 = student
#     # scores = [score1, score2, score3]
#     average = sum(scores) / len(scores)
#     print(f"{name}: {average}")


# cities = ['Tashkent', 'Tbilisi', 'Warsaw']
# for city in cities:
#     for char in city:
#         print(char)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
#
#
# for row in matrix:
#     for element in row:
#         print(element)

# numbers = list(range(1, 6))  # [1, 2, 3, 4, 5]
# i = 0

# for i in numbers:
# while i < len(numbers):
#     for j in range(numbers[i]):
#         print(j, end=' ')
#     print()
#     i += 1

# Тема: Генераторы списков (List comprehension). Вложенные циклы и вложенные генераторы списков.
# Продемонстрируйте и объясните использование генераторов списков.
# В том числе использование вложенных генераторов списков.
# print('Генераторы списков (List comprehension)')
# numbers = list(range(1, 6))  # [1, 2, 3, 4, 5]
# squares = []
# for i in numbers:
#     squares.append(i ** 2)
# squares = [i ** 2 for i in numbers]
# squares = [i ** 2 for i in range(1, 6)]
# print(squares)

# print('Использование генератора списков для обработки строк')
# text = 'Hello, world! Have a Good day!'
# vowels = [char for char in text if char.lower() in 'aeiou']
# print(vowels)
# words = [word for word in text.split() if word.istitle()]  # ['Hello,', 'world!', 'Have', 'a', 'Good', 'day!']
# print(words)

# print('Использование генератора для обработки матриц')
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# flattened = [element for row in matrix for element in row]
# print(flattened)

# print('Вложенные генераторы списков')
# n = 10
# matrix =[[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]
# print(matrix)

print('Вложенные генераторы для обработки матриц')
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
# вариант через цикл
# normalized = []
# for row in matrix:
#     new_row = []
#     for element in row:
#         new_row.append(element / 10)
#     normalized.append(new_row)
# вариант через генерацию списков
# normalized = [[element / 10 for element in row] for row in matrix]
# print(normalized)

# Тема: Итератор и итерируемые объекты. Функции iter и next. Сравнение iter и next с циклом for и функцией range.
# Продемонстрируйте создание итератора и использование функций iter и next.
# print('Итератор и итерируемые объекты.')
cities = ['Istanbul', 'Batumi', 'Berlin', 'Porto', 'Beijin']
# for city in cities:
#     print(city)
# city_iter = iter(cities)
# # print(city_iter)
# print(next(city_iter))
# print(next(city_iter))
# print(next(city_iter))
# print(next(city_iter))
# print(next(city_iter))

# print('считывание файла')
# file = open('live-coding.py', encoding='utf-8')
# file_iter = iter(file)
# print(next(file_iter))
# print(next(file_iter))
# print(next(file_iter))
# print(next(file_iter))
# print(next(file_iter))
# file.close()

# print('ручная итерация')
def manual_iteration(iterable):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
            print(item)
        except StopIteration:
            break

# for city in cities:
#     print(city)

manual_iteration(cities)
