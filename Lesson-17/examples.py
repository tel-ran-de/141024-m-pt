# Создание модуля
# файл my_module.py
# def greet(name):
#     return f"Hello, {name}!"
#
#
# # другой файл
# import my_module
# 
# print(my_module.greet("Alice"))
#
# # Вывод: Hello, Alice!


# Основные функции модуля ramdom
#
# import random
#
# random.random()
# # Генерация случайного дробного число от 0.0 до 1.0
#
# random.randint(1, 10)
# # Генерация случайного целого числа в указанном диапазоне, включая обе границы
#
# random.uniform(1.5, 10.5)
# # Генерация случайного дробного числа в указанном диапазоне [a, b]
#
# random.choice(['apple', 'banana', 'cherry'])
# # Выбор случайного элемента из последовательности
#
# items = [1, 2, 3, 4, 5]
# random.shuffle(items)
# # Перемешивание последовательности
#
# random.sample(range(1, 100), 5)
# # Генерация указанного количества случайных элементов из диапазона


# Основные функции модуля math

# import math
#
# math.floor(4.7)
# # Округление числа до ближайшего целого числа в меньшую сторону
#
# math.ceil(4.2)
# # Округление числа до ближайшего целого числа в большую сторону
#
# math.trunc(4.1)
# # Отбрасывание дробной части и возврат целого числа
#
# math.sqrt(16)
# # Вычисление квадратного корня числа
#
# math.factorial(5)
# # Вычисление факториала числа
#
# print(math.pow(2, 3))
# # Возведение числа в степень


# Основные команды PIP
#
# pip install <package_name> # Установка пакета
#
# pip uninstall <package_name> # Удаление пакета
#
# pip install --upgrade <package_name> # Обновление пакета
#
# pip list # Список установленных пакетов
#
# pip freeze > requirements.txt
# # Создание файла requirements.txt со списком всех установленных пакетов
#
# pip install -r requirements.txt # Установка пакетов из файла requirements.txt