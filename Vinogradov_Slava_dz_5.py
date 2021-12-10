src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result_list = [i for i in src if src.count(i) == 1]  # решение с помощью List Comprehension
print(result_list)

tmp = set()
result = set()
for i in src:
    if i not in tmp:
        result.add(i)
    else:
        result.discard(i)
    tmp.add(i)
print(result)  # решение циклом и множеством

final_result = [i for i in src if i in result]
print(final_result)  # вывод решения в той же последовательности что и в списке
