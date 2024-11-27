class CustomList:
    def __init__(self, items):
        if all(isinstance(item, int) for item in items):
            self.items = items
        else:
            raise ValueError("All items must be integers")

    # срабатывает при обращении к индексу
    def __getitem__(self, index):
        return self.items[index]

    # срабатывает при изменении индекса
    def __setitem__(self, index, value):
        self.items[index] = value

    # срабатывает при удалении индекса
    def __delitem__(self, index):
        del self.items[index]

    # срабатывает при вызове функции len()
    def __len__(self):
        return len(self.items)

    # срабатывает при вызове функции print()
    def __str__(self):
        return str(self.items)

    # срабатывает при вызове оператора +
    def __add__(self, other):
        if isinstance(other, int):
            new_items = self.items + [other]
            return CustomList(new_items)
        elif isinstance(other, CustomList):
            new_items = [i + j for i, j in zip(self.items, other.items)]
            return CustomList(new_items)
        return NotImplemented

    # срабатывает при старте итератора (например цикл for)
    def __iter__(self):
        return iter(self.items[::-1])

    # срабатывает при прохождении каждого шага итератора
    def __next__(self):
        return next(self.items)

    def append(self, item):
        if not isinstance(item, int):
            raise ValueError("All items must be integers")
        self.items.append(item)


# Тестирование
cl = CustomList([1, 2, 3, 4, 5])
print(cl[0])  # Output: 1
print(cl[2])  # Output: 3

cl[1] = 0
print(cl)  # Output: [1, 0, 3, 4, 5]

del cl[4]
print(cl)  # Output: [1, 3, 4, 5]

cl.append(6)
print(cl)  # Output: [1, 3, 4, 5, 6]

print(len(cl))  # Output: 5

cl = cl + 10 + 11
print(cl)

cl2 = CustomList([2, 3, 4, 5, 1, 2, 3])

cl3 = cl + cl2

print(cl)
print(cl2)
print(cl3)
# cl2 = CustomList([1, 'a', True])  # ValueError: All items must be integers

print()
print(cl3)
for i in cl3:
    print(i)
print(cl3)
