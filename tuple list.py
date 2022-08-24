d=(15,16,17,18,19)
c=(15,25,20)
e=d+c
print(e)
print(e.count(15))
print(e.index(19))

a=(23,15,55j,256,(55,"JJJ"),("fff","Black"))
(b,*z,y)=a
print(b)
print(z)
print(y)

for p in e:
    print(p)
i=0
while i<len(e):
    print(e[i])
    i+=1
for i in range(1,10):
    print(i)
for i in range(1,10,2):
    print(i)

#list
lst=[25,15j,"abc",{256:"abc"},"xyz"]
print(lst)
lst.insert(1,115)
print(lst)
lst.append("mno")
print(lst)
lst[3]="ppp"
print(lst)
lst.remove("ppp")
print(lst)
lst.pop(1)
print(lst)
lst.clear()
print(lst)
del(lst)
print(lst)