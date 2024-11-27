# Создайте класс ComplexNumber, который будет представлять комплексные числа.
# Перегрузите различные магические методы для выполнения арифметических операций, сравнения и для
# управления атрибутами воспользуйтесь методами установки атрибутов.

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag


    def __str__(self):
        return f"({self.real} + {self.imag}i)"
