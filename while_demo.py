


j=1
while(j<=20):
    print(j)
    j=j+1

#conditional 
a,b=map(int,input("Enter two number:").split())
if(a>b):
    print(a,"is greater value")
elif (a==b):
    print(b)
else:
    print(b,"is greater value")
#task1
x,y,z=map(int,input("Enter three numbers:").split())
if(x>y and x>z):
    print(x,"is greatest number")
elif(y>x and y>z):
    print(y,"is greatest number")
else:
    print(z,"is greatest number")
#task2
c,d=map(int,input("Enter two numbers:").split())
if(c%2==0 and d%2==0):
    print("Both are even")
elif(c%2==0 and d%2!=0):
    print(c,"is even and",d," is odd") 
else:
    print(d,"is even and",c," is odd")



