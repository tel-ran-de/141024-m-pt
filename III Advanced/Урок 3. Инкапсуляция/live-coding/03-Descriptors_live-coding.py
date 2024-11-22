class PositiveNumber:
    # вызывается при попытке получить значение атрибута
    # возвращает значение атрибута из словаря __dict__
    # если атрибут не существует, возвращает None
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, None)

    # вызывается при попытке изменить значение атрибута
    # если значение меньше нуля, вызывается исключение ValueError
    # иначе значение атрибута помещается в словарь __dict__
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Value must be non-negative")
        instance.__dict__[self.name] = value

    # вызывается при инициализации атрибута
    # он сохраняет имя атрибута, к которому привязан дескриптор в атрибут self.name
    def __set_name__(self, owner, name):
        print(f"__set_name__ called for {owner.__name__}.{name}")
        self.name = name
        print(f"self.name is set to: {self.name}")


class BankAccount:
    # атрибут является экземпляром класса-дексриптора PositiveNumber
    balance = PositiveNumber()

    def __init__(self, balance):
        self.balance = balance


def main():
    # Использование
    account = BankAccount(100)
    print(account.balance)  # Output: 100

    try:
        account.balance = -50
    except ValueError as e:
        print(e)  # Output: Value must be non-negative


if __name__ == "__main__":
    main()
