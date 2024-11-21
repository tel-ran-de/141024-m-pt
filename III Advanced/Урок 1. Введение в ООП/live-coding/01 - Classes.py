class Car:
    wheel = 4

    def __init__(self):
        self.fuel = 100
        self.distance = 200
        print(f'Class car __init__(fuel={self.fuel}, distance={self.distance})')


class Truck(Car):
    def __init__(self, weight):
        super().__init__()  # super() - вызов родительского класса, в данном случае Car, то есть, помимо weight у него есть fuel и distance
        self.weight = weight
        print(f'Class Truck __init__(weight={self.weight})')


class HyperTruck(Truck):
    def __init__(self, weight, wheel):
        super().__init__()  # super() - вызов родительского класса, в данном случае Car, то есть, помимо weight у него есть fuel и distance
        self.wheel = wheel
        print(f'Class Truck __init__(weight={self.weight})')


class LightCar(Car):
    def __init__(self, passengers):
        super().__init__()
        self.passengers = passengers
        print(f'Class Light_car __init__(passengers={self.passengers})')


def main():
    print('Base class "Car"')
    car1 = Car()
    print(car1.wheel)
    print(car1.fuel)
    print(car1.distance)

    print('\nClass "Truck"')
    truck1 = Truck(weight=100)
    print(truck1.wheel)
    print(truck1.fuel)
    print(truck1.distance)
    print(truck1.weight)

    print('\nClass "LightCar"')
    light_car1 = LightCar(passengers=100)
    print(light_car1.wheel)
    print(light_car1.fuel)
    print(light_car1.distance)
    print(light_car1.passengers)

    print('\nClass "LightCar"')
    light_car2 = LightCar(passengers=150)
    print(light_car1.wheel)
    print(light_car1.fuel)
    print(light_car1.distance)
    print(light_car1.passengers)


if __name__ == "__main__":
    main()
