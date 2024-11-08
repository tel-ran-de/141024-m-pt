### Тема: Рекурсия

# 1. Напишите функцию `is_palindrome(s)`, которая проверяет, является ли строка `s` палиндромом
# (порядок букв одинаковый при чтении слева направо и справа налево) с помощью рекурсии.
# Пример использования:
# print(is_palindrome("radar"))  # Вывод: True
# print(is_palindrome("hello"))  # Вывод: False


# 2. Напишите функцию `find_max(lst)`, которая возвращает максимальный элемент в списке `lst` с помощью рекурсии.
# Пример использования:
# print(find_max([1, 5, 3, 9, 2]))  # Вывод: 9
def find_max(lst):
    # Базовый случай: если список, состоит из одного элемента, то этот элемент максимальный
    if len(lst) == 1:
        return lst[0]
    else:
        max_of_rest = find_max(lst[1:])
        if lst[0] > max_of_rest:
            return lst[0]
        else:
            return max_of_rest

print(find_max([1, 17, 5, 3, 9, 2, 11]))  # Вывод: 17

# 3. Напишите функцию `find_min`, которая возвращает минимальный элемент в списке `lst` с помощью рекурсии.
# Пример использования:
# print(find_min([4, 2, 8, 1, 5]))  # Вывод: 1