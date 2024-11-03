# Тема: Цикл while. Операторы break, continue, else.

# Упражнение 1: Поиск числа
#
# Напишите программу, которая запрашивает у пользователя числа, пока он не введет число совпадающее
# с переменной num (num = любое число от 0 до 100).  Если введенное число меньше num, программа должна
# выводить сообщение "Слишком маленькое число" и продолжать запрашивать числа. Если число больше num,
# программа должна вывести сообщение "Вы ввели большее число" и продолжать запрашивать числа.
# Если пользователь угадал, то программа должна вывести "Вы угадали число" и завершиться.

# Упражнение 2: Проверка пароля
#
# Напишите программу, которая будет запрашивать у пользователя пароль до тех пор, пока не будет введен
# правильный пароль "python123", либо пока не закончатся попытки. Если введенный пароль содержит пробелы,
# программа должна выводить сообщение "Пароль не должен содержать пробелов" и продолжать запрашивать пароль.
# Если введен правильный пароль, программа должна выводить сообщение "Доступ разрешен" и завершаться.
# Если после трех неправильных попыток пароль не введен правильно, программа должна выводить сообщение
# "Превышено количество попыток" и завершаться.



# Упражнение 3: Работа со списком покупок
#
# Напишите программу, которая будет запрашивать у пользователя элементы для списка покупок до тех пор,
# пока не будет введено слово "стоп", либо пока количество покупок не станет больше 6. Если введенное
# слово уже есть в списке, программа должна выводить сообщение "Этот элемент уже в списке" и продолжать
# запрашивать новые элементы. Если введено слово "стоп", программа должна выводить сообщение
# "Формирование списка завершено" и завершаться. Если количество покупок ставится больше 6,
# то программа должна вывести: “Превышен лимит покупок.” и завершиться.
# Перед завершением программа должна выводить итоговый список покупок и общее количество элементов в нем.


# Тема: Цикл for

# Упражнение 1: Подсчет гласных в строке
#
# Напишите программу, которая принимает строку от пользователя и подсчитывать количество гласных букв (a, e, i, o, u)
# в этой строке.Используйте цикл for и условие if.


# Упражнение 2: Генерация и вывод последовательности чисел
#
# Напишите программу, которая генерит и выводит последовательность чисел от 1 до 20,
# но выводит "Fizz" вместо чисел, кратных 3, "Buzz" вместо чисел, кратных 5, и "FizzBuzz"
# вместо чисел, кратных как 3, так и 5. Используйте цикл for и функцию range.


# Проект 1: Управление библиотекой
#
# Описание:
# Разработайте программу для управления библиотекой. Программа должна позволять добавлять книги в библиотеку,
# удалять книги, искать книги по автору и выводить список всех книг с их авторами и статусами (в наличии или выдана).
#
# Требования: Реализуйте работу всех пунктов меню.
#
# library = [["Война и мир", "Толстой", "в наличии"],
#            ["Преступление и наказание", "Достоевский", "выдана"],
#            ["Мастер и Маргарита", "Булгаков", "в наличии"]]
#
# while True:
#     print("\nМеню")
#     print("1. Показать список всех книг")
#     print("2. Добавить книгу")
#     print("3. Удалить книгу")
#     print("4. Поменять статус книги")
#     print("5. Показать книги определенного автора")
#     print("6. Показать книги с определенным статусом")
#     choice = input("Выберите действие, введя его номер: ")
#
#     # Продолжите программу ниже.


# Проект 2: Анализ посещаемости на сайте
#
# Разработайте программу для анализа посещаемости на сайте. Программа должна позволять вводить количество посещений
# за каждый день недели, определять дни с наибольшей и наименьшей посещаемостью, рассчитывать среднюю посещаемость
# за неделю и выводить дни с посещаемостью выше среднего.
#
# days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
# visits = []