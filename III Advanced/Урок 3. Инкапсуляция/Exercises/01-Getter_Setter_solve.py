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

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise ValueError("Name must be a string")

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            raise ValueError("Age must be non-negative")


class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def set_width(self, width):
        if width > 0:
            self.__width = width
        else:
            raise ValueError("Width must be positive")

    def get_height(self):
        return self.__height

    def set_height(self, height):
        if height > 0:
            self.__height = height
        else:
            raise ValueError("Height must be positive")


def main():
    # Ex 1
    # Создание объекта Person
    person = Person("Alice", 30)

    # Доступ и изменение атрибута name
    print(person.get_name())  # Output: Alice
    person.set_name("Bob")
    print(person.get_name())  # Output: Bob

    # Доступ и изменение атрибута age
    print(person.get_age())  # Output: 30
    person.set_age(35)
    print(person.get_age())  # Output: 35

    # Проверка валидации возраста
    try:
        person.set_age(-5)
    except ValueError as e:
        print(e)  # Output: Age must be non-negative

    # Ex 2
    # Создание объекта Rectangle
    rectangle = Rectangle(10, 20)

    # Доступ и изменение атрибута width
    print(rectangle.get_width())  # Output: 10
    rectangle.set_width(15)
    print(rectangle.get_width())  # Output: 15

    # Доступ и изменение атрибута height
    print(rectangle.get_height())  # Output: 20
    rectangle.set_height(25)
    print(rectangle.get_height())  # Output: 25

    # Проверка валидации высоты и ширины
    try:
        rectangle.set_width(-5)
    except ValueError as e:
        print(e)  # Output: Width must be positive

    try:
        rectangle.set_height(-10)
    except ValueError as e:
        print(e)  # Output: Height must be positive


if __name__ == "__main__":
    main()
