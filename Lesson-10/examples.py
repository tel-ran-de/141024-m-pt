### Примеры кода из презентации урока 5: Циклы

# Пример работы цикла while
i = 0
while i < 5:
    print(i)
    i += 1
# Вывод: 0 1 2 3 4

# Пример работы цикла while для проверки пароля
password = ""
while password != "secret":
    password = input("Введите пароль: ")
print("Пароль верен!")

# Пример работы оператора break
i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1
# Вывод: 0 1 2 3 4

# Пример работы оператора continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
# Вывод: 1 2 4 5

# Пример работы оператора else с циклом while
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Цикл завершен")
# Вывод: 0 1 2 3 4
# Цикл завершен

# Пример работы цикла for с функцией range
for i in range(5):
    print(i)
# Вывод: 0 1 2 3 4

# Пример использования функции range
print(list(range(5)))       # [0, 1, 2, 3, 4]
print(list(range(1, 6)))    # [1, 2, 3, 4, 5]
print(list(range(1, 10, 2))) # [1, 3, 5, 7, 9]

# Пример работы цикла for с последовательностью
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Вывод: apple banana cherry

# Пример использования функции enumerate
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
# Вывод: 0 apple 1 banana 2 cherry