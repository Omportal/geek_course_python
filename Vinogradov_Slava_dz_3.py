from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n=5, flag=True):
    """Введите Число,True или False для кол-ва и уникальности шуток"""
    if flag:
        for i in range(n):
            print(choice(nouns), choice(adverbs), choice(adjectives))

    else:
        for i in range(5):
            print(nouns.pop(nouns.index(choice(nouns))),
                  adverbs.pop(adverbs.index(choice(adverbs))),
                  adjectives.pop(adjectives.index(choice(adjectives))))
        print("Уникальные шутки закончились!")


get_jokes(9, False)
