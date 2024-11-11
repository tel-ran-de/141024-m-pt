# Тема: Обработка исключений (try/except/else/finally)
# Продемонстрируйте использование блоков try, except, else и finally.
# Покажите обработку исключений при чтении и записи файла.

# Примеры исключений
# x = 1 / 0  # ZeroDivisionError
# file = open("non_existent_file.txt", "r")  # FileNotFoundError
# int("abc")  # ValueError

# try:
#     x = 1 / 0
# except ZeroDivisionError:
#     print("Деление на ноль невозможно")
# print('Программа продолжает свою работу')

# # try
# try:
#     x = 1 / 0
# except:
#     print("Произошла ошибка")

# # finally
# try:
#     file = open("examples.py", "r", encoding="utf-8")
#     content = file.read()
# except FileNotFoundError:
#     print("Файл не найден")
# finally:
#     print('Операция завершена')
#     file.close()

# # else
# try:
#     file = open("example.txt", "w")
#     file.write("Hello, world!")
# except IOError:
#     print("Ошибка ввода-вывода")
# else:
#     print("Запись успешна")
# finally:
#     print("Операция завершена")

# # именование исключений
# try:
#     file = open("example.txt", "r")
#     content = file.read()
# except FileNotFoundError as e:
#     print(f"Ошибка: файл не найден: {e}")
# except PermissionError as e:
#     print(f"Ошибка: нет доступа к файлу: {e}")
# except IOError as e:
#     print(f"Ошибка ввода-вывода: {e}")
# else:
#     print("Запись успешна")
# finally:
#     print("Операция завершена")


# Тема: Распространение исключения. Возбуждение исключения.
# Покажите в режиме live-coding и объясните:
# - Иерархию исключений
# - Распространение исключения
# - Возбуждение исключение через raise

# ПРИМЕР 1
# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError as e:
#         return f'На ноль делить нельзя {e}'
#     else:
#         return result
#
#
# def main():
#     try:
#         result = divide(10, 'a')
#     except Exception as e:
#         return 'Необработанное исключение'
#     else:
#         return result
#
#
# print(main())


# ПРИМЕР 2
# def process_list(lst):
#     try:
#         print(lst[10])  # Попытка доступа к элементу с индексом 10
#         result = 10 / lst[0]  # Попытка деления на элемент списка
#     except IndexError as e:
#         result = f"Ошибка индекса: {e}"
#     except ZeroDivisionError as e:
#         result = f"Ошибка деления на ноль: {e}"
#     except Exception as e:
#         result = f"Другая ошибка: {e}"
#     return result
#
#
# def main():
#     print(process_list([1, 2, 3]))  # Список слишком короткий — Ошибка индекса: list index out of range
#     print(process_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Деление на ноль — Ошибка деления на ноль: division by zero
#     print(process_list([]))  # Пустой список — Ошибка индекса: list index out of range
#     print(process_list(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']))  # Другая ошибка: unsupported operand type(s) for /: 'int' and 'str'
#
# main()


## raise
# ПРИМЕР 1
# def check_positive(number):
#     if number < 0:
#         raise ValueError("Число должно быть положительным")
#     print(f"Число: {number}")
#
# try:
#     check_positive(-5)
# except ValueError as e:
#     print(f"Ошибка: {e}")

# ПРИМЕР 2
# class MyCustomError(Exception):
#     pass
#
# def custom_function(value):
#     if value < 0:
#         raise MyCustomError("Значение должно быть неотрицательным")
#     print(f"Значение: {value}")
#
# try:
#     custom_function(-10)
# except MyCustomError as e:
#     print(f"Ошибка: {e}")

## ПРИМЕР 3
def check_age(age):
    if age < 18:
        raise ValueError("Вход только для взрослых!")
    print(f"Возраст: {age}")

try:
    check_age(19)
except ValueError as e:
    print(f"Ошибка: {e}")
