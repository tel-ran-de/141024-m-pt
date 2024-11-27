class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # должен возвращать True или False
    def __bool__(self):
        return self.x != 0 or self.y != 0

    # должен возвращать str
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    # должен возвращать str
    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v = Vector(0, 0)
print(bool(v))

v2 = Vector(1, 1)
print(bool(v2))

if v2:
    print('Вектор не нулевой')