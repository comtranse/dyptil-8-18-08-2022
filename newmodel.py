# import camelcase
# c = camelcase.CamelCase()
# txt="hello windos"
# print(c.hump(txt))

# import camelcase as cm
# c= cm.CamelCase()
# t="welcome"
# print(c.hump(t))

#excetion Handling
# try:
#     k=20
#     j="xyz"
#     a=k/j
#     print(a)
# except TypeError as zde:
#     print("TypeError found",zde)
# finally:
#     print("finally block ")

class abc:
    n="PP"
    rno=80
    def func(self):
        print("fucntion")
    def info(self):
        print("name",self.n)
        print("roll no ",self.rno)
print(abc.n)
print(abc.rno)



obj=abc()
obj.func()
obj.info()