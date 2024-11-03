# Тема: Словари
#
# Продемонстрируйте в режиме live-coding и объясните:
# - Создание словарей
# - Примеры их использования
# - Основные методы словарей
# - Генератор словарей

# ключами словаря могут быть только неизменяемые объекты:
# int, float, bool, str, tuple, frozenset
# изменяемые объекты не могут быть ключами словаря: list, set, dict

print('Создание словарей')
print()
print('# Способ 1: Фигурные скобки')
person = {
    'name': 'Alice',
    'age': 30,
    'city': 'London',
}
print(person)
print(person['name'])

print()
print('# Способ 2: функция dict()')
person = dict(name='Alice', age=30)
print(person)
print(person['name'])
person['city'] = 'Athens'
print(person)

print()
print('# Методы словарей')
print('# Доступ к значениям словаря с методом .get()')
print(person['city'])  # Athens
# print(person['lastname'])  # KeyError: 'lastname'
print(person.get('city'))  # Athens
print(person.get('lastname'))  # None
print(person.get('salary', 0))  # 0
print(person)

print()
print('# .clear() очищает словарь')
person.clear()
print(person)  # {}

print()
print('# .fromkeys() создаёт словарь из коллекции ключей')
countries = ['Poland', 'Spain', 'UK', 'Italy']
countries_none = dict.fromkeys(countries, None)
print(countries_none)  # {'Poland': None, 'Spain': None, 'UK': None, 'Italy': None}

print()
print('# .copy() копирует содержимое словаря в другой словарь')
countries_none_copy = countries_none.copy()
print(id(countries_none))  # 2106654671744
print(id(countries_none_copy))  # 2106652577024

print()
print('# .setdefault() создаёт значение по умолчанию, если такой ключ не найден')
person = {
    'name': 'Alice',
    'age': 30,
    'city': 'London',
}
print(person.get('address', 'Not found'))  # Not found
print(person)  # {'name': 'Alice', 'age': 30, 'city': 'London'}
person.setdefault('address', 'Not found')
print(person)  # {'name': 'Alice', 'age': 30, 'city': 'London', 'address': 'Not found'}
person.setdefault('name', 'Mary')
print(person)

print()
print('# .pop() - удаляет значение по ключу и ВОЗВРАЩАЕТ его')
print(person)
alice_address = person.pop('address')
print(alice_address)  # Not found
print(person)  # {'name': 'Alice', 'age': 30, 'city': 'London'}

print()
print('# .popitem() - удаляет последнее добавленное значение по ключу и ВОЗВРАЩАЕТ ПАРУ ключ-значение')
print(person)
alice_city = person.popitem()
print(alice_city)  # ('city', 'London')
print(person)  # {'name': 'Alice', 'age': 30}

print()
print('# len() - длина словаря, считает ключей в словаре')
person_len = len(person)
print(person_len)  # 2

print()
print('# in - проверяет есть ли такой ключ (НЕ ЗНАЧЕНИЕ) в словаре')
print('name' in person)  # True
print('age' in person)  # True
print('Alice' in person)  # False
print(30 in person)  # False

print()
print('# перебор элементов словаря')
capitals = {
    'Spain': 'Madrid',
    'Portugal': 'Lisbon',
    'Poland': 'Warsaw',
    'UK': 'London',
}
# capitals_list = [
#     ['Spain', 'Madrid'],
#     ['Portugal', 'Lisbon'],
#     ['Poland', 'Warsaw'],
#     ['UK', 'London'],
# ]
print('## только ключи')
for key in capitals:
    print(key)
# Spain
# Portugal
# Poland
# UK

# print()
print('## ключи и значения')
for key in capitals:
    print(key, capitals[key])
# Spain Madrid
# Portugal Lisbon
# Poland Warsaw
# UK London

print('## .items() - возвращает ПАРЫ ключ-значения')
print(capitals.items())  # dict_items([('Spain', 'Madrid'), ('Portugal', 'Lisbon'), ('Poland', 'Warsaw'), ('UK', 'London')])
# for item in capitals.items():
#     country = item[0]
#     capital = item[1]
#     print(country, capital)
for country, capital in capitals.items():
    print(country, capital)
# Spain Madrid
# Portugal Lisbon
# Poland Warsaw
# UK London
print('# .keys() - возвращает список ключей словаря')
print(capitals.keys())  # dict_keys(['Spain', 'Portugal', 'Poland', 'UK'])
print('# .values() - возвращает список значений словаря')
print(capitals.values())  # dict_values(['Madrid', 'Lisbon', 'Warsaw', 'London'])

