# Тема: Сортировка с использованием sort и sorted

def f(a):
    print(f'\n---{a}---')
# Задача 1: Сортировка списка чисел по возрастанию и убыванию
# Дан список чисел `[10, 3, 7, 1, 9, 4]`.
# 1. Отсортируйте список по возрастанию с помощью метода `sort`.
# Ожидаемый результат: [1, 3, 4, 7, 9, 10]
f(5)
list1 = [10, 3, 7, 1, 9, 4]
list1.sort()
print(list1)

# 2. Отсортируйте список по убыванию с помощью функции `sorted`.
# Ожидаемый результат: [10, 9, 7, 4, 3, 1]
f(14)
print(sorted(list1, key=lambda x: -x))
print(sorted(list1, reverse=True))

# Задача 2: Сортировка списка строк по длине
# Дан список строк `["house", "cat", "elephant", "car", "building"]`.
# Отсортируйте список по длине строк с помощью функции `sorted`.
# Ожидаемый результат: ['cat', 'car', 'house', 'building', 'elephant']
f(20)
list1 = ["house", "cat", "elephant", "car", "building"]
print(sorted(list1, key=len))

# Задача 3: Сортировка списка кортежей по второму элементу
# Дан список кортежей `[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]`.
# Отсортируйте список по второму элементу кортежей с помощью метода `sort`.
# Ожидаемый результат: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
f(28)
list1 = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
list1.sort(key= lambda x:x[1])
print(list1)

# Задача 4: Сортировка списка словарей по значению ключа
# Дан список словарей `[{ "name": "Alice", "age": 25 }, { "name": "Bob", "age": 20 }, { "name": "Charlie", "age": 23 }]`.
# Отсортируйте список по значению ключа `age` с помощью функции `sorted`.
# Ожидаемый результат: [{'name': 'Bob', 'age': 20}, {'name': 'Charlie', 'age': 23}, {'name': 'Alice', 'age': 25}]
f(37)
dic1 = [{ "name": "Alice", "age": 25 }, { "name": "Bob", "age": 20 }, { "name": "Charlie", "age": 23 }]
print(sorted(dic1, key=lambda x: x["age"]))

# Задача 5: Сортировка списка кортежей по сумме элементов
# Дан список кортежей `[(3, 5), (1, 7), (4, 2), (6, 3)]`.
# Отсортируйте кортежи по сумме их элементов с помощью метода `sort`.
# Ожидаемый результат: [(4, 2), (3, 5), (6, 3), (1, 7)]
f(45)
list1 = [(3, 5), (1, 9), (4, 2), (6, 3)]
list1.sort(key = lambda x: sum(x))
print(list1)

# Тема: Cортировка с all, any, isinstance

# Задача 1: Сортировка списка строк с проверкой типов
# Дан список `["tree", 3, "mountain", 1, "river", 2]`.
# Отсортируйте только строки в списке по алфавиту с помощью функции `sorted`,
# Ожидаемый результат: ['mountain', 'river', 'tree']
f(56)
list1 = ["tree", 3, "mountain", 1, "river", 2]
# print(sorted(list1, key= lambda x:  isinstance(x, str)))
list1 = filter(lambda x: isinstance(x, str), list1)
print(sorted(list1))

# Задача 2: Сортировка списка словарей по значению ключа с проверкой типов
# Дан список словарей
# [{ "title": "Book A", "price": 15.99 }, { "title": "Book B", "price": "free" }, { "title": "Book C", "price": 9.99 }].
# Отсортируйте словари по значению ключа `price`, предварительно проверив, что значение является числом,
# с помощью функции `isinstance`.
# Ожидаемый результат: [{'title': 'Book C', 'price': 9.99}, {'title': 'Book A', 'price': 15.99}]
f(66)
list1 = [{ "title": "Book A", "price": 15.99 }, { "title": "Book B", "price": "free" }, { "title": "Book C", "price": 9.99 }]
list1 = list(filter(lambda x : isinstance( x['price'], float), list1))
print(sorted(list1, key= lambda x: isinstance(x['price'], float)))

