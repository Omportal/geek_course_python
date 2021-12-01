lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(lst))
for i in lst[::-1]:
    if i.isdigit():
        lst.insert(lst.index(i), '"')
        lst.insert(lst.index(i) + 1, '"')
        lst.insert(lst.index(i), i.zfill(2))
        lst.remove(i)

    if not i.isalpha() and not i.isdigit():
        lst.insert(lst.index(i), '"')
        lst.insert(lst.index(i) + 1, '"')
        lst.insert(lst.index(i), i.zfill(3))
        lst.remove(i)

print(" ".join(lst))
print(id(lst))
