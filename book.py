class Publisher:
    def __init__(self):
        print("Parent class")
class Book(Publisher):
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display(self):
        print("The title of the book is", self.title)
        print("The author of the book is", self.author)
class Python(Book):
    def __init__(self, price, pages):
        self.price = price
        self.pages = pages
    def display(self):
        print("Price of the book is", self.price)
        print("Pages of the book is", self.pages)


a = str(input("Enter the title of the book: "))
b = str(input("Enter the author of the book: "))
c = Book(a, b)
c.display()
p = int(input("Enter the price of the book: "))
q = int(input("Enter the pages of the book: "))
c = Python(p, q)
c.display()