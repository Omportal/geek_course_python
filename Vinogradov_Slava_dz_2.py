class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, massa=25, th=1):
        s = (self._width * self._length * massa * th) / 1000
        return f"масса асфальта : {s} тонн"


a = Road(20, 5000)
print(a.mass())
print(a.mass(th=5))
