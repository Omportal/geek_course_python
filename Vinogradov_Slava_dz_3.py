from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Слава', 'Катя', 'Миша'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def tutor():
    for i in tutors:
        yield i


def klass():
    for i in klasses:
        yield i


result = zip_longest(tutor(), klass())  # Решение через функции и yield
print(next(result), next(result), next(result), next(result), next(result), next(result))

print("*" * 10 ** 2)  # Просто разделитель

result = zip_longest((tutor for tutor in tutors), (klass for klass in klasses))  # Решение через генераторы

for i in range(len(tutors)):
    print(next(result))

print(next(result))  # Вызываем истощение генератора
