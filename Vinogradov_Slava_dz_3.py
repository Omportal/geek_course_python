class Worker:
    def __init__(self):
        self.name = None
        self.surname = None
        self.position = None
        self._income = {"wage": 0, "bonus": 0}


class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


neo = Position()
neo.name = "Томас"
neo.surname = "Андерсон"
neo.position = "Избранный"
neo._income = {"wage": 1024, "bonus": 101}
print(neo.get_full_name())
print(neo.position)
print(neo.get_total_income())