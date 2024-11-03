import time

# Обычный цикл for
start_time = time.time()
result_for = []
for i in range(100000000):
    result_for.append(i * 2)
end_time = time.time()
print(f"Обычный цикл for: {end_time - start_time} секунд")

# List comprehension
start_time = time.time()
result_comprehension = [i * 2 for i in range(100000000)]
end_time = time.time()
print(f"List comprehension: {end_time - start_time} секунд")
