# Темы: Спецсимволы и экранирование символов, Форматирование строк и F-строки
# Результат по каждому заданию необходимо выводить в консоль через print().

# 1. Вставьте символ новой строки в строку "Hello World".
# Ожидаемый результат:
# Hello
# World


# 2. Вставьте символ обратного слэша в строку "This is a backslash: ".
# Ожидаемый результат: "This is a backslash: \"


# 3. Экранируйте кавычки в строке "He said, "Hello!"".
# Ожидаемый результат: He said, "Hello!"


# 4. Экранируйте одинарные кавычки в строке "It's a sunny day".
# Ожидаемый результат: It's a sunny day


# 5. Вставьте символ новой строки в строку "Python Programming".
# Ожидаемый результат:
# Python
# Programming


# 6. Экранируйте кавычки в строке "She said, 'Hi!'".
# Ожидаемый результат: She said, 'Hi!'


# 7. Экранируйте обратный слэш в строке "Path to file: C:\\".
# Ожидаемый результат: Path to file: C:\\


# 8. Используйте метод `format()` для строки "This is a ... course for ... learners." с переменными course="Python"
# и level="beginner". Ожидаемый результат: "This is a Python course for beginner learners."


# 9. Используйте F-строку для строки "This is a ... course for ... learners." с переменными
# course="Python" и level="beginner". Ожидаемый результат: "This is a Python course for beginner learners."


# 10. Используйте метод `format()` для строки "Welcome to the ... workshop." с переменной topic="Machine Learning".
# Ожидаемый результат: "Welcome to the Machine Learning workshop."


# 11. Используйте F-строку для строки "Welcome to the ... workshop." с переменной topic="Machine Learning".
# Ожидаемый результат: "Welcome to the Machine Learning workshop."


# 12. Придумайте название переменной и поместите в нее строку "machine learning",
# затем преобразуйте первые буквы слов в заглавный регистр, чтобы получилось "Machine Learning".
# Затем создайте переменную со строкой "Course: ". Используйте метод `format()`, чтобы показать в консоле
# "Course: Machine Learning"


# 13. Объедините строки "Data" и "Science" с пробелом между ними, дублируйте результат три раза, и используйте F-строку
# для строки "Field: ...". Ожидаемый результат: "Field: Data ScienceData ScienceData Science"


# 14. Выведите третий символ строки "Information", затем используйте метод `format()` для строки "Third character: ...".
# Ожидаемый результат: "Third character: f"


# 15. Определите длину строки "Neural Networks", умножьте её на 2, и используйте F-строку для строки "Length: ".
# Ожидаемый результат: "Length: 28"


# 16. Преобразуйте строку "Deep Learning" в заглавный регистр, найдите индекс подстроки "LEARNING", и выведите символ
# на этом индексе. Ожидаемый результат: "L"


# 20. Определите длину строки "Starta", затем преобразуйте её в строку и добавьте к строке " has length of ",
# используя метод `format()`. Ожидаемый результат: "Starta has length of 6"

name = "Starta"
lange = len(name)
print(lange)
part2 = "has length of"
print(name + " " + "{}".format(part2) + " " + str(lange))
print("{} {} {}".format(name, part2, lange))
print(f'{name} {part2} {lange}')

test = "{}".format(lange)
print("Переменная test: ", type(test))

print(6)
print('6')
print(type(6))
print(type('6'))
