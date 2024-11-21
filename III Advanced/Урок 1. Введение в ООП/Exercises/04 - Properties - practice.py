# Ex 1
# Создайте класс `Employee` с приватными атрибутами `__name` и `__salary`.
# Реализуйте геттеры и сеттеры для этих атрибутов, добавив проверку,
# что зарплата не может быть ниже минимальной зарплаты (например, 10000).

class Employee:
    """
    Class Employee
    attributes:
        __name: string (private attribute)
        __salary: float (private attribute)
    """
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary  # Используем сеттер для проверки

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary >= 10000:
            self.__salary = salary
        else:
            raise ValueError("Salary cannot be less than 10000")

# Ex 2
# Создайте класс `Circle` с приватным атрибутом `__radius`.
# Реализуйте свойства (property) для получения и установки значения радиуса,
# а также метод для вычисления площади круга.


def main():
    # Создание объектов и выполнение операций
    employee = Employee("Alice", 12000)
    print(f"Employee name: {employee.name}")  # Output: Employee name: Alice
    print(f"Employee salary: {employee.salary}")  # Output: Employee salary: 12000

    try:
        employee.salary = 9000  # Это вызовет исключение
    except ValueError as e:
        print(e)  # Output: Salary cannot be less than 10000

    employee.salary = 15000
    print(f"Updated employee salary: {employee.salary}")  # Output: Updated employee salary: 15000


if __name__ == '__main__':
    main()
