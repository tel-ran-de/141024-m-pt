# Примеры для урока 7: Словари, кортежи, множества

# Словари

# Что такое словари и зачем они нужны
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(person["name"])  # Вывод: Alice

# Синтаксис словарей. Способы создания словарей
# Способ 1: Фигурные скобки
person = {"name": "Alice", "age": 30}
print(person)  # Вывод: {'name': 'Alice', 'age': 30}

# Функция dict()
person = dict(name="Alice", age=30)
print(person)  # Вывод: {'name': 'Alice', 'age': 30}

# Доступ к значениям в словаре
person = {"name": "Alice", "age": 30}
print(person["name"])  # Вывод: Alice
print(person.get("age"))  # Вывод: 30

# Добавление и удаление элементов в словаре
# Добавление элемента
person["city"] = "New York"
print(person)  # Вывод: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Удаление элемента
del person["age"]
print(person)  # Вывод: {'name': 'Alice', 'city': 'New York'}

# Функции len, in, not in, del для словарей
person = {"name": "Alice", "age": 30, "city": "New York"}
print(len(person))  # Вывод: 3
print("name" in person)  # Вывод: True
print("address" not in person)  # Вывод: True
del person["city"]
print(person)  # Вывод: {'name': 'Alice', 'age': 30}

# Методы словаря: fromkeys, clear, copy
# fromkeys
keys = ['name', 'age', 'city']
person = dict.fromkeys(keys, None)
print(person)  # Вывод: {'name': None, 'age': None, 'city': None}

# clear
person.clear()
print(person)  # Вывод: {}

# copy
original = {"name": "Alice"}
copy = original.copy()
print(copy)  # Вывод: {'name': 'Alice'}

# Методы словаря: get, setdefault
person = {"name": "Alice", "age": 30}
print(person.get("name"))  # Вывод: Alice
print(person.get("address", "Not Found"))  # Вывод: Not Found
person.setdefault("city", "Unknown")
print(person)  # Вывод: {'name': 'Alice', 'age': 30, 'city': 'Unknown'}

# Методы словаря: pop, popitem
person = {"name": "Alice", "age": 30}
age = person.pop("age")
print(age)  # Вывод: 30
print(person)  # Вывод: {'name': 'Alice'}
item = person.popitem()
print(item)  # Вывод: ('name', 'Alice')
print(person)  # Вывод: {}

# Методы словаря: keys, values, items, update
person = {"name": "Alice", "age": 30}
print(person.keys())  # Вывод: dict_keys(['name', 'age'])
print(person.values())  # Вывод: dict_values(['Alice', 30])
print(person.items())  # Вывод: dict_items([('name', 'Alice'), ('age', 30)])
person.update({"city": "New York"})
print(person)  # Вывод: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Перебор элементов словаря в цикле
person = {"name": "Alice", "age": 30, "city": "New York"}
for key in person:
    print(key, person[key])  # Вывод: name Alice \n age 30 \n city New York
for key, value in person.items():
    print(key, value)  # Вывод: name Alice \n age 30 \n city New York

# Генераторы словарей
keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]
person = {keys[i]: values[i] for i in range(len(keys))}
print(person)  # Вывод: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Сравнение генераторов словарей и генераторов списков
# Генератор словаря
keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]
person = {keys[i]: values[i] for i in range(len(keys))}
print(person)  # Вывод: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Генератор списка
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)  # Вывод: [1, 4, 9, 16, 25]

# Кортежи

# Кортежи: синтаксис, создание кортежа, распаковка
# Создание кортежа
person = ("Alice", 30, "New York")
print(person)  # Вывод: ('Alice', 30, 'New York')

# Распаковка кортежа
name, age, city = person
print(name, age, city)  # Вывод: Alice 30 New York

# Сравнение кортежей и списков
# Список
my_list = [1, 2, 3]
my_list[0] = 0  # Изменение элемента
print(my_list)  # Вывод: [0, 2, 3]

# Кортеж
my_tuple = (1, 2, 3)
# my_tuple[0] = 0  # Ошибка: кортежи неизменяемы

# Списки внутри кортежей. Методы кортежа
# Кортеж со списками
person = ("Alice", [30, "New York"])
print(person)  # Вывод: ('Alice', [30, 'New York'])

# Методы кортежа
print(person.count("Alice"))  # Вывод: 1
print(person.index([30, "New York"]))  # Вывод: 1

# Множества

# Множества: синтаксис, создание, методы
# Создание множества
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Вывод: {1, 2, 3, 4, 5}

# Добавление элемента
my_set.add(6)
print(my_set)  # Вывод: {1, 2, 3, 4, 5, 6}

# Удаление элемента
my_set.remove(3)
print(my_set)  # Вывод: {1, 2, 4, 5, 6}

# Операции над множествами
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Объединение
union_set = set1.union(set2)
print(union_set)  # Вывод: {1, 2, 3, 4, 5}

# Пересечение
intersection_set = set1.intersection(set2)
print(intersection_set)  # Вывод: {3}

# Разность
difference_set = set1.difference(set2)
print(difference_set)  # Вывод: {1, 2}

# Сравнение списков и множеств
# Список
my_list = [1, 2, 2, 3]
print(my_list)  # Вывод: [1, 2, 2, 3]

# Множество
my_set = set(my_list)
print(my_set)  # Вывод: {1, 2, 3}

# Генераторы множеств
# Генератор множества
numbers = [1, 2, 3, 4, 5]
squared_set = {x**2 for x in numbers}
print(squared_set)  # Вывод: {1, 4, 9, 16, 25}

# Сравнение генераторов множеств и генераторов списков
# Генератор множества
numbers = [1, 2, 3, 4, 5]
squared_set = {x**2 for x in numbers}
print(squared_set)  # Вывод: {1, 4, 9, 16, 25}

# Генератор списка
squared_list = [x**2 for x in numbers]
print(squared_list)  # Вывод: [1, 4, 9, 16, 25]
