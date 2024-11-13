# # Тема: map, filter, zip
#
# # Задача 1: Применение функции map для преобразования чисел
# # Напишите функцию `square`, которая принимает число и возвращает его квадрат.
# # Используйте функцию `map`, чтобы применить эту функцию к списку чисел `[1, 2, 3, 4, 5]` и выведите результат.
# #
numbers = [1, 2, 3, 4, 5]
# Ожидаемый результат: [1, 4, 9, 16, 25]
def square(x):
    return x * x
squared_numbers = map(square, numbers)
print(list(squared_numbers))

#
# # Задача 2: Применение функции filter для отбора четных чисел
# # Напишите функцию `is_even`, которая принимает число и возвращает `True`, если число четное,
# # и `False` в противном случае. Используйте функцию `filter`, чтобы отобрать четные числа из
# # списка `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` и выведите результат.
# #
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Ожидаемый результат: [2, 4, 6, 8, 10]
def is_even(x):
    return x % 2 ==0
even_numbers = filter(is_even,numbers)
print(list(even_numbers))
#
# # Задача 3: Применение функции zip для объединения списков
# # У вас есть два списка: `names = ["Alice", "Bob", "Charlie"]` и `ages = [25, 30, 35]`.
# # Используйте функцию `zip`, чтобы создать список кортежей, где каждый кортеж содержит имя и возраст,
# # и выведите результат.
# #
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
# Ожидаемый результат: [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
combi= zip(names,ages)


print(list(combi))
#
# # Задача 4: Применение функции map для преобразования строк в числа
# # Напишите функцию `to_int`, которая принимает строку и возвращает ее преобразование в целое число.
# # Используйте функцию `map`, чтобы применить эту функцию к списку строк `["1", "2", "3", "4", "5"]`
# # и выведите результат.
# #
str_numbers = ["1", "2", "3", "4", "5"]
# Ожидаемый результат: [1, 2, 3, 4, 5]
def to_int(x):
    return int(x)
int_num=map(to_int,str_numbers)
print(list(int_num))
#
#
# # Задача 5: Применение функции filter для отбора слов длиннее 3 символов
# # Напишите функцию `longer_than_three`, которая принимает строку и возвращает `True`,
# # если длина строки больше 3 символов, и `False` в противном случае. Используйте функцию `filter`,
# # чтобы отобрать слова длиной больше 3 символов из списка `["apple", "kiwi", "banana", "pear"]` и выведите результат.
# #
words = ["apple", "kiwi", "banana", "pear"]
# Ожидаемый результат: ["apple", "banana", "pear"]
def long_than_three(x):
     if len(x) > 4:
         return True
words_three= filter(long_than_three,words)
print(list(words_three))
#
#
#
#
#
# # Тема: map, filter, zip для итераторов, генераторов и файлов с лямбда функциями
#
# # Задача 1: Использование filter с генератором и лямбда функцией
# # Напишите генератор, который возвращает числа от 1 до 20.
# # Используйте функцию `filter` с лямбда функцией для отбора четных чисел и выведите результат.
# # Ожидаемый результат: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# number=(range(1,21))
# def gen_number():
#     for num in range(1,21):
#         yield num
#
# gen_num=filter(lambda x: x % 2 == 0, gen_number())
# print(list(gen_num))
#
#
# # Задача 2: Использование zip с итераторами и лямбда функцией
# # Создайте два итератора: один для чисел от 1 до 5, другой для их квадратов. Используйте функцию `zip`,
# # чтобы объединить эти итераторы в список кортежей, и примените лямбда функцию для их вывода
# # в формате строки "число: квадрат".
# # Ожидаемый результат: ['1: 1', '2: 4', '3: 9', '4: 16', '5: 25']
# numbers = iter(range(1, 6))
# squares = iter(map(lambda x: x * x, range(1, 6)))
#
# result = zip(numbers, squares)
# formatted_result = list(map(lambda x: f'{x[0]}: {x[1]}', result))
#
# print(formatted_result)
#
#
#
# # Задача 3: Использование map и filter с файлом и лямбда функцией
# # Напишите генератор, который читает строки из файла `example.txt`.
# # Используйте функцию `filter` с лямбда функцией, чтобы отобрать строки, содержащие слово "Python",
# # и затем примените функцию `map` с лямбда функцией для преобразования этих строк в верхний регистр.
def read_line(file_path):
    with open(file_path,"r")as file:
        for line in file:
            yield line.strip()
