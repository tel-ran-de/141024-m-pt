
# Упаковка аргументов с *args
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))  # Вывод: 10


# Распаковка значений из кортежа
numbers = (1, 2, 3)
print(*numbers)  # Вывод: 1 2 3


# Распаковка значений с помощью *args
def print_args(*args):
    for arg in args:
        print(arg)

values = [1, 2, 3]
print_args(*values)  # Вывод: 1 2 3


# Упаковка именованных аргументов с **kwargs
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="Alice", age=30)
# Вывод:
# name: Alice
# age: 30


# Распаковка словаря с помощью **
data = {"name": "Bob", "age": 25}
print_info = lambda name, age: f"Name: {name}, Age: {age}"
print(print_info(**data))
# Вывод: Name: Bob, Age: 25


# Использование ключевого слова global
counter = 0

def increment_global():
    global counter
    counter += 1

increment_global()
print(counter)  # Вывод: 1
increment_global()
print(counter)  # Вывод: 2


# Использование ключевого слова nonlocal
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner

counter1 = outer()
print(counter1())  # Вывод: 1
print(counter1())  # Вывод: 2


# Замыкание для создания функции умножения
def make_multiplier(factor):
    def multiplier(number):
        return number * factor
    return multiplier

mult_by_2 = make_multiplier(2)
print(mult_by_2(5))  # Вывод: 10

mult_by_3 = make_multiplier(3)
print(mult_by_3(5))  # Вывод: 15


# Замыкание для создания функции приветствия
def make_greeter(greeting):
    def greeter(name):
        return f"{greeting}, {name}!"
    return greeter

hello_greeter = make_greeter("Hello")
print(hello_greeter("Alice"))  # Вывод: Hello, Alice!

hi_greeter = make_greeter("Hi")
print(hi_greeter("Bob"))  # Вывод: Hi, Bob!