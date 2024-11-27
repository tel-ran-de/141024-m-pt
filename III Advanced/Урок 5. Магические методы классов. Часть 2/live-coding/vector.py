class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # addition
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x + other, self.y + other)
        return NotImplemented

    # subtraction
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x - other, self.y - other)
        return NotImplemented

    # multiplication
    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented

    # true division
    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x / scalar, self.y / scalar)
        return NotImplemented

    # equal
    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False

    # not equal
    def __ne__(self, other):
        # if isinstance(other, Vector):
        #     return self.x != other.x and self.y != other.y
        # return False
        return not self.__eq__(other)

    # less than
    def __lt__(self, other):
        if isinstance(other, Vector):
            return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)
        return NotImplemented

    # less or equal
    def __le__(self, other):
        if isinstance(other, Vector):
            return (self.x**2 + self.y**2) <= (other.x**2 + other.y**2)
        return NotImplemented

    # greater than
    def __gt__(self, other):
        if isinstance(other, Vector):
            return (self.x**2 + self.y**2) > (other.x**2 + other.y**2)
        return NotImplemented

    # greater or equal
    def __ge__(self, other):
        if isinstance(other, Vector):
            return (self.x**2 + self.y**2) >= (other.x**2 + other.y**2)
        return NotImplemented

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


def main():
    # Примеры использования
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = Vector(1, 2)

    # Арифметические операции
    print(v1 + v2)  # Output: Vector(4, 6)
    print(v1 - v2)  # Output: Vector(-2, -2)
    print(v1 * 3)  # Output: Vector(3, 6)
    print(v1 / 2)  # Output: Vector(0.5, 1.0)
    print(v1 + 10)  # Output: Vector(11, 12)
    print(v1 - 2)  # Output: Vector(-1, 0)

    print()
    # Сравнения
    print(v1 == v2)  # Output: False
    print(v1 == v3)  # Output: True
    print(v1 != v2)  # Output: True
    print(v1 < v2)  # Output: True (сравнение по длине вектора)
    print(v1 <= v2)  # Output: True (сравнение по длине вектора)
    print(v1 > v2)  # Output: False (сравнение по длине вектора)
    print(v1 >= v2)  # Output: False (сравнение по длине вектора)


if __name__ == "__main__":
    main()
