# Ex 1
# Создайте базовый класс `Person` с атрибутами `name` и `age`.
# Затем создайте два производных класса `Student` и `Teacher`.
# Класс `Student` должен иметь дополнительный атрибут `student_id`, а класс `Teacher` — атрибут `subject`.
# Реализуйте методы для вывода информации о каждом объекте.
from functools import total_ordering
from stringprep import b1_set


def p(a):
    print(f'\n-----{a}-----')
p(1)
class Person:
    """
    Base class Person
    attributes:
        name: string
        age: int
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"


class Student(Person):
    """
    Class Student
    attributes: student_id: int
    """
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        return f"{super().display_info()}, Student ID: {self.student_id}"


class Teacher(Person):
    'hallo world'
    """
    Class Teacher
    attributes: subject: string
    """
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        return f"{super().display_info()}, Subject: {self.subject}"

a = Teacher('Anna', 22, 1000821)

print(a.__doc__)# print 35
print(a.__dict__)
print(a.display_info())
for i in a.__dict__:
    print(f'{i} --- {a.__dict__[i]}')


# Ex 2
# Создайте класс `Vehicle` с атрибутами `make` и `model`.
# Создайте производный класс `Car` с дополнительным атрибутом `num_doors` (количество дверей) и
# производный класс `Motorcycle` с атрибутом `has_sidecar` (имеет ли мотоцикл коляску).
# Реализуйте метод, который выводит полное описание транспортного средства.
p(59)
class Vehicle:
    "Введите мк и модель"
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def f(self):
        return f'Make: {self.make}, Model: {self.model}'

class Car(Vehicle):
    "Mashinka"
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def f(self):
        return f"{super().f()}, Numbers of doors: {self.num_doors}"

class Motorcycle(Vehicle):
    "Motik!!!"
    def __init__(self, make, model, has_sidecar):
        super().__init__(make, model)
        self.has_sidercar = has_sidecar

    def f(self):
        return f'{super().f()}, sidecar -{self.has_sidercar}'

kawa = Motorcycle('kawa', 'sport', True)

print(kawa.__doc__)
print(kawa.f())
print()
zaper = Car('Zapor', 'Sport', 2)
print(zaper.__doc__)
print(zaper.__dict__)
print(zaper.model, zaper.make, zaper.num_doors)


# Ex 1
# Создайте класс `Library`, у которого будет атрибут класса `total_books` и
# атрибут объекта `books` (список книг в данной библиотеке).
# Реализуйте методы для добавления книги в библиотеку и вывода общего количества книг во всех библиотеках.
#
# Ex 2
# Создайте класс `Company` с атрибутом класса `company_name` и
# атрибутом объекта `employees` (список сотрудников).
# Реализуйте методы для добавления сотрудника и вывода списка всех сотрудников данной компании.

p(103)
class Company:
    """
    Class Company
    attributes:
        company_name: string (class attribute)
        employees: list (instance attribute)
    """
    company_name = "Default Company"

    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_employees(self):
        return self.employees

class Library:
    'Library for me'
    total_books = 0
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        Library.total_books += 1

    def f(self):
        return f'{len(self.books)}книг всего в этой библиотеке\nтут вы найдете следующие книги:\n{self.total_books}'


def main():
   # Создание объектов и выполнение операций
    library1 = Library()
    library2 = Library()

    library1.add_book("Book 1")
    library1.add_book("Book 2")
    library2.add_book("Book 3")

    print(f"Total books in all libraries: {Library.total_books}")  # Output: 3
    print(f"Books in library1: {library1.books}")  # Output: ['Book 1', 'Book 2']
    print(f"Books in library2: {library2.books}")  # Output: ['Book 3']

    company1 = Company()
    company2 = Company()

    company1.add_employee("Alice")
    company1.add_employee("Bob")
    company2.add_employee("Charlie")

    print(f"Employees in company1: {company1.get_employees()}")  # Output: ['Alice', 'Bob']
    print(f"Employees in company2: {company2.get_employees()}")  # Output: ['Charlie']


if __name__ == '__main__':
    main()

# Ex 1
# Создайте класс `BankAccount` с публичным атрибутом `owner` и приватным атрибутом `__balance`.
# Реализуйте методы для внесения депозита и снятия денег, обеспечивая корректность операций
# (например, нельзя снять больше, чем есть на балансе).
#
# Ex 2
# Создайте класс `Product` с публичным атрибутом `name` и приватным атрибутом `__price`.
# Реализуйте методы для получения и изменения цены,
# добавив проверки на корректность (цена не может быть отрицательной).
p(176)
class Product:

    def __init__(self, name, price = 32.25):
        self.name = name
        self.__price = price

    def set_price(self, new):
        if new >= 0:
            self.__price = new
        else:
            print('Price can\'t be negative')

    def get_price(self):
        return self.__price


class BankAccount:
    """
    Class BankAccount
    attributes:
        owner: string (public attribute)
        __balance: float (private attribute)
    """
    def __init__(self, owner, initial_balance=0.0):
        self.owner = owner
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew {amount}. New balance: {self.__balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.__balance


def main1():
    # Создание объектов и выполнение операций
    account_alice = BankAccount("Alice", 1000.0)
    account_alice .deposit(500.0)  # Output: Deposited 500.0. New balance: 1500.0
    account_alice .withdraw(200.0)  # Output: Withdrew 200.0. New balance: 1300.0
    account_alice .withdraw(2000.0)  # Output: Insufficient funds.
    print(f"Final balance: {account_alice .get_balance()}")  # Output: Final balance: 1300.0

    product = Product("Laptop", 999.99)
    print(f"Product price: {product.get_price()}")  # Output: Product price: 999.99
    product.set_price(899.99)  # Output: Price updated to 899.99.
    print(f"Product price: {product.get_price()}")
    product.set_price(-100.0)  # Output: Price cannot be negative.


if __name__ == '__main__':
    main1()

# Ex 1
# Создайте класс `Employee` с приватными атрибутами `__name` и `__salary`.
# Реализуйте геттеры и сеттеры для этих атрибутов, добавив проверку,
# что зарплата не может быть ниже минимальной зарплаты (например, 10000).
p(252)
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

def main2():
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
    main2()
# Ex 2
# Создайте класс `Circle` с приватным атрибутом `__radius`.
# Реализуйте свойства (property) для получения и установки значения радиуса,
# а также метод для вычисления площади круга.

p(304)
import math
class Circle:
    def __init__(self, radius=1):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if radius >= 0:
            self.__radius = radius
        else:
            raise ValueError("Radius must be positiv")

    def squer(self):
            return math.pi * self.__radius ** 2# При негативном радиусе ....



a = Circle()
print(a.squer())
try :
    a.radius =-2
except ValueError as error:
    print(error)
print(a.squer())
print(a.radius)



# Ex 1
# Создайте класс `Temperature` с методами для преобразования температуры из градусов Цельсия в Фаренгейты и Кельвины.
# Реализуйте методы как статические.
p(342)
class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32

    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15

if __name__ == '__main__':
    # Пример использования класса Temperature
    celsius = 25
    print(f"{celsius}°C = {Temperature.celsius_to_fahrenheit(celsius)}°F")
    print(f"{celsius}°C = {Temperature.celsius_to_kelvin(celsius)}K")
# #### Задание 2:
# Создайте класс `Counter` с атрибутом класса `count`,
# который будет отслеживать количество созданных экземпляров класса.
# Реализуйте метод класса `get_count`, который возвращает текущее значение `count`.
p(361)
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1 #почему не идёт ни подсчет ни изменение локальной переменной если  "Counter" заменить на "self"

    def f():
        return Counter.count

a = Counter()
b= Counter()
print(Counter.count)

# Ex 1
# Создайте базовый класс `Appliance` с методом `turn_on`, который должен быть переопределен в
# производных классах `WashingMachine` и `Refrigerator`.
# В каждом из производных классов метод `turn_on` должен выводить сообщение о том, что прибор включен.
# Создайте список различных приборов и продемонстрируйте полиморфизм, вызвав метод `turn_on` для каждого прибора.

from abc import ABC, abstractmethod


# Базовый класс
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass


# Производный класс WashingMachine
class WashingMachine(Appliance):
    def turn_on(self):
        print("Washing machine is now running.")


# Производный класс Refrigerator
class Refrigerator(Appliance):
    def turn_on(self):
        print("Refrigerator is now cooling.")



# Демонстрация полиморфизма
if __name__ == '__main__':
    appliances = [WashingMachine(), Refrigerator()]

    for appliance in appliances:
        appliance.turn_on()  # Вызов метода turn_on для каждого прибора


# #### Задание 2:
# Создайте базовый класс `Employee` с методом `calculate_pay`,
# который должен быть переопределен в производных классах `SalariedEmployee` и `HourlyEmployee`.
# В классе `SalariedEmployee` метод должен рассчитывать ежемесячную зарплату на основе фиксированного оклада,
# а в классе `HourlyEmployee` — на основе количества отработанных часов и почасовой ставки.
# Продемонстрируйте полиморфизм, вызвав метод `calculate_pay` для объектов различных классов.

p(415)# ???? по аналогии с 361 ?????
class Employee(ABC):
    @abstractmethod
    def calculate_pay(self):
        pass

class SalariedEmployee(Employee):
    fix_mony = 1200
    num_se = 0
    def __init__(self):
        SalariedEmployee.num_se += 1

    def calculate_pay(self):
        print(f'У нас работают {SalariedEmployee.num_se} рабочих\n и ежемесячно мы выплачиваем {SalariedEmployee.num_se * SalariedEmployee.fix_mony}')

class HourlyEmployee(Employee):
    h_mony = 12
    h_in_week = 0
    def __init__(self):
        HourlyEmployee.h_in_week += 1

    def calculate_pay(self):
        print(f'у нас работают {HourlyEmployee.h_in_week} человек\n они вырабатывают в неделю {HourlyEmployee.h_in_week * 40} часов\nэто нам обходится в {HourlyEmployee.h_in_week * 40 * HourlyEmployee.h_mony}')


a1 = HourlyEmployee()
a2 = HourlyEmployee()
print(a2.calculate_pay())

b1 = SalariedEmployee()
print(b1.calculate_pay())
b2 = SalariedEmployee()
print(b2.calculate_pay())
b3 = SalariedEmployee()
print(b3.calculate_pay())
b4 = SalariedEmployee()
print(b4.calculate_pay())