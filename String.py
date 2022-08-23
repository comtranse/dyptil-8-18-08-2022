var1="'HII'"
print(var1)

var2='"HII"'
print(var2)

var3="My \bname is \tAtharv"
print(var3)

var4=" My name is Atharv{}"
print(len(var4))
print(var4.upper())
print(var4.lower())
print(var4.strip())
print(var4.count("A"))
print(var4.replace("My","MY"))

var5="AL{}"
print(var5.center(10))
print(var4+var5)
var6=10

print(var5.format(var6))
print(var4.format(var6))

var7="Atharv"
var8=10
print("My name is {} and roll no is {}".format(var7,var8))

num1=10
print(float(num1))

num2=10.3
print(int(num2))



tup=(10,12,23,"AL",(1,2),[12,22])
print(tup)
print(tup[2])
tup2=([1,2,3],[4,5,6])
print(tup2[1][1])

str=("AL", "AL")
print(5*str)
str2=(("AL ")*4)
print(str2)


a=(1,2,3,4)
(r1,r2,r3,r4)=a
print(r1)
print(len(tup))

print(tup[-4])
print(tup[1:3])
print(tup[:3])
li=(list(tup))
li.append(200)
print(li)
li.remove(200)
print(li)

