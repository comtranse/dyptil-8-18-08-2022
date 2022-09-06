import camelcase 
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))

import camelcase as cm
c = cm.CamelCase()
t = "welcome"
print(c.hump(t))


#Exception Handling
try:
    k = "hello"
    j = 10
    a = k/j
    print(a)
    
except TypeError as zde:
    print("Error Found: ",zde)    
finally:
    print("Finally block")




class cname:
    n = "al"
    rno = 82
    def func(self):
        print("Inside Function")
    def info(self):
        print("Name",self.n)    
        print("Roll no",self.rno)    
print(cname.n)    
print(cname.rno) 
# cname.func()   
obj = cname()   #object created
obj.func()
obj.info()