print()
print('# генераторы словарей')
colors_en = ['Red', 'Blue', 'Green', 'Yellow', 'Purple']  # keys
colors_ru = ['Красный', 'Синий', 'Зелёный', 'Жёлтый', 'Фиолетовый']  # values
colors_matching = {colors_en[i]: colors_ru[i] for i in range(len(colors_en))}
# создаётся арифметическая прогрессия от 0 до 4 с помощью range(5)
# на каждой итерации, i принимает значение 0, 1, 2, 3, 4
# на каждой итерации мы обращаемся к двум элементам каждого списка
# первая итерация i = 0, colors_en[i] -> Red; colors_ru[i] -> Красный; создаётся пара ключ: значение в словаре
# вторая итерация i = 1 ...
# третья итерация i = 2 ...
# четвёртая итерация i = 3 ...
# последняя итерация i = 4, colors_en[i] -> Purple; colors_ru[i] -> Фиолетовый; создаётся пара ключ: значение в словаре
print(colors_matching)  # {'Red': 'Красный', 'Blue': 'Синий', 'Green': 'Зелёный', 'Yellow': 'Жёлтый', 'Purple': 'Фиолетовый'}

person = {
    'name': 'Alice',
    'age': 30,
    'study': {
        'elementary': 2011,
        'high': 2015,
        'university': 2019,
    }
}

# Тема: Кортежи и множества
#
# Продемонстрируйте в режиме live-coding и объясните:
# - Создание кортежей и множеств
# - Примеры их использования
# - Основные методы кортежей и множеств
# - Генератор множеств
print()
print('# Создание кортежей')
my_tuple = (1, 2, 3)
my_tuple2 = 1, 2, 3
my_tuple3 = tuple([1, 2, 3])
print(my_tuple)
single_tuple = (1,)
print(single_tuple)
print(my_tuple[0])
# my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment
print('# Кортеж может содержать в себе список')
print('# При этом список внутри кортежа можно изменить')
my_tuple4 = ('Alice', [30, 'New York'])
print(my_tuple4)
# my_tuple4[0] = 'Bob'  # TypeError: 'tuple' object does not support item assignment
my_tuple4[1][0] = 37
print(my_tuple4)

# Методы кортежа
print('# Методы кортежа')
person = ("Alice", [30, "New York"], 35000, "Alice", "Alice")
print(person[0])
print(person[1])
print(person[2])
print(person.count("Alice"))  # Вывод: 3
print(person.index(35000))  # Вывод: 2
print(person.index('Alice'))  # Вывод: 0
print(person.index('Alice', 1))  # Вывод: 3

print()
print('# Множества')
my_set = {2, 3, 4, 5, 5, 5, 5, 3, 4, 1, 2, 3, 1, 2, 3, 3, 3, 3}
print(my_set)
# print(my_set[0])  # TypeError: 'set' object is not subscriptable
my_set.add(6)
print(my_set)
my_set.remove(1)
print(my_set)

print()
print('# Операции над множествами')
set1 = {'apple', 'banana', 'cherry'}
set2 = {'cherry', 'melon', 'peach'}
print('# объединение |')
print(set1)
print(set2)
print(set1 | set2)  # {'banana', 'melon', 'cherry', 'apple', 'peach'}
print(set1.union(set2))  # {'banana', 'melon', 'cherry', 'apple', 'peach'}
print('# пересечение &')
print(set1)
print(set2)
print(set1 & set2)  # {'cherry'}
print(set1.intersection(set2))  # {'cherry'}
print('# симметричная разность ^')
print(set1)
print(set2)
print(set1 ^ set2)  # {'melon', 'peach', 'apple', 'banana'}
print(set1.symmetric_difference(set2))  # {'melon', 'peach', 'apple', 'banana'}
print('# разность set1 - set2')
print(set1)
print(set2)
print(set1 - set2)  # {'banana', 'apple'}
print(set1.difference(set2))  # {'banana', 'apple'}
print('# разность set2 - set1')
print(set1)
print(set2)
print(set2 - set1)  # {'peach', 'melon'}
print(set2.difference(set1))  # {'peach', 'melon'}
# set1.union_update(set2)  # делают тоже самое что .union(), но при этом меняют множество
# set1.intersection_update(set2)  # делают тоже самое что .intersection(), но при этом меняют множество
# set1.symmetric_difference_update(set2)  # делают тоже самое что .symmetric_difference(), но при этом меняют множество
# set1.difference_update(set2)  # делают тоже самое что .difference(), но при этом меняют множество

set3 = {1, 2, 1, 2, 1, 2, 3, 4}  # {1, 2, 3}
set4 = {1, 2, 1, 2, 1, 2, 3, 1, 2, 1, 2, 1, 2, 3, 1, 2, 1, 2, 1, 2, 3}  # {1, 2, 3}
print(set3 - set4)  # {4}

print()
print('# генератор множеств')
squared_set = {x ** 2 for x in range(1, 11)}
print(squared_set)
print('# множества можно перебирать в цикле')
for i in squared_set:
    print(int(i ** 0.5))


# пример
print('# пример')
l = ['Alice', 'Alice', 'Alice', 'David', 'Bob', 'David']
print(list(set(l)))