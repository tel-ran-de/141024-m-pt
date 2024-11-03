def adder(n):
    def add(x):
        return x + n
    return add


add_five = adder(n=5)
print(add_five(x=10))
print(add_five(x=12))

add_nine = adder(9)
print(add_nine(7))
print(add_nine(27))

print(adder(n=3)(x=2))