# Задача 3: Сортировка списка кортежей по количеству слов с использованием all
# Дан список кортежей `[(3, "high"), (1, "low"), (4, "medium"), (6, "very high")]`.
# Отсортируйте кортежи по количеству слов во втором элементе, предварительно проверив,
# что все строки содержат только алфавитные символы, с помощью функции `all`.
# Ожидаемый результат: [(1, 'low'), (3, 'high'), (4, 'medium'), (6, 'very high')]
f(77)
list1 = [(3, "high"), (1, "low"), (4, "medium"), (6, "very high")]

def len_list_el2(a):
        a = len(a[1].split())
        return a

list2 = []
for i in list1:
    if all(not a in '1234567890' for a in i[1]):
        list2.append(i)
list1 = sorted(list2, key= len_list_el2)
print(list(list1))

# def is_alpha(func):
#     def i_a(a):
#         for i in a[1]:
#             if i in "1234567890":
#                 return False
#         return func
#
# print(sorted(list1, key= is_alpha(len_list_el2)))


# Задача 4: Сортировка списка словарей по длине значений с использованием any
# Дан список словарей
# [{ "country": "USA", "capital": "Washington" }, { "country": "UK", "capital": "London" },
#  { "country": "Australia", "capital": "Canberra" }].
# Отсортируйте словари по длине значений ключа `capital`, предварительно проверив,
# что хотя бы одна длина значения ключа `capital` больше 6, с помощью функции `any`.
# Ожидаемый результат: [{'country': 'UK', 'capital': 'London'}, {'country': 'Australia', 'capital': 'Canberra'}, {'country': 'USA', 'capital': 'Washington'}]
f(106)
list_1 = [{ "country": "USA", "capital": "Washington" }, { "country": "UK", "capital": "London" }, { "country": "Australia", "capital": "Canberra" }]

if any(len(i['capital']) > 6 for i in list_1):
    # print(list_1)
    list_1 = sorted(list_1, key= lambda i: len(i["capital"]))
print(list_1)
# Тема: Дополнительная практика

# Задача 1: Сортировка списка строк по количеству гласных с использованием isinstance
# Дан список `["engineering", 2, "artificial", 3.14, "intelligence"]`.
# Отсортируйте только строки в списке по количеству гласных с помощью функции `sorted`,
# предварительно проверив тип данных с помощью функции `isinstance`.
# Ожидаемый результат: ['artificial', 'enginering', 'intelligence']
f(122)
list1 = ["engineeeeering", 2, "artificiaal", 3.14, "intelligenceee"]
def var_a(x):
    n = 0
    for i in x:
        if i in 'aeoui':
           n += 1
    return n

list1 = list(filter(lambda x: isinstance(x,str), list1))
list1 = sorted(list1, key= var_a)
print(list1)

# Задача 2: Сортировка списка списков по минимальному значению элемента с использованием all
# Дан список списков `[[3, 5, 1], [0, -2, 3], [4, 4, 4], [-1, 3, 5]]`.
# Отсортируйте списки по их минимальному значению, предварительно проверив,
# что все элементы списков являются положительными, с помощью функции `all`.
# Ожидаемый результат: [[3, 5, 1], [4, 4, 4]]
f(140)
list1 = [[3, 5, 1], [0, -2, 3], [4, 4, 4], [-1, 3, 5]]
list1 = list(filter(lambda x: all( num > 0 for num in x ), list1))
print(sorted(list1, key= lambda x: min(x)))

