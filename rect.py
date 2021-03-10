class Rect:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def peri(self):
        return 2 * (self.length + self.breadth)


a = int(input("Enter the length of the rectangle 1:"))
b = int(input("Enter the breadth of the rectangle 1:"))
s = Rect(a, b)
print("Area of a rectangle 1 is:", s.area())
print("Perimeter of the Rectangle is:", s.peri())
p = int(input("Enter the length of the rectangle 2:"))
q = int(input("Enter the breadth of the rectangle 2:"))
s1 = Rect(p, q)
print("Area of Rectangle 2 is:", s1.area())
print("Perimeter of Rectangle 2 is:", s1.peri())

if s.area() == s1.area():
    print("The 2 Rectangle have equal area")
else:
    print("The 2 Rectangles are not equal")



