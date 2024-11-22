class MyClass:
    def __init__(self, value):
        # Используем метод __setattr__ для установки атрибута
        self.__setattr__('value', value)

    # используется для валидации
    def __setattr__(self, name, value):
        print(f"Setting attribute {name} to {value}")
        super().__setattr__(name, value)

    # вызывается для всех атрибутов, независимо от того существуют они или нет
    def __getattribute__(self, name):
        print(f"Getting attribute {name}")
        return super().__getattribute__(name)

    # вызывается только тогда, когда атрибут не найден в классе
    def __getattr__(self, name):
        print(f"Attribute {name} not found, returning default value")
        return "Default Value"

    # используется когда на нужно удалить атрибут
    def __delattr__(self, name):
        print(f"Deleting attribute {name}")
        super().__delattr__(name)


def main():
    print('# Создание объекта')
    obj = MyClass(10)

    print()
    print('# Доступ к существующему атрибуту')
    print(obj.value)  # Output: Getting attribute value\n10

    print()
    print('# Доступ к несуществующему атрибуту')
    print(
        obj.non_existent_attr)  # Output: Getting attribute non_existent_attr
    # Attribute non_existent_attr not found, returning default value\nDefault Value

    print()
    print('# Установка атрибута')
    obj.value = 20  # Output: Setting attribute value to 20

    print()
    print('# Удаление атрибута')
    del obj.value  # Output: Deleting attribute value

    print()
    print('# Попытка доступа к удаленному атрибуту')
    print(
        obj.value)  # Output: Getting attribute value\nAttribute value not found, returning default value\nDefault Value


if __name__ == '__main__':
    main()
