# Пример 1: Сортировка списка in-place и создание отсортированной копии
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print(numbers)  # [1, 2, 5, 5, 6, 9]

numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 2, 5, 5, 6, 9]

# Пример 2: Сравнение различных типов данных
3 < 5  # True
'apple' < 'banana'  # True
(1, 'a') < (2, 'b')  # True, так как 1 < 2
(1, 'a') < (1, 'b')  # True, так как 'a' < 'b'

# Пример 3: Сортировка списка строк по длине
my_list = ['apple', 'banana', 'cherry']
sorted_list = sorted(my_list, key=len)  # Сортировка по длине строки
print(sorted_list)  # Вывод: ['apple', 'cherry', 'banana']
print(my_list)  # Исходный список остается неизменным

my_list = ['apple', 'banana', 'cherry']
my_list.sort(key=len)  # Сортировка по длине строки
print(my_list)  # Вывод: ['apple', 'cherry', 'banana']

# Пример 4: Сортировка списка кортежей и строк с учетом регистра
data = [(1, 'b'), (2, 'a'), (3, 'c')]
sorted_data = sorted(data, key=lambda x: x[1])  # Сортировка списка кортежей по второму элементу
print(sorted_data)  # Вывод: [(2, 'a'), (1, 'b'), (3, 'c')]

words = ['banana', 'Apple', 'cherry', 'date']
sorted_words = sorted(words, key=lambda s: s.lower())  # Сортировка списка строк с учетом регистра
print(sorted_words)  # Вывод: ['Apple', 'banana', 'cherry', 'date']

# Пример 5: Сортировка словаря по ключу
my_dict = {
    'banana': 3,
    'apple': 4,
    'cherry': 1,
    'date': 2
}
sorted_dict_by_key = sorted(my_dict.items(), key=lambda item: item[0])  # Сортировка словаря по ключу
print(sorted_dict_by_key)  # Вывод: [('apple', 4), ('banana', 3), ('cherry', 1), ('date', 2)]

# Пример 6: Проверка типа данных с помощью isinstance
x = 5
print(isinstance(x, int))  # True
print(isinstance(x, str))  # False

# Пример 7: Фильтрация и сортировка чисел из списка с различными типами данных
data = [3, 'a', 5, 'b', 2]

# Фильтруем только числа для сортировки
numbers = list(filter(lambda x: isinstance(x, int), data))
numbers.sort()
print(numbers)  # [2, 3, 5]

# Пример 8: Проверка условий для всех или некоторых элементов списка
numbers = [1, 2, 3, 4, 5]
print(all(num > 0 for num in numbers))  # True
print(any(num > 3 for num in numbers))  # True

# Пример 9: Сортировка списка на основе условий
data = [3, 5, 2, 8, 1]

# Проверяем, все ли элементы больше 0
if all(num > 0 for num in data):
    sorted_data = sorted(data)
    print(sorted_data)  # [1, 2, 3, 5, 8]

# Проверяем, есть ли элементы больше 3
if any(num > 3 for num in data):
    sorted_data = sorted(data, reverse=True)
    print(sorted_data)  # [8, 5, 3, 2, 1]
