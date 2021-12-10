src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
src_copy = src[1:]
print([src_copy[i] for i in range(len(src) - 1) if src[i] < src_copy[i]])
