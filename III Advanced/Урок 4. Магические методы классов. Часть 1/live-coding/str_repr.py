# Ex 1
# Создайте класс `Library`, у которого будет атрибут класса `total_books` и
# атрибут объекта `books` (список книг в данной библиотеке).
# Реализуйте методы для добавления книги в библиотеку и вывода общего количества книг во всех библиотеках.
#
# Ex 2
# Создайте класс `Company` с атрибутом класса `company_name` и
# атрибутом объекта `employees` (список сотрудников).
# Реализуйте методы для добавления сотрудника и вывода списка всех сотрудников данной компании.

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

    def __str__(self):
        return f"Company: {self.company_name}, employees: {self.employees}"

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.employees)

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_employees(self):
        return self.employees



def main():
    # Создание объектов и выполнение операций
    # library1 = Library()
    # library2 = Library()
    #
    # library1.add_book("Book 1")
    # library1.add_book("Book 2")
    # library2.add_book("Book 3")
    #
    # print(f"Total books in all libraries: {Library.get_total_books()}")  # Output: 3
    # print(f"Books in library1: {library1.books}")  # Output: ['Book 1', 'Book 2']
    # print(f"Books in library2: {library2.books}")  # Output: ['Book 3']

    company1 = Company()
    company2 = Company()

    company1.add_employee("Alice")
    company1.add_employee("Bob")
    company2.add_employee("Charlie")

    print(f"Employees in company1: {company1.get_employees()}")  # Output: ['Alice', 'Bob']
    print(f"Employees in company2: {company2.get_employees()}")  # Output: ['Charlie']

    print(company1)
    repr(company1)
    print(len(company1))
    print(len(company2))

if __name__ == '__main__':
    main()
