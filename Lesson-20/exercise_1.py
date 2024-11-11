# Тема: Обработка исключений (try/except/else/finally)

# Задача 1: Деление чисел
# Напишите функцию, которая принимает два числа в качестве аргументов и возвращает результат их деления.
# Обработайте исключения для случаев, когда:
# - деление на ноль
# - ввод не числовых значений.
def divide_numbers(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        return f'На ноль делить нельзя {e}'
    except TypeError as e:
        return f'Введено не число {e}'
    except ValueError as e:
        return f'Введено не число {e}'
    # except:
    #     return 'Что-то пошло не так!'
    else:
        return result


print(divide_numbers(1, 0))
print(divide_numbers(1, '0'))
print(divide_numbers(1, None))
print(divide_numbers(144, 12))


# Задача 2: Обработка пользовательского ввода
# Напишите программу, которая запрашивает у пользователя ввод числа и выводит его квадрат.
# Обработайте исключения для случаев, когда ввод не является числом.
def square_number():
    try:
        number = float(input('Введите число: '))
        result = number ** 2
    except ValueError:
        return "Введённое значение не является числом"
    else:
        return f'Квадрат числа {number} равен {result}'


print(square_number())


# Задача 3. Вернитесь к задачам предыдущего урока из файла exercise_1 и добавьте в решение обработку возможных ошибок,
# которые могут случиться при работе с файлами (FileNotFoundError, PermissionError, IOError).
# Проверьте, что ошибки обрабатываются на примере FileNotFoundError.