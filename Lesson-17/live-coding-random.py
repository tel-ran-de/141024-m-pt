# Основные функции модуля ramdom
#
from random import random, randint, uniform, choice, shuffle, sample

# Генерация случайного дробного число от 0.0 до 1.0
print('# Генерация случайного дробного число от 0.0 до 1.0')
print(random())


# Генерация случайного целого числа в указанном диапазоне, включая обе границы
print('# Генерация случайного целого числа в указанном диапазоне, включая обе границы')
print(randint(1, 1000))

# Генерация случайного дробного числа в указанном диапазоне [a, b]
print('# Генерация случайного дробного числа в указанном диапазоне [a, b]')
print(uniform(0.123, 10.7))

# Выбор случайного элемента из последовательности
print('# Выбор случайного элемента из последовательности')
print(choice(['apple', 'banana', 'cherry', 'orange', 'pineapple', 'peach']))

# Перемешивание последовательности
print('# Перемешивание последовательности')
fruits = ['apple', 'banana', 'cherry', 'orange', 'pineapple', 'peach']
shuffle(fruits)
print(fruits)

# Генерация указанного количества случайных элементов из диапазона
print('# Генерация указанного количества случайных элементов из диапазона')
print(sample(range(1, 101), 10))
