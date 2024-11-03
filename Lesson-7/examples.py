# Конкатенация строк
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2  # "Hello World"

str3 = "Python"
str4 = "Rocks"
result2 = str3 + " " + str4  # "Python Rocks"

# Дублирование строк
str1 = "Hello"
result = str1 * 3  # "HelloHelloHello"

str2 = "Python"
result2 = str2 * 2  # "PythonPython"

# Live-coding преподавателя: Конкатенация и дублирование строк
str1 = "Hello"
str2 = "Python"
result = str1 + " " + str2
print(result)  # "Hello Python"

repeat = str1 * 2
print(repeat)  # "HelloHello"

str3 = "Coding"
str4 = "is fun"
result3 = str3 + " " + str4
print(result3)  # "Coding is fun"

repeat2 = str4 * 3
print(repeat2)  # "is funis funis fun"

# Индексация строк
str1 = "Hello"
first_char = str1[0]  # "H"
last_char = str1[-1]  # "o"

str2 = "World"
second_char = str2[1]  # "o"
second_last_char = str2[-2]  # "l"

# Срезы строк
str1 = "Hello, World!"
substring = str1[0:5]  # "Hello"

str2 = "Python Programming"
substring2 = str2[7:18]  # "Programming"

# Live-coding преподавателя: Индексация и срезы строк
str1 = "Hello, World!"
first_char = str1[0]
last_char = str1[-1]
substring = str1[7:]

print(first_char)  # "H"
print(last_char)  # "!"
print(substring)  # "World!"

str2 = "Python Programming"
third_char = str2[2]
fourth_last_char = str2[-4]
substring2 = str2[:6]

print(third_char)  # "t"
print(fourth_last_char)  # "m"
print(substring2)  # "Python"


# Методы строк
# Приведение к нижнему и верхнему регистру
str1 = "Python is Awesome!"
print(str1.lower())  # "python is awesome!"
print(str1.upper())  # "PYTHON IS AWESOME!"

# Удаление пробелов
str2 = "   Hello, World!   "
print(str2.strip())   # "Hello, World!"
print(str2.rstrip())  # "   Hello, World!"
print(str2.lstrip())  # "Hello, World!   "

# Замена, поиск и подсчет символов
str3 = "Python is awesome!"
print(str3.replace("awesome", "great"))  # "Python is great"
print(str3.find("is"))  # 7
print(str3.count("o"))  # 1

# Разделение и объединение строк
str4 = "Python is awesome!"
words = str4.split(" ")
print(words)  # ["Python", "is", "awesome!"]
joined_str = " ".join(words)
print(joined_str)  # "Python is awesome!"

# Дополнительные методы
str5 = "python is awesome!"
print(str5.capitalize())  # "Python is awesome!"
print(str5.title())       # "Python Is Awesome!"


# Live-coding преподавателя: Методы строк
str1 = "Hello, World!"
upper_str = str1.upper()
found_index = str1.find("World")
replaced_str = str1.replace("World", "Python")

print(upper_str)  # "HELLO, WORLD!"
print(found_index)  # 7
print(replaced_str)  # "Hello, Python!"

str2 = "Python Programming"
title_str = str2.title()
count_o = str2.count("o")
split_str = str2.split(" ")

print(title_str)  # "Python Programming"
print(count_o)  # 2
print(split_str)  # ["Python", "Programming"]

# Длина строки: len()
str1 = "Hello"
length = len(str1)  # 5
str2 = "Привет"
length2 = len(str2)  # 6

str3 = "Python"
length3 = len(str3)  # 6
str4 = "Длина строки"
length4 = len(str4)  # 12

# Live-coding преподавателя: Длина строки
str1 = "Hello"
str2 = "Hello, World!"
str3 = " "
str4 = "OpenAI GPT-4"

print(len(str1))  # 5
print(len(str2))  # 13
print(len(str3))  # 1
print(len(str4))  # 12

# Спецсимволы и экранирование
# Новая строка: \n
print("Hello\nWorld")
# Вывод:
# Hello
# World

# Табуляция: \t
print("Hello\tWorld")
# Вывод:
# Hello   World

# Обратный слэш: \\
print("This is a backslash: \\")
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


# Live-coding преподавателя: Спецсимволы и экранирование
str1 = "Hello\nWorld"
str2 = "Hello\tWorld"
str3 = "This is a backslash: \\"
str4 = "Hello\rWorld"
str5 = "She said, \"Hello!\""

print(str1)
print(str2)
print(str3)
print(str4)
print(str5)

# Форматирование строк: метод format()
name = "John"
age = 30
greeting = "My name is {} and I am {} years old".format(name, age)  # "My name is John and I am 30 years old"

course = "Python"
level = "beginner"
description = "This is a {} course for {} learners.".format(course, level)  # "This is a Python course for beginner learners."

# Форматирование строк: F-строки
name = "John"
age = 30
greeting = f"My name is {name} and I am {age} years old"  # "My name is John and I am 30 years old"

course = "Python"
level = "beginner"
description = f"This is a {course} course for {level} learners."  # "This is a Python course for beginner learners."

# Live-coding преподавателя: Форматирование строк и F-строки
name = "Alice"
age = 28

formatted_str1 = "My name is {} and I am {} years old".format(name, age)
formatted_str2 = f"My name is {name} and I am {age} years old"

print(formatted_str1)  # "My name is Alice and I am 28 years old"
print(formatted_str2)  # "My name is Alice and I am 28 years old"

course = "Data Science"
duration = "3 months"
formatted_str3 = "The {} course lasts for {}.".format(course, duration)
formatted_str4 = f"The {course} course lasts for {duration}."

print(formatted_str3)  # "The Data Science course lasts for 3 months."
print(formatted_str4)  # "The Data Science course lasts for 3 months."