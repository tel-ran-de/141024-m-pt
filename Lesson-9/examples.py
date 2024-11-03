# Создание списка
fruits = ["apple", "banana", "cherry"]
print(fruits)  # ["apple", "banana", "cherry"]

# Доступ к элементам списка
print(fruits[0])  # "apple"
print(fruits[2])  # "cherry"

# Изменение значения элемента списка
fruits[1] = "blueberry"
print(fruits)  # ["apple", "blueberry", "cherry"]

# Получение среза списка
print(fruits[1:3])  # ["blueberry", "cherry"]

# Сравнение списков
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)  # True

# Вложенные списки
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0])  # [1, 2, 3]
print(matrix[1][1])  # 5

# Жизненные примеры
users = [
    ["user1", "password1", "email1@example.com"],
    ["user2", "password2", "email2@example.com"],
    ["user3", "password3", "email3@example.com"]
]
print(users[0])  # ["user1", "password1", "email1@example.com"]
print(users[1][1])  # "password2"

menu = [
    ["Главная", "/"],
    ["О нас", "/about"],
    ["Услуги", [
        ["Консалтинг", "/services/consulting"],
        ["Разработка", "/services/development"]
    ]],
    ["Контакты", "/contact"]
]
print(menu[2][1][0])  # ["Консалтинг", "/services/consulting"]
print(menu[3][0])  # "Контакты"

# Методы списков
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # [1, 2, 3, 4]

numbers.extend([5, 6])
print(numbers)  # [1, 2, 3, 4, 5, 6]

numbers.insert(1, 1.5)
print(numbers)  # [1, 1.5, 2, 3, 4, 5, 6]

numbers.remove(1.5)
print(numbers)  # [1, 2, 3, 4, 5, 6]

popped_number = numbers.pop(3)
print(popped_number)  # 4
print(numbers)  # [1, 2, 3, 5, 6]

numbers.clear()
print(numbers)  # []

numbers = [1, 2, 3, 2, 2]
index_of_2 = numbers.index(2)
print(index_of_2)  # 1

count_of_2 = numbers.count(2)
print(count_of_2)  # 3

numbers.sort()
print(numbers)  # [1, 2, 2, 2, 3]

numbers.reverse()
print(numbers)  # [3, 2, 2, 2, 1]

# Сравнение методов строк и списков
string = "hello"
string_replaced = string.replace("e", "a")
print(string_replaced)  # "hallo"

fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)  # ["apple", "blueberry", "cherry"]

print(len(string))  # 5
print(len(fruits))  # 3

print(sorted(string))  # ['e', 'h', 'l', 'l', 'o']
print(sorted(fruits))  # ['apple', 'banana', 'cherry']

print(string.count("l"))  # 2
print(fruits.count("apple"))  # 1
