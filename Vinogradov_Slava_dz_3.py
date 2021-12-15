from itertools import zip_longest

with open("users.csv", "r", encoding="utf-8") as f:
    username = f.read().replace(",", " ").split("\n")
with open("hobby.csv", "r", encoding="utf-8") as f:
    hobby = f.read().split("\n")

result = dict(zip_longest(username, hobby, fillvalue='None'))

if len(username) >= len(hobby):
    with open("User_Hobby.csv", "w", encoding="utf-8") as f:
        f.write(str(result))
else:
    exit(1)
