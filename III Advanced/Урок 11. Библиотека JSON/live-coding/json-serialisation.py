import json


def dict_to_json(python_object):
    return json.dumps(python_object)


def json_to_dict(json_string):
    return json.loads(json_string)


def main():
    # Пример объекта Python
    data = {
        'name': 'John',
        'age': 30,
        'city': 'New York',
        'is_student': True,
        'grades': [90, 80, 85],
        'phd': None,
    }

    # Преобразование объекта Python в строку JSON
    json_string = dict_to_json(data)
    print(json_string)

    python_object = json_to_dict(json_string)
    print(python_object)


if __name__ == '__main__':
    main()
