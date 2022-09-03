f1 = open("./file.txt","r")
print(f1.read())

f2 = open("./file.txt","w")
f2.write("Hello")
print(f2.write("Hello"))

f3 = open("./file.txt","a")
f3.write("World")

f1.close()
f2.close()
f3.close()