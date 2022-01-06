class IntValidation(ValueError):
    pass


result = []
while True:
    try:
        inp_list = input().lower()
        if not inp_list.isdigit() and inp_list != "stop":
            raise IntValidation("Введите число или stop")
    except IntValidation as e:
        print(e)
    else:
        if inp_list.isdigit():
            result.append(int(inp_list))
        if inp_list == "stop":
            break
print(result)
print(type(result[0]))
