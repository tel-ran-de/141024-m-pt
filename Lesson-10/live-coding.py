# Цикл while. Операторы break, continue, else.

# while
# i = 0  # i, j, k - нормальные абстрактные названия для переменных
# while i < 5:
#     print(i)
#     i += 1
# Вывод 0 1 2 3 4

# password = ''
# while password != 'secret':
#     password = input('Введите пароль: ')
# print('Пароль верный')

# break c while
# i = 0
# while True:
#     if i == 10:
#         break
#     print(i)
#     i += 1
#
# print(f'Переменная i после завершения цикла равна {i}')
# print('Цикл завершил свою работу, но программа работает дальше')

# continue c while
# i = 0
# while i < 100:
#     i += 1
#     if i % 2 == 0:  # проверяется чётность
#         continue  # если число чётное, то происходит пропуск дальнейших строк кода и происходит запуск следующей итерации
#     print(i)  # когда запускается оператор continue, поток выполнения программы не доходит до этой строки

# else с while
# код в цикле под оператором else
# выполняется только если не сработал break
#
# i = 0
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print('Цикл завершён')

# number = 0
# while number != 100:
#     number = int(input('Введите число: '))
#     print(f'Вы ввели число {number}')
#     if number % 2 == 0 and number != 100:
#         print('Вы ввели чётное число и запустили оператор break.\nБлок else не будет выполнен.')
#         break
# else:
#     print('Вы вводили только нечётные числа')
#
# print('Этот print сработал за пределами цикла')
#
# word = ''
# while word != 'soft_stop':
#     word = input('Введите слово: ')
#     if word == 'STOP':
#         print('цикл остановлен с помощью break, else не будет выполнен')
#         break
# else:
#     print('Цикл был выполнен полностью и был запущен оператор else')

# if word == 'soft_stop':
#     print('Цикл был выполнен полностью и был запущен оператор else')

# Тема: Цикл for
# Продемонстрируйте создание и использование цикла for.
# Показать использование функций range, enumerate.

# for
# cities = ['Tbilisi', 'Berlin', 'Kogon', 'Beijin', 'London']
# for city in cities:  # на каждой итерации переменная city будет равна 'Tbilisi', 'Berlin', ...
#     print(f'Name of {city} starts with letter {city[0]}')

# i = 0
# while i < len(cities):
#     city = cities[i]
#     print(f'Name of {city} starts with letter {city[0]}')
#     i += 1

# print('Tbilisi')
# ...
# print('London')

# range
# print(list(range(5)))  # арифметическая прогрессия от 0 до 4
# print(list(range(10, 21)))  # арифметическая прогрессия от 10 до 20
# print(list(range(10, 100, 10)))  # арифметическая прогрессия от 10 до 99 с шагом 10

# for и range
# for i in range(10, 100, 10):  # 10, 20, 30, ..., 80, 90
#     if i % 3 == 0:
#         print(f'{i} кратно трём')
#     elif i % 7 == 0:
#         print(f'{i} кратно семи')
#     else:
#         print(i)

# enumerate - первый аргумент коллекция, второй аргумент с какого числа начать отсчёт
# countries = ['Germany', 'Italy', 'Brazil', 'Georgia', 'Italy']
# index = 0
# for country in countries:
#     print(f'{index}. {country}')
#     index += 1

# countries = ['Germany', 'Italy', 'Brazil', 'Georgia', 'Italy']
# for index, country in enumerate(countries, 1):
#     print(f'{index}. {country}')

# countries = ['Germany', 'Italy', 'Brazil', 'Georgia', 'Italy']
# for index, country in enumerate(countries, 1):
#     print(f'{index}. {country}')

# word = 'television noromende'
# for letter in word:
#     if letter in 'aeuio':
#         print(letter.upper())
#     else:
#         print(letter)

# VOWELS = 'aeuio'
# fruits = ['banana', 'orange', 'apple', 'peach', 'pear']
# for word in fruits:
#     print(f'word {word} consists of: ')
#     for letter in word:
#         if letter in VOWELS:
#             print(f'\t{letter} is vowel')
#         else:
#             print(f'\t{letter} is consonant')
#     print()

# l1 = [1]
# for i in l1:
#     print(i)
#     l1.append(i + 1)
#     if i == 100000:
#         break
