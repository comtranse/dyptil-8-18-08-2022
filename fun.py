

def func1():
    x = 10
    print(x)

func1()

y = 12
print(y)


city = "World"
def func2():
    city = "Kolhapur"   #Local Variable
    print("Inside func2: ", city)

func2()
print(city)


a = 12
b = 10
def op():
    print("Addition: ", a+b)
    print("Subtraction: ", a-b)
    print("Multiplication: ", a*b)
    print("Division: ", a/b)

op()

def sub(c,d):
    return c-d

print(sub(25,10))

def add(c,d):
    yield c + d

addition = add(35,15)
for x in addition:
    print(x)



def opns(p,q):
    yield p + q
    yield p - q
    yield p * q
    yield p / q
opr = opns(45,15)
for i in opr:
    print(i)