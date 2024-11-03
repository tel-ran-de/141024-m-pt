# Тема 1. Продемонстрируйте и объясните в режиме live-coding:
# - создание списка,
print('# - создание списка')
fruits = ['apple', 'banana', 'peach', 'melon', 'lemon']
print(fruits)

# - доступ к элементам списка,
print('# - доступ к элементам списка')
print(fruits[0])
print(fruits[2])

# - изменение значения элемента списка,
fruits[1] = 'orange'
print(fruits)

# name = 'Steve'
# name[0] = 'O'
# TypeError: 'str' object does not support item assignment

# - получение среза,
print(fruits[1:3])  # ['orange', 'peach']

# - создание и работу с вложенными списками.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
row2_col1 = matrix[1][0]
print(row2_col1)  # 4
row3_col2 = matrix[2][1]
print(row3_col2)  # 8
row1 = matrix[0]
print(row1)  # [1, 2, 3]

users = [
    ['user1', 'password1', 'email1@example.com'],
    ['user2', 'password2', 'email2@example.com'],
    ['user3', 'password3', 'email3@example.com'],
]
u1 = users[0]
print(u1)  # ['user1', 'password1', 'email1@example.com']
u2 = users[0][2]
print(u2)  # email1@example.com
u3 = users[0][2][6]
print(u3)  # @


print()
# Тема 2. Продемонстрируйте и объясните в режиме live-coding:
# - Использование различных методов списков.
print('\n# - Использование различных методов списков.')
numbers = [1, 2, 4]
print(numbers)  # [1, 2, 4]

print('\n# - метод .append() - добавляет ОДИН элемент')
numbers.append(6)
print(numbers)  # [1, 2, 4, 6]

print('\n# - метод .extend() - расширяет список другим списком')
numbers.extend([9, 10])
print(numbers)  # [1, 2, 4, 6, 9, 10]
numbers.append([11, 12])
print(numbers)  # [1, 2, 4, 6, 9, 10, [11, 12]]

print('\n# - метод .pop() - удаляет элемент (по умолчанию последний) и ВОЗВРАЩАЕТ его')
last_element = numbers.pop()
print(last_element)  # [11, 12]
print(numbers)  # [1, 2, 4, 6, 9, 10]
first_element = numbers.pop(0)
print(first_element)  # 1
print(numbers)  # [2, 4, 6, 9, 10]

print('\n# - метод .insert() - вставляет значение по указанному индексу')
numbers.insert(3, 7)
print(numbers)  # [2, 4, 6, 7, 9, 10]

print('\n# - метод .remove() - удаляет указанное значение (первое вхождение)')
numbers.append(6)
numbers.append(6)
numbers.append(6)
print(numbers)  # [2, 4, 6, 7, 9, 10, 6, 6, 6]
numbers.remove(6)
print(numbers)  # [2, 4, 7, 9, 10, 6, 6, 6]
numbers.remove(6)
print(numbers)  # [2, 4, 7, 9, 10, 6, 6]

print('\n# - метод .index() - возвращает индекс значения (первое вхождение)')
# index_of_5 = numbers.index(5)  # ValueError: 5 is not in list
numbers.insert(3, 2)
print(numbers)  # [2, 4, 7, 2, 9, 10, 6, 6]
print(numbers.index(2))  # 0
print(numbers.index(2, 1))  # 3

print('\n# - метод .reverse() - разворачивает список')
numbers.reverse()
print(numbers)  # [6, 6, 10, 9, 2, 7, 4, 2]

print('\n# - метод .sort() - сортирует список (ИЗМЕНЯЕТ ЕГО)')
numbers.sort()
print(numbers)  # [2, 2, 4, 6, 6, 7, 9, 10]
numbers.sort(reverse=True)
print(numbers)  # [10, 9, 7, 6, 6, 4, 2, 2]

print('\n# - метод .count() - подсчитывает элементы')
counts_of_6 = numbers.count(6)
print(counts_of_6)  # 2

print('\n# - метод .clear() - очищает список')
numbers.clear()
print(numbers)  # []

print('\n# - функция len() - подсчитывает количество элементов в списке')
progression = list(range(10))
print(progression)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(progression))  # 10

print('\n# - функция sum() - подсчитывает сумму элементов')
print(sum(progression))  # 45

print('\n# - функция min() - выводит минимальный элемент')
print(min(progression))  # 0

print('\n# - функция max() - выводит максимальный элемент')
print(max(progression))  # 9

print('\n# - функция sorted() - сортирует список (НЕ МЕНЯЕТ ЕГО)')
sorted(progression, reverse=True)
print(progression)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
reversed_progression = sorted(progression, reverse=True)
print(reversed_progression)  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# - Сравнение списков
print('\n# - Сравнение списков')
print([1, 2, 3] < [1, 2, 4])  # True
print([5, 2, 7] < [1, 2, 3, 4])  # False
print([3] < [1, 2, 3])  # False

# - Изменяемость списков и неизменяемость строк
print('\n# - Изменяемость списков и неизменяемость строк')
x = [1, 2, 3]
y = x  # мы просто создали ещё одну ссылку на тот же список
print(x)  # [1, 2, 3]
print(y)  # [1, 2, 3]
y.append(5)
print(x)  # [1, 2, 3, 5]
print(y)  # [1, 2, 3, 5]
print(id(x))  # 2489709793984
print(id(y))  # 2489709793984

print('\n# копирование списков')
x1 = x[:]
print(x1)  # [1, 2, 3, 5]
print(id(x1))  # 2575081968512
x2 = [*x]  # распаковали список и получили значения 1, 2, 3, 5 -> [1, 2, 3, 5]
print(x2)  # [1, 2, 3, 5]
print(id(x2))  # 1853610103872
x3 = x.copy()
print(x3)  # [1, 2, 3, 5]
print(id(x3))  # 2515763303488
