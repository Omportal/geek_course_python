def thesaurus(*args):
    result = {}
    for name in args:
        key = name[:1]
        if key not in result:
            result[key] = []
        result[key].append(name)
    print(result)


thesaurus("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
