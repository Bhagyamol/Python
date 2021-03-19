f = open('C:/Users/HP/Desktop/bhagyaMCA/python/p1.txt', 'r')
f1 = open('C:/Users/HP/Desktop/bhagyaMCA/python/p2.txt', 'w')
content = f.readlines()
for i in range(0, len(content)):
 if(i % 2 != 0):
  f1.write(content[i])
f1 = open("C:/Users/HP/Desktop/bhagyaMCA/python/p2.txt", 'r')
content1 = f1.read()
print(content1)
f.close()
f1.close()
