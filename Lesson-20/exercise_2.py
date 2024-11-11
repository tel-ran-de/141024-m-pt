# Тема: Расространение исключения. Возбуждение исключения.

# Задача 1. Допишите код ниже.
#
# import math
#
# def calculate_square_root(number):
#     # Добавьте проверку на отрицательное число и возбуждение исключения
#
#     return math.sqrt(number)
#
# def safe_calculate_square_root(number):
#     try:
#         result = calculate_square_root(number)
#         print(f"Квадратный корень из {number} равен {result}")
#     except ValueError as e:
#         print(f"Ошибка: {e}")
#
# # Тесты функции
# safe_calculate_square_root(25)  # Ожидаемый результат: Квадратный корень из 25 равен 5.0
# safe_calculate_square_root(-9)  # Ожидаемый результат: Ошибка: Число должно быть положительным


# Задача 2. Допишите код ниже.
# def convert_to_number(string):
#     # Добавьте проверку на некорректное значение и возбуждение исключения
#
#     return int(string)
#
# def safe_convert_to_number(string):
#     try:
#         number = convert_to_number(string)
#         print(f"Конвертированное число: {number}")
#     except ValueError as e:
#         print(f"Ошибка: {e}")
#
# # Тесты функции
# safe_convert_to_number("123")  # Ожидаемый результат: Конвертированное число: 123
# safe_convert_to_number("abc")  # Ожидаемый результат: Ошибка: Введенное значение не является числом
