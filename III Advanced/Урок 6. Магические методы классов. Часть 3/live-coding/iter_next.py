class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        current = self.current
        self.current += 1
        return current


# Тестирование
my_range = MyRange(1, 5)
for num in my_range:
    print(num)  # Output: 1 2 3 4 5