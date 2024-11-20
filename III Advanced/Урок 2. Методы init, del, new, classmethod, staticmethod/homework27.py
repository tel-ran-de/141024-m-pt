# 01-Constructors
def p(a):
    print(f'\n------{a}------')
#

# Задание 1: Работа с методами __init__ и __del__.
# Создайте класс Book, который будет иметь атрибуты title, author и year.
# Реализуйте методы __init__ и __del__ для инициализации объектов и
# вывода сообщения при удалении объекта соответственно.
#
# Метод __init__ должен инициализировать атрибуты title, author и year.
# Метод __del__ должен выводить сообщение, содержащее название книги и автора, когда объект удаляется.
p(5)
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        print(f'Das Buch {self.title} von {self.author} ist gelöscht')

def main():
    a = Book('Spiele', 'HR', 2024)
    print(a.__dict__)
    del a
if __name__ == '__main__':
    main()




#
# Задание 2: Вызов конструктора базового класса.
#
# Создайте базовый класс Animal, который будет иметь атрибуты name и age.
# Затем создайте производный класс Dog, который будет наследовать от Animal и добавит атрибут breed.
# Реализуйте вызов конструктора базового класса внутри конструктора производного класса.
#
# Класс Animal должен иметь метод __init__, инициализирующий атрибуты name и age.
# Класс Dog должен наследовать от Animal и иметь свой метод __init__, который вызывает конструктор базового класса
# и инициализирует атрибут breed.
#
p(34)
class Animal:
    num_an = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Animal.num_an += 1

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

def main():
    a= Dog('Hanny', 4, 'Mops')
    print(a.name)
    print(a.__dict__)
    print(Animal.num_an)

if __name__== '__main__':
    main()


#
# 02-Static_Class_method
#
#
# Задание 3: Работа с методами класса.
# Создайте класс Library, который будет отслеживать количество созданных библиотек и
# хранить общее количество книг во всех библиотеках.
#
# Реализуйте атрибут класса total_books, который будет отслеживать общее количество книг во всех библиотеках.
# Реализуйте метод класса get_total_books, который будет возвращать значение total_books.
# Реализуйте метод класса add_books, который будет принимать количество книг в качестве аргумента и
# добавлять их к total_books.
# Метод __init__ должен увеличивать счетчик количества библиотек.
#
p(71)
class Library:
    total_library = 0
    total_books = 0
    def __init__(self, numb_books = 0):
        Library.total_library += 1
        self.numb_books = numb_books
        Library.total_books += numb_books

    def add_books(self, num):
        self.num = num
        Library.total_books += num
        self.numb_books += num

    def get_total_books(self):
        return Library.total_books

    def get_total_library(self):
        return Library.total_library

    def get_book_in_library(self):
        return self.numb_books

    def __del__(self):
        Library.total_library -=1
        Library.total_books -= self.numb_books
        print('Library is deleted')

def main():
    a = Library()
    print(f'Librarys now - {Library.total_library}')
    print(f'Books in thise libary: {a.numb_books}')
    print(f'All-Books now - {Library.total_books}')

    b = Library(10)
    print()
    print(f'Librarys now -{Library.total_library}')
    print(f'Books in thise libary: {b.numb_books}')
    print(f'All-Books now - {Library.total_books}')
    del b
    print()
    print(f'Librarys now -{Library.total_library}')
    print(f'All-Books now - {Library.total_books}')
if __name__ == '__main__': #Почему удаляется а
    main()

# Задание 4: Работа со статическими методами.
# Создайте класс MathOperations, который будет содержать статические методы для
# выполнения различных математических операций.
#
# Реализуйте статический метод add, который будет принимать два числа и возвращать их сумму.
# Реализуйте статический метод subtract, который будет принимать два числа и возвращать результат их вычитания.
# Реализуйте статический метод multiply, который будет принимать два числа и возвращать их произведение.
# Реализуйте статический метод divide, который будет принимать два числа и возвращать результат их деления.
# Если второе число равно нулю, метод должен возвращать сообщение об ошибке.
#
p(127)
class MathOperations:

    @staticmethod
    def add(a, s):
        return a + s

    @staticmethod
    def substract(a, s):
        return a - s

    @staticmethod
    def multiply(a, s):
        return a * s

    @staticmethod
    def divide(a, s):
        if s == 0:
            return f'На ноль делить нельзя'
        else:
            return a / s

def main():
    a = MathOperations()
    print()
    print(f'{a.add(2,4)}')
    print(a.substract(2, 4))
    print(a.multiply(2, 4))
    print(a.divide(2, 0))
    print(a.divide(2, 4))
if __name__ == '__main__':
    main()
#
# 03-New_Singleton
#
#
# Задание 5: Реализация Singleton для подключения к базе данных.
#
# Создайте класс DatabaseConnection, который будет реализовывать паттерн Singleton.
# Этот класс должен содержать информацию о подключении к базе данных и обеспечивать, что существует
# только один экземпляр подключения.
#
# Требования:
# Реализуйте класс DatabaseConnection с атрибутом класса _instance, который будет хранить единственный экземпляр класса.
# Метод __new__ должен гарантировать, что создается только один экземпляр класса.
# Реализуйте метод connect, который будет выводить сообщение о подключении к базе данных.
# Продемонстрируйте, что при создании нескольких объектов класса DatabaseConnection все они ссылаются на
# один и тот же экземпляр.
p(173)
class DatabaseConnection:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value):
        self.value = value

    @staticmethod
    def connect():
        return DatabaseConnection._instance

def main():
    a = DatabaseConnection('url_a')
    # print(a.connect())
    print("a - ", a.value)
    print(id(a))
    b = DatabaseConnection('url_b')
    print(id(b))
    print(b.connect())
    print(a.connect())
    print("b - ", b.value)
    print("a - ", a.value)

if __name__ == '__main__':
    main()

# Задание 6: Реализация Singleton для логгера.
#
# Создайте класс Logger для ведения логов, который будет реализовывать паттерн Singleton.
# Этот класс должен обеспечивать, что существует только один экземпляр логгера.
#
# Требования:
#
# Реализуйте класс Logger с атрибутом класса _instance, который будет хранить единственный экземпляр класса.
# Метод __new__ должен гарантировать, что создается только один экземпляр класса.
# Реализуйте метод log_message, который будет принимать строку и выводить сообщение о записи лога.
# Продемонстрируйте, что при создании нескольких объектов класса Logger все они ссылаются на один и тот же экземпляр.
p(215)
class Loger:
    _instance = None
    user_id_mane = None
    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, user_name):
        self.user_name = user_name
        if Loger.user_id_mane == None:
            Loger.user_id_mane = user_name
        else:
            Loger.user_id_mane = Loger.user_id_mane

    @staticmethod
    def log_message():
        return f'{Loger.user_id_mane} is logget'

def main():
    a = Loger('Heinrich')
    print(a.log_message())
    print(a.user_name)
    b = Loger('Benny')
    print(b.log_message())

if __name__ == '__main__':
    main()