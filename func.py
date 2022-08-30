# a="Welcome"
# def fun():
#     a="Hello"
#     print(a)
# fun()
# print(a)

# def fun():
#     a=15
#     b=16
#     c=a+b
#     return c
# print(fun())

# def fun():
#     a=10
#     b=20
#     yield a+b
# add = fun()
# for x in add:
#     print(x)


# def fun(a,b):
#     add=a+b
#     # yield add
#     sub=a-b
#     # yield sub
#     mul=a*b
#     # yield mul
#     div=a/b
#     # yield div
#     return add,sub,mul,div
# for x in fun(5,10):
#     print(x)

def square(a):
    result=a ** 2
    return result

def cube(b):
    result= b ** 3
    return result

# ### File Handling
# f=open("D:/Course/Python ES/keywords.txt","r")
# print(f.read())
# f.close()
# f2=open("D:/Course/Python ES/keywords.txt","w")
# f2.write("Hello")
# f2.close()
# f3=open("D:/Course/Python ES/keywords.txt","a")
# f3.write("Hi")