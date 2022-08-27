#while loop
var = 1
while(var<20):
    print(var)
    var = var + 1

#Conditional statement 
print("Enter two numbers")
a = int(input())
b =  int(input())
if(a>b):
    print("{} is greater".format(a))
else:
    print("{} is greater".format(b))    

#Task 7 : print greatest among 3 numbers
print("Enter any three numbers")
num1 = int(input())
num2 = int(input())
num3 = int(input())
if(num1>num2 and num1>num3):
    print("{} is greater".format(num1))
elif(num2>num1 and num2>num3):    
    print("{} is greater".format(num2))
else:
    print("{} is greater".format(num3))   

#Task8
print("Enter two numbers")
n1 = int(input()) 
n2 = int(input()) 
if(n1 % 2 == 0 and n2 % 2 ==0):
    print("Both are even")
elif(n1 % 2 == 0 and n2 % 2 !=0):
    print("{} is even and {} is odd".format(n1,n2))    
elif(n1 % 2 != 0 and n2 % 2 ==0):
     print("{} is odd and {} is even".format(n1,n2)) 
else:
    print("Both are odd")


#Functions
def fun():
    print("Function")

fun()

def fun2(x):
    print("value of x is {}".format(x))

fun2(10)


def op(m,n):
    print("Addition is {}".format(m+n))
    print("Subtraction is {}".format(m-n))
    print("Multiplication is {}".format(m*n))
    print("Division is {}".format(m/n))
print("Operations on two numbers")
op(10,5)
