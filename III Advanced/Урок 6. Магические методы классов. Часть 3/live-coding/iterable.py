import random


class IterableClass:
    def __init__(self, values):
        self.values = values

    def __iter__(self):
        return IterableClassIterator(self.values)

    def reversed(self):
        return ReverseIterableClassIterator(self.values)

    def even_iter(self):
        return EvenIterableClassIterator(self.values)

    def odd_iter(self):
        return OddIterableClassIterator(self.values)

    def random_iter(self):
        return RandomIterableClassIterator(self.values)


class IterableClassIterator:
    def __init__(self, values):
        self.values = values
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.values):
            raise StopIteration
        value = self.values[self.index]
        self.index += 1
        return value


class ReverseIterableClassIterator:
    def __init__(self, values):
        self.values = values
        self.index = len(values) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.values[self.index]
        self.index -= 1
        return value


class EvenIterableClassIterator:
    def __init__(self, values):
        self.values = values
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.values):
            value = self.values[self.index]
            self.index += 1
            if value % 2 == 0:
                return value
        raise StopIteration


class OddIterableClassIterator:
    def __init__(self, values):
        self.values = values
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.values):
            value = self.values[self.index]
            self.index += 1
            if value % 2 != 0:
                return value
        raise StopIteration


class RandomIterableClassIterator:
    def __init__(self, values):
        self.values = values
        self.index = 0
        self.shuffled_values = random.sample(values, len(values))

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.shuffled_values):
            raise StopIteration
        value = self.shuffled_values[self.index]
        self.index += 1
        return value


def main():
    # Тестирование
    iterable = IterableClass([10, 21, 30, 45, 50, 63])

    print("Forward iteration:")
    for value in iterable:
        print(value)  # Output: 10 21 30 45 50 63

    print("Reverse iteration:")
    for value in iterable.reversed():
        print(value)  # Output: 63 50 45 30 21 10

    print("Even iteration:")
    for value in iterable.even_iter():
        print(value)  # Output: 10 30 50

    print("Odd iteration:")
    for value in iterable.odd_iter():
        print(value)  # Output: 21 45 63

    print("Random iteration:")
    for value in iterable.random_iter():
        print(value)  # Output: в случайном порядке


if __name__ == '__main__':
    main()
