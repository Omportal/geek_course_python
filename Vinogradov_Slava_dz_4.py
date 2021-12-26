class Car:

    def __init__(self, color, name, is_police=False, speed=0):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} поехала"

    def stop(self):
        return f"{self.name} остановилась"

    def turn(self, direction):
        if direction == "направо":
            return f"{self.name} повернула направо"
        if direction == "налево":
            return f"{self.name} повернула налево"
        if self.is_police == True and direction == "разворот":
            return "Полицейский разворот"

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return "Превышение скорости"
        else:
            return self.speed


town_car = TownCar("Grey", "Reno", speed=65)
print(town_car.go())
print(town_car.speed)
print(town_car.show_speed())
print(town_car.turn("налево"))
print(town_car.stop())


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return "Превышение скорости"
        else:
            return self.speed


work_car = WorkCar("Blue", "Mazda")
work_car.speed = 45
print(work_car.go())
print(work_car.speed)
print(work_car.show_speed())
print(work_car.stop())


class PoliceCar(Car):
    pass


cops = PoliceCar("Black", "Ford", is_police=True, speed=90)
print(cops.go())
print(cops.show_speed())
print(cops.turn("разворот"))
print(cops.stop())
