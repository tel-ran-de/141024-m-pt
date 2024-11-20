# Абстракция
from abc import ABC, abstractmethod


class Animal(ABC):
    legs = 4

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def run(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"

    def run(self):
        return "Dog is running"


class Cat(Animal):
    def speak(self):
        return "Meow!"

    def run(self):
        return "Cat is running"


def make_animal_speak(animal):
    print(animal.speak())


def main():
    print('Abstraction')
    dog = Dog()
    cat = Cat()

    make_animal_speak(dog)
    make_animal_speak(cat)

    print(dog.legs)
    print(cat.legs)


if __name__ == "__main__":
    main()