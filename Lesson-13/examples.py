# Объявление и вызов функций
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Вывод: Hello, Alice!

# Оператор return
def add(a, b):
    return a + b

result = add(2, 3)
print(result)  # Вывод: 5

# Именованные аргументы
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")  # Вывод: Hello, Alice!
greet("Bob", greeting="Hi")  # Вывод: Hi, Bob!

# Фактические и формальные параметры
def greet(name):  # 'name' - формальный параметр
    print(f"Hello, {name}!")

greet("Alice")  # "Alice" - фактический параметр

# Функции с произвольным числом параметров
def add(*args):
    return sum(args)

print(add(1, 2, 3))  # Вывод: 6

def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Alice", age=30)  # Вывод: name: Alice \n age: 30

# Примеры с *args и **kwargs
def describe_person(name, age, *args, **kwargs):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print("Additional info:", args)
    print("Other details:", kwargs)

describe_person("Alice", 30, "Engineer", "USA", height=170, weight=65)
# Вывод:
# Name: Alice
# Age: 30
# Additional info: ('Engineer', 'USA')
# Other details: {'height': 170, 'weight': 65}

