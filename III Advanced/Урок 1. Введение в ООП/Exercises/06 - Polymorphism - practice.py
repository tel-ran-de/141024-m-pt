# Ex 1
# Создайте базовый класс `Appliance` с методом `turn_on`, который должен быть переопределен в
# производных классах `WashingMachine` и `Refrigerator`.
# В каждом из производных классов метод `turn_on` должен выводить сообщение о том, что прибор включен.
# Создайте список различных приборов и продемонстрируйте полиморфизм, вызвав метод `turn_on` для каждого прибора.

from abc import ABC, abstractmethod


# Базовый класс
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass


# Производный класс WashingMachine
class WashingMachine(Appliance):
    def turn_on(self):
        print("Washing machine is now running.")


# Производный класс Refrigerator
class Refrigerator(Appliance):
    def turn_on(self):
        print("Refrigerator is now cooling.")



# Демонстрация полиморфизма
if __name__ == '__main__':
    appliances = [WashingMachine(), Refrigerator()]

    for appliance in appliances:
        appliance.turn_on()  # Вызов метода turn_on для каждого прибора


# #### Задание 2:
# Создайте базовый класс `Employee` с методом `calculate_pay`,
# который должен быть переопределен в производных классах `SalariedEmployee` и `HourlyEmployee`.
# В классе `SalariedEmployee` метод должен рассчитывать ежемесячную зарплату на основе фиксированного оклада,
# а в классе `HourlyEmployee` — на основе количества отработанных часов и почасовой ставки.
# Продемонстрируйте полиморфизм, вызвав метод `calculate_pay` для объектов различных классов.




