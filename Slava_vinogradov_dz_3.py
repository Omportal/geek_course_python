class Cell:

    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return f"{self.arg}"

    def __add__(self, other):
        return f'ячеек после сложения: {Cell(self.arg + other.arg)}'

    def __sub__(self, other):
        result = self.arg - other.arg
        if result > 0:
            return f"ячеек после вычитания {Cell(result)}"
        else:
            return f"Вычитание клеток невозможно"

    def __mul__(self, other):
        result = self.arg * other.arg
        if result > 0:
            return f"ячеек после умножения: {Cell(result)}"
        else:
            return "Умножение на нулевую клетку невозможно"

    def __floordiv__(self, other):
        if other.arg > 0:
            return f"ячеек после деления: {Cell(self.arg // other.arg)}"
        else:
            return "Деление на нулевую клетку невозможно"

    def __truediv__(self, other):
        if other.arg > 0:
            return f"ячейки после округления деления: {Cell(round(self.arg / other.arg))}"
        else:
            return "Деление на нулевую клетку невозможно"

    def make_order(self, num_cell):
        result = ""
        count = 0
        for i in range(self.arg):
            result += "".join("*")
            count += 1
            if count == num_cell:
                result += "".join("\n")
                count = 0
        return f"Ячейки клетки, орагнизованные по рядам:\n{result}"


a = Cell(12)
b = Cell(5)
print(a.make_order(5))
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
