# Напишите класс, который переопределяет все методы сравнения (__eq__, __ne__, __lt__, __le__, __gt__, __ge__)
# для сравнения объектов по нескольким критериям: сначала по имени, затем по возрасту

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return (self.name, self.age) == (other.name, other.age)

    def __hash__(self):
        return hash((self.name, self.age))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return (self.name, self.age) < (other.name, other.age)

    def __le__(self, other):
        return (self.name, self.age) <= (other.name, other.age)

    def __gt__(self, other):
        return (self.name, self.age) > (other.name, other.age)

    def __ge__(self, other):
        return (self.name, self.age) >= (other.name, other.age)

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"


def main():
    p1 = Person("Alice", 30)
    p2 = Person("Bob", 25)
    p3 = Person("Alice", 25)
    print(p1 == p3)  # Output: False
    print(p1 != p2)  # Output: True
    print(p1 < p2)  # Output: True
    print(p1 <= p3)  # Output: False
    print(p1 > p2)  # Output: False
    print(p1 >= p3)  # Output: True

    # не работает без переопределения __hash__
    person_set = {p1, p2, p3}
    person_dict_employers = {p1: True, p2: False, p3: True}
    print(person_dict_employers)


if __name__ == "__main__":
    main()
