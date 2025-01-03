# 01-Constructors
#
#
# Задание 1: Работа с методами __init__ и __del__.
# Создайте класс Book, который будет иметь атрибуты title, author и year.
# Реализуйте методы __init__ и __del__ для инициализации объектов и
# вывода сообщения при удалении объекта соответственно.
#
# Метод __init__ должен инициализировать атрибуты title, author и year.
# Метод __del__ должен выводить сообщение, содержащее название книги и автора, когда объект удаляется.
#
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
#
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
#
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
#
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
