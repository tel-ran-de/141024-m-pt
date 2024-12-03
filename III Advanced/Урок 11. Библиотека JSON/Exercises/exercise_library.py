### Задача: Управление библиотекой

#### Описание:
# Создайте систему управления библиотекой, которая позволяет добавлять книги, пользователей и отслеживать,
# какие книги взяты пользователями.
# Система должна поддерживать сохранение и загрузку данных в формате JSON.

#### Требования:
# 1. Класс `Book` должен иметь поля: `title`, `author`, и `available` (доступна ли книга).
# 2. Класс `User` должен иметь поля: `name` и `borrowed_books` (список книг, которые пользователь взял).
# 3. Класс `Library` должен иметь поля: `books` (список всех книг) и `users` (список всех пользователей).
# 4. Методы для добавления книг и пользователей в библиотеку.
# 5. Методы для взятия и возврата книг пользователями.
# 6. Методы для сохранения и загрузки данных библиотеки в формате JSON.

#### Решение:


import json


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def to_dict(self):
        ...

    @classmethod
    def from_dict(cls, data):
        ...


class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def to_dict(self):
        ...

    @classmethod
    def from_dict(cls, data):
        ...


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        ...

    def add_user(self, user):
        ...

    def borrow_book(self, user, book_title):
        ...

    def return_book(self, user, book_title):
        ...

    def to_dict(self):
        ...

    @classmethod
    def from_dict(cls, data):
        ...


def save_library_to_json(library, filename):
    ...


def load_library_from_json(filename):
    ...


def main():
    # Создаем библиотеку
    library = Library()

    # Добавляем книги
    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))

    # Добавляем пользователей
    user1 = User("Alice")
    user2 = User("Bob")
    library.add_user(user1)
    library.add_user(user2)

    # Пользователь берет книгу
    library.borrow_book(user1, "1984")

    # Сохраняем библиотеку в JSON файл
    save_library_to_json(library, 'library.json')

    # Загружаем библиотеку из JSON файла
    loaded_library = load_library_from_json('library.json')

    # Выводим информацию о загруженной библиотеке
    for user in loaded_library.users:
        print(f"User: {user.name}")
        for book in user.borrowed_books:
            print(f"  Borrowed Book: {book.title} by {book.author}")


if __name__ == '__main__':
    main()
