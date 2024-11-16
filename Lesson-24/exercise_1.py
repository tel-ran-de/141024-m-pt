# Тема: Модуль datetime
from datetime import datetime

# Задача 1: Определение текущей даты и времени
# Напишите программу, которая выводит текущие дату и время в формате "YYYY-MM-DD HH:MM:SS".
# Пример: 2024-06-11 14:35:45


# Задача 2: Вычисление возраста
# Напишите программу, которая принимает дату рождения пользователя в формате "YYYY-MM-DD" и вычисляет его возраст.

# # Функция для вычисления возраста
# def calculate_age(birth_date):
#     birth_date = datetime.strptime(birth_date, "%d.%m.%Y")
#     today = datetime.today()
#     result = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
#     return result
#
#
# # Пример использования
# bd = input("Введите дату рождения в формате DD.MM.YYYY: ")
# age = calculate_age(bd)
# print(f"Ваш возраст: {age} лет")


# Задача 3: Расчет дней до следующего мероприятия
# Напишите программу, которая принимает дату следующего мероприятия в формате "YYYY-MM-DD" и выводит количество дней,
# оставшихся до этой даты.

# Функция для расчёта дней до мероприятия
def days_until_event(event_date):
    event_date = datetime.strptime(event_date, "%d.%m.%Y")
    return (event_date - datetime.today()).days


# Пример использования
days_left = days_until_event(input("Введите дату мероприятия в формате DD.MM.YYYY: "))
print(f"До мероприятия осталось {days_left} дней")

# Задача 4: Определение дня недели
# Напишите программу, которая принимает дату в формате "YYYY-MM-DD" и выводит день недели для этой даты.


# Задача 5: Сравнение двух дат
# Напишите программу, которая принимает две даты в формате "YYYY-MM-DD" и определяет, какая из них позже.
