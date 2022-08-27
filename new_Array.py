import array as arr
from operator import index
from pickle import TRUE
a=arr.array('B',[1,2,3,4])
# print(a[1])
# b=arr.array('B'['abc','xyz'])
# print(b[1])
# a[2]=30
# print(a)
b=[2,3,5,4,6,8]
# for x in b:
#     print(x)
#find prime number by using for and while loop
for x in b:
    if x==3:
        break
    print(x)
# for x in b:
#      if x==3:
#         continue
#     print(x)

# while loop
j=1
while (j<=20):
    print(j)
    j=j+1
# amstrong number
i=1
k=2

# while(i<=10):
#     count=0

#     while(k<1):
#         if(i%k)==0:
#             count=count+1
#         i=i+1
#         k=k+1
#     if count==0:
#         print(i)
#     else:
#         count=0
#     # int(input(""))
    
# a=10
# b=20
# if (a<b):
#    print(a,"is greater value")
# elif(a==b):
#     print(b)
# else:
#     print(b,"is greater value")



# c,d=map(int,input("enter two numbers:").split())
# if (c%2==0 and d%2==0):
#     print(c,d,"both numbers are even")
# elif(c%2==0 and d%2!=0):
#     print(c,"is even",d,"is odd")
# else:
#     print(d,"is even",c,"is odd")

def demo(x,y):
    print("the addition is :",x+y)
    print("the substraction is:",x-y)

demo(20,45)

