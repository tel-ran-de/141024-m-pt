# Примеры исключений
x = 1 / 0  # ZeroDivisionError

file = open("non_existent_file.txt", "r")  # FileNotFoundError

int("abc")  # ValueError


try:
    x = 1 / 0
except ZeroDivisionError:
    print("Деление на ноль невозможно")

# try/catch
try:
    x = 1 / 0
except:
    print("Произошла ошибка")


# finally
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Файл не найден")
finally:
    file.close()

# else
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Деление на ноль невозможно")
else:
    print("Результат:", result)

# Все блоки
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Деление на ноль невозможно")
else:
    print("Результат:", x)
finally:
    print("Блок finally выполнен")


# Обработка ошибок при чтении файла
try:
    with open("example.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Файл не найден")
except IOError:
    print("Ошибка ввода-вывода")
else:
    print(content)
finally:
    print("Операция завершена")


# Обработка ошибок при записи в файл
try:
    with open("example.txt", "w") as file:
        file.write("Hello, World!")
except IOError:
    print("Ошибка ввода-вывода")
else:
    print("Запись успешна")
finally:
    print("Операция завершена")


try:
    with open("example.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Ошибка: файл не найден")
except PermissionError:
    print("Ошибка: нет доступа к файлу")
except IOError as e:
    print(f"Ошибка ввода-вывода: {e}")


# Распространение исключения
def function1():  # Запуск цепочки вызовов
    function1()

def function1():
    try:
        function2()  # Вызов function2
    except ZeroDivisionError:
        print("Ошибка обработана в function1")  # Обработка исключения

def function2():
    function3()  # Вызов function3

def function3():
    result = 1 / 0  # Исключение возникает здесь (деление на ноль)
    # Исключение передается из function3 в function2, затем в function1,
    # где оно и обрабатывается.


def check_positive_number(number):
    if number < 0:
        raise ValueError("Число должно быть положительным.")
    return True

try:
    check_positive_number(-1)
except ValueError as e:
    print(e)  # Вывод: Число должно быть положительным.
