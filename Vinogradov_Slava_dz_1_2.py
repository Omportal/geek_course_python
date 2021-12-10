n = 15


def odd_num(n):
    for i in range(1, n + 1, 2):
        yield i


odd_to_n = odd_num(n)
print(next(odd_to_n), next(odd_to_n), next(odd_to_n))

odd_gen = (i for i in range(1, n + 1, 2))
print(next(odd_gen), next(odd_gen), next(odd_gen))
