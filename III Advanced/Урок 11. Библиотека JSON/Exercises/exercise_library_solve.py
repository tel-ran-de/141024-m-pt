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
        return {
            'title': self.title,
            'author': self.author,
            'available': self.available
        }

    @classmethod
    def from_dict(cls, data):
        book = cls(data['title'], data['author'])
        book.available = data['available']
        return book


class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def to_dict(self):
        return {
            'name': self.name,
            'borrowed_books': [book.to_dict() for book in self.borrowed_books]
        }

    @classmethod
    def from_dict(cls, data):
        user = cls(data['name'])
        user.borrowed_books = [Book.from_dict(book_data) for book_data in data['borrowed_books']]
        return user


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def borrow_book(self, user, book_title):
        for book in self.books:
            if book.title == book_title and book.available:
                book.available = False
                user.borrowed_books.append(book)
                return True
        return False

    def return_book(self, user, book_title):
        for book in user.borrowed_books:
            if book.title == book_title:
                book.available = True
                user.borrowed_books.remove(book)
                return True
        return False

    def to_dict(self):
        return {
            'books': [book.to_dict() for book in self.books],
            'users': [user.to_dict() for user in self.users]
        }

    @classmethod
    def from_dict(cls, data):
        library = cls()
        library.books = [Book.from_dict(book_data) for book_data in data['books']]
        library.users = [User.from_dict(user_data) for user_data in data['users']]
        return library


def save_library_to_json(library, filename):
    with open(filename, 'w') as file:
        json.dump(library.to_dict(), file, indent=4)


def load_library_from_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        return Library.from_dict(data)


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


### Объяснение:
# 1. **Класс `Book`**:
# Представляет книгу с полями `title`, `author` и `available`.
# Методы `to_dict` и `from_dict` используются для сериализации и десериализации объектов.

# 2. **Класс `User`**:
# Представляет пользователя с полями `name` и `borrowed_books`.
# Методы `to_dict` и `from_dict` используются для сериализации и десериализации объектов.

# 3. **Класс `Library`**:
# Представляет библиотеку с полями `books` и `users`.
# Методы для добавления книг и пользователей, а также для взятия и возврата книг.
# Методы `to_dict` и `from_dict` используются для сериализации и десериализации объектов.

# 4. **Функции `save_library_to_json` и `load_library_from_json`**:
# Сохраняют и загружают данные библиотеки в формате JSON.

# 5. **Функция `main`**:
# Демонстрирует создание библиотеки, добавление книг и пользователей, взятие книги пользователем,
# сохранение и загрузку данных библиотеки.
