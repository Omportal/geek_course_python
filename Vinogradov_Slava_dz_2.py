numbers = [i ** 3 for i in range(1, 1000, 2)]
print(numbers)  # Список всех кубов нечетных чисел в диапозоне от 1 до 1000

result = []

for i in numbers:  # Проход по каждому числу ,создание новой переменной для каждой цифры в числе
    x = i % 10
    i1 = i // 10
    x1 = i1 % 10
    i2 = i1 // 10
    x2 = i2 % 10
    i3 = i2 // 10
    x3 = i3 % 10
    i4 = i3 // 10
    x4 = i4 % 10
    i5 = i4 // 10
    x5 = i5 % 10
    i6 = i5 // 10
    x6 = i6 % 10
    i7 = i6 // 10
    x7 = i7 % 10
    i8 = i7 // 10
    x8 = i8 % 10
    i9 = i8 // 10
    x9 = i9 % 10
    i10 = i9 // 10
    x10 = i10 % 10
    if (x + x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10) % 7 == 0:  # Проверка суммы цифр на деление на 7
        result.append(i)  # Если условие верно,добавляем число в отдельный список

print(result)  # Список кубов сумма цифр в которых делится нацело на  7
print(sum(result))  # Сумма  кубов сумма цифр в которых делится нацело на  7

result_2 = []

for i in result:
    i += 17  # Добавляем к  каждому числу 17
    x = i % 10
    i1 = i // 10
    x1 = i1 % 10
    i2 = i1 // 10
    x2 = i2 % 10
    i3 = i2 // 10
    x3 = i3 % 10
    i4 = i3 // 10
    x4 = i4 % 10
    i5 = i4 // 10
    x5 = i5 % 10
    i6 = i5 // 10
    x6 = i6 % 10
    i7 = i6 // 10
    x7 = i7 % 10
    i8 = i7 // 10
    x8 = i8 % 10
    i9 = i8 // 10
    x9 = i9 % 10
    i10 = i9 // 10
    x10 = i10 % 10
    if (x + x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10) % 7 == 0:  # Проверка суммы цифр на деление на 7
        result_2.append(i)  # Если условие верно,добавляем число в отдельный список

print(result_2) # Таких чисел в новом списке нет, поэтому список пустой
