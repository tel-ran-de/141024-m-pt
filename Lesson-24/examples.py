import datetime

# 1. Получение текущей даты и времени
now = datetime.datetime.now()
print(now)  # Вывод: текущие дата и время, например, 2024-05-21 15:26:53.123456

# 2. Получение текущей даты
today = datetime.date.today()
print(today)  # Вывод: текущая дата, например, 2024-05-21

# 3. Создание объекта даты
my_date = datetime.date(2023, 5, 21)
print(my_date)  # Вывод: 2023-05-21

# 4. Создание объекта времени
my_time = datetime.time(15, 30, 0)
print(my_time)  # Вывод: 15:30:00

# 5. Создание объекта даты и времени
my_datetime = datetime.datetime(2023, 5, 21, 15, 30, 0)
print(my_datetime)  # Вывод: 2023-05-21 15:30:00

# 6. Разбор строки в объект даты и времени (строка -> datetime)
date_string = "2023-05-21 15:30:00"
date_object = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(date_object)  # Вывод: 2023-05-21 15:30:00

# 7. Форматирование объекта даты и времени в строку (datetime -> строка)
now = datetime.datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)  # Вывод: 2024-05-21 15:26:53

# 8. Получение компонента даты или времени
now = datetime.datetime.now()
print(now.year)    # Вывод: текущий год, например, 2024
print(now.month)   # Вывод: текущий месяц, например, 5
print(now.day)     # Вывод: текущий день, например, 21
print(now.hour)    # Вывод: текущий час, например, 15
print(now.minute)  # Вывод: текущая минута, например, 26
print(now.second)  # Вывод: текущая секунда, например, 53

# 9. Вычисление разницы между двумя датами (timedelta)
date1 = datetime.date(2023, 5, 21)
date2 = datetime.date(2022, 5, 21)
difference = date1 - date2
print(difference.days)  # Вывод: 365

# 10. Добавление или вычитание времени с использованием timedelta
now = datetime.datetime.now()
future = now + datetime.timedelta(days=10)
print(future)  # Вывод: дата и время через 10 дней от текущей

past = now - datetime.timedelta(days=10)
print(past)  # Вывод: дата и время 10 дней назад от текущей

# 11. Работа с часовыми поясами
import pytz

utc = pytz.UTC
eastern = pytz.timezone('US/Eastern')

now = datetime.datetime.now(utc)
print(now)  # Вывод: текущие дата и время в UTC

eastern_time = now.astimezone(eastern)
print(eastern_time)  # Вывод: текущие дата и время в часовом поясе US/Eastern


import os

# 1. Получение текущей рабочей директории
current_directory = os.getcwd()
print(current_directory)  # Вывод: текущая рабочая директория

# 2. Изменение текущей рабочей директории
os.chdir('/path/to/new_directory')
print(os.getcwd())  # Вывод: новая рабочая директория /path/to/new_directory

# 3. Список файлов и директорий в указанной директории
files_and_directories = os.listdir('.')
print(files_and_directories)  # Вывод: ['file1.txt', 'file2.txt', 'directory1']

# 4. Создание новой директории
os.mkdir('new_directory')  # Создает директорию с именем 'new_directory'

# 5. Удаление директории
os.rmdir('new_directory')  # Удаляет директорию с именем 'new_directory'

# 6. Удаление файла
os.remove('file1.txt')  # Удаляет файл с именем 'file1.txt'

# 7. Переименование файла или директории
os.rename('old_name.txt', 'new_name.txt')  # Переименовывает 'old_name.txt' в 'new_name.txt'

# 8. Проверка существования файла или директории
exists = os.path.exists('file1.txt')
print(exists)  # Вывод: True, если файл существует, иначе False

# 9. Получение информации о файле или директории
info = os.stat('file1.txt')
print(info)  # Вывод: информация о файле в виде объекта os.stat_result

# 10. Создание вложенных директорий
os.makedirs('parent_directory/child_directory')  # Создает директорию 'parent_directory' и вложенную 'child_directory'

# 11. Удаление вложенных директорий
os.removedirs('parent_directory/child_directory')  # Удаляет директорию 'child_directory' и пустую 'parent_directory'

# 12. Выполнение системных команд
os.system('echo Hello, World!')  # Выполняет команду echo в системной оболочке

# 13. Получение значений переменных окружения
path = os.environ.get('PATH')
print(path)  # Вывод: значение переменной окружения PATH

# 14. Установка значений переменных окружения
os.environ['NEW_VAR'] = 'value'
print(os.environ['NEW_VAR'])  # Вывод: значение новой переменной окружения NEW_VAR

# 15. Разделение пути на директорию и файл
directory, filename = os.path.split('/path/to/file.txt')
print(directory)  # Вывод: /path/to
print(filename)  # Вывод: file.txt

# 16. Получение абсолютного пути
absolute_path = os.path.abspath('file.txt')
print(absolute_path)  # Вывод: абсолютный путь к 'file.txt'

# 17. Проверка, является ли путь файлом
is_file = os.path.isfile('file.txt')
print(is_file)  # Вывод: True, если путь является файлом, иначе False

# 18. Проверка, является ли путь директорией
is_directory = os.path.isdir('directory')
print(is_directory)  # Вывод: True, если путь является директорией, иначе False
