from sys import argv

if len(argv) == 1:
    with open("bakery.csv", "r", encoding="utf-8") as f:
        print(f.read())

if len(argv) == 2:
    with open("bakery.csv", "r", encoding="utf-8") as f:
        arg = int(argv[1])
        rea = f.read().split()
        print('\n'.join(rea[arg - 1:]))

if len(argv) == 3:
    with open("bakery.csv", "r", encoding="utf-8") as f:
        arg = int(argv[1])
        arg_2 = int(argv[2])
        rea = f.read().split()
        print('\n'.join(rea[arg - 1:arg_2]))
