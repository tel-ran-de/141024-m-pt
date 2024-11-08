# Открытие файла
file_r = open("example.txt") # Режим чтения по умолчанию

file_r = open("example.txt", "r")  # Явно указанный режим чтения

file_w = open("example.txt", "w")  # Запись данных

file_a = open("example.txt", "a")  # Добавление данных

file_rp = open("example.txt", "r+")  # Чтение и запись

file_ap = open("example.txt", "a+")  # Добавление данных и чтение


# Чтение файла

file = open("example.txt", "r")

content = file.read()  # Читает весь файл целиком

partial_content = file.read(5)  # Читает первые 5 символов

one_line = file.readline()  # Читает первую строку

all_lines = file.readlines()  # Читает все строки и возвращает список строк

file.close() # В конце нужно всегда закрывать файл




file = open("text_files/example.txt", "r")

# Пример текста в файле: "Hello, World!\nWelcome to file handling in Python."

# Чтение первых 5 символов
content = file.read(5)  # "Hello"
position1 = file.tell()  # 5
print(content, position1)

# Чтение следующих 7 символов
content = file.read(7)  # ", World"
position2 = file.tell()  # 12
print(content, position2)


# Чтение одной строки (остальной части строки после "Hello, World!")
content = file.readline()  # "!\n"
position3 = file.tell()  # 14
print(content, position3)


# Чтение следующей строки
content = file.readline()  # "Welcome to file handling in Python."
position4 = file.tell()  # 47
print(content, position4)

file.close()


# Добавление данных

# Метод write(): Запись строки в конец файла
file_a.write("Appending this line.\n")

# Метод writelines(): Запись списка строк в конец файла
lines_to_append = ["Line 1\n", "Line 2\n", "Line 3\n"]
file_a.writelines(lines_to_append)

file_a.close()

# Открытие файла для чтения в бинарном режиме
file = open("example.bin", "rb")

# Открытие файла для записи в бинарном режиме
file = open("example.bin", "wb")


# Работе с указателем

file = open("example.txt", "r")
file.read(5)
print(file.tell())  # текущая позиция указателя (5)

file.seek(0)  # перемещение указателя в начало файла
print(file.tell())  # проверка позиции указателя (0)

file.seek(10)  # перемещение указателя на 10 символов вперед
print(file.tell())  # проверка позиции указателя (10)

file.close()


# Работе с JSON

import json

data = {
    "name": "John",
    "age": 30
}

# Запись в файл
with open("data.json", "w") as file:
    json.dump(data, file)

# Преобразование в строку JSON
json_string = json.dumps(data)

# Преобразование строки JSON в объект Python
json_string = '{"name": "John", "age": 30}'
data = json.loads(json_string)

# Чтение из файла
with open("data.json", "r") as file:
    data = json.load(file)
