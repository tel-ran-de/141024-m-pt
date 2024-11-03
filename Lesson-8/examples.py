
# Сравнение на равенство
print("apple" == "apple")  # True
print("apple" == "Apple")  # False

# Сравнение на неравенство
print("apple" != "banana")  # True

# Лексикографическое сравнение
print("apple" < "banana")   # True (поскольку 'a' < 'b')
print("apple" > "banana")   # False

# Сравнение с учетом длины строк
print("app" < "apple")      # True (поскольку "app" короче "apple")

# Сравнение с учетом регистра
print("Apple" < "apple")    # True (поскольку 'A' < 'a' в кодировке Unicode)


# Примеры булевых значений
is_raining = True
is_sunny = False

# Булевые значения могут быть результатом операций сравнения
a = 10
b = 20
print(a < b)  # True
print(a == b) # False

# Операторы сравнения (сравнение чисел)
a = 5
b = 10
print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= b)  # False
print(a <= b)  # True

# Операторы сравнения (сравнение строк)
str1 = "apple"
str2 = "banana"
print(str1 == str2)  # False
print(str1 != str2)  # True
print(str1 > str2)   # False
print(str1 < str2)   # True

# Live-coding преподавателя (булевые переменные и операторы сравнения)
x = 7
y = 14
print(x == y)  # False
print(x != y)  # True
print(x > y)   # False
print(x < y)   # True
print(x >= y)  # False
print(x <= y)  # True

str1 = "hello"
str2 = "world"
print(str1 == str2)  # False
print(str1 != str2)  # True
print(str1 > str2)   # False
print(str1 < str2)   # True

# Условный оператор if
a = 5
if a > 0:
    print("a больше нуля")

# Конструкция if-else
a = -3
if a > 0:
    print("a больше нуля")
else:
    print("a не больше нуля")

# Live-coding преподавателя (условные операторы if и if-else)
num = 10
if num % 2 == 0:
    print("Число четное")
else:
    print("Число нечетное")

# Вложенные условия
a = 15
if a > 0:
    if a % 2 == 0:
        print("a положительное и четное")
    else:
        print("a положительное и нечетное")
else:
    print("a не положительное")

# Множественный выбор: if-elif-else
a = 0
if a > 0:
    print("a положительное")
elif a < 0:
    print("a отрицательное")
else:
    print("a равно нулю")

# Live-coding преподавателя (вложенные условия и конструкция if-elif-else)
score = 85
if score >= 90:
    print("Отлично")
elif score >= 75:
    print("Хорошо")
elif score >= 50:
    print("Удовлетворительно")
else:
    print("Неудовлетворительно")

# Тернарный условный оператор
a = 5
result = "Положительное" if a > 0 else "Неположительное"
print(result)

# Live-coding преподавателя (тернарный условный оператор)
num = 7
parity = "четное" if num % 2 == 0 else "нечетное"
print(parity)  # нечетное

temperature = -5
weather = "тепло" if temperature > 0 else "холодно"
print(weather)  # холодно


