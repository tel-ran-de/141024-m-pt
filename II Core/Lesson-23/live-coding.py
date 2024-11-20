# Тема: Сортировка с использованием sort и sorted
# Покажите в режиме live-coding и объясните:
# - Как выполняется сортировка через sort и sorted;
# - Как выполнять сортировку по ключу.


# Пример 1: Сортировка списка in-place и создание отсортированной копии
# numbers = [5, 2, 9, 1, 5, 6]
# numbers.sort()
# print(numbers)  # [1, 2, 5, 5, 6, 9]
#
# numbers = [5, 2, 9, 1, 5, 6]
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)  # [1, 2, 5, 5, 6, 9]


# Пример 2: Сравнение различных типов данных
# print(3 < 5)  # True
# print('apple' < 'banana')  # True
# print((1, 'a') < (2, 'b'))  # True, так как 1 < 2
# print((1, 'a') < (1, 'b'))  # True, так как 'a' < 'b'


# Пример 3: Сортировка списка строк по длине
# my_list = ['kiwi', 'pineapple', 'cherry']
#
# sorted_list = sorted(my_list)  # Сортировка лексикографическая
# print(sorted_list)  # Вывод: ['cherry', 'kiwi', 'pineapple']
#
# sorted_list_by_len = sorted(my_list, key=len)  # Сортировка по длине строки
# print(sorted_list_by_len)  # Вывод: ['kiwi', 'cherry', 'pineapple']
#
# print(my_list)  # Исходный список остается неизменным
#
# my_list = ['kiwi', 'pineapple', 'cherry']
# my_list.sort(key=len)  # Сортировка по длине строки
# print(my_list)  # Вывод: ['kiwi', 'cherry', 'pineapple']


# Пример 4: Сортировка списка кортежей и строк с учетом регистра
# data = [(1, 'b'), (2, 'a'), (3, 'c')]
# sorted_data = sorted(data, key=lambda x: x[1])  # Сортировка списка кортежей по второму элементу
# print(sorted_data)  # Вывод: [(2, 'a'), (1, 'b'), (3, 'c')]
#
# words = ['banana', 'Apple', 'cherry', 'Date']
# sorted_words = sorted(words)  # Сортировка списка строк
# print(sorted_words)  # Вывод: ['Apple', 'Date','banana', 'cherry']
#
# sorted_words_ignore_case = sorted(words, key=lambda s: s.lower())  # Сортировка списка строк без учёта регистра
# print(sorted_words_ignore_case)  # Вывод: ['Apple', 'banana', 'cherry', 'Date']


# Пример 5: Сортировка словаря по значению
# my_dict = {
#     'banana': 3,
#     'apple': 4,
#     'cherry': 1,
#     'date': 2
# }
#
# sorted_dict_by_key = sorted(my_dict.items())  # Сортировка словаря по ключу
# print(sorted_dict_by_key)  # Вывод: [('apple', 4), ('banana', 3), ('cherry', 1), ('date', 2)]
#
# sorted_dict_by_value = sorted(my_dict.items(), key=lambda item: item[1])
# print(sorted_dict_by_value)  # Вывод: [('cherry', 1), ('date', 2), ('banana', 3), ('apple', 4)]
#
# def sort_by_value(item):
#     return item[1]
#
# sorted_dict_by_value = sorted(my_dict.items(), key=sort_by_value)
# print(sorted_dict_by_value)  # Вывод: [('cherry', 1), ('date', 2), ('banana', 3), ('apple', 4)]



# Тема: Cортировка с all, any, isinstance
# Покажите в режиме live-coding и объясните:
# - Как использовать isinstance, all и any при сортировке.

# Пример 6: Проверка типа данных с помощью isinstance
# x = 5
# print(isinstance(x, int))  # True
# print(isinstance(x, str))  # False

# print(type(x) is int)  # True
# print(type(x) is str)  # False

# Пример 7: Фильтрация и сортировка чисел из списка с различными типами данных
# data = [3, 'a', 5, 'b', 2]

# Фильтруем только числа для сортировки
# numbers = list(filter(lambda x: isinstance(x, int), data))
# strings = list(filter(lambda x: isinstance(x, str), data))
#
# numbers.sort()
# print(numbers)  # [2, 3, 5]
#
# strings.sort()
# print(strings)  # ['a', 'b']

# Пример 8: Проверка условий для всех или некоторых элементов списка
# numbers = [1, 2, 3, 4, 5]
# print(all(num > 0 for num in numbers))  # True, [True, True, True, True, True]
# print(any(num > 3 for num in numbers))  # True  [False, False, False, True, True]
# print(all(num > 3 for num in numbers))  # False  [False, False, False, True, True]

# Пример 9: Сортировка списка на основе условий
# data = [3, 5, 2, 8, 1]
#
# # Проверяем, все ли элементы больше 0
# if all(num > 0 for num in data):
#     sorted_data = sorted(data)
#     print(sorted_data)  # [1, 2, 3, 5, 8]
#
# # Проверяем, есть ли элементы больше 3
# if any(num > 3 for num in data):
#     sorted_data = sorted(data, reverse=True)
#     print(sorted_data)  # [8, 5, 3, 2, 1]