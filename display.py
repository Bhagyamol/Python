class Student:
    def __init__(self, name, mark1,mark2,branch):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.branch = branch

    def displayStudent(self):
        print("Name : ", self.name, ", Mark1: ", self.mark1,",Mark2:",self.mark2, ",Branch :", self.branch)
    def __del(self):
        print("Deleted")
s1 = Student("Bhagya", 95,85,"MCA")
s2 = Student("Meenu", 100,96,"Bcom")
s1.displayStudent();
s2.displayStudent();
del (s1.mark1)
