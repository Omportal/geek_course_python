class ComplexNum:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real} + {self.imag}j"

    def __add__(self, other):
        return f"{self.real + other.real} + {self.imag + other.imag}j"

    def __mul__(self, other):
        return f"{(self.real * other.real) - (self.imag * other.imag)}" \
               f" + {(self.real * other.imag) + (self.imag * other.real)}j"


a = ComplexNum(2, 4)
b = ComplexNum(3, 5)
print(a)
print(b)
print(a + b)
print(a * b)
