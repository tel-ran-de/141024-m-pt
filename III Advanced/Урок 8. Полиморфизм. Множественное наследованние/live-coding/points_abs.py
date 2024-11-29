import timeit
from abc import ABC, abstractmethod


class Point(ABC):
    __slots__ = ['x', 'y']

    @abstractmethod
    def __init__(self, x, y):
        pass

    @abstractmethod
    def calc(self):
        pass


class Point2(Point):
    __slots__ = ['x', 'y']

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1


def main():
    p2 = Point2(10, 20)

    print(f'Memory allocation for object Point2: {p2.__sizeof__()} b')

    t2 = timeit.timeit(p2.calc)

    # print(p2.__dict__)  # AttributeError: 'Point2' object has no attribute '__dict__'
    # p2.z = 1000  # AttributeError: 'Point2' object has no attribute 'z'




if __name__ == '__main__':
    main()
