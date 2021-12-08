def currency_rates(args="None"):
    import time
    from requests import get
    from decimal import Decimal

    response = get("http://www.cbr.ru/scripts/XML_daily.asp").text
    result = []
    result_abr = []
    for i in response.split():  # Забираем аббревиатуру валюты
        if i.count("<CharCode>"):
            result.append(i.split())
    for j in str(result).replace("<", " ").replace(">", " ").split():
        if len(j) == 3 and j.isalpha():
            result_abr.append(j)

    value = []
    number = ''
    for i in response.replace("<Value>", " ").replace("</Value>", " ").replace(",", ".").split():
        value.append(i)
    for j in str(value):
        if j.isdigit():
            number += j
        elif j == "." or j == " ":
            number += j
        else:
            continue
    num_val = number.split()
    date = time.strftime("Дата: %Y-%m-%d")
    price_result = []
    for i in num_val:
        if not i.startswith("0"):
            price_result.append((round(Decimal(i), 2)))
    course_val = dict(zip(result_abr, price_result[2:]))
    if args.upper() in course_val:
        print(f"Курс {args.upper()} =", course_val[args.upper()], "руб.", date)
    else:
        print("None")


currency_rates("usd")
currency_rates("EUR")
