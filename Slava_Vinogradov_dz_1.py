class Matrix:
    def __init__(self, args):
        self.args = args

    def __str__(self):
        return '\n'.join(str(i) for i in self.args)

    def __add__(self, other):
        temp = []
        for i in range(len(self.args)):
            temp.append(list(map(lambda x, y: x + y, self.args[i], other.args[i])))
        return Matrix(temp)


s = Matrix([[2, 3, 2, 3], [3, 3, 5, 3], [1, 2, 3, 4]])
a = Matrix([[2, 3, 2, 3], [3, 3, 5, 3], [1, 2, 3, 4]])
print(s)
print("*" * 15)
print(a + s)
