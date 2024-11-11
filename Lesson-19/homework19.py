# Тема: Чтение и запись данных в файл.
from os import write


def f(a):
    print(f'------{a}------')

# Задание 1: Чтение данных из файла
# 1. Откройте файл `data.txt` для чтения.
# 2. Прочитайте весь контент файла и выведите его на экран.
# 3. Прочитайте первые 10 символов файла и выведите их на экран.
# 4. Прочитайте одну строку из файла и выведите ее на экран.
# 5. Прочитайте все строки файла и выведите их на экран.
f(6.1)
with open('text/data.txt', 'r') as file:
    content1 = file.read()
print(content1)

f(6.3)
with open('text/data.txt') as file:
    content1 = file.read(10)
print(content1)

f(6.4)
with open('text/data.txt') as file:
    content1 = file.readline()
    content1 = file.readline()
print(content1)

f(6.5)
with open('text/data.txt') as file:
    content1 = file.readlines()
print(content1)

# Задание 2: Запись данных в файл
# 1. Откройте (создайте) файл `output.txt` для записи.
# 2. Запишите в файл строку "Hello, World!".
# 3. Запишите в файл список строк: ["This is line 1\n", "This is line 2\n"].
# 4. Закройте файл.
# 5. Откройте файл `output.txt` для чтения и выведите его содержимое на экран.
f(33.1)
with open('text/output.txt', 'w') as file:
    file.write("Hello, World!")

file = open('text/output.txt', 'a')
l_add = ["This is line 1\n", "This is line 2\n"]
print(file.tell())
file.writelines(l_add)
file.close()
file = open('text/output.txt', 'a')
l_add = ["This is line 3\n", "This is line 4\n"]
file.writelines(l_add)
file.close()

f(33.5)
with open('text/output.txt') as file:
    content1 = file.read()
print(content1)


# Задание 3: Добавление данных в файл
# 1. Откройте (создайте) файл `log.txt` для добавления данных.
# 2. Добавьте строку "New log entry\n" в конец файла.
# 3. Добавьте список строк ["Log entry 1\n", "Log entry 2\n"] в конец файла.
# 4. Закройте файл.
# 5. Откройте файл `log.txt` для чтения и выведите его содержимое на экран.

f(59.1)
with open('text/log.txt', 'w') as file:
    file.write('')
    print(content1)
f(59.2)
with open('text/log.txt', 'a') as file:
    l_add = "New log entry\n"
    file.write(l_add)
f(59.3)
with open('text/log.txt', 'a') as file:
    l_add = ["Log entry 1\n", "Log entry 2\n"]
    file.writelines(l_add)
f(59.5)
with open('text/log.txt') as file:
    content1 = file.read()
print(content1)


# Задание 4: Работа с указателем
# 1. Откройте (создайте) файл `pointer_example.txt` для чтения и записи.
# 2. Запишите в файл строку "Python File Handling\n".
# 3. Переместите указатель в начало файла и прочитайте первую строку.
# 4. Переместите указатель на позицию 7 и прочитайте следующие 5 символов.
# 5. Переместите указатель в конец файла и добавьте строку "End of file\n".
# 6. Переместите указатель в начало файла и прочитайте весь файл.
f(84.1)
file = open('text/pointer_example.txt', 'r+')
file.write("Python File Handling\n")
print(file.tell())
file.seek(0)
print(file.tell())
content1=file.readline()
print(content1)
file.seek(5)
print(file.tell())
content1 = file.read(5)
print(content1)
file.seek(0, 2)
print(file.tell())
file.write("End of file\n")
file.seek(0)
content1= file.read()
print(content1)
file.close()
with open('text/pointer_example.txt', 'w') as file:
    file.write('')

# Тема: Менеджер контекста и JSON

import json

