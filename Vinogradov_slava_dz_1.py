class Data:
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_int(cls, date):
        result = list(map(int, date.split("-")))
        return result[0], result[1], result[2], type(result[0])

    @staticmethod
    def validate(date):
        result = Data.date_int(date)
        msg = "Введите корректную дату"
        if result[0] not in range(1, 32):
            raise ValueError(msg)
        if result[1] not in range(1, 13):
            raise ValueError(msg)
        if result[2] not in range(1, 2022):
            raise ValueError(msg)


true_date = Data("31-12-1988")
false_date = Data("33-12-1988")

print(true_date.date)
print(Data.date_int(true_date.date))
true_date.validate(true_date.date)
false_date.validate(false_date.date)
