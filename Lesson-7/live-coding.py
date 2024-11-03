# конкатенация строк
print('конкатенация строк')
str1 = 'Hello'
str2 = 'World'
print(str1 + ' ' + str2 + '!')

# дублирование строк
print('дублирование строк')
str3 = "Hi!"
print(str3 * 8)

enter = '\n'
space = ' '
word = 'Python'
print(word * 3 + enter + word + space + word)

# индексация
print('положительная индексация')
hello_word = 'HELLO'
print(hello_word[0])
print(hello_word[1])
print(hello_word[2])
print(hello_word[3])
print(hello_word[4])
print('отрицательная индексация')
print(hello_word[-1])
print(hello_word[-2])
print(hello_word[-3])
print(hello_word[-4])
print(hello_word[-5])

# HELLO
# H [0] [-5]
# E [1] [-4]
# L [2] [-3]
# L [3] [-2]
# O [4] [-1]

# cрезы строки (str slice)
hello_py = 'Hello, Python!'
substring = hello_py[0:5]  # Hello
print(substring)

py_prog = 'Python Programming'
print(py_prog[7:19])  # Programming
print(py_prog[7:])  # Programming
print(py_prog[:6])  # Python

# методы строк
print('методы строк')
print(len('Python'))

# Приведение к нижнему и верхнему регистру
print()
print('Приведение к нижнему и верхнему регистру')
str1 = "Python is Awesome!"
print(str1.lower())  # "python is awesome!"
print(str1.upper())  # "PYTHON IS AWESOME!"

# Удаление пробелов
print()
print('Удаление пробелов')
str2 = "   Hello, World!   "
print(str2.strip())   # "Hello, World!"
print(str2.rstrip())  # "   Hello, World!"
print(str2.lstrip())  # "Hello, World!   "

# Замена, поиск и подсчет символов
print()
print('Замена, поиск и подсчет символов')
str3 = "Python is awesome!"
print(str3.replace('awesome', 'great'))  # "Python is great"
print(str3.find("is"))  # 7
print(str3.count("o"))  # 2

# Разделение и объединение строк
print()
print('Разделение и объединение строк')
str4 = "Python is awesome!"
words = str4.split(" ")
print(words)  # ["Python", "is", "awesome!"]
joined_str = " ".join(words)
print(joined_str)  # "Python is awesome!"
joined_str_dash = "-".join(words)
print(joined_str_dash)  # "Python-is-awesome!"
joined_str_asterisk = "*".join(words)
print(joined_str_asterisk)  # "Python*is*awesome!"

# Дополнительные методы
print()
print('Дополнительные методы')
str5 = "python is awesome!"
print(str5.capitalize())          # "Python is awesome!"
print(str5.title())               # "Python Is Awesome!"
print(str5.upper())               # "PYTHON IS AWESOME!"
print(str5.lower())               # "python is awesome!"
print(str5.title().swapcase())    # "Python Is Awesome!" -> "pYTHON iS aWESOME!"

# спецсимволы и экранирование
print()
print('спецсимволы и экранирование')
print('Hello\nworld!')
print('Hello\tworld!')
# обратный слэш
print('This is a backslash: \\')
# Вывод:
# This is a backslash: \

# Одинарная кавычка: \'
print('It\'s a beautiful day')
# Вывод:
# It's a beautiful day

# Двойная кавычка: \"
print("She said, \"Hello, World!\"")
# Вывод:
# She said, "Hello, World!"

# Форматирование строк: F-строки
print()
print('Форматирование строк: F-строки')
course = 'Python'
level = 'beginner'
description = f'This is a course {course} for {level}.'
print(description)

name = 'Kurt'
age = 27
greeting = f'My name is {name} and I am {age} years old.'
print(greeting)

# Форматирование строк: метод format()
print()
print('Форматирование строк: метод format()')
course = 'Python'
level = 'beginner'
description = 'This is a course {} for {}.'.format(course, level)
print(description)

name = 'Kurt'
age = 27
greeting = 'My name is {} and I am {} years old.'.format(name, age)
print(greeting)

print()
username = input('Введите имя: ')
age = int(input('Введите возраст: '))
birthdate = 2024 - age
print(f'Привет, {username}. Ты родился в {birthdate} году.')
