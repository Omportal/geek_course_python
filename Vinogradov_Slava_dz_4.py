class Storage:
    def __init__(self):
        pass

    @staticmethod
    def input(self, numbers):
        try:
            if isinstance(numbers, int):
                try:
                    temp = self.amount - numbers
                    if temp >= 0:
                        self.amount = self.amount - numbers
                    else:
                        raise ValueError
                    if self.amount >= 0:
                        if self.name not in bd.keys():
                            self.sklad.append(numbers)
                            bd[self.name] = [self.model, self.coast, f"в магазине: {self.amount}",
                                             f"на складе: {sum(self.sklad)}"]

                        else:
                            self.sklad.append(numbers)
                            bd[self.name] = [self.model, self.coast, f"в магазине: {self.amount}",
                                             f"на складе: {sum(self.sklad)}"]
                    else:

                        raise ValueError
                except ValueError:
                    print("Недостаточно товара для перемещения")
                    print(f"Остаток {self.model} в магазине: {self.amount}")
            else:
                raise ValueError
        except ValueError:
            print("Введите кол-во в формате числа ")

    @staticmethod
    def output(self, numbers):
        try:
            if isinstance(numbers, int):
                try:
                    temp = sum(self.sklad) - numbers
                    if temp >= 0:
                        self.amount = self.amount + numbers
                        self.sklad.append(-numbers)
                    else:
                        raise ValueError
                    if sum(self.sklad) >= 0:
                        if self.name not in bd.keys():

                            bd[self.name] = [self.model, self.coast, f"в магазине: {self.amount}",
                                             f"на складе: {sum(self.sklad)}"]

                        else:
                            bd[self.name] = [self.model, self.coast, f"в магазине: {self.amount}",
                                             f"на складе: {sum(self.sklad)}"]
                    else:

                        raise ValueError
                except ValueError:
                    print("Недостаточно товара для перемещения")
                    print(f"Остаток {self.model} на складе : {sum(self.sklad)}")
            else:
                raise ValueError
        except ValueError:
            print("Введите кол-во в формате числа ")


bd = {}


class OfficeEquip:

    def __init__(self, name, model, coast, amount):
        self.model = model
        self.coast = coast
        self.amount = amount
        self.sklad = []
        self.name = name

    def __str__(self):
        return f"Модель: {self.model}, цена: {self.coast}, " \
               f"в магазине: {self.amount} шт., на cкладе: {sum(self.sklad)} шт. "


class Printer(OfficeEquip):
    def __init__(self, name, model, coast, amount, color=True):
        super().__init__(name, model, coast, amount)
        self.color = color


class Computer(OfficeEquip):
    def __init__(self, name, model, coast, amount, gpu):
        super().__init__(name, model, coast, amount)
        self.gpu = gpu


class Scanner(OfficeEquip):
    def __init__(self, name, model, coast, amount, fax=True, ):
        super().__init__(name, model, coast, amount)
        self.fax = fax


scanner_1 = Scanner("Scanner_1", "LG-1", 10000, 50, fax=True)
scanner_2 = Scanner("Scanner_2", "LG-2", 10000, 50, fax=True)
comp_1 = Computer("Computer", "lenovo", 20000, 100, "Geforce RTX")
printer = Printer("Printer", "Sony", 22500, 25, color=False)
Storage.input(scanner_1,30)
Storage.input(scanner_2,20)
Storage.input(comp_1,40)


print(bd)
Storage.output(scanner_1,20)
print(bd)
print(scanner_1)
