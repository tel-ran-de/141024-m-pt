# Атрибуты классов — это переменные, определенные внутри класса, но вне любых методов.
# Эти атрибуты являются общими для всех экземпляров (объектов) этого класса.
# Они принадлежат самому классу, а не конкретному объекту.

# Атрибуты объектов — это переменные, которые принадлежат конкретному экземпляру класса.
# Они определяются внутри методов, обычно внутри метода __init__,
# который является конструктором класса.

class Car:
    wheels = 4  # атрибут класса

    def __init__(self, color, model):
        self.color = color  # атрибут объекта
        self.model = model  # атрибут объекта


def main():
    # Создаем два объекта класса Car
    car1 = Car('red', 'Toyota')
    car2 = Car('blue', 'Honda')

    # Доступ к атрибутам объекта
    print(f'Доступ к атрибуту объекта car1.color: {car1.color}')  # Output: red
    print(f'Доступ к атрибуту объекта car1.model: {car1.model}')  # Output: Toyota
    print(f'Доступ к атрибуту объекта car1.wheels: {car1.wheels}')  # Output: 4
    print(f'Доступ к атрибуту объекта car2.color: {car2.color}')  # Output: blue
    print(f'Доступ к атрибуту объекта car2.model: {car2.model}')  # Output: Honda
    print(f'Доступ к атрибуту объекта car2.wheels: {car2.wheels}')  # Output: 4

    # Доступ к атрибуту класса
    print(f'Доступ к атрибуту класса Сar.wheels: {Car.wheels}')  # Output: 4

    Car.wheels = 6

    print(f'Доступ к атрибуту объекта car1.wheels: {car1.wheels}')  # Output: 6
    print(f'Доступ к атрибуту объекта car2.wheels: {car2.wheels}')  # Output: 6

    car1.wheels = 8

    print(f'Доступ к атрибуту объекта car1.wheels: {car1.wheels}')  # Output: 8
    print(f'Доступ к атрибуту объекта car2.wheels: {car2.wheels}')  # Output: 6


if __name__ == '__main__':
    main()
