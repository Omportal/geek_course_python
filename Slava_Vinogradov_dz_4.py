from itertools import zip_longest

with open("users.csv", "r", encoding="utf-8") as f:
    human = f.read().replace(",", " ").split()
    name = (human[i] for i in range(1, len(human), 3))
    surname = (human[i + 1] for i in range(1, len(human), 3))
    third_name = (human[i - 1] for i in range(1, len(human), 3))
    human_tuple = tuple(zip_longest(name, surname, third_name))
    humans_dict = {"humans": human_tuple}

with open("hobby.csv", "r", encoding="utf-8") as f:
    hobbies = set(f.read().replace("\n", ",").split(","))
    hobbies_dict = {"hobby": hobbies}

with open("User_Hobby_all.csv", "w", encoding="utf-8") as f:
    f.write(f"{hobbies_dict}\n")
    f.write(f"{humans_dict}\n")
