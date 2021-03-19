f = open("C:/Users/HP/Desktop/bhagyaMCA/python/book.csv", 'a')
import json
thisdict = {
"Fname":"Deepa",
"Lname":"Rose",
"Email":"deepa1819@gmail.com"
}
result = json.dumps(thisdict)
f.write(result)
f.close()
f = open("C:/Users/HP/Desktop/bhagyaMCA/python/book.csv", 'r')
print(f.read())