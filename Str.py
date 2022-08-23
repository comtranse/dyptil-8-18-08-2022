#Strings
var1 = "Hello"
var2 = 'Hello "World"'
print(var1)
print(var2)

var3 = "My name is 'Yugandhar'"
print(var3)

var4 = "Welcome \nto \"Programming\""           # \"Programming\"   is used for o/p as "Programming"
print(var4)




var5 = " Welcome to Python " 
print(len(var5))    # len is used to determine the length of the string

print(var5.upper())     #.upper() is used to convert to uppercase
print(var5.lower())     #.upper() is used to convert to lowercase
print(var5.strip())     #Return a copy of the string with leading and trailing whitespace removed.
print(var5.count("o"))  #To count occurences of o
print(var5.replace("Python","Java"))

var6 = "World"
print(var6.center(10))
print(var5+var6)

var8 = "Name{}"
var7 = 10
# print(var6+var7) #TypeError: can only concatenate str (not "int") to str
print(var8.format(var7))

var9 = "Demo"
var10 = 82
# print("My name is {} and roll number is {}".format(var9,var10))           # O/p: My name is Demo and roll number is 82
var11 = "My name is {} and roll number is {}"
print(var11.format(var9,var10))




var12 = 14
var13 = 45.32
var14 = 76.32j
print(float(var12))
print(int(var13))
print(float(var14))
print(int(var14))

# Tuple
var15 = (12,14,16,18)
print(var15)
print(var15[2])         # To print number at 2nd index

var16 = ("Yugandhar",10,(78,49),[12,16])        # Can pass tuple and array inside a tuple
print(var16)
print(var16[3])
print(len(var16))
print(var16[-1])
print(var16[1:3])   #prints the value from 1 to (3-1) i.e 2
print(var16[2:])
var20 = list(var16)
var20.append(42)
var20.remove([12,16])
print(var20)  
var20[1] = "Hello"
x = tuple(var20)
print(x)


var17 = ([1,2,3,4],[5,6,7,8])
print(var17[0][0])
print(var17[0][1])
print(var17[0][2])
print(var17[1][0])
print(var17[1][1])

var18 =("YL","YL")
var19 = (("YL ")*4)
print(var18)
print(var19)



a = ("dyp",81,"Yugandhar")
b = ("dyp",82,"Atharv")
(college,rollno,name) = a
(clg,rno,nm) = b
print(college)
print(rollno)
print(name)