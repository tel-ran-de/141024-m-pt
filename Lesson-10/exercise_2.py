# Тема: Цикл for
#
# Упражнение 1: Подсчет гласных в строке
#
# Напишите программу, которая принимает строку от пользователя и подсчитывает количество гласных букв (a, e, i, o, u)
# в этой строке. Используйте цикл for и условие if.
user_string = input('Введите строку: ')
vowels_cnt = 0
for char in user_string:
    if char in 'aeuio':
        vowels_cnt = vowels_cnt + 1
print(vowels_cnt)

# Упражнение 2: Генерация и вывод последовательности чисел
#
# Напишите программу, которая генерит и выводит последовательность чисел от 1 до 20,
# но выводит "Fizz" вместо чисел, кратных 3, "Buzz" вместо чисел, кратных 5, и "FizzBuzz"
# вместо чисел, кратных как 3, так и 5. Используйте цикл for и функцию range.

for digit in range(1, 21):
    if digit % 3 == 0 and digit % 5 == 0:
        print('FizzBuzz')
    elif digit % 3 == 0:
        print('Fizz')
    elif digit % 5 == 0:
        print('Buzz')
    else:
        print(digit)