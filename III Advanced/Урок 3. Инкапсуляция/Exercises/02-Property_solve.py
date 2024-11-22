# Задача 1: Создание класса Student с использованием декоратора property
# Описание:
#
# Создайте класс Student, который будет иметь приватные атрибуты name и grade.
# Реализуйте геттеры и сеттеры для этих атрибутов с использованием декоратора property.
#
# Требования:
#
# Приватные атрибуты __name и __grade.
# Свойства name и grade с геттерами и сеттерами.
# В сеттере для grade реализуйте проверку, что оценка должна быть в диапазоне от 0 до 100.
#
# Задача 2: Создание класса BankAccount с использованием декоратора property
# Описание:
#
# Создайте класс BankAccount, который будет иметь приватные атрибуты account_number и balance.
# Реализуйте геттеры и сеттеры для этих атрибутов с использованием декоратора property.
#
# Требования:
#
# Приватные атрибуты __account_number и __balance.
# Свойства account_number и balance с геттерами и сеттерами.
# В сеттере для balance реализуйте проверку, что баланс не может быть отрицательным.

class Student:
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise ValueError("Name must be a string")

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            raise ValueError("Grade must be between 0 and 100")


class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, account_number):
        if isinstance(account_number, str):
            self.__account_number = account_number
        else:
            raise ValueError("Account number must be a string")

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            raise ValueError("Balance must be non-negative")


def main():
    # Создание объекта Student
    student = Student("Alice", 85)

    # Доступ и изменение атрибута name
    print(student.name)  # Output: Alice
    student.name = "Bob"
    print(student.name)  # Output: Bob

    # Доступ и изменение атрибута grade
    print(student.grade)  # Output: 85
    student.grade = 90
    print(student.grade)  # Output: 90

    # Проверка валидации оценки
    try:
        student.grade = 105
    except ValueError as e:
        print(e)  # Output: Grade must be between 0 and 100

    # Создание объекта BankAccount
    account = BankAccount("12345678", 1000)

    # Доступ и изменение атрибута account_number
    print(account.account_number)  # Output: 12345678
    account.account_number = "87654321"
    print(account.account_number)  # Output: 87654321

    # Доступ и изменение атрибута balance
    print(account.balance)  # Output: 1000
    account.balance = 1500
    print(account.balance)  # Output: 1500

    # Проверка валидации баланса
    try:
        account.balance = -500
    except ValueError as e:
        print(e)  # Output: Balance must be non-negative


if __name__ == "__main__":
    main()
