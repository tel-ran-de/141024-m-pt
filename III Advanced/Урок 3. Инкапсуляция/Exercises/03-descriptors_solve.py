# Задание 2: Реализация дескриптора для строкового атрибута
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

class StringAttribute:
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, None)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Person:
    name = StringAttribute()

    def __init__(self, name):
        self.name = name


def main():
    # Использование
    person = Person("Alice")
    print(person.name)  # Output: Alice

    try:
        person.name = 123
    except ValueError as e:
        print(e)  # Output: Value must be a string


if __name__ == "__main__":
    main()
