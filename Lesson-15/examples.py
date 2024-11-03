def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Вывод: 120


def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

nested = [1, [2, [3, 4], 5], 6]
print(flatten(nested))  # Вывод: [1, 2, 3, 4, 5, 6]
