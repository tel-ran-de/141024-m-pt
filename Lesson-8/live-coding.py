# операторы сравнения
print('операторы сравнения')
print('сравнение чисел')
a = 5
b = 30
print(a == b)  # False
print(a != b)  # True
print(a > b)  # False
print(a < b)  # True
print(a >= b)  # False
print(a <= b)  # True

print()
print('сравнение строк')
print('Q' > 'F')  # True
print('J' < 'D')  # False
print('R' == 'r')  # False

print('A' == 'А')  # первая латинская, вторая кириллическая
print('A' < 'А')
print('e' > '2')

print('вода' > 'водяной')  # False, потому что "а" стоит раньше, чем "я"
print('лак' < 'лакировщик')  # True
print('лак' < 'лакировщик водяного')  # True

print('Apple' != 'apple')  # True
print('Apple' < 'apple')  # True

# условные операторы if и if-else
print()
print('условные операторы if и if-else')
a = 5
if a > 0:  # в первой строке задаётся условие
    print('a больше нуля')  # блок кода, который выполняется, если условие ИСТИННО
else:  # не обязателен, выполняется в случае, если условие ложное
    print('a не больше нуля')


# вложенные условия
# print('вложенные условия')
# x = int(input('Введите число: '))
# if x > 0:
#     if x % 2 == 0:
#         print(f'{x} число положительное и чётное')
#     else:
#         print(f'{x} число положительное и нечётное')
# else:
#     print(f'Число {x} не положительное.')

# Множественный выбор: if-elif-else
# print('Множественный выбор: if-elif-else')
# a = 0
# if a > 0:
#     print("a положительное")
# elif a < 0:  # elif дополнительное условие, оно не обязательно и их может быть неограниченное количество
#     print("a отрицательное")
# else:
#     print("a равно нулю")
#
# print('Перевод 100-балльной оценки в 5-балльную')
# grade = int(input('Введите оценку: '))
# if grade >= 80:
#     print('5!')
# elif grade >= 60:
#     print('4!')
# elif grade >= 40:
#     print('3!')
# elif grade >= 20:
#     print('2!')
# else:
#     print('1!')

# print()
# print('Тернарный оператор')
# x = int(input('Введите число: '))
# if x > 0:
#     y = 'Положительное'
# else:
#     y = 'Не положительное'
# y = 'Положительное' if x > 0 else 'Не положительное'
# y = 'Положительное' if x > 0 else ('Отрицательное' if x < 0 else 'Ноль')
# print(y)

# логический операторы: and, or, not
print('логический операторы: and, or, not')
# is_raining = bool(int(input('Введите\n1 если дождь или\n0 если не дождь: ')))
# temp = float(input('Введите температуру: '))
# if is_raining or temp < 18:
#     print('Не выходи из комнаты')
# else:
#     print('Пора гулять!')

x = int(input('Введите число: '))
if x == 0:
    print('Это ноль')
elif x > 0 and x % 2 == 0:
    print('Положительное чётное число')
elif x < 0 and x % 2 == 0:
    print('Отрицательное чётное число')
elif x > 0 and not x % 2 == 0:
    print('Положительное нечётное число')
else:
    print('Отрицательное нечётное число')

