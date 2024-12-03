# Создайте класс Student, который имеет поля имени, возраста и курса.
# Напишите код сохранения и загрузки объектов данного класса в/из объектов JSON

import json


class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'course': self.course
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data['name'],
            age=data['age'],
            course=data['course']
        )


def save_students_to_json(students, filename):
    with open(filename, 'w') as file:
        json.dump([student.to_dict() for student in students], file, indent=4)


def load_students_from_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        return [Student.from_dict(student_data) for student_data in data]


def main():
    # Создаем несколько объектов Student
    students = [
        Student("Alice", 20, "Computer Science"),
        Student("Bob", 22, "Mathematics"),
        Student("Charlie", 21, "Physics")
    ]

    # Сохраняем объекты в JSON файл
    save_students_to_json(students, 'students.json')

    # Загружаем объекты из JSON файла
    loaded_students = load_students_from_json('students.json')

    # Выводим загруженные объекты
    for student in loaded_students:
        print(f"Name: {student.name}, Age: {student.age}, Course: {student.course}")


if __name__ == '__main__':
    main()
