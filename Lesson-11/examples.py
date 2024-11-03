# Цикл `for` и итераторы
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Вывод: apple banana cherry

# Итератор и итерируемые объекты
fruits = ["apple", "banana", "cherry"]
fruit_iter = iter(fruits)
print(next(fruit_iter))  # "apple"
print(next(fruit_iter))  # "banana"
print(next(fruit_iter))  # "cherry"

# Преимущества использования `iter` и `next`
file = open('data.txt')
file_iter = iter(file)
print(next(file_iter))
print(next(file_iter))
file.close()

# Сравнение `iter` и `next` с циклом `for` и функцией `range`
numbers = [1, 2, 3]
for num in numbers:
    print(num)
# Вывод: 1 2 3

for num in range(1, 4):
    print(num)
# Вывод: 1 2 3

# Когда использовать `iter` и `next`
def manual_iteration(iterable):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
            print(item)
        except StopIteration:
            break

manual_iteration([1, 2, 3])
# Вывод: 1 2 3

# Вложенные циклы: цикл `for` вложенный в `for`
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
# Вывод:
# 1 2 3
# 4 5 6
# 7 8 9

# Пример: работа с двумерными массивами
grades = [
    ["Alice", 90, 85, 88],
    ["Bob", 78, 81, 85],
    ["Charlie", 92, 88, 91]
]

for student in grades:
    name, *scores = student
    average = sum(scores) / len(scores)
    print(f"{name}: {average}")
# Вывод:
# Alice: 87.66666666666667
# Bob: 81.33333333333333
# Charlie: 90.33333333333333

# Вложенные циклы: `for` вложенный в `while`
numbers = [1, 2, 3]
i = 0

while i < len(numbers):
    print(f"Processing number {numbers[i]}")
    for j in range(numbers[i]):
        print(j, end=" ")
    print()
    i += 1
# Вывод:
# Processing number 1
# 0
# Processing number 2
# 0 1
# Processing number 3
# 0 1 2

# Пример: работа с переменным числом итераций
password = "secret"
attempt = ""

while attempt != password:
    attempt = input("Введите пароль: ")
    if attempt != password:
        print("Неправильный пароль, попробуйте снова.")

print("Пароль верен!")

# Генераторы списков (List comprehension)
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)  # [1, 4, 9, 16, 25]

# Пример использования генераторов списков
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # [2, 4, 6]

# Пример использования генераторов списков для обработки строк
text = "Hello, world!"
vowels = [char for char in text if char.lower() in 'aeiou']
print(vowels)  # ['e', 'o', 'o']

# Слайд 14: Вложенные циклы и вложенные генераторы списков
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened = [element for row in matrix for element in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Пример использования вложенных генераторов списков
n = 3
matrix = [[i * j for j in range(1, n+1)] for i in range(1, n+1)]
print(matrix)
# Вывод:
# [[1, 2, 3],
#  [2, 4, 6],
#  [3, 6, 9]]

# Пример использования вложенных генераторов списков для фильтрации данных
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

even_elements = [element for row in matrix for element in row if element % 2 == 0]
print(even_elements)  # [2, 4, 6, 8]

# Использование вложенных генераторов списков для обработки данных
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

normalized = [[element / 10 for element in row] for row in matrix]
print(normalized)
# Вывод:
# [[1.0, 2.0, 3.0],
#  [4.0, 5.0, 6.0],
#  [7.0, 8.0, 9.0]]