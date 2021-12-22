def type_logger(func):
    def type_wrapper(arg):
        result = func(arg)

        return f"{func.__name__}({arg}: {type(arg)}), result = {result}"

    return type_wrapper


@type_logger
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
