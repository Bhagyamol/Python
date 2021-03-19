import csv
f = open("C:/Users/HP/Desktop/bhagyaMCA/python/book.csv", 'r')
content = csv.reader(f)
for x in content:
    print(x)


