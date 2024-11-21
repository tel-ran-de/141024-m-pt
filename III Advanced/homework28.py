from collections.abc import async_generator
from multiprocessing.managers import Value


def p(a):
    print(f'-----{a}-----')
# Задание 1: Реализация геттера и сеттера для класса Person
# Описание:
#
# Создайте класс Person, который будет иметь приватные атрибуты name и age.
# Реализуйте геттеры и сеттеры для этих атрибутов без использования декораторов.
#
# Требования:
#
# Приватные атрибуты __name и __age.
# Методы get_name и set_name для доступа и изменения атрибута __name.
# Методы get_age и set_age для доступа и изменения атрибута __age.
# Проверка, что возраст не может быть отрицательным.
#
p(3)
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age < 0:
            raise ValueError('can not be negative')
        else:
            self.__age = age

def main():
    a = Person('Heidi', 38)
    print(a.__dict__)
    print(a.get_age())
    print(a.get_name())
    a.set_age(25)
    a.set_name('Heidiliny')
    print(a.__dict__)
    try:
        a.set_age(-25)
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()
# Задание 2: Реализация геттера и сеттера для класса Rectangle
# Описание:
#
# Создайте класс Rectangle, который будет иметь приватные атрибуты width и height.
# Реализуйте геттеры и сеттеры для этих атрибутов без использования декораторов.
#
# Требования:
#
# Приватные атрибуты __width и __height.
# Методы get_width и set_width для доступа и изменения атрибута __width.
# Проверка, что ширина должна быть положительной.
# Методы get_height и set_height для доступа и изменения атрибута __height.
# Проверка, что высота должна быть положительной.
p(55)

class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_height(self):
        return self.__height

    def set_height(self, height):
        if height < 0:
            raise ValueError('ERROR: ширина должна быть положительной')
        else:
            self.__height = height

    def get_width(self):
        return self.__width

    def set_width(self, width):
        if width < 0:
            raise ValueError('ERROR: высота должна быть положительной')
        else:
            self.__width = width

def main():
    a = Rectangle(10, 25)
    print(a.get_width())
    print(a.get_height())
    a.set_width(100)
    a.set_height(20)
    print(a.__dict__)
    try:
        a.set_height(-10)
    except ValueError as e:
        print(e)

    try:
        a.set_width(-10)
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()

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
p(113)
class Student:
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, grade):
        if 0 <= grade < 100:
            self.__grade =grade
        else:
            raise ValueError('ERROR: оценка должна быть в диапазоне от 0 до 100')

def main():
    a = Student('Olek', 68)
    print(a.__dict__)
    a.grade = 78
    a.name = 'Oooolek'
    print(a.__dict__)
    print(a.name)
    print(a.grade)
    try:
        a.grade = 101
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()

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
p(166)
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, account_number):
        self.__account_number = account_number

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        if balance < 0:
            raise ValueError('ERROR: баланс не может быть отрицательным')
        else:
            self.__balance = balance

def main():
    a = BankAccount('id:111111', 2000)
    print(a.__dict__)
    a.account_number = 'id:345345'
    a.balance = 1500
    print(a.balance)
    print(a.account_number)
    try:
        a.balance = -200
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()

# Задание 1: Реализация дескриптора для строкового атрибута
# Описание:
#
# Создайте дескриптор StringAttribute, который будет проверять, что устанавливаемое значение является строкой.
# Примените этот дескриптор к атрибуту name в классе Person.
#
# Требования:
#
# Дескриптор StringAttribute должен реализовывать методы __get__, __set__ и __set_name__.
# Метод __set__ должен проверять, что значение является строкой. Если значение не является строкой,
# должно вызываться исключение ValueError.
# Класс Person должен использовать дескриптор StringAttribute для атрибута name.
p(217)
class StringAttribute:
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, None)

    def __set__(self, instance, value):
        # if isinstance(value, str):
        # if type(value) == str:
        if value == str(value):
            instance.__dict__[self.name] = value
        else:
            raise ValueError('ERROR: значение не является строкой')

    def __set_name__(self, owner, name):
        self.name = name


class Person:
    name = StringAttribute()
    def __init__(self, name):
        self.name = name

def main():
    a = Person('Klerik')
    print(a.__dict__)
    print(a.name)
    a.name = 'Mlerik'
    print(a.name)
    try:
        a.name = 123
    except ValueError as e:
        print(e)
    try:
        b = Person(12334)
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()
