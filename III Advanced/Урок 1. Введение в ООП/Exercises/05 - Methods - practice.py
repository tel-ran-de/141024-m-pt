# Ex 1
# Создайте класс `Temperature` с методами для преобразования температуры из градусов Цельсия в Фаренгейты и Кельвины.
# Реализуйте методы как статические.

class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32

    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15

<<<<<<< HEAD
if __name__ == '__main__':
    # Пример использования класса Temperature
    celsius = 25
    print(f"{celsius}°C = {Temperature.celsius_to_fahrenheit(celsius)}°F")
    print(f"{celsius}°C = {Temperature.celsius_to_kelvin(celsius)}K")
=======
>>>>>>> 18af0241bd7aced7e5c37ce4b91c305fa9274a1a
# #### Задание 2:
# Создайте класс `Counter` с атрибутом класса `count`,
# который будет отслеживать количество созданных экземпляров класса.
# Реализуйте метод класса `get_count`, который возвращает текущее значение `count`.

<<<<<<< HEAD
class Counter:
    count = 0
    def __init__(self):
        self.count += 1

a = Counter()
b = Counter()
print(Counter.count)





=======

if __name__ == '__main__':
    # Пример использования класса Temperature
    celsius = 25
    print(f"{celsius}°C = {Temperature.celsius_to_fahrenheit(celsius)}°F")
    print(f"{celsius}°C = {Temperature.celsius_to_kelvin(celsius)}K")
>>>>>>> 18af0241bd7aced7e5c37ce4b91c305fa9274a1a
