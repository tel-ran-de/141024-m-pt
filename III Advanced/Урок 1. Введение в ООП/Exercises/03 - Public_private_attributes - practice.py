# Ex 1
# Создайте класс `BankAccount` с публичным атрибутом `owner` и приватным атрибутом `__balance`.
# Реализуйте методы для внесения депозита и снятия денег, обеспечивая корректность операций
# (например, нельзя снять больше, чем есть на балансе).
#
# Ex 2
# Создайте класс `Product` с публичным атрибутом `name` и приватным атрибутом `__price`.
# Реализуйте методы для получения и изменения цены,
# добавив проверки на корректность (цена не может быть отрицательной).


class BankAccount:
    """
    Class BankAccount
    attributes:
        owner: string (public attribute)
        __balance: float (private attribute)
    """
    def __init__(self, owner, initial_balance=0.0):
        self.owner = owner
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew {amount}. New balance: {self.__balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.__balance


def main():
    # Создание объектов и выполнение операций
    account_alice = BankAccount("Alice", 1000.0)
    account_alice .deposit(500.0)  # Output: Deposited 500.0. New balance: 1500.0
    account_alice .withdraw(200.0)  # Output: Withdrew 200.0. New balance: 1300.0
    account_alice .withdraw(2000.0)  # Output: Insufficient funds.
    print(f"Final balance: {account_alice .get_balance()}")  # Output: Final balance: 1300.0

    # product = Product("Laptop", 999.99)
    # print(f"Product price: {product.get_price()}")  # Output: Product price: 999.99
    # product.set_price(899.99)  # Output: Price updated to 899.99.
    # product.set_price(-100.0)  # Output: Price cannot be negative.


if __name__ == '__main__':
    main()
