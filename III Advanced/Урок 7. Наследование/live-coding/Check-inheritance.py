# Проверка отношений наследования
# Задача:
#
# Создайте иерархию классов для различных типов сотрудников.
# Используйте функцию issubclass() для проверки, являются ли определенные классы подклассами других классов
# в этой иерархии.
#
# Шаги:
# Создайте базовый класс Employee.
# Создайте подклассы Manager, Engineer и Intern, которые наследуются от Employee.
# Создайте подкласс SoftwareEngineer, который наследуется от Engineer.
# Напишите функцию, которая принимает два класса и возвращает, является ли первый класс подклассом второго.
# Протестируйте функцию с использованием созданных классов.
#
# Реализация:
# Создание классов: Мы создаем базовый класс Employee и несколько подклассов
# (Manager, Engineer, Intern, SoftwareEngineer).
# Функция проверки: Функция check_subclass использует issubclass для проверки,
# является ли первый переданный класс подклассом второго.
# Тестирование: Примеры проверок показывают, как issubclass может определить отношения наследования
# между различными классами.

class Employee:
    pass


class Manager(Employee):
    pass


class Engineer(Employee):
    pass


class Intern(Employee):
    pass


class SoftwareEngineer(Engineer):
    pass


def main():
    # Тестирование
    print(issubclass(SoftwareEngineer, Engineer))  # Output: True
    print(issubclass(SoftwareEngineer, Employee))  # Output: True
    print(issubclass(Manager, Engineer))  # Output: False
    print(issubclass(Intern, Employee))  # Output: True
    print(issubclass(SoftwareEngineer, object))  # Output: True


if __name__ == "__main__":
    main()
