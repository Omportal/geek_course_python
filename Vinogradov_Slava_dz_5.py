prices = [99.9, 65.5, 36.6, 3.14, 0.99, 69, 19.03, 15.06, 16.5, 666, 31, 27, 14.88, 0.15]
print(id(prices))

prices.sort()
for i in prices:
    rub = int(i)
    cent = int((i - rub) * 100)
    print(f"{rub} руб {cent:02d} коп", end=", ")
print()

print(id(prices))

max_prices = []
new_price = sorted(prices, reverse=True)
for i in new_price:
    rub = int(i)
    cent = int((i - rub) * 100)
    print(f"{rub} руб {cent:02d} коп", end=", ")
    max_prices.append(f"{rub} руб {cent:02d} коп")
print()
print(', '.join(max_prices[:5]))
