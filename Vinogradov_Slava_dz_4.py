def val_cheker(lambda_func):
    def _val_cheker(func):
        def wrapper(arg):
            result = lambda_func(arg)
            if result:
                return func(arg)
            else:
                msg = f"wrong val {arg}"
                raise ValueError(msg)

        return wrapper

    return _val_cheker


@val_cheker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)
a = calc_cube(-5)
print(a)
