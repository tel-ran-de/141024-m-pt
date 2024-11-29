from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Cow(Animal):
    def speak(self):
        return "Moo!"


def main():
    # Тестирование
    animals = [Dog(), Cat(), Cat(), Cat(), Cat(), Dog(), Cow()]

    for animal in animals:
        print(animal.speak())

    # Попытка создания экземпляра абстрактного класса вызывает ошибку
    # animal = Animal()  # Raises TypeError


if __name__ == '__main__':
    main()
