numbers = {
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
    "ten": "десять"
}


def num_translate_adv(num):
    if num.lower() in numbers:
        if num == num.title():
            print(numbers[num.lower()].title())
        else:
            print(numbers[num])
    else:
        print("None")


num_translate_adv("One")
num_translate_adv("two")
num_translate_adv("another")
