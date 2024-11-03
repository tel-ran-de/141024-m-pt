# Проект: Управление библиотекой
#
# Описание:
# Разработайте программу для управления библиотекой. Программа должна позволять добавлять книги в библиотеку,
# удалять книги, искать книги по автору и выводить список всех книг с их авторами и статусами (в наличии или выдана).
#
# Требования: Реализуйте работу всех пунктов меню.


library = [["Война и мир", "Толстой", "в наличии"],
           ["Преступление и наказание", "Достоевский", "выдана"],
           ["Мастер и Маргарита", "Булгаков", "в наличии"]]

while True:
    print("\nМеню")
    print("1. Показать список всех книг")
    print("2. Добавить книгу")
    print("3. Удалить книгу")
    print("4. Поменять статус книги")
    print("5. Показать книги определенного автора")
    print("6. Показать книги с определенным статусом")
    choice = input("Выберите действие, введя его номер: ")

    # Продолжите программу ниже.
    if choice == "1":
        print("\nСписок всех книг:")
        for book in library:
            print(f"{book[0]} - {book[1]} ({book[2]})")

    elif choice == "2":
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        status = input("Введите статус книги (в наличии/выдана): ")
        library.append([title, author, status])
        print(f"Книга '{title}' добавлена.")

    elif choice == "3":
        title = input("Введите название книги, которую хотите удалить: ")
        found = False
        for book in library:
            if book[0].lower() == title.lower():
                library.remove(book)
                found = True
                print(f"Книга '{title}' удалена.")
                break
        if not found:
            print(f"Книга '{title}' не найдена.")

    elif choice == "4":
        title = input("Введите название книги, статус которой хотите поменять: ")
        found = False
        for book in library:
            if book[0].lower() == title.lower():
                new_status = input(f"Введите новый статус для книги '{title}' (в наличии/выдана): ")
                book[2] = new_status
                found = True
                print(f"Статус книги '{title}' изменен на '{new_status}'.")
                break
        if not found:
            print(f"Книга '{title}' не найдена.")

    elif choice == "5":
        author = input("Введите автора: ")
        print(f"\nКниги автора {author}:")
        found = False
        for book in library:
            if book[1].lower() == author.lower():
                print(f"{book[0]} ({book[2]})")
                found = True
        if not found:
            print(f"Книги автора {author} не найдены.")

    elif choice == "6":
        status = input("Введите статус (в наличии/выдана): ")
        print(f"\nКниги со статусом '{status}':")
        found = False
        for book in library:
            if book[2].lower() == status.lower():
                print(f"{book[0]} - {book[1]}")
                found = True
        if not found:
            print(f"Книги со статусом '{status}' не найдены.")

    elif choice == "7":
        print("Программа завершена.")
        break

    else:
        print("Некорректный выбор. Пожалуйста, выберите пункт из меню.")
