for i in range(1, 101):
    if i == 1:
        print(str(i) + " процент")
    if 2 <= i < 5:
        print(str(i) + " процента")
    if i in range(5, 21):
        print(str(i) + " процентов")
    if i in range(21, 100, 10):
        print(str(i) + " процент")
    if i in range(22, 100, 10) or i in range(23, 100, 10) or i in range(24, 100, 10):
        print(str(i) + " процента")
    if i in range(25, 100, 10) or i in range(27, 100, 10) or i in range(29, 100, 10):
        print(str(i) + " процентов")
        print(str(i + 1) + " процентов")
