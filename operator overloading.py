class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self,other):
        return self.a+other.a, self.b+other.b


o1 = Complex(1, 2)
o2 = Complex(2, 3)
o3 = o1+o2
print(o3)

