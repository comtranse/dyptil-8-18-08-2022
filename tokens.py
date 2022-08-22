#Arithmetic Operator
a = 5 
b = 7
print(a+b)
print(6+8)
print(7*8)

#Assignment Operator
x = 10
print(x)
x += 12
print(x)

y = 15
print(y)
y -=10
print(y)

z = 20
print(z)
z *= 10
print(z)

#Bitwise Operator   
a = 10
b = 4
print('a&b', a&b)

w = 10
d = -5
print("w>>1 = ", w>>1) # Right Shift
print("w>>2 = ", w>>2) # Right Shift


#Comparison Operator
v = 5
print(v == 5)
print(v == 4)
print(v != 3)
print(v >= 5)
print(v >= 6)



#Logical Operator
j = 8
k = 5
print("j and k = ", j==8 and k>=6)
print("j and k = ", j==8 or k>=10)
print("not j = ", not j == 7)


#Identity Operator
id(45)
print(id)       #O/P : <built-in function id>
print(id(45))   # It prints address
print(id("Hello"))  # It prints address

print(1 is 1)   #O/p : True
print(1 is 2)   #O/p : False
print(1 is not 5)   #O/p : True

# Membership Operator :- in, not in 
print(1 in 1) #Error statement

arr = [3,4,5,6]
print(arr)
print(5 in arr)     #True
print(8 in arr)     #False
print(7 not in arr) #True


#Identifiers
A = 10 
a = 5
print(A)
print(a)

#Literals
#String Literal
str = "Name"
print(str)
str2 = '''abc
def
ghi
jkl'''
print(str2)    

# Numerical Literal
num = 19
print(num)
f = 4.5
print(f)

# Complex Literal
z = 78j
print(z)

# Boolean Literal
passwd = 12345
print(passwd == 12345)
print(passwd == 6755)


#Task-1: Find between two numbers which is greater 
a = 5
b = 4 
print(a > b)
print(b > a)
if(a>b):
 print("a is greater")
else:
 print("b is greater")