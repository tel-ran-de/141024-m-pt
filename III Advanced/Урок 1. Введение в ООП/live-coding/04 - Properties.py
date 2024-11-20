# Свойства (Properties)
# Python предоставляет более удобный способ использования геттеров и сеттеров с помощью декоратора property.
# Он позволяет определять геттеры, сеттеры и методы удаления для атрибутов класса в виде свойств.

class Car:
    def __init__(self, model, year):
        self.__model = model  # Приватный атрибут
        self.__year = year    # Приватный атрибут

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if isinstance(model, str):
            self.__model = model
        else:
            raise ValueError("Model must be a string")

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if year > 1885:
            self.__year = year
        else:
            raise ValueError("Year must be greater than 1885")


def main():
    # Приватные атрибуты через property
    car = Car(model="Toyota", year=2019)
    print(f'Доступ к приватному атрибуту car.model: {car.model}')  # Доступ к приватному атрибуту через property
    car.year = 2021  # Изменение приватного атрибута через property
    print(f'Доступ к приватному атрибуту car.year: {car.year}')  # Output: 2021

    # car.year = 1880  # ValueError: Year must be greater than 1885
    car.year = 2024
    print(f'Доступ к приватному атрибуту car.year: {car.year}')  # Output: 2024


if __name__ == "__main__":
    main()
