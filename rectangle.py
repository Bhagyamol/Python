class Rectangle:
    area = 0
    perimeter = 0

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_area(self):
        self.area = self.length*self.width
        print("Area of rectangle 1 is:", self.area)

    def area1(self):
         self.area = self.length*self.width
         print("Area of Rectangle 2 is", self.area)

    def __lt__(self, second):
        if self.area < second.area:
            return True
        else:
            return False


length1 = int(input("Enter the length of the rectangle 1:"))
width1 = int(input("Enter the width of the rectangle 1:"))
length2 = int(input("Enter the length of the rectangle 2:"))
width2 = int(input("Enter the width of the rectangle 2:"))
obj1 = Rectangle(length1, width1)
obj2 = Rectangle(length2, width2)
obj1.calc_area()
obj2.area1()

if obj1 < obj2:
    print("Rectangle 2 is large")
else:
    print("Rectangle 1 is large ")

