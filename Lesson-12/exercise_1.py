# Задача 1: Анализ данных о сотрудниках
# У вас есть словарь, содержащий информацию о сотрудниках компании.
# Необходимо провести различные операции с этими данными.
#
# Задание:
# 1. Выведите имена всех сотрудников.
# 2. Найдите и выведите общую сумму зарплат всех сотрудников.
# 3. Добавьте нового сотрудника "David" с возрастом 28, отделом "IT" и зарплатой 6500.
# 4. Обновите зарплату "Alice" до 5500.
# 5. Удалите сотрудника "Charlie".
# 6. Выведите данные о каждом сотруднике в формате:
# "Имя: {name}, Возраст: {age}, Отдел: {department}, Зарплата: {salary}"
#
employees = {
    "Alice": {"age": 30, "department": "HR", "salary": 5000},
    "Bob": {"age": 25, "department": "IT", "salary": 6000},
    "Charlie": {"age": 35, "department": "Finance", "salary": 7000}
}
# 0. Исследуем словарь.
print('# 0. Исследуем словарь.')
for key in employees.keys():
    print(key)

print()

for values in employees.values():
    print(values)

print()

for item in employees.items():
    print(item)

print()
# 1. Выведите имена всех сотрудников.
print('# 1. Выведите имена всех сотрудников.')
# print(f'{list(employees.keys())}')
for name in employees:
    print(name)

print()
# 2. Найдите и выведите общую сумму зарплат всех сотрудников.
print('# 2. Найдите и выведите общую сумму зарплат всех сотрудников.')

summator = 0
# for name, info in employees.items():
for info in employees.values():
    summator = summator + info['salary']
print(summator)

print()
# 3. Добавьте нового сотрудника "David" с возрастом 28, отделом "IT" и зарплатой 6500.
print('# 3. Добавьте нового сотрудника "David" с возрастом 28, отделом "IT" и зарплатой 6500.')
# new_info = {"age": 28, "department": "IT", "salary": 6500}
# employees['David'] = new_info
employees['David'] = {"age": 28, "department": "IT", "salary": 6500}

for name, info in employees.items():
    print(f'{name}: {info}')

print()
# 4. Обновите зарплату "Alice" до 5500.
print('# 4. Обновите зарплату "Alice" до 5500.')
employees['Alice']['salary'] = 5500

for name, info in employees.items():
    print(f'{name}: {info}')

print()
# 5. Удалите сотрудника "Charlie".
print('# 5. Удалите сотрудника "Charlie".')
del employees['Charlie']

for name, info in employees.items():
    print(f'{name}: {info}')

print()
# 6. Выведите данные о каждом сотруднике в формате: "Имя: {name}, Возраст: {age}, Отдел: {department}, Зарплата: {salary}"
print('# 6. Выведите данные о каждом сотруднике в формате: "Имя: {name}, Возраст: {age}, Отдел: {department}, Зарплата: {salary}"')
for name, info in employees.items():
    age, department, salary = info.values()
    print(f'Имя: {name}, Возраст: {age}, Отдел: {department}, Зарплата: {salary}')
    # print(f"Имя: {name}, Возраст: {info['age']}, Отдел: {info['department']}, Зарплата: {info['salary']}")


# Задача 2: Управление запасами товаров
# У вас есть словарь, содержащий информацию о запасах товаров в магазине.
# Необходимо провести различные операции с этими данными.
#
# Задание:
# 1. Выведите названия всех товаров.
# 2. Увеличьте количество "Apples" на 10.
# 3. Измените цену "Bananas" на 1.5.
# 4. Удалите товар "Cherries".
# 5. Добавьте новый товар "Dates" с количеством 15 и ценой 4.
# 6. Выведите общую стоимость всех товаров (количество * цена для каждого товара и сумма этих значений).
#
inventory = {
    "Apples": {"quantity": 50, "price": 2},
    "Bananas": {"quantity": 30, "price": 1},
    "Cherries": {"quantity": 20, "price": 3},
}

