import timeit


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1


class Point2:
    __slots__ = ['x', 'y']

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1


class Point3(Point2):
    __slots__ = ['z']

    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z


def main():
    p = Point(10, 20)
    p2 = Point2(10, 20)

    print(f'Memory allocation for object Point: {p.__sizeof__() + p.__dict__.__sizeof__()} b')
    print(f'Memory allocation for object Point2: {p2.__sizeof__()} b')

    t1 = timeit.timeit(p.calc)
    t2 = timeit.timeit(p2.calc)

    print(f'Time for operation in object Point: {t1}')
    print(f'Time for operation in object Point2: {t2}')
    print(f'Point2 is {((t1 / t2) - 1)*100 :.2f}% faster')

    print(p.__dict__)
    p.z = 1000
    print(p.__dict__)

    # print(p2.__dict__)  # AttributeError: 'Point2' object has no attribute '__dict__'
    # p2.z = 1000  # AttributeError: 'Point2' object has no attribute 'z'

    p3 = Point3(10, 20, 30)
    # print(p3.__dict__)  # AttributeError: 'Point3' object has no attribute '__dict__'.
    print(p3.z)
    print(p3.y)
    print(p3.x)
    print(p3.__slots__)
    print(p2.__slots__)


if __name__ == '__main__':
    main()
