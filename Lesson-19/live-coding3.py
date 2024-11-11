# работа с JSON

import json

data = {
    'name': 'John',
    'age': 30,
    'city': 'New York',
    'is_student': True
}

# запись в файл
with open('text_files/data.json', 'w') as file:
    json.dump(data, file)

with open('text_files/data.json', 'w') as file:
    json.dump(data, file, indent=4)


# Чтение из файла
with open("text_files/data_for_read.json", "r") as file:
    data_alice = json.load(file)

print(data_alice)

with open("text_files/students.json", "r") as file:
    data = json.load(file)

print(data)

# создание json-строки из объекта Python
json_string = json.dumps(data)
print(json_string)

# преобразование строки JSON в объект Python
data = json.loads(json_string)
print(data)
