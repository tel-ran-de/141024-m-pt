class X:
    def __init__(self):
        print("X")


class Y:
    def __init__(self):
        print("Y")

    def __str__(self):
        return "Y"


class Z:
    def __init__(self):
        print("Z")

    def __str__(self):
        return "Z"


class A(X, Y):
    def __init__(self):
        super().__init__()
        print("A")


class B(Y, Z):
    def __init__(self):
        super().__init__()
        print("B")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("C")
        print(self)


def main():
    # Тестирование
    c = C()
    print(C.__mro__)  # Method Resolution Order


if __name__ == "__main__":
    main()
