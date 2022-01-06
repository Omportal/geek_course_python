class DivisionError(ZeroDivisionError):
    pass


inp_x = int(input("Введите число которое будем делить: "))
inp_y = int(input("Введите делитель: "))


def division(x, y):
    try:
        if y == 0:
            raise DivisionError("Деление на ноль невозможно")
    except DivisionError as e:
        print(e)
    else:
        return x / y


print(division(inp_x, inp_y))
