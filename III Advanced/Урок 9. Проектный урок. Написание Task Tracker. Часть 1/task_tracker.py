# 1. Отображать список задач
# 2. Добавлять задачи
# 3. Удалять задачи
# 4. Предусмотреть файл настроек приложения
# 5. Сохранять список задач при выходе
# 6. Загружать список задач при старте приложения


import json
import os


class Task:
    def __init__(self, title):
        self.__id = None
        self.__title = title
        self.__description = None
        self.__status = None
        self.__deadline = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if isinstance(description, str):
            self.__description = description

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def deadline(self):
        return self.__deadline

    @deadline.setter
    def deadline(self, value):
        self.__deadline = value

    def to_dict(self):
        return {
            'id': self.__id,
            'title': self.__title,
            'description': self.__description,
            'status': self.__status,
            'deadline': self.__deadline
        }

    @staticmethod
    def from_dict(data):
        task = Task(data['title'])
        task.id = data['id']
        task.description = data['description']
        task.status = data['status']
        task.deadline = data['deadline']
        return task


class Manager:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def add_task(self, task):
        task.id = self.next_id
        self.tasks[task.id] = task
        self.next_id += 1

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]

    def show_tasks(self):
        for task_id, task in self.tasks.items():
            print(f"ID: {task_id}, Title: {task.title}, Description: {task.description}, Status: {task.status}, Deadline: {task.deadline}")

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            tasks_data = [task.to_dict() for task in self.tasks.values()]
            json.dump(tasks_data, file)

    def load_tasks(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                tasks_data = json.load(file)
                self.tasks = {data['id']: Task.from_dict(data) for data in tasks_data}
                self.next_id = max(self.tasks.keys(), default=0) + 1


def main():
    command_list = {
        '1': 'Show tasks',
        '2': 'Add task',
        '3': 'Delete task',
        '4': 'Exit'
    }

    manager = Manager()
    manager.load_tasks('tasks.json')

    while True:
        print("\nCommands:")
        for key, value in command_list.items():
            print(f"{key}: {value}")

        command = input("Enter command: ")

        match command:
            case '1':
                manager.show_tasks()
            case '2':
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                status = input("Enter task status: ")
                deadline = input("Enter task deadline: ")
                task = Task(title)
                task.description = description
                task.status = status
                task.deadline = deadline
                manager.add_task(task)
            case '3':
                task_id = int(input("Enter task ID to delete: "))
                manager.delete_task(task_id)
            case '4':
                manager.save_tasks('tasks.json')
                print("Exiting...")
                break
            case _:
                print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
