# Ex 1
# Создайте базовый класс `Person` с атрибутами `name` и `age`.
# Затем создайте два производных класса `Student` и `Teacher`.
# Класс `Student` должен иметь дополнительный атрибут `student_id`, а класс `Teacher` — атрибут `subject`.
# Реализуйте методы для вывода информации о каждом объекте.

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
    """
    Class Teacher
    attributes: subject: string
    """
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        return f"{super().display_info()}, Subject: {self.subject}"


# Ex 2
# Создайте класс `Vehicle` с атрибутами `make` и `model`.
# Создайте производный класс `Car` с дополнительным атрибутом `num_doors` (количество дверей) и
# производный класс `Motorcycle` с атрибутом `has_sidecar` (имеет ли мотоцикл коляску).
# Реализуйте метод, который выводит полное описание транспортного средства.

class Vehicle:
    """
    Class Vehicle
    attributes:
        make: string
        model: string
    """
    pass  # you code here


class Car(Vehicle):
    """
    Class Car
    attributes:
        num_doors: int
    """
    pass  # you code here


class Motorcycle(Vehicle):
    """
    Class Motorcycle
    attributes:
        has_sidecar: bool
    """
    pass  # you code here


def main():
    # Создание объектов и вывод информации
    student = Student(name="Alice", age=20, student_id=12345)
    teacher = Teacher(name="Bob", age=40, subject="Mathematics")
    # car = Car(make="Toyota", model="Corolla", num_doors=4)
    # motorcycle = Motorcycle(make="Harley-Davidson", model="Sportster", has_sidecar=False)

    print(student.display_info())
    print(teacher.display_info())
#     print(car.display_info())
#     print(motorcycle.display_info())


if __name__ == '__main__':
    main()
