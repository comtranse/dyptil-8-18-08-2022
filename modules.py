
import camelcase as cm
c=cm.CamelCase()
txt="hello world"
print(c.hump(txt))

try:
    k=20
    j='aa'
    a=k/j
    print(a)
except TypeError as z:
    print("ERROR",z)
finally:
    print("DONE")


class demo:
    name="AL"
    rn=12
    def d(self):
        print("Name:",self.name)
    def c(self):
        print("Roll no",self.rn)
print(demo.name)

de=demo()
de.d()
de.c()

