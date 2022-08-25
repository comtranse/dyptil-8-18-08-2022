from operator import index
from unicodedata import name


var='"hi"'
print(var)

var="'xyz'"
print(var)

var='my name is "soham"'
print(var)

var="my name is \'soham\'"
print(var)

var="my name\n is  \t \"soham\""
print(var)

var=" my name\n is  \b \"soham\" "
print(var)
print(len(var))
print(var.upper())
print(var.lower())
print(var.strip)
print(var.count("m"))
print(var.replace("my","I"))

var1= "Soham"
print(var.center(10))
var2="d"
var3= var1+ var2
print(var3)
var4=20
var5=var2+"{}"
#print(var5)
print(var5.format(var4))

a=1.0j
b="xyz"
var6="My name is {} and my roll no is {}"
print(var6.format(b,a))
print(float(var4))
#print(int(a))
#print(float(a))

var7=(30,35,40,"xyz","abc",("pqr","40",45))
print(var7[2])
print(var7)

c=([1,2,3],[4,5,6],[7,8,9])
print(c)
print(c[1])
print(c[2])
print(c[0][0])
print(c[0][0],c[1][0],c[1][2])

d=(55,50,55)
print(d)
e=((d)*2)
print(e)
f=("comp" *2)
print(f)

g=(12,13,14,15,16)
(clgname,rollno,add,coloney,phoneno)=g
print(clgname)
print(rollno)
print(len(d))

h=(20,25,30,35,40)
print(h[-1])
print(h[1:-1])

x=('Soham',1.4,22,['g',8,12],(12,2,1,90))
#print(x)

li=list(x)
li[1]="ttt"
x=tuple(li)
print(x)
li.append(30)
x=tuple(li)
print(x)
li.remove(22)
x=tuple(li)
print(x)
z=x+h
print(z)
print(x.count(1.4))
print(x.index)
#(*a,b,c)=x
(a,*b,c)=x
print(a)
print(b)
print(c)
for p in x:
    print(p)
i=0
while i<len(x):
    print(x[i])
    i=i+1
for i in range(1,10,2):
    print(i)
for i in range(1,50,3):
    print(i)
   