# Задача 1: Чтение и запись JSON данных с использованием менеджера контекста
# 1. Создайте словарь с информацией о пользователе (имя, возраст, город).
# 2. Запишите этот словарь в файл JSON `user.json` с использованием менеджера контекста.
# 3. Прочитайте данные из файла `user.json` и выведите их на экран.
f(119.1)
data = {
    'name': 'Gretta',
    'age': 41,
    'city': 'Berlin',
    'la': True
}
f(119.2)
with open('text/user.json', 'w') as file:
    json.dump(data, file, indent=4)
f(119.3)
with open('text/user.json', 'r') as file:
    data1= json.load(file)
print(data1)
# json_string = json.dumps(data1)
# print(json_string)
# data1 = json.loads(json_string)
# print(data1)

# Задача 2: Обновление данных в файле JSON
# 1. Прочитайте данные из файла `user.json`.
# 2. Обновите возраст пользователя на 29 лет.
# 3. Запишите обновленные данные обратно в файл JSON с использованием менеджера контекста.
f(142)
with open('text/user.json', 'r') as file:
    data = json.load(file)
data['age'] = 29
with open('text/user.json', 'w') as file:
    json.dump(data, file)

# Задача 3: Добавление нового пользователя в массив JSON
# 1. Прочитайте массив объектов из файла `users.json`
# (каждый объект содержит информацию о пользователе: имя, возраст, город).
# 2. Добавьте нового пользователя в массив.
# 3. Запишите обновленный массив обратно в файл JSON с использованием менеджера контекста.
f(153)
data1 = [{'name': 'Slonik', 'age': 22, 'city': 'Gotta'},{'name': 'Geck', 'age': 23, 'city': 'Borabora'}]
with open('text/users.json', 'w') as file:
    json.dump(data1, file, indent=4)


with open('text/users.json', 'r') as file:
    data = json.load(file)

k = {'name': 'Slonik1', 'age': 93, 'city': 'Born'}

# если не хочу чтоб пользователи повторялись по имени
# n = 0
# for i in data:
#     if k['name'] == i['name']:
#         n = 1
# if n == 0:
#     data.append(k)
data.append(k)
print(data)
with open('text/users.json', 'w') as file:
    json.dump(data, file)



# Задача 4: Удаление пользователя из массива JSON
# 1. Прочитайте массив объектов из файла `users.json`.
# 2. Удалите одного из пользователей.
# 3. Запишите обновленный массив обратно в файл JSON с использованием менеджера контекста.
f(183)

with open('text/users.json', 'r') as file:
    data = json.load(file)
for i in data:
    if i['name'] == 'Slonik1':
        print(i)
        data.remove(i)
print(data)
with open('text/users.json', 'w') as file:
    json.dump(data, file, indent=4)


# Тема: Интеграционная практика. Мини-проект

# Проект: Перепишите проект из уроков 7-8 с записью, чтением, обновлением и удалением товаров в файле (через JSON).
# Используйте файл как базу данных проекта.
#
# Управление инвентарем в интернет-магазине
# Разработайте программу для управления инвентарем интернет-магазина.
# Программа должна позволять добавлять новые товары и удалять имеющиеся,
# обновлять наименование, цену и количество существующих товаров,
# искать товары по названию, выводить список всех товаров и их количество,
# а также выводить товары с количеством ниже заданного значения стоимости и количества.
#
# Меню:
# 1. Показать список товаров.
# 2. Добавить товар.
# 3. Удалить товар.
# 4. Обновить название товара, стоимость или количество.
# 5. Найти товар по названию.
# 6. Вывести список товаров меньше определнной стоимости.
# 7. Вывести список товаров меньше определенного количества.
f(200)
inventory = [
    {'product': "Laptop", 'price': 10, 'count': 13},
    {'product': "Mouse", 'price': 50, 'count': 1},
    {'product': "Keyboard", 'price': 30, 'count': 33},
    {'product': "Monitor", 'price': 20, 'count': 10}
]
with open("text/inventory.json", "w") as file:
    json.dump(inventory, file, indent=4)

