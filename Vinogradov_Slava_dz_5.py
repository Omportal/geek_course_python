class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Рисуем ручкой")


pen = Pen("ручка")
pen.draw()


class Pencil(Stationery):
    def draw(self):
        print("Рисуем карандашом")


pencil = Pencil("карандаш")
pencil.draw()


class Handle(Stationery):
    def draw(self):
        print("Рисуем маркером")


handle = Handle("маркер")
handle.draw()