# Задача 3: Сортировка списка словарей по статусу пользователя и преобразование с помощью map
# **Задание:**
# Дан список словарей, представляющих пользователей веб-приложения
# [{ "username": "alice", "status": "active" }, { "username": "bob", "status": "inactive" },
#  { "username": "charlie", "status": "active" }]`.
# Отсортируйте пользователей по статусу, а затем используйте функцию `map`,
# чтобы преобразовать статусы в верхний регистр.
# Ожидаемый результат:
# [{'username': 'alice', 'status': 'ACTIVE'},
# {'username': 'charlie', 'status': 'ACTIVE'},
# {'username': 'bob', 'status': 'INACTIVE'}]
f(150)
list1 = [{ "username": "alice", "status": "active" }, { "username": "bob", "status": "inactive" }, { "username": "charlie", "status": "active" }]
list1 = sorted(list1, key= lambda x : x["status"])
def upper_dic(x):
    x["status"] = x["status"].upper()
    return x

list1 = list(map(upper_dic, list1))
for i in list1:
    print(i)


# Задача 4: Сортировка списка URL по длине и фильтрация с помощью filter
# Дан список URL-адресов
# ["https://example.com", "https://longexample.com/page", "http://short.io", "https://medium.com/article"]`.
# Отсортируйте URL по длине, а затем используйте функцию `filter`,
# чтобы отобрать только те URL, которые содержат подстроку "example".
# Ожидаемый результат: ['https://example.com', 'https://longexample.com/page']
f(173)
list1 = ["https://example.com", "https://longexample.com/page", "http://short.io", "https://medium.com/article"]
list1 = list(sorted(list1, key = lambda x: len(x)))
list1 = list(filter(lambda x : "example" in x , list1))
print(list1)

# Задача 5: Сортировка списка запросов по времени выполнения и объединение с URL с помощью zip
# Дан список времени выполнения запросов в миллисекундах `[120, 30, 150, 90]` и список соответствующих URL
# `["/home", "/login", "/profile", "/settings"]`. Отсортируйте время выполнения по возрастанию,
# а затем используйте функцию `zip`, чтобы объединить отсортированные времена выполнения с URL, и выведите результат.
# Ожидаемый результат: [(30, '/home'), (90, '/login'), (120, '/profile'), (150, '/settings')]
f(185)
list1 = [120, 30, 150, 90]
list2 = ["/home", "/login", "/profile", "/settings"]
list1.sort()
print(list(zip(list1, list2)))


# Задача 6: Сортировка списка API ответов по статус-коду и преобразование с помощью map и zip
# Дан список словарей, представляющих ответы от API
# [{ "url": "/api/user", "status": 200 },
#   { "url": "/api/admin", "status": 403 },
#   { "url": "/api/data", "status": 404 }]`.
# Отсортируйте ответы по статус-коду, а затем используйте функцию `zip` для объединения отсортированных ответов
# с их порядковыми номерами, и функцию `map` для преобразования в кортежи вида (номер, url, статус).
# Ожидаемый результат: [(0, '/api/user', 200), (1, '/api/admin', 403), (2, '/api/data', 404)]
f(197)
dic1 = [{ "url": "/api/user", "status": 200 }, { "url": "/api/admin", "status": 403 }, { "url": "/api/data", "status": 404 }]

def funk_map3(a):
    x,c = a
    return x, c["url"], c["status"]

list3 = sorted(dic1, key=lambda i: i["status"])
print(list3)
list3 = enumerate(list3)
list3 = map(funk_map3, list3)
print(list(list3))

# dic2 = map(enumerate(sort_dic()) )
# for a,b,c in enumerate(sort_dic()):
#     i= a+b+c
#     print(i)

# print(list(dic2))
# dic1 = sorted(dic1, key = lambda x: x['status'])
# print(enumerate(dic1,1))
# dic2 = list(a for a in sort_dic())
# dic2 = enumerate(dic2)

# def sort_dic_ur():
#     for i in dic1:
#         yield i["url"]
#
# def sort_dic_st():
#     for i in dic1:
#         yield i["status"]
#
# def en_li(a):
#     x = a
#     return x
#
# list2 = list(zip(sort_dic_ur(), sort_dic_st()))
# list1 = list(map(en_li, enumerate(list2)))
# print(list2)