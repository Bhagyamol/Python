class Rectangle:
    area =0
    perimeter =0
    def __init__(self, length, breadth):
        self.length=length
        self.breadth=breadth
    def calc_area(self):
        self.area=self.length*self.breadth
        print("Area of rectangle1 is:", self.area)
        print("Area of Rectangle2 is", self.area)
    def __lt__(self, second):
        if self.area < second.area:
            return True
        else:
            return False


length1=int(input("Enter the length of the rectangle1:"))
breadth1=int(input("Entr the breath of the rectangle1:"))
length2=int(input("Enter the length of the rectangle2:"))
breadth2=int(input("Enter the breadth of the rectangle2:"))
obj1 = Rectangle(length1, breadth1)
obj2 = Rectangle(length2, breadth2)
obj1.calc_area()
obj2.calc_area()
if obj1 < obj2:
    print("Rectangle2 is large")
else:
    print("Rectangle1 is large or these are equal ")

