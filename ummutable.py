var=" 'Computer' "
print(var)

var1="I am not 'Robot'"
print(var1)

var2="My name is \"Pranav\""
print(var2)

var3="My name is \n \"Pranav\""
print(var3)

var4="My name is \t \"Pranav\""
print(var4)

var5="My name is \b \"Pranav\""
print(var5)

print(len(var))

print(var.upper())

print(var.lower())

print(var.strip)

print(var1.count("o"))

print(var1.replace("am","was"))

var6='e'
print(var6.center(3))

var7=var1+var2
print(var7)

a=5
var8=var+"{}"
print(var8.format(a))

var9="My name is {} and rollno is {}"
print(var9.format(var,a))

print(float(a))

b=5.2
print(int(b))

#c=12.1j
#print(float(c))

var10=("Computer")
print(var10)
print(var10[3])

var11=("Computer",55,(1,2))
print(var11)

var12=([1,2,3],[4,5,6],[7,8,9])
print(var12)
print(var12[0])
print(var12[1])
print(var12[2])
print(var12[0][2],var12[1][1],var12[2][0])

var13=(55,55)
print(var13)
var14=((" Comp ")*2,(2)*2)
print(var14)

c=(15,25)
(fstno,secno)=c
print(c)
print(fstno)
print(secno)
print(len(c))
print(len(var13))
print(len(var12))

d=(15,16,17,18,19)
print(d[-1])
print(d[1:-1])
print(d[2:])

e=list(d)
e[4]="exit"
d=tuple(e)
print(d)
e.append(25)
d=tuple(e)
print(d)
e.remove("exit")
d=tuple(e)
print(d)