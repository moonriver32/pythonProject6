class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def go(self):
        print(f"машина {self.name} поехала")

    def stop(self):
        print(f"машина {self.name} остановилась")

    def turn_left(self):
        print(f"машина {self.name} повернула налево")

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def show_speed(self):
        print(f"Текущая скорость авто {self.speed}")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()

        if self.speed > 60:
            print("Скорость превышена")
        else:
            print("")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()

        if self.speed > 40:
            print("Скорость превышена")
        else:
            print("")


class PoliceCar(Car):
    pass


car = Car("Lada", 40)
car1 = TownCar("kia", 50)
car2 = WorkCar("Mazda", 50)
car.go()
car.stop()
car.turn_left()

car.show_speed()
car1.show_speed()
car2.show_speed()
