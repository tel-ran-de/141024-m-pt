# 1. Отображать список задач
# 2. Добавлять задачи
# 3. Удалять задачи
# 4. Предусмотреть файл настроек приложения
# 5. Сохранять список задач при выходе
# 6. Загружать список задач при старте приложения


class Task:

    def __init__(self, title):
        self.__id = None
        self.__title = title
        self.__description = None
        self.__status = None
        self.__deadline = None

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if isinstance(description, str):
            self.__description = description

    ...


class Manager:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    ...


def main():
    command_list = {
        '1': 'Show tasks',
        '2': 'Add task',
        '3': 'Delete task',
        '4': 'Exit'
    }

    while True:
        ...