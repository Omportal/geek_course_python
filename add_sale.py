from sys import argv

sale = argv[-1]
name = argv[0]
if not str(sale).isalpha():
    with open("bakery.csv", "a", encoding="utf-8") as f:
        f.write(f'{sale}\n')
        print(f"Сумма: {sale} руб. добавлена")
else:
    print("Неккоретный ввод.Введите сумму выручки")
