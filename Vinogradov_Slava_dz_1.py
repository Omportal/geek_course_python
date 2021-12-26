from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = ["красный", "жёлтый", "зелёный"]

    def running(self):
        print("Светофор включен")
        i = 0
        while i != 3:
            print("Красный")
            sleep(7)
            print("Жёлтый")
            sleep(2)
            print("Зелёный")
            sleep(2)
            i += 1
        print("Светофор выключен")


a = TrafficLight()
a.running()