with open("text/inventory.json", 'r') as file:
    inventory = json.load(file)
print(inventory)
def inv_menu():
    print('---------')
    print('1. Показать список товаров.')
    print('2. Добавить товар.')
    print('3. Удалить товар.')
    print('4. Обновить название товара, стоимость или количество.')
    print('5. Найти товар по названию.')
    print('6. Вывести список товаров меньше определнной стоимости.')
    print('7. Вывести список товаров меньше определенного количества.')

def li_inv():
    for i in inventory:
        print(f'{i["product"]:9}  {i["price"]}  {i["count"]}')

def new_product(product, price, count):
    inventory.append({"product": product, "price": price, "count": count})

def save_inventory():
    global inventory
    with open('text/inventory.json', 'w') as file:
        json.dump(inventory, file)


def menu_3():
    while True:
        li_inv()
        # for i in inventory:
        #     print(f'{i["product"]:9}  {i["price"]}  {i["count"]}')
        print('--------')
        key1 = input('(x for quit)\nkeys for del - ')
        if key1 == "x":
            break
        else:
            n = -1
            for i in inventory:
                n += 1
                if i["product"] == key1:
                    inventory.remove(i)
                    continue
            print('-----\nnot finde\n------')

def menu_4():
    while True:
        li_inv()

        print('--------')
        key1 = input('(x for quit)\nkeys for rename - ')
        if key1 == "x":
            break
        else:
            for i in inventory:
                if i["product"] == key1:
                    while True:

                        print('--------')
                        print(f'{i["product"]:9}  {i["price"]}  {i["count"]}')
                        print('1 - new product name: ')
                        print('2 - new price: ')
                        print('3 - new count: ')
                        print('x  - quit')
                        choise = input(': ')
                        if choise == '1':
                            i["product"] = input('new name: ')
                        elif choise == "2":
                            i["price"] = input('new price: ')
                        elif choise == "3":
                            i["count"] = input('new count: ')
                        elif choise == 'x':
                            break
                else:
                    print('produkt not found')

def menu_5():
    key1 = input('seurch key: ')
    a = 0
    for i in inventory:
        if i['product'] == key1:
            a += 1
            print(f'{i["product"]:9}  {i["price"]}  {i["count"]}')
    if a == 0:
        print('Not found')

def menu_6():
    while True:

        print('------')

        a = int(input('0- for exit\nEnter max price: '))
        print(f'---------\n{"produkt":9}  Max|count')
        if a <= 0:
            print('Chuuus!')
            break
        for i in inventory:
            if a >= i['price']:
                print(f'{i["product"]:9}  {i["price"]}  {i["count"]}')

def menu_7():
    while True:

        print('------')

        a = int(input('0- for exit\nEnter min price: '))
        print(f'---------\n{"produkt":9}  Min|count')
        if a <= 0:
            print('Chuuus!')
            break
        for i in inventory:
            if a <= i['price']:
                print(f'{i["product"]:9}  {i["price"]}  {i["count"]}')


# inventory = [
#     {'product': "Laptop", 'price': 10, 'count': 13},
#     {'product': "Mouse", 'price': 50, 'count': 1},
#     {'product': "Keyboard", 'price': 30, 'count': 33},
#     {'product': "Monitor", 'price': 20, 'count': 10}
# ]

while True:
    inv_menu()
    menu = input('N: ')
    print('---------')
    if menu == "x":
        break
    if menu == "1":
        li_inv()

    if menu == "2":
        product = input('product - ')
        price = int(input('price - '))
        count = int(input('count - '))
        new_product(product, price, count)
        save_inventory()

    if menu == "3":
        menu_3()
        save_inventory()

    if menu == "4":
        menu_4()
        save_inventory()

    if menu == '5':
        menu_5()

    if menu ==  '6':
        menu_6()

    if menu ==  '7':
        menu_7()