file_4=read_line("example.txt")
python_lines = filter(lambda x: "Python" in x, file_4)
upper_lines = map(lambda x: x.upper(), python_lines)
print(list(upper_lines))
#
#
# ## Тема: Дополнительная практика
#
# # Задача 1: Использование map с генератором и лямбда функцией для конвертации температур
# # Напишите генератор, который возвращает температуры в Цельсиях от -10 до 10.
# # Используйте функцию `map` с лямбда функцией для конвертации этих температур в Фаренгейты и выведите результат.
# # Ожидаемый результат: [14.0, 15.8, 17.6, 19.4, 21.2, 23.0, 24.8, 26.6, 28.4, 30.2,
# # 32.0, 33.8, 35.6, 37.4, 39.2, 41.0, 42.8, 44.6, 46.4, 48.2, 50.0]
# # °F = °C * 1,8 + 32
# def gen_celcium():
#     for value in range(-10,11):
#         yield value
# cel_faringeyt=map(lambda x:x*1.8+32,gen_celcium())
#
# print(list(cel_faringeyt))
#
#
# # Задача 2: Использование filter с итератором и лямбда функцией для фильтрации строк по длине
# # Создайте итератор для списка строк `["hello", "world", "python", "is", "awesome"]`.
# # Используйте функцию `filter` с лямбда функцией для отбора строк длиной более 5 символов и выведите результат.
# # Ожидаемый результат: ['python', 'awesome']
#
# linie_1= iter(["hello", "world", "python", "is", "awesome"])
# five_word=filter(lambda x:len(x)>5,linie_1)
# print(list(five_word))
# # Задача 3: Использование zip и map для объединения и форматирования данных из двух генераторов
# # Напишите два генератора: один для чисел от 1 до 3, другой для их кубов. Используйте функцию `zip`,
# # чтобы объединить эти генераторы в список кортежей, и примените функцию `map` с лямбда функцией
# # для вывода данных в формате строки "число: куб".
# # Ожидаемый результат: ['1: 1', '2: 8', '3: 27']
# # def num_gen_1():
# #     for i in range(1,4):
# #         yield i
# # def num_gen_2():
# #     for l in range(1,4):
# #         yiled l**3
#
# gen_num_1=(x for x in range(1,4))
# gen_num_2=(x**3 for x in range(1,4))
#
# gen_num_combi=zip(gen_num_1,gen_num_2)
# result=list(map(lambda x:f"{x[0]}:{x[1]}",gen_num_combi))
# print(result)
#
# # Задача 4: Использование filter и map с файлом для преобразования данных
# # Напишите генератор, который читает строки из файла `data.txt`.
# # Используйте функцию `filter` с лямбда функцией для отбора строк, содержащих числа.
# # Затем примените функцию `map` с лямбда функцией для преобразования этих строк в целые числа и выведите результат.
def read_line(file_path):
    with open(file_path,"r")as file:
        for line in file:
            yield line.strip()

file3_path=read_line("data.txt")
filter_string=filter(lambda x:x.isdigit(),file3_path)
numbers=map(lambda x: int(x), filter_string)
print(list(numbers))
#
#
#
# # Задача 5: Использование zip с итераторами для обработки данных из двух файлов
# # Создайте два генератора, которые читают строки из файлов `file1.txt` и `file2.txt`.
# # Используйте функцию `zip`, чтобы объединить данные из этих файлов, и примените лямбда функцию
# для вывода данных в формате "file1_line - file2_line".
def read_file(file_path):
    with open(file_path,"r")as file:
        for line in file:
            yield line.strip()
file1_path=read_file("file1.txt")
file2_path=read_file("file2.txt")
combined_lines = map(lambda x: f"{x[0]} - {x[1]}", zip(file1_path, file2_path))
print(list(combined_lines))